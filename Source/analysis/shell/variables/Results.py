#############################################################################
# MSAShell - Finite element analysis with solid element model (v0.0.1)

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
from analysis.shell.util import Postprocessing
from analysis.shell.util import Transformation

class CyCRes:
    LF = 0
    CurU = {}      ##  Displacement;
    Rect = {}      ##  Reaction Forces;
    EleStrs = {}   ##  Element Stress;
    ElePStrs = {}  ##  Element Principal Stress;
    Time = 0
    VEL = {}   ##  Velocity;
    ACC = {}   ##  Acceleration;
    EigenBuckling = {}
    def __init__(self):
        self.CurU = {}  ##  Displacement;
        self.Rect = {}  ##  Reaction Forces;

    @staticmethod
    def GetResF_g(Node, U, K):
        # Rg = np.zeros(Node.Count * 3)
        Rg = np.dot(K, U)
        tRg = np.asarray(Rg)
        tRg = tRg.tolist()[0]
        # print("Type of Rg = ", type(Rg))
        # print("Type of tRg = ", type(tRg))
        return tRg

    @staticmethod
    def GetNodeReactForce(Boundary, Node, Rg):
        CyCRes.Rect = np.zeros((Boundary.Count, 6))
        for ii in Boundary.NodeID:
            tNodeID = Node.ID[ii]
            tBoundID = Boundary.NodeID[ii]
            CyCRes.Rect[tBoundID, 0] = Rg[tNodeID * 6]
            # Rg[tNodeID * 3] = 0
            CyCRes.Rect[tBoundID, 1] = Rg[tNodeID * 6 + 1]
            # Rg[tNodeID * 3 + 1] = 0
            CyCRes.Rect[tBoundID, 2] = Rg[tNodeID * 6 + 2]
            # Rg[tNodeID * 3 + 2] = 0
            CyCRes.Rect[tBoundID, 3] = Rg[tNodeID * 6 + 3]
            # Rg[tNodeID * 3] = 0
            CyCRes.Rect[tBoundID, 4] = Rg[tNodeID * 6 + 4]
            # Rg[tNodeID * 3 + 1] = 0
            CyCRes.Rect[tBoundID, 5] = Rg[tNodeID * 6 + 5]

##
    @staticmethod
    def GetElementStress(Material, Section, Node, Element, U):
        for ii in Element.ID:
            tSectID = Element.SectID[ii]
            tMatID = Section.MatID[tSectID]
            tE = Material.E[tMatID]
            tu = Material.Nu[tMatID]
            t = Section.t[tMatID]
            tI_index = Element.I[ii]
            tI_in = Node.ID[tI_index]
            tX1 = Node.X[tI_index]
            tY1 = Node.Y[tI_index]
            tZ1 = Node.Z[tI_index]
            tJ_index = Element.J[ii]
            tJ_in = Node.ID[tJ_index]
            tX2 = Node.X[tJ_index]
            tY2 = Node.Y[tJ_index]
            tZ2 = Node.Z[tJ_index]
            tK_index = Element.K[ii]
            tK_in = Node.ID[tK_index]
            tX3 = Node.X[tK_index]
            tY3 = Node.Y[tK_index]
            tZ3 = Node.Z[tK_index]

            teU = np.array([U[tI_in * 6], U[tI_in * 6 + 1], U[tI_in * 6 + 2], U[tI_in * 6 + 3], U[tI_in * 6 + 4], U[tI_in * 6 + 5],
                   U[tJ_in * 6], U[tJ_in * 6 + 1], U[tJ_in * 6 + 2], U[tJ_in * 6 + 3], U[tJ_in * 6 + 4], U[tJ_in * 6 + 5],
                   U[tK_in * 6], U[tK_in * 6 + 1], U[tK_in * 6 + 2], U[tK_in * 6 + 3], U[tK_in * 6 + 4], U[tK_in * 6 + 5]
                   ])

            sigma_ii = Postprocessing.GetEleStrs(tE, tu, t, tX1, tY1, tZ1, tX2, tY2, tZ2, tX3, tY3, tZ3, teU)
            CyCRes.EleStrs.setdefault(ii, sigma_ii)

            # Calculation of the global stress
            s = np.array([[sigma_ii[0], sigma_ii[5], sigma_ii[3]],
                          [sigma_ii[5], sigma_ii[1], sigma_ii[4]],
                          [sigma_ii[3], sigma_ii[4], sigma_ii[2]]])

            T = np.zeros((3, 3))
            T[0:3, 0:3] = Transformation.GetMtxL(tX1, tY1, tZ1, tX2, tY2, tZ2, tX3, tY3, tZ3)[0:3, 0:3]
            # S = np.dot(np.dot(T, s), T.transpose())
            print("T = ", T)
            S = [0, 0, 0, 0, 0, 0]
            S[0] = ((T[0, 0] ** 2) * sigma_ii[0] + (T[0, 1] ** 2) * sigma_ii[1] + (T[0, 2] ** 2) * sigma_ii[2]
                       + 2 * T[0, 0] * T[0, 1] * sigma_ii[5] + 2 * T[0, 1] * T[0, 2] * sigma_ii[3] + 2 * T[0, 2] * T[0, 0] * sigma_ii[4])

            S[1] = ((T[1, 0] ** 2) * sigma_ii[0] + (T[1, 1] ** 2) * sigma_ii[1] + (T[1, 2] ** 2) * sigma_ii[2]
                    + 2 * T[1, 0] * T[1, 1] * sigma_ii[5] + 2 * T[1, 1] * T[1, 2] * sigma_ii[4] + 2 * T[1, 2] * T[
                        1, 0] * sigma_ii[3])

            S[2] = ((T[2, 0] ** 2) * sigma_ii[0] + (T[2, 1] ** 2) * sigma_ii[1] + (T[2, 2] ** 2) * sigma_ii[2]
                    + 2 * T[2, 0] * T[2, 1] * sigma_ii[5] + 2 * T[2, 1] * T[2, 2] * sigma_ii[4] + 2 * T[2, 2] * T[
                        2, 0] * sigma_ii[3])

            Psigma_ii = [0, 0, 0, 0, 0, 0]
            Psigma_ii[0], Psigma_ii[1], Psigma_ii[2] = S[0], S[1], S[2]
            Psigma_ii[3], Psigma_ii[4], Psigma_ii[5] = S[3], S[4], S[5]

            CyCRes.ElePStrs.setdefault(ii, Psigma_ii)
        return

    # @staticmethod
    # def GetElementPStress(Element, ):
    #     for ii in Element.ID:
    #         tEleStrs = CyCRes.EleStrs[ii]
    #         tEleStrs_list = list(tEleStrs)
    #         Psigma_ii =Postprocessing.GetElePStrs(tEleStrs_list)
    #         CyCRes.ElePStrs.setdefault(ii, Psigma_ii)
    #     return

