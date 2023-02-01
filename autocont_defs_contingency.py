    # autocont_defs_contingency.py
    #
    #
    # *** CHECK UNITS TARGETED FOR SPS ACTION - ML OR LG/PA AND MATCH TO STUDY CASES *** 
    #
    # ----------------------------------------------------------------------------------------------------
    # LOADFLOW Contingencies for 2019 Load Transfer Study
    # Post ML - Use ML runback for Group 5 SPS and Group 6 SPS
    # Added LG1 and LG4 options for SPS action where we are exporting to NL
    # Updated:	September 2017, John Charlton
    # Removed dummy bus 199040 on L7014, added Spider Lake, 
    # ----------------------------------------------------------------------------------------------------

    #import psspy
    #from psspy import _i, _f, _s, _o

    #def import_contingencydata():

def_contingencies = {
    # ----------
    # 88S-Lingan
    # ----------
    '88S_L-7014':[
    '''psspy.branch_data(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '88S_L-7021':[
    '''psspy.branch_data(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '88S_L-7022':[
    '''psspy.branch_data(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    # 88S-710 trips 88S-GT3 and 88S-T71
    '88S-710':[
    '''psspy.dscn(199003)''',
    '''psspy.two_winding_data_3(199000,199005,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""88S-T71""")''',
    ],
    # 88S-711 trips 88S-T71 and 88S-GT1
    '88S-711':[
    '''psspy.two_winding_data_3(199000,199005,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""88S-T71""")''',
    '''psspy.dscn(199001)'''],
    # 88S-713 trips 88S-T72 and L-7021
    '88S-713':[
    '''psspy.branch_data(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199000,199006,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""88S-T72""")''',
    ],
    # 88S-714 trips 88S-T72 and 88S-GT2
    '88S-714':[
    '''psspy.dscn(199002)''',
    '''psspy.two_winding_data_3(199000,199006,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""88S-T72""")''',
    ],
    # 88S-715 trips 88S-T71 and 88S-GT2
    '88S-715':[
    '''psspy.dscn(199002)''',
    '''psspy.two_winding_data_3(199000,199005,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""88S-T71""")''',
    ],
    # 88S-720 trips 88S-T72 and L-7014
    '88S-720':[
    '''psspy.two_winding_data_3(199000,199006,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""88S-T72""")''',
    '''psspy.branch_data(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 88S-721 trips 88S-GT4 and 88S-GT3
    '88S-721':[
    '''psspy.dscn(199003)''',
    '''psspy.dscn(199004)''',
    ],
    # 88S-722 trips L-7022 and 88S-GT4
    '88S-722':[
    '''psspy.dscn(199004)''',
    '''psspy.branch_data(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 88S-723 trips L-7014 and L-7022
    '88S-723_G0':[
    '''psspy.branch_data(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 88S-723 trips L-7014 and L-7022
    '88S-723_G8':[
    '''psspy.branch_data(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199002)''',
    ],

    '88S-T71':[
    '''psspy.dscn(199005)'''],

    '88S-T72':[
    '''psspy.dscn(199006)'''],

    '88S-G2':[
    '''psspy.dscn(199002)'''],

    '88S-G3':[
    '''psspy.dscn(199003)'''],

    '88S-G4':[
    '''psspy.dscn(199004)'''],
    # -------------
    # 101S-Woodbine
    # -------------
    '101S_ML-POLE1':[
    '''psspy.dscn(199855)''',
    '''psspy.shunt_data(199045,r"""2""",0,[_f,_f])'''],

    '101S_ML-POLE2':[
    '''psspy.dscn(199857)''',
    '''psspy.shunt_data(199045,r"""3""",0,[_f,_f])'''],

    '101S_ML-BIPOLE':[
    '''psspy.dscn(199855)''',
    '''psspy.shunt_data(199045,r"""2""",0,[_f,_f])''',
    '''psspy.fdns([0,0,0,1,1,0,99,0])''',
    '''psspy.fdns([0,0,0,1,1,0,99,0])''',
    '''psspy.dscn(199857)''',
    '''psspy.shunt_data(199045,r"""3""",0,[_f,_f])''',
    '''psspy.shunt_chng(199042, '2', intgar1 = 0)''',
    '''psspy.shunt_chng(199042, '3', intgar1 = 0)''',
    ],

    '101S-T81':[
    '''psspy.two_winding_data_3(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T81""")'''],

    '101S-T82':[
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")'''],

    '101S_L-7011':[
    '''psspy.branch_data(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '101S_L-7011_G1':[
    '''psspy.branch_data(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    ],

    '101S_L-7012':[
    '''psspy.branch_data(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '101S_L-7012_G2':[
    '''psspy.branch_data(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    ],

    '101S_L-7015':[
    '''psspy.branch_data(199042,199044,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199044)''',
    '''psspy.dscn(199043)''',
    ],

    '101S_L-8004_G0':[
    '''psspy.branch_data(199045,199120,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '101S_L-8004_G5':[
    '''psspy.branch_data(199045,199120,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    ],

    '101S_L-8004_G6':[
    '''psspy.branch_data(199045,199120,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G6')'''],

    # 101S-701 trips L-7012 and 101S-T81
    '101S-701':[
    '''psspy.two_winding_data_3(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T81""")''',
    '''psspy.branch_data(199050,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 101S-702 trips L-7012 and L-7014
    '101S-702':[
    '''psspy.branch_data(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199050,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 101S-703 trips 101S-T82 and L-7014
    '101S-703':[
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    '''psspy.branch_data(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 101S-704 trips 101S-T82 and L-7011
    '101S-704':[
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    '''psspy.branch_data(199050,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 101S-705 trips L-7022 and L-7011
    '101S-705':[
    '''psspy.branch_data(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199050,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 101S-706 trips 101S-T81 and L-7022
    '101S-706':[
    '''psspy.branch_data(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T81""")''',
    ],
    # 101S-711 trips 101S-T81 and L-7021
    '101S-711':[
    '''psspy.branch_data(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T81""")''',
    ],
    # 101S-712 trips L-7021 and L-7015
    '101S-712':[
    '''psspy.branch_data(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199044)''',
    '''psspy.dscn(199043)''',
    ],
    # 101S-713 trips 101S-T82 and L-7015
    '101S-713':[
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    '''psspy.dscn(199044)''',
    '''psspy.dscn(199043)''',
    ],
    # 101S-811 trips 101S-T81 and ML Pole 1
    '101S-811':[
    '''psspy.two_winding_data_3(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T81""")''',
    '''psspy.dscn(199855)''',
    '''psspy.shunt_data(199045,r"""2""",0,[_f,_f])'''],
    # 101S-812 trips L-8004 and ML Pole 1
    '101S-812_G0':[
    '''psspy.dscn(199855)''',
    '''psspy.branch_data(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.shunt_data(199045,r"""2""",0,[_f,_f])'''],
    # 101S-812 trips L-8004 and ML Pole 1
    '101S-812_G5':[
    '''psspy.branch_data(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    '''psspy.dscn(199855)''',
    '''psspy.shunt_data(199045,r"""2""",0,[_f,_f])''',
    ],
    # 101S-812 trips L-8004 and ML Pole 1
    '101S-812_G6':[
    '''psspy.branch_data(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G6')''',
    '''psspy.dscn(199855)''',
    '''psspy.shunt_data(199045,r"""2""",0,[_f,_f])''',
    ],
    # 101S-813 trips L-8004 and 101S-T82
    '101S-813_G0':[
    '''psspy.branch_data(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    ],
    # 101S-813 trips L-8004 and 101S-T82
    '101S-813_G5':[
    '''psspy.branch_data(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    '''sps('G5')''',
    ],
    # 101S-813 trips L-8004 and 101S-T82
    '101S-813_G6':[
    '''psspy.branch_data(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    '''sps('G6')''',
    ],
    # 101S-814 trips ML Pole 2 and 101S-T82
    '101S-814':[
    '''psspy.dscn(199857)''',
    '''psspy.shunt_data(199045,r"""3""",0,[_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T82""")''',
    ],
    # 101S-814 trips ML Pole 2 and 101S-T81
    '101S-816':[
    '''psspy.dscn(199857)''',
    '''psspy.shunt_data(199045,r"""3""",0,[_f,_f])''',
    '''psspy.two_winding_data_3(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""101S-T81""")''',
    ],
    # ------------------
    # 3C-Port Hastings
    # ------------------
    '3C_L-7003':[
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '3C_L-7004':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '3C_L-7005_G0':[
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '3C_L-7005_G3':[
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G3')''',
    ],

    '3C-T71':[
    '''psspy.two_winding_data_3(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T71""")''',
    ],

    '3C-T72':[
    '''psspy.two_winding_data_3(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T72""")''',
    ],

    # 3C-710 trips L-7005 and 3C-T71
    '3C-710_G0':[
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T71""")''',
    ],
    # 3C-710 trips L-7005 and 3C-T71 - G3 armed in some cases
    '3C-710_G3':[
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T71""")''',
    '''sps('G3')''',
    ],
    # 3C-711 trips L-7011 and 3C-T71
    '3C-711':[
    '''psspy.branch_data(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T71""")''',
    ],
    # 3C-712 trips L-7003 and L-7011
    '3C-712':[
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 3C-712 trips L-7003 and L-7011
    '3C-712_G4-1':[
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    ],
    '3C-712_G4-2':[
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G6')''',
    ],
    # 3C-713 trips L-7003 and 3C-T72
    '3C-713':[
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T72""")''',
    ],
    # 3C-714 trips L-7012 and 3C-T72
    '3C-714':[
    '''psspy.two_winding_data_3(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T72""")''',
    '''psspy.branch_data(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 3C-715 trips L-7004 and L-7012
    '3C-715':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    '3C-715_G4-1':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    ],
    '3C-715_G4-2':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G6')''',
    ],
    # 3C-716 trips L-7004 and 3C-T71
    '3C-716':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""3C-T71""")''',
    ],
    # ------------
    # 79N-Hopewell			   
    # ------------   
    '79N_L-8003_G0':[
    '''psspy.branch_data(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '79N_L-8003_G5':[
    '''psspy.branch_data(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G5')''',
    ],

    '79N_L-8003_G6':[
    '''psspy.branch_data(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G6')''',
    ],

    '79N_L-6507':[
    '''psspy.branch_data(199090,199121,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '79N_L-6508':[
    #'''psspy.branch_data(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',     # Modified for Stellarton substation
    '''psspy.branch_data(199121,199963,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '79N-T81_G0':[
    '''psspy.dscn(199121)''',
    '''psspy.dscn(199120)''',
    ],

    '79N-T81_G5':[
    '''psspy.dscn(199121)''',
    '''psspy.dscn(199120)''',
    '''sps('G5')''',
    ],

    '79N-T81_G6':[
    '''psspy.dscn(199121)''',
    '''psspy.dscn(199120)''',
    '''sps('G6')''',
    ],

    # SAME AS 79N-T81! 
    # 79N-803 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
    # 79N-810 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
    # 79N-601 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
    # 79N-606 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
    # ----------
    # 67N-Onslow    
    # ----------	   
    '67N_L-8001_G0':[
    '''psspy.dscn(190381)''',
    ],

    '67N_L-8001_NSX1':[
    '''psspy.dscn(190381)''',
    '''sps('NSX1')''',
    ],

    '67N_L-8001_NSX2':[
    '''psspy.dscn(190381)''',
    '''sps('NSX2')''',
    ],

    '67N_L-8002':[
    '''psspy.branch_data(199125,199195,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '67N_L-7019':[
    '''psspy.branch_data(199130,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '67N_L-7001':[
    '''psspy.branch_data(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '67N_L-7002':[
    '''psspy.branch_data(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '67N-T81':[
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    ],

    '67N-T82':[
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    ],

    '67N-T71':[
    '''psspy.two_winding_data_3(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T71""")''',
    ],
    # 67N-811 trips L-8003 and 67N-T82
    '67N-811_G0':[
    '''psspy.branch_data(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    ],
    # 67N-811 trips L-8003 and 67N-T82
    '67N-811_G5':[
    '''psspy.branch_data(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    '''sps('G5')''',
    ],
    # 67N-811 trips L-8003 and 67N-T82
    '67N-811_G6':[
    '''psspy.branch_data(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    '''sps('G6')''',
    ],
    # 67N-813 trips L-8002 and 67N-T81
    '67N-813':[
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    '''psspy.branch_data(199125,199195,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 67N-814 trips L-8001 and 67N-T81
    '67N-814_G0':[
    '''psspy.dscn(190381)''',
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    ],
    # 67N-814 trips L-8001 and 67N-T81
    '67N-814_NSX1':[
    '''psspy.dscn(190381)''',
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    '''sps('NSX1')''',
    ],
    # 67N-814 trips L-8001 and 67N-T81
    '67N-814_NSX2':[
    '''psspy.dscn(190381)''',
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    '''sps('NSX2')''',
    ],

    # 67N-815 trips L-8001 and [empty node]
    # SAME AS L-8001

    # 67N-701 trips L-7002 and 67N-T71
    '67N-701':[
    '''psspy.branch_data(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T71""")''',
    ],
    # 67N-702 trips L-7002 and L-7003
    '67N-702':[
    '''psspy.branch_data(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 67N-703 trips L-7003 and 67N-T81
    '67N-703':[
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199130,199125,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    ],
    # 67N-704 trips L-7001 and 67N-T81
    '67N-704':[
    '''psspy.branch_data(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    ],
    # 67N-705 trips L-7001 and L-7019
    '67N-705':[
    '''psspy.branch_data(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199130,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 67N-706 trips L-7019 and 67N-T71
    '67N-706':[
    '''psspy.branch_data(199130,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T71""")''',
    ],
    # 67N-710 trips 67N-T82 and 67N-T71
    '67N-710':[
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    '''psspy.two_winding_data_3(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T71""")''',
    ],
    # 67N-711 trips L-7005 and 67N-T82
    '67N-711_G0':[
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    ],
    # 67N-711 trips L-7005 and 67N-T82
    '67N-711_G3':[
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T82""")''',
    '''sps('G3')''',
    ],
    # 67N-712 trips L-7005 and L-7018
    '67N-712':[
    '''psspy.branch_data(199200,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 67N-713 trips 67N-T81 and L-7018
    '67N-713':[
    '''psspy.branch_data(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T81""")''',
    ],
    # ---------
    # 1N-Onslow
    # ---------
    '1N_L-6513':[
    '''psspy.dscn(199134)''',
    ],

    '1N_L-6503':[
    '''psspy.dscn(199100)''',
    ],

    '1N_L-6001':[
    '''psspy.dscn(199154)''',
    '''psspy.dscn(199156)''',
    '''psspy.dscn(199159)''',
    '''psspy.dscn(199155)''',
    ],

    '1N-T1':[
    '''psspy.dscn(199584)''',
    '''psspy.dscn(199583)''',
    '''psspy.dscn(199582)''',
    '''psspy.dscn(199581)''',
    '''psspy.dscn(199580)''',
    '''psspy.dscn(199118)''',
    '''psspy.dscn(199116)''',
    '''psspy.dscn(199115)''',
    '''psspy.dscn(199111)''',
    ],

    '1N-T4':[
    '''psspy.dscn(199112)''',
    '''psspy.dscn(199114)''',
    ],

    '1N-T65':[
    '''psspy.load_data_3(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
    ],

    '1N-C61':[
    '''psspy.shunt_data(199110,r"""2""",0,[_f,_f])''',
    ],

    '1N-B61':[
    '''psspy.shunt_data(199110,r"""2""",0,[_f,_f])''',
    '''psspy.two_winding_data_3(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T71""")''',
    '''psspy.two_winding_data_3(199110,199112,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""1N-T4""")''',
    '''psspy.branch_data(199110,199154,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199112)''',
    '''psspy.dscn(199114)''',
    ],

    '1N-B62':[
    '''psspy.load_data_3(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199110,199111,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""1N-T1""")''',
    '''psspy.branch_data(199110,199134,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199584)''',
    '''psspy.dscn(199583)''',
    '''psspy.dscn(199582)''',
    '''psspy.dscn(199581)''',
    '''psspy.dscn(199580)''',
    '''psspy.dscn(199118)''',
    '''psspy.dscn(199116)''',
    '''psspy.dscn(199115)''',
    '''psspy.dscn(199111)''',
    ],

    '1N-600':[
    '''psspy.dscn(199110)''',
    '''psspy.dscn(199584)''',
    '''psspy.dscn(199583)''',
    '''psspy.dscn(199582)''',
    '''psspy.dscn(199581)''',
    '''psspy.dscn(199580)''',
    '''psspy.dscn(199118)''',
    '''psspy.dscn(199116)''',
    '''psspy.dscn(199115)''',
    '''psspy.dscn(199111)''',
    '''psspy.dscn(199112)''',
    '''psspy.dscn(199114)''',
    ],

    '1N-601':[
    '''psspy.dscn(199159)''',
    '''psspy.dscn(199156)''',
    '''psspy.dscn(199154)''',
    '''psspy.dscn(199155)''',
    '''psspy.two_winding_data_3(199110,199112,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""1N-T4""")''',
    '''psspy.dscn(199112)''',
    '''psspy.dscn(199114)''',
    '''psspy.two_winding_data_3(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""67N-T71""")''',
    '''psspy.shunt_data(199110,r"""2""",0,[_f,_f])''',
    ],

    '1N-613':[
    '''psspy.dscn(199134)''',
    '''psspy.branch_data(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.load_data_3(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199584)''',
    '''psspy.dscn(199583)''',
    '''psspy.dscn(199582)''',
    '''psspy.dscn(199581)''',
    '''psspy.dscn(199580)''',
    '''psspy.dscn(199118)''',
    '''psspy.dscn(199116)''',
    '''psspy.dscn(199115)''',
    '''psspy.dscn(199111)''',
    ],
    # ----------------
    # 120H-Brushy Hill
    # ----------------			   
    '120H_L-7008':[
    '''psspy.branch_data(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '120H_L-7009':[
    '''psspy.branch_data(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '120H_L-6005':[
    '''psspy.dscn(199203)''',
    ],

    '120H_L-6010':[
    '''psspy.branch_data(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '120H_L-6011':[
    '''psspy.branch_data(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '120H_L-6051':[
    '''psspy.branch_data(199201,199300,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '120H_L-6016':[
    '''psspy.dscn(199208)''',
    '''psspy.dscn(199209)''',
    ],

    '120H-T71':[
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    ],

    '120H-T72':[
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    ],

    '120H-SVC':[
    '''psspy.dscn(199202)''',
    ],
    # 120H-710 trips L-7018 and 120H-T71
    '120H-710':[
    '''psspy.branch_data(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    ],
    # 120H-711 trips L-7002 and 120H-T71
    '120H-711':[
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    '''psspy.branch_data(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-712 trips L-7002 and L-7009
    '120H-712':[
    '''psspy.branch_data(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-713 trips L-7009 and 120H-T72
    '120H-713':[
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    '''psspy.branch_data(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-714 trips L-7001 and 120H-T72
    '120H-714':[
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    '''psspy.branch_data(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-715 trips L-7001 and L-7008
    '120H-715':[
    '''psspy.branch_data(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-716 trips L-7008 and 120H-T71
    '120H-716':[
    '''psspy.branch_data(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    ],
    # 120H-720 trips L-7018 and 120H-T72
    '120H-720':[
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    '''psspy.branch_data(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-621 trips L-6005 and 120H-T71
    '120H-621':[
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    '''psspy.branch_data(199201,199203,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-622 trips L-6005 and L-6016B
    '120H-622':[
    '''psspy.branch_data(199201,199203,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199201,199208,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-623 trips L-6016B and 120H-T72
    '120H-623':[
    '''psspy.branch_data(199201,199208,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    ],
    # 120H-624 trips L-6010 and 120H-T72
    '120H-624':[
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    '''psspy.branch_data(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],
    # 120H-626 trips L-6011 and 120H-T71
    '120H-626':[
    '''psspy.branch_data(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    ],
    # 120H-627 trips L-6051 and 120H-T71
    '120H-627':[
    '''psspy.branch_data(199201,199300,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T71""")''',
    ],
    # 120H-628 trips L-6051 and 120H-SVC
    '120H-628':[
    '''psspy.branch_data(199201,199300,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199202)''',
    ],
    # 120H-629 trips 120H-SVC and 120H-T72
    '120H-629':[
    '''psspy.dscn(199202)''',
    '''psspy.two_winding_data_3(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""120H-T72""")''',
    ],
    # -------------
    # 103H-Lakeside
    # -------------   
    '103H_L-6008':[
    '''psspy.branch_data(199184,199190,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '103H_L-6033':[
    '''psspy.dscn(199197)''',
    ],

    '103H_L-6038':[
    '''psspy.dscn(199192)''',
    ],

    '103H-T81':[
    '''psspy.two_winding_data_3(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""103H-T81""")''',
    ],

    '103H-T61':[
    '''psspy.dscn(199191)''',
    '''psspy.two_winding_data_3(199191,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""103H-T61""")''',
    ],

    '103H-T63':[
    '''psspy.dscn(199205)''',
    '''psspy.dscn(199196)''',
    '''psspy.dscn(199180)''',
    ],

    '103H-B61':[
    '''psspy.two_winding_data_3(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""103H-T81""")''',
    '''psspy.branch_data(199190,199197,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199205)''',
    '''psspy.dscn(199196)''',
    '''psspy.dscn(199180)''',
    ],

    '103H-B62':[
    '''psspy.dscn(199191)''',
    '''psspy.branch_data(199184,199190,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199192)''',
    '''psspy.dscn(199208)''',
    '''psspy.dscn(199209)'''],

    '103H-881':[
    '''psspy.dscn(199195)''',
    '''psspy.two_winding_data_3(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""103H-T81""")''',
    ],
    # 103H-600 trips B-61 and B-62
    '103H-600':[
    '''psspy.dscn(199205)''',
    '''psspy.dscn(199196)''',
    '''psspy.dscn(199180)''',
    '''psspy.dscn(199191)''',
    '''psspy.dscn(199192)''',
    '''psspy.dscn(199190)''',
    ],
    # 103H-608 trips L-6008 and B-62
    '103H-608':[
    '''psspy.dscn(199191)''',
    '''psspy.dscn(199192)''',
    '''psspy.dscn(199208)''',
    '''psspy.dscn(199209)''',
    '''psspy.branch_data(199184,199190,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''],
    # 103H-681 trips B-61 and 103H-T81
    '103H-681':[
    '''psspy.dscn(199205)''',
    '''psspy.dscn(199196)''',
    '''psspy.dscn(199180)''',
    '''psspy.two_winding_data_3(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""103H-T81""")''',
    '''psspy.dscn(199197)''',
    ],
    # ---------------
    # 89S-Point Aconi
    # ---------------  
    '89S-G1':[
    '''psspy.dscn(199043)''',
    ],
    # ---------------
    # 91H-Tuft's Cove
    # ---------------
    '91H_L-5049':[
    '''psspy.branch_data(199166,199170,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '91H_L-5012':[
    '''psspy.dscn(199176)''',
    '''psspy.dscn(199175)''',
    ],

    '91H_L-5041':[
    '''psspy.branch_data(199166,199170,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '91H-T62':[
    '''psspy.two_winding_data_3(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""91H-T62""")''',
    ],

    '91H-T11':[
    '''psspy.two_winding_data_3(199165,199166,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""91H-T11""")''',
    ],
    # 91H-511 trips B-52 and L-5049
    '91H-511':[
    '''psspy.branch_data(199166,199170,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""91H-T62""")''',
    ],
    # 91H-516 trips B-52 and L-5012
    '91H-516':[
    '''psspy.dscn(199176)''',
    '''psspy.dscn(199175)''',
    '''psspy.two_winding_data_3(199166,199165,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""91H-T62""")''',
    ],
    # 91H-521 trips B-52 and L-5041
    '91H-521':[
    '''psspy.branch_data(199166,199170,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199166,199165,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""91H-T62""")''',
    ],
    # 91H-523 trips 91H-T11 and L-5041
    '91H-523':[
    '''psspy.branch_data(199166,199170,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_data_3(199166,199165,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""91H-T11""")''',
    ],
    # ----------------------
    # 91N-Dalhousie Mountain
    # ----------------------
    '91N-701':[
    '''psspy.dscn(199590)''',
    '''psspy.dscn(199591)''',
    '''psspy.dscn(199592)''',
    '''psspy.dscn(199593)''',
    ],

    '91N-702':[
    '''psspy.branch_data(199590,199130,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199591)''',
    '''psspy.dscn(199592)''',
    '''psspy.dscn(199593)''',
    ],
         
    '91N-703':[
    '''psspy.branch_data(199590,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199591)''',
    '''psspy.dscn(199592)''',
    '''psspy.dscn(199593)''',
    ],

    '91N-B71':[
    '''psspy.dscn(199591)''',
    '''psspy.dscn(199592)''',
    '''psspy.dscn(199593)''',
    ],
    # *********************
    # 99W-Bridgewater 230kV
    # *********************
    '99W-708':[
    '''psspy.dscn(199240)''',
    ],

    '99W-709':[
    '''psspy.dscn(199241)''',
    ],

    '99W-T71':[
    '''psspy.two_winding_data_3(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""99W-T71""")''',
    ],

    '99W-T72':[
    '''psspy.two_winding_data_3(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],r"""99W-T72""")''',
    ],
    # ---------------------
    # Double Circuit Towers    
    # ---------------------  
    'DCT_L-5039][L-6033':[
    '''psspy.dscn(199197)''',
    '''psspy.dscn(199205)''',
    '''psspy.dscn(199196)''',
    '''psspy.dscn(199180)''',
    ],    

    'DCT_L-7009][L-8002':[
    '''psspy.branch_data(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199125,199195,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    'DCT_L-6011][L-6010':[
    '''psspy.branch_data(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    'DCT_L-6010][L-6005':[
    '''psspy.branch_data(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199203)''',
    ],

    'DCT_L-6005][L-6016':[
    '''psspy.dscn(199203)''',
    '''psspy.dscn(199208)''',
    '''psspy.dscn(199209)''',
    ],

    'DCT_L-7008][L-7009':[
    '''psspy.branch_data(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199292)''',
    '''psspy.branch_data(199252,199259,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
     '''no_island()''',
    ],

    'DCT_L-7003][L-7004_G0':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    'DCT_L-7003][L-7004_G3':[
    '''psspy.branch_data(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''sps('G3')''',
    ],

    'DCT_L-6507][L-6508':[
    '''psspy.branch_data(199090,199121,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    #'''psspy.branch_data(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',     # Changed to accomodate new Stellarton substation
    '''psspy.branch_data(199121,199963,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    'DCT_L-7021][L-6534':[
    '''psspy.dscn(199006)''',
    '''psspy.branch_data(199042,199000,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''],

    'DCT_L-6033][L-6035':[
    '''psspy.dscn(199193)''',
    '''psspy.dscn(199197)''',
    '''no_island()''',
    ],
    # ----------------------
    # Wreck Cove Area
    # ----------------------
    #Same as L6549
    '85S_L-6545':[
    '''psspy.branch_data(199035,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '5S_L-6538':[
    '''psspy.branch_data(199031,199025,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    '3S_L-6539':[
    '''psspy.dscn(199961)''',
    ],

    # Replaced with below for IR606: Lewis Mtn
    #'5S_L-6537':[
    #'''psspy.dscn(199033)''',
    #'''psspy.dscn(199057)''',
    #'''no_island()''',
    #],

    # Modified for IR606: Lewis Mtn
    '5S_L-6537':[
    '''psspy.dscn(199033)''',
    '''psspy.dscn(199057)''',
    '''psspy.dscn(199760)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199761)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199762)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199763)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199764)''',      # IR606: Lewis Mtn
    '''no_island()''',
    ],

    '5S_L-6516':[
    '''psspy.dscn(199063)''',
    '''psspy.dscn(199056)''',
    '''psspy.dscn(199070)''',
    ],

    #BBU trips L6549 and L6538
    '5S-606':[
    '''psspy.branch_data(199035,199031,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(199031,199025,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    # Replaced with below for IR606: Lewis Mtn
    ##BBU trips L6545 and L6537
    #'5S-607':[
    #'''psspy.branch_data(199035,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    #'''psspy.dscn(199033)''',
    #'''psspy.dscn(199057)''',
    #'''no_island()''',
    #],

    # Modified for IR606: Lewis Mtn
    #BBU trips L6545 and L6537
    '5S-607':[
    '''psspy.branch_data(199035,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(199033)''',
    '''psspy.dscn(199057)''',
    '''psspy.dscn(199760)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199761)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199762)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199763)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199764)''',      # IR606: Lewis Mtn
    '''no_island()''',
    ],

    # -------------------------------------------
    # Other BES Generator transformers/generators
    # -------------------------------------------
    # 2S-513 VJ BUS TIE BREAKER
    '2S-513':[
    '''psspy.dscn(199007)''',
    '''no_island()''',
    ],

    # 89S-GT1 AND 89S-G1
    '89S-G1':[
    '''psspy.dscn(199043)''',
    ],

    # 1C-GT2 and 1C-G2
    '1C-G2':[
    '''psspy.dscn(199055)''',
    ],

    # 47C-T68 and 48C-G1
    '48C-G1':[
    '''psspy.dscn(199072)''',
    ],

    # 50N-GT5 and 50N-G5
    '50N-G5':[
    '''psspy.dscn(199085)''',
    ],

    # 50N-GT6 and 50N-G6
    '50N-G6':[
    '''psspy.dscn(199086)''',
    ],

    # 91H-GT3 and 91H-G3 
    '91H-G3':[
    '''psspy.dscn(199169)''',
    ],

    # 91H-T64 and 91H-G4
    '91H-G4':[
    '''psspy.dscn(199181)''',
    ],

    # 91H-T65 and 91H-G5
    '91H-G5':[
    '''psspy.dscn(199182)''',
    ],

    # 91H-T66 and 91H-G6
    '91H-G6':[
    '''psspy.dscn(199164)''',
    ],

    # 104W-MPT and 104W-G1
    '104W-G1':[
    '''psspy.dscn(199279)''',
    ],

    # 110W-T62 and 110W-G1/G34
    '110W-T62':[
    '''psspy.dscn(199502)''',
    '''psspy.dscn(199503)''',
    '''psspy.dscn(199504)''',
    ],

    # 104H-600 KEMPT ROAD BUS TIE BREAKER 
    '104H-600':[
    '''psspy.dscn(199198)''',
    '''psspy.dscn(199199)''',
    ],
    # -------------------------------------------
    # Key New Brunswick Contingencies
    # -------------------------------------------
    # L3004 
    'SALISBURY_L3004':[
    '''psspy.branch_data(190197,190498,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    # L3013 
    'SALISBURY_L3013':[
    '''psspy.branch_data(190320,190498,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    # L3006 + L3017 NO SPS
    'SALISBURY_SA3-2':[
    '''psspy.branch_data(190320,190402,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(190320,190417,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''],

    # L3006 + L3017 TRIP PEI
    'SALISBURY_SA3-2_SPS':[
    '''psspy.branch_data(190320,190402,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.branch_data(190320,190417,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(190291)''',
    '''psspy.dscn(190292)''',
    '''psspy.dscn(192258)''',
    '''psspy.dscn(192259)''',
    '''no_island()''',
    ],

    # L3006 no SPS
    'SALISBURY_L3006':[
    '''psspy.branch_data(190320,190402,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    ],

    # L3006 TRIP PEI
    'SALISBURY_L3006_SPS':[
    '''psspy.branch_data(190402,190320,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.dscn(190291)''',
    '''psspy.dscn(190292)''',
    '''psspy.dscn(192258)''',
    '''psspy.dscn(192259)''',
    '''no_island()''',
    ],

    # ME1 TRIP L1159
    'MEMRAMCOOK_L1159':[
    '''psspy.dscn(190275)''',
    '''psspy.dscn(190379)''',
    '''no_island()''',
    ],
       
    # ME1 TRIP L1160
    'MEMRAMCOOK_L1160':[
    '''psspy.dscn(190408)''',
    '''psspy.dscn(199152)''',
    ],
  
    # ME3-1 WITH SPS TRIP L3006, L8001 AND PEI
    'MEMRAMCOOK_ME3-1_SPS':[
    '''psspy.dscn(190402)''',
    '''psspy.dscn(190381)''',
    '''psspy.dscn(190291)''',
    '''psspy.dscn(190292)''',
    '''psspy.dscn(192258)''',
    '''psspy.dscn(192259)''',
    '''no_island()''',
    ],


    # -------------------------------------------
    # IR606: Lewis Mtn
    # -------------------------------------------
    # IR606 trip
    'IR606-site':[
    '''psspy.dscn(199761)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199762)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199763)''',      # IR606: Lewis Mtn
    '''psspy.dscn(199764)''',      # IR606: Lewis Mtn
    ],

    # 2C-L6537
    '2C-L6537':[
    #'''psspy.dscn(199057)'''       # Disconnects 67C
    '''psspy.branch_data(199051,199057,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''
    ],

    # 5S-L6537
    '5S-L6537':[
    '''psspy.branch_data(199031,199760,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''
    ],

    # 2C-B61
    '2C-B61':[
    #'''psspy.branch_data(199031,199760,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',     # Removed for IR602
    '''psspy.branch_data(199051,199057,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
    '''psspy.two_winding_chng_6(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)''',
    '''psspy.branch_data(199051,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''
    ],

    # 2C-B62
    '2C-B62':[
    '''psspy.branch_data(199051,199052,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',   # L6517
    '''psspy.load_chng_5(199051,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',    # 2C-T61
    '''psspy.dscn(199063)''',    # L6516
    '''psspy.dscn(199056)''',    # L6516
    '''psspy.dscn(199070)''',    # L6516
    '''psspy.dscn(199075)''',    # L6515
    ],
}
    #    return contingency
