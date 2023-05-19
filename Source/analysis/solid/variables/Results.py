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

class CyCRes:
    LF = 0
    CurU = {}      ##  Displacement;
    Rect = {}      ##  Reaction Forces;
    EleStrs = {}   ##  Element Stress;
    ElePStrs = {}  ##  Element Principal Stress;
    Time = 0
    VEL = {}   ##  Velocity;
    ACC = {}   ##  Acceleration;
    EigenBuckling = {}  ## Eigen buckling analysis-{key: Modes No., value: Load Factor}
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
        CyCRes.Rect = np.zeros((Boundary.Count, 3))
        for ii in Boundary.NodeID:
            tNodeID = Node.ID[ii]
            tBoundID = Boundary.NodeID[ii]
            if not Boundary.UX[ii]:
                CyCRes.Rect[tBoundID, 0] = Rg[tNodeID * 3]
                # Rg[tNodeID * 3] = 0
            if not Boundary.UY[ii]:
                CyCRes.Rect[tBoundID, 1] = Rg[tNodeID * 3 + 1]
                # Rg[tNodeID * 3 + 1] = 0
            if not Boundary.UZ[ii]:
                CyCRes.Rect[tBoundID, 2] = Rg[tNodeID * 3 + 2]
                # Rg[tNodeID * 3 + 2] = 0
    ##
    @staticmethod
    def GetElementStress(Material, Node, Element, FourNodeTetrahedron, U):
        for ii in Element.ID:
            tMID = Element.MatID[ii]
            tE = Material.E[tMID]
            tPR = Material.PR[tMID]
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
            tN_index = Element.N[ii]
            tN_in = Node.ID[tN_index]
            tX4 = Node.X[tN_index]
            tY4 = Node.Y[tN_index]
            tZ4 = Node.Z[tN_index]
            teU = [U[tI_in * 3], U[tI_in * 3+1], U[tI_in * 3+2], U[tJ_in * 3], U[tJ_in * 3+1], U[tJ_in * 3+2], U[tK_in * 3], U[tK_in * 3+1], U[tK_in * 3+2],
                   U[tN_in * 3], U[tN_in * 3+1], U[tN_in * 3+2]]
            ##
            sigma_ii = FourNodeTetrahedron.GetEleStrs(tE, tPR, tX1, tY1, tZ1, tX2, tY2, tZ2, tX3, tY3, tZ3, tX4, tY4, tZ4, teU)
            CyCRes.EleStrs.setdefault(ii, sigma_ii)
        return

    @staticmethod
    def GetElementPStress(Element, FourNodeTetrahedron):
        # tOMz_y_list = list(MomCurvaResults.OMz_y.values())
        for ii in Element.ID:
            tEleStrs = CyCRes.EleStrs[ii]
            tEleStrs_list = list(tEleStrs)
            Psigma_ii = FourNodeTetrahedron.GetElePStrs(tEleStrs_list)
            CyCRes.ElePStrs.setdefault(ii, Psigma_ii)
        return

