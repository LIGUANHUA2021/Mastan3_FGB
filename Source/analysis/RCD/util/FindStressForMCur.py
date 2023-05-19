#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
#import math
# ===========================================================================
from analysis.RCD.variables import Model

def FindStressForMCur(CurStrn, CurMatID):
    # global RunType, MatIn

    ##
    MatIn = Model.Material
    if CurStrn < 0:
        CurStress = 0
        return CurStress

    if MatIn.MatProperty[CurMatID] == 1:  # Simple property
        # if RunType == 0:  # ULS
        #     CurStress = CurStrn * MatIn[CurMatID]['pc'] / MatIn[CurMatID]['kc']
        #     if CurStress > MatIn[CurMatID]['pc']:
        #         CurStress = MatIn[CurMatID]['pc']
        # if RunType == 1:  # SLS
        CurStress = CurStrn * MatIn.Fc[CurMatID]/ MatIn.Kc[CurMatID]
        CurStress = min(CurStress, MatIn.Fc[CurMatID])

    # else:  # Advanced property
    #     if abs(CurStrn) >= MatIn[CurMatID]['CurStrain'][MatIn[CurMatID]['CurNum']]:
    #         CurStress = MatIn[CurMatID]['CurStress'][MatIn[CurMatID]['CurNum']]
    #         return CurStress
    #
    #     for JJ in range(MatIn[CurMatID]['CurZero'], MatIn[CurMatID]['CurNum'] + 1):
    #         if MatIn[CurMatID]['CurStrain'][JJ] > abs(CurStrn):
    #             if JJ == 1:
    #                 s1 = 0
    #                 n1 = 0
    #             else:
    #                 s1 = MatIn[CurMatID]['CurStress'][JJ - 1]
    #                 n1 = MatIn[CurMatID]['CurStrain'][JJ - 1]
    #
    #             s2 = MatIn[CurMatID]['CurStress'][JJ]
    #             n2 = MatIn[CurMatID]['CurStrain'][JJ]
    #
    #             CurStress = s1 + (abs(CurStrn) - n1) * (s2 - s1) / (n2 - n1)
    #             return CurStress

    return CurStress

