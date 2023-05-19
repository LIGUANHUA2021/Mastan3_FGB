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

def InitFibers(tAnalF=1):
    ##
    tNumFiber = 0
    if tAnalF == 1:
        print('INITIALIZING FIBERS ...')
    ##
    ComIn = Model.Component
    ##
    for ii in ComIn.ID:
        if ComIn.ComType[ii] in [1, 2, 3]:
            ## Get the number of Fibers by Component ID
            tCompFibers = np.array(ComIn.CompFibersInfo[ii]["Fibers"])
            tNumFiber += len(tCompFibers)
    if tAnalF == 1:
        print(f"Total number of initialized fibers = {tNumFiber}")