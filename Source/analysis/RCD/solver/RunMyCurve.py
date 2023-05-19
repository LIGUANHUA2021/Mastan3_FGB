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
# import numba as nb

# ===========================================================================
from analysis.RCD.variables import Model
from analysis.RCD.util.RotateToAngle import RotToAngle
from analysis.RCD.solver.CalSectionCapacityForMCur import CalSectCapacityForMCur
from analysis.RCD.solver.CalSectionCapacityForMCur import CalComCapacityForMCur
from analysis.RCD.util import CalMaxAxialForce
from analysis.RCD.util import CalMinAxialForce

# @nb.jit()
def RunMyCurve():
    # global KOUT, bRun_Analysis, NumResults, NumP, ResOut
    # global NumCom, ComIn, MatIn, AnaP
    # Constants
    PI = np.pi

    ##
    ComIn = Model.Component
    AnalInfo = Model.AnalysisInfo
    MatIn = Model.Material
    PosNStep = AnalInfo.AxialStep
    NegNStep = AnalInfo.AxialStep
    MomentStep = AnalInfo.MomentStep
    #
    MaxAxial = CalMaxAxialForce.CalSectionMaxP()
    MinAxial = CalMinAxialForce.CalSectionMinP()
    ##
    ## For testing %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    AnaP = np.zeros(1, dtype=float)
    # AnaP[0] = tAnaP/1e3
    #
    tAnaP = AnalInfo.Anap
    #
    if AnalInfo.AxialLoadType == 0:
        AnaP[0] = tAnaP
    elif AnalInfo.AxialLoadType == 1:
        AnaP[0] = tAnaP/100*MaxAxial
    ##
    ##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # AnaP = np.zeros(PosNStep + NegNStep, dtype=float)  ## PosNStep+NegNStep Axial load + Inputted by user
    # AnaP[0] = tAnaP/1e3
    # PNx_step = MaxAxial / PosNStep
    # NNx_step = MinAxial / NegNStep
    # for i in np.arange(1, PosNStep):
    #     tAxialP = MaxAxial - i * PNx_step
    #     AnaP[i] = tAxialP/1e3
    # for j in np.arange(NegNStep):
    #     tAxialP = j * NNx_step
    #     AnaP[PosNStep + j] = tAxialP/1e3
    ##------------------------------------------------------------

    # Declarations
    InNx, InAngle, OutMy, OutMz = 0, 0, 0, 0
    IsConvergence, IsSubConvergence = True, True
    II, JJ, KK = 0, 0, 0
    dA, ncur, minstr, matstr, EA, limN, tOutStrn, TempComStr, TempTenStr = 0, 0, 0, 0, 0, 0, 0, 0, 0
    MoN, LoN, PreN = 0, 0, 0
    Mst, Lst = 0, 0
    tA = 0

    print("   Run My Curvature analysis ...")

    # NumResults = (NumP) * (MomentStep + 1)
    # ResOut = [0] * NumResults
    # tNumRes = 0
    # NumResults = 0

    bRun_Analysis = True

    minstr = 0.0035
    InAngle = PI / 2
    tA = -1 * InAngle

    for ii in ComIn.ID:
        RotToAngle(tA, ii)  # Rotate to current angle

    TempComStr = 0.2
    TempTenStr = -0.2
    for ii in ComIn.ID:
        ActMatID = ComIn.MatID[ii]
        if MatIn.Kc[ActMatID] < TempComStr:
            TempComStr = MatIn.Kc[ActMatID]
        if ComIn.ComType[ii] != 2:
            if TempTenStr < MatIn.Kt[ActMatID]:
                TempTenStr = MatIn.Kt[ActMatID]

    Idn = -100000
    PreN = 0.00001
    ##
    # NumResults = 1
    ## Reset Results
    Model.MomentCurvatureResults.ResetMyCurva()
    ##
    for ii in np.arange(len(AnaP)):
        InNx = AnaP[ii]
        IsConvergence = True
        Counter = 0
        if InNx == 0:
            ncur = 0
        elif InNx > 0:
            tOutStrn = 0
            LoN = 0
            Lst = tOutStrn

            tOutStrn = TempComStr
            TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
            MoN = TN
            Mst = tOutStrn
            tDn = TN - InNx

            while abs(tDn) > PreN:
                if abs(MoN - LoN) > 0.001:
                    tOutStrn = (Mst - Lst) / (MoN - LoN) * (InNx - LoN) + Lst
                    TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
                    tDn = TN - InNx
                    if TN > InNx:
                        MoN = TN
                        Mst = tOutStrn

                    if TN < InNx:
                        LoN = TN
                        Lst = tOutStrn

                    Counter += 1
                    if Counter >= 1000:
                        IsConvergence = False
                        break

                    if abs(Mst - Lst) <= 0.000005:
                        tDn = 0  # Converged result

                else:
                    IsConvergence = False
                    break

        elif InNx < 0:
            tOutStrn = TempTenStr
            TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
            LoN = TN
            Lst = tOutStrn
            tOutStrn = 0
            TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
            MoN = TN
            Mst = tOutStrn
            tDn = TN - InNx

            while abs(tDn) > PreN:
                if abs(MoN - LoN) > 0.001:
                    tOutStrn = (Mst - Lst) / (MoN - LoN) * (InNx - LoN) + Lst
                    TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
                    tDn = TN - InNx
                    if TN > InNx:
                        MoN = TN
                        Mst = tOutStrn

                    if TN < InNx:
                        LoN = TN
                        Lst = tOutStrn

                    Counter += 1
                    if Counter >= 1000:
                        IsConvergence = False
                        break

                    if abs(Mst - Lst) <= 0.000005:
                        tDn = 0  # Converged result

                else:
                    IsConvergence = False
                    break

        if IsConvergence:
            ncur = tOutStrn
            InAngle = 0  # My Curvature=0 Mz Curvature=PI/2
            # IsSubConvergence = True
            NumResults = ii * MomentStep
            IsCalConvergence = CalSectCapacityForMCur(InNx, InAngle, MaxAxial, MinAxial, ncur, NumResults)
        # print("********************************************************************************")
        # print("--------------------------------------------------------------------------------")
        print(f"    >>> Analysis under axial load = {InNx:.2f}, Convergence = {'Ture' if IsCalConvergence else 'False'}")
        print(" ")

        # InAngle = 0  # My Curvature=0 Mz Curvature=PI/2
        # IsSubConvergence = True
        # NumResults = ii * MomentStep
        # IsConvergence = CalSectCapacityForMCur(InNx, InAngle, MaxAxial, MinAxial, ncur, NumResults)
        # print(f"    >>> Analysis under axial load = {InNx / 1000:.2f} kN, Converge = {'Ture' if IsConvergence else 'False'}")

