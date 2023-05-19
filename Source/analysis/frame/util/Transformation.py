###########################################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software
#
# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import numpy as np
import math
# =========================================================================================
# Import internal functions


def GetMtxL(L, X1, X2, Y1, Y2, Z1, Z2, thx1, thx2, thy1, thy2, thz1, thz2, Beta):
    tMtx = np.zeros((3, 3))
    Cx = (X2 - X1) / L
    Cy = (Y2 - Y1) / L
    Cz = (Z2 - Z1) / L
    Q = math.sqrt(Cx * Cx + Cz * Cz)
    tBetai = (X2 - X1) / L * thx1 + (Y2 - Y1) / L * thy1 + (Z2 - Z1) / L * thz1
    tBetaj = (X2 - X1) / L * thx2 + (Y2 - Y1) / L * thy2 + (Z2 - Z1) / L * thz2
    Beta = Beta + (tBetai + tBetaj) / 2
    if Q > 0.0001:
        tMtx0 = np.array([
            [Cx, (-Cx * Cy * math.cos(Beta) - Cz * math.sin(Beta)) / Q, \
             (Cx * Cy * math.sin(Beta) - Cz * math.cos(Beta)) / Q],
            [Cy, Q * math.cos(Beta), -Q * math.sin(Beta)],
            [Cz, (-Cy * Cz * math.cos(Beta) + Cx * math.sin(Beta)) / Q, \
             (Cy * Cz * math.sin(Beta) + Cx * math.cos(Beta)) / Q]])
    else:
        tMtx0 = np.array([[0, -Cy * math.cos(Beta), Cy * math.sin(Beta)],
                          [Cy, 0, 0], [0, math.sin(Beta), math.cos(Beta)]])
    tMtx = tMtx0
    return tMtx


def GetMtxT(L):
    tMtx = np.zeros((12, 6))
    tMtx[0, 0] = tMtx[3, 3] = -1
    tMtx[4, 1] = tMtx[5, 2] = tMtx[6, 0] = tMtx[9, 3] = tMtx[10, 4] = tMtx[11, 5] = 1
    tMtx[1, 2] = tMtx[1, 5] = tMtx[8, 1] = tMtx[8, 4] = 1 / L
    tMtx[7, 2] = tMtx[7, 5] = tMtx[2, 1] = tMtx[2, 4] = -1 / L
    return tMtx


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

