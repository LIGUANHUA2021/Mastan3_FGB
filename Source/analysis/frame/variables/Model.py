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
from analysis.frame.util import Transformation, GaussPoint


# ===========================================================================
def initialize():
    # Member Geometry
    Member.Initialize(Member.Count)
    # Initialize member length & member matrix L
    for ii in Member.ID:
        Member.MemLenUpdate(Member, Node, ii)
        Member.MemMtxLUpdate(Member, Node, ii)
    # MemGeometry.update(model.Member,model.Node)
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

class Node:
    Count = 0
    ID = []
    X = {}
    Y = {}
    Z = {}
    thX = {}
    thY = {}
    thZ = {}
    thB = {}
    X0 = {}
    Y0 = {}
    Z0 = {}
    thX0 = {}
    thY0 = {}
    thZ0 = {}
    thB0 = {}
    Fg = {}
    CurU = {}
    CurF = {}

    def __init__(self):
        self.Count = 0
        self.ID = []
        self.X = {}
        self.Y = {}
        self.Z = {}
        self.thX = {}
        self.thY = {}
        self.thZ = {}
        self.thB = {}
        self.X0 = {}
        self.Y0 = {}
        self.Z0 = {}
        self.thX0 = {}
        self.thY0 = {}
        self.thZ0 = {}
        self.thB0 = {}
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
        self.thB = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.X0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 1]))
        self.Y0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 2]))
        self.Z0 = dict(zip_longest(NodeInfo[:, 0], NodeInfo[:, 3]))
        self.thX0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thY0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thZ0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.thB0 = dict(zip_longest(NodeInfo[:, 0], np.zeros(Node.Count)))
        self.Fg = np.zeros(Node.Count * 7)
        self.CurU = np.zeros(Node.Count * 7)
        self.CurF = np.zeros(Node.Count * 7)
        return

    def NodeUpdate(self, tDelU):
        for ii in Node.ID:
            self.X[ii] += tDelU[self.ID[ii] * 7]
            self.Y[ii] += tDelU[self.ID[ii] * 7 + 1]
            self.Z[ii] += tDelU[self.ID[ii] * 7 + 2]
            self.thX[ii] += tDelU[self.ID[ii] * 7 + 3]
            self.thY[ii] += tDelU[self.ID[ii] * 7 + 4]
            self.thZ[ii] += tDelU[self.ID[ii] * 7 + 5]
            self.thB[ii] += tDelU[self.ID[ii] * 7 + 6]

    def NodeFgUpdate(self):

        for ii in JointLoad.NodeID:
            self.Fg[Node.ID[ii] * 7 + 0] = JointLoad.FX[ii]
            self.Fg[Node.ID[ii] * 7 + 1] = JointLoad.FY[ii]
            self.Fg[Node.ID[ii] * 7 + 2] = JointLoad.FZ[ii]
            self.Fg[Node.ID[ii] * 7 + 3] = JointLoad.MX[ii]
            self.Fg[Node.ID[ii] * 7 + 4] = JointLoad.MY[ii]
            self.Fg[Node.ID[ii] * 7 + 5] = JointLoad.MZ[ii]
        # Apply boundary
        for ii in Boundary.NodeID:
            tNodeID = Node.ID[ii]
            if Boundary.UX[ii]: Node.Fg[tNodeID * 7] = 0
            if Boundary.UY[ii]: Node.Fg[tNodeID * 7 + 1] = 0
            if Boundary.UZ[ii]: Node.Fg[tNodeID * 7 + 2] = 0
            if Boundary.RX[ii]: Node.Fg[tNodeID * 7 + 3] = 0
            if Boundary.RY[ii]: Node.Fg[tNodeID * 7 + 4] = 0
            if Boundary.RZ[ii]: Node.Fg[tNodeID * 7 + 5] = 0

        return


# --------------------------------------------------------------------------
class Member:
    Count = 0
    ID = []
    SectID = []
    I = {}
    J = {}
    L0 = {}
    Beta = {}

    def Initialize(tMemCount):
        #
        Member.L = np.zeros(tMemCount)
        # Member.L0 = np.zeros(tMemCount)
        Member.x1 = np.zeros(tMemCount)
        Member.y1 = np.zeros(tMemCount)
        Member.z1 = np.zeros(tMemCount)
        Member.Fx1 = np.zeros(tMemCount)
        Member.Fy1 = np.zeros(tMemCount)
        Member.Fz1 = np.zeros(tMemCount)
        Member.Mx1 = np.zeros(tMemCount)
        Member.My1 = np.zeros(tMemCount)
        Member.Mz1 = np.zeros(tMemCount)
        Member.Mb1 = np.zeros(tMemCount)
        Member.thx1 = np.zeros(tMemCount)
        Member.thy1 = np.zeros(tMemCount)
        Member.thz1 = np.zeros(tMemCount)
        Member.thb1 = np.zeros(tMemCount)
        Member.x2 = np.zeros(tMemCount)
        Member.y2 = np.zeros(tMemCount)
        Member.z2 = np.zeros(tMemCount)
        Member.Fx2 = np.zeros(tMemCount)
        Member.Fy2 = np.zeros(tMemCount)
        Member.Fz2 = np.zeros(tMemCount)
        Member.Mx2 = np.zeros(tMemCount)
        Member.My2 = np.zeros(tMemCount)
        Member.Mz2 = np.zeros(tMemCount)
        Member.Mb2 = np.zeros(tMemCount)
        Member.thx2 = np.zeros(tMemCount)
        Member.thy2 = np.zeros(tMemCount)
        Member.thz2 = np.zeros(tMemCount)
        Member.thb2 = np.zeros(tMemCount)
        Member.delthx1 = np.zeros(tMemCount)
        Member.delthy1 = np.zeros(tMemCount)
        Member.delthz1 = np.zeros(tMemCount)
        Member.delthx2 = np.zeros(tMemCount)
        Member.delthy2 = np.zeros(tMemCount)
        Member.delthz2 = np.zeros(tMemCount)
        Member.EleMtxL = np.zeros((Member.Count * 3, 3))
        Member.EleMtxL0 = np.zeros((Member.Count * 3, 3))
        Member.EleMtxK = np.zeros((Member.Count * 14, 14))
        # [x, y, z, Torsion(thx)]
        Member.GaussPointLocation = GaussPoint.GetGaussPointLocation(Member.ID, Member.I, Member.J)
        # The deflection on the Gauss point on the initial refercence coordinate
        Member.GaussPointCurUL0 = np.zeros([Member.Count, 7, 4])
        # Initialize member length
        for ii in Member.ID:
            tI = Member.I[ii]
            tJ = Member.J[ii]
            X1 = Node.X0[tI];
            Y1 = Node.Y0[tI];
            Z1 = Node.Z0[tI]
            X2 = Node.X0[tJ];
            Y2 = Node.Y0[tJ];
            Z2 = Node.Z0[tJ]
            Member.L0[ii] = np.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2 + (Z2 - Z1) ** 2)

    def ReadMember(MembInfo):
        Member.Count = len(MembInfo)
        Member.ID = dict(zip_longest(MembInfo[:, 0], np.arange(Member.Count)))
        Member.SectID = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 1]))
        Member.I = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 2]))
        Member.J = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 3]))
        Member.Beta = dict(zip_longest(MembInfo[:, 0], MembInfo[:, 4]))
        Member.L0 = dict(zip_longest(MembInfo[:, 0], np.zeros(Member.Count)))
        Member.Initialize(Member.Count)
        return
    # def GaussPointCurUL0Update(Member, Node, Section, Material, EleType):
    #     GaussPointCurUL0 = np.zeros([Member.Count, 7, 4])
    #     for ii in Member.ID:
    #         tMemID = Member.ID[ii]
    #         GaussPointCurUL0[tMemID] = EleType.GetGSPointDefl(ii, Member, Node, Section, Material)
    #     return GaussPointCurUL0



    # def MemberGaussPointCurUUpdate(CurU):
    #     GaussPointCoefficients = [0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]

    # def GetMtxT(L):
    #     tMtx = np.zeros((12, 6))
    #     tMtx[0, 0] = tMtx[3, 3] = -1
    #     tMtx[4, 1] = tMtx[5, 2] = tMtx[6, 0] = tMtx[9, 3] = tMtx[10, 4] = tMtx[11, 5] = 1
    #     tMtx[1, 2] = tMtx[1, 5] = tMtx[8, 1] = tMtx[8, 4] = 1 / L
    #     tMtx[7, 2] = tMtx[7, 5] = tMtx[2, 1] = tMtx[2, 4] = -1 / L
    #     return tMtx
    '''
    def GetMtxL(L,X1,X2,Y1,Y2,Z1,Z2,thx1,thx2,thy1,thy2,thz1,thz2,Beta):
        tMtx=np.zeros((3,3))
        Cx=(X2-X1)/L; Cy=(Y2-Y1)/L; Cz=(Z2-Z1)/L
        Q=math.sqrt(Cx*Cx+Cz*Cz)
        tBetai=(X2-X1)/L*thx1+(Y2-Y1)/L*thy1+(Z2-Z1)/L*thz1
        tBetaj=(X2-X1)/L*thx2+(Y2-Y1)/L*thy2+(Z2-Z1)/L*thz2
        Beta=Beta+(tBetai+tBetaj)/2
        if Q>0.0001:
            tMtx0=np.array([
                    [Cx, (-Cx*Cy*math.cos(Beta)-Cz*math.sin(Beta))/Q,\
                          (Cx*Cy*math.sin(Beta)-Cz*math.cos(Beta))/Q],
                    [Cy, Q*math.cos(Beta), -Q*math.sin(Beta)],
                    [Cz, (-Cy*Cz*math.cos(Beta)+Cx*math.sin(Beta))/Q,\
                          (Cy*Cz*math.sin(Beta)+Cx*math.cos(Beta))/Q]])
        else:
            tMtx0=np.array([[0, -Cy*math.cos(Beta), Cy*math.sin(Beta)],
                           [Cy, 0, 0],[0,math.sin(Beta),math.cos(Beta)]])
        tMtx=tMtx0
        return tMtx
    '''

    # --------------------------------------------------------------------------
    def GetMemberDelU(self, Node, DelU, tindex):
        tMID = self.ID[tindex]
        # mL = self.L[tMID]
        tSectID = self.SectID[tindex]
        # Get Matrix L
        MtxL = self.EleMtxL[tMID * 3:tMID * 3 + 3, 0:3]
        # Update member length
        # Get Member Deflections from global
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
        # Initilize Member length
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

    # Get member deformations by removing the rigid body movements
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
class Material:
    Count = 0
    ID = []
    E = {}
    G = {}
    Fy = {}
    Dens = {}

    def ReadMat(MatInfo):
        Material.Count = len(MatInfo)
        Material.ID = dict(zip_longest(MatInfo[:, 0], np.arange(Material.Count)))
        Material.E = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 1]))
        Material.G = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 2]))
        Material.Fy = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 3]))
        Material.Dens = dict(zip_longest(MatInfo[:, 0], MatInfo[:, 4]))
        # ...... for Density & Coefficient of Themal Expansion and so on
        return


# --------------------------------------------------------------------------
class Section:
    Count = 0
    ID = []
    ElementType = 2
    MatID = []
    A = {}
    Iy = {}
    Iz = {}
    J = {}
    Cw = {}
    yc = {}
    zc = {}
    ky = {}
    kz = {}
    betay = {}
    betaz = {}
    betaw = {}

    ## To be added
    ## -----------

    # Read Section Dimensions Information
    def ReadSect(SectInfo):
        Section.Count = len(SectInfo)
        Section.ID = dict(zip_longest(SectInfo[:, 0], np.arange(Section.Count)))
        Section.MatID = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 1]))
        Section.ElementType = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 2]))
        Section.A = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 3]))
        Section.Iy = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 4]))
        Section.Iz = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 5]))
        Section.J = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 6]))
        Section.Cw = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 7]))
        Section.yc = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 8]))
        Section.zc = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 9]))
        Section.ky = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 10]))
        Section.kz = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 11]))
        Section.betay = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 12]))
        Section.betaz = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 13]))
        Section.betaw = dict(zip_longest(SectInfo[:, 0], SectInfo[:, 14]))
        return


# --------------------------------------------------------------------------
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


class Coupling:
    Count = 0
    ID = {}
    Master = {}
    Slave = {}
    UX = {}
    UY = {}
    UZ = {}
    RX = {}
    RY = {}
    RZ = {}
    def ReadCoupl(CouplInfo):
        tMaster = []
        tSlave = []
        tUX = []
        tUY = []
        tUZ = []
        tRX = []
        tRY = []
        tRZ = []
        for ii in CouplInfo:
            for jj in ii[1:]:
                tMaster.append(ii[0])
                tSlave.append(jj[0])
                tUX.append(jj[1])
                tUY.append(jj[2])
                tUZ.append(jj[3])
                tRX.append(jj[4])
                tRY.append(jj[5])
                tRZ.append(jj[6])
        Coupling.Count = len(tMaster)
        Coupling.ID = dict(enumerate(range(Coupling.Count)))
        Coupling.Master = dict(enumerate(tMaster))
        Coupling.Slave = dict(enumerate(tSlave))
        Coupling.UX = dict(enumerate(tUX))
        Coupling.UY = dict(enumerate(tUY))
        Coupling.UZ = dict(enumerate(tUZ))
        Coupling.RX = dict(enumerate(tRX))
        Coupling.RY = dict(enumerate(tRY))
        Coupling.RZ = dict(enumerate(tRZ))
        return

# --------------------------------------------------------------------------
class SpringBoundary:
    Count = 0
    NodeID = []
    Type = {}
    UX = {}
    UY = {}
    UZ = {}
    RX = {}
    RY = {}
    RZ = {}

    def ReadSpringBound(SpringBoundInfo):
        SpringBoundary.Initialize()
        SpringBoundary.Count = len(SpringBoundInfo)
        for ii in range(len(SpringBoundInfo)):
            tSpringBound = SpringBoundInfo[ii]
            tNID = tSpringBound[0]
            SpringBoundary.NodeID.append(tNID)
            SpringBoundary.Type[tNID] = tSpringBound[1]
            SpringBoundary.UX[tNID] = tSpringBound[2]
            SpringBoundary.UY[tNID] = tSpringBound[3]
            SpringBoundary.UZ[tNID] = tSpringBound[4]
            SpringBoundary.RX[tNID] = tSpringBound[5]
            SpringBoundary.RY[tNID] = tSpringBound[6]
            SpringBoundary.RZ[tNID] = tSpringBound[7]
        # SpringBoundary.NodeID = SpringBoundInfo[:, 0]
        # SpringBoundary.Type = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 1]))
        # SpringBoundary.UX = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 2]))
        # SpringBoundary.UY = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 3]))
        # SpringBoundary.UZ = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 4]))
        # SpringBoundary.RX = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 5]))
        # SpringBoundary.RY = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 6]))
        # SpringBoundary.RZ = dict(zip_longest(SpringBoundInfo[:, 0], SpringBoundInfo[:, 7]))

    def Initialize():
        SpringBoundary.Count = 0
        SpringBoundary.NodeID = []
        SpringBoundary.Type = {}
        SpringBoundary.UX = {}
        SpringBoundary.UY = {}
        SpringBoundary.UZ = {}
        SpringBoundary.RX = {}
        SpringBoundary.RY = {}
        SpringBoundary.RZ = {}


# --------------------------------------------------------------------------
class SpringModel:
    Count = 0
    ID = []
    U = {}
    F ={}

    def ReadSpringModel(SpringModelInfo):
        SpringModel.Initialize()
        SpringModel.Count = len(SpringModelInfo)
        for ii in range(SpringModel.Count):
            SpringModel.ID.append(SpringModelInfo[ii][0])
            SpringModel.U[SpringModelInfo[ii][0]] = np.array(SpringModelInfo[ii][1])
            SpringModel.F[SpringModelInfo[ii][0]] = np.array(SpringModelInfo[ii][2])

    def Initialize():
        SpringModel.Count = 0
        SpringModel.ID = []
        SpringModel.U = {}
        SpringModel.R = {}
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
    Yp = {}
    Zp = {}

    def ReadJNTL(JNTLInfo):
        JointLoad.Count = len(JNTLInfo)
        JointLoad.NodeID = dict(zip_longest(JNTLInfo[:, 0], np.arange(JointLoad.Count)))
        JointLoad.FX = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 1]))
        JointLoad.FY = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 2]))
        JointLoad.FZ = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 3]))
        JointLoad.MX = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 4]))
        JointLoad.MY = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 5]))
        JointLoad.MZ = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 6]))
        JointLoad.Yp = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 7]))
        JointLoad.Zp = dict(zip_longest(JNTLInfo[:, 0], JNTLInfo[:, 8]))
        return


# --------------------------------------------------------------------------
class SoilParameter:
    LateralID = []
    LateralCurve = {}
    AxialID = []
    AxialCurve = {}
    TorsionID = []
    TorsionCurve = {}
    ShearID = []
    ShearCurve = {}

    def ReadSoilParameter(SPInfo):
        SoilParameter.Initialize()
        SoilParameter.ReadLateralCurve(SPInfo[0])
        SoilParameter.ReadAxialCurve(SPInfo[1])
        SoilParameter.ReadTorsionCurve(SPInfo[2])
        SoilParameter.ReadShearCurve(SPInfo[3])

    def Initialize():
        SoilParameter.LateralID = []
        SoilParameter.LateralCurve = {}
        SoilParameter.AxialID = []
        SoilParameter.AxialCurve = {}
        SoilParameter.TorsionID = []
        SoilParameter.TorsionCurve = {}
        SoilParameter.ShearID = []
        SoilParameter.ShearCurve = {}

    def ReadLateralCurve(LateralCurveInfo):
        for ii in range(len(LateralCurveInfo) - 1):
            tLateralCurveInfo = LateralCurveInfo[ii + 1]
            SoilParameter.LateralID.append(tLateralCurveInfo[0])
            SoilParameter.LateralCurve[tLateralCurveInfo[0]] = np.array(tLateralCurveInfo[1])

    def ReadAxialCurve(AxialCurveInfo):
        for ii in range(len(AxialCurveInfo) - 1):
            tAxialCurveInfo = AxialCurveInfo[ii + 1]
            SoilParameter.AxialID.append(tAxialCurveInfo[0])
            SoilParameter.AxialCurve[tAxialCurveInfo[0]] = np.array(tAxialCurveInfo[1])

    def ReadTorsionCurve(TorsionCurveInfo):
        for ii in range(len(TorsionCurveInfo) - 1):
            tTorsionCurveInfo = TorsionCurveInfo[ii + 1]
            SoilParameter.TorsionID.append(tTorsionCurveInfo[0])
            SoilParameter.TorsionCurve[tTorsionCurveInfo[0]] = np.array(tTorsionCurveInfo[1])

    def ReadShearCurve(ShearCurveInfo):
        for ii in range(len(ShearCurveInfo) - 1):
            tShearCurveInfo = ShearCurveInfo[ii + 1]
            SoilParameter.ShearID.append(tShearCurveInfo[0])
            SoilParameter.ShearCurve[tShearCurveInfo[0]] = np.array(tShearCurveInfo[1])


# --------------------------------------------------------------------------
class Buried:
    MemID = []
    Lateral = {}
    Axial = {}
    Torsion = {}
    Shear = {}
    R = {}

    def ReadBuried(BuriedInfo):
        Buried.Initialize()
        for ii in range(len(BuriedInfo)):
            tBuriedInfo = BuriedInfo[ii]
            tID = tBuriedInfo[0]
            Buried.MemID.append(tID)
            Buried.Lateral[tID] = tBuriedInfo[1]
            if tBuriedInfo[4] == 0:
                Buried.Axial[tID] = tBuriedInfo[2]
                Buried.Torsion[tID] = tBuriedInfo[3]
                Buried.Shear[tID] = 0
            else:
                Buried.Axial[tID] = 0
                Buried.Torsion[tID] = 0
                Buried.Shear[tID] = tBuriedInfo[4]
            tRI, tRJ = tBuriedInfo[5], tBuriedInfo[6]
            GaussPointCoefficients = [0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]
            GaussPointNum = 7
            tR = np.zeros(GaussPointNum)
            for jj in range(GaussPointNum):
                tR[jj] = np.interp(GaussPointCoefficients[jj], np.array([0, 1]), np.array([tRI, tRJ]))
            Buried.R[tID] = tR

    def Initialize():
        Buried.MemID = []
        Buried.Lateral = {}
        Buried.Axial = {}
        Buried.Torsion = {}
        Buried.Shear = {}
        Buried.R = {}


# --------------------------------------------------------------------------
class GroundAcceleration:
    def __init__(self):
        self.AccDir = 0
        self.iterTime = 0.0
        self.TimeX = []
        self.AccY = []

    def ReadGroundACC(self, GROUNDACCInfo):
        self.AccDir = int(GROUNDACCInfo[0, 0])
        self.iterTime = GROUNDACCInfo[0, 1]
        self.AccY = GROUNDACCInfo[0, 2:]
        self.TimeX = np.linspace(0.0, self.iterTime * np.size(self.AccY), np.size(self.AccY))
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
        # print("tAanalInfo = ", tAanalInfo)
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
