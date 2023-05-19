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
# import numba
# ===========================================================================
from analysis.RCD.variables import Model
from analysis.RCD.util.FindStress import FindStress
from analysis.RCD.util.FindStressForMCur import FindStressForMCur

def CalSectCapacityForMCur(InNx, InAngle, MaxAxial, MinAxial, ncur, NumResults):
    # global NumCom, ComIn, MatIn, MomentStep, MaxIter, MaxAxial, MinAxial, NumResults, ResOut
    ##
    ComIn = Model.Component
    MatIn = Model.Material
    #
    AnalInfo = Model.AnalysisInfo
    MomentStep = AnalInfo.MomentStep
    ##
    max_iter = Model.AnalysisInfo.MaxIter
    CurMaxIter = max_iter
    #
    CurMaxIter = 10000

    InNx = min(MaxAxial * 0.995, InNx) if InNx > MaxAxial else InNx
    InNx = max(MinAxial * 0.995, InNx) if InNx < MinAxial else InNx

    if InNx > (0.9 * MaxAxial) or InNx < (0.9 * MinAxial) or abs(InNx) < 100:
        CurMaxIter = max_iter * 100

    #---------------------------------------------------------------------------------------
    #Initializing
    OutMy = 0.0
    OutMz = 0.0
    OutNx = 0.0
    IsConvergence = True
    CurAngle = InAngle
    #---------------------------------------------------------------------------------------
    #Find initial neutral axis height
    Idn = 0

    MaxComStr = 0.0035
    MaxComV = 0.035
    MaxTenStr = 0.02
    MinTenV = 0.2

    for ii in ComIn.ID:
        if ComIn.MaxV[ii] > 0:
            ActMatID = ComIn.MatID[ii]
            TempComStr = MatIn.Kc[ActMatID]
            if abs(TempComStr / ComIn.MaxV[ii]) < abs(MaxComStr / MaxComV):
                MaxComStr = TempComStr
                MaxComV = ComIn.MaxV[ii]

        if ComIn.MinV[ii] < 0 and ComIn.ComType[ii] != 2:
            ActMatID = ComIn.MatID[ii]
            TempTenStr = MatIn.Kt[ActMatID]
            if abs(TempTenStr / ComIn.MinV[ii]) < abs(MaxTenStr / MinTenV):
                MaxTenStr = TempTenStr
                MinTenV = ComIn.MinV[ii]

    Idn_limt = (MaxTenStr * MaxComV - MaxComStr * MinTenV) / (MaxTenStr - MaxComStr)
    #
    Model.GlobalViariables.MaxComStr = MaxComStr    ## The maximum compression strain of whole section
    Model.GlobalViariables.MaxComV = MaxComV        ## The Location of maximum compression strain in present whole section
    Model.GlobalViariables.MaxTenStr = MaxTenStr    ## The maximum tension strain of whole section
    Model.GlobalViariables.MinTenV = MinTenV        ## The Location of maximum tension strain in present whole section
    Model.GlobalViariables.Idn_limt = Idn_limt      ## The neutral axis depth
    ##
    Counter = 0
    tDn = 0
    CurN = InNx
    PreN = abs(InNx / 10000000)
    PreN = 0.00001 if PreN == 0 else PreN
    ##
    Idn = Idn_limt
    ##
    de = (MaxComStr - ncur) / MomentStep
    ##
    # NumResults = 1
    ##
    for ii in np.arange(1, MomentStep+1):
        tOutStrn = ncur + de * ii
        TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
        MoN = TN
        Mdn = Idn

        if CurN >= MoN:
            LoN = MoN
            Ldn = Mdn
            TempStr = MaxTenStr
            MaxTenStr = 0.9999 * MaxComStr
            Idn = MinTenV - MaxTenStr * (MaxComV - MinTenV) / (MaxComStr - MaxTenStr)
            TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
            MaxTenStr = TempStr
            ##
            Model.GlobalViariables.MaxTenStr = MaxTenStr
            ##
            MoN = TN
            Mdn = Idn
        else:
            TempStr = MaxComStr
            MaxComStr = 0.9999 * MaxTenStr
            Idn = MaxComV - 0.01
            TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
            MaxComStr = TempStr
            ##
            Model.GlobalViariables.MaxComStr = MaxComStr
            ##
            LoN = TN
            Ldn = Idn
        tDn = TN - InNx

        while abs(tDn) > PreN:
            if abs(MoN - LoN) > 0.001:
                Idn = (Mdn - Ldn) / (MoN - LoN) * (InNx - LoN) + Ldn
                TN, TMy, TMz = CalComCapacityForMCur(Idn, tOutStrn)
                tDn = TN - InNx

                if TN > InNx:
                    MoN = TN
                    Mdn = Idn

                if TN < InNx:
                    LoN = TN
                    Ldn = Idn

                Counter += 1
                if Counter >= CurMaxIter:
                    IsConvergence = False
                    break

                if abs(Mdn - Ldn) <= 0.005:
                    tDn = 0

            else:
                IsConvergence = False
                break
        #print("Counter = ", Counter)
        if IsConvergence:
            Tempt = tOutStrn * (Idn - MinTenV) / (Idn - MaxComV)
            if Tempt >= abs(MaxTenStr):
                break
            ##
            t_an = tOutStrn / (MaxComV - Idn) * 1000
            OutMy = TMy
            OutMz = TMz
            OutNx = CurN
            if abs(InAngle-0) < 1e-3:
                Model.MomentCurvatureResults.ONx_y.setdefault(NumResults, OutNx)
                Model.MomentCurvatureResults.Oan_y.setdefault(NumResults, t_an)
                Model.MomentCurvatureResults.OMy_y.setdefault(NumResults, OutMy)
                Model.MomentCurvatureResults.OMz_y.setdefault(NumResults, OutMz)
                Model.MomentCurvatureResults.Idn_y.setdefault(NumResults, Idn)
                Model.MomentCurvatureResults.OutStrn_y.setdefault(NumResults, tOutStrn)
                ##
                tOutStrs = 0.0
                for kk in ComIn.ID:
                    ActMatID = ComIn.MatID[kk]
                    teStress = FindStress(tOutStrn, ActMatID)
                    tOutStrs += teStress
                Model.MomentCurvatureResults.OutStrs_y.setdefault(NumResults, tOutStrs)
                ##
            elif abs(InAngle-np.pi/2.0) < 1e-3:
                Model.MomentCurvatureResults.ONx_z.setdefault(NumResults, OutNx)
                Model.MomentCurvatureResults.Oan_z.setdefault(NumResults, t_an)
                Model.MomentCurvatureResults.OMy_z.setdefault(NumResults, OutMy)
                Model.MomentCurvatureResults.OMz_z.setdefault(NumResults, OutMz)
                Model.MomentCurvatureResults.Idn_z.setdefault(NumResults, Idn)
                Model.MomentCurvatureResults.OutStrn_z.setdefault(NumResults, tOutStrn)
                ##
                tOutStrs = 0.0
                for jj in ComIn.ID:
                    ActMatID = ComIn.MatID[jj]
                    teStress = FindStress(tOutStrn, ActMatID)
                    tOutStrs += teStress
                Model.MomentCurvatureResults.OutStrs_z.setdefault(NumResults, tOutStrs)
                ##
            NumResults += 1
            # ResOut[NumResults]['an'] = tOutStrn / (MaxComV - Idn) * 1000
            # ResOut[NumResults]['Nx'] = CurN
            # ResOut[NumResults]['My'] = TMz
            # ResOut[NumResults]['Mz'] = TMz
            # NumResults += 1

        else:
            IsConvergence = False
            break
        print(f"    >>> Curvature Step = {int(ii)}, Current Moment =".ljust(45, ' ') +f"{OutMz:.2f}, Convergence = {'Ture' if IsConvergence else 'False'}".rjust(35, ' '))

    return IsConvergence


def CalComCapacityForMCur(tIdn, tOutStrn):
    # global NumCom, ComIn
    ComIn = Model.Component
    oNx = 0
    oMy = 0
    oMz = 0

    for ii in ComIn.ID:
        temNx = 0
        temMy = 0
        temMz = 0

        if ComIn.ComType[ii] == 1:  # Steel
            temNx, temMy, temMz = Cal_SteelCapacity(ii, tIdn, tOutStrn)

        # if ComIn.ComType[ii] == 2:  # Concrete
        #     temNx, temMy, temMz = Cal_ConcreteCapacity(ii, tIdn, tOutStrn)

        if ComIn.ComType[ii] == 3:  # Rebar
            temNx, temMy, temMz = Cal_RebarCapacity(ii, tIdn, tOutStrn)

        oNx += temNx
        oMy += temMy
        oMz += temMz

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