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
from itertools import zip_longest  # For establishing dictionary
import numpy as np
import math
# ===========================================================================
# Import internal functions

# ===========================================================================
def initialize():
    # Member Geometry
    Element.Initialize(Element.Count)
    # Initialize member length & member matrix L
    # for ii in Element.ID:
    #     Element.MemLenUpdate(Element, Node, ii)
    #     Element.MemMtxLUpdate(Element, Node, ii)
    # # MemGeometry.update(model.Member,model.Node)
    # External force vector
    Node.NodeFgUpdate()

    return


class Information:
    Version = " "
    EDate = " "
    Description = " "

    def __init__(self):
        self.Version = " "
        self.EDate = " "
        self.Description = " "

    @staticmethod
    def ReadModelGenlInfo(ModelGenlInfo):
        Information.Version = ModelGenlInfo[0, 1]
        Information.EDate = ModelGenlInfo[1, 1]
        Information.Description = ModelGenlInfo[2, 1]
        return

class Node:
    Count = 0
    ID = []
    X = {}
    Y = {}
    Z = {}
    X0 = {}
    Y0 = {}
    Z0 = {}
    Fg = {}
    CurU = {}
    CurF = {}

    def __init__(self):
        self.Count = 0
        self.ID = []
        self.X = {}
        self.Y = {}
        self.Z = {}
        self.X0 = {}
        self.Y0 = {}
        self.Z0 = {}
        self.Fg = {}
        self.CurU = {}
        self.CurF = {}
    @staticmethod
    def ReadNode(NodeInfo):
        Node.Count = len(NodeInfo)
        Node.ID = dict(zip_longest(NodeInfo[:, 0], np.arange(Node.Count)))
        Node.X = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 1]))
        Node.Y = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 2]))
        Node.Z = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 3]))
        Node.X0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 1]))
        Node.Y0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 2]))
        Node.Z0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 3]))
        Node.Fg = np.zeros(Node.Count * 3)
        Node.CurU = np.zeros(Node.Count * 3)
        Node.CurF = np.zeros(Node.Count * 3)
        return

    # def NodeUpdate(self, tDelU):
    #     for ii in Node.ID:
    #         self.X[ii] += tDelU[self.ID[ii] * 7]
    #         self.Y[ii] += tDelU[self.ID[ii] * 7 + 1]
    #         self.Z[ii] += tDelU[self.ID[ii] * 7 + 2]
    #
    # def NodeFgUpdate(self):
    #
    #     for ii in PointLoad.NodeID:
    #         self.Fg[Node.ID[ii] * 7 + 0] = PointLoad.FX[ii]
    #         self.Fg[Node.ID[ii] * 7 + 1] = PointLoad.FY[ii]
    #         self.Fg[Node.ID[ii] * 7 + 2] = PointLoad.FZ[ii]
    #     # Apply boundary
    #     for ii in Boundary.NodeID:
    #         tNodeID = Node.ID[ii]
    #         if Boundary.UX[ii]: Node.Fg[tNodeID * 7] = 0
    #         if Boundary.UY[ii]: Node.Fg[tNodeID * 7 + 1] = 0
    #         if Boundary.UZ[ii]: Node.Fg[tNodeID * 7 + 2] = 0
    #
    #     return
    @staticmethod
    def NodeFgUpdate():
        for ii in PointLoad.NodeID:
            Node.Fg[Node.ID[ii] * 3 + 0] = PointLoad.FX[ii]
            Node.Fg[Node.ID[ii] * 3 + 1] = PointLoad.FY[ii]
            Node.Fg[Node.ID[ii] * 3 + 2] = PointLoad.FZ[ii]
        # Apply boundary
        for ii in Boundary.NodeID:
            tNodeID = Node.ID[ii]
            if Boundary.UX[ii]: Node.Fg[tNodeID * 3] = 0
            if Boundary.UY[ii]: Node.Fg[tNodeID * 3 + 1] = 0
            if Boundary.UZ[ii]: Node.Fg[tNodeID * 3 + 2] = 0
        return


# --------------------------------------------------------------------------
class Element:
    Count = 0
    ID = {}
    MatID = {}
    I = {}
    J = {}
    K = {}
    N = {}
    V0 = {}
    def __init__(self):
        self.ID = {}
        self.MatID = {}
        self.I = {}
        self.J = {}
        self.K = {}
        self.N = {}
        self.V0 = {}
    @staticmethod
    def Initialize(tMemCount):
        #
        # Element.V0 = np.zeros(tMemCount)
        Element.x1 = np.zeros(tMemCount)
        Element.y1 = np.zeros(tMemCount)
        Element.z1 = np.zeros(tMemCount)
        Element.Fx1 = np.zeros(tMemCount)
        Element.Fy1 = np.zeros(tMemCount)
        Element.Fz1 = np.zeros(tMemCount)
        ##
        Element.x2 = np.zeros(tMemCount)
        Element.y2 = np.zeros(tMemCount)
        Element.z2 = np.zeros(tMemCount)
        Element.Fx2 = np.zeros(tMemCount)
        Element.Fy2 = np.zeros(tMemCount)
        Element.Fz2 = np.zeros(tMemCount)
        ##
        Element.x3 = np.zeros(tMemCount)
        Element.y3 = np.zeros(tMemCount)
        Element.z3 = np.zeros(tMemCount)
        Element.Fx3 = np.zeros(tMemCount)
        Element.Fy3 = np.zeros(tMemCount)
        Element.Fz3 = np.zeros(tMemCount)
        ##
        Element.x4 = np.zeros(tMemCount)
        Element.y4 = np.zeros(tMemCount)
        Element.z4 = np.zeros(tMemCount)
        Element.Fx4 = np.zeros(tMemCount)
        Element.Fy4 = np.zeros(tMemCount)
        Element.Fz4 = np.zeros(tMemCount)
        ##
        Element.EleMtxL = np.zeros((Element.Count * 3, 3))
        Element.EleMtxL0 = np.zeros((Element.Count * 3, 3))
        Element.EleMtxK = np.zeros((Element.Count * 14, 14))
        # [x, y, z, Torsion(thx)]
        # Element.GaussPointLocation = GaussPoint.GetGaussPointLocation(Element.ID, Element.I, Element.J)
        # # The deflection on the Gauss point on the initial refercence coordinate
        # Element.GaussPointCurUL0 = np.zeros([Element.Count, 7, 4])
        # Initialize member length
        for ii in Element.ID:
            tI = Element.I[ii]
            tJ = Element.J[ii]
            tK = Element.K[ii]
            tN = Element.N[ii]
            X1 = Node.X0[tI]
            Y1 = Node.Y0[tI]
            Z1 = Node.Z0[tI]
            X2 = Node.X0[tJ]
            Y2 = Node.Y0[tJ]
            Z2 = Node.Z0[tJ]
            X3 = Node.X0[tK]
            Y3 = Node.Y0[tK]
            Z3 = Node.Z0[tK]
            X4 = Node.X0[tN]
            Y4 = Node.Y0[tN]
            Z4 = Node.Z0[tN]
            # Element.V0[ii] = np.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2 + (Z2 - Z1) ** 2)
    @staticmethod
    def ReadElement(ElementInfo):
        Element.Count = len(ElementInfo)
        Element.ID = dict(zip_longest(ElementInfo[:, 0], np.arange(Element.Count)))
        Element.MatID = dict(zip_longest(ElementInfo[:, 0], ElementInfo[:, 1]))
        Element.I = dict(zip_longest(ElementInfo[:, 0], ElementInfo[:, 2]))
        Element.J = dict(zip_longest(ElementInfo[:, 0], ElementInfo[:, 3]))
        Element.K = dict(zip_longest(ElementInfo[:, 0], ElementInfo[:, 4]))
        Element.N = dict(zip_longest(ElementInfo[:, 0], ElementInfo[:, 5]))
        # Element.Initialize(Element.Count)
        return

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
class Material:
    Count = 0
    ID = {}
    E = {}
    G = {}
    PR = {}
    Fy = {}
    Dens = {}

    def __init__(self):
        self.ID = {}
        self.E = {}
        self.G = {}
        self.PR = {}
        self.Fy = {}
        self.Dens = {}

    @staticmethod
    def ReadMat(MatInfo):
        Material.Count = len(MatInfo)
        Material.ID = dict(zip_longest(MatInfo[:, 0], np.arange(Material.Count)))
        Material.E = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 1]))
        Material.G = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 2]))
        Material.PR = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 3]))
        Material.Fy = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 4]))
        Material.Dens = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 5]))
        # ...... for Density & Coefficient of Themal Expansion and so on
        return

# --------------------------------------------------------------------------
class Boundary:
    Count = 0
    NodeID = {}
    UX = {}
    UY = {}
    UZ = {}

    def __init__(self):
        self.NodeID = {}
        self.UX = {}
        self.UY = {}
        self.UZ = {}

    @staticmethod
    def ReadBoun(BounInfo):
        Boundary.Count = len(BounInfo)
        Boundary.NodeID = dict(zip_longest(BounInfo[:, 0], np.arange(Boundary.Count)))
        Boundary.UX = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 1]))
        Boundary.UY = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 2]))
        Boundary.UZ = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 3]))
        return

# --------------------------------------------------------------------------
class PointLoad:
    Count = 0
    NodeID = {}
    FX = {}
    FY = {}
    FZ = {}
    # Yp = {}
    # Zp = {}
    def __init__(self):
        self.NodeID = {}
        self.FX = {}
        self.FY = {}
        self.FZ = {}

    @staticmethod
    def ReadPNTL(PNTLInfo):
        PointLoad.Count = len(PNTLInfo)
        PointLoad.NodeID = dict(zip_longest(PNTLInfo[:, 0], np.arange(PointLoad.Count)))
        PointLoad.FX = dict(zip_longest(PNTLInfo[:, 0], PNTLInfo[:, 1]))
        PointLoad.FY = dict(zip_longest(PNTLInfo[:, 0], PNTLInfo[:, 2]))
        PointLoad.FZ = dict(zip_longest(PNTLInfo[:, 0], PNTLInfo[:, 3]))
        # PointLoad.Yp = dict(zip_longest(PNTLInfo[:, 0], PNTLInfo[:, 7]))
        # PointLoad.Zp = dict(zip_longest(PNTLInfo[:, 0], PNTLInfo[:, 8]))
        return


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
class Analysis:
    Type = ""
    AnalInfo = {}
    ## Static Analysis
    TargetLF = 0.0
    LoadStep = 0.0
    MaxIter = 0.0
    TOL = 0.0
    SolnTech = ""
    ModesNum = 0.0
    CtlNode = 0.0
    CtlDir = 0.0
    CtlDis = 0.0

    ## Dynamic Analysis
    MassType = ""
    NewmarkGamma = 0.0
    NewmarkBeta = 0.0
    TotalTimeSteps = 0.0
    Timeincr = 0.0
    DampingRatio = 0.0
    FirstFreq = 0.0
    SecondFreq = 0.0
    AddMassDir = ""
    GraAcc = 0.0

    # Read Analysis Information
    @staticmethod
    def ReadAnal(tAanalInfo):
        print("tAanalInfo = ", tAanalInfo)
        AnalInfo =dict(zip_longest(tAanalInfo[:, 0], tAanalInfo[:, 1]))
        Analysis.Type = AnalInfo.get('Type', "staticLinear")
        ## Static
        Analysis.TargetLF = float(AnalInfo.get('Target Load Factor', 1.0))
        Analysis.LoadStep = int(AnalInfo.get('Load Step', 10))
        Analysis.MaxIter = int(AnalInfo.get('Max. Iteration', 99))
        Analysis.TOL = float(AnalInfo.get('Convergence', 0.001))
        Analysis.ModesNum = int(AnalInfo.get('Modes Number', 1))
        Analysis.SolnTech = AnalInfo.get('Solution Technique', "NL")
        Analysis.CtlNode = int(AnalInfo.get('Control Node', 2))
        Analysis.CtlDir = AnalInfo.get('Control Direction', "X")
        Analysis.CtlDis = float(AnalInfo.get('Control Displacement', 0.001))
        #
        if Analysis.CtlDir == 'X':
            Analysis.CtlDir = 0
        elif Analysis.CtlDir == 'Y':
            Analysis.CtlDir = 1
        elif Analysis.CtlDir == 'Z':
            Analysis.CtlDir = 2
        else:
            print("The input control direction of DisCtrl is error")
        #
        ## Dynamic
        Analysis.MassType = AnalInfo.get('Mass Type', "Consistent")
        Analysis.AddMassDir = AnalInfo.get('Additional Mass Direction', "Y-")
        Analysis.NewmarkGamma = float(AnalInfo.get('Newmark Gamma', 0.5))
        Analysis.NewmarkBeta = float(AnalInfo.get('Newmark Beta', 0.25))
        Analysis.TotalTimeSteps = float(AnalInfo.get('Total Time Steps', 12.0))
        Analysis.Timeincr = float(AnalInfo.get('Time increment (Sec.)', 0.01))
        Analysis.DampingRatio = float(AnalInfo.get('Damping Ratio', 0.02))
        Analysis.FirstFreq = float(AnalInfo.get('First Frequency', 1.2))
        Analysis.SecondFreq = float(AnalInfo.get('Second Frequency', 2.4))
        Analysis.GraAcc = float(AnalInfo.get('Second Frequency', 9.8))
        return

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
class OutResult:
    FileName = ""
    Folder = ""
    ModelName = ""
