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

def InitControlingStrain(tAnalF=1):

    # Initializing
    MaxComStrn = 999  # Positive
    MaxTenStrn = -999  # Initially positive
    if tAnalF == 1:
        tempout = 'Controling Strain for pure compression and tension:'
        print(f'    {tempout}')
    ##
    MatIn = Model.Material
    ##
    for ii in MatIn.ID:
        # Maximum compressive strain
        if MatIn.Kc[ii] > 0:
            if MatIn.Kc[ii] <= MaxComStrn:
                Model.GlobalViariables.MaxComStrn = MatIn.Kc[ii]

        # Maximum tensile strain - Only Steel
        if MatIn.MatType[ii] in [1, 3]:
            if abs(MatIn.Kt[ii]) <= abs(MaxTenStrn):
                Model.GlobalViariables.MaxTenStrn = MatIn.Kt[ii]
    if tAnalF == 1:
        print(f'    Max. Com. Strain    = {Model.GlobalViariables.MaxComStrn:10.5f}; Max. Ten. Strain    = {Model.GlobalViariables.MaxTenStrn:10.4f}')