#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Description:
# ===========================================================================
# Import standard libraries
import numpy as np
import math


def GetRayleighDampingCoef(DampRatio, Freq1, Freq2):
    # for testing
    Freq1 = 0.0
    Freq2 = 1.0
    DampRatio = 2.0
    # -------------------------
    chsi = DampRatio
    w1 = 2 * math.pi * Freq1
    w2 = 2 * math.pi * Freq2

    Dyna = (2 * chsi * w1 * w2) / (w1 + w2)
    Dynb = (2 * chsi) / (w1 + w2)
    return Dyna, Dynb



def GetNewmarkCoef(DynGama, DynBeta, TInc):
    # for testing
    C1 = 1/DynBeta/(TInc**2)
    C2 = -1/DynBeta/TInc
    C3 = -1/2/DynBeta
    C4 = DynGama/DynBeta/TInc
    C5 = -DynGama/DynBeta
    C6 = -(DynGama/2.0/DynBeta-1)*TInc
    return C1, C2, C3, C4, C5, C6
