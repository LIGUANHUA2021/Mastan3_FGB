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

# e.g. local coordinate = GetMtxL * global coordinate
def GetMtxL(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3):
    Vx = np.array([X2 - X1, Y2 - Y1, Z2 - Z1])
    Vr = np.array([X3 - X1, Y3 - Y1, Z3 - Z1])
    Vz = np.cross(Vx, Vr)
    Vy = np.cross(Vz, Vx)
    # direction cosine λx, λy, λz
    lamdax = Vx / (np.sqrt(Vx[0] ** 2 + Vx[1] ** 2 + Vx[2] ** 2))
    lamday = Vy / (np.sqrt(Vy[0] ** 2 + Vy[1] ** 2 + Vy[2] ** 2))
    lamdaz = Vz / (np.sqrt(Vz[0] ** 2 + Vz[1] ** 2 + Vz[2] ** 2))
    lamda = np.array([[lamdax[0], lamdax[1], lamdax[2]],
                      [lamday[0], lamday[1], lamday[2]],
                      [lamdaz[0], lamdaz[1], lamdaz[2]]])
    Tp = np.zeros((6, 6))
    Tp[0:3, 0:3], Tp[3:6, 3:6] = lamda, lamda
    tMtx = np.zeros((18, 18))
    tMtx[0:6, 0:6], tMtx[6:12, 6:12], tMtx[12:18, 12:18] = Tp, Tp, Tp
    return tMtx
