#############################################################################
# MSAShell - Finite element analysis with shell element model (v0.0.1)

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2023 Siwei Liu, All Right Reserved.
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
from analysis.shell.util import Assembly
from analysis.shell.element import NLThinTriShell
from analysis.shell.util import Transformation

# To obtain the global linear stiffness matrix in global coordinates
def FormKg(Material, Section, Node, Element, NLThinTriShell, KL0, tMtrType, U):
    ##
    for ii in Element.ID:
        tSectID = Element.SectID[ii]
        tMatID = Section.MatID[tSectID]
        tE = Material.E[tMatID]
        tu = Material.Nu[tMatID]
        tt = Section.t[tSectID]
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

        # Calculate the local coordinate
        Vx = np.array([tX2 - tX1, tY2 - tY1, tZ2 - tZ1])
        Vr = np.array([tX3 - tX1, tY3 - tY1, tZ3 - tZ1])
        Vz = np.cross(Vx, Vr)
        Vy = np.cross(Vz, Vx)
        x1, y1, z1 = 0, 0, 0
        x2, y2, z2 = ((tX2 - tX1) ** 2 + (tY2 - tY1) ** 2 + (tZ2 - tZ1) ** 2) ** 0.5, 0, 0
        x3, y3, z3 = (np.dot(Vx, Vr) / (np.linalg.norm(Vx))), (np.dot(Vy, Vr) / (np.linalg.norm(Vy))), 0
        #Calculate the transformation matrix
        T = Transformation.GetMtxL(tX1, tY1, tZ1, tX2, tY2, tZ2, tX3, tY3, tZ3)

        if tMtrType == "eigenBuckling":

            # Calculate the B matrix (local coordinate)
            A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3) * 0.5
            Em = (tE / (1 - tu ** 2)) * np.array([[1, tu, 0], [tu, 1, 0], [0, 0, (1 - tu) / 2]])
            CSTb = (1 / (2 * A)) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                       [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])

            # To obtain the CST displacement (local coordinate)
            EleU = np.zeros((1, 18))
            EleU[0, 0], EleU[0, 1], EleU[0, 2], EleU[0, 3], EleU[0, 4], EleU[0, 5] = U[(tI_index - 1) * 6], U[(tI_index - 1) * 6 + 1], \
                                                                   U[(tI_index - 1) * 6 + 2], U[(tI_index - 1) * 6 + 3], \
                                                                   U[(tI_index - 1) * 6 + 4], U[(tI_index - 1) * 6 + 5]
            EleU[0, 6], EleU[0, 7], EleU[0, 8], EleU[0, 9], EleU[0, 10], EleU[0, 11] = U[(tJ_index - 1) * 6], U[(tJ_index - 1) * 6 + 1], \
                                                                   U[(tJ_index - 1) * 6 + 2], U[(tJ_index - 1) * 6 + 3], \
                                                                   U[(tJ_index - 1) * 6 + 4], U[(tJ_index - 1) * 6 + 5]
            EleU[0, 12], EleU[0, 13], EleU[0, 14], EleU[0, 15], EleU[0, 16], EleU[0, 17] = U[(tK_index - 1) * 6], U[(tK_index - 1) * 6 + 1], \
                                                                     U[(tK_index - 1) * 6 + 2], U[(tK_index - 1) * 6 + 3], \
                                                                     U[(tK_index - 1) * 6 + 4], U[(tK_index - 1) * 6 + 5]
            Eleu = np.dot(Transformation.GetMtxL(tX1, tY1, tZ1, tX2, tY2, tZ2, tX3, tY3, tZ3), EleU.transpose()).transpose()
            CSTu = np.zeros((1, 6))
            CSTu[0, 0], CSTu[0, 1], CSTu[0, 2], CSTu[0, 3], CSTu[0, 4], CSTu[0, 5] = Eleu[0, 0], Eleu[0, 1], Eleu[0, 6], Eleu[0, 7], Eleu[0, 12], Eleu[0, 13]

            # Calculate the stress (local coordinate)
            CSTs = np.dot(Em, np.dot(CSTb, CSTu.transpose()))

            # Calculate the DKT geometric stiffness 18 x 18 (global coordinate)
            TriDKTMtxKG = NLThinTriShell.GetEleKG(x1, y1, x2, y2, x3, y3, CSTs, tt, T)


            # Form Total Element linear Stiffness Matrix (global coordinate), KLO (6n x 6n)
            KL_ii = Assembly.EleKGMtxToGlo(KL0, TriDKTMtxKG, tI_index, tJ_index, tK_index)

        elif tMtrType == "linear":

            # Calculate the CST  + DKT linear stiffness 18 x 18 (global coordinate)
            kl_ii = NLThinTriShell.GetEleKL(x1, y1, x2, y2, x3, y3, tE, tu, tt, T)

            # Form Total Element linear Stiffness Matrix (global coordinate), KLO (6n x 6n)
            KL_ii = Assembly.EleMtxToGlo(KL0, kl_ii, tI_index, tJ_index, tK_index)

    KL0 = copy.deepcopy(KL_ii)
    return KL0

