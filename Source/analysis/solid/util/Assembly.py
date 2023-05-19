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

def ApplyBdyCond(Boundary, Node, Kg):
    # tKg = np.zeros((Node.Count * 3, Node.Count * 3))
    tKg = copy.deepcopy(Kg)
    for ii in Boundary.NodeID:
        tNodeID = Node.ID[ii]
        if not Boundary.UX[ii]:
            tKg[:, tNodeID * 3] = tKg[tNodeID * 3, :] = 0
            tKg[tNodeID * 3, tNodeID * 3] = 1
        if not Boundary.UY[ii]:
            tKg[:, tNodeID * 3 + 1] = tKg[tNodeID * 3 + 1, :] = 0
            tKg[tNodeID * 3 + 1, tNodeID * 3 + 1] = 1
        if not Boundary.UZ[ii]:
            tKg[:, tNodeID * 3 + 2] = tKg[tNodeID * 3 + 2, :] = 0
            tKg[tNodeID * 3 + 2, tNodeID * 3 + 2] = 1
    return tKg

def ApplyBdyCond_eigen(Boundary, Node, Kg):
    deletelist = []
    for ii in Boundary.NodeID:
        tNodeID = Node.ID[ii] + 1
        if Boundary.UX[ii]:
            deletelist.append(tNodeID * 3)
        if Boundary.UY[ii]:
            deletelist.append(tNodeID * 3 + 1)
        if Boundary.UZ[ii]:
            deletelist.append(tNodeID * 3 + 2)
    # axis = 0
    Kg = np.delete(Kg, deletelist, axis=0)
    # axis = 1
    Kg = np.delete(Kg, deletelist, axis=1)
    return Kg