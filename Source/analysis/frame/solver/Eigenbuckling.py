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
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix
from scipy import linalg as LA #For solving eigen-equations

# Import internal functions
from analysis.frame.variables import Model
from analysis.frame.element import NonsymWarpingBeam
from analysis.frame.util import Assembly
from analysis.frame.util import FormMtxg
from analysis.frame.util.PrintLog import PrintLog as pl

def run():
    # pl.Print("Start Eigen-buckling analysis ...")
    # Preparation
    # initialize KG
    KgL = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float64).todense()

    tKgL, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member,
                                    Model.Member.EleMtxL, Model.Member.EleMtxK, NonsymWarpingBeam, KgL, Model.Analysis.Type)
    tKgLs = np.array(tKgL)
    # ----------------------------------------------------------------------
    KgL, Fg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, tKgL, Model.Node.Fg)
    DelU = np.linalg.solve(KgL, Fg)
    # ----------------------------------------------------------------------
    KgG = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float64).todense()
    # Update node coordinate
    Model.Node.NodeUpdate(Model.Node, DelU)
    # Update Member length
    # model.Member.MemLenUpdate(model.Member,model.Node)
    # Update member
    for ii in Model.Member.ID:
        tMID = Model.Member.ID[ii]
        mL = Model.Member.L[tMID]
        MemDelUG, MemDelUL = Model.Member.GetMemberDelU(Model.Member, Model.Node, DelU, ii)
        # Update member deformation
        Model.Member.MemDelUUpdate(Model.Member, MemDelUL, tMID)
        # Update member matrix L
        # model.Member.MemMtxLUpdate(model.Member, model.Node)
        # Get member deformations by removing the rigid body movements
        MemDelU = Model.Member.GetMemURemoveRBMove(MemDelUL, mL)  # mL reference last config
        # Recall Stiffness Matrix
        tEleKl = EleMtxK[tMID * 14:tMID * 14 + 14, 0:14]  # 14x14
        MemResF = np.dot(tEleKl, MemDelU)  # 14
        # Store member forces
        Model.Member.StoreMemForces(Model.Member, MemResF, tMID)

    tKgG, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member,
                                    Model.Member.EleMtxL, Model.Member.EleMtxK, NonsymWarpingBeam, KgG, Model.Analysis.Type)
    tTtKgG = tKgG - tKgLs
    # ----------------------------------------------------------------------
    # Apply boundary condition
    KgG, Fg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, tTtKgG, Fg)
    # ----------------------------------------------------------------------

    tarryKgLs = np.array(KgL)
    tarryKgGs = np.array(KgG)
    eigenvalues, eigenvectors = LA.eig(KgL, -1 * KgG)
    eigenvalues = eigenvalues.reshape(Model.Node.Count * 7, 1)
    eigen_pairs = np.hstack([eigenvalues.real, eigenvectors.transpose().real])
    eigen_pairs=sorted(eigen_pairs,key=lambda eigen_pairs: eigen_pairs[0])
    eigen_pairs=np.array(eigen_pairs)
    pointer = 0
    modenum = 0
    for ii in eigen_pairs[:, 0]:
        if float(ii) <= 0:
            pointer += 1
        elif float(ii) != math.inf:
            modenum += 1
    eigen_pairs = eigen_pairs[pointer:pointer + modenum, :]

    #print("---------------------------------------------------")
    # pl.Print("[Mode NO.]\t[Load Factor]")
    #logging.info("[Mode NO.]\t[Load Factor]")
    for ii in range(modenum):
        SolnMsg1 = str("\t" + str(ii + 1) + "\t\t" + str(format(eigen_pairs[ii, 0], "0<18.4f")))
    #     pl.Print(SolnMsg1)
    SolnMsg = []
    for ii in range(modenum):
        SolnMsg.append(float(format(eigen_pairs[ii, 0], "0<18.4f")))
    #----------------------------------------------------------------------
    # outputResults.OutCyCRes()
    #----------------------------------------------------------------------

    return SolnMsg
