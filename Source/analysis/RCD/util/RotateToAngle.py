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

def RotToAngle(tAngle, tComID):
    # ---------------------------------------------------------------------------------------
    # Note:
    #     u=z*cos(dA)-y*sin(dA)
    #     v=z*sin(dA)+y*cos(dA)
    #
    # Anti-Clockwise rotate!
    # ---------------------------------------------------------------------------------------
    ComIn = Model.Component
    dA = tAngle

    # Initial boundary of the component
    ComIn.MaxV[tComID] = -9999
    ComIn.MinV[tComID] = 9999
    ComIn.MaxW[tComID] = -9999
    ComIn.MinW[tComID] = 9999

    # Fibers or rebars
    tCompSFibers = ComIn.CompFibersInfo[tComID]
    tFibers = np.array(tCompSFibers["Fibers"])
    tV = np.array([])   ## refer to ty
    tW = np.array([])   ## refer to tz
    if tFibers.shape[1] > 4:
        tFibers = tFibers[:, :4]
    tNew_cols = np.zeros((len(tFibers), 2))
    tEdit_Fibers = np.hstack((tFibers, tNew_cols))
    for ii in np.arange(len(tFibers)):
        ty = tFibers[ii, 1]
        tz = tFibers[ii, 2]
        tv = tz * np.sin(dA) - ty * np.cos(dA)
        tw = tz * np.cos(dA) + ty * np.sin(dA)
        tV = np.append(tV, [tv])
        tW = np.append(tW, [tw])
        # ---------------------------------
        if tv >= ComIn.MaxV[tComID]:
            ComIn.MaxV[tComID] = tv
        if tv <= ComIn.MinV[tComID]:
            ComIn.MinV[tComID] = tv
        if tw >= ComIn.MaxW[tComID]:
            ComIn.MaxW[tComID] = tw
        if tw <= ComIn.MinW[tComID]:
            ComIn.MinW[tComID] = tw
        # ---------------------------------
    # tV = tV.reshape((len(tFibers), 1))
    # tW = tW.reshape((len(tFibers), 1))
    tV = tV.reshape((1, len(tFibers)))
    tW = tW.reshape((1, len(tFibers)))
    # print("shape of tEdit_Fibers", tEdit_Fibers.shape)
    # print("shape of tV", tV.shape)
    tEdit_Fibers[::, 4] = tV
    tEdit_Fibers[::, 5] = tW
    # tFibers = np.append(tFibers, tV, axis=1)
    # tFibers = np.append(tFibers, tW, axis=1)
    ComIn.CompFibersInfo[tComID]["Fibers"] = tEdit_Fibers
    return