#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix
from scipy import linalg as LA #For solving eigen-equations
import logging
# Import internal functions
from analysis.frame.variables import Model
from analysis.frame.element import NonsymWarpingBeam
from analysis.frame.util import Assembly
from analysis.frame.util import FormMtxg
from analysis.frame.util.PrintLog import PrintLog as pl

def run():
    pl.Print("Start Modal analysis ...")
    # for testing
    MassType = "Consistent"
    # Preparation
    tFg = np.zeros(Model.Node.Count * 7)
    # initialize Kg, calculate the Global Stiffness and Mass Matrix
    Kg = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()
    Mg = coo_matrix((Model.Node.Count * 7, Model.Node.Count * 7), dtype=np.float).todense()

    Kg, EleMtxK = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Member,
                                  Model.Member.EleMtxL, Model.Member.EleMtxK, NonsymWarpingBeam, Kg, Model.Analysis.Type)
    Mg = FormMtxg.FormMg(Model.Material, Model.Section, Model.Node, Model.Member,
                         Model.Member.EleMtxL, MassType, NonsymWarpingBeam, Mg)
    # ==================================================================================================================
    # Apply the Boundary Condition
    Kg, tFg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, Kg, tFg)
    Mg, tFg = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, Mg, tFg)
    # ==================================================================================================================
    # Calculation the Eigenvalue and Eigenvector
    if Model.Analysis.ModesNum > 6 * Model.Node.Count - Model.Boundary.Count:
        Model.Analysis.ModesNum = 6 * Model.Node.Count - Model.Boundary.Count
    # ------------------------------------------------------------------------------------------------------------------
    eigenvalues, eigenvectors = LA.eig(Kg, Mg)
    eigenvalues = eigenvalues.reshape(Model.Node.Count * 7, 1)
    eigen_pairs = np.hstack([eigenvalues.real, eigenvectors.transpose().real])
    eigen_pairs = sorted(eigen_pairs, key=lambda eigen_pairs: eigen_pairs[0])
    eigen_pairs = np.array(eigen_pairs)
    pointer = 0
    modenum = 0
    for ii in eigen_pairs[:, 0]:
        if float(ii) <= 1.0:
            pointer += 1
        elif float(ii) != math.inf:
            modenum += 1
    modenum = min(modenum, Model.Analysis.ModesNum)
    eigen_pairs = eigen_pairs[pointer:pointer + modenum, :]
    eigen_pairs[:, 0] = np.sqrt(eigen_pairs[:, 0])
    Frequencies = eigen_pairs[:, 0] / 2 / math.pi
    Periods = 1 / Frequencies

    #print("---------------------------------------------------")
    pl.Print("[Mode NO.]\t[Frequency(rad/sec)]\t[Frequency(cyc/sec)]\t[Period(s)]")
    for ii in range(modenum):
        SolnMsg1 = str("\t" + str(ii + 1) + '\t\t\t' + str(format(eigen_pairs[ii, 0], "0<12.4f")) + '\t\t\t'\
                       + str(format(Frequencies[ii], "0<12.4f")) + '\t\t' + str(format(Periods[ii], "0<12.4f")))
        pl.Print(SolnMsg1)
    # print("---------------------------------------------------")
    return