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
import numpy as np
import math
# Import internal functions

# =========================================================================================
####ECC

# def GetMtxTf(tMember, tSect, tSID):
def GetMtxTf(tyc, tzc):
    # ty = tSect.yc[tSID]
    # tz = tSect.zc[tSID]
    ty = tyc
    tz = tzc
    tMtx = np.eye(14, 14)
    tMtxe1 = np.eye(7, 7)
    tMtxe2 = np.eye(7, 7)
    tMtxe1[3, 1] = -tz
    tMtxe1[3, 2] = ty
    tMtxe2[3, 1] = -tz
    tMtxe2[3, 2] = ty
    tMtx[0:7, 0:7] = tMtxe1
    tMtx[7:14, 7:14] = tMtxe2
    return tMtx

# --------------------------------------------------------------------------
def GetMtxTp(tMember, ii, tthx, tYp, tZp):
    thx0 = tMember.Beta[ii]
    thx = -thx0 - tthx
    Yp = tYp * math.cos(thx) + tZp * math.sin(thx)
    Zp = tZp * math.cos(thx) - tYp * math.sin(thx)
    tMtx = np.zeros((12, 12))
    tMtxei = np.zeros((6, 6))
    tMtxej = np.zeros((6, 6))
    # tMtx=np.eye(12,12); tMtxei=np.eye(6,6); tMtxej=np.eye(6,6)
    tMtxei[3, 1] = (-Zp)
    tMtxei[3, 2] = -(-Yp)
    tMtxei[4, 0] = -(-Zp)
    tMtxei[5, 0] = (-Yp)
    tMtxej[3, 1] = (-Zp)
    tMtxej[3, 2] = -(-Yp)
    tMtxej[4, 0] = -(-Zp)
    tMtxej[5, 0] = (-Yp)
    tMtx[0:6, 0:6] = tMtxei
    tMtx[6:12, 6:12] = tMtxej
    return tMtx

# --------------------------------------------------------------------------
'''
def GetMtxT(L):
    tMtx = np.zeros((12, 6))
    tMtx[0, 0] = tMtx[3, 3] = -1
    tMtx[4, 1] = tMtx[5, 2] = tMtx[6, 0] = tMtx[9, 3] = tMtx[10, 4] = tMtx[11, 5] = 1
    tMtx[1, 2] = tMtx[1, 5] = tMtx[8, 1] = tMtx[8, 4] = 1 / L
    tMtx[7, 2] = tMtx[7, 5] = tMtx[2, 1] = tMtx[2, 4] = -1 / L
    return tMtx
'''
# --------------------------------------------------------------------------
# Transform the Element Matrix from local to global systems
def MemEleMtxToGlo(MtxL, EleK):
    tEleK = np.zeros((14, 3))
    tEleK[0:14, 0:3] = EleK[0:14, 0:3]
    tEleK = np.dot(tEleK, MtxL.transpose())
    EleK[0:14, 0:3] = tEleK[0:14, 0:3]
    tEleK = np.zeros((14, 3))
    tEleK[0:14, 0:3] = EleK[0:14, 3:6]
    tEleK = np.dot(tEleK, MtxL.transpose())
    EleK[0:14, 3:6] = tEleK[0:14, 0:3]
    tEleK = np.zeros((14, 3))
    tEleK[0:14, 0:3] = EleK[0:14, 7:10]
    tEleK = np.dot(tEleK, MtxL.transpose())
    EleK[0:14, 7:10] = tEleK[0:14, 0:3]
    tEleK = np.zeros((14, 3))
    tEleK[0:14, 0:3] = EleK[0:14, 10:13]
    tEleK = np.dot(tEleK, MtxL.transpose())
    EleK[0:14, 10:13] = tEleK[0:14, 0:3]
    tEleK = np.zeros((3, 14))
    tEleK[0:3, 0:14] = EleK[0:3, 0:14]
    tEleK = np.dot(MtxL, tEleK)
    EleK[0:3, 0:14] = tEleK[0:3, 0:14]
    tEleK = np.zeros((3, 14))
    tEleK[0:3, 0:14] = EleK[3:6, 0:14]
    tEleK = np.dot(MtxL, tEleK)
    EleK[3:6, 0:14] = tEleK[0:3, 0:14]
    tEleK = np.zeros((3, 14))
    tEleK[0:3, 0:14] = EleK[7:10, 0:14]
    tEleK = np.dot(MtxL, tEleK)
    EleK[7:10, 0:14] = tEleK[0:3, 0:14]
    tEleK = np.zeros((3, 14))
    tEleK[0:3, 0:14] = EleK[10:13, 0:14]
    tEleK = np.dot(MtxL, tEleK)
    EleK[10:13, 0:14] = tEleK[0:3, 0:14]
    return EleK

# --------------------------------------------------------------------------

def AssmbelEleMtxToGlo(tI,tJ,EleK,Kg):
    #tI = Node.ID[Member.I[tMID]]
    #tJ = Node.ID[Member.J[tMID]]
    Kg[tI * 7:tI * 7 + 7, tI * 7:tI * 7 + 7] += EleK[0:7, 0:7]
    Kg[tJ * 7:tJ * 7 + 7, tJ * 7:tJ * 7 + 7] += EleK[7:14, 7:14]
    Kg[tI * 7:tI * 7 + 7, tJ * 7:tJ * 7 + 7] += EleK[0:7, 7:14]
    Kg[tJ * 7:tJ * 7 + 7, tI * 7:tI * 7 + 7] += EleK[7:14, 0:7]

    return Kg


def ApplyCoupl(Coupling, Node, Kg, UnbF):
    for ii in Coupling.ID:
        tMasterID = Coupling.Master[ii]
        tSlaveID = Coupling.Slave[ii]
        tMaster = Node.ID[tMasterID]
        tSlave = Node.ID[tSlaveID]
        Kg[:, tSlave * 7 + 6] = Kg[tSlave * 7 + 6, :] = 0
        Kg[tSlave * 7 + 6, tSlave * 7 + 6] = 1
        UnbF[tSlave * 7 + 6] = 0
        if Coupling.UX[ii]:
            Kg[tMaster * 7, tMaster * 7] += Kg[tSlave * 7, tSlave * 7]
            Col = Kg[:, tSlave * 7]
            Row = Kg[tSlave * 7, :]
            Col[tMaster, 0] = Col[tSlave, 0] = 0
            Row[0, tMaster] = Row[0, tSlave] = 0
            Kg[:, tMaster * 7] += Col
            Kg[tMaster * 7, :] += Row
        if Coupling.UY[ii]:
            Kg[tMaster * 7 + 1, tMaster * 7 + 1] += Kg[tSlave * 7 + 1, tSlave * 7 + 1]
            Col = Kg[:, tSlave * 7 + 1]
            Row = Kg[tSlave * 7 + 1, :]
            Col[tMaster, 0] = Col[tSlave, 0] = 0
            Row[0, tMaster] = Row[0, tSlave] = 0
            Kg[:, tMaster * 7 + 1] += Col
            Kg[tMaster * 7 + 1, :] += Row
        if Coupling.UZ[ii]:
            Kg[tMaster * 7 + 2, tMaster * 7 + 2] += Kg[tSlave * 7 + 2, tSlave * 7 + 2]
            Col = Kg[:, tSlave * 7 + 2]
            Row = Kg[tSlave * 7 + 2, :]
            Col[tMaster, 0] = Col[tSlave, 0] = 0
            Row[0, tMaster] = Row[0, tSlave] = 0
            Kg[:, tMaster * 7 + 2] += Col
            Kg[tMaster * 7 + 2, :] += Row
        if Coupling.RX[ii]:
            Kg[tMaster * 7 + 3, tMaster * 7 + 3] += Kg[tSlave * 7 + 3, tSlave * 7 + 3]\
                                                 + (Node.Z[tSlaveID] - Node.Z[tMasterID]) ** 2 * Kg[tSlave * 7 + 1, tSlave * 7 + 1]\
                                                 + (Node.Y[tSlaveID] - Node.Y[tMasterID]) ** 2 * Kg[tSlave * 7 + 2, tSlave * 7 + 2]\
                                                 - 2 * (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[tMaster * 7 + 3, tMaster * 7 + 1]\
                                                 + 2 * (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[tMaster * 7 + 3, tMaster * 7 + 2]\
                                                 - 2 * (Node.Z[tSlaveID] - Node.Z[tMasterID]) * (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[tMaster * 7 + 1, tMaster * 7 + 2]
            Col = Kg[:, tSlave * 7 + 3] - (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[:, tSlave * 7 + 1] + (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[:, tSlave * 7 + 2]
            Row = Kg[tSlave * 7 + 3, :] - (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[tSlave * 7 + 1, :] + (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[tSlave * 7 + 2, :]
            Col[tMaster, 0] = Col[tSlave, 0] = 0
            Row[0, tMaster] = Row[0, tSlave] = 0
            Kg[:, tMaster * 7 + 3] += Col
            Kg[tMaster * 7 + 3, :] += Row
        if Coupling.RY[ii]:
            Kg[tMaster * 7 + 4, tMaster * 7 + 4] += Kg[tSlave * 7 + 4, tSlave * 7 + 4] \
                                                 + (Node.Z[tSlaveID] - Node.Z[tMasterID]) ** 2 * Kg[tSlave * 7, tSlave * 7] \
                                                 + (Node.X[tSlaveID] - Node.X[tMasterID]) ** 2 * Kg[tSlave * 7 + 2, tSlave * 7 + 2] \
                                                 + 2 * (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[tMaster * 7 + 4, tMaster * 7] \
                                                 - 2 * (Node.X[tSlaveID] - Node.X[tMasterID]) * Kg[tMaster * 7 + 4, tMaster * 7 + 2] \
                                                 - 2 * (Node.Z[tSlaveID] - Node.Z[tMasterID]) * (Node.X[tSlaveID] - Node.X[tMasterID]) * Kg[tMaster * 7, tMaster * 7 + 2]
            Col = Kg[:, tSlave * 7 + 4] + (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[:, tSlave * 7] - (Node.X[tSlaveID] - Node.X[tMasterID]) * Kg[:, tSlave * 7 + 2]
            Row = Kg[tSlave * 7 + 4, :] + (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[tSlave * 7, :] - (Node.X[tSlaveID] - Node.X[tMasterID]) * Kg[tSlave * 7 + 2, :]
            Col[tMaster, 0] = Col[tSlave, 0] = 0
            Row[0, tMaster] = Row[0, tSlave] = 0
            Kg[:, tMaster * 7 + 4] += Col
            Kg[tMaster * 7 + 4, :] += Row
        if Coupling.RZ[ii]:
            Kg[tMaster * 7 + 5, tMaster * 7 + 5] += Kg[tSlave * 7 + 5, tSlave * 7 + 5] \
                                                 + (Node.Y[tSlaveID] - Node.Y[tMasterID]) ** 2 * Kg[tSlave * 7, tSlave * 7] \
                                                 + (Node.X[tSlaveID] - Node.X[tMasterID]) ** 2 * Kg[tSlave * 7 + 1, tSlave * 7 + 1] \
                                                 - 2 * (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[tMaster * 7 + 5, tMaster * 7] \
                                                 + 2 * (Node.X[tSlaveID] - Node.X[tMasterID]) * Kg[tMaster * 7 + 5, tMaster * 7 + 1] \
                                                 - 2 * (Node.Y[tSlaveID] - Node.Y[tMasterID]) * (Node.X[tSlaveID] - Node.X[tMasterID]) * Kg[tMaster * 7, tMaster * 7 + 1]
            Col = Kg[:, tSlave * 7 + 5] - (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[:, tSlave * 7 + 1] + (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[:, tSlave * 7 + 2]
            Row = Kg[tSlave * 7 + 5, :] - (Node.Z[tSlaveID] - Node.Z[tMasterID]) * Kg[tSlave * 7 + 1, :] + (Node.Y[tSlaveID] - Node.Y[tMasterID]) * Kg[tSlave * 7 + 2, :]
            Col[tMaster, 0] = Col[tSlave, 0] = 0
            Row[0, tMaster] = Row[0, tSlave] = 0
            Kg[:, tMaster * 7 + 5] += Col
            Kg[tMaster * 7 + 5, :] += Row
    for ii in Coupling.ID:
        tMaster = Node.ID[Coupling.Master[ii]]
        tSlave = Node.ID[Coupling.Slave[ii]]
        if Coupling.UX[ii]:
            Kg[:, tSlave * 7] = Kg[tSlave * 7, :] = 0
            Kg[tSlave * 7, tSlave * 7] = 1
            UnbF[tMaster * 7] += UnbF[tSlave * 7]
            UnbF[tSlave * 7] = 0
        if Coupling.UY[ii]:
            Kg[:, tSlave * 7 + 1] = Kg[tSlave * 7 + 1, :] = 0
            Kg[tSlave * 7 + 1, tSlave * 7 + 1] = 1
            UnbF[tMaster * 7 + 1] += UnbF[tSlave * 7 + 1]
            UnbF[tSlave * 7 + 1] = 0
        if Coupling.UZ[ii]:
            Kg[:, tSlave * 7 + 2] = Kg[tSlave * 7 + 2, :] = 0
            Kg[tSlave * 7 + 2, tSlave * 7 + 2] = 1
            UnbF[tMaster * 7 + 2] += UnbF[tSlave * 7 + 2]
            UnbF[tSlave * 7 + 2] = 0
        if Coupling.RX[ii]:
            Kg[:, tSlave * 7 + 3] = Kg[tSlave * 7 + 3, :] = 0
            Kg[tSlave * 7 + 3, tSlave * 7 + 3] = 1
            UnbF[tMaster * 7 + 3] += UnbF[tSlave * 7 + 3]
            UnbF[tSlave * 7 + 3] = 0
        if Coupling.RY[ii]:
            Kg[:, tSlave * 7 + 4] = Kg[tSlave * 7 + 4, :] = 0
            Kg[tSlave * 7 + 4, tSlave * 7 + 4] = 1
            UnbF[tMaster * 7 + 4] += UnbF[tSlave * 7 + 4]
            UnbF[tSlave * 7 + 4] = 0
        if Coupling.RZ[ii]:
            Kg[:, tSlave * 7 + 5] = Kg[tSlave * 7 + 5, :] = 0
            Kg[tSlave * 7 + 5, tSlave * 7 + 5] = 1
            UnbF[tMaster * 7 + 5] += UnbF[tSlave * 7 + 5]
            UnbF[tSlave * 7 + 5] = 0
    return Kg, UnbF


def ApplyBdyCond(Boundary, Node, Kg, UnbF):
    for ii in Boundary.NodeID:
        tNodeID = Node.ID[ii]
        if Boundary.UX[ii]:
            Kg[:, tNodeID * 7] = Kg[tNodeID * 7, :] = 0
            Kg[tNodeID * 7, tNodeID * 7] = 1
            UnbF[tNodeID * 7] = 0
        if Boundary.UY[ii]:
            Kg[:, tNodeID * 7 + 1] = Kg[tNodeID * 7 + 1, :] = 0
            Kg[tNodeID * 7 + 1, tNodeID * 7 + 1] = 1
            UnbF[tNodeID * 7 + 1] = 0
        if Boundary.UZ[ii]:
            Kg[:, tNodeID * 7 + 2] = Kg[tNodeID * 7 + 2, :] = 0
            Kg[tNodeID * 7 + 2, tNodeID * 7 + 2] = 1
            UnbF[tNodeID * 7 + 2] = 0
        if Boundary.RX[ii]:
            Kg[:, tNodeID * 7 + 3] = Kg[tNodeID * 7 + 3, :] = 0
            Kg[tNodeID * 7 + 3, tNodeID * 7 + 3] = 1
            UnbF[tNodeID * 7 + 3] = 0
        if Boundary.RY[ii]:
            Kg[:, tNodeID * 7 + 4] = Kg[tNodeID * 7 + 4, :] = 0
            Kg[tNodeID * 7 + 4, tNodeID * 7 + 4] = 1
            UnbF[tNodeID * 7 + 4] = 0
        if Boundary.RZ[ii]:
            Kg[:, tNodeID * 7 + 5] = Kg[tNodeID * 7 + 5, :] = 0
            Kg[tNodeID * 7 + 5, tNodeID * 7 + 5] = 1
            UnbF[tNodeID * 7 + 5] = 0
    return Kg, UnbF

