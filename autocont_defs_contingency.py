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
#
#   2024/08/22: PVH
#   IR671 contingencies to reflect 101V-MacDonald Pond POI. 
#


def_contingencies = {
# ----------
# 88S-Lingan
# ----------
                   '88S_L-7014':['''psspy.branch_chng(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

		   '88S_L-7021':['''psspy.branch_chng(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
				   
		   '88S_L-7022':['''psspy.branch_chng(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   # 88S-710 trips 88S-GT3 and 88S-T71
                   '88S-710':['''psspy.dscn(199003)''',
                              '''psspy.two_winding_chng_4(199000,199005,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""88S-T71""",_s])''',],
                   # 88S-711 trips 88S-T71 and 88S-GT1
                   '88S-711':['''psspy.two_winding_chng_4(199000,199005,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""88S-T71""",_s])''',
                              '''psspy.dscn(199001)'''],
                   # 88S-712 trips 88S-L-7021 and 88S-GT1
                   '88S-712':['''psspy.branch_chng(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.dscn(199001)''',],  
                   # 88S-713 trips 88S-T72 and L-7021
                   '88S-713':['''psspy.branch_chng(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199000,199006,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""88S-T72""",_s])''',],
                   # 88S-714 trips 88S-T72 and 88S-GT2
                   '88S-714':['''psspy.dscn(199002)''',
                              '''psspy.two_winding_chng_4(199000,199006,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""88S-T72""",_s])''',],
                   # 88S-715 trips 88S-T71 and 88S-GT2
                   '88S-715':['''psspy.dscn(199002)''',
                              '''psspy.two_winding_chng_4(199000,199005,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""88S-T71""",_s])'''],
                   # 88S-720 trips 88S-T72 and L-7014           
                   '88S-720':['''psspy.two_winding_chng_4(199000,199006,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""88S-T72""",_s])''',
                              '''psspy.branch_chng(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 88S-721 trips 88S-GT4 and 88S-GT3
                   '88S-721':['''psspy.dscn(199003)''',
                              '''psspy.dscn(199004)''',],
                   # 88S-722 trips L-7022 and 88S-GT4
                   '88S-722':['''psspy.dscn(199004)''',
                              '''psspy.branch_chng(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 88S-723 trips L-7014 and L-7022
                   '88S-723_G0':['''psspy.branch_chng(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.branch_chng(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 88S-723 trips L-7014 and L-7022
		   '88S-723_G8':['''psspy.branch_chng(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.branch_chng(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
				 '''psspy.dscn(199002)''',],

                   '88S-T71':['''psspy.dscn(199005)'''],
				   
		   '88S-T72':['''psspy.dscn(199006)'''],
				   
		   '88S-G2':['''psspy.dscn(199002)'''],
				   
		   '88S-G3':['''psspy.dscn(199003)'''],
				   
		   '88S-G4':['''psspy.dscn(199004)'''],
# -------------
# 101S-Woodbine
# -------------
                   '101S_ML-POLE1':['''psspy.dscn(199855)''',
                                    '''psspy.shunt_chng(199045,r"""2""",0,[_f,_f])'''],

                   '101S_ML-POLE2':['''psspy.dscn(199857)''',
                                    '''psspy.shunt_chng(199045,r"""3""",0,[_f,_f])'''],

                   '101S_ML-BIPOLE':['''psspy.dscn(199855)''',
                                     '''psspy.shunt_chng(199045,r"""2""",0,[_f,_f])''',
                                     '''psspy.fdns([0,0,0,1,1,0,99,0])''',
				     '''psspy.fdns([0,0,0,1,1,0,99,0])''',
				     '''psspy.dscn(199857)''',
                                     '''psspy.shunt_chng(199045,r"""3""",0,[_f,_f])''',
                                     '''psspy.shunt_chng(199042, '2', intgar1 = 0)''',
                                     '''psspy.shunt_chng(199042, '3', intgar1 = 0)''',],

                   '101S-T81':['''psspy.two_winding_chng_4(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T81""",_s])''',],

		   '101S-T82':['''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',],

                   '101S_L-7011':['''psspy.branch_chng(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '101S_L-7011_G1':['''psspy.branch_chng(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                     '''sps('G5')''',],
				   
                   '101S_L-7012':['''psspy.branch_chng(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
		   '101S_L-7012_G2':['''psspy.branch_chng(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                     '''sps('G5')''',],
                   
                   '101S_L-7015':['''psspy.branch_chng(199042,199044,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.dscn(199044)''',
                                  '''psspy.dscn(199043)''',],

                   '101S_L-8004_G0':['''psspy.branch_chng(199045,199120,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
				   
		   '101S_L-8004_G5':['''psspy.branch_chng(199045,199120,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
				     '''sps('G5')''',],

		   '101S_L-8004_G6':['''psspy.branch_chng(199045,199120,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
				     '''sps('G6')'''],
				   
                   # 101S-701 trips L-7012 and 101S-T81
                   '101S-701':['''psspy.two_winding_chng_4(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T81""",_s])''',
                               '''psspy.branch_chng(199050,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 101S-702 trips L-7012 and L-7014
                   '101S-702':['''psspy.branch_chng(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.branch_chng(199050,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 101S-703 trips 101S-T82 and L-7014
                   '101S-703':['''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',
                               '''psspy.branch_chng(199000,199042,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 101S-704 trips 101S-T82 and L-7011
                   '101S-704':['''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',
                               '''psspy.branch_chng(199050,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 101S-705 trips L-7022 and L-7011
                   '101S-705':['''psspy.branch_chng(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.branch_chng(199050,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 101S-706 trips 101S-T81 and L-7022
		   '101S-706':['''psspy.branch_chng(199000,199042,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.two_winding_chng_4(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T81""",_s])''',],
                   # 101S-711 trips 101S-T81 and L-7021
                   '101S-711':['''psspy.branch_chng(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.two_winding_chng_4(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T81""",_s])''',],
                   # 101S-712 trips L-7021 and L-7015
                   '101S-712':['''psspy.branch_chng(199000,199042,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.dscn(199044)''',
                               '''psspy.dscn(199043)''',],
                   # 101S-713 trips 101S-T82 and L-7015
                   '101S-713':['''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',
                               '''psspy.dscn(199044)''',
			       '''psspy.dscn(199043)''',],
                   # 101S-811 trips 101S-T81 and ML Pole 1
		   '101S-811':['''psspy.two_winding_chng_4(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T81""",_s])''',
                               '''psspy.dscn(199855)''',
                               '''psspy.shunt_chng(199045,r"""2""",0,[_f,_f])'''],
                   # 101S-812 trips L-8004 and ML Pole 1
		   '101S-812_G0':['''psspy.dscn(199855)''',
                                  '''psspy.branch_chng(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.shunt_chng(199045,r"""2""",0,[_f,_f])'''],
                   # 101S-812 trips L-8004 and ML Pole 1
		   '101S-812_G5':['''psspy.branch_chng(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''sps('G5')''',
                                  '''psspy.dscn(199855)''',
                                  '''psspy.shunt_chng(199045,r"""2""",0,[_f,_f])''',],
                   # 101S-812 trips L-8004 and ML Pole 1
		   '101S-812_G6':['''psspy.branch_chng(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''sps('G6')''',
                                  '''psspy.dscn(199855)''',
                                  '''psspy.shunt_chng(199045,r"""2""",0,[_f,_f])''',],
                   # 101S-813 trips L-8004 and 101S-T82
		   '101S-813_G0':['''psspy.branch_chng(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',],
                   # 101S-813 trips L-8004 and 101S-T82
		   '101S-813_G5':['''psspy.branch_chng(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',
				  '''sps('G5')''',],
                   # 101S-813 trips L-8004 and 101S-T82
		   '101S-813_G6':['''psspy.branch_chng(199120,199045,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',
				  '''sps('G6')''',],
                   # 101S-814 trips ML Pole 2 and 101S-T82
		   '101S-814':['''psspy.dscn(199857)''',
                               '''psspy.shunt_chng(199045,r"""3""",0,[_f,_f])''',
                               '''psspy.two_winding_chng_4(199042,199045,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T82""",_s])''',],
                   # 101S-816 trips ML Pole 2 and 101S-T81
		   '101S-816':['''psspy.dscn(199857)''',
                               '''psspy.shunt_chng(199045,r"""3""",0,[_f,_f])''',
                               '''psspy.two_winding_chng_4(199042,199045,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""101S-T81""",_s])''',],
                
# ------------------
# 3C-Port Hastings
# ------------------
                   '3C_L-7003':['''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '3C_L-7004':['''psspy.branch_chng(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '3C_L-7005_G0':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

		   '3C_L-7005_G3':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
				   '''sps('G3')''',],
				   
                   '3C-T71':['''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',],
                   '3C-L6543':['''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',],#Same as 3C T71

                   '3C-T72':['''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',],

                   # 3C-710 trips L-7005 and 3C-T71
                   '3C-710_G0':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',],
                   # 3C-710 trips L-7005 and 3C-T71 - G3 armed in some cases
		   '3C-710_G3':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',
				'''sps('G3')''',],
		   # 3C-711 trips L-7011 and 3C-T71
                   '3C-711':['''psspy.branch_chng(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',],
                   # 3C-712 trips L-7003 and L-7011
                   '3C-712':['''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.branch_chng(199042,199050,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 3C-713 trips L-7003 and 3C-T72
                   '3C-713':['''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',],
                   # 3C-714 trips L-7012 and 3C-T72
                   '3C-714':['''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',
                             '''psspy.branch_chng(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 3C-715 trips L-7004 and L-7012
                   '3C-715':['''psspy.branch_chng(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.branch_chng(199042,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 3C-716 trips L-7004 and 3C-T71
                   '3C-716':['''psspy.branch_chng(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',],
                   # 3C-720 trips L-7005, 3C-T72, L-6548
                   '3C-720_G0':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',],

                   # 3C-720 trips L-7005, 3C-T72, L-6548; G3 armed in some cases
                   '3C-720_G3':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',
                                '''sps('G3')''',],


                   
# ------------
# 2C-Hastings			   
# ------------  
                   '2C_L-6515':['''psspy.dscn(199075)''',],

                   '2C_L-6516':['''psspy.dscn(199063)''',
                                '''psspy.dscn(199056)''',
                                '''psspy.dscn(199070)''',],
                   
                   '2C_L-6517':['''psspy.branch_chng(199051,199052,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   '2C_L-6518':['''psspy.branch_chng(199051,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   '2C_L-6523':['''psspy.branch_chng(199052,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '2C_L-6537':['''psspy.dscn(199033)''',
                                '''psspy.dscn(199057)''',
                                '''psspy.dscn(199058)''',
                                '''psspy.dscn(199066)''',
                                '''psspy.dscn(199067)''',
                                '''psspy.dscn(199068)''',
                                '''psspy.dscn(199069)''', ],
                                      
                   '2C_B61':['''psspy.dscn(199033)''',
                             '''psspy.dscn(199057)''',
                             '''psspy.dscn(199058)''',
                             '''psspy.dscn(199066)''',
                             '''psspy.dscn(199067)''',
                             '''psspy.dscn(199068)''',
                             '''psspy.dscn(199069)''',
                             '''psspy.branch_chng(199051,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                             '''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',],

                   '2C_B61_SPS':['''psspy.dscn(199033)''',
                                 '''psspy.dscn(199057)''',
                                 '''psspy.dscn(199058)''',
                                 '''psspy.dscn(199066)''',
                                 '''psspy.dscn(199067)''',
                                 '''psspy.dscn(199068)''',
                                 '''psspy.dscn(199069)''',
                                 '''psspy.branch_chng(199051,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                                 '''psspy.two_winding_chng_4(199050,199051,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T71""",_s])''',
                                 #85S-WRECK COVE HYDRO GT1
                                 '''psspy.dscn(199036)''',
                                 #L6538
                                 '''psspy.branch_chng(199025,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 #No ISLAND
                                 '''psspy.dscn(199031)''',
                                 '''psspy.dscn(199035)''',
                                 '''no_island()''',],
                   
                   '2C_B62':['''psspy.branch_chng(199051,199075,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6515
                             '''psspy.branch_chng(199051,199063,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6516
                             '''psspy.branch_chng(199051,199052,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6517   
                             '''psspy.load_chng_5(199051,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',           
                             '''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',],

                   #WC L6538 O/L: where L-6538>=114MVA: after 6 minutes, trip a pre-selected Wreck Cove unit; after 6.5 minutes, trip L-6538 breaker at 5S; alarm reset at 94MVA
                   '2C_L-6537_SPS':[
                                #L6537
                                '''psspy.dscn(199033)''',
                                '''psspy.dscn(199057)''',
                                '''psspy.dscn(199058)''',
                                '''psspy.dscn(199066)''',
                                '''psspy.dscn(199067)''',
                                '''psspy.dscn(199068)''',
                                '''psspy.dscn(199069)''',
                                #85S-WRECK COVE HYDRO GT1
                                '''psspy.dscn(199036)''',
                                #L6538
                                '''psspy.branch_chng(199025,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                #No ISLAND
                                '''psspy.dscn(199031)''',
                                '''psspy.dscn(199035)''',
                                '''no_island()''',],

                   '2C_B62_SPS':[
                            #L6515
                            '''psspy.dscn(199075)''',
                            #L6516
                            '''psspy.dscn(199063)''',
                            '''psspy.dscn(199056)''',
                            '''psspy.dscn(199070)''',
                            #L6517
                            '''psspy.branch_chng(199051,199052,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            #2C-T61
                            '''psspy.load_chng_5(199051,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                            #3C-T72
                            '''psspy.two_winding_chng_4(199050,199051,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""3C-T72""",_s])''',

                            #85S-WRECK COVE HYDRO GT1
                            '''psspy.dscn(199036)''',
                            #L6538
                            '''psspy.branch_chng(199025,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            #No ISLAND
                            '''psspy.dscn(199031)''',
                            '''psspy.dscn(199035)''',
                            '''no_island()''',],
                   
# ------------
# 47C-Port Hawkesbury Paper		   
# ------------                     
                   # 47C-B1 trips L-6523 and 48C-G1
                   '47C_B1':['''psspy.branch_chng(199052,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.dscn(199072)''',],
                   # 47C-B2 trips 47C T68 and 47C T66
                   '47C_B2':['''psspy.dscn(199072)''',
                             '''psspy.dscn(199064)''',],
                   # 47C-B3 trips 47C T65 and 47C T66
                   '47C_B3':['''psspy.dscn(199062)''',
                             '''psspy.dscn(199064)''',],
                   # 47C-B4 trips 47C T65 and 47C T64
                   '47C_B4':['''psspy.dscn(199061)''',
                             '''psspy.dscn(199062)''',],
                   # 47C-B5 trips 47C T63 and 47C T64
                   '47C_B5':['''psspy.dscn(199061)''',
                             '''psspy.dscn(199060)''',],
                   # 47C-B6 trips 47C T63 and L-6518
                   '47C_B6':['''psspy.branch_chng(199051,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.dscn(199060)''',],
                   # 47C-B7 trips 47C T67 and L-6518
                   '47C_B7':['''psspy.branch_chng(199051,199053,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.dscn(199065)''',],
                   
# ------------
# 4C-Lochaber			   
# ------------  
                   '4C_L-6552':['''psspy.branch_chng(199076,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   
                   '4C_T63':['''psspy.load_chng_5(199076,r"""61""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""62""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""63""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""64""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""65""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""66""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   '4C_T2':['''psspy.two_winding_chng_4(199076,199077,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""4C-T2""",_s])''',
                            '''no_island()''',],
                  
                   '4C_620':['''psspy.branch_chng(199076,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""61""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""62""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""63""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""64""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""65""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""66""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   '4C_621':['''psspy.dscn(199075)''',
                             '''psspy.load_chng_5(199076,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""61""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""62""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""63""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',  
                             '''psspy.load_chng_5(199076,r"""64""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""65""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199076,r"""66""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   '4C_622':['''psspy.dscn(199075)''',
                             '''psspy.two_winding_chng_4(199076,199077,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""4C-T2""",_s])''',
                             '''no_island()''',],   
                   
                   '4C_623':['''psspy.branch_chng(199076,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.two_winding_chng_4(199076,199077,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""4C-T2""",_s])''',
                             '''no_island()''',],   
                   
# ------------
# 79N-Hopewell			   
# ------------   
                   '79N_L-8003_G0':['''psspy.branch_chng(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

		   '79N_L-8003_G5':['''psspy.branch_chng(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
				    '''sps('G5')''',],

		   '79N_L-8003_G6':['''psspy.branch_chng(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
				    '''sps('G6')''',],
				   
                   '79N_L-6507':['''psspy.dscn(199695)''',],

                   '79N_L-6508':['''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   #'79N_L-6508':['''psspy.dscn(199963)''',],
                   
                   '79N-T81_G0':['''psspy.dscn(199121)''',
                                 '''psspy.dscn(199120)''',],

		   '79N-T81_G5':['''psspy.dscn(199121)''',
                                 '''psspy.dscn(199120)''',
				 '''sps('G5')''',],
				   
		   '79N-T81_G6':['''psspy.dscn(199121)''',
                         '''psspy.dscn(199120)''',
				 '''sps('G6')''',],
                   
                   # SAME AS 79N-T81! 
                   # 79N-803 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
                   # 79N-810 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
                   # 79N-601 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
                   # 79N-606 trips L-8003, L-8004, L-6507, L-6508 and 79N-T81
                   # 79N-B61
                   # 79N-B81

        
# ----------
# 67N-Onslow				   
# ----------	   
                   '67N_L-8001_G0':['''psspy.dscn(190381)''',],
				   
		   '67N_L-8001_NSX1':['''psspy.dscn(190381)''',
				      '''sps('NSX1')''',],
				   
		   '67N_L-8001_NSX2':['''psspy.dscn(190381)''',
				      '''sps('NSX2')''',],

                   #67N-L7018 SAME AS 120H-L7018

                   #G10 NSI: where NB Tie flow -100MW: cross trip 1N-613 (opens L-6613 at 1N)
		   '67N_L-8001_NSI':[
                                   #67N-L8001
                                   '''psspy.dscn(190381)''',
                                   #1N-613
                                   '''psspy.branch_chng(199110,199134,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                   ],

                   '67N_L-8002':['''psspy.branch_chng(199125,199195,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '67N_L-7019':['''psspy.branch_chng(199130,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '67N_L-7001':['''psspy.branch_chng(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '67N_L-7002':['''psspy.branch_chng(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '67N-T81':['''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',],

                   '67N-T82':['''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',],

                   '67N-T71':['''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''',],
                   #67N-L6527 same as 67N-T71
                   '67N-L6527':['''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''',],
                   
                   # 67N-811 trips L-8003 and 67N-T82
                   '67N-811_G0':['''psspy.branch_chng(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                                 '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                                 '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
                                 ],
                   # 67N-811 trips L-8003 and 67N-T82
		   '67N-811_G5':['''psspy.branch_chng(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                                 '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                                 '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
				 '''sps('G5')''',],
                   # 67N-811 trips L-8003 and 67N-T82
		   '67N-811_G6':['''psspy.branch_chng(199120,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                                 '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                                 '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
				 '''sps('G6')''',],
                   # 67N-812 trips L-8002 and 67N-T82
		   '67N-812':['''psspy.branch_chng(199195,199125,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                              '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                              '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
                              ],  
                   # 67N-813 trips L-8002 and 67N-T81
                   '67N-813':['''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                              '''psspy.branch_chng(199125,199195,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                              '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
                              ],
                   # 67N-814 trips L-8001 and 67N-T81
                   '67N-814_G0':['''psspy.dscn(190381)''',
                                 '''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                                 '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                                 '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
                                 ],
                   # 67N-814 trips L-8001 and 67N-T81
		   '67N-814_NSX1':['''psspy.dscn(190381)''',
                                   '''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                                   '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                                   '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
				   '''sps('NSX1')''',],
                   # 67N-814 trips L-8001 and 67N-T81
		   '67N-814_NSX2':['''psspy.dscn(190381)''',
                                   '''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                                   '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                                   '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
				   '''sps('NSX2')''',],
                   # 67N-814 trips L-8001 and 67N-T81
		   '67N-814_NSI':[
                                   #67N-814
                                   '''psspy.dscn(190381)''',
                                   '''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                                   '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                                   '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
                                   #1N-613
                                   #1N-613
                                   '''psspy.branch_chng(199110,199134,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                   ],
                   
                   # 67N-815 trips L-8001 and [empty node]
                   # SAME AS L-8001
                   
                   # 67N-701 trips L-7002 and 67N-T71
                   '67N-701':['''psspy.branch_chng(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''',],
                   # 67N-702 trips L-7002 and L-7003
                   '67N-702':['''psspy.branch_chng(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 67N-703 trips L-7003 and 67N-T81
                   '67N-703':['''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199130,199125,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                              '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                              '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
                              ],
                   # 67N-704 trips L-7001 and 67N-T81
                   '67N-704':['''psspy.branch_chng(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                              '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                              '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
                              ],
                   # 67N-705 trips L-7001 and L-7019
                   '67N-705':['''psspy.branch_chng(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.branch_chng(199130,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 67N-706 trips L-7019 and 67N-T71
                   '67N-706':['''psspy.branch_chng(199130,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''',],
                   # 67N-710 trips 67N-T82 and 67N-T71
                   '67N-710':['''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                              '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                              '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
                              '''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''',],
                   # 67N-711 trips L-7005 and 67N-T82
                   '67N-711_G0':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                                 '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                                 '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
                              ],
                   # 67N-711 trips L-7005 and 67N-T82
		   '67N-711_G3':['''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                 '''psspy.two_winding_chng_4(199125,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T82""",_s])''',
                                 '''psspy.shunt_chng(199130,r"""4""",0,[_f,_f])''', #67N-R321
                                 '''psspy.shunt_chng(199130,r"""5""",0,[_f,_f])''', #67N-R322
				 '''sps('G3')''',],
                   # 67N-712 trips L-7005 and L-7018
                   '67N-712':['''psspy.branch_chng(199200,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.branch_chng(199050,199130,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 67N-713 trips 67N-T81 and L-7018
                   '67N-713':['''psspy.branch_chng(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199125,199130,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T81""",_s])''',
                              '''psspy.shunt_chng(199130,r"""2""",0,[_f,_f])''', #67N-R311
                              '''psspy.shunt_chng(199130,r"""3""",0,[_f,_f])''', #67N-R312
                              ],
# ---------
# 1N-Onslow
# ---------
                   '1N_L-6613':['''psspy.dscn(199134)''',],

                   '1N_L-6503':['''psspy.dscn(199100)''',],

                   #L6001, 82V-600
                   '1N_L-6001':['''psspy.dscn(199154)''',
                                '''psspy.dscn(199156)''',
                                # '''psspy.dscn(199159)''',
                                '''psspy.dscn(199155)''',],
                   '82V-600':['''psspy.dscn(199154)''',
                                '''psspy.dscn(199156)''',
                                # '''psspy.dscn(199159)''',
                                '''psspy.dscn(199155)''',],

                   '1N-T1':['''psspy.dscn(199584)''',
                            '''psspy.dscn(199583)''',
                            '''psspy.dscn(199582)''',
                            '''psspy.dscn(199581)''',
                            '''psspy.dscn(199580)''',
                            '''psspy.dscn(199118)''',
                            '''psspy.dscn(199116)''',
                            '''psspy.dscn(199115)''',
                            '''psspy.dscn(199111)''',
                            '''psspy.dscn(199696)''',],

                   '1N-T4':['''psspy.dscn(199112)''',
                            '''psspy.dscn(199114)''',],

                   '1N-T65':['''psspy.load_chng_5(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',],

                   '1N-C61':['''psspy.shunt_chng(199110,r"""2""",0,[_f,_f])''',],

                   '1N-B61':['''psspy.shunt_chng(199110,r"""2""",0,[_f,_f])''',
			     '''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''',
			     '''psspy.two_winding_chng_4(199110,199112,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""1N-T4""",_s])''',
			     '''psspy.branch_chng(199110,199154,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                 #'''psspy.branch_chng(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
			     '''psspy.dscn(199112)''',
                             '''psspy.dscn(199114)''',],

                   '1N-B62':['''psspy.load_chng_5(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
                             '''psspy.two_winding_chng_4(199110,199111,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""1N-T1""",_s])''',
                             '''psspy.branch_chng(199110,199134,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.branch_chng(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.dscn(199696)''',
                             '''psspy.dscn(199584)''',
                             '''psspy.dscn(199583)''',
                             '''psspy.dscn(199582)''',
                             '''psspy.dscn(199581)''',
                             '''psspy.dscn(199580)''',
                             '''psspy.dscn(199118)''',
                             '''psspy.dscn(199116)''',
                             '''psspy.dscn(199115)''',
                             '''psspy.dscn(199111)''',],
##                   '1N-B62_IR663':[
##                             '''psspy.load_chng_5(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
##                             '''psspy.two_winding_chng_4(199110,199111,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""1N-T1""",_s])''',
##                             '''psspy.branch_chng(199110,199134,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
##                             #'''psspy.branch_chng(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
##                             '''psspy.dscn(199696)''',
##                             '''psspy.dscn(199584)''',
##                             '''psspy.dscn(199583)''',
##                             '''psspy.dscn(199582)''',
##                             '''psspy.dscn(199581)''',
##                             '''psspy.dscn(199580)''',
##                             '''psspy.dscn(199118)''',
##                             '''psspy.dscn(199116)''',
##                             '''psspy.dscn(199115)''',
##                             '''psspy.dscn(199111)''',
##                             #IR663
##                             '''psspy.dscn(199843)''',
##                             '''psspy.dscn(199844)''',
##                             '''psspy.dscn(199845)''',
##                             ],

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
                             '''psspy.dscn(199696)''',
##                             #IR663
##                             '''psspy.dscn(199843)''',
##                             '''psspy.dscn(199844)''',
##                             '''psspy.dscn(199845)''',
                             ],

                   '1N-601':[
                             '''psspy.dscn(199156)''',#L6001
                             '''psspy.dscn(199154)''',#L6001
                             '''psspy.dscn(199155)''',#L6001
                             '''psspy.two_winding_chng_4(199110,199112,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""1N-T4""",_s])''', #T4
                             '''psspy.dscn(199112)''',#T4
                             '''psspy.dscn(199114)''',#T4
                             '''psspy.two_winding_chng_4(199110,199130,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""67N-T71""",_s])''', #T71
                             '''psspy.shunt_chng(199110,r"""2""",0,[_f,_f])''',#C61
                             #'''psspy.branch_chng(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6503
                            ],

                   '1N-613':['''psspy.dscn(199134)''',
                             '''psspy.branch_chng(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.load_chng_5(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
                             '''psspy.dscn(199696)''',
                             '''psspy.dscn(199696)''',
                             '''psspy.dscn(199584)''',
                             '''psspy.dscn(199583)''',
                             '''psspy.dscn(199582)''',
                             '''psspy.dscn(199581)''',
                             '''psspy.dscn(199580)''',
                             '''psspy.dscn(199118)''',
                             '''psspy.dscn(199116)''',
                             '''psspy.dscn(199115)''',
                             '''psspy.dscn(199111)''',],
##                   '1N-613_IR663':[
##                             '''psspy.dscn(199134)''',
##                             #'''psspy.branch_chng(199110,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
##                             '''psspy.load_chng_5(199110,r"""1""",[0,_i,_i,_i,1],[_f,_f,_f,_f,_f,_f])''',
##                             '''psspy.dscn(199696)''',
##                             #'''psspy.dscn(199696)''',
##                             '''psspy.dscn(199584)''',
##                             '''psspy.dscn(199583)''',
##                             '''psspy.dscn(199582)''',
##                             '''psspy.dscn(199581)''',
##                             '''psspy.dscn(199580)''',
##                             '''psspy.dscn(199118)''',
##                             '''psspy.dscn(199116)''',
##                             '''psspy.dscn(199115)''',
##                             '''psspy.dscn(199111)''',
##                             #IR663
##                             '''psspy.dscn(199843)''',
##                             '''psspy.dscn(199844)''',
##                             '''psspy.dscn(199845)''',
##                             ],

# ----------------
# 50N- Trenton
# ----------------	

                   '50N-l5500':['''psspy.dscn(199092)''',],

                   '50N-l5501':['''psspy.dscn(199094)''', '''no_island()''',],
                        
                   '50N-l5502':['''psspy.dscn(199102)''', '''no_island()''',],

                   '50N-l6503':['''psspy.dscn(199100)''',],

                   '50N-l6511':['''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '50N-l6507':['''psspy.dscn(199695)''',],

                   '50N-l6508':['''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '50N-GT6':['''psspy.dscn(199086)''',],
                        
                   '50N-GT5':['''psspy.dscn(199085)''',],
                        
                   '50N-T12':['''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',],
                       
                   '50N-T8':['''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',],

                   '50N-LOAD1':['''psspy.load_chng_5(199091,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '50N-LOAD2':['''psspy.load_chng_5(199091,r"""2""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # 50N-614, 50N-621, 50N-606, 50N-666
                   '50N-614':[
                        # L-6511
                        '''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6507
                        '''psspy.dscn(199695)''',
                        # GT6
                        '''psspy.dscn(199085)''',
                        # T8 (open circuit except out in 606)
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                   ],
                   '50N-621':[
                        # L-6511
                        '''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6507
                        '''psspy.dscn(199695)''',
                        # GT6
                        '''psspy.dscn(199085)''',
                        # T8 (open circuit except out in 606)
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                   ],
                   '50N-606':[
                        # L-6511
                        '''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6507
                        '''psspy.dscn(199695)''',
                        # GT6
                        '''psspy.dscn(199085)''',
                        # T8 (open circuit except out in 606)
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                   ],
                   '50N-666':[
                        # L-6511
                        '''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6507
                        '''psspy.dscn(199695)''',
                        # GT6
                        '''psspy.dscn(199085)''',
                        # T8 (open circuit except out in 606)
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                   ],
                   

                   # 50N-607, 50N-622, 50N-612, 50N-601
                   '50N-607':[
                        # L-6503
                        '''psspy.dscn(199100)''',
                        # L-6508
                        '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT5
                        '''psspy.dscn(199085)''',
                        # T12 (open circuit except out in 506)
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                   ],
                   '50N-622':[
                        # L-6503
                        '''psspy.dscn(199100)''',
                        # L-6508
                        '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT5
                        '''psspy.dscn(199085)''',
                        # T12 (open circuit except out in 506)
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                   ],
                   '50N-612':[
                        # L-6503
                        '''psspy.dscn(199100)''',
                        # L-6508
                        '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT5
                        '''psspy.dscn(199085)''',
                        # T12 (open circuit except out in 506)
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                   ],
                   '50N-601':[
                        # L-6503
                        '''psspy.dscn(199100)''',
                        # L-6508
                        '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT5
                        '''psspy.dscn(199085)''',
                        # T12 (open circuit except out in 506)
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                   ],

                   # 50N-604
                   '50N-604':[
                        # L-6511
                        '''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6507
                        '''psspy.branch_chng(199090,199695,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT6
                        '''psspy.dscn(199086)''',
                        # T8
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                        # L-6503
                        '''psspy.branch_chng(199090,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6508
                        '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT5
                        '''psspy.dscn(199085)''',
                        # T12 (open circuit except out in 506)
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                        '''no_island()''',
                   ],
                   
                   '50N-B62':[
                        # L-6503
                        '''psspy.branch_chng(199090,199100,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-6508
                        '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # GT5
                        '''psspy.dscn(199085)''',
                        # T12 (open circuit except out in 506)
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                        '''no_island()''',
                   ],

                   # 50N-513, 50N-512, 50N-521
                   '50N-513':[
                        # L-5500
                        '''psspy.dscn(199092)''',
                        # 50N-T12
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                        # L2
                        '''psspy.load_chng_5(199091,r"""2""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '50N-512':[
                        # L-5500
                        '''psspy.dscn(199092)''',
                        # 50N-T12
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                        # L2
                        '''psspy.load_chng_5(199091,r"""2""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '50N-521':[
                        # L-5500
                        '''psspy.dscn(199092)''',
                        # 50N-T12
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                        # L2
                        '''psspy.load_chng_5(199091,r"""2""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],

                   # 50N-508, 50N-522. 50N-511
                   '50N-508':[
                        # L-5501
                        '''psspy.dscn(199094)''', '''no_island()''',
                        # L-5502
                        '''psspy.dscn(199102)''', '''no_island()''',
                        # T8
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                        # L1
                        '''psspy.load_chng_5(199091,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '50N-522':[
                        # L-5501
                        '''psspy.dscn(199094)''', '''no_island()''',
                        # L-5502
                        '''psspy.dscn(199102)''', '''no_island()''',
                        # T8
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                        # L1
                        '''psspy.load_chng_5(199091,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '50N-511':[
                        # L-5501
                        '''psspy.dscn(199094)''', '''no_island()''',
                        # L-5502
                        '''psspy.dscn(199102)''', '''no_island()''',
                        # T8
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                        # L1
                        '''psspy.load_chng_5(199091,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],

                   # 50N-500
                   '50N-500':[
                        # L-5500
                        '''psspy.dscn(199092)''',
                        # 50N-T12
                        '''psspy.two_winding_chng_4(199090,199091,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T12""",_s])''',
                        # L2
                        '''psspy.load_chng_5(199091,r"""2""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                        # L-5501
                        '''psspy.dscn(199094)''', '''no_island()''',
                        # L-5502
                        '''psspy.dscn(199102)''', '''no_island()''',
                        # T8
                        '''psspy.two_winding_chng_4(199090,199091,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50N-T8""",_s])''',
                        # L1
                        '''psspy.load_chng_5(199091,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                        '''no_island()''',
                   ],


# ----------------
# 120H-Brushy Hill
# ----------------			   
                   '120H_L-7008':['''psspy.branch_chng(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '120H_L-7009':['''psspy.branch_chng(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '120H_L-6005':['''psspy.dscn(199203)''',],

                   '120H_L-6010':['''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '120H_L-6011':['''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # '120H_L-6051':['''psspy.branch_chng(199201,199300,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   '120H, Open L-6051':['''psspy.branch_chng(199201,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '120H, L-6051':['''psspy.dscn(199800)''',
                                   '''psspy.dscn(199801)''',
                                   '''psspy.dscn(199802)''',
                                   '''psspy.dscn(199803)''',
                                   '''psspy.dscn(199804)''',],

                   '120H_L-6016':['''psspy.dscn(199208)''',
                                  '''psspy.dscn(199209)''',],

                   '120H-T71':['''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',],
                   #120H-B61 trips 120H-T71
		   #SAME AS 120H-T71
                   '120H-B61':['''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',],

                   '120H-T72':['''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',],

                   '120H-SVC':['''psspy.dscn(199202)''',],
                   
                   '120H_L-7018':['''psspy.branch_chng(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-710 trips L-7018 and 120H-T71
                   '120H-710':['''psspy.branch_chng(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',],
                   # 120H-711 trips L-7002 and 120H-T71
                   '120H-711':['''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',
                               '''psspy.branch_chng(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-712 trips L-7002 and L-7009
                   '120H-712':['''psspy.branch_chng(199130,199200,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.branch_chng(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-713 trips L-7009 and 120H-T72
                   '120H-713':['''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',
                               '''psspy.branch_chng(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-714 trips L-7001 and 120H-T72
                   '120H-714':['''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',
                               '''psspy.branch_chng(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-715 trips L-7001 and L-7008
                   '120H-715':['''psspy.branch_chng(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.branch_chng(199130,199200,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-716 trips L-7008 and 120H-T71
                   '120H-716':['''psspy.branch_chng(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',],
                   # 120H-720 trips L-7018 and 120H-T72
                   '120H-720':['''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',
                               '''psspy.branch_chng(199130,199200,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-621 trips L-6005 and 120H-T71
                   '120H-621':['''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',
                               '''psspy.dscn(199203)''',],
                   # 120H-622 trips L-6005 and L-6016B
                   '120H-622':['''psspy.dscn(199203)''',
                               '''psspy.dscn(199208)''',
                               '''no_island()''',],
                   # 120H-623 trips L-6016B and 120H-T72
                   '120H-623':['''psspy.dscn(199208)''',
                               '''no_island()''',
                               '''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',],
                   # 120H-624 trips L-6010 and 120H-T72
                   '120H-624':['''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',
                               '''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-625 trips L-6010 and L-6011
                   '120H-625':['''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 120H-626 trips L-6011 and 120H-T71
                   '120H-626':['''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',],
                   # 120H-627 trips L-6051 and 120H-T71
                   '120H-627':['''psspy.dscn(199800)''',
                               '''psspy.dscn(199801)''',
                               '''psspy.dscn(199802)''',
                               '''psspy.dscn(199803)''',
                               '''psspy.dscn(199804)''',#L-6051
                               '''psspy.two_winding_chng_4(199200,199201,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T71""",_s])''',],
                   # 120H-628 trips L-6051 and 120H-SVC
                   '120H-628':['''psspy.dscn(199800)''',
                               '''psspy.dscn(199801)''',
                               '''psspy.dscn(199802)''',
                               '''psspy.dscn(199803)''',
                               '''psspy.dscn(199804)''',#L-6051
                               '''psspy.dscn(199202)''',],
                   # 120H-629 trips 120H-SVC and 120H-T72
                   '120H-629':['''psspy.dscn(199202)''',
                               '''psspy.two_winding_chng_4(199200,199201,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""120H-T72""",_s])''',],
                   
# -------------
# 90H - SACKVILLE
# -------------

                   '90H-L6002-1':['''psspy.dscn(199204)''', '''no_island()''',],

                   # NS_L6009-2
                   '90H-L6009-2':['''psspy.branch_chng(199184,199185,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 101H taps off L-6009
                   '90H-L6009':['''psspy.dscn(199185)''', '''no_island()''',],

                   '90H-L-6008':['''psspy.dscn(199697)''', '''no_island()''',],

                   # L-6010, L-6005 handled in 120H

                   # NS_L6003
                   '90H-L6003':['''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # NS_L6004-1 handled in 101V
                   # 'NS_L6004-1':[#'''psspy.branch_chng(199184,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],


                   '90H-L5003-2':['''psspy.dscn(199177)''',],

                   '90H-L5004-1':['''psspy.dscn(199179)''',],

                   '90H-T1':['''psspy.two_winding_chng_4(199178,199184,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""90H-T1""",_s])''',],

                   # 90H-C61, 90H-613
                   '90H-C61':['''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],

                   #90H-C51
                   '90H-C51':['''psspy.shunt_chng(199178,r"""2""",0,[_f,_f])''',],

                   # 90H-611 trips NS_L6009-2, NS_L6008
                   '90H-611':['''psspy.dscn(199185)''',
                              '''psspy.dscn(199697)''', '''no_island()''',],
                              #'''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],

                   # 90H-608 trips NS_L6010, NS_L6005-2
                   '90H-608':['''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.dscn(199203)''',],
                              #'''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],

                   # 90H-605 trips NS_L6003, NS_L6004-1
                   '90H-605':['''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              #'''psspy.branch_chng(199184,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],     # modded
                              '''psspy.dscn(199570)''',                                                                                                 # modded
                              #'''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])'''],

                   # 90H-602 trips 90H-T1, NS_L6002-1
                   '90H-602':['''psspy.two_winding_chng_4(199178,199184,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""90H-T1""",_s])''',
                              '''psspy.dscn(199204)''', '''no_island()''',],
                              #'''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],


                   # 90H-612 trips NS_L6008
                   '90H-612':['''psspy.dscn(199697)''', '''no_island()''',
                              '''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],
                        
                   # 90H-609 trips NS_L6010
                   '90H-609':['''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],
                        
                   # 90H-606 trips NS_L6003, 90H-C61
                   '90H-606':['''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],
                        
                   # 90H-603 trips 90H-T1, 90H-C61, 
                   '90H-603':['''psspy.two_winding_chng_4(199178,199184,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""90H-T1""",_s])''',
                              '''psspy.shunt_chng(199184,r"""2""",0,[_f,_f])''',],


                   # 90H-610 trips NS_L6009-2
                   '90H-610':['''psspy.dscn(199185)''', '''no_island()''',],

                   # 90H-607 trips NS_L6005-2
                   '90H-607':[ '''psspy.dscn(199203)''',],

                   # 90H-604 trips NS_L6004-1
                   '90H-604':[#'''psspy.branch_chng(199184,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],     # modded
                                '''psspy.dscn(199570)'''],                                                                                              # modded

                   # 90H-601 trips NS_L6002-1
                   '90H-601':['''psspy.dscn(199204)''', '''no_island()''',],


                   # 90H-503 trips 90H-T1, 90H-C51
                   '90H-503':['''psspy.two_winding_chng_4(199178,199184,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""90H-T1""",_s])''',
                              '''psspy.dscn(199178)''', 
                              '''no_island()''',],

                   # 90H-502 trips 90H-C51 same as 90H-503


                   # 90H-506
                   '90H-506':['''psspy.dscn(199178)''',
                              '''psspy.dscn(199177)''',
                              '''no_island()''',],

                   # 90H-501 
                   '90H-501':['''psspy.dscn(199178)''',
                              '''psspy.branch_chng(199178,199179,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''no_island()''',],

# -------------
# 103H-Lakeside
# -------------   
                   '103H_L-6008':['''psspy.dscn(199697)''',],

                   '103H_L-6033':['''psspy.dscn(199197)''',],

                   '103H_L-6038':['''psspy.dscn(199192)''',],

                   '103H-T81':['''psspy.two_winding_chng_4(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""103H-T81""",_s])''',],

		   '103H-T61':['''psspy.dscn(199191)''',
                               '''psspy.two_winding_chng_4(199191,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""103H-T61""",_s])''',],

                   '103H-T63':['''psspy.dscn(199205)''',
                               '''psspy.dscn(199196)''',
                               '''psspy.dscn(199180)''',],

                   '103H-B61':['''psspy.two_winding_chng_4(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""103H-T81""",_s])''',
                               '''psspy.branch_chng(199190,199197,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.dscn(199205)''',
                               '''psspy.dscn(199196)''',
                               '''psspy.dscn(199180)''',],

                   '103H-B62':['''psspy.dscn(199191)''',
                               '''psspy.branch_chng(199697,199190,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               '''psspy.dscn(199192)''',
                               '''psspy.branch_chng(199208,199190,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '103H-881':['''psspy.dscn(199195)''',
                               '''psspy.two_winding_chng_4(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""103H-T81""",_s])''',],
                   # 103H-600 trips B-61 and B-62
                   '103H-600':['''psspy.dscn(199205)''',
                               '''psspy.dscn(199196)''',
                               '''psspy.dscn(199180)''',
                               '''psspy.dscn(199191)''',
                               '''psspy.dscn(199192)''',
                               '''psspy.dscn(199190)''',],
                   # 103H-608 trips L-6008 and B-62
                   '103H-608':['''psspy.dscn(199191)''', #T61
                               '''psspy.dscn(199192)''', #L6038
                              '''psspy.branch_chng(199208,199190,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6016
                              '''psspy.dscn(199697)''', #L6008
                              '''psspy.shunt_chng(199190,r"""3""",0,[_f,_f])''',],  #C62
                   # 103H-681 trips B-61 and 103H-T81
                   '103H-681':['''psspy.dscn(199205)''',
                               '''psspy.dscn(199196)''',
                               '''psspy.dscn(199180)''',
                               '''psspy.two_winding_chng_4(199195,199190,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""103H-T81""",_s])''',
                               '''psspy.dscn(199197)''',],
# ---------------
# 89S-Point Aconi
# ---------------  
                   '89S-G1':['''psspy.dscn(199043)''',],
# ---------------
# 91H-Tuft's Cove
# ---------------
                   '91H_L-5049':['''psspy.branch_chng(199166,199170,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '91H_L-5012':['''psspy.dscn(199176)''',
                                 '''psspy.dscn(199175)''',],

                   '91H_L-5041':['''psspy.branch_chng(199166,199170,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '91H-T62':['''psspy.two_winding_chng_4(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',],

                   '91H-T11':['''psspy.two_winding_chng_4(199165,199166,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T11""",_s])''',
                              '''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   # 91H-511 trips B-52 and L-5049
                   '91H-511':['''psspy.branch_chng(199166,199170,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',],
                   # 91H-516 trips B-52 and L-5012
                   '91H-516':['''psspy.dscn(199176)''',
                              '''psspy.dscn(199175)''',
                              '''psspy.two_winding_chng_4(199166,199165,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',],
                   # 91H-521 trips B-52 and L-5041
                   '91H-521':['''psspy.branch_chng(199166,199170,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199166,199165,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',],
                   # 91H-523 trips 91H-T11 and L-5041
                   '91H-523':['''psspy.branch_chng(199166,199170,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.two_winding_chng_4(199166,199165,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T11""",_s])''',
                              '''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',], #L-6003
                   #91H-621 trips 91H-T62 and L6042
                   '91H-621':[
                       '''psspy.branch_chng(199161,199165,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6042
                       '''psspy.two_winding_chng_4(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',#T62
                       ],

                   '91H_L-6042':['''psspy.branch_chng(199161,199165,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   #91H-613 trips 91H-T62, 91H-T64, 91H-T65, 91H-T66
                   '91H-613':[
                       '''psspy.two_winding_chng_4(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',#T62
                       '''psspy.dscn(199181)''', #T64
                       '''psspy.dscn(199182)''', #T65
                       '''psspy.dscn(199164)''', #T66
                       ],

                   #91H-603 trips 91H-T11, L6003
                   #the same as the 91H-T11
                   '91H-603':['''psspy.two_winding_chng_4(199165,199166,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T11""",_s])''',
                              '''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   #91H-604 trips 91H-T62, L6007, L6042
                   '91H-604':[
                       '''psspy.branch_chng(199165,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6007
                       '''psspy.branch_chng(199161,199165,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6042
                       '''psspy.two_winding_chng_4(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',#T62
                       ],

                   '91H_L-6007':['''psspy.branch_chng(199165,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],


                   #91H-605 trips L6040, L6007
                   '91H-605':[
                       '''psspy.branch_chng(199165,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6007
                       '''psspy.dscn(199158)''',
                       '''psspy.dscn(199153)''',#L6040
                       ],

                   #91H-606 trips L6040, L6003, T11
                   '91H-606':[
                       '''psspy.two_winding_chng_4(199165,199166,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T11""",_s])''',#T11
                       '''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6003
                       '''psspy.dscn(199158)''',
                       '''psspy.dscn(199153)''',#L6040
                       ],

                   #91H-607 trips L6014, L6042, T62
                   '91H-607':[
                       '''psspy.branch_chng(199161,199165,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6042
                       '''psspy.two_winding_chng_4(199165,199166,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T62""",_s])''',#T62
                       '''psspy.branch_chng(199165,199198,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6014
                       ],

                   '91H_L-6014':['''psspy.branch_chng(199165,199198,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   #91H-608 trips L6014, GT3
                   '91H-608':[
                       '''psspy.dscn(199169)''', #GT3
                       '''psspy.branch_chng(199165,199198,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6014
                       ],

                   #91H-609 trips GT3, L6003, T11
                   '91H-609':[
                       '''psspy.two_winding_chng_4(199165,199166,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T11""",_s])''',#T11
                       '''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6003
                       '''psspy.dscn(199169)''', #GT3
                       ],

                   #91H-611 trips 91H-T64, 91H-T65, 91H-T66, L6003, T11
                   '91H-611':[
                       '''psspy.two_winding_chng_4(199165,199166,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""91H-T11""",_s])''',#T11
                       '''psspy.branch_chng(199165,199184,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6003
                       '''psspy.dscn(199181)''', #T64
                       '''psspy.dscn(199182)''', #T65
                       '''psspy.dscn(199164)''', #T66
                       ],
          

                   
# ----------------------
# 91N-Dalhousie Mountain
# ----------------------
                   '91N-701':['''psspy.dscn(199590)''',
                              '''psspy.dscn(199591)''',
                              '''psspy.dscn(199592)''',
                              '''psspy.dscn(199593)''',],

                   '91N-702':['''psspy.branch_chng(199590,199130,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.dscn(199591)''',
                              '''psspy.dscn(199592)''',
                              '''psspy.dscn(199593)''',],
         
                   '91N-703':['''psspy.branch_chng(199590,199050,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.dscn(199591)''',
                              '''psspy.dscn(199592)''',
                              '''psspy.dscn(199593)''',],

                   '91N-B71':['''psspy.dscn(199591)''',
                              '''psspy.dscn(199592)''',
                              '''psspy.dscn(199593)''',],
# *********************
# 99W-Bridgewater 230kV
# *********************
                   '99W-708':['''psspy.dscn(199240)''',],
                   
                   '99W-709':['''psspy.dscn(199241)''',],

                   #99W-T71, 99W-B71
                   '99W-T71':['''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',],
                   '99W-B71':['''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',],
                   #99W-T71, 99W-B72
                   '99W-T72':['''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',],
                   '99W-B72':['''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',],
                   
# -------------
# 99W - BRIDGEWATER (ADDITIONAL)
# -------------
                   '99W-L5545-a':['''psspy.dscn(199233)''', '''no_island()''',],

                   '99W-L5546':['''psspy.dscn(199232)''',],

                   '99W-L6531':['''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '99W-L6006':['''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '99W-L6025':['''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   #L-6002-6
                   '99W-L6002':['''psspy.dscn(199228)''', '''no_island()''',],

                   '99W-L7009':['''psspy.branch_chng(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '99W-L7008':['''psspy.branch_chng(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '99W-601':['''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                   # L-6025 segment
                   '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                   # L-6006
                   '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                    
                   # L-6002
                   '''psspy.dscn(199228)''', '''no_island()''',
                    
                   # 99W-T61
                   '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                   '''psspy.dscn(199240)''',
                   '''no_island()''',],
                   
                  '99W-601-IR664':['''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                   # L-6025 segment
                   '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                   # L-6006
                   '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                    
                   # L-6002
                   '''psspy.dscn(199228)''', '''no_island()''',
                    
                   # 99W-T61
                   '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                   '''psspy.dscn(199240)''',
                   
                   # IR664
                   '''psspy.dscn(199846)''',
                   '''no_island()''',],
                   #99W-B61 trips 99W-T61, L-6002, L-6006, L6025
		   #SAME AS 99W-T61

                   
                   # 99W-T62, 99W-619, 99W-622, 99W-631, 99W-602
                   #'99W-T62':[
                   #    # 99W-T72 (technically open circuit except fully out in 99W-602)
                   #    '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                   #           
                   #    # 99W-T62
                   #    '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                   #	
                   #    # L-6531
                   #    '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                   #	
                   #    # 99W shunt
                   #    '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''', 
                   #	
                   #    # L-6002
                   #    '''psspy.dscn(199228)''', '''no_island()''',
                   #],

                   #99W-B62 trips 99W-T62, 99W-C61, L-6531
		   #SAME AS 99W-T62
                   '99W-T62':[
                         # 99W-T72 (technically open circuit except fully out in 99W-602)
                         '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                               
                         # 99W-T62
                         '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                     	
                         # L-6531
                         '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                     	
                         # 99W shunt
                         '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''',
                         ],
                   '99W-B62':[
                         # 99W-T72 (technically open circuit except fully out in 99W-602)
                         '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                               
                         # 99W-T62
                         '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                     	
                         # L-6531
                         '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                     	
                         # 99W shunt
                         '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''',
                         ],

                   '99W-602':[
                        # 99W-T72 (technically open circuit except fully out in 99W-602)
                        '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                               
                        # 99W-T62
                        '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                            
                        # L-6531
                        '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                            
                        # 99W shunt
                        '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''', 
                        '''psspy.dscn(199241)''','''no_island()''',
                   ],		
                   
                   '99W-602-IR664':[
                        # 99W-T72 (technically open circuit except fully out in 99W-602)
                        '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                               
                        # 99W-T62
                        '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                            
                        # L-6531
                        '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                            
                        # 99W shunt
                        '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''', 
                        '''psspy.dscn(199241)''','''no_island()''',
                        
                        #IR664
                        '''psspy.dscn(199846)''',
                        '''no_island()''',],
                        
                   # 99W-T61, 99W-606, 99W-625, 99W-601, 99W-B61	
                   '99W-T61':[
                        # 99W-T71 (technically open circuit except fully out in 99W-601)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        
                        '''no_island()''',
                   ],
                   '99W-606':[
                        # 99W-T71 (technically open circuit except fully out in 99W-601)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        
                        '''no_island()''',
                   ],
                   '99W-625':[
                        # 99W-T71 (technically open circuit except fully out in 99W-601)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        
                        '''no_island()''',
                   ],
                   '99W-601':[
                        # 99W-T71 (technically open circuit except fully out in 99W-601)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        
                        '''no_island()''',
                   ],
                   '99W-B61':[
                        # 99W-T71 (technically open circuit except fully out in 99W-601)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        
                        '''no_island()''',
                   ],
                   
                   '99W-T61-IR664':[
                        # 99W-T71 (technically open circuit except fully out in 99W-601)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',

                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                            
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        # IR664
                        '''psspy.dscn(199846)''',
                        '''no_island()''',],
                   '99W-T62-IR664':[
                         # 99W-T72 (technically open circuit except fully out in 99W-602)
                         '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                               
                         # 99W-T62
                         '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                     	
                         # L-6531
                         '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                     	
                         # 99W shunt
                         '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''',
                         # IR664
                         '''psspy.dscn(199846)''',
                         '''no_island()''',
                         ],
                            
                   '99W-SHUNT':['''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''',],

                   # 99W-545, 99W-546, 99W-B51
                   '99W-545':['''psspy.dscn(199233)''', '''psspy.dscn(199232)''', '''no_island()''',],
                   '99W-546':['''psspy.dscn(199233)''', '''psspy.dscn(199232)''', '''no_island()''',],
                   '99W-B51':['''psspy.dscn(199233)''', '''psspy.dscn(199232)''', '''no_island()''',],

                   # 99W-501
                   '99W-501':[
                        # 99W-T71 (technically open circuit)
                        '''psspy.two_winding_chng_4(199230,199240,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T71""",_s])''',
                        
                        # L-6025 segment
                        '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6006
                        '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        '''no_island()''',
                        
                        # L-6002
                        '''psspy.dscn(199228)''', '''no_island()''',
                        # 99W-T61
                        '''psspy.two_winding_chng_4(199230,199231,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T61""",_s])''',
                        
                        # L-5545, L-5546
                        '''psspy.dscn(199231)''', '''no_island()''',
                        
                        # 99W-T62 is then open circuit
                   ],

                   # 99W-562 
                   '99W-562':[ 
                       # 99W-T72 (technically open circuit)
                        '''psspy.two_winding_chng_4(199230,199241,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T72""",_s])''',
                               
                        # 99W-T62
                        '''psspy.two_winding_chng_4(199230,199231,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""99W-T62""",_s])''', 
                       
                        # L-6531
                        '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', 
                       
                        # 99W shunt
                        '''psspy.shunt_chng(199230,r"""2""",0,[_f,_f])''', 
                       
                        # L-6002
                        '''psspy.dscn(199228)''', # '''no_island()''',
                       
                       # L-5545, L-5546
                       '''psspy.dscn(199231)''', '''no_island()''',
                       
                       # 99W-T61 is then open circuit
                   ],
                        
##                   # 99W-600 (Leaves 99W-T71, 99W-T72 open circuit)
##                   '99W-600':['''psspy.dscn(199230)''', '''no_island()''',],
                       


# -------------
# 3W - Big Fall HYDRO
# -------------
                   '3W-B53':['''psspy.dscn(199252)''', 
                             '''no_island()''',],
# -------------
# 3V - HELLS'S GATE HYDRO
# -------------
                   #If L-5033, L-5035, or L-5019 are taken out, so are the other two. But they do not reach Bus 199322 without passing a breaker.

                   # NS_L4049-1 -> open 3V-551
                   '3V-L4049':['''psspy.dscn(199326)''', 
                                 '''no_island()''',],

                   # NS_L5035 -> L-5033 and L-5019 also; Bus 199326 local distribution becomes islanded.
                   # SAME AS NS_L5035 CONTINGENCY = 3V-T41, 3V-T51, 3V-551, 3V-201 or 3V-202 or 6V-GT1
                   '3V-L5035':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   '3V-T41':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   '3V-T51':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   '3V-551':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   '3V-201':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   '3V-202':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   '6V-GT1':['''psspy.dscn(199326)''',
                               
                               # L-5019
                               '''psspy.dscn(199341)''',
                               '''no_island()''',],
                   

                   # 3V-G1   
                   '3V-G1':['''psspy.machine_chng_2(199327,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   # 3V-G2
                   '3V-G2':['''psspy.machine_chng_2(199327,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                

# -------------
# 22V - NEW MINAS
# -------------
                   # 22V modelled as a load at bus 199324 no breakers
                   # 36V shares the same tap
                   # Handled in 3V as losing NS_L5033-1                 
                   '22V-L5033':['''psspy.dscn(199324)''',
                                '''psspy.dscn(199325)''',],       
# -------------
# 43V - CANAAN RD., WHITE ROCK
# -------------
                   #If L-5033, L-5035, or L-5019 are taken out, so are the other two. But they do not reach Bus 199322 without passing a breaker.
                   # NS_L5019-1, NS_L5035, NS_L5033-1 same effect and handled in 3V

                   '43V-L6012':['''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '43V-L6013':['''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '43V-L6054':['''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '43V-L6015':['''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # 50V Load
                   '43V-50VLoad': ['''psspy.dscn(199694)''',],

                   # L-6052 to 99V
                   '43V-L6052':['''psspy.dscn(199333)''',],

                   # NS_L5017-2 
                   '43V-L5017':['''psspy.dscn(199320)''', '''no_island()''',],

                   '43V-L5022':['''psspy.branch_chng(199322,199335,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # NS_L5021 (to 50V)
                   '43V-L5021':['''psspy.dscn(199323)''',],

                   #43V-T62, 43V-615, 43V-652, 43V-604, 43V-602
                   '43V-T62':['''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                               
                                # L-6054       
                                '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6015
                                '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6052
                                '''psspy.dscn(199333)''',
                   ], #43V-B62
                   '43V-615':['''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                               
                                # L-6054       
                                '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6015
                                '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6052
                                '''psspy.dscn(199333)''',
                   ], #43V-B62
                   '43V-652':['''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                               
                                # L-6054       
                                '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6015
                                '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6052
                                '''psspy.dscn(199333)''',
                   ], #43V-B62
                   '43V-604':['''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                               
                                # L-6054       
                                '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6015
                                '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6052
                                '''psspy.dscn(199333)''',
                   ], #43V-B62
                   '43V-602':['''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                               
                                # L-6054       
                                '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6015
                                '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6052
                                '''psspy.dscn(199333)''',
                   ], #43V-B62

                   # 43V-T61, 43V-612, 43V-613, 43V-619, 43V-601
                   '43V-T61':['''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                               
                                # 43V shunt
                                '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                                # L-6013 open
                                '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # L-6012
                                '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # 50V Load
                                '''psspy.dscn(199694)''',
                   ], #43V-B61
                   '43V-612':['''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                               
                                # 43V shunt
                                '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                                # L-6013 open
                                '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # L-6012
                                '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # 50V Load
                                '''psspy.dscn(199694)''',
                   ], #43V-B61
                   '43V-613':['''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                               
                                # 43V shunt
                                '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                                # L-6013 open
                                '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # L-6012
                                '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # 50V Load
                                '''psspy.dscn(199694)''',
                   ], #43V-B61
                   '43V-619':['''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                               
                                # 43V shunt
                                '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                                # L-6013 open
                                '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # L-6012
                                '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # 50V Load
                                '''psspy.dscn(199694)''',
                   ], #43V-B61
                   '43V-601':['''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                               
                                # 43V shunt
                                '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                                # L-6013 open
                                '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # L-6012
                                '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                # 50V Load
                                '''psspy.dscn(199694)''',
                   ], #43V-B61

                

                   '43V-B61':['''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                               
                                # 43V shunt
                                '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                                # L-6013 open
                                '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                # L-6012
                                '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                
                                #L-5021
                                '''psspy.dscn(199323)''',
                                # 50V Load
                                '''psspy.dscn(199694)''',
                   ],

                   '43V-B62':['''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                              
                                 # L-6054       
                                 '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               
                                 # L-6015
                                 '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                               
                                 # L-6052
                                 '''psspy.dscn(199333)''',
                   ],

                   

                   '43V-SHUNT':['''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',],

                   '43V-B51':[    '''psspy.dscn(199322)''', '''no_island()''',],
                   # 43V-505, 43V-501, 43V-504, 43V-502
                   '43V-505':['''psspy.dscn(199322)''', '''no_island()''',],
                   '43V-501':['''psspy.dscn(199322)''', '''no_island()''',],
                   '43V-502':['''psspy.dscn(199322)''', '''no_island()''',],
                   '43V-504':['''psspy.dscn(199322)''', '''no_island()''',],

                   # 43V-562
                   '43V-562':[
                        # 43V-T62
                        '''psspy.two_winding_chng_4(199322,199340,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T62""",_s])''',
                                   
                        # L-6054       
                        '''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6015
                        '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                        # L-6052
                        '''psspy.dscn(199333)''',
                        
                        # All connections to bus 199322 opened
                        '''psspy.dscn(199322)''', '''no_island()''',
                   ],

                   # 43V-503
                   '43V-503':[
                        # 43V-T61
                        '''psspy.two_winding_chng_4(199322,199340,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""43V-T61""",_s])''',
                                   
                        # 43V shunt
                        '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',

                        # L-6013 open
                        '''psspy.branch_chng(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                         
                        # L-6012
                        '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                         
                        #50VLoad
                        '''psspy.dscn(199694)''',
                        # All connections to bus 199322 opened
                        '''psspy.dscn(199322)''', '''no_island()''',
                   ],

                   # 43V-506
                   '43V-506':[
                        # All connections to bus 199322 opened
                        '''psspy.dscn(199322)''', # '''no_island()''',
                        
                        # L-5017
                        '''psspy.dscn(199320)''', '''no_island()''',
                   ],       
                                       
# -------------
# 41V - MINAS BASIN PULP & POWER MILL
# -------------
# Elements: L-4048-2, L-4047, 41V-SHUNT, 41V-LOAD, 41V-407

                   # NS_L4048-2
                   '41V-L4048':['''psspy.dscn(199314)''',],

                   # NS_L4047, 41V-SHUNT, 41V-LOAD
                   '41V-L4047':['''psspy.branch_chng(199313,199315,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.dscn(199316)''',
                                '''psspy.dscn(199317)''',
                                '''psspy.shunt_chng(199313,r"""2""",0,[_f,_f])''',	
                                '''psspy.load_chng_5(199313,r"""51""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   '41V-SHUNT':['''psspy.branch_chng(199313,199315,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.dscn(199316)''',
                                '''psspy.dscn(199317)''',
                                '''psspy.shunt_chng(199313,r"""2""",0,[_f,_f])''',	
                                '''psspy.load_chng_5(199313,r"""51""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   '41V-LOAD':['''psspy.branch_chng(199313,199315,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                '''psspy.dscn(199316)''',
                                '''psspy.dscn(199317)''',
                                '''psspy.shunt_chng(199313,r"""2""",0,[_f,_f])''',	
                                '''psspy.load_chng_5(199313,r"""51""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '41V-407':['''psspy.branch_chng(199313,199315,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.dscn(199316)''',
                              '''psspy.dscn(199317)''',
                              '''psspy.shunt_chng(199313,r"""2""",0,[_f,_f])''',
                              '''psspy.load_chng_5(199313,r"""51""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.dscn(199314)''',
                              '''no_island()''',],

# -------------
# 79V - THREE MILE PLAINS
# -------------
                   #L-5015-2, L-5015-3, L-5016-1, L-5016-2, 79V-LOAD
                   # No breakers are present
                   # if any of these are taken out, all have same consequences

                   '79V-L5015':['''psspy.dscn(199303)''',
                                  '''psspy.dscn(199310)''',
                                  '''psspy.dscn(199309)''',
                                  '''no_island()''',], #Same as 1V-442
                   '1V-442':['''psspy.dscn(199303)''',
                                  '''psspy.dscn(199310)''',
                                  '''psspy.dscn(199309)''',
                                  '''no_island()''',], #Same as 1V-442

                   '79V-L5016':['''psspy.dscn(199308)''',],

# -------------
# 20V - FIVE POINTS, HANTSPORT
# -------------
                   # Elements L-5016-2, L-5017-1, L-4048-1, 20V-T1, 20V-LOAD, 20V-503, 20V-504, 20V-401

                   # NS_L5016 handled in 79V
                   # NS_L4048 handled in 41V
                   # NS_L5017 handled in 43V

                   '20V-T1':['''psspy.dscn(199311)''',
                             '''no_island()''',], # same as 20V-B51
                   '20V-B51':['''psspy.dscn(199311)''',
                             '''no_island()''',], # same as 20V-B51

                   '20V-503':['''psspy.dscn(199311)''',
                              '''psspy.dscn(199320)''',
                              '''no_island()''',],

                   '20V-504':['''psspy.dscn(199311)''',
                              '''psspy.dscn(199308)''',
                              '''no_island()''',],
                     
                   '20V-401':['''psspy.dscn(199311)''',
                              '''psspy.dscn(199314)''',
                              '''psspy.dscn(199312)''',
                              '''no_island()''',],

# -------------
# 102V - ELLERSHOUSE WIND
# -------------
                   #Elements: L-5060, 102V-T51, 102V-551, 102V-411, 102V-GT1, 102V-G1

                   # NS_L5060, 102V-551
                   '102V-L5060':['''psspy.dscn(199635)''','''no_island()''',],

                   # 102V-T51, 102V-411
                   '102V-T51':['''psspy.two_winding_chng_4(199635,199636,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""102V-T51""",_s])''',
                               '''psspy.dscn(199636)''',
                               '''no_island()''',],
                                            
                   # 102V-GT1, 102V-G1
                   '102V-GT1':['''psspy.dscn(199637)''', '''no_island()''',],

# -------------
# 17V - ST. CROIX
# -------------

                   # L-6012 handled in 43V
                   # 'NS_L6012':['''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # L-6051 segment
                   '17V-L6051':['''psspy.branch_chng(199300,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   '17V-L6011':['''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # NS_L5060 handled in 102V
                   # NS_L5015-1 handled in 79V
                   # NS_L5016-1 handled in 79V

                   # NS_L5014
                   '17V-L5014':['''psspy.dscn(199307)''',],

                   # NS_L4047 handled in 41V

                   '17V-L4046':['''psspy.dscn(199315)''',
                                '''psspy.dscn(199316)''',
                                '''psspy.dscn(199317)''',],

                   '17V-L4045':['''psspy.dscn(199315)''',
                                '''psspy.dscn(199316)''',
                                '''psspy.dscn(199317)''',],

                   '17V-SHUNT':['''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',],

                   # 17V-T2, 17V-651, 17V-B2
                   '17V-T2':['''psspy.two_winding_chng_4(199300,199301,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T2""",_s])''',
                              
                             # L-6051 segment
                             '''psspy.branch_chng(199300,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '17V-651':['''psspy.two_winding_chng_4(199300,199301,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T2""",_s])''',
                              
                             # L-6051 segment
                             '''psspy.branch_chng(199300,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '17V-B2':['''psspy.two_winding_chng_4(199300,199301,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T2""",_s])''',
                              
                             # L-6051 segment
                             '''psspy.branch_chng(199300,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],

                   #17V-T63, 17V-610
                   '17V-T63':['''psspy.two_winding_chng_4(199300,199301,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T63""",_s])''',
                               
                              #L-6011
                              '''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '17V-610':['''psspy.two_winding_chng_4(199300,199301,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T63""",_s])''',
                               
                              #L-6011
                              '''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],

                   '17V-T1':['''psspy.two_winding_chng_4(199301,199315,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T1""",_s])''',],


                   # 17V-612
                   '17V-612':['''psspy.two_winding_chng_4(199300,199301,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T2""",_s])''',
                              
                              # L-6051 segment
                              '''psspy.branch_chng(199300,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                              # L-6012
                              '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],

                   #17V-611
                   '17V-611':['''psspy.two_winding_chng_4(199300,199301,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T63""",_s])''',
                               
                              #L-6011
                              '''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                        
                              # L-6012
                              '''psspy.branch_chng(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],

                   # 17V-563
                   '17V-563':['''psspy.dscn(199301)''', '''no_island()''',
                               
                              # 17V-T63
                              '''psspy.two_winding_chng_4(199300,199301,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T63""",_s])''',
                                   
                              #L-6011
                              '''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                                    
                   # 17V-512
                   '17V-512':['''psspy.dscn(199301)''', '''no_island()''',
                               
                              # 17V-T2
                              '''psspy.two_winding_chng_4(199300,199301,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""17V-T2""",_s])''',
                                  
                              # L-6051 segment
                              '''psspy.branch_chng(199300,199800,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                            
                   # 17V-519, 17V-503, 17V-502, 17V-506, 17V-B1
                   '17V-519':['''psspy.dscn(199301)''',
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()''',],
                   '17V-503':['''psspy.dscn(199301)''',
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()''',],
                   '17V-502':['''psspy.dscn(199301)''',
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()''',],
                   '17V-506':['''psspy.dscn(199301)''',
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()''',],
                   '17V-B1':['''psspy.dscn(199301)''',
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()''',],
                                            
                   # 17V-505, 17V-504
                   '17V-505':['''psspy.dscn(199301)''',
                              '''psspy.dscn(199303)''',
                              '''psspy.dscn(199310)''',
                              '''psspy.dscn(199309)''',
                                                    
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()'''],
                   '17V-504':['''psspy.dscn(199301)''',
                              '''psspy.dscn(199303)''',
                              '''psspy.dscn(199310)''',
                              '''psspy.dscn(199309)''',
                                                    
                              #'''psspy.shunt_chng(199301,r"""2""",0,[_f,_f])''',
                              '''no_island()'''],
                                            
# -------------
# 101V - MACDONALD POND
# -------------

                   #L-6004 to 90H
                   '101V-L6004-a':['''psspy.dscn(199570)''',],          # modded
                   # '101V-L6004-1':['''psspy.dscn(199790)''','''no_island()''',],
                   # NS_L6004-2 (L-6054), handled in 43V
                   # 'NS_L6004-2':['''psspy.branch_chng(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   # NS_L6053 -> Bus 199501 local area becomes islanded
                   '101V-L6053':['''psspy.dscn(199501)''','''no_island()''',],

                   # 101V-601, 101V-602, 101V-603
                   '101V-601':['''psspy.dscn(199500)''','''no_island()''',],

# -------------
# 110W - SOUTH CANOE LAKE
# -------------
                   # 110W taps line from 101V
                   'IR379-GT':['''psspy.dscn(199503)''', '''no_island()''',],

                   'IR372-GT':['''psspy.dscn(199509)''', '''no_island()''',],

                   'IR379-TX':['''psspy.dscn(199502)''', '''no_island()''',],

                   'IR372-TX':['''psspy.dscn(199508)''', '''no_island()''',],

                   '110W-661':['''psspy.dscn(199501)''', '''no_island()''',],
                   #110W-B61 trips 110W (110W-T61, 110W-T62, no island)
                   #SAME AS 110W-661
                   '110W-B61':['''psspy.dscn(199501)''', '''no_island()''',],

# *********************
# 11V-Paradise 69kV
# *********************
                   '11V, 11V-B51':['''psspy.dscn(199356)''',
                                   '''psspy.dscn(199357)''',],

                   '11V, 11V-B51_SPS':['''psspy.dscn(199356)''',
                                       '''psspy.dscn(199357)''',
                                       '''psspy.dscn(199712)''',],

# *********************
# 13V-Gulch 69kV
# *********************
                   '13V, L-5026':['''psspy.dscn(199362)''',
                                  '''psspy.dscn(199363)''',
                                  '''psspy.dscn(199351)''',
                                  '''psspy.dscn(199349)''',
                                  '''psspy.dscn(199352)''',
                                  '''psspy.dscn(199353)''',
                                  '''psspy.dscn(199354)''',
                                  '''psspy.dscn(199355)''',],

                   # Gulliver's Cove Wind Rejection RAS - loss of L-5026 trip Gullivers Cove if Armed
                   '13V, L-5026_SPS':['''psspy.dscn(199362)''',
                                      '''psspy.dscn(199363)''',
                                      '''psspy.dscn(199351)''',
                                      '''psspy.dscn(199349)''',
                                      '''psspy.dscn(199352)''',
                                      '''psspy.dscn(199353)''',
                                      '''psspy.dscn(199354)''',
                                      '''psspy.dscn(199355)''',
                                      '''psspy.dscn(199712)''',],

                   '13V, L-5531':['''psspy.branch_chng(199364,199370,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '13V, L-5532':['''psspy.dscn(199367)''',
                                  '''psspy.dscn(199368)''',
                                  '''psspy.dscn(199369)''',
                                  '''psspy.dscn(199261)''',
                                  '''psspy.dscn(199262)''',
                                  '''psspy.dscn(199260)''',
                                  '''psspy.dscn(199259)''',],


                   '13V, 13V-B51':['''psspy.dscn(199364)''',
                                   '''psspy.dscn(199365)''',
                                   '''psspy.dscn(199372)''',
                                   '''psspy.dscn(199366)''',
                                   '''psspy.dscn(199710)''',
                                   '''psspy.dscn(199709)''',
                                   '''psspy.dscn(199711)''',
                                   '''psspy.dscn(199712)''',],

                   '13V, L-5533':['''psspy.dscn(199366)''',
                                  '''psspy.dscn(199710)''',
                                  '''psspy.dscn(199709)''',
                                  '''psspy.dscn(199711)''',
                                  '''psspy.dscn(199712)''',],
	
# *********************
# 51V-Tremont 138kV
# *********************
                   '51V, 51V-B61':['''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_s,_s])''',],
                   '51V-601':['''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_s,_s])''',
                              '''psspy.branch_chng(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                   ],
                   '51V-T62':['''psspy.two_winding_chng_4(199345,199346,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_s,_s])''',],
                   
# *********************
# 51V-Tremont 69kV
# *********************
                   # Automated Action Scheme 51V U/V - O/L on either 138kV-69kV transformer or 69kV U/V trips 51V-553 to 63V-Kingston and 64V-Greenwood (Low Probability event)
                   # Automated Action Scheme Western Valley Import - Operators limit I/P to 80MW via out of merit gen 
                   '51V, L-5025':['''psspy.dscn(199360)''',
                                  '''psspy.dscn(199361)''',
                                  '''psspy.dscn(199358)''',
                                  '''psspy.dscn(199359)''',], 

                   # Valley Export SPS: Where Valley Export > 40MW, trip Gullivers Cove for loss of L-5025, L-5026, & 51V-502
                   '51V, L-5025_SPS':['''psspy.dscn(199360)''',
                                      '''psspy.dscn(199361)''',
                                      '''psspy.dscn(199358)''',
                                      '''psspy.dscn(199359)''',
                                      '''psspy.dscn(199712)''',],

                   '51V, 51V-B51':['''psspy.branch_chng(199346,199360,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                   '''psspy.load_chng_4(199346,r"""1""",[0,_i,_i,_i,1,0],[_f,_f,_f,_f,_f,_f])''',
                                   '''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""51V-T61""",_s])''',],

                   '51V, 51V-B51_OL':['''psspy.branch_chng(199346,199360,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                      '''psspy.load_chng_4(199346,r"""1""",[0,_i,_i,_i,1,0],[_f,_f,_f,_f,_f,_f])''',
                                      '''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""51V-T61""",_s])''',
                                      '''psspy.dscn(199347)''',
                                      '''psspy.dscn(199348)''',], 

                   '51V, 51V-B51_SPS':['''psspy.branch_chng(199346,199360,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                       '''psspy.load_chng_4(199346,r"""1""",[0,_i,_i,_i,1,0],[_f,_f,_f,_f,_f,_f])''',
                                       '''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""51V-T61""",_s])''',
                                       '''psspy.dscn(199712)''',],

                   '51V, 51V-B52':['''psspy.branch_chng(199338,199346,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                   '''psspy.two_winding_chng_4(199345,199346,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""51V-T62""",_s])''',
                                   '''psspy.dscn(199347)''',
                                   '''psspy.dscn(199348)''',],

                   '51V, 51V-T61':['''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""51V-T61""",_s])''',],

                   '51V, 51V-T61_OL':['''psspy.two_winding_chng_4(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""51V-T61""",_s])''',
                                      '''psspy.dscn(199347)''',
                                      '''psspy.dscn(199348)''',],
                    
                   '51V-L5053':['''psspy.dscn(199338)''',
                                '''psspy.dscn(199339)''',
                                '''psspy.dscn(199337)''',
                                '''psspy.dscn(199336)''',],
# *********************
# 9W-Tusket 138kV
# *********************
                   '9W, 9W-T2':['''psspy.dscn(199287)''',
                                '''psspy.dscn(199270)''',],

                   '9W, 9W-T2_OL':['''psspy.dscn(199287)''',
                                   '''psspy.dscn(199270)''',
                                   '''psspy.dscn(199282)''',
                                   '''no_island()''',],    	
 
# *********************
# 9W-Tusket 69kV
# *********************
                   '9W, L-5535':['''psspy.dscn(199292)''',],
                        
                   '9W, 9W-B53':['''psspy.switched_shunt_chng_3(199281,[_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,0,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")''', # C52
                                 '''psspy.dscn(199292)''', # L5535
                                 '''psspy.dscn(199288)''', # 16W
                                 '''psspy.dscn(199291)''', # 88W
                                 '''psspy.dscn(199282)''', # L5027
                                 '''psspy.dscn(199280)''', # 9W-T63 / L6024
                                 '''no_island()''',],
                        
                   '9W, 9W-B52':['''psspy.dscn(199294)''', # L5536
                                 '''psspy.dscn(199285)''', # Hydro
                                 '''psspy.dscn(199286)''', # L5537
                                 '''psspy.dscn(199287)''', # 9W-T2 / L6021
                                 '''no_island()''',],
                    
                   '9W, L-5027':['''psspy.dscn(199282)''',
                                  '''no_island()''',], # L5027
# *********************
# 30W-Souriquoi 138kV
# *********************
                   #30W-T62, 30W-B61
                   '30W, 30W-T62':['''psspy.two_winding_chng_4(199270,199271,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""30W-T62""",_s])''',],
                   '30W, 30W-B61':['''psspy.two_winding_chng_4(199270,199271,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""30W-T62""",_s])''',],

# *********************
# 30W-Souriquoi 69kV
# *********************	   
                   '30W, 30W-B51':['''psspy.dscn(199271)''',    	
                                   '''no_island()''',],     	  	
    	
# *********************
# 50W-Milton 138kV
# *********************
                   '50W, L-6020':['''psspy.dscn(199270)''',
                                  '''psspy.dscn(199287)''',],

                   '50W, L-6024':['''psspy.dscn(199280)''',],

                   '50W, L-6048':['''psspy.dscn(199298)''',
                                  '''psspy.dscn(199279)''',],

                # Automated Action Scheme - SCADA Warning: L6020+L6024+L5530 > 70MVA; SCADA Alarm: > 75MVA thru 9W-T63 will trip L-5027 at 9W. Operators dispatch system to limit sum of these lines to < 75MW
                   '50W, 50W-B3':['''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])''', #T1
                                  '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6531
                                  '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6047
                                  '''psspy.branch_chng(199245,199270,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',], #L6020

                   '50W, 50W-B3_OL':['''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])''',
                                     '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                     '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                     '''psspy.branch_chng(199245,199270,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                     '''psspy.dscn(199282)''',
                                     '''no_island()''',],

                   '50W, 50W-615':['''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])''', #T1
                                  '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6531
                                  '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6047
                                  '''psspy.dscn(199270)''',
                                  '''psspy.dscn(199287)''',], #L6020

                   '50W, 50W-615_OL':['''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])''', #T1
                                  '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6531
                                  '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6047
                                  '''psspy.dscn(199270)''',
                                  '''psspy.dscn(199287)''',#L6020
                                  '''psspy.dscn(199282)''',
                                  '''no_island()''',],

                   '50W, 50W-B4':['''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6006
                                  '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6025
                                  '''psspy.branch_chng(199245,199298,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6048
                                  '''psspy.branch_chng(199245,199280,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6024
                                  '''psspy.dscn(199725)''', '''no_island()''', #IR597
                                  ],

                # *********************
                # 50W-Milton 69kV
                # *********************
                   '50W, L-5541':['''psspy.dscn(199249)''',
                                  '''psspy.dscn(199250)''',],
                   '50W, L-5530':['''psspy.dscn(199265)''',
                                  '''psspy.dscn(199264)''',
                                  '''no_island()''',],
                   '50W, L-5539':['''psspy.dscn(199263)'''],
                   '50W, 50W-B2':['''psspy.dscn(199246)''',
                                  '''psspy.dscn(199263)''',
                                  '''psspy.dscn(199247)''',
                                  '''psspy.dscn(199248)''',
                                  '''no_island()''',],
                   '50W, IR597': ['''psspy.dscn(199728)''',],
                   '50W, 50W-T53':[
                       '''psspy.load_chng_5(199246,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                       '''psspy.load_chng_5(199246,r"""51""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
                       ],
                   '50W, L-5540':['''psspy.dscn(199248)''',
                                  '''psspy.dscn(199247)''',],

# *********************
#113H DARTMOUTH EAST
# *********************
                   '113H-601': ['''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6044
                                '''psspy.two_winding_chng_4(199160,199161,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""106: 113H-T63""",_s])''',],#T63

                   '113H-L6043':[
                       '''psspy.dscn(199162)''',
                       '''psspy.dscn(199163)''',
                       ],

                   
# *********************
#132H SPIDER LAKE
# *********************
                   #132H-602 trips L6001, L6044
                   '132H-602': ['''psspy.dscn(199154)''',
                                '''psspy.dscn(199156)''',
                                # '''psspy.dscn(199159)''',
                                '''psspy.dscn(199155)''',
                                '''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
##                   '132H-602-IR662': [
##                                '''psspy.dscn(199154)''',
##                                '''psspy.dscn(199156)''',
##                                # '''psspy.dscn(199159)''',
##                                '''psspy.dscn(199155)''',
##                                '''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
##                                # IR662
##                                '''psspy.dscn(199840)''',
##                                '''psspy.dscn(199841)''',
##                                '''psspy.dscn(199842)''',
##                                ],

                   #132H-603 trips L6001, L6040
                   '132H-603': ['''psspy.dscn(199154)''',
                                '''psspy.dscn(199156)''',
                                # '''psspy.dscn(199159)''',
                                '''psspy.dscn(199155)''',#L6001
                                '''psspy.dscn(199158)''',
                                '''psspy.dscn(199153)''',#L6040
                                ],
                   
                   #132H-605 trips L6055, L6040
                   '132H-605': ['''psspy.branch_chng(199159,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6055
                                '''psspy.dscn(199158)''',
                                '''psspy.dscn(199153)''',#L6040
                                ],

                   #132H-606 trips L6055, L6044
                   '132H-606': ['''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6044
                                '''psspy.branch_chng(199159,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6055
                                ],
##                   '132H-606-IR662': [
##                                '''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6044
##                                '''psspy.branch_chng(199159,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', #L6055
##                                # IR662
##                                '''psspy.dscn(199840)''',
##                                '''psspy.dscn(199841)''',
##                                '''psspy.dscn(199842)''',
##                                ],

                   '132H-L6044': ['''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',], #L6044
##                   '132H-L6044-IR662': [
##                                  '''psspy.branch_chng(199159,199161,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',#L6044
##                                  # IR662
##                                  '''psspy.dscn(199841)''',
##                                  '''psspy.dscn(199840)''',
##                                  '''psspy.dscn(199842)''',
##                                  ], 

                   '132H-L6040':[
                                '''psspy.dscn(199158)''',
                                '''psspy.dscn(199153)''',#L6040
                                ],

                   '132H-L6055': ['''psspy.branch_chng(199159,199187,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],#L6055

# *********************
#1H WATER STREET 
# *********************
                   #1H-603 trips L6033,  T61
                   '1H-603': ['''psspy.dscn(199197)''',#L6033
                              '''psspy.two_winding_chng_4(199193,199194,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""106: 1H-T61""",_s])''',],#T61

                   '1H-L-6035':[
                       '''psspy.dscn(199207)''',
                       '''no_island()''',
                       ],

# *********************
#74N SPRINGHILL 
# *********************
                   '74N-600':[
                       '''psspy.dscn(199135)''',
                       '''psspy.dscn(199136)''',
                       '''no_island()''',
                       ],


                   '74N-L6536':['''psspy.dscn(199152)''',],

                   '74N-L6514':['''psspy.branch_chng(199135,199145,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '74N-L5029':[
                       '''psspy.dscn(199139)''',
                       '''psspy.dscn(199141)''',
                       ],

                   '74N-L5058':[
                       '''psspy.dscn(199137)''',
                       '''psspy.dscn(199138)''',
                       ],

# *********************
#92V-MICHELIN - WATERVILLE
# *********************
                   #92V-B51, 92V-B52
                   '92V-B51':[
                       '''psspy.dscn(199335)''',
                       ],
                   '92V-B52':[
                       '''psspy.dscn(199335)''',
                       ],
                   

# *********************
#15V SISSIBOO HYDRO
# *********************
                   '15V-B51':[
                       '''psspy.dscn(199370)''',
                       '''no_island()''',
                       ],

                   '15V-L5050':[
                       '''psspy.dscn(199373)''',
                       ],

                   '15V-L5538':[
                       '''psspy.dscn(199374)''',
                       '''no_island()''',
                       ],
# *********************
#101H COBEQUID ROAD
# *********************
                    '101H-600':[
                       '''psspy.dscn(199185)''',
                       '''no_island()''',
                       ],# same as L6009        
# *********************
#108H BURNSIDE G.T.SW.STA
# *********************
                    # 108H-600 trips first branch of L6009, L6007 and L6055, as well as the whole 108H
                    '108H-600':[
                       '''psspy.dscn(199187)''',
                       '''psspy.dscn(199188)''',
                       '''psspy.dscn(199189)''',
                       ],       
                    
                    # 108H-B1 trips G1G2, T61(load), first branch of L6007
                    '108H-B1':[
                       '''psspy.dscn(199188)''', # G1G2
                       '''psspy.load_chng_5(199187,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''', # T61
                       '''psspy.branch_chng(199187,199165,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', # L6007
                       ],  
                    # 108H-B3 trips G3G4, first branch of L6009 and L6055
                    '108H-B3':[
                       '''psspy.dscn(199189)''', # G3G4
                       '''psspy.branch_chng(199187,199185,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', # L6009-1
                       '''psspy.branch_chng(199187,199159,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''', # L6055
                       ], 
                       
# ---------------------
# Double Circuit Towers				   
# ---------------------  
                   'DCT_L-5039][L-6033':['''psspy.dscn(199197)''',
                                         '''psspy.dscn(199205)''',
                                         '''psspy.dscn(199196)''',
                                         '''psspy.dscn(199180)''',],    
                   
                   'DCT_L-7009][L-8002':['''psspy.branch_chng(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                         '''psspy.branch_chng(199125,199195,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   'DCT_L-6011][L-6010':['''psspy.branch_chng(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                         '''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   'DCT_L-6010][L-6005':['''psspy.branch_chng(199184,199201,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                         '''psspy.dscn(199203)''',],

                   'DCT_L-6005][L-6016':['''psspy.dscn(199203)''',
                                         '''psspy.dscn(199208)''',
                                         '''psspy.dscn(199209)''',],

                   'DCT_L-7008][L-7009':['''psspy.branch_chng(199200,199240,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                         '''psspy.branch_chng(199200,199241,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                         '''psspy.dscn(199292)''',
                                         '''psspy.branch_chng(199252,199259,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                         '''no_island()''',],
				   
                   'DCT_L-7003][L-7004_G0':['''psspy.branch_chng(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                            '''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
				   
		   'DCT_L-7003][L-7004_G3':['''psspy.branch_chng(199050,199590,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                            '''psspy.branch_chng(199050,199130,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                            '''sps('G3')''',],
				   
                   'DCT_L-6507][L-6508':['''psspy.dscn(199695)''',
                                         '''psspy.branch_chng(199090,199121,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
				   
		   'DCT_L-7021][L-6534':['''psspy.dscn(199006)''',
                                         '''psspy.branch_chng(199042,199000,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''],
                   
		   'DCT_L-6033][L-6035':['''psspy.dscn(199207)''',
                                         '''psspy.dscn(199197)''',
                                         '''no_island()''',],
# ----------------------
# Wreck Cove Area
# ----------------------
                   #Same as L6549
                   '85S_L-6545':['''psspy.branch_chng(199035,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   '85S_L-6549':['''psspy.branch_chng(199035,199031,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '5S_L-6538':['''psspy.branch_chng(199031,199025,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
                   
                   '5S_L-6549':['''psspy.branch_chng(199031,199035,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   '3S_L-6539':['''psspy.dscn(199961)''',],
                   
                   '3S_bus':['''psspy.dscn(199025)''',
                             '''psspy.dscn(199026)''',],

                   '5S_L-6537':['''psspy.dscn(199033)''',
                                '''psspy.dscn(199057)''',
                                '''no_island()''',],
                   
                   '2S_L-6516':['''psspy.dscn(199063)''',
                                '''psspy.dscn(199056)''',
                                '''psspy.dscn(199070)''',],
                   
                   #BBU trips L6549 and L6538
                   '5S-606':['''psspy.branch_chng(199035,199031,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.branch_chng(199031,199025,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

                   #BBU trips L6545 and L6537
                   '5S-607':['''psspy.branch_chng(199035,199031,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                             '''psspy.dscn(199033)''',
                             '''psspy.dscn(199057)''',
                             '''no_island()''',],
# -------------------------------------------
# Other BES Generator transformers/generators
# -------------------------------------------
# 2S-513 VJ BUS TIE BREAKER
                   '2S-513':['''psspy.dscn(199010)''',
                             '''no_island()''',],

# 89S-GT1 AND 89S-G1
                   '89S-G1':['''psspy.dscn(199043)''',],

# 1C-GT2 and 1C-G2
                   '1C-G2':['''psspy.dscn(199055)''',],

# 47C-T68 and 48C-G1
                   '48C-G1':['''psspy.dscn(199072)''',],

# 50N-GT5 and 50N-G5
                   '50N-G5':['''psspy.dscn(199085)''',],

# 50N-GT6 and 50N-G6
                   '50N-G6':['''psspy.dscn(199086)''',],
                 
# L-6511 Trenton 
                   '50N-L-6511':['''psspy.branch_chng(199090,199610,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],

# 91H-GT3 and 91H-G3 
                   '91H-G3':['''psspy.dscn(199169)''',],

# 91H-T64 and 91H-G4
                   '91H-G4':['''psspy.dscn(199181)''',],

# 91H-T65 and 91H-G5
                   '91H-G5':['''psspy.dscn(199182)''',],

# 91H-T66 and 91H-G6
                   '91H-G6':['''psspy.dscn(199164)''',],

# 104W-MPT and 104W-G1
                   '104W-G1':['''psspy.dscn(199279)''',],

# 110W-T62 and 110W-G1/G34
                   '110W-T62':['''psspy.dscn(199502)''',
                               '''psspy.dscn(199503)''',
                               '''psspy.dscn(199504)''',],
           
# 104H-600 KEMPT ROAD BUS TIE BREAKER 
                   '104H-600':['''psspy.dscn(199198)''',
                               '''psspy.dscn(199199)''',],
# -------------------------------------------
# Key New Brunswick Contingencies
# -------------------------------------------
# L3004 
           'SALISBURY_L3004':['''psspy.branch_chng(190197,190498,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
           
# L3013 
           'SALISBURY_L3013':['''psspy.branch_chng(190320,190498,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
           
# L3006 + L3017 NO SPS
           'SALISBURY_SA3-2':['''psspy.branch_chng(190320,190402,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                              '''psspy.branch_chng(190320,190417,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])'''],
           
# L3006 + L3017 TRIP PEI
           'SALISBURY_SA3-2_SPS':['''psspy.branch_chng(190320,190402,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.branch_chng(190320,190417,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.dscn(190291)''',
                                  '''psspy.dscn(190292)''',
                                  '''psspy.dscn(192258)''',
                                  '''psspy.dscn(192259)''',
                                  '''no_island()''',],
           
# L3006 no SPS
           'SALISBURY_L3006':['''psspy.branch_chng(190320,190402,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',],
           
# L3006 TRIP PEI
           'SALISBURY_L3006_SPS':['''psspy.branch_chng(190402,190320,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
                                  '''psspy.dscn(190291)''',
                                  '''psspy.dscn(190292)''',
                                  '''psspy.dscn(192258)''',
                                  '''psspy.dscn(192259)''',
                                  '''no_island()''',],
 
# ME1 TRIP L1159
           'MEMRAMCOOK_L1159':['''psspy.dscn(190275)''',
                               '''psspy.dscn(190379)''',
                               '''no_island()''',],
       
# ME1 TRIP L1160
           'MEMRAMCOOK_L1160':['''psspy.dscn(190408)''',
                               '''psspy.dscn(199152)''',],
  
# ME3-1 WITH SPS TRIP L3006, L8001 AND PEI
           'MEMRAMCOOK_ME3-1_SPS':['''psspy.dscn(190402)''',
                                   '''psspy.dscn(190381)''',
                                   '''psspy.dscn(190291)''',
                                   '''psspy.dscn(190292)''',
                                   '''psspy.dscn(192258)''',
                                   '''psspy.dscn(192259)''',
                                   '''no_island()''',],

            '50W, 50W-501':[
            '''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])#50WT1''',
            '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])#L5631''',
            '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])#L6047''',
            '''psspy.branch_chng(199245,199270,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])#L6020''',
            '''psspy.dscn(199246)''',
            '''psspy.dscn(199263)''',
            '''psspy.dscn(199247)''',
            '''psspy.dscn(199248)''',
            '''psspy.dscn(199264)''',
            '''psspy.dscn(199265)''',
            '''psspy.dscn(199266)'''
            ],
            '50W-600':[
            '''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])#50WT1''',
            '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])#L5631''',
            '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])#L6047''',
            '''psspy.branch_chng(199245,199270,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])#L6020''',
            '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199298,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199280,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.dscn(199725)''',
            '''no_island()'''
            ],
            '50W-600_OL':[
            '''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])''',
            '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199270,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.dscn(199282)''',
            '''no_island()''',
            '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199298,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199280,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.dscn(199725)''',
            '''no_island()'''
            ],
            '50W-600_OL_ISL':[
            '''psspy.two_winding_chng_4(199245,199246,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""50W-T1""",_s])''',
            '''psspy.branch_chng(199230,199245,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199277,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199270,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.dscn(199282)''',
            '''no_island()''',
            '''psspy.branch_chng(199230,199245,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199230,199245,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199298,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.branch_chng(199245,199280,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.dscn(199725)''',
            '''psspy.dscn(199281)''',
            '''psspy.dscn(199369)''',
            '''psspy.dscn(199264)''',
            '''psspy.dscn(199252)''',
            '''no_island()'''
            ],
            '9W-500':[
            '''psspy.dscn(199281)''',
            '''psspy.dscn(199288)''',
            '''psspy.dscn(199291)''',
            '''psspy.dscn(199294)''',
            '''psspy.dscn(199282)''',
            '''psspy.dscn(199285)''',
            '''psspy.dscn(199286)''',
            '''psspy.dscn(199289)''',
            '''psspy.dscn(199283)''',
            '''psspy.dscn(199275)''',
            '''psspy.dscn(199400)''',
            '''psspy.dscn(199401)''',
            '''psspy.dscn(199284)''',
            '''psspy.dscn(199276)'''
            ],
            '43V-562':[
            '''psspy.dscn(199322)''',
            '''psspy.dscn(199341)''',
            '''psspy.dscn(199330)''',
            '''psspy.dscn(199332)''',
            '''psspy.dscn(199331)''',
            '''psspy.dscn(199342)''',
            '''psspy.dscn(199334)''',
            '''psspy.dscn(199324)''',
            '''psspy.dscn(199325)''',
            '''psspy.dscn(199326)''',
            '''psspy.dscn(199343)''',
            '''psspy.dscn(199327)''',
            '''psspy.dscn(199344)''',
            '''psspy.dscn(199328)''',
            '''psspy.dscn(199329)''',
            '''psspy.branch_chng_3(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''psspy.dscn(199333)''',
            '''psspy.branch_chng_3(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)'''
            ],
            '43V-503':[
            '''psspy.dscn(199322)''',
            '''psspy.dscn(199341)''',
            '''psspy.dscn(199330)''',
            '''psspy.dscn(199332)''',
            '''psspy.dscn(199331)''',
            '''psspy.dscn(199342)''',
            '''psspy.dscn(199334)''',
            '''psspy.dscn(199324)''',
            '''psspy.dscn(199325)''',
            '''psspy.shunt_chng(199340,r"""2""",0,[_f,_f])''',
            '''psspy.dscn(199326)''',
            '''psspy.dscn(199343)''',
            '''psspy.dscn(199327)''',
            '''psspy.dscn(199344)''',
            '''psspy.dscn(199328)''',
            '''psspy.dscn(199329)''',
            '''psspy.branch_chng_3(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''psspy.branch_chng_3(199340,199345,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)'''
            ],
            '17V-512':[
            '''psspy.dscn(199301)''',
            '''psspy.branch_chng_3(199300,199340,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''psspy.dscn(199800)''',
            '''psspy.dscn(199801)''',
            '''psspy.dscn(199802)''',
            '''psspy.dscn(199803)''',
            '''psspy.dscn(199804)''',
            '''no_island()'''
            ],
            '17V-563':[
            '''psspy.dscn(199301)''',
            '''psspy.branch_chng_3(199201,199300,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''no_island()'''
            ],
            '51V-562':[
            '''psspy.dscn(199322)''',
            '''psspy.branch_chng_3(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''psspy.dscn(199333)''',
            '''psspy.branch_chng_3(199340,199345,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''no_island()'''
            ],
            '51V-521':[
            '''psspy.two_winding_chng_6(199345,199346,r"""1""",[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)''',
            '''psspy.shunt_chng(199346,r"""2""",0,[_f,_f])''',
            '''psspy.load_chng_5(199346,r"""1""",[0,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f])''',
            '''psspy.dscn(199360)''',
            '''psspy.dscn(199361)''',
            '''psspy.dscn(199358)''',
            '''psspy.dscn(199359)'''
            ],
            '99W-601':[
            '''psspy.dscn(199230)''',
            '''no_island()'''
            ],
            '99W-601_island':[
            '''psspy.dscn(199230)''',
            '''psspy.dscn(199367)''',
            '''psspy.dscn(199292)''',
            '''no_island()'''
            ],

#   IR671:Bear Lake 101V-POI
            # 101V-601
            # Outages L6054, L6004, 110W, IR671
            '101V-601_new':[
            '''psspy.dscn(199500)''',
            '''psspy.dscn(199501)''',
            '''psspy.dscn(199502)''',
            '''psspy.dscn(199503)''',
            '''psspy.dscn(199504)''',
            '''psspy.dscn(199508)''',
            '''psspy.dscn(199509)''',
            '''psspy.dscn(199510)''',
            '''psspy.dscn(199571)''',
            '''psspy.dscn(199572)''',
            '''psspy.dscn(199573)''',
            '''psspy.dscn(199574)'''
            ],

            # 101V-602
            # Outages L6004, IR671
            '101V-602_new':[
            '''psspy.dscn(199570)''',
            '''psspy.dscn(199571)''',
            '''psspy.dscn(199572)''',
            '''psspy.dscn(199573)''',
            '''psspy.dscn(199574)'''
            ],

            # 101V-604
            # Outages 110W, IR671
            '101V-604_new':[
            '''psspy.dscn(199501)''',
            '''psspy.dscn(199502)''',
            '''psspy.dscn(199503)''',
            '''psspy.dscn(199504)''',
            '''psspy.dscn(199508)''',
            '''psspy.dscn(199509)''',
            '''psspy.dscn(199510)''',
            '''psspy.dscn(199571)''',
            '''psspy.dscn(199572)''',
            '''psspy.dscn(199573)''',
            '''psspy.dscn(199574)'''
            ],

            # 101V-603
            # Outages L6054, 110W
            '101V-603_new':[
            '''psspy.branch_chng_3(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            '''psspy.dscn(199501)''',
            '''psspy.dscn(199502)''',
            '''psspy.dscn(199503)''',
            '''psspy.dscn(199504)''',
            '''psspy.dscn(199508)''',
            '''psspy.dscn(199509)''',
            '''psspy.dscn(199510)'''
            ],
            
            # 101V-L6004
            # Outages L6004
            '101V-L6004_new':[
            '''psspy.dscn(199570)''',
            ],
            
            # 101V-L6054
            # Outages L6054
            '101V-L6054_new':[
            '''psspy.branch_chng_3(199340,199500,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)''',
            ],

}
    #    return contingency
    
