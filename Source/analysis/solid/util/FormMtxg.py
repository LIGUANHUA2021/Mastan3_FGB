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
import copy
import math
import logging
from scipy import linalg as LA
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix

def FormKg(Material, Node, Element, FourNodeTetrahedron, tMtr_K, tMtrType, U):
    ##
    for ii in Element.ID:
        tMID = Element.MatID[ii]
        tE = Material.E[tMID]
        tPR = Material.PR[tMID]
        tI_index = Element.I[ii]
        tX1 = Node.X[tI_index]
        tY1 = Node.Y[tI_index]
        tZ1 = Node.Z[tI_index]
        tJ_index = Element.J[ii]
        tX2 = Node.X[tJ_index]
        tY2 = Node.Y[tJ_index]
        tZ2 = Node.Z[tJ_index]
        tK_index = Element.K[ii]
        tX3 = Node.X[tK_index]
        tY3 = Node.Y[tK_index]
        tZ3 = Node.Z[tK_index]
        tN_index = Element.N[ii]
        tX4 = Node.X[tN_index]
        tY4 = Node.Y[tN_index]
        tZ4 = Node.Z[tN_index]
        # Form Element Stiffness Matrix_local
        if tMtrType == "eigenBuckling":
            kl_ii = FourNodeTetrahedron.GetElekgeo(tE, tPR, tX1, tY1, tZ1,
                                                   tX2, tY2, tZ2, tX3, tY3, tZ3, tX4, tY4, tZ4, U)
        elif tMtrType == "linear":
            kl_ii = FourNodeTetrahedron.GetElekl(tE, tPR, tX1, tY1, tZ1,
                                                 tX2, tY2, tZ2, tX3, tY3, tZ3, tX4, tY4, tZ4)

        # Form Element Stiffness Matrix_global
        KL_ii = FourNodeTetrahedron.GetEleKLG(tMtr_K, kl_ii, tI_index, tJ_index, tK_index, tN_index)
    ##
    tMtr_K = copy.deepcopy(KL_ii)
    return tMtr_K