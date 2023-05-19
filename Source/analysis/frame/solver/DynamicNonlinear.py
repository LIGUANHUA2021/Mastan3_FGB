#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software
#
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
import logging
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix
from scipy import linalg as LA
from scipy import interpolate
# Import internal functions
from analysis.frame.variables import Model, Result
from analysis.frame.file import OutputResults
from analysis.frame.util import Assembly
from analysis.frame.util import GetNorm
from analysis.frame.util import FormMtxg, DynParam
from analysis.frame.util.PrintLog import PrintLog as pl
from analysis.frame.element import NonsymWarpingBeam


def run():
    pl.Print("Start dynamic 2nd-order elastic analysis ...")
    #print("Start dynamic 2nd-order elastic analysis ...")
    OutputResults.IniResults()
    # Preparation
    # initialize KL
    KgL = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()
    Mg = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()
    AddMg = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()
    tKgL, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member,
                                    Model.Member.EleMtxL, Model.Member.EleMtxK, NonsymWarpingBeam, KgL, Model.Analysis.Type)
    Mg = FormMtxg.FormMg(Model.Material, Model.Section, Model.Node, Model.Member,
                         Model.Member.EleMtxL, Model.Analysis.MassType, NonsymWarpingBeam, Mg)
    tKgLs = np.array(tKgL)
    KgL, Fg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, tKgL, Model.Node.Fg)
    Kg0 = KgL # Linear Stiffness Matirx
    ## additional mass
    AddMg0 = FormMtxg.FormAddMg(Model.Analysis.AddMassDir, Model.Analysis.GraAcc, Model.Node, Model.JointLoad, AddMg)
    tMg0 = Mg + AddMg0
    Dyna,Dynb = DynParam.GetRayleighDampingCoef(Model.Analysis.DampingRatio, Model.Analysis.FirstFreq, Model.Analysis.SecondFreq)
    Mg0, Fg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, tMg0, Model.Node.Fg)
    ## Form damping matrix
    Cg0 = Dyna*Mg0+Dynb*Kg0
    # ---------------------------------------------------------------------------------
    ## Get Newmark parameters
    C1, C2, C3, C4, C5, C6 = DynParam.GetNewmarkCoef(Model.Analysis.NewmarkGamma, Model.Analysis.NewmarkBeta, Model.Analysis.Timeincr)
    ## Form Dynamic Stiffness Matrix
    DynKg = C1 * Mg0 + C4 * Cg0

    VecAcc = np.zeros(Model.Node.Count * 7)
    #model.TimeHistoryInfo.AccDir = 'Y-'
    tTimeX = Model.GroundAcceleration.TimeX
    tAccY = Model.GroundAcceleration.AccY
    TotGndMotTime = Model.GroundAcceleration.iterTime * (np.array(tTimeX).shape[0]-1)
    print(Model.GroundAcceleration.AccDir)
    for ii in np.arange(Model.Node.Count):
        if Model.GroundAcceleration.AccDir == 1:
            VecAcc[7 * ii + 0] = 1
        elif Model.GroundAcceleration.AccDir == 2:
            VecAcc[7 * ii + 1] = 1
        elif Model.GroundAcceleration.AccDir == 3:
            VecAcc[7 * ii + 2] = 1
    #---------------------------------------------------------------------------------
    # Begin Time Steps
    CurTim = 0   # Start time is 0
    CurStep = 0  # Current Step
    break_flag = 0
    TInc = Model.Analysis.Timeincr
    # Open memory for matrixes and vectors
    CurUg = np.zeros(Model.Node.Count * 7)
    CurVg = np.zeros(Model.Node.Count * 7)
    CurAg = np.zeros(Model.Node.Count * 7)
    # Open memory for matrixes and vectors
    CurU=np.zeros(Model.Node.Count * 7)
    LastU=np.zeros(Model.Node.Count * 7)
    ExecTime = min(TotGndMotTime, Model.Analysis.TotalTimeSteps)
    while CurTim < ExecTime:
        CurStep = CurStep + 1
        CurTim = CurTim + TInc
        # Update from previous incr
        CurU = LastU
        # ---------------------------------------------------------------------------
        # Get the delta ground acceleration at the time step
        tinterpfun = interpolate.interp1d(tTimeX, tAccY, kind='linear')
        Delacc = tinterpfun(CurTim)-tinterpfun(CurTim + TInc)
        NIter = 0 # Iteration Number
        # ---------------------------------------------------------------------------
        # Caclulate dynamic force - keep constant during time step
        DelFa = np.array(np.dot(np.dot(Mg0, VecAcc), Delacc))
        DelF1 = np.array(np.dot(-(C2 * Mg0 + C5 * Cg0), CurVg))
        DelF2 = np.array(np.dot(-(C3 * Mg0 + C6 * Cg0), CurAg))
        DelFeff = np.squeeze(DelFa + DelF1 + DelF2)
        DelUg = np.zeros(Model.Node.Count * 7)
        ResNormU = 1.0; ResNormF = 1.0
        while (NIter < 1 or ResNormU > Model.Analysis.TOL  or ResNormF > Model.Analysis.TOL):
            p_load = DelFeff
            NIter = NIter + 1
            # Step 1 : Formulate the effective stiffness matrix
            tKgL, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member, Model.Member.EleMtxL,
                                            Model.Member.EleMtxK, NonsymWarpingBeam, KgL, Model.Analysis.Type)
            KgL, Fg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, tKgL, Model.Node.Fg)
            keff = KgL + DynKg
            # ---------------------------------------------------------------------------
            # Step 2 : Calculate displacement increment
            DelU = np.linalg.solve(keff, DelFeff)
            CurU += DelU
            Model.Node.NodeUpdate(Model.Node, DelU)
            Rg = Result.CyCRes.GetRg(Model.Node, Model.Member, EleMtxK, DelU, Model.Analysis.Type)
            Rg = Result.CyCRes.GetNodeReaction(Model.Boundary, Model.Node, Rg)
            # Step 3 : Update geometry, velocity and accelerations and so on
            DelUg = DelU
            if NIter == 1:
                DelVg = C4 * DelUg + C5 * CurVg + C6 * CurAg
                DelAg = C1 * DelUg + C2 * CurVg + C3 * CurAg
            else:
                DelVg = C4 * DelUg
                DelAg = C1 * DelUg

            CurUg = CurUg + DelUg
            CurVg = CurVg + DelVg
            CurAg = CurAg + DelAg
            # ---------------------------------------------------------------------------
            tKgL2, EleMtxK2 = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member, Model.Member.EleMtxL,
                                              Model.Member.EleMtxK, NonsymWarpingBeam, KgL, Model.Analysis.Type)
            KgL2, Fg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, tKgL2, Model.Node.Fg)
            keff2 = KgL2 + DynKg
            DelFeff = DelFeff - np.squeeze(np.array(np.dot(keff2, DelUg)))

            ResNormU = LA.norm(DelUg) / LA.norm(CurUg)
            ResNormF = LA.norm(DelFeff) / LA.norm(Rg)
            if NIter == 1:
                SolnMsg1 = str("CURRENT TIME=  " + "%.4f"%CurTim + "; " + "TIME INCREMENT = " + "%.4f"%TInc)
                pl.Print(SolnMsg1)
            SolnMsg2 = str("ITER.= " + "%02d"%NIter + ";"+ " NORM detU/U,resF/FCE= " + str(format(ResNormU, "0.4e")) + ", " \
                           + str(format(ResNormF, "0.4e")))
            pl.Print(SolnMsg2)
            # -----------------------------------------------------------------------
            if NIter > Model.Analysis.MaxIter:
                pl.Print("Exceed max. iteration times!")
                break_flag = 1
                break
            # -----------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        if break_flag: break
        pl.Print("Incremental step has been completed ..." + '\n')
        # Save the last converged results
        Result.CyCRes.CurU = CurU
        Result.CyCRes.Time = CurTim
        Result.CyCRes.VEL = CurVg
        Result.CyCRes.ACC = CurAg
        # ---------------------------------------------------------------------------
        #outputResults.OutCyCRes()
        OutputResults.OutCyCRes(Result)
        # ---------------------------------------------------------------------------
    return