#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Internal

# External
import pyqtgraph as pg
import numpy as np
#############################################################################

#Class list
class Nodes:
    MaxNodeNum = 2000
    NodeNum=[]; Nodexval=[]; Nodeyval=[]; Nodezval=[]
    Nodepos = np.empty((MaxNodeNum, 3))  #
    Nodesize = np.empty((MaxNodeNum))  #
    Nodecolor = np.empty((MaxNodeNum, 4)) #



#=========================================================================================
if __name__ == '__main__':
    pg.exec()
#=========================================================================================
# END OF PROGRAM
#=========================================================================================