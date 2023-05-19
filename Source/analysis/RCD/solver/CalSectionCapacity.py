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
from analysis.RCD.util import CalMaxAxialForce
from analysis.RCD.util import CalMinAxialForce
from analysis.RCD.util.FindStress import FindStress
from analysis.RCD.util.RotateToAngle import RotToAngle

def CalSectCapacity(in_px, in_angle, max_axial, min_axial, strnContType=0, strnatVal=999):
    ##
    ComIn = Model.Component
    MatIn = Model.Material
    # max_axial = CalMaxAxialForce.CalSectionMaxP()
    # min_axial = CalMinAxialForce.CalSectionMinP()
    # AnalInfo = Model.AnalysisInfo
    max_iter = Model.AnalysisInfo.MaxIter
    cur_max_iter = max_iter
    ##
    # For numerical stability, 0.5% of reduction is included.
    in_px = min(max_axial * 0.995, in_px) if in_px > max_axial else in_px
    in_px = max(min_axial * 0.995, in_px) if in_px < min_axial else in_px

    # For some extreme case, interaction times is increased.
    if in_px > 0.9 * max_axial or in_px < 0.9 * min_axial or abs(in_px) < 100:
        cur_max_iter = max_iter * 100

    # Initializing
    out_my = 0
    out_mz = 0
    is_convergence = True

    cur_angle = in_angle
    ta = -1 * in_angle
    ##
    for ii in ComIn.ID:
        RotToAngle(ta, ii)  # Rotate to current angle

    # Find initial neutral axis height
    idn = 0

    max_com_str = 0.0035  # Default value
    max_com_v = 0.035
    max_ten_str = 0.02  # Default value
    min_ten_v = 0.2

    ## For testing
    # if abs(in_px-1197.00*1e3) < 1e-3:
    #     print("This is for testing")
    ## For testing


    for ii in ComIn.ID:
        # Maximum Compressive Strain and Location
        if ComIn.MaxV[ii] > 0:
            ActMatId = ComIn.MatID[ii]
            ## Strain Controlling
            if strnContType == 0:
                temp_com_str = MatIn.Kc[ActMatId]
            elif strnContType == 1:
                temp_com_str = MatIn.Fc[ActMatId]/MatIn.E[ActMatId]
            elif strnContType == 2:
                temp_com_str = strnatVal
            ##
            if abs(temp_com_str / ComIn.MaxV[ii]) < abs(max_com_str / max_com_v):
                max_com_str = temp_com_str
                max_com_v = ComIn.MaxV[ii]

        # Minimum Tensile Strain and Location
        if ComIn.MinV[ii] < 0:
            if ComIn.ComType[ii] != 2:
                ActMatId = ComIn.MatID[ii]
                ## Strain Controlling
                if strnContType == 0:
                    temp_com_str = MatIn.Kc[ActMatId]
                elif strnContType == 1:
                    temp_com_str = MatIn.Ft[ActMatId] / MatIn.E[ActMatId]
                elif strnContType == 2:
                    temp_com_str = strnatVal
                ##
                temp_ten_str = MatIn.Kt[ActMatId]
                if abs(temp_ten_str / ComIn.MinV[ii]) < abs(max_ten_str / min_ten_v):
                    max_ten_str = temp_ten_str
                    min_ten_v = ComIn.MinV[ii]

    idn_limt = (max_ten_str * max_com_v - max_com_str * min_ten_v) / (max_ten_str - max_com_str)
    ##
    Model.GlobalViariables.MaxComStr = max_com_str    ## The maximum compression strain of whole section
    Model.GlobalViariables.MaxComV = max_com_v        ## The Location of maximum compression strain in present whole section
    Model.GlobalViariables.MaxTenStr = max_ten_str    ## The maximum tension strain of whole section
    Model.GlobalViariables.MinTenV = min_ten_v        ## The Location of maximum tension strain in present whole section
    Model.GlobalViariables.Idn_limt = idn_limt        ## The neutral axis depth
    ##
    # Initializing variables
    Counter = 0
    tDn = 0
    CurN = in_px

    # PreN is the tolerance of the iteration 0.01% of the axial force
    PreN = abs(in_px / 10000000)
    if PreN == 0:
        PreN = 0.00001

    Idn = idn_limt

    # Idn=0

    TN, TMy, TMz = Cal_ComponentCapacity(Idn)
    MoN = TN
    Mdn = Idn

    if CurN >= MoN:  # Compressive strain control
        # To store lower bound
        LoN = MoN
        Ldn = Mdn
        # To find upper bound
        TempStr = max_ten_str
        MaxTenStr = 0.9999 * max_com_str
        Idn = min_ten_v - MaxTenStr * (max_com_v - min_ten_v) / (max_com_str - MaxTenStr)
        TN, TMy, TMz = Cal_ComponentCapacity(Idn)
        MaxTenStr = TempStr
        ##
        Model.GlobalViariables.MaxTenStr = MaxTenStr
        ##
        MoN = TN
        Mdn = Idn
    else:  # Tensile strain control
        # To find lower bound
        TempStr = max_com_str
        MaxComStr = 0.9999 * max_ten_str
        Idn = min_ten_v - max_ten_str * (max_com_v - min_ten_v) / (MaxComStr - max_ten_str)
        TN, TMy, TMz = Cal_ComponentCapacity(Idn)
        MaxComStr = TempStr
        ##
        Model.GlobalViariables.MaxComStr = MaxComStr
        ##
        LoN = TN
        Ldn = Idn

    tDn = TN - in_px

    # ---------------------------------------------------------------------------------------
    while abs(tDn) > PreN:
        if abs(MoN - LoN) > 0.001:
            Idn = (Mdn - Ldn) / (MoN - LoN) * (in_px - LoN) + Ldn
            # Idn = (Mdn - Ldn) / (MoN - LoN) * (InNx - LoN) * (InNx - LoN) / (MoN - LoN)+ Ldn
            TN, TMy, TMz = Cal_ComponentCapacity(Idn)
            tDn = TN - in_px
            if TN > in_px:
                MoN = TN
                Mdn = Idn

            if TN < in_px:
                LoN = TN
                Ldn = Idn

            Counter += 1
            if Counter > cur_max_iter:
                is_convergence = False
                break

            if abs(Mdn - Ldn) <= 0.005:
                tDn = 0  # Converged result
        else:
            is_convergence = False
            break

    # ---------------------------------------------------------------------------------------
    # Save the neutral axis
    Dn = Idn
    # print("Counter = ", Counter)
    # Output Moment Capacities
    # Revise at 2013-03-20
    OutMy = TMy * np.cos(in_angle) - TMz * np.sin(in_angle)
    OutMz = TMy * np.sin(in_angle) + TMz * np.cos(in_angle)

    return OutMy, OutMz, Dn, is_convergence

# def RotateToAngle(tAngle, tComID):
#     # ---------------------------------------------------------------------------------------
#     # Note:
#     #     u=z*cos(dA)-y*sin(dA)
#     #     v=z*sin(dA)+y*cos(dA)
#     #
#     # Anti-Clockwise rotate!
#     # ---------------------------------------------------------------------------------------
#     ComIn = Model.Component
#     dA = tAngle
#
#     # Initial boundary of the component
#     ComIn.MaxV[tComID] = -9999
#     ComIn.MinV[tComID] = 9999
#     ComIn.MaxW[tComID] = -9999
#     ComIn.MinW[tComID] = 9999
#
#     # Fibers or rebars
#     tCompSFibers = ComIn.CompFibersInfo[tComID]
#     tFibers = np.array(tCompSFibers["Fibers"])
#     tV = np.array([])   ## refer to ty
#     tW = np.array([])   ## refer to tz
#     if tFibers.shape[1] > 4:
#         tFibers = tFibers[:, :4]
#     tNew_cols = np.zeros((len(tFibers), 2))
#     tEdit_Fibers = np.hstack((tFibers, tNew_cols))
#     for ii in np.arange(len(tFibers)):
#         ty = tFibers[ii, 1]
#         tz = tFibers[ii, 2]
#         tv = tz * np.sin(dA) - ty * np.cos(dA)
#         tw = tz * np.cos(dA) + ty * np.sin(dA)
#         tV = np.append(tV, [tv])
#         tW = np.append(tW, [tw])
#         # ---------------------------------
#         if tv >= ComIn.MaxV[tComID]:
#             ComIn.MaxV[tComID] = tv
#         if tv <= ComIn.MinV[tComID]:
#             ComIn.MinV[tComID] = tv
#         if tw >= ComIn.MaxW[tComID]:
#             ComIn.MaxW[tComID] = tw
#         if tw <= ComIn.MinW[tComID]:
#             ComIn.MinW[tComID] = tw
#         # ---------------------------------
#     # tV = tV.reshape((len(tFibers), 1))
#     # tW = tW.reshape((len(tFibers), 1))
#     tV = tV.reshape((1, len(tFibers)))
#     tW = tW.reshape((1, len(tFibers)))
#     # print("shape of tEdit_Fibers", tEdit_Fibers.shape)
#     # print("shape of tV", tV.shape)
#     tEdit_Fibers[::, 4] = tV
#     tEdit_Fibers[::, 5] = tW
#     # tFibers = np.append(tFibers, tV, axis=1)
#     # tFibers = np.append(tFibers, tW, axis=1)
#     ComIn.CompFibersInfo[tComID]["Fibers"] = tEdit_Fibers
#     return


def Cal_ComponentCapacity(tIdn):
    # ---------------------------------------------------------------------------------------
    MaxComStr = Model.GlobalViariables.MaxComStr
    MaxComV = Model.GlobalViariables.MaxComV
    MinTenV = Model.GlobalViariables.MinTenV
    MaxTenStr = Model.GlobalViariables.MaxTenStr
    Idn_limt = Model.GlobalViariables.Idn_limt
    # ---------------------------------------------------------------------------------------
    oNx = 0
    oMy = 0
    oMz = 0

    temNx = 0
    temMy = 0
    temMz = 0
    # ---------------------------------------------------------------------------------------
    # Determine strain distribution
    tOutStrn = MaxComStr

    if tIdn < Idn_limt:  # Compressive strain control
        tOutStrn = MaxComStr
    else:  # Tensile strain control
        tOutStrn = MaxTenStr * (tIdn - MaxComV) / (tIdn - MinTenV)
    # ---------------------------------------------------------------------------------------
    ComIn = Model.Component
    for ii in ComIn.ID:
        if ComIn.ComType[ii] == 1:  # Steel
            temNx, temMy, temMz = Cal_SteelCapacity(ii, tIdn, tOutStrn)
        # elif ComIn.ComType[ii] == 2:  # Concrete
        #     temNx, temMy, temMz = Cal_ConcreteCapacity(ii, tIdn, tOutStrn)
        elif ComIn.ComType[ii] == 3:  # Rebar
            temNx, temMy, temMz = Cal_RebarCapacity(ii, tIdn, tOutStrn)

        oNx += temNx
        oMy += temMy
        oMz += temMz
    # ---------------------------------------------------------------------------------------
    return oNx, oMy, oMz

def Cal_SteelCapacity(tComID, tIdn, tOutStrn):
    # ---------------------------------------------------------------------------------------
    oNx = 0
    oMy = 0
    oMz = 0
    # ---------------------------------------------------------------------------------------
    ComIn = Model.Component
    MaxComV = Model.GlobalViariables.MaxComV
    tCompSFibers = ComIn.CompFibersInfo[tComID]
    tFibers = np.array(tCompSFibers["Fibers"])
    # ---------------------------------------------------------------------------------------
    for ii in np.arange(len(tFibers)):
        t_V = tFibers[ii, 4]
        t_W = tFibers[ii, 5]
        eAs = tFibers[ii, 3]
        eFs = 0.0

        # linear proportion
        eStrain = tOutStrn * (t_V - tIdn) / (MaxComV - tIdn)
        ActMatID = ComIn.MatID[tComID]

        # Add residual strain
        # rStrain = tComIn.AlpStrs * abs(MatIn[ActMatID].pc) / MatIn[ActMatID].E
        # eStrain += rStrain
        ##
        YStress = FindStress(eStrain, ActMatID)
        eFs = eAs * YStress
        ##
        oNx += eFs
        oMy += eFs * t_W
        oMz += eFs * t_V
    # ---------------------------------------------------------------------------------------
    return oNx, oMy, oMz


def Cal_ConcreteCapacity(tComID, tIdn, tOutStrn):

    return


def Cal_RebarCapacity(tComID, tIdn, tOutStrn):
    # ---------------------------------------------------------------------------------------
    oNx = 0
    oMy = 0
    oMz = 0
    # ---------------------------------------------------------------------------------------
    ComIn = Model.Component
    MaxComV = Model.GlobalViariables.MaxComV
    tCompSFibers = ComIn.CompFibersInfo[tComID]
    tFibers = np.array(tCompSFibers["Fibers"])
    # ---------------------------------------------------------------------------------------
    for ii in np.arange(tFibers):
        t_V = tFibers[ii, 4]
        t_W = tFibers[ii, 5]
        eAs = tFibers[ii, 3]
        eFs = 0.0

        # linear proportion
        eStrain = tOutStrn * (t_V - tIdn) / (MaxComV - tIdn)
        ActMatID = ComIn.MatID[tComID]
        eFs = eAs * FindStress(eStrain, ActMatID)

        oNx += eFs
        oMy += eFs * t_W
        oMz += eFs * t_V
    # ---------------------------------------------------------------------------------------
    return oNx, oMy, oMz