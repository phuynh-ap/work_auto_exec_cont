# autocont_exec.py
#
#   Main auto contingency script. Execute this to perform power flow contingency
#   runs.
#
#   Instructions:
#   - Runs in command prompt, outside the PSS/e GUI.
#   - This script dumps the output in the .\out\ directory.
#
#   Dependencies:
#   - Basecases to run against are in the "autocont_runlist_basecase.py" list.
#   - Contingencies to run are in the "autocont_runlist_contingency.py" list.
#   - Contingency definitions are in the "autocont_defs_contingency.py" list.
#   - PSS/e .sav files must be inside the start directory.
#
#   Outputs:
#   session_[yymmdd_hhmmss].csv
#
#   With the schema:
#   - basecase
#   - rate
#   - contingency
#   - status (solved, iteration limit, blowup)
#   - voltage violation
#   -   bus number
#   -   bus name
#   -   base kV
#   -   area
#   -   voltage (pu)
#   -   voltage (kV)
#   - branch violation
#   -   bus from number
#   -   from name
#   -   from area
#   -   from kV
#   -   bus to number
#   -   to name
#   -   to area
#   -   to kV
#   -   branch ID
#   -   loading (MVA)
#   -   rate limit (MVA)
#   -   rate limit (%)
#   - branch 2-wdg transformer violation
#   -   bus from number
#   -   from name
#   -   from area
#   -   from kV
#   -   bus to number
#   -   to name
#   -   to area
#   -   to kV
#   -   branch ID
#   -   loading (MVA)
#   -   rate limit (MVA)
#   -   rate limit (%)
#
#   Syntax:
#   python autocont_exec.py
#
#   example:
#   python scripts\autocont_exec.py
#
#   2023/01/31  PVH
#   Added solved() to end of fdns to reflect blownup or other solved status.
#
#
#   2022/02/18  PVH
#   Added current expressed as MVA for transformers.
#
#   2020/12/06  PVH
#   Initial release
#

# ---- Start of imports -------------------------------------------------------
# System imports start here
import os, glob, socket, sys                                                    # OS calls
import fileinput                                                                # File handling
import pdb                                                                      # Python debugging library
import logging                                                                  # Python logging
import re                                                                       # RegEx
import math                                                                     # Math functions
import numpy                                                                    # numpy
import winsound                                                                 # For making beeps

# Timekeeping
from datetime import datetime
import time

# ---- Initialize program settings for PSSE run outside of GUI ----------------
# Hostnames
nameSrv         = "EMAPSSE02"                               # PSS/e server name
nameWstn        = "EMA171275L"                              # Workstation name

# Install paths
locPsse34Def    = "C:\Program Files (x86)\PTI\PSSE34\PSSBIN"
locPsse348Wksn = "C:\Program Files (x86)\dev\psse34r8\PSSBIN"
nameHost = socket.gethostname()

# Add  PSSEBIN dir, if it's the server, use the server path
if nameHost == nameWstn:
    PSSE_LOCATION = locPsse348Wksn
    # Include Peter's tools path
    sys.path.append('c:/work/resources/planning/psse/psse_api')
else:
    PSSE_LOCATION = locPsse34Def
    # Include Peter's tools path
    sys.path.append('h:/work/resources/planning/psse/psse_api')

sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION

# ---- Resuming imports -------------------------------------------------------
import psse34
import psspy
import redirect

redirect.psse2py()
psspy.throwPsseExceptions = True

# Include Peter's custom tools
import ierrRef
import pvhTools

# Case-specific
import autocont_runlist_basecase                                                # Basecase runlist
import autocont_runlist_contingency                                             # Contingency runlist
import autocont_defs_contingency                                                # Contingency defs


# ---- Start of global definitions --------------------------------------------
name_study      = "IR602: Lewis Mountain"                                       # Study name

strPathOut  = "out\\"

# Voltage and branch limits
vLimLo  = 0.90                                                                  # Low voltage limit (PU)
vLimHi  = 1.10                                                                  # High voltage limit (PU)
brnLim  = 110                                                                   # Branch loading limit in 100's of percents (90 = 90% for example)

# Output csv header columns
csvHeaders = [  ["base",    "basecase"],
                ["base",    "rate"],
                ["base",    "contingency"],
                ["base",    "status"],
                ["vv",      "vv bus number"],
                ["vv",      "vv bus name"],
                ["vv",      "vv base kV"],
                ["vv",      "vv area"],
                ["vv",      "vv voltage (pu)"],
                ["vv",      "vv voltage (kV)"],
                ["bv",      "bv from number"],
                ["bv",      "bv from name"],
                ["bv",      "bv from area"],
                ["bv",      "bv from kV"],
                ["bv",      "bv to number"],
                ["bv",      "bv to name"],
                ["bv",      "bv to area"],
                ["bv",      "bv to kV"],
                ["bv",      "bv ckt number"],
                ["bv",      "bv loading (MVA)"],
                ["bv",      "bv rate limit (MVA)"],
                ["bv",      "bv rate limit (%)"],
                ["tv",      "tv from number"],
                ["tv",      "tv from name"],
                ["tv",      "tv from area"],
                ["tv",      "tv from kV"],
                ["tv",      "tv to number"],
                ["tv",      "tv to name"],
                ["tv",      "tv to area"],
                ["tv",      "tv to kV"],
                ["tv",      "tv ckt number"],
                ["tv",      "tv loading (MVA)"],
                ["tv",      "tv rate limit (MVA)"],
                ["tv",      "tv rate limit (%)"]
                ]

csvDelim    = "\t"                                                                  # Delimiter character for output csv
csvNa       = "0"                                                                   # Delimiter charactor for n/a

# Beep vars
frequency       = 1500
duration        = 250

# PSS\e placeholders
_i  = psspy.getdefaultint()
_f  = psspy.getdefaultreal()
_s  = psspy.getdefaultchar()
# ---- End of   global definitions --------------------------------------------

# ---- Start of ml_runback()---------------------------------------------------
# Maritime Link runback function
def ml_runback(tot_amt = 150):
    ibus_wbn_p1 = 199855
    ibus_wbn_p2 = 199857
    ibus_bbk_p1 = 195203
    ibus_bbk_p2 = 195204
    
    # Get current ML output (Wbn)
    iErr, pow_WbnP1  = psspy.macdat(ibus    = ibus_wbn_p1,
                                    id      = "1",
                                    string  = "P"
                                    )
    iErr, pow_WbnP2  = psspy.macdat(ibus    = ibus_wbn_p2,
                                    id      = "1",
                                    string  = "P"
                                    )

    # Calculate new power order
    nuPow_WbnP1 = pow_WbnP1 - (tot_amt / 2)
    nuPow_WbnP2 = pow_WbnP2 - (tot_amt / 2)
    
    # Enter new power order
    iErr    = psspy.machine_data_2( i = ibus_wbn_p1,
                                    id = "1",
                                    realar1 = nuPow_WbnP1
                                    )
    iErr    = psspy.machine_data_2( i = ibus_wbn_p2,
                                    id = "1",
                                    realar1 = nuPow_WbnP2
                                    )
                                    
    # Get current ML output (Bbk)
    iErr, pow_BbkP1  = psspy.macdat(ibus    = ibus_bbk_p1,
                                    id      = "1",
                                    string  = "P"
                                    )
    iErr, pow_BbkP2  = psspy.macdat(ibus    = ibus_bbk_p2,
                                    id      = "1",
                                    string  = "P"
                                    )

    # Calculate new power order
    nuPow_BbkP1 = pow_BbkP1 - (tot_amt / 2)
    nuPow_BbkP2 = pow_BbkP2 - (tot_amt / 2)
    
    # Enter new power order
    iErr    = psspy.machine_data_2( i = ibus_bbk_p1,
                                    id = "1",
                                    realar1 = nuPow_BbkP1
                                    )
    iErr    = psspy.machine_data_2( i = ibus_bbk_p2,
                                    id = "1",
                                    realar1 = nuPow_BbkP2
                                    )
# ---- End of   ml_runback() --------------------------------------------------

# ---- Start of sps() ---------------------------------------------------------
def sps(sps_group): # sps() is used in the contingency instructions to runback ML or trip units based on SPS activated. Targeted unit is based on what's online and MW output.
    # Check MW loading of Maritime Link
    ierr, P_ML_1 = psspy.macdat(199855, '1', 'P')
    if (ierr == 3) or (ierr == 4): P_ML_1 = 0
    ierr, P_ML_2 = psspy.macdat(199857, '1', 'P')
    if (ierr == 3) or (ierr == 4): P_ML_2 = 0
    # If Maritime Link is greater than 165 MW, target ML runback for SPS action
    if (P_ML_1 + P_ML_2 >= 165.0) and ((sps_group == 'G5') or (sps_group == 'NSX1') or (sps_group == 'G3')):
        psspy.machine_data_2(199855, r"""1""", realar1=(P_ML_1-(165.0/2)))
        psspy.machine_data_2(199857, r"""1""", realar1=(P_ML_2-(165.0/2)))
        psspy.machine_data_2(195203, r"""1""", realar1=(-1/0.95)*(P_ML_1-(165.0/2)))
        psspy.machine_data_2(195204, r"""1""", realar1=(-1/0.95)*(P_ML_2-(165.0/2)))
        # print 'ML runback 165'
        return 0
    elif (P_ML_1 + P_ML_2 >= 330.0) and ((sps_group == 'G6') or (sps_group == 'NSX2')):
        psspy.machine_data_2(199855, r"""1""", realar1=(P_ML_1-(330.0/2)))
        psspy.machine_data_2(199857, r"""1""", realar1=(P_ML_2-(330.0/2)))
        psspy.machine_data_2(195203, r"""1""", realar1=(-1/0.95)*(P_ML_1-(330.0/2)))
        psspy.machine_data_2(195204, r"""1""", realar1=(-1/0.95)*(P_ML_2-(330.0/2)))
        # print 'ML runback 330'
        return 0
    # Check MW loading of SPS target generators
    ierr, P_88S_1 = psspy.macdat(199001, '1', 'P')
    if (ierr == 3) or (ierr == 4): P_88S_1 = 0
    ierr, P_88S_2 = psspy.macdat(199002, '2', 'P')
    if (ierr == 3) or (ierr == 4): P_88S_2 = 0
    ierr, P_88S_3 = psspy.macdat(199003, '3', 'P')
    if (ierr == 3) or (ierr == 4): P_88S_3 = 0
    ierr, P_88S_4 = psspy.macdat(199004, '4', 'P')
    if (ierr == 3) or (ierr == 4): P_88S_4 = 0
    ierr, P_89S_1 = psspy.macdat(199043, '1', 'P')
    if (ierr == 3) or (ierr == 4): P_89S_1 = 0
    sps_gens_a = numpy.array([(P_88S_1, 199001), (P_88S_2, 199002), (P_88S_3, 199003), (P_88S_4, 199004), (P_89S_1, 199043)], dtype=[('mw', float), ('busnum', int)])
    sps_gens_b = numpy.array([(P_88S_1, 199001), (P_88S_2, 199002), (P_88S_3, 199003), (P_88S_4, 199004)], dtype=[('mw', float), ('busnum', int)])
    # Sort generators by MW output (min to max)
    sorted_sps_gens_a = numpy.sort(sps_gens_a, order = 'mw')
    sorted_sps_gens_b = numpy.sort(sps_gens_b, order = 'mw')    # Does not include Point Aconi
    # Trip generators based on the SPS group armed - Group 3 cannot trip PA
    if (sps_group == 'G5') or (sps_group == 'NSX1'):
        psspy.dscn(sorted_sps_gens_a[-1][1])
    elif (sps_group == 'G6') or (sps_group == 'NSX2'):
        psspy.dscn(sorted_sps_gens_a[-1][1])
        psspy.dscn(sorted_sps_gens_a[-2][1])
    elif (sps_group == 'G3'):
        psspy.dscn(sorted_sps_gens_b[-1][1])
    return 0
# ---- End of   sps() ---------------------------------------------------------

# ---- Start of no_island() ---------------------------------------------------
def no_island():
    iErr, buses = psspy.tree(   apiopt  = 1,    # Init and check for swingless island
                                option  = 0     # Leave this island alone and check for another
                                )
    while(buses > 0):
        iErr, buses = psspy.tree(   apiopt  = 2,    # Process previously detected island then check for another
                                    option  = 1     # Disconnect and check for another swingless island
                                    )
# ---- End of   no_island() ---------------------------------------------------


# ---- Start of wrtBaseSchema() -----------------------------------------------
def wrtBaseSchema(fCsv = 0, baseCaseData = {"case":"","cont":"","rate":"","status":""}):
    fCsv.write(baseCaseData["case"] + csvDelim)
    fCsv.write(str(baseCaseData["rate"]) + csvDelim)
    fCsv.write(baseCaseData["cont"] + csvDelim)
    fCsv.write(str(baseCaseData["status"]) + csvDelim)

# ---- End of   wrtBaseSchema() -----------------------------------------------

# ---- Start of wrtBlanks()----------------------------------------------------
# Writes blanks for specified data class
#
# dataClass is based on the first column in the csvHeaders list def  (base, vv, bv).
#
def wrtBlanks(fCsv = 0, dataClass = ""):
    for index, indCol in enumerate(csvHeaders):
        if(indCol[0] == dataClass):
            fCsv.write(csvNa)
        
            if(index < (len(csvHeaders) - 1)):
                fCsv.write(csvDelim)
# ---- End of   wrtBlanks() ---------------------------------------------------

# ---- Start of chkVoltViol()--------------------------------------------------
def chkVoltViol(mySid = 0, vLo = vLimLo, vHi = vLimHi, appLog = 0, fCsv = 0, baseCaseData = {"case":"","cont":"","rate":"","status":""}):
    # Get bus data
    # Start getting bus data, each variable type gets the following treatment:
    #   - Generate list of keys.
    #   - Use key list to generate PSS/e query string
    #   - Get the PSS/e data.
    #   - Dump the PSS/e data back into a dictionary for that class.
    
    bDebug  = 0
    fInServ = 2
    ctrErr  = 0


    # Get char
    strQuery    = []
    keys        = [ "Name"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABusChar[key])
    iErr, datChar   = psspy.abuschar(   sid     = mySid,
                                        flag    = fInServ,
                                        string  = strQuery
                                        )
    dictChar    = dict(zip(keys, datChar))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkVoltViol():\t datChar iErr [" + str(iErr) + "]")
        print(datChar)

    # Get count
    iErr, datCount   = psspy.abuscount( sid     = mySid,
                                        flag    = fInServ
                                        )
    ctrErr = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkVoltViol():\t datCount iErr [" + str(iErr) + "]")
        print(datCount)

    # Get cplx
    strQuery    = []
    keys        = [ "Voltage"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABusCplx[key])
    iErr, datCplx   = psspy.abuscplx(   sid     = mySid,
                                        flag    = fInServ,
                                        string  = strQuery
                                        )
    dictCplx    = dict(zip(keys, datCplx))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkVoltViol():\t datCplx iErr [" + str(iErr) + "]")
        print(datCplx)

    # Get int
    strQuery    = []
    keys        = [ "Number",
                    "Type",
                    "Area",
                    "Zone"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABusInt[key])
    iErr, datInt    = psspy.abusint(    sid     = mySid,
                                        flag    = fInServ,
                                        string  = strQuery
                                        )
    dictInt     = dict(zip(keys, datInt))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkVoltViol():\t datInt iErr [" + str(iErr) + "]")
        print(datInt)

    # Get real
    strQuery    = []
    keys        = [ "Base",
                    "PU",
                    "KV",
                    "AngleD"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABusReal[key])
    iErr, datReal   = psspy.abusreal(   sid     = mySid,
                                        flag    = fInServ,
                                        string  = strQuery
                                        )
    dictReal    = dict(zip(keys, datReal))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkVoltViol():\t datReal iErr [" + str(iErr) + "]")
        print(datReal)
    
    # Combine all dictioanries into a larger one for easier iterating
    dictAll = { "char"  : dictChar,
                "cplx"  : dictCplx,
                "int"   : dictInt,
                "real"  : dictReal
                }


    # Now check for high voltages
    ctrDict         = 0
    ctrViolations   = 0
    
    while(ctrDict < datCount):
        # Write data if we have a voltage violation
        if( (dictAll["real"]["PU"][ctrDict] <= vLo) or (dictAll["real"]["PU"][ctrDict] >= vHi) ):
#            strWrite = "Voltage violation: " + str(dictAll["int"]["Number"][ctrDict]) \
#                        + ", " + dictAll["char"]["Name"][ctrDict] \
#                        + ": " + str(dictAll["real"]["PU"][ctrDict])
#            print(strWrite)
            # Write csv header data
            wrtBaseSchema(fCsv = fCsv, baseCaseData = baseCaseData)

            # Write voltage violation data
            fCsv.write(str(dictAll["int"]["Number"][ctrDict]) + csvDelim)
            fCsv.write(dictAll["char"]["Name"][ctrDict] + csvDelim)
            fCsv.write(str(dictAll["real"]["Base"][ctrDict]) + csvDelim)
            fCsv.write(str(dictAll["int"]["Area"][ctrDict]) + csvDelim)
            fCsv.write(str(dictAll["real"]["PU"][ctrDict]) + csvDelim)
            fCsv.write(str(dictAll["real"]["KV"][ctrDict]) + csvDelim)
            
            # Write branch violation blanks
            wrtBlanks(fCsv = fCsv, dataClass = "bv")
            
            # Write branch transformer violation blanks
            wrtBlanks(fCsv = fCsv, dataClass = "tv")
            fCsv.write("\n")
            
            # Increment violation counter
            ctrViolations = ctrViolations + 1


        ctrDict = ctrDict + 1

    return ctrViolations
# ---- End of   chkVoltViol()--------------------------------------------------

# ---- Start of chkBrchViol()--------------------------------------------------
def chkBrchViol(mySid = 0, brnchLim = brnLim, brnType = "bv", appLog = 0, fCsv = 0, baseCaseData = {"case":"","cont":"","rate":"","status":""}):
    # Get branch data
    # Start getting branch data, each variable type gets the following treatment:
    #   - Generate list of keys.
    #   - Use key list to generate PSS/e query string
    #   - Get the PSS/e data.
    #   - Dump the PSS/e data back into a dictionary for that class.
    
    bDebug  = 0
    fTies   = 3                                                                 # In-system and tie branches
    fEntry  = 1                                                                 # Single direction

    ctrErr  = 0
    
    # Dynamic rate set string placeholders (initialized to null for failsafe)
    strMaxPctLoading    = ""
    strMVALim           = ""
    
    # Set type flag depending on brnType argument "bv" or "tv".
    if(brnType == "bv"):
        fType = 1                                                               # All in-service branches
    else:
        fType = 5                                                               # All in-service two-wdg transfromers

    # Set rating sets
    if(baseCaseData["rate"] == 1):
        strMaxPctLoading    = "MaxPctRateA"
        strMVALim           = "RateA"
    elif(baseCaseData["rate"] == 2):
        strMaxPctLoading    = "MaxPctRateB"
        strMVALim           = "RateB"
    elif(baseCaseData["rate"] == 3):
        strMaxPctLoading    = "MaxPctRateC"
        strMVALim           = "RateC"
   
    # Get char
    strQuery    = []
    keys        = [ "Id",
                    "FrName",
                    "FrExName",
                    "ToName",
                    "ToExName",
                    "MeterName",
                    "MeterExName",
                    "NMeterName",
                    "NMeterExName"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABrnChar[key])
    iErr, datChar   = psspy.abrnchar(   sid     = mySid,
                                        ties    = fTies,
                                        flag    = fType,
                                        entry   = fEntry,
                                        string  = strQuery
                                        )
    dictChar    = dict(zip(keys, datChar))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkBrchViol():\t datChar iErr [" + str(iErr) + "]")
        print(datChar)

    # Get count
    iErr, datCount   = psspy.abrncount( sid     = mySid,
                                        ties    = fTies,
                                        flag    = fType,
                                        entry   = fEntry
                                        )
    ctrErr = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkBrchViol():\t datCount iErr [" + str(iErr) + "]")
        print(datCount)

    # Get cplx
    strQuery    = []
    keys        = [ "PQ",
                    "PQLoss",
                    "O_PQ",
                    "O_PQLoss"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABrnCplx[key])
    iErr, datCplx   = psspy.abrncplx(   sid     = mySid,
                                        ties    = fTies,
                                        flag    = fType,
                                        entry   = fEntry,
                                        string  = strQuery
                                        )
    dictCplx    = dict(zip(keys, datCplx))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkBrchViol():\t datCplx iErr [" + str(iErr) + "]")
        print(datCplx)

    # Get int
    strQuery    = []
    keys        = [ "FrNumber",
                    "ToNumber",
                    "Status",
                    "MeterNumber",
                    "NMeterNumber",
                    "Own1"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABrnInt[key])
    iErr, datInt    = psspy.abrnint(    sid     = mySid,
                                        ties    = fTies,
                                        flag    = fType,
                                        entry   = fEntry,
                                        string  = strQuery
                                        )
    dictInt     = dict(zip(keys, datInt))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkBrchViol():\t datInt iErr [" + str(iErr) + "]")
        print(datInt)

    # Get real
    strQuery    = []
    keys        = [ "P",
                    "Q",
                    "MVA",
                    "MaxMVA",
                    "PLoss",
                    "QLoss",
                    "MaxPctRateA",
                    "MaxPctRateB",
                    "MaxPctRateC",
                    "RateA",
                    "RateB",
                    "RateC"
                    ]
    for key in keys:
        strQuery.append(pvhTools.dictABrnReal[key])
    iErr, datReal   = psspy.abrnreal(   sid     = mySid,
                                        ties    = fTies,
                                        flag    = fType,
                                        entry   = fEntry,
                                        string  = strQuery
                                        )
    dictReal    = dict(zip(keys, datReal))
    ctrErr      = ctrErr + iErr
    if(bDebug and iErr):
        print("\n\n")
        print("chkBrchViol():\t datReal iErr [" + str(iErr) + "]")
        print(datReal)
        
    # Combine all dictioanries into a larger one for easier iterating
    dictAll = { "char"  : dictChar,
                "cplx"  : dictCplx,
                "int"   : dictInt,
                "real"  : dictReal
                }


    # Now check for branch violations
    ctrDict         = 0
    ctrViolations   = 0
    
    while(ctrDict < datCount):
        # Write data if we have a branch violation
        if( dictAll["real"][strMaxPctLoading][ctrDict] >= brnchLim ):
            #print("---- branch violation:")
            #print("    " + str(dictAll["int"]["FrNumber"][ctrDict]) + "/" + str(dictAll["int"]["ToNumber"][ctrDict]) + ":" + dictAll["char"]["Id"][ctrDict] + " " + str(dictAll["real"][strMaxPctLoading][ctrDict]))

            # Write csv header data
            wrtBaseSchema(fCsv = fCsv, baseCaseData = baseCaseData)

            # Write voltage violation blanks
            wrtBlanks(fCsv = fCsv, dataClass = "vv")
            
            # Determine what kind of output (branch or transformer)
            if(brnType == "bv"):
                # Write branch violation data
                fCsv.write(str(dictAll["int"]["FrNumber"][ctrDict]) + csvDelim)
                fCsv.write(dictAll["char"]["FrName"][ctrDict] + csvDelim)
                fCsv.write(str(0) + csvDelim)                                   # Area placeholder
                fCsv.write(str(0) + csvDelim)                                   # kV placeholder
                fCsv.write(str(dictAll["int"]["ToNumber"][ctrDict]) + csvDelim)
                fCsv.write(dictAll["char"]["ToName"][ctrDict] + csvDelim)
                fCsv.write(str(0) + csvDelim)                                   # Area placeholder
                fCsv.write(str(0) + csvDelim)                                   # kV placeholder
                fCsv.write(dictAll["char"]["Id"][ctrDict] + csvDelim)
                fCsv.write(str(dictAll["real"]["MaxMVA"][ctrDict]) + csvDelim)
                fCsv.write(str(dictAll["real"][strMVALim][ctrDict]) + csvDelim)
                fCsv.write(str(dictAll["real"][strMaxPctLoading][ctrDict]) + csvDelim)
                
                # Write branch transformer violation blanks
                wrtBlanks(fCsv = fCsv, dataClass = "tv")
                fCsv.write("\n")
            else:
                # Write branch violation data
                wrtBlanks(fCsv = fCsv, dataClass = "bv")
                
                # Write branch transformer violation data
                fCsv.write(str(dictAll["int"]["FrNumber"][ctrDict]) + csvDelim)
                fCsv.write(dictAll["char"]["FrName"][ctrDict] + csvDelim)
                fCsv.write(str(0) + csvDelim)                                   # Area placeholder
                fCsv.write(str(0) + csvDelim)                                   # kV placeholder
                fCsv.write(str(dictAll["int"]["ToNumber"][ctrDict]) + csvDelim)
                fCsv.write(dictAll["char"]["ToName"][ctrDict] + csvDelim)
                fCsv.write(str(0) + csvDelim)                                   # Area placeholder
                fCsv.write(str(0) + csvDelim)                                   # kV placeholder
                fCsv.write(dictAll["char"]["Id"][ctrDict] + csvDelim)
                fCsv.write(str(dictAll["real"]["MaxMVA"][ctrDict]) + csvDelim)
                fCsv.write(str(dictAll["real"][strMVALim][ctrDict]) + csvDelim)
                fCsv.write(str(dictAll["real"][strMaxPctLoading][ctrDict]) + csvDelim)
                
                fCsv.write("\n")
            
            # Increment violation counter
            ctrViolations = ctrViolations + 1

        ctrDict = ctrDict + 1
    
    return ctrViolations
# ---- End of   chkBrchViol()--------------------------------------------------

# ---- Start of main() --------------------------------------------------------
if __name__ == "__main__":
    iErr    = 0
    ctrErr  = 0                                                                 # Running error total
    
    timeStart = time.time()

    # Init session log
    formatterLog = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s', datefmt='%y-%m-%d %H:%M:%S')

    fNameSession    = "session_" +  datetime.now().strftime("%y%m%d_%H%M%S")     #session_[case]_yymmdd_hhmmss.txt

    # Set up file handler
    hLog = logging.FileHandler(strPathOut + fNameSession + pvhTools.dictExt["ext_txt"])
    hLog.setFormatter(formatterLog)
    hLog.setLevel(logging.INFO)

    # Set up console stream handler
    sLog = logging.StreamHandler()
    sLog.setFormatter(formatterLog)
    sLog.setLevel(logging.INFO)

    # Get logger
    appLog = logging.getLogger('root')
    appLog.setLevel(logging.INFO)

    # Add both handlers
    appLog.addHandler(hLog)
    appLog.addHandler(sLog)
    
    # Set up csv output file
    fCsv    = open( strPathOut + "contingency_results" + pvhTools.dictExt["ext_csv"],
                    "w"
                    )
    
    # Write headers
    for index, indCol in enumerate(csvHeaders):
        fCsv.write(indCol[1])
        
        if(index < (len(csvHeaders) - 1)):
            fCsv.write(csvDelim)
    fCsv.write("\n")
    
    strWrite = "---- Starting " + name_study + " powerflow contingencies: -------------------------------------------\n"
    strWrite = strWrite + "Voltage limits: " + str("{:.2f}".format(vLimLo)) + " - " + str("{:.2f}".format(vLimHi)) + "\n"
    strWrite = strWrite + "Branch limit:   " + str("{:.2f}".format(110)) + "\n"
    appLog.info(strWrite)
    
    # Start PSS/e
    iErr = psspy.psseinit()
    
    # Loop through basecases
    for basecase in autocont_runlist_basecase.runlist_basecases:
        # Set case name (full name w/o extension)
        nameCase = os.path.splitext(basecase[0])[0]
        
        # Set report file
        psspy.lines_per_page_one_device(    device  = 1,
                                            ival    = 60)
        psspy.report_output(    islct       = 2,
                                filarg      = strPathOut + "report_-_" + nameCase + pvhTools.dictExt['ext_txt'],
                                options1    = 0
                                )
        psspy.progress_output(  islct       = 2,
                                filarg      = strPathOut + "prog_-_" + nameCase + pvhTools.dictExt['ext_txt'],
                                options     = 0
                                )
                                
        psspy.progress("---- PSS/e started with code [" + str(iErr) + "]\n")
        psspy.progress("     Working path is: [" + os.getcwd() + "].\n")

        ctrCont = 0
        totCont = len(autocont_runlist_contingency.runlist_contingencies)
        # Loop through the contingencies
        for contingency in autocont_runlist_contingency.runlist_contingencies:
            baseCaseData = {    "case":     basecase[0],
                                "cont":     contingency,
                                "rate":     basecase[1],
                                "status":   0
                            }

            # Load case
            iErr = psspy.case(baseCaseData["case"])
            iErr = psspy.transformer_percent_units(ival = 1)                    # 1: current expressed as MVA
            
            # Set title
            iErr = psspy.case_title_data(   line1 = name_study,
                                            line2 = baseCaseData["cont"]
                                            )

            strWrite = baseCaseData["case"] + ": Starting contingency " + str("{:03}".format(ctrCont)) + "/" + str(totCont) + " [" + contingency + "]."
            appLog.info(strWrite)


            # Run the contingency
            for step in autocont_defs_contingency.def_contingencies[contingency]:
                exec step

            # Solve
            iErr = psspy.solution_parameters_4(intgar2  = 100)
            iErr = psspy.fdns(  options1    = 0,    # tap adj
                                options2    = 0,    # area interchange
                                options3    = 0,    # phase shifters
                                options4    = 1,    # DC tap adj
                                options5    = 1,    # switched shunt adj
                                options6    = 0,    # no flat start
                                options7    = 0,    # apply VAR limits immediately
                                options8    = 0     # disable non-divergent solution
                                )
            iSolved = psspy.solved()
            baseCaseData["status"] = iErr + iSolved
            #text = autocont_defs_contingency.def_contingencies[contingency]
            #baseCaseData["status"] = 0
            
            # Define bus subsystem
            mySid   = 10
            iErr = psspy.bsys(  sid     = mySid,
                                usekv   = 0,
                                numarea = 1,
                                areas    = [106]
                                )
            # If we have a solved solution, process voltage and branch violations (if any)
            ctrVV = 0
            ctrBV = 0
            ctrTV = 0
            
            # Do bus voltage check
            ctrVV = chkVoltViol(mySid   = mySid,
                                vLo     = vLimLo,
                                vHi     = vLimHi,
                                appLog  = appLog,
                                fCsv    = fCsv,
                                baseCaseData = baseCaseData
                                )

            # Do branch check
            ctrBV = chkBrchViol(mySid   = mySid,
                                brnchLim  = brnLim,
                                brnType = "bv",
                                appLog  = appLog,
                                fCsv    = fCsv,
                                baseCaseData = baseCaseData
                                )

            
            # If no violations found, write in blank entry 
            if( (ctrVV == 0) and (ctrBV == 0) and (ctrTV ==0) ):
                # Write csv header data
                wrtBaseSchema(fCsv = fCsv, baseCaseData = baseCaseData)
                
                # Write voltage violation blanks
                wrtBlanks(fCsv = fCsv, dataClass = "vv")
                
                # Write branch violation blanks
                wrtBlanks(fCsv = fCsv, dataClass = "bv")
                
                # Write branch transformer violation blanks
                wrtBlanks(fCsv = fCsv, dataClass = "tv")
                fCsv.write("\n")
            
            
            
            strWrite = "Finished " + contingency + ".\n"
            appLog.info(strWrite)
            
            ctrCont = ctrCont + 1

        # End of contingency loop
    # End of basecase loop

    # Cleanup    
    fCsv.close()
    
    # Close PSS/e
    iErr = psspy.pssehalt_2()

    # Calculate end time and duration
    timeEnd = time.time()
    simTime = timeEnd - timeStart
    
    appLog.info("\n\n")
    strWrite = "Session complete, duration was " + str("{:.0f}".format(simTime)) + " seconds."
    appLog.info(strWrite)

    # Make the beep
    winsound.Beep(frequency, duration)
    winsound.Beep(frequency/2, duration)
    winsound.Beep(frequency, duration)
    winsound.Beep(frequency/2, duration)
# ---- End of main() ----------------------------------------------------------