import numpy as np
from analysis.shell.util import Transformation

def GetJacobianMtx(x_list, y_list):
    x1, x2, x3 = x_list[0], x_list[1], x_list[2]
    y1, y2, y3 = y_list[0], y_list[1], y_list[2]
    mtxJa = np.zeros((2, 2))
    mtxJa[0, 0] = x2 - x1
    mtxJa[0, 1] = y2 - y1
    mtxJa[1, 0] = x3 - x1
    mtxJa[1, 1] = y3 - y1
    return mtxJa

#Get B matrix, 3x9
def GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint):

    x12, x23, x31 = x1 - x2, x2 - x3, x3 - x1
    y12, y23, y31 = y1 - y2, y2 - y3, y3 - y1
    l12, l23, l31 = (x12 ** 2 + y12 ** 2) ** 0.5, (x23 ** 2 + y23 ** 2) ** 0.5, (x31 ** 2 + y31 ** 2) ** 0.5
    pm4, qm4, tm4, rm4 = - 6 * (x12) / (l12 ** 2), (3 * x12 * y12) / (l12 ** 2), - 6 * (y12) / (l12 ** 2), (3 * y12 ** 2) / (l12 ** 2)
    pm5, qm5, tm5, rm5 = - 6 * (x23) / (l23 ** 2), (3 * x23 * y23) / (l23 ** 2), - 6 * (y23) / (l23 ** 2), (3 * y23 ** 2) / (l23 ** 2)
    pm6, qm6, tm6, rm6 = - 6 * (x31) / (l31 ** 2), (3 * x31 * y31) / (l31 ** 2), - 6 * (y31) / (l31 ** 2), (3 * y31 ** 2) / (l31 ** 2)

    A = (x31 * y12 - x12 * y31)

    # Gauss points
    eta = Gausspoint[0]
    xi = Gausspoint[1]

    Hxxi = np.array([pm6 * (1 - 2 * xi) + (pm5 - pm6) * eta, qm6 * (1 - 2 * xi) - (qm5 + qm6) * eta,
                     - 4 + 6 * (xi + eta) + rm6 * (1 - 2 * xi) - eta * (rm5 + rm6), -pm6 * (1 - 2 * xi) + eta * (pm4 + pm6),
                    qm6 * (1 - 2 * xi) - eta * (qm6 - qm4), - 2 + 6 * xi + rm6 * (1 - 2 * xi) - eta * (rm4 - rm6),
                     - eta * (pm5 + pm4), eta * (qm4 - qm5), - eta * (rm5 - rm4)])

    Hyxi = np.array([tm6 * (1 - 2 * xi) + eta * (tm5 - tm6), 1 + rm6 * (1 - 2 * xi) - eta * (rm5 + rm6),
                        qm6 * (1 - 2 * xi) + eta * (qm5 + qm6), - tm6 * (1 - 2 * xi) + eta * (tm4 + tm6),
                      - 1 + rm6 * (1 - 2 * xi) + eta * (rm4 - rm6), - qm6 * (1 - 2 * xi) - eta * (qm4 -qm6),
                      - eta * (tm4 + tm5), eta * (rm4 - rm5), - eta * (qm4 - qm5)])

    Hxeta = np.array([-pm5 * (1 - 2 * eta) - xi * (pm6 - pm5), qm5 * (1 - 2 * eta) - xi * (qm5 + qm6),
                      - 4 + 6 * (xi + eta) + rm5 * (1 - 2 * eta) - xi * (rm5 + rm6), xi * (pm4 + pm6),
                      xi * (qm4 - qm6), - xi * (rm6 - rm4), pm5 * (1 - 2 * eta) - xi * (pm4 + pm5),
                      qm5 * (1 - 2 * eta) + xi * (qm4 - qm5), - 2 + 6 * eta + rm5 * (1 - 2 * eta) + xi * (rm4 - rm6)])

    Hyeta = np.array([-tm5 * (1 - 2 * eta) - xi * (tm6 - tm5), 1 + rm5 * (1 - 2 * eta) - xi * (rm5 + rm6),
                      qm5 * (1 - 2 * eta) + xi * (qm5 + qm6), xi * (tm4 + tm6), xi * (rm4 - rm6), - xi * (qm4 - qm6),
                      tm5 * (1 - 2 * eta) - xi * (tm4 + tm5), - 1 + rm5 * (1 - 2 * eta) - xi * (rm4 - rm5),
                      qm5 * (1 - 2 * eta) - xi * (qm4 - qm5)])

    CSTMtxB = (1 / A) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                  [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])

    DKTMtxB = (1 / A) * np.array([(-y1 + y3) * Hxxi + (y1 - y2) * Hxeta, (x1 - x3) * Hyxi + (-x1 + x2) * Hyeta,
                               (x1 - x3) * Hxxi + (x2 - x1) * Hxeta + (-y1 + y3) * Hyxi + (y1-y2) * Hyeta])

    MtxB = [CSTMtxB, DKTMtxB]
    return MtxB

#Get Linear Stiffness Matrix, 9x14
def GetEleKl(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, E, v, t):

    #传node类 + node ID, tnode(类)，传入一个member ID, 把member 的node iD抓出来，确定坐标 还有就是在外部确定node ID，传入tiid, tjid, tkid
    VX = np.array([X2 - X1, Y2 - Y1, Z2 - Z1])
    VR = np.array([X3 - X1, Y3 - Y1, Z3 - Z1])
    VZ = np.cross(VX, VR)
    VY = np.cross(VZ, VX)
    x1, y1, z1 = 0, 0, 0
    x2, y2, z2 = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2 + (Z2 - Z1) ** 2) ** 0.5, 0, 0
    x3, y3, z3 = (np.dot(VX, VR)/(np.linalg.norm(VX))), (np.dot(VY, VR)/(np.linalg.norm(VY))), 0

    Em = (E / (1 - v ** 2)) * np.array([[1, v, 0], [v, 1, 0], [0, 0, (1 - v) / 2]])

    Db = ((E * t ** 3) / (12 * (1 - v))) * np.array([[1, v, 0], [v, 1, 0], [0, 0, (1 - v) / 2]])

    A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3)

    CSTMtxB = (1 / A) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                  [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])

    CSTMtxK = np.dot(CSTMtxB.transpose(), Em)

    CSTMtxK = np.dot(CSTMtxK, CSTMtxB) * t * A * (1/2)

    Gausspoint = np.array([[1/2, 0], [1/2, 1/2], [0, 1/2]])

    Sum = 0
    for i in range(len(Gausspoint)):
        a = np.dot(GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint[i])[1].transpose(), Db)
        Sum += np.dot(a, GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint[i])[1])

    DKTMtxK = A * (1/3) * (1/3) * Sum

    TriCSTDKTMtxK = np.zeros((18, 18))

    for i in range(3):
        TriCSTDKTMtxK[i * 6, 0: 2] = CSTMtxK[i * 2, 0:2]
        TriCSTDKTMtxK[i * 6, 6: 8] = CSTMtxK[i * 2, 2:4]
        TriCSTDKTMtxK[i * 6, 12: 14] = CSTMtxK[i * 2, 4:6]
        TriCSTDKTMtxK[i * 6 + 1, 0: 2] = CSTMtxK[i * 2 + 1, 0:2]
        TriCSTDKTMtxK[i * 6 + 1, 6: 8] = CSTMtxK[i * 2 + 1, 2:4]
        TriCSTDKTMtxK[i * 6 + 1, 12: 14] = CSTMtxK[i * 2 + 1, 4:6]

        TriCSTDKTMtxK[i * 6 + 2, 2: 5] = DKTMtxK[i * 3, 0:3]
        TriCSTDKTMtxK[i * 6 + 2, 8: 11] = DKTMtxK[i * 3, 3:6]
        TriCSTDKTMtxK[i * 6 + 2, 14: 17] = DKTMtxK[i * 3, 6:9]
        TriCSTDKTMtxK[i * 6 + 3, 2: 5] = DKTMtxK[i * 3 + 1, 0:3]
        TriCSTDKTMtxK[i * 6 + 3, 8: 11] = DKTMtxK[i * 3 + 1, 3:6]
        TriCSTDKTMtxK[i * 6 + 3, 14: 17] = DKTMtxK[i * 3 + 1, 6:9]
        TriCSTDKTMtxK[i * 6 + 4, 2: 5] = DKTMtxK[i * 3 + 2, 0:3]
        TriCSTDKTMtxK[i * 6 + 4, 8: 11] = DKTMtxK[i * 3 + 2, 3:6]
        TriCSTDKTMtxK[i * 6 + 4, 14: 17] = DKTMtxK[i * 3 + 2, 6:9]

    TriCSTDKTMtxK[5, 5] = max(TriCSTDKTMtxK[0, 0], TriCSTDKTMtxK[1, 1], TriCSTDKTMtxK[2, 2], TriCSTDKTMtxK[3, 3],
                              TriCSTDKTMtxK[4, 4])/1000
    TriCSTDKTMtxK[11, 11] = max(TriCSTDKTMtxK[6, 6], TriCSTDKTMtxK[7, 7], TriCSTDKTMtxK[8, 8], TriCSTDKTMtxK[9, 9],
                              TriCSTDKTMtxK[10, 10]) / 1000
    TriCSTDKTMtxK[17, 17] = max(TriCSTDKTMtxK[12, 12], TriCSTDKTMtxK[13, 13], TriCSTDKTMtxK[14, 14], TriCSTDKTMtxK[15, 15],
                              TriCSTDKTMtxK[16, 16]) / 1000

    MtxL = Transformation.GetMtxL(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
    # print('MtxL = ', MtxL)

    TriCSTDKTMtxK = np.dot(np.dot(MtxL, TriCSTDKTMtxK), MtxL.transpose())

    return TriCSTDKTMtxK

def MemEleMtxToGlo(EleK, Elek, i, j, k):

    I = np.array([6 * i - 6, 6 * i - 5, 6 * i - 4, 6 * i - 3, 6 * i - 2, 6 * i - 1])
    J = np.array([6 * j - 6, 6 * j - 5, 6 * j - 4, 6 * j - 3, 6 * j - 2, 6 * j - 1])
    K = np.array([6 * k - 6, 6 * k - 5, 6 * k - 4, 6 * k - 3, 6 * k - 2, 6 * k - 1])

    a = np.append(np.append(I, J), K)

    for p in range(0, 18):
        EleK[a[p], I[0]] += Elek[p, 0]
        EleK[a[p], I[1]] += Elek[p, 1]
        EleK[a[p], I[2]] += Elek[p, 2]
        EleK[a[p], I[3]] += Elek[p, 3]
        EleK[a[p], I[4]] += Elek[p, 4]
        EleK[a[p], I[5]] += Elek[p, 5]

        EleK[a[p], J[0]] += Elek[p, 6]
        EleK[a[p], J[1]] += Elek[p, 7]
        EleK[a[p], J[2]] += Elek[p, 8]
        EleK[a[p], J[3]] += Elek[p, 9]
        EleK[a[p], J[4]] += Elek[p, 10]
        EleK[a[p], J[5]] += Elek[p, 11]

        EleK[a[p], K[0]] += Elek[p, 12]
        EleK[a[p], K[1]] += Elek[p, 13]
        EleK[a[p], K[2]] += Elek[p, 14]
        EleK[a[p], K[3]] += Elek[p, 15]
        EleK[a[p], K[4]] += Elek[p, 16]
        EleK[a[p], K[5]] += Elek[p, 17]

    return EleK

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
    DKTB = 0
    for i in range(3):
        DKTB += GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint[i])[1]
    # B matrix for CST element
    CSTB = (1 / A) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                  [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])
    # Calculation of the stress σx, σy, σz, τxy, τxz, τyz using local coordinate
    # transform the global u to local u
    u = np.dot(Transformation.GetMtxL(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3).transpose(), U.transpose())
    u = u.transpose()
    # Calculation of local Stress
    DKTu = np.array([u[2], u[3], u[4], u[8], u[9], u[10], u[14], u[15], u[16]])
    DKTS = np.dot(Db, np.dot(DKTB, DKTu.transpose()))
    CSTu = np.array([u[0], u[1], u[6], u[7], u[12], u[13]])
    CSTS = np.dot(Em, np.dot(CSTB, CSTu.transpose()))
    S = np.array([CSTS[0], CSTS[1], DKTS[0], DKTS[1], DKTS[2], CSTS[2]])

    #Calculation of global Stress
    MtxL = Transformation.GetMtxL(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
    q1 = MtxL[0:6, 0:6]
    S = np.dot(q1.transpose(), S)
    return S

def GetElePStrs(sigma):

    R = (sigma[0] + sigma[1]) / 2
    Q = ((sigma[0] - sigma[1]) / 2 ) ** 2 + sigma[2] * sigma[2]
    M = 2 * sigma[2] / (sigma[0] - sigma[1])
    s1 = R + np.sqrt(Q)
    s2 = R - np.sqrt(Q)
    s3 = (np.tan(M) / 2) * 180 / (np.pi)
    y = np.array([s1, s2, s3])
    return y

# if __name__ == '__main__':


