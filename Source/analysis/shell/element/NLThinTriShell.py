import numpy as np
from analysis.shell.util import Transformation
from analysis.shell.util import Assembly
# Routine: Local element stiffness matrix (local coordinate) → Global element stiffness matrix (global coordinate) → Assemble global element stiffness matrix (global coordinate)

#Get B matrix, 3x9
def GetBMtx(x1, y1, x2, y2, x3, y3, GP):
    # -----------------------------------------------------------------------
    # Calculation of the B matrix according to the local coordinates
    x12, x23, x31 = x1 - x2, x2 - x3, x3 - x1
    y12, y23, y31 = y1 - y2, y2 - y3, y3 - y1
    l12, l23, l31 = (x12 ** 2 + y12 ** 2) ** 0.5, (x23 ** 2 + y23 ** 2) ** 0.5, (x31 ** 2 + y31 ** 2) ** 0.5
    am4, bm4, cm4, dm4, em4 = - x23 / (l23 ** 2), 3 * x23 * y23 / (4 * l23 ** 2), ((x23 ** 2) / (4 * l23 ** 2)) - ((y23 ** 2) / (2 * l23 ** 2)), \
                                - y23 / (l23 ** 2), ((y23 ** 2) / (4 * l23 ** 2)) - ((x23 ** 2) / (2 * l23 ** 2))
    am5, bm5, cm5, dm5, em5 = - x31 / (l31 ** 2), 3 * x31 * y31 / (4 * l31 ** 2), ((x31 ** 2) / (4 * l31 ** 2)) - (
                                (y31 ** 2) / (2 * l31 ** 2)), - y31 / (l31 ** 2), ((y31 ** 2) / (4 * l31 ** 2)) - ((x31 ** 2) / (2 * l31 ** 2))
    am6, bm6, cm6, dm6, em6 = - x12 / (l12 ** 2), 3 * x12 * y12 / (4 * l12 ** 2), ((x12 ** 2) / (4 * l12 ** 2)) - ((y12 ** 2) / (2 * l12 ** 2)),\
                              - y12 / (l12 ** 2), ((y12 ** 2) / (4 * l12 ** 2)) - ((x12 ** 2) / (2 * l12 ** 2))
    p4, q4, t4, r4 = 6 * am4, 4 * bm4, 6 * dm4, 3 * (y23 ** 2) / (l23 ** 2)
    p5, q5, t5, r5 = 6 * am5, 4 * bm5, 6 * dm5, 3 * (y31 ** 2) / (l31 ** 2)
    p6, q6, t6, r6 = 6 * am6, 4 * bm6, 6 * dm6, 3 * (y12 ** 2) / (l12 ** 2)
    A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3) * 0.5
    # Gauss points
    eta = GP[0]
    xi = GP[1]
    # -----------------------------------------------------------------------
    # Calculation of the Hxxi, Hyxi, Hxeta, Hyeta
    Hxeta = np.array([- p5 * (1 - 2 * eta) - (p6 - p5) * xi, q5 * (1 - 2 * eta) - (q5 + q6) * xi, - 4 + 6 * (xi + eta) + r5 * (1 - 2 * eta) - (r5 + r6) * xi,
                      (p4 + p6) * xi, (q4 - q6) * xi, - (r6 - r4) * xi, p5 * (1 - 2 * eta) - (p5 + p4) * xi, q5 * (1 - 2 * eta) + (q4 - q5) * xi,
                     - 2 + 6 * eta + r5 * (1 - 2 * eta) + xi * (r4 - r5)])
    Hyxi = np.array([t6 * (1 - 2 * xi) + (t5 - t6) * eta, 1 + r6 * (1 - 2 * xi) - (r5 + r6) * eta, - q6 * (1 - 2 * xi) + (q5 + q6) * eta,
                     - t6 * (1 - 2 * xi) + (t4 + t6) * eta, - 1 + r6 * (1 - 2 * xi) + (r4 - r6) * eta, - q6 * (1 - 2 * xi) - (q4 - q6) * eta,
                     - (t4 + t5) * eta, (r4 - r5) * eta, - (q4 - q5) * eta])
    Hxxi = np.array([p6 * (1 - 2 * xi) + (p5 - p6) * eta, q6 * (1 - 2 * xi) - (q5 + q6) * eta, - 4 + 6 * (xi + eta) + r6 * (1 - 2 * xi) - (r5 + r6) * eta,
                      - p6 * (1 - 2 * xi) + (p4 + p6) * eta, q6 * (1 - 2 * xi) - (q6 - q4) * eta, - 2 + 6 * xi + r6 * (1 - 2 * xi) + (r4 - r6) * eta,
                      - (p5 + p4) * eta, (q4 - q5) * eta, - (r5 - r4) * eta])
    Hyeta = np.array([- t5 * (1 - 2 * eta) - (t6 - t5) * xi, 1 + r5 * (1 - 2 * eta) - (r5 + r6) * xi, (q5 + q6) * xi - q5 * (1 - 2 * eta),
                       (t4 + t6) * xi, (r4 - r6) * xi, - (q4 - q6) * xi, t5 * (1 - 2 * eta) - (t4 + t5) * xi, - 1 + r5 * (1 - 2 * eta) + (r4 - r5) * xi,
                       - (q4 - q5) * xi - q5 * (1 - 2 * eta)])
    # -----------------------------------------------------------------------
    # Assemble the B matrix
    CSTMtxB = (1 / (2 * A)) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                  [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])
    DKTMtxB = (1 / (2 * A)) * np.array([y31 * Hxxi + y12 * Hxeta, - x31 * Hyxi - x12 * Hyeta,
                              - x31 * Hxxi - x12 * Hxeta + y31 * Hyxi + y12 * Hyeta])
    MtxB = [CSTMtxB, DKTMtxB]
    return MtxB


#Get linear stiffness matrix, 18x18, into the global coordinate, return a stiffness matrix (Global coordinate)
def GetEleKL(x1, y1, x2, y2, x3, y3, E, v, t, T):
    # -----------------------------------------------------------------------
    # Calculate and obtain the CST (9x9) and DKT (9x9) linear stiffness matrix (local coordinate)
    CSTMtxKL = GetEleKL_CST(x1, y1, x2, y2, x3, y3, E, v, t)
    DKTMtxKL = GetEleKL_DKT(x1, y1, x2, y2, x3, y3, E, v, t)
    # -----------------------------------------------------------------------
    # Assemble the CST and DKT linear stiffness matrix to obtain TriCSTDKT (18x18) in a local coordinate
    TriCSTDKTMtxKL = np.zeros((18, 18))
    TriCSTDKTMtxKL = Assembly.AssmbelEleMtx(CSTMtxKL, DKTMtxKL, TriCSTDKTMtxKL)
    # -----------------------------------------------------------------------
    # Transfer TriCSTDKT (18x18) from local to global coordinates
    TriCSTDKTMtxKL = np.dot(np.dot(T.transpose(), TriCSTDKTMtxKL), T)
    return TriCSTDKTMtxKL

#Get CST stiffness matrix, 6x6, not including the drilling degree
def GetEleKL_CST(x1, y1, x2, y2, x3, y3, E, v, t):
    Em = (E / (1 - v ** 2)) * np.array([[1, v, 0], [v, 1, 0], [0, 0, (1 - v) / 2]])
    A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3) * 0.5
    CSTMtxB = (1 / (2 * A)) * np.array([[y2 - y3, 0, y3 - y1, 0, y1 - y2, 0], [0, x3 - x2, 0, x1 - x3, 0, x2 - x1],
                                  [x3 - x2, y2 - y3, x1 - x3, y3 - y1, x2 - x1, y1 - y2]])
    CSTMtxKL = np.dot(CSTMtxB.transpose(), Em)
    CSTMtxKL = t * A * np.dot(CSTMtxKL, CSTMtxB)  # local coordinate

    return CSTMtxKL


#Get DKT stiffness matrix, 9x9
def GetEleKL_DKT(x1, y1, x2, y2, x3, y3, E, v, t):
    Db = ((E * t ** 3) / (12 * (1 - v ** 2))) * np.array([[1, v, 0], [v, 1, 0], [0, 0, (1 - v) / 2]])
    A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3) * 0.5
    Gausspoint = np.array([[1 / 2, 0], [1 / 2, 1 / 2], [0, 1 / 2]])
    Sum = 0
    for i in range(len(Gausspoint)):
        a = np.dot(GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint[i])[1].transpose(), Db)
        Sum += (1 / 3) * np.dot(a, GetBMtx(x1, y1, x2, y2, x3, y3, Gausspoint[i])[1])
    DKTMtxKL = A * Sum
    # local coordinate
    return DKTMtxKL

def GetEleKG(x1, y1, x2, y2, x3, y3, CSTs, t, T):
    # -----------------------------------------------------------------------
    #Calculation of the alpha matrix, 12x9
    x12, x23, x31 = x1 - x2, x2 - x3, x3 - x1
    y12, y23, y31 = y1 - y2, y2 - y3, y3 - y1
    l12, l23, l31 = (x12 ** 2 + y12 ** 2) ** 0.5, (x23 ** 2 + y23 ** 2) ** 0.5, (x31 ** 2 + y31 ** 2) ** 0.5
    a4, b4, c4, d4, e4 = (- x23 / l23 ** 2), (3 * x23 * y23 / (4 * l23 ** 2)), (x23 ** 2 - 2 * y23 ** 2) / (4 * l23 ** 2),\
                         (- y23 / l23 ** 2), (y23 ** 2 - 2 * x23 ** 2) / (l23 ** 2)
    a5, b5, c5, d5, e5 = (- x31 / l31 ** 2), (3 * x31 * y31 / (4 * l31 ** 2)), (x31 ** 2 - 2 * y31 ** 2) / (4 * l31 ** 2), \
                         (- y31 / l31 ** 2), (y31 ** 2 - 2 * x31 ** 2) / (l31 ** 2)
    a6, b6, c6, d6, e6 = (- x12 / l12 ** 2), (3 * x12 * y12 / (4 * l12 ** 2)), (x12 ** 2 - 2 * y12 ** 2) / (4 * l12 ** 2), \
                         (- y12 / l12 ** 2), (y12 ** 2 - 2 * x12 ** 2) / (l12 ** 2)
    A = (-x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3) * 0.5
    p4, q4, t4, r4 = 6 * a4, 4 * b4, 6 * d4, 3 * (y23 ** 2) / (l23 ** 2)
    p5, q5, t5, r5 = 6 * a5, 4 * b5, 6 * d5, 3 * (y31 ** 2) / (l31 ** 2)
    p6, q6, t6, r6 = 6 * a6, 4 * b6, 6 * d6, 3 * (y12 ** 2) / (l12 ** 2)
    alphag = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [-p6, -q6, 3 - r6, p6, -q6, 3 - r6, 0, 0, 0],
                    [p5, -q5, 3 - r5, 0, 0, 0, -p5, -q5, 3 - r5],
                    [p5 - p6, - q5 - q6, 6 - r5 - r6, p4 + p6, q4 - q6, r4 - r6, - p4 - p5, q4 - q5, r4 - r5],
                    [p6, q6, r6 - 4, - p6, q6, r6 - 2, 0, 0, 0],
                    [- p5, q5, r5 - 4, 0, 0, 0, p5, q5, r5 -2],
                    [0, -1, 0, 0, 0, 0, 0, 0, 0],
                    [- t6, - r6, q6, t6, - r6, q6, 0, 0, 0],
                    [t5, - r5, q5, 0, 0, 0, - t5, - r5, q5],
                    [t5 - t6, - r5 - r6, q5 + q6, t4 + t6, r4 - r6, q6 - q4, -t4 - t5, r4 - r5, q5 - q4],
                    [t6, 1 + r6, - q6, - t6, r6 - 1, - q6, 0, 0, 0],
                    [- t5, 1 + r5, - q5, 0, 0, 0, t5, r5 - 1, - q5]])
    # -----------------------------------------------------------------------
    # Calculation of the C matrix, 12x12
    C = np.array([[180, 30, 30, 15, 60, 60],
                  [30, 12, 2, 3, 18, 6],
                  [30, 2, 12, 3, 6, 18],
                  [15, 3, 3, 2, 6, 6],
                  [60, 18, 6, 6, 30, 15],
                  [60, 6, 18, 6, 15, 30]])
    G = np.zeros((12, 12))
    G[0:6, 0:6], G[0:6, 6:12], G[6:12, 0:6], G[6:12, 6:12] = CSTs[0, 0] * t * C / 360, CSTs[2, 0] * t * C / 360, CSTs[2, 0] * t * C / 360, CSTs[1, 0] * t * C / 360
    # -----------------------------------------------------------------------
    # Calculation of the geometric stiffness matrix, 9x9 (local coordinate)
    kg = 2 * A * np.dot(np.dot(alphag.transpose(), G), alphag)

    KG = np.zeros((18, 18))
    # transfer to 18 x 18 (local coordinate)
    a = [2, 3, 4, 8, 9, 10, 14, 15, 16]
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(len(a)):
        for j in range(len(a)):
            KG[a[i], a[j]] = kg[b[i], b[j]]

    # Calculate the CST geometric stiffness 9 x 9 (local coordinate)
    TriDKTMtxKG = np.zeros((6, 6))
    AIP = (t / 2) * np.array([- CSTs[2], CSTs[0], -CSTs[1], CSTs[2]])
    TriDKTMtxKG[0:2, 2:4], TriDKTMtxKG[0:2, 4:6] = AIP[0:2, 0:2], - 1 * AIP[0:2, 0:2]
    TriDKTMtxKG[2:4, 0:2], TriDKTMtxKG[2:4, 4:6] = - 1 * AIP[0:2, 0:2], AIP[0:2, 0:2]
    TriDKTMtxKG[4:6, 0:2], TriDKTMtxKG[4:6, 2:4] = AIP[0:2, 0:2], - 1 * AIP[0:2, 0:2]
    # transfer to 18 x 18 (local coordinate)
    a = [0, 1, 6, 7, 12, 13]
    b = [0, 1, 2, 3, 4, 5]
    for i in range(len(a)):
        for j in range(len(a)):
            KG[a[i], a[j]] = TriDKTMtxKG[b[i], b[j]]

    # transfer 18 x 18 matrix to global coordinate
    TriDKTMtxKG = np.dot(np.dot(T.transpose(), KG), T)

    return TriDKTMtxKG
