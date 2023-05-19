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
from scipy import linalg as LA
import math
import logging,os
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix
# Import internal functions
from analysis.frame.variables import Model, Result
from analysis.frame.file import OutputResults
from analysis.frame.element import NonsymWarpingBeam
from analysis.frame.element import SoilBoundaryElement
from analysis.frame.util import Assembly
from analysis.frame.util import FormMtxg
from analysis.frame.util import LoadFactor
from analysis.frame.util import GetNorm
from analysis.frame.util.PrintLog import PrintLog as pl
from analysis.frame.util import ActiveDOF

def run():
    pl.Print("Start 2nd-order elastic analysis ...")
    # Preparation
    incLF = Model.Analysis.TargetLF / Model.Analysis.LoadStep
    DelF = incLF * Model.Node.Fg
    OutputResults.IniResults()
    # Open memory for matrixes and vectors
    CurU=np.zeros(Model.Node.Count * 7)
    LastU=np.zeros(Model.Node.Count * 7)
    CurF=np.zeros(Model.Node.Count * 7)
    LastF=np.zeros(Model.Node.Count * 7)
    # ===========================================================================
    # Start analysis
    pl.Print("Start incremental-iterative procedure ...")
    CurStep = 0
    break_flag = 0
    while CurStep < Model.Analysis.LoadStep:
        # Initializing for the iteration
        CurStep += 1
        CurU = LastU
        CurF = LastF + DelF
        UnbF = DelF  # first step
        DelU = np.zeros(Model.Node.Count * 7)
        NIter = 0
        ResNormU = 1.0; ResNormF = 1.0
        while (ResNormU > Model.Analysis.TOL or ResNormF > Model.Analysis.TOL):
            NIter += 1
            # initialize KG
            Kg0 = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()
            Kg, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member,
                                          Model.Member.EleMtxL, Model.Member.EleMtxK, NonsymWarpingBeam, Kg0, Model.Analysis.Type)
            # Apply soil boundary conditions
            # ---------------------------------------------------------------------------
            Kgs = FormMtxg.FormKgs(Model.Material, Model.Section, Model.Node, Model.Member, SoilBoundaryElement, Model.SoilParameter, Model.Buried,
                                   Model.Member.EleMtxL0, coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense())
            Kg += Kgs
            KgSpr = Assembly.ApplySprBdyCond(Model.SpringBoundary, Model.SpringModel, Model.Node,
                                             coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7),dtype=np.float).todense())
            Kg += KgSpr
            # ---------------------------------------------------------------------------
            # Apply Coupling
            Kg, UnbF = Assembly.ApplyCoupl(Model.Coupling, Model.Node, Kg, UnbF)
            # ---------------------------------------------------------------------------
            # Apply boundary condition-
            Kg, UnbF = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, Kg, UnbF)
            Kg = ActiveDOF.ActiveWarpingDOF(True, Kg)
            # ---------------------------------------------------------------------------
            # Newton-Raphson method
            try:
                DelU = np.linalg.solve(Kg, UnbF)
            except:
                pl.Print("NO CONVERGENCE! Please Check!")
                break_flag = 1
                break
            else:
                pass
            CurU += DelU
            # Model.Member.GaussPointCurUUpdate(CurU)
            Model.Node.NodeUpdate(Model.Node, DelU)
            # Model.Member.GaussPointCurUL0 = Model.Member.GaussPointCurUL0Update(Model.Member, Model.Node, Model.Section,\
            #                                    Model.Material, NonsymWarpingBeam.NonsymWarpingBeam)
            # MemDelU = result.CyCRes.GetMemberDeflections(DelU)
            Rg = Result.CyCRes.GetRg(Model.Node, Model.Member, EleMtxK, DelU, Model.Analysis.Type)
            Rgs = Result.CyCRes.GetRgs(SoilBoundaryElement, Model.Material, Model.Section, Model.Node, Model.Member, Model.SoilParameter, Model.Buried)
            Rg += Rgs
            RgSpr = Result.CyCRes.GetRgSpr(Model.SpringBoundary, Model.SpringModel, Model.Node)
            Rg += RgSpr
            Rg = Result.CyCRes.GetNodeReaction(Model.Boundary, Model.Node, Rg)
            Rg = ActiveDOF.ActiveWarpingDOF(True, Rg)
            # ---------------------------------------------------------------------------
            UnbF = CurF - Rg
            # ---------------------------------------------------------------------------
            CurLF = LoadFactor.GetLF(Model.Node.Fg, CurF)
            ResNormU = LA.norm(DelU) / LA.norm(CurU)
            ResNormF = LA.norm(UnbF) / LA.norm(CurF)
            if NIter == 1:
                SolnMsg1 = str("TIME = -1 " + "; " + "LOAD FACTOR = " + "%.4f"%CurLF + "; " + "LOAD INCREMENT = " + "%.4f"%incLF)
                pl.Print(SolnMsg1)
            SolnMsg2 = str("STEP = " + "%03d"%CurStep + ";" + " ITER.= " + "%02d"%NIter + ";"\
                           + " NORM detU/U,resF/FCE= " + str(format(ResNormU, "0.4e")) + ", "\
                           + str(format(ResNormF, "0.4e")))
            pl.Print(SolnMsg2)
            # -----------------------------------------------------------------------
            if NIter > Model.Analysis.MaxIter:
                pl.Print("Exceed max. iteration times!")
                break_flag = 1
                break
            # -----------------------------------------------------------------------

        if break_flag: break
        pl.Print("Incremental step has been completed ..." + '\n')
        Result.CyCRes.GetCoupledDOF(Model.Coupling, Model.Node, CurU)
        # Save the last converged results
        Result.CyCRes.CurU = CurU
        Result.CyCRes.LF = CurLF
        LastF = CurF
        LastU = CurU
        # ---------------------------------------------------------------------------
        OutputResults.OutCyCRes(Result)
        # ---------------------------------------------------------------------------

    return
