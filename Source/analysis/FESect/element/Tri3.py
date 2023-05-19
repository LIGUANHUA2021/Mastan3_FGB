###########################################################################################
#
# PyFESect - Python-based Cross-platforms Section Analysis Software
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Liang Chen, Haoyi Zhang, Guanhua Li
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import numpy as np
import os
# =========================================================================================
# Import internal functions


def GetA(V, W):
    A = 0
    Seq = ""
    if V[0] != V[-1] or W[0] != W[-1]:
        V.append(V[0])
        W.append(W[0])

    for i in range(len(V) - 1):
        A += (V[i + 1] * W[i] - V[i] * W[i + 1]) / 2

    if A < 0:
        Seq = "Clockwise"
    elif A > 0:
        Seq = "AntiClockwise"

    A = abs(A)
    return A, Seq

def GetCy(Y, Z, A, Seq):
    cy = 0
    if Y[0] != Y[-1] or Z[0] != Z[-1]:
        Y.append(Y[0])
        Z.append(Z[0])

    if A == 0:
        cy = 0
    else:
        for i in range(len(Y) - 1):
            cy += (Y[i] + Y[i + 1]) * (Y[i + 1] * Z[i] - Y[i] * Z[i + 1]) / (6 * A)

    if Seq == "Clockwise":
        cy = -cy
    return cy

def GetCz(Y, Z, A, Seq):
    cz = 0
    if Y[0] != Y[-1] or Z[0] != Z[-1]:
        Y.append(Y[0])
        Z.append(Z[0])

    if A == 0:
        cz = 0
    else:
        for i in range(len(Y) - 1):
            cz += (Z[i] + Z[i + 1]) * (Y[i + 1] * Z[i] - Y[i] * Z[i + 1]) / (6 * A)

    if Seq == "Clockwise":
        cz = -cz
    return cz

def GetIy(Y, Z, A, cz):
    Iy = 0
    if Y[0] != Y[-1] or Z[0] != Z[-1]:
        Y.append(Y[0])
        Z.append(Z[0])

    for i in range(len(Y) - 1):
        Iy += (Y[i + 1] * Z[i] - Y[i] * Z[i + 1]) * (Z[i] ** 2 + Z[i] * Z[i + 1] + Z[i + 1] ** 2) / 12
    Iy = abs(Iy) - A * cz ** 2
    return Iy

def GetIz(Y, Z, A, cy):
    Iz = 0
    if Y[0] != Y[-1] or Z[0] != Z[-1]:
        Y.append(Y[0])
        Z.append(Z[0])

    for i in range(len(Y) - 1):
        Iz += (Y[i + 1] * Z[i] - Y[i] * Z[i + 1]) * (Y[i] ** 2 + Y[i] * Y[i + 1] + Y[i + 1] ** 2) / 12
    Iz = abs(Iz) - A * cy ** 2
    return Iz

def GetIyz(Y, Z, A, cy, cz, Seq):
    Iyz = 0
    if Y[0] != Y[-1] or Z[0] != Z[-1]:
        Y.append(Y[0])
        Z.append(Z[0])

    for i in range(len(Y) - 1):
        Iyz += (Y[i + 1] * Z[i] - Y[i] * Z[i + 1]) * (Y[i + 1] * Z[i] + Y[i] * Z[i + 1] + 2 * (Y[i] * Z[i] + Y[i + 1] * Z[i + 1])) / 24
    if Seq == "Clockwise":
        Iyz = -Iyz - A * cy * cz
    elif Seq == "AntiClockwise":
        Iyz = Iyz - A * cy * cz
    return Iyz

def TruncatedTriangleAreas(V, W, A, AxisV):
    Vt = []
    Vb = []
    Wt = []
    Wb = []

    for i in range(len(V)):
        if V[i] >= AxisV:
            Vt.append(V[i])
            Wt.append(W[i])
        else:
            Vb.append(V[i])
            Wb.append(W[i])

    if len(Vt) == 1:
        Wdv1 = Wb[0] + (Wt[0] - Wb[0]) * (AxisV - Vb[0]) / (Vt[0] - Vb[0])
        Wdv2 = Wb[1] + (Wt[0] - Wb[1]) * (AxisV - Vb[1]) / (Vt[0] - Vb[1])
        Ac = abs((Wdv2 - Wdv1) * (Vt[0] - AxisV) / 2)
        At = A - Ac
    elif len(Vt) == 2:
        Wdv1 = Wt[0] + (Wb[0] - Wt[0]) * (AxisV - Vt[0]) / (Vb[0] - Vt[0])
        Wdv2 = Wt[1] + (Wb[0] - Wt[1]) * (AxisV - Vt[1]) / (Vb[0] - Vt[1])
        At = abs((Wdv2 - Wdv1) * (Vb[0] - AxisV) / 2)
        Ac = A - At

    return Ac, At

def TruncatedTriangleStatics(V, W, A, AxisV):
    Vt = []
    Vb = []
    Wt = []
    Wb = []

    for i in range(len(V)):
        if V[i] >= AxisV:
            Vt.append(V[i])
            Wt.append(W[i])
        else:
            Vb.append(V[i])
            Wb.append(W[i])

    if len(Vt) == 1:
        Wdv1 = Wb[0] + (Wt[0] - Wb[0]) * (AxisV - Vb[0]) / (Vt[0] - Vb[0])
        Wdv2 = Wb[1] + (Wt[0] - Wb[1]) * (AxisV - Vb[1]) / (Vt[0] - Vb[1])
        Ac = abs((Wdv2 - Wdv1) * (Vt[0] - AxisV) / 2)
        At = A - Ac
        Qc = Ac * (Vt[0] - AxisV) / 3
        Coords = [[Vb[0], Wb[0]], [Vb[1], Wb[1]], [AxisV, Wdv2], [AxisV, Wdv1]]
        UniCoords = [list(j) for j in set(tuple(k) for k in Coords)]
        UniCoords.sort(key=Coords.index)
        Seq = GetA([j[0] for j in UniCoords], [j[1] for j in UniCoords])[1]
        Qt = At * (AxisV - GetCy([j[0] for j in UniCoords], [j[1] for j in UniCoords], At, Seq))

    elif len(Vt) == 2:
        Wdv1 = Wt[0] + (Wb[0] - Wt[0]) * (AxisV - Vt[0]) / (Vb[0] - Vt[0])
        Wdv2 = Wt[1] + (Wb[0] - Wt[1]) * (AxisV - Vt[1]) / (Vb[0] - Vt[1])
        At = abs((Wdv2 - Wdv1) * (Vb[0] - AxisV) / 2)
        Ac = A - At
        Qt = At * (AxisV - Vb[0]) / 3
        Coords = [[Vt[0], Wt[0]], [Vt[1], Wt[1]], [AxisV, Wdv2], [AxisV, Wdv1]]
        UniCoords = [list(j) for j in set(tuple(k) for k in Coords)]
        UniCoords.sort(key=Coords.index)
        Seq = GetA([j[0] for j in UniCoords], [j[1] for j in UniCoords])[1]
        Qc = Ac * (GetCy([j[0] for j in UniCoords], [j[1] for j in UniCoords], Ac, Seq) - AxisV)

    return Qc, Qt


def GetMtxN(Eta, Xi):
    MtxN = np.array([Eta, Xi, 1 - Xi - Eta])
    return MtxN

def GetdNdGlobal(Y, Z):
    Y1 = Y[0]
    Y2 = Y[1]
    Y3 = Y[2]
    Z1 = Z[0]
    Z2 = Z[1]
    Z3 = Z[2]
    dEtady = (-Z2 + Z3) / (Y3 * (-Z1 + Z2) + Y2 * (Z1 - Z3) + Y1 * (-Z2 + Z3))
    dXidy = (Z1 - Z3) / (Y2 * Z1 - Y3 * Z1 - Y1 * Z2 + Y3 * Z2 + Y1 * Z3 - Y2 * Z3)
    dEtadz = (Y2 - Y3) / (Y2 * Z1 - Y3 * Z1 - Y1 * Z2 + Y3 * Z2 + Y1 * Z3 - Y2 * Z3)
    dXidz = (Y1 - Y3) / (Y3 * (Z1 - Z2) + Y1 * (Z2 - Z3) + Y2 * (-Z1 + Z3))
    dN1dEta = 1
    dN1dXi = 0
    dN2dEta = 0
    dN2dXi = 1
    dN3dEta = -1
    dN3dXi = -1
    dN1dy = dN1dEta * dEtady + dN1dXi * dXidy
    dN2dy = dN2dEta * dEtady + dN2dXi * dXidy
    dN3dy = dN3dEta * dEtady + dN3dXi * dXidy
    dN1dz = dN1dEta * dEtadz + dN1dXi * dXidz
    dN2dz = dN2dEta * dEtadz + dN2dXi * dXidz
    dN3dz = dN3dEta * dEtadz + dN3dXi * dXidz
    dNdy = np.array([dN1dy, dN2dy, dN3dy])
    dNdz = np.array([dN1dz, dN2dz, dN3dz])
    return dNdy, dNdz

def GetMtxB(Y, Z):
    dNdy = GetdNdGlobal(Y, Z)[0]
    dNdz = GetdNdGlobal(Y, Z)[1]
    MtxB = np.array([[dNdy[0], 0, dNdy[1], 0, dNdy[2], 0],
                     [0, dNdz[0], 0, dNdz[1], 0, dNdz[2]],
                     dNdz[0], dNdy[0], dNdz[1], dNdy[1], dNdz[2], dNdy[2]])
    return MtxB


def GetMtxJ(Y, Z):
    Y1 = Y[0]
    Y2 = Y[1]
    Y3 = Y[2]
    Z1 = Z[0]
    Z2 = Z[1]
    Z3 = Z[2]
    MtxJ = np.array([[Z1 - Z3, Y1 - Y3],
                     [Z2 - Z3, Y2 - Y3]])
    return MtxJ


def GetKePe(y, z, GPNum, GPs, Wts):
    Ke = np.zeros([3, 3])
    Pe = np.zeros([3, 1])
    MtxJ = GetMtxJ(y, z)
    (tdNdy, tdNdz) = GetdNdGlobal(y, z)
    dNdy = np.array([tdNdy])
    dNdz = np.array([tdNdz])
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        Ke += 0.5 * Wts[i] * (dNdy.T.dot(dNdy) + dNdz.T.dot(dNdz)) * abs(np.linalg.det(MtxJ))
        Pe += 0.5 * Wts[i] * (N.dot(y) * dNdz.T - N.dot(z) * dNdy.T) * abs(np.linalg.det(MtxJ))
    return Ke, Pe


def GetAomg(V, W, Omega, GPNum, GPs, Wts):
    Aomg = 0
    MtxJ = GetMtxJ(V, W)
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        Aomg += 0.5 * Wts[i] * N.dot(Omega) * abs(np.linalg.det(MtxJ))
    return Aomg

def GetAvomgAwomg(V, W, Omega, GPNum, GPs, Wts):
    Avomg = 0
    Awomg = 0
    MtxJ = GetMtxJ(V, W)
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        Avomg += 0.5 * Wts[i] * N.dot(V) * N.dot(Omega) * abs(np.linalg.det(MtxJ))
        Awomg += 0.5 * Wts[i] * N.dot(W) * N.dot(Omega) * abs(np.linalg.det(MtxJ))
    return Avomg, Awomg

def GetJ(Y, Z, Omega, cys, czs, GPNum, GPs, Wts):
    J = 0
    (dNdy, dNdz) = GetdNdGlobal(Y, Z)
    MtxJ = GetMtxJ(Y, Z)
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        J += 0.5 * Wts[i] * ((dNdy.dot(Omega) + (N.dot(Z) - czs)) * (N.dot(Z) - czs) - (dNdz.dot(Omega) - (N.dot(Y) - cys)) * (N.dot(Y) - cys)) * abs(np.linalg.det(MtxJ))
    return J

def GetIomg(Y, Z, Omega, GPNum, GPs, Wts):
    Iomg = 0
    MtxJ = GetMtxJ(Y, Z)
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        Iomg += 0.5 * Wts[i] * (N.dot(Omega)) ** 2 * abs(np.linalg.det(MtxJ))
    return Iomg


def GetWagnerCoefIntg(Y, Z, Omega, GPNum, GPs, Wts):
    Betay = 0
    Betaz = 0
    Betaomg = 0
    MtxJ = GetMtxJ(Y, Z)
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        Betay += 0.5 * Wts[i] * ((N.dot(Z)) ** 3 + (N.dot(Z)) * (N.dot(Y)) ** 2) * abs(np.linalg.det(MtxJ))
        Betaz += 0.5 * Wts[i] * ((N.dot(Y)) ** 3 + (N.dot(Y)) * (N.dot(Z)) ** 2) * abs(np.linalg.det(MtxJ))
        Betaomg += 0.5 * Wts[i] * (N.dot(Omega)) * ((N.dot(Y)) ** 2 + (N.dot(Z)) ** 2) * abs(np.linalg.det(MtxJ))
    return Betay, Betaz, Betaomg


def GetShearLoad(y, z, Iy, Iz, Iyz, nu, GPNum, GPs, Wts):
    Pey = np.zeros([3, 1])
    Pez = np.zeros([3, 1])
    MtxJ = GetMtxJ(y, z)
    (dNdy, dNdz) = GetdNdGlobal(y, z)
    B = np.array([dNdy,
                  dNdz])
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        N = np.array([N])
        r = N.dot(z) ** 2 - N.dot(y) ** 2
        q = 2 * N.dot(y) * N.dot(z)
        h1 = -Iy * r - Iyz * q
        h2 = -Iyz * r + Iy * q
        d1 = Iyz * r + Iz * q
        d2 = Iz * r - Iyz * q
        h = np.array([h1,
                      h2])
        d = np.array([d1,
                      d2])

        Pey += 0.5 * Wts[i] * (nu / 2 * B.T.dot(h) + 2 * (1 + nu) * N.T * (Iy * N.dot(y) - Iyz * N.dot(z))) * abs(np.linalg.det(MtxJ))
        Pez += 0.5 * Wts[i] * (nu / 2 * B.T.dot(d) + 2 * (1 + nu) * N.T * (Iz * N.dot(z) - Iyz * N.dot(y))) * abs(np.linalg.det(MtxJ))
    return Pey, Pez


def GetKappa(y, z, Phi, Psi, Iy, Iz, Iyz, nu, GPNum, GPs, Wts):
    Kappay = 0
    Kappaz = 0
    Phi = np.array([Phi]).T
    Psi = np.array([Psi]).T
    MtxJ = GetMtxJ(y, z)
    (dNdy, dNdz) = GetdNdGlobal(y, z)
    B = np.array([dNdy,
                  dNdz])
    for i in range(GPNum):
        N = GetMtxN(GPs[i, 0], GPs[i, 1])
        r = N.dot(z) ** 2 - N.dot(y) ** 2
        q = 2 * N.dot(y) * N.dot(z)
        h1 = -Iy * r - Iyz * q
        h2 = -Iyz * r + Iy * q
        d1 = Iyz * r + Iz * q
        d2 = Iz * r - Iyz * q
        h = np.array([[h1],
                      [h2]])
        d = np.array([[d1],
                      [d2]])

        Kappay += np.squeeze(0.5 * Wts[i] * (Phi.T.dot(B.T) - nu / 2 * h.T).dot(B.dot(Phi) - nu / 2 * h) * abs(np.linalg.det(MtxJ)))
        Kappaz += np.squeeze(0.5 * Wts[i] * (Psi.T.dot(B.T) - nu / 2 * d.T).dot(B.dot(Psi) - nu / 2 * d) * abs(np.linalg.det(MtxJ)))
    return Kappay, Kappaz