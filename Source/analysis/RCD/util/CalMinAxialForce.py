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
import math
from itertools import zip_longest  # For establishing dictionary
# ===========================================================================
from analysis.RCD.variables import Model
from analysis.RCD.util.FindStress import FindStress

def CalSectionMinP():
    # ---------------------------------------------------------------------------------------
    ComIn = Model.Component
    MatIn = Model.Material
    MinAxial = 0
    for ii in ComIn.ID:
        eComArea = ComIn.Area[ii]
        ActMatID = ComIn.MatID[ii]
        MaxTenStrn = Model.GlobalViariables.MaxTenStrn
        YieldStress = FindStress(MaxTenStrn, ActMatID)
        # YieldStress = MatIn.MaxTenStrn[ActMatID]
        MinAxial += eComArea * YieldStress

    return MinAxial