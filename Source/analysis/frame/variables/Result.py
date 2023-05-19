#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Description:
# ===========================================================================
# Import standard libraries
import math
import numpy as np
from numpy import linalg as LA

# Import internal functions
from analysis.frame.variables import Model
from analysis.frame.util import Transformation

class analysisHandler:

    def __init__(self):
        self.Fg = {}
        self.CurU = {}
        self.CurF = {}

class solverStatus:

    def __init__(self):
        self.Cycle = 0
        self.iiter = 0
        self.Time = 0.0
        self.LF = 0.0
        self.dtime = 0.0

    def increaseStep(self):
        self.Cycle += 1
        self.Time += self.dtime
        self.iiter += 1

    def incLoadStep(self, incLF):
        self.LF += incLF
        self.Iter = 0

    def incTimeStep(self,incTime):
        self.Time += incTime


#solverStatus(cycle,ii)


# --------------------------------------------------------------------------

class CyCRes:
    LF = 0
    CurU = {}  ##  Displacement;
    Rect = {}  ##  Reaction Forces;
    MemF = {}  ##  Member Forces;
    Time = 0
    VEL = {}   ##  Velocity;
    ACC = {}   ##  Acceleration;

    def GetRg(Node,Member,EleMtxK,DelU,AnalysisType):
        #MemResF = np.zeros((model.Member.Count, 14))
        Rg = np.zeros(Node.Count * 7)
        CyCRes.MemF = np.zeros((Member.Count, 14))
        flag = 0
        for ii in Member.ID:
            tMID = Member.ID[ii]
            tI = Node.ID[Member.I[ii]]
            tJ = Node.ID[Member.J[ii]]
            MemDelUG, MemDelUL = Member.GetMemberDelU(Member,Node,DelU,ii)
            # Update Member Deformations
            if AnalysisType == "staticLinear":
                pass
            else:
                # Update member length
                Member.MemLenUpdate(Member,Node, ii)
                # Update member deformation
                Member.MemDelUUpdate(Member, MemDelUL,tMID)
                # Update member matrix L
                Member.MemMtxLUpdate(Member, Node, ii)
            # Get member deformations by removing the rigid body movements
            mL = Member.L[tMID]
            MemDelU = Member.GetMemURemoveRBMove(MemDelUL, mL) # mL reference last config
            # Recall Stiffness Matrix
            tEleKl = EleMtxK[tMID * 14:tMID * 14 + 14, 0:14]  # 14x14
            # print(LA.norm(tEleKl))
            MemResF = np.dot(tEleKl, MemDelU)  # 14

            # if flag == 0:
            #     print("Times*************************************************")
            #     fd = open("C:/A_User_Space/test/Revised.txt", "w")
            #     fd.write(MemDelUL.__str__())
            #     # fd.write("\nThis is membU" + MemDelU.__str__())
            #     # fd.write("\nThis is MemF" + MemResF.__str__())
            #     fd.flush()
            #     flag = 1
            #     exit(-99)

            # Store member forces
            Member.StoreMemForces(Member,MemResF,tMID)
            # Form member internal forces matrix
            MtxT = Transformation.GetMtxT(mL)
            P = (Member.Fx2[tMID] - Member.Fx1[tMID]) / 2
            Mt = (Member.Mx2[tMID] - Member.Mx1[tMID]) / 2
            MemResF = np.array([
                Member.Fx1[tMID], Member.Fy1[tMID], Member.Fz1[tMID],
                Member.Mx1[tMID], Member.My1[tMID], Member.Mz1[tMID],
                Member.Mb1[tMID],
                Member.Fx2[tMID], Member.Fy2[tMID], Member.Fz2[tMID],
                Member.Mx2[tMID], Member.My2[tMID], Member.Mz2[tMID],
                Member.Mb2[tMID]])
            MemResF6 = np.array([P, Member.My1[tMID], Member.Mz1[tMID], Mt, Member.My2[tMID], Member.Mz2[tMID]])
            MemResF12 = np.dot(MtxT, MemResF6)
            # Form Transformation matrix
            # Get Matrix L
            MtxL = Member.EleMtxL[tMID * 3:tMID * 3 + 3, 0:3]
            MtxL12 = np.zeros((12, 12))
            MtxL12[0:3, 0:3] = MtxL12[3:6, 3:6] = MtxL12[6:9, 6:9] = MtxL12[9:12, 9:12] = MtxL
            # Get Member force at the global axes
            MemResF12 = np.dot(MtxL12, MemResF12) # global member forces
            MemResF[0:6] = MemResF12[0:6]
            MemResF[7:13] = MemResF12[6:12]
            # Add to global force resisitance vector
            Rg[tI * 7:tI * 7 + 7] += MemResF[0:7]
            Rg[tJ * 7:tJ * 7 + 7] += MemResF[7:14]
            CyCRes.MemF[tMID] = MemResF
        return Rg

    def GetRgs(teletype, Material, Section, Node, Member, SoilParameter, Buried):
        Rgs = np.zeros(Node.Count * 7)
        for ii in Member.ID:
            if ii in Buried.MemID:
                tMID = Member.ID[ii]
                tEleMtxL0 = Member.EleMtxL0[tMID * 3:tMID * 3 + 3, 0:3]
                tRgs = teletype.SoilBoundaryElement.GetRgs(ii, Material, Section, Node, Member, SoilParameter, Buried)
                tRgs[0 : 3] = np.dot(tEleMtxL0, tRgs[0 : 3])
                tRgs[3 : 6] = np.dot(tEleMtxL0, tRgs[3 : 6])
                tRgs[7 : 10] = np.dot(tEleMtxL0, tRgs[7 : 10])
                tRgs[10 : 13] = np.dot(tEleMtxL0, tRgs[10 : 13])
                tI = Node.ID[Member.I[ii]]
                tJ = Node.ID[Member.J[ii]]
                # print("===========================", ii, "=======================================")
                # print("Rsy:", tRgs[1],tRgs[8])
                # print("Msz:", tRgs[5], tRgs[12])
                # Add to global force resisitance vector
                Rgs[tI * 7:tI * 7 + 7] += tRgs[0:7]
                Rgs[tJ * 7:tJ * 7 + 7] += tRgs[7:14]
            else:
                continue
        return Rgs

    def GetRgSpr(SpringBoundary, SpringModel, Node):
        RgSpr = np.zeros(Node.Count * 7)
        for ii in SpringBoundary.NodeID:
            tNID = Node.ID[ii]
            tUX, tUY, tUZ = Node.X[ii] - Node.X0[ii], Node.Y[ii] - Node.Y0[ii], Node.Z[ii] - Node.Z0[ii]
            tRX, tRY, tRZ = Node.thX[ii] - Node.thX0[ii], Node.thY[ii] - Node.thY0[ii], Node.thZ[ii] - Node.thZ0[ii]
            if SpringBoundary.UX[ii] in SpringModel.ID:
                tSprID = SpringBoundary.UX[ii]
                tU, tF = SpringModel.U[tSprID], SpringModel.F[tSprID]
                RgSpr[tNID * 7] += np.interp(abs(tUX), tU, tF) * np.sign(tUX)
            if SpringBoundary.UY[ii] in SpringModel.ID:
                tSprID = SpringBoundary.UY[ii]
                tU, tF = SpringModel.U[tSprID], SpringModel.F[tSprID]
                RgSpr[tNID * 7 + 1] += np.interp(abs(tUY), tU, tF) * np.sign(tUY)
            if SpringBoundary.UZ[ii] in SpringModel.ID:
                tSprID = SpringBoundary.UZ[ii]
                tU, tF = SpringModel.U[tSprID], SpringModel.F[tSprID]
                RgSpr[tNID * 7 + 2] += np.interp(abs(tUZ), tU, tF) * np.sign(tUZ)
            if SpringBoundary.RX[ii] in SpringModel.ID:
                tSprID = SpringBoundary.RX[ii]
                tU, tF = SpringModel.U[tSprID], SpringModel.F[tSprID]
                RgSpr[tNID * 7 + 3] += np.interp(abs(tRX), tU, tF) * np.sign(tRX)
            if SpringBoundary.RY[ii] in SpringModel.ID:
                tSprID = SpringBoundary.RY[ii]
                tU, tF = SpringModel.U[tSprID], SpringModel.F[tSprID]
                RgSpr[tNID * 7 + 4] += np.interp(abs(tRY), tU, tF) * np.sign(tRY)
            if SpringBoundary.RZ[ii] in SpringModel.ID:
                tSprID = SpringBoundary.RZ[ii]
                tU, tF = SpringModel.U[tSprID], SpringModel.F[tSprID]
                RgSpr[tNID * 7 + 5] += np.interp(abs(tRZ), tU, tF) * np.sign(tRZ)
        return RgSpr
    def GetNodeReaction(tbound,Node,Rg):
        # Form member internal forces matrix
        CyCRes.Rect = np.zeros((tbound.Count, 7))
        #Reaction = np.zeros((model.Boundary.Count, 7))
        for ii in tbound.NodeID:
            tNodeID = Node.ID[ii]
            tBoundID = tbound.NodeID[ii]
            if tbound.UX[ii]:
                CyCRes.Rect[tBoundID, 0] = Rg[tNodeID * 7]
                Rg[tNodeID * 7] = 0
            if tbound.UY[ii]:
                CyCRes.Rect[tBoundID, 1] = Rg[tNodeID * 7 + 1]
                Rg[tNodeID * 7 + 1] = 0
            if tbound.UZ[ii]:
                CyCRes.Rect[tBoundID, 2] = Rg[tNodeID * 7 + 2]
                Rg[tNodeID * 7 + 2] = 0
            if tbound.RX[ii]:
                CyCRes.Rect[tBoundID, 3] = Rg[tNodeID * 7 + 3]
                Rg[tNodeID * 7 + 3] = 0
            if tbound.RY[ii]:
                CyCRes.Rect[tBoundID, 4] = Rg[tNodeID * 7 + 4]
                Rg[tNodeID * 7 + 4] = 0
            if tbound.RZ[ii]:
                CyCRes.Rect[tBoundID, 5] = Rg[tNodeID * 7 + 5]
                Rg[tNodeID * 7 + 5] = 0
        return Rg

    def GetCoupledDOF(Coupling, Node, CurU):
        for ii in Coupling.ID:
            tMasterID = Coupling.Master[ii]
            tSlaveID = Coupling.Slave[ii]
            tMaster = Node.ID[tMasterID]
            tSlave = Node.ID[tSlaveID]
            if Coupling.UX:
                CurU[tSlave * 7] = CurU[tMaster * 7]\
                                 + (Node.Z[tSlaveID] - Node.Z[tMasterID]) * CurU[tMaster * 7 + 4]\
                                 - (Node.Y[tSlaveID] - Node.Y[tMasterID]) * CurU[tMaster * 7 + 5]
            if Coupling.UY:
                CurU[tSlave * 7 + 1] = CurU[tMaster * 7 + 1] \
                                     - (Node.Z[tSlaveID] - Node.Z[tMasterID]) * CurU[tMaster * 7 + 3] \
                                     + (Node.X[tSlaveID] - Node.X[tMasterID]) * CurU[tMaster * 7 + 5]
            if Coupling.UZ:
                CurU[tSlave * 7 + 2] = CurU[tMaster * 7 + 2] \
                                     + (Node.Y[tSlaveID] - Node.Y[tMasterID]) * CurU[tMaster * 7 + 3] \
                                     - (Node.X[tSlaveID] - Node.X[tMasterID]) * CurU[tMaster * 7 + 4]
            if Coupling.RX:
                CurU[tSlave * 7 + 3] = CurU[tMaster * 7 + 3]
            if Coupling.RY:
                CurU[tSlave * 7 + 4] = CurU[tMaster * 7 + 4]
            if Coupling.RZ:
                CurU[tSlave * 7 + 5] = CurU[tMaster * 7 + 5]
        return