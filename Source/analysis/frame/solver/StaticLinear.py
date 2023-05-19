#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

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
from scipy import linalg as LA
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix

# Import internal functions
from analysis.frame.variables import Model, Result
from analysis.frame.file import OutputResults
from analysis.frame.element import NonsymWarpingBeam, SoilBoundaryElement
from analysis.frame.util import Assembly
from analysis.frame.util import FormMtxg
from analysis.frame.util import LoadFactor
from analysis.frame.util import GetNorm
from analysis.frame.util.PrintLog import PrintLog as pl

def run():
    pl.Print("Start 1st-order elastic analysis ...")
    # Preparation
    DelF = Model.Analysis.TargetLF * Model.Node.Fg
    OutputResults.IniResults()
    CurF = UnbF = DelF
    DelU = np.zeros(Model.Node.Count * 7)
    # initialize KG
    Kg0 = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()
    Kg, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member,
                                  Model.Member.EleMtxL, Model.Member.EleMtxK, NonsymWarpingBeam, Kg0, Model.Analysis.Type)
    # ---------------------------------------------------------------------------
    Kgs = FormMtxg.FormKgs(Model.Material, Model.Section, Model.Node, Model.Member, SoilBoundaryElement, Model.SoilParameter, Model.Buried,
                                   Model.Member.EleMtxL0, coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense())
    Kg += Kgs
    # ---------------------------------------------------------------------------
    KgSpr = Assembly.ApplySprBdyCond(Model.SpringBoundary, Model.SpringModel, Model.Node, coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense())
    Kg += KgSpr
    # =========================================================
    # Apply Coupling
    Kg, UnbF = Assembly.ApplyCoupl(Model.Coupling, Model.Node, Kg, UnbF)
    # ---------------------------------------------------------------------------
    # Apply boundary condition-
    Kg, UnbF = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, Kg, UnbF)
    # ---------------------------------------------------------------------------
    # Newton-Raphson method
    TestKg = Kg.A
    DelU = np.linalg.solve(Kg, UnbF)
    # MemDelU = result.CyCRes.GetMemberDeflections(DelU)
    Rg = Result.CyCRes.GetRg(Model.Node, Model.Member, EleMtxK, DelU, Model.Analysis.Type)
    Rgs = Result.CyCRes.GetRgs(SoilBoundaryElement, Model.Material, Model.Section, Model.Node, Model.Member, Model.SoilParameter, Model.Buried)
    Rg += Rgs
    RgSpr = Result.CyCRes.GetRgSpr(Model.SpringBoundary, Model.SpringModel, Model.Node)
    Rg += RgSpr
    # ---------------------------------------------------------------------------
    # Record Results
    CurU = DelU
    Result.CyCRes.CurU = CurU
    Result.CyCRes.GetNodeReaction(Model.Boundary, Model.Node, Rg)
    Result.CyCRes.GetCoupledDOF(Model.Coupling, Model.Node, CurU)
    Result.CyCRes.CurU = CurU
    CurLF = LoadFactor.GetLF(Model.Node.Fg, CurF)
    Result.CyCRes.LF = CurLF
    ResNormU = LA.norm(DelU) / LA.norm(CurU)
    ResNormF = LA.norm(UnbF) / LA.norm(CurF)

    SolnMsg1 = str("TIME = -1 " + "; " + "LOAD FACTOR = " + "%.4f" % CurLF + "; ")
    SolnMsg2 = str("STEP = " + "%03d" % 1 + ";" + " ITER.= " + "%02d" % 1 + ";" \
             + " NORM detU/U,resF/FCE= " + str(format(ResNormU, "0.4e")) + ", " + str(format(ResNormF, "0.4e")) + '\n')
    pl.Print(SolnMsg1); pl.Print(SolnMsg2)

    # pl.Print('Current Load Factor CurF= %.4f' % (CurLF))
    # pl.Print(('Time = -1', 'KCYC= %03d' % (1), 'ITER.= %02d' % (1), \
    #                  'NORM detU/U, resF/FCE= %6.4e, %6.4e' % (ResNormU, ResNormF)))
    #----------------------------------------------------------------------
    OutputResults.OutCyCRes(Result)
    #----------------------------------------------------------------------

    return
