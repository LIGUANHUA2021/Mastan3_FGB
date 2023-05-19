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

def SteelPanToCG(tComID: int):
    Section = Model.Section
    tComIn = Model.Component
    # shift the center of gravity of the component to the origin
    tComIn.cy[tComID] -= Section.gcy
    tComIn.cz[tComID] -= Section.gcz
    # shift the coordinates of the external points to the origin
    tCompSFibers = tComIn.CompFibersInfo[tComID]
    tFibers = np.array(tCompSFibers["Fibers"])
    for ii in np.arange(len(tFibers)):
        tFibers[ii, 1] -= Section.gcy
        tFibers[ii, 2] -= Section.gcz
    # Update the Fibers coordinate
    tComIn.CompFibersInfo[tComID]["Fibers"] = tFibers
    return

def RebarPanToCG(tComID: int):
    Section = Model.Section
    tComIn = Model.Component
    # shift the center of gravity of the component to the origin
    tComIn.cy[tComID] -= Section.gcy
    tComIn.cz[tComID] -= Section.gcz
    # shift the coordinates of the external points to the origin
    tCompSFibers = tComIn.CompFibersInfo[tComID]
    tFibers = np.array(tCompSFibers["Fibers"])
    for ii in np.arange(len(tFibers)):
        tFibers[ii, 1] -= Section.gcy
        tFibers[ii, 2] -= Section.gcz
    # Update the Fibers coordinate
    tComIn.CompFibersInfo[tComID]["Fibers"] = tFibers
    return

def ConcretePanToCG(tComID: int):
    Section = Model.Section
    tComIn = Model.Component
    # shift the center of gravity of the component to the origin
    tComIn.cy[tComID] -= Section.gcy
    tComIn.cz[tComID] -= Section.gcz
    # shift the coordinates of the external points to the origin
    tCompSFibers = tComIn.CompFibersInfo[tComID]
    tFibers = np.array(tCompSFibers["Fibers"])
    for ii in np.arange(len(tFibers)):
        tFibers[ii, 1] -= Section.gcy
        tFibers[ii, 2] -= Section.gcz
    # Update the Fibers coordinate
    tComIn.CompFibersInfo[tComID]["Fibers"] = tFibers
    return