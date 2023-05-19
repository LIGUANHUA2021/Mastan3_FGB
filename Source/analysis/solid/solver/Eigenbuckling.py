#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math
import logging
from scipy import linalg as LA
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
from scipy.sparse.linalg import eigs
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix

# Import internal functions
from analysis.solid.variables import Model, Results
from analysis.solid.file import OutputResults
from analysis.solid.element import FourNodeTetrahedron
from analysis.solid.util import FormMtxg
from analysis.solid.util import Assembly
from analysis.solid.util import PrintLog as pl
from analysis.solid.util.CalculateEigenSubspaceInteration import CalEigenSubIter

def run():
    pl.Print("Start Eigen-buckling analysis ...")
    OutputResults.IniResults_Eigen()
    AppliedF = Model.Analysis.TargetLF * Model.Node.Fg
    # initialize
    KL0 = coo_matrix((Model.Node.Count * 3, Model.Node.Count * 3), dtype=np.float64).todense()
    tMtrType = "linear"
    U0 = np.zeros(Model.Node.Count * 3)
    KL = FormMtxg.FormKg(Model.Material, Model.Node, Model.Element, FourNodeTetrahedron, KL0, tMtrType, U0)
    # ---------------------------------------------------------------------------
    # Apply boundary condition
    KLb = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, KL)
    # ---------------------------------------------------------------------------
    # Newton-Raphson method
    U = np.linalg.solve(KLb, AppliedF)
    U_g = np.array(U)
    # ---------------------------------------------------------------------------
    KGeo = coo_matrix((Model.Node.Count * 3, Model.Node.Count * 3), dtype=np.float64).todense()
    tMtrType1 = "eigenBuckling"
    tKGe = FormMtxg.FormKg(Model.Material, Model.Node, Model.Element, FourNodeTetrahedron, KGeo, tMtrType1, U_g)
    KGe = tKGe - KL
    # ---------------------------------------------------------------------------
    # Apply boundary condition
    KLb = Assembly.ApplyBdyCond_eigen(Model.Boundary, Model.Node, KLb)
    KGeb = Assembly.ApplyBdyCond_eigen(Model.Boundary, Model.Node, KGe)
    #
    if Model.Analysis.ModesNum == 0:
        eigenvalues, eigenvectors = LA.eig(KLb, -1 * KGeb)
        eigenvalues = eigenvalues.reshape(Model.Node.Count * 3, 1)
        eigen_pairs = np.hstack([eigenvalues.real, eigenvectors.transpose().real])
        eigen_pairs = sorted(eigen_pairs, key=lambda eigen_pairs: eigen_pairs[0])
        eigen_pairs = np.array(eigen_pairs)
        pointer = 0
        modenum = 0
        for ii in eigen_pairs[:, 0]:
            if float(ii) <= 0:
                pointer += 1
            elif float(ii) != math.inf:
                modenum += 1
        eigen_pairs = eigen_pairs[pointer:pointer + modenum, :]
    else:
        eigenvalues, eigenvectors = eigsh(A = KLb, k = Model.Analysis.ModesNum, M = - 1 * KGeb, sigma = 1, which = 'LM', mode = 'buckling')
    # ---------------------------------------------------------------------------
    ## Record Results
    if Model.Analysis.ModesNum == 0:
        Results.CyCRes.EigenBuckling = {i + 1: eigen_pairs[:, 0][i] for i in range(len(eigen_pairs[:, 0]))}
    else:
        Results.CyCRes.EigenBuckling = {i + 1: eigenvalues[i] for i in range(len(eigenvalues))}
    # print("---------------------------------------------------")
    # ---------------------------------------------------------------------------
    # Output Results
    OutputResults.OutCyCRes_Eigen(Results)
    # ---------------------------------------------------------------------------
    pl.Print("[Mode NO.]\t[Load Factor]")
    logging.info("[Mode NO.]\t[Load Factor]")
    #
    if Model.Analysis.ModesNum == 0:
        for ii in range(modenum):
            SolnMsg1 = str("\t" + str(ii + 1) + "\t\t" + str(format(eigen_pairs[ii, 0], "0<18.4f")))
            pl.Print(SolnMsg1)
        SolnMsg = []
        for ii in range(modenum):
            SolnMsg.append(float(format(eigen_pairs[ii, 0], "0<18.4f")))
    ##
    else:
        for ii in range(len(eigenvalues)):
            SolnMsg1 = str("\t" + str(ii + 1) + "\t\t" + str(format(eigenvalues[ii], "0<18.4f")))
            pl.Print(SolnMsg1)
        SolnMsg = []
        for ii in range(len(eigenvalues)):
            SolnMsg.append(float(format(eigenvalues[ii], "0<18.4f")))