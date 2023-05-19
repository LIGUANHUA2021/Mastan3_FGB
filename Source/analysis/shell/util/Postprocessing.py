import numpy as np
from analysis.shell.util import Transformation
from analysis.shell.element import NLThinTriShell

def GetEleStrs(E, NU, t, X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, U):
    # Calculation of the local coordinate, Vx, Vy and Vz are the local coordinate vector
    Vx = np.array([X2 - X1, Y2 - Y1, Z2 - Z1])
    Vr = np.array([X3 - X1, Y3 - Y1, Z3 - Z1])
    Vz = np.cross(Vx, Vr)
    Vy = np.cross(Vz, Vx)
    x1, y1, z1 = 0, 0, 0
    x2, y2, z2 = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2 + (Z2 - Z1) ** 2) ** 0.5, 0, 0
    x3, y3, z3 = (np.dot(Vx, Vr) / (np.linalg.norm(Vx))), (np.dot(Vy, Vr) / (np.linalg.norm(Vy))), 0

    # Calculation of the B matrix for DKT and CST element using local coordinate
    A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3)
    Em = (E / (1 - NU ** 2)) * np.array([[1, NU, 0], [NU, 1, 0], [0, 0, (1 - NU) / 2]])
    Db = ((E * t ** 3) / (12 * (1 - NU))) * np.array([[1, NU, 0], [NU, 1, 0], [0, 0, (1 - NU) / 2]])

    # B matrix for DKT element
    Gausspoint = np.array([[1 / 2, 0], [1 / 2, 1 / 2], [0, 1 / 2]])
    DKTb = 0
    for i in range(3):
        DKTb += NLThinTriShell.GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint[i])[1]

    # B matrix for CST element
    CSTb = (1 / A) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                  [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])
    # Calculation of the stress σx, σy, σz, τxy, τxz, τyz using local coordinate
    # transform the global U to local u
    u = np.dot(Transformation.GetMtxL(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3), U.transpose()).transpose()

    # Calculation of local Stress
    DKTu = np.array([u[2], u[3], u[4], u[8], u[9], u[10], u[14], u[15], u[16]])
    DKTs = np.dot(Db, np.dot(DKTb, DKTu.transpose()))
    CSTu = np.array([u[0], u[1], u[6], u[7], u[12], u[13]])
    CSTs = np.dot(Em, np.dot(CSTb, CSTu.transpose()))

    TriCSTDKTs = [0, 0, 0, 0, 0, 0]
    TriCSTDKTs[0], TriCSTDKTs[1], TriCSTDKTs[2] = CSTs[0], CSTs[1], DKTs[0]
    TriCSTDKTs[3], TriCSTDKTs[4], TriCSTDKTs[5] = DKTs[1], DKTs[2], CSTs[2]

    return TriCSTDKTs

# def GetElePStrs(sigma):
#     s = np.array([[sigma[0], sigma[5], sigma[3]],
#                   [sigma[5], sigma[1], sigma[4]],
#                   [sigma[3], sigma[4], sigma[2]]])
#     if sigma[0] and sigma[1]:
#         R = (sigma[0] + sigma[1]) / 2
#         Q = ((sigma[0] - sigma[1]) / 2) ** 2 + sigma[2] * sigma[2]
#         M = 2 * sigma[2] / (sigma[0] - sigma[1])
#         s1 = R + np.sqrt(Q)
#         s2 = R - np.sqrt(Q)
#         theta = (np.arctan(M) / 2) * 180 / (np.pi)
#         S = np.array([s1, s2, theta])
#     else:
#         R = 0
#         Q = 0
#         M = 0
#         s1 = 0
#         s2 = 0
#         s3 = sigma[2]
#         S = np.array([s1, s2, s3])
#     return S