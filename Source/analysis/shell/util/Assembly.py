#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math, copy
import logging
from scipy import linalg as LA
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix

# Join the CST and DKT linear stiffness matrix together (local coordinate)
def AssmbelEleMtx(CSTMtxKL, DKTMtxKL, TriCSTDKTMtxKL):
    a = [0, 1, 6, 7, 12, 13]
    b = [0, 1, 2, 3, 4, 5]
    for i in range(len(a)):
        for j in range(len(a)):
            TriCSTDKTMtxKL[a[i], a[j]] = CSTMtxKL[b[i], b[j]]

    c = [2, 3, 4, 8, 9, 10, 14, 15, 16]
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(len(c)):
        for j in range(len(c)):
            TriCSTDKTMtxKL[c[i], c[j]] = DKTMtxKL[d[i], d[j]]

    TriCSTDKTMtxKL[5, 5] = max(TriCSTDKTMtxKL[0, 0], TriCSTDKTMtxKL[1, 1], TriCSTDKTMtxKL[2, 2], TriCSTDKTMtxKL[3, 3],
                              TriCSTDKTMtxKL[4, 4]) / 1000
    TriCSTDKTMtxKL[11, 11] = max(TriCSTDKTMtxKL[6, 6], TriCSTDKTMtxKL[7, 7], TriCSTDKTMtxKL[8, 8], TriCSTDKTMtxKL[9, 9],
                                TriCSTDKTMtxKL[10, 10]) / 1000
    TriCSTDKTMtxKL[17, 17] = max(TriCSTDKTMtxKL[12, 12], TriCSTDKTMtxKL[13, 13], TriCSTDKTMtxKL[14, 14],
                                TriCSTDKTMtxKL[15, 15],
                                TriCSTDKTMtxKL[16, 16]) / 1000

    return TriCSTDKTMtxKL

# Assemble the local element linear stiffness matrix to global element linear stiffness matrix (global coordinate)
def EleMtxToGlo(EleK, Elek, i, j, k):
    I = np.array([6 * i - 6, 6 * i - 5, 6 * i - 4, 6 * i - 3, 6 * i - 2, 6 * i - 1])
    J = np.array([6 * j - 6, 6 * j - 5, 6 * j - 4, 6 * j - 3, 6 * j - 2, 6 * j - 1])
    K = np.array([6 * k - 6, 6 * k - 5, 6 * k - 4, 6 * k - 3, 6 * k - 2, 6 * k - 1])
    a = np.append(np.append(I, J), K)
    for p in range(18):

        EleK[a[p], I[0]] += Elek[p, 0]
        EleK[a[p], I[1]] += Elek[p, 1]
        EleK[a[p], I[2]] += Elek[p, 2]
        EleK[a[p], I[3]] += Elek[p, 3]
        EleK[a[p], I[4]] += Elek[p, 4]
        EleK[a[p], I[5]] += Elek[p, 5]

        EleK[a[p], J[0]] += Elek[p, 6]
        EleK[a[p], J[1]] += Elek[p, 7]
        EleK[a[p], J[2]] += Elek[p, 8]
        EleK[a[p], J[3]] += Elek[p, 9]
        EleK[a[p], J[4]] += Elek[p, 10]
        EleK[a[p], J[5]] += Elek[p, 11]

        EleK[a[p], K[0]] += Elek[p, 12]
        EleK[a[p], K[1]] += Elek[p, 13]
        EleK[a[p], K[2]] += Elek[p, 14]
        EleK[a[p], K[3]] += Elek[p, 15]
        EleK[a[p], K[4]] += Elek[p, 16]
        EleK[a[p], K[5]] += Elek[p, 17]

    return EleK

# Assemble the CST local element linear stiffness matrix to global element linear stiffness matrix (global coordinate)
def EleKGMtxToGlo(EleK, Elek, i, j, k):
    # EleK 6n x 6n, Elek 9 x 9
    I = np.array([6 * i - 6, 6 * i - 5, 6 * i - 4, 6 * i - 3, 6 * i - 2, 6 * i - 1])
    J = np.array([6 * j - 6, 6 * j - 5, 6 * j - 4, 6 * j - 3, 6 * j - 2, 6 * j - 1])
    K = np.array([6 * k - 6, 6 * k - 5, 6 * k - 4, 6 * k - 3, 6 * k - 2, 6 * k - 1])
    a = np.append(np.append(I, J), K)
    for p in range(18):

        EleK[a[p], I[0]] += Elek[p, 0]
        EleK[a[p], I[1]] += Elek[p, 1]
        EleK[a[p], I[2]] += Elek[p, 2]
        EleK[a[p], I[3]] += Elek[p, 3]
        EleK[a[p], I[4]] += Elek[p, 4]
        EleK[a[p], I[5]] += Elek[p, 5]

        EleK[a[p], J[0]] += Elek[p, 6]
        EleK[a[p], J[1]] += Elek[p, 7]
        EleK[a[p], J[2]] += Elek[p, 8]
        EleK[a[p], J[3]] += Elek[p, 9]
        EleK[a[p], J[4]] += Elek[p, 10]
        EleK[a[p], J[5]] += Elek[p, 11]

        EleK[a[p], K[0]] += Elek[p, 12]
        EleK[a[p], K[1]] += Elek[p, 13]
        EleK[a[p], K[2]] += Elek[p, 14]
        EleK[a[p], K[3]] += Elek[p, 15]
        EleK[a[p], K[4]] += Elek[p, 16]
        EleK[a[p], K[5]] += Elek[p, 17]

    return EleK

# Apply the boundary conditions to the global stiffness matrix (global coordinate)
def ApplyBdyCond(Boundary, Node, Kg):
    kb = copy.deepcopy(Kg)
    for ii in Boundary.NodeID:
        tNodeID = Node.ID[ii]
        if Boundary.UX[ii]:
            kb[:, tNodeID * 6] = kb[tNodeID * 6, :] = 0
            kb[tNodeID * 6, tNodeID * 6] = 1
        if Boundary.UY[ii]:
            kb[:, tNodeID * 6 + 1] = kb[tNodeID * 6 + 1, :] = 0
            kb[tNodeID * 6 + 1, tNodeID * 6 + 1] = 1
        if Boundary.UZ[ii]:
            kb[:, tNodeID * 6 + 2] = kb[tNodeID * 6 + 2, :] = 0
            kb[tNodeID * 6 + 2, tNodeID * 6 + 2] = 1
        if Boundary.RX[ii]:
            kb[:, tNodeID * 6 + 3] = kb[tNodeID * 6 + 3, :] = 0
            kb[tNodeID * 6 + 3, tNodeID * 6 + 3] = 1
        if Boundary.RY[ii]:
            kb[:, tNodeID * 6 + 4] = kb[tNodeID * 6 + 4, :] = 0
            kb[tNodeID * 6 + 4, tNodeID * 6 + 4] = 1
        if Boundary.RZ[ii]:
            kb[:, tNodeID * 6 + 5] = kb[tNodeID * 6 + 5, :] = 0
            kb[tNodeID * 6 + 5, tNodeID * 6 + 5] = 1
    return kb

# Apply the boundary conditions to the global stiffness matrix (global coordinate)
def ApplyBdyCond_eigen(Boundary, Node, K):
    kb = copy.deepcopy(K)
    deletelist = []
    for ii in Boundary.NodeID:
        tNodeID = Node.ID[ii] + 1
        if Boundary.UX[ii]:
            deletelist.append(tNodeID * 6 - 6)
        if Boundary.UY[ii]:
            deletelist.append(tNodeID * 6 - 5)
        if Boundary.UZ[ii]:
            deletelist.append(tNodeID * 6 - 4)
        if Boundary.RX[ii]:
            deletelist.append(tNodeID * 6 - 3)
        if Boundary.RY[ii]:
            deletelist.append(tNodeID * 6 - 2)
        if Boundary.RZ[ii]:
            deletelist.append(tNodeID * 6 - 1)
    # axis = 0 删除行
    kb = np.delete(kb, deletelist, axis=0)
    # axis = 1 删除列
    kb = np.delete(kb, deletelist, axis=1)
    return kb