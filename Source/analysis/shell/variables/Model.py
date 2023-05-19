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
from itertools import zip_longest  # For establishing dictionary
import numpy as np
import math
# ===========================================================================
# Import internal functions
from analysis.shell.util import Transformation, GaussPoint


# ===========================================================================
def initialize():
    # Element Geometry
    Element.Initialize(Element.Count)
    # Initialize Element length & Element matrix L
    # for ii in Element.ID:
    #     Element.MemLenUpdate(Element, Node, ii)
    #     Element.MemMtxLUpdate(Element, Node, ii)
    # MemGeometry.update(model.Element,model.Node)
    # External force vector
    Node.NodeFgUpdate(Node)
    return


class Information:
    Version = " "
    EDate = " "
    Description = " "

    # def __init__(self):
    #     self.Version = " "
    #     self.EDate = " "
    #     self.Description = " "

    def ReadModelGenlInfo(ModelGenlInfo):
        Information.Version = ModelGenlInfo[0, 1]
        Information.EDate = ModelGenlInfo[1, 1]
        Information.Description = ModelGenlInfo[2, 1]
        return

# --------------------------------------------------------------------------

class Material:
    Count = 0
    ID = []
    E = {}
    G = {}
    Nu = {}
    Fy = {}
    Dens = {}

    def ReadMat(MatInfo):
        Material.Count = len(MatInfo)
        Material.ID = dict(zip_longest(MatInfo[:, 0], np.arange(Material.Count)))
        Material.E = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 1]))
        Material.G = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 2]))
        Material.Nu = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 3]))
        Material.Fy = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 4]))
        Material.Dens = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 5]))
        # ...... for Density & Coefficient of Themal Expansion and so on
        return

# --------------------------------------------------------------------------
class Section:
    Count = 0
    ID = []
    MatID = []
    ElementType = []
    t = {}

    ## To be added
    ## -----------

    # Read Section Dimensions Information
    def ReadSect(SectInfo):
        Section.Count = len(SectInfo)
        Section.ID = dict(zip_longest(SectInfo[:, 0], np.arange(Section.Count)))
        Section.MatID = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 1]))
        Section.ElementType = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 2]))
        Section.t = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 3]))

        return

class Node:
    Count = 0
    ID = []
    X = {}
    Y = {}
    Z = {}
    thX = {}
    thY = {}
    thZ = {}
    X0 = {}
    Y0 = {}
    Z0 = {}
    thX0 = {}
    thY0 = {}
    thZ0 = {}
    Fg = {}

    def __init__(self):
        self.Count = 0
        self.ID = []
        self.X = {}
        self.Y = {}
        self.Z = {}
        self.thX = {}
        self.thY = {}
        self.thZ = {}
        self.X0 = {}
        self.Y0 = {}
        self.Z0 = {}
        self.thX0 = {}
        self.thY0 = {}
        self.thZ0 = {}
        self.Fg = {}
        self.CurU = {}
        self.CurF = {}

    def ReadNode(self, NodeInfo) -> object:
        self.Count = len(NodeInfo)
        self.ID = dict(zip_longest(NodeInfo[:, 0], np.arange(Node.Count)))
        self.X = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 1]))
        self.Y = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 2]))
        self.Z = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 3]))
        self.thX = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thY = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thZ = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.X0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 1]))
        self.Y0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 2]))
        self.Z0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 3]))
        self.thX0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thY0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thZ0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))

        self.Fg = np.zeros(Node.Count * 6)
        self.CurU = np.zeros(Node.Count * 6)
        self.CurF = np.zeros(Node.Count * 6)
        return

    def NodeUpdate(self, tDelU):
        for ii in Node.ID:
            self.X[ii] += tDelU[self.ID[ii] * 6]
            self.Y[ii] += tDelU[self.ID[ii] * 6 + 1]
            self.Z[ii] += tDelU[self.ID[ii] * 6 + 2]
            self.thX[ii] += tDelU[self.ID[ii] * 6 + 3]
            self.thY[ii] += tDelU[self.ID[ii] * 6 + 4]
            self.thZ[ii] += tDelU[self.ID[ii] * 6 + 5]


    def NodeFgUpdate(self):

        for ii in JointLoad.NodeID:
            self.Fg[Node.ID[ii] * 6 + 0] = JointLoad.FX[ii]
            self.Fg[Node.ID[ii] * 6 + 1] = JointLoad.FY[ii]
            self.Fg[Node.ID[ii] * 6 + 2] = JointLoad.FZ[ii]
            self.Fg[Node.ID[ii] * 6 + 3] = JointLoad.MX[ii]
            self.Fg[Node.ID[ii] * 6 + 4] = JointLoad.MY[ii]
            self.Fg[Node.ID[ii] * 6 + 5] = JointLoad.MZ[ii]
        # Apply boundary
        for ii in Boundary.NodeID:
            tNodeID = Node.ID[ii]
            if Boundary.UX[ii]: Node.Fg[tNodeID * 6] = 0
            if Boundary.UY[ii]: Node.Fg[tNodeID * 6 + 1] = 0
            if Boundary.UZ[ii]: Node.Fg[tNodeID * 6 + 2] = 0
            if Boundary.RX[ii]: Node.Fg[tNodeID * 6 + 3] = 0
            if Boundary.RY[ii]: Node.Fg[tNodeID * 6 + 4] = 0
            if Boundary.RZ[ii]: Node.Fg[tNodeID * 6 + 5] = 0

        return
# --------------------------------------------------------------------------
class Element:
    Count = 0
    ID = []
    SectID = {}
    I = {}
    J = {}
    K = {}
    A0 = {}
    A = {}

    def __init__(self):
        self.ID = {}
        self.SectID = {}
        self.I = {}
        self.J = {}
        self.K = {}
        self.N = {}
        self.A0 = {}
        self.A = {}

    def Initialize(tMemCount):
        #
        # Element.L0 = np.zeros(tMemCount)
        Element.x1 = np.zeros(tMemCount)
        Element.y1 = np.zeros(tMemCount)
        Element.z1 = np.zeros(tMemCount)
        Element.Fx1 = np.zeros(tMemCount)
        Element.Fy1 = np.zeros(tMemCount)
        Element.Fz1 = np.zeros(tMemCount)
        Element.Mx1 = np.zeros(tMemCount)
        Element.My1 = np.zeros(tMemCount)
        Element.Mz1 = np.zeros(tMemCount)
        Element.thx1 = np.zeros(tMemCount)
        Element.thy1 = np.zeros(tMemCount)
        Element.thz1 = np.zeros(tMemCount)

        Element.x2 = np.zeros(tMemCount)
        Element.y2 = np.zeros(tMemCount)
        Element.z2 = np.zeros(tMemCount)
        Element.Fx2 = np.zeros(tMemCount)
        Element.Fy2 = np.zeros(tMemCount)
        Element.Fz2 = np.zeros(tMemCount)
        Element.Mx2 = np.zeros(tMemCount)
        Element.My2 = np.zeros(tMemCount)
        Element.Mz2 = np.zeros(tMemCount)
        Element.thx2 = np.zeros(tMemCount)
        Element.thy2 = np.zeros(tMemCount)
        Element.thz2 = np.zeros(tMemCount)

        Element.x3 = np.zeros(tMemCount)
        Element.y3 = np.zeros(tMemCount)
        Element.z3 = np.zeros(tMemCount)
        Element.Fx3 = np.zeros(tMemCount)
        Element.Fy3 = np.zeros(tMemCount)
        Element.Fz3 = np.zeros(tMemCount)
        Element.Mx3 = np.zeros(tMemCount)
        Element.My3 = np.zeros(tMemCount)
        Element.Mz3 = np.zeros(tMemCount)
        Element.thx3 = np.zeros(tMemCount)
        Element.thy3 = np.zeros(tMemCount)
        Element.thz3 = np.zeros(tMemCount)

        Element.delthx1 = np.zeros(tMemCount)
        Element.delthy1 = np.zeros(tMemCount)
        Element.delthz1 = np.zeros(tMemCount)
        Element.delthx2 = np.zeros(tMemCount)
        Element.delthy2 = np.zeros(tMemCount)
        Element.delthz2 = np.zeros(tMemCount)
        Element.delthx3 = np.zeros(tMemCount)
        Element.delthy3 = np.zeros(tMemCount)
        Element.delthz3 = np.zeros(tMemCount)

        Element.EleMtxL = np.zeros((Element.Count * 6, 6))
        Element.EleMtxL0 = np.zeros((Element.Count * 6, 6))
        Element.EleMtxK = np.zeros((Element.Count * 18, 18))
        # [x, y, z, Torsion(thx)]
        Element.GaussPointLocation = GaussPoint.GetGaussPointLocation(Element.ID, Element.I, Element.J)
        # The deflection on the Gauss point on the initial refercence coordinate
        Element.GaussPointCurUL0 = np.zeros([Element.Count, 7, 4])
        # Initialize Element length
        for ii in Element.ID:
            tI = Element.I[ii]
            tJ = Element.J[ii]
            tK = Element.K[ii]
            X1 = Node.X0[tI];
            Y1 = Node.Y0[tI];
            Z1 = Node.Z0[tI]
            X2 = Node.X0[tJ];
            Y2 = Node.Y0[tJ];
            Z2 = Node.Z0[tJ]
            X3 = Node.X0[tK];
            Y3 = Node.Y0[tK];
            Z3 = Node.Z0[tK]

            Element.A0[ii] = (-X2 * Y1 + X3 * Y1 + X1 * Y2 - X3 * Y2 - X1 * Y3 + X2 * Y3)

    def ReadElement(MembInfo):
        Element.Count = len(MembInfo)
        Element.ID = dict(zip_longest(MembInfo[:, 0], np.arange(Element.Count)))
        Element.SectID = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 1]))
        Element.I = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 2]))
        Element.J = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 3]))
        Element.K = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 4]))
        # Element.L0 = dict(zip_longest(MembInfo[:, 0], np.zeros(Element.Count)))
        Element.Initialize(Element.Count)
        return

    # --------------------------------------------------------------------------
    def GetElementDelU(self, Node, DelU, tindex):
        tMID = self.ID[tindex]
        # mL = self.L[tMID]
        tSectID = self.SectID[tindex]
        # Get Matrix L
        MtxL = self.EleMtxL[tMID * 3:tMID * 3 + 3, 0:3]
        # Update Element length
        # Get Element Deflections from global
        MemDelUL = np.zeros(14)
        MemDelU12L = np.zeros(12)
        MemDelUG = np.zeros(14)
        MemDelU12G = np.zeros(12)
        # Transfer to the Local axes
        tI = Node.ID[self.I[tindex]]
        tJ = Node.ID[self.J[tindex]]
        MemDelUG[0:7] = DelU[7 * tI:7 * tI + 7]  # global
        MemDelUG[7:14] = DelU[7 * tJ:7 * tJ + 7]  # global
        MemDelU12G[0:6] = DelU[7 * tI:7 * tI + 6]  # global
        MemDelU12G[6:12] = DelU[7 * tJ:7 * tJ + 6]  # global
        MtxL12 = np.zeros((12, 12))
        MtxL12[0:3, 0:3] = MtxL12[3:6, 3:6] = MtxL12[6:9, 6:9] = MtxL12[9:12, 9:12] = MtxL
        MemDelU12 = np.dot(MtxL12.transpose(), MemDelU12G)
        # MemDelU[0:6]=MemDelU12[0:6]; MemDelU[7:13]=MemDelU12[6:12]
        self.delthx1[tMID] = MemDelU12[3]  # local
        self.delthx2[tMID] = MemDelU12[9]  # local
        self.delthy1[tMID] = MemDelU12[4]  # local
        self.delthy2[tMID] = MemDelU12[10]  # local
        self.delthz1[tMID] = MemDelU12[5]  # local
        self.delthz2[tMID] = MemDelU12[11]  # local
        MemDelUL[0:6] = MemDelU12[0:6]  # local
        MemDelUL[7:13] = MemDelU12[6:12]  # local
        MemDelUL[6] = MemDelUG[6] # local warping displacement
        MemDelUL[13] = MemDelUG[13] # local warping displacement
        return MemDelUG, MemDelUL

    def MemDelUUpdate(self, MemDelU, MID):
        self.x1[MID] += MemDelU[0]
        self.x2[MID] += MemDelU[7]
        self.y1[MID] += MemDelU[1]
        self.y2[MID] += MemDelU[8]
        self.z1[MID] += MemDelU[2]
        self.z2[MID] += MemDelU[9]
        self.thx1[MID] += MemDelU[3]
        self.thx2[MID] += MemDelU[10]
        self.thy1[MID] += MemDelU[4]
        self.thy2[MID] += MemDelU[11]
        self.thz1[MID] += MemDelU[5]
        self.thz2[MID] += MemDelU[12]
        self.thb1[MID] += MemDelU[6]
        self.thb2[MID] += MemDelU[13]

    def MemLenUpdate(self, Node,ii):
        # Initilize Element length
        tI = self.I[ii]
        tJ = self.J[ii]
        tX1 = Node.X[tI]
        tX2 = Node.X[tJ]
        tY1 = Node.Y[tI]
        tY2 = Node.Y[tJ]
        tZ1 = Node.Z[tI]
        tZ2 = Node.Z[tJ]
        self.L[self.ID[ii]] = math.sqrt((tX2 - tX1) ** 2 + (tY2 - tY1) ** 2 + (tZ2 - tZ1) ** 2)
        return

    def MemMtxLUpdate(self, Node, ii):
        tMID = self.ID[ii]
        mL = self.L[tMID]
        mL0 = self.L0[ii]
        tX1 = Node.X[self.I[ii]];
        tX01 = Node.X0[self.I[ii]]
        tX2 = Node.X[self.J[ii]];
        tX02 = Node.X0[self.J[ii]]
        tY1 = Node.Y[self.I[ii]];
        tY01 = Node.Y0[self.I[ii]]
        tY2 = Node.Y[self.J[ii]];
        tY02 = Node.Y0[self.J[ii]]
        tZ1 = Node.Z[self.I[ii]];
        tZ01 = Node.Z0[self.I[ii]]
        tZ2 = Node.Z[self.J[ii]];
        tZ02 = Node.Z0[self.J[ii]]
        tBeta = self.Beta[ii]
        mthx1 = self.thx1[tMID]
        mthx2 = self.thx2[tMID]
        mthy1 = self.thy1[tMID]
        mthy2 = self.thy2[tMID]
        mthz1 = self.thz1[tMID]
        mthz2 = self.thz2[tMID]
        self.EleMtxL[tMID * 3:tMID * 3 + 3, 0:3] = Transformation.GetMtxL(mL, tX1, tX2, tY1, tY2, tZ1, tZ2, mthx1,
                                                                          mthx2, mthy1, mthy2, mthz1, mthz2, tBeta)
        self.EleMtxL0[tMID * 3:tMID * 3 + 3, 0:3] = Transformation.GetMtxL(mL0, tX01, tX02, tY01, tY02, tZ01, tZ02,
                                                                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tBeta)


        return

    # Get Element deformations by removing the rigid body movements
    def GetMemURemoveRBMove(MemDelU, mL):
        tY1 = MemDelU[1]
        tZ1 = MemDelU[2]
        tY2 = MemDelU[8]
        tZ2 = MemDelU[9]
        DelFy = math.atan2((tZ2 - tZ1), mL)
        DelFz = math.atan2((tY2 - tY1), mL)
        MemDelU[7] = MemDelU[7] - MemDelU[0]
        MemDelU[0] = 0
        MemDelU[8] = 0
        MemDelU[1] = 0
        MemDelU[9] = 0
        MemDelU[2] = 0
        MemDelU[10] = MemDelU[10] - MemDelU[3]
        MemDelU[3] = 0
        MemDelU[4] = MemDelU[4] + DelFy
        MemDelU[11] = MemDelU[11] + DelFy
        MemDelU[5] = MemDelU[5] - DelFz
        MemDelU[12] = MemDelU[12] - DelFz
        return MemDelU

    def StoreMemForces(self, MemResF, MID):
        self.Fx1[MID] += MemResF[0]
        self.Fy1[MID] += MemResF[1]
        self.Fz1[MID] += MemResF[2]
        self.Mx1[MID] += MemResF[3]
        self.My1[MID] += MemResF[4]
        self.Mz1[MID] += MemResF[5]
        self.Mb1[MID] += MemResF[6]
        self.Fx2[MID] += MemResF[7]
        self.Fy2[MID] += MemResF[8]
        self.Fz2[MID] += MemResF[9]
        self.Mx2[MID] += MemResF[10]
        self.My2[MID] += MemResF[11]
        self.Mz2[MID] += MemResF[12]
        self.Mb2[MID] += MemResF[13]
        return

# --------------------------------------------------------------------------
class JointLoad:
    Count = 0
    NodeID = []
    FX = {}
    FY = {}
    FZ = {}
    MX = {}
    MY = {}
    MZ = {}

    def ReadJNTL(JNTLInfo):
        JointLoad.Count = len(JNTLInfo)
        JointLoad.NodeID = dict(zip_longest(JNTLInfo[:, 0], np.arange(JointLoad.Count)))
        JointLoad.FX = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 1]))
        JointLoad.FY = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 2]))
        JointLoad.FZ = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 3]))
        JointLoad.MX = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 4]))
        JointLoad.MY = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 5]))
        JointLoad.MZ = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 6]))
        return
class Boundary:
    Count = 0
    NodeID = []
    UX = {}
    UY = {}
    UZ = {}
    RX = {}
    RY = {}
    RZ = {}

    def ReadBoun(BounInfo):
        Boundary.Count = len(BounInfo)
        Boundary.NodeID = dict(zip_longest(BounInfo[:, 0], np.arange(Boundary.Count)))
        Boundary.UX = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 1]))
        Boundary.UY = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 2]))
        Boundary.UZ = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 3]))
        Boundary.RX = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 4]))
        Boundary.RY = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 5]))
        Boundary.RZ = dict(zip_longest(BounInfo[:, 0], BounInfo[:, 6]))
        return

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
    def ReadAna(tAanalInfo):
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
