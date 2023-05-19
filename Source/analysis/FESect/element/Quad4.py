import numpy as np


def GetMtxN(Eta, Xi):
    MtxN = np.array([[1 / 4 - Xi / 4 - Eta / 4 + (Xi * Eta) / 4,
                      1 / 4 + Xi / 4 - Eta / 4 - (Xi * Eta) / 4,
                      1 / 4 - Xi / 4 + Eta / 4 - (Xi * Eta) / 4,
                      1 / 4 + Xi / 4 + Eta / 4 + (Xi * Eta) / 4]])
    return MtxN


def GetMtxB(Eta, Xi, Y, Z):
    Y1 = Y[0]
    Y2 = Y[1]
    Y3 = Y[2]
    Y4 = Y[3]
    Z1 = Z[0]
    Z2 = Z[1]
    Z3 = Z[2]
    Z4 = Z[3]
    dEtady = (2 * (Z1 + Z2(-1 + Eta) - Z1 * Eta + (Z3 - Z4)(1 + Eta))) / \
             ((Y1 - Y4) * (Z2 - Z3) - Y4 * Z1 * Eta - Y1 * Z2 * Eta + Y4 * Z3 * Eta + Y1 * Z4 * Eta + Y4 * Z1 * Xi - Y4 * Z2 * Xi + Y1 * Z3 * Xi - Y1 * Z4 * Xi + Y3 * (Z1 - Z4 * (1 + Eta) - Z1 * Xi + Z2 * (Eta + Xi)) + Y2 * (Z4 + Z1 * (-1 + Eta) + Z4 * Xi - Z3 * (Eta + Xi)))
    dXidy = (2 * (Z3 + Z4 + Z1(-1 + Xi) - Z3 * Xi + Z4 * Xi - Z2 * (1 + Xi))) / \
            ((Y1 - Y4) * (Z2 - Z3) - Y4 * Z1 * Eta - Y1 * Z2 * Eta + Y4 * Z3 * Eta + Y1 * Z4 * Eta + Y4 * Z1 * Xi - Y4 * Z2 * Xi + Y1 * Z3 * Xi - Y1 * Z4 * Xi + Y3 * (Z1 - Z4 * (1 + Eta) - Z1 * Xi + Z2 * (Eta + Xi)) + Y2 * (Z4 + Z1 * (-1 + Eta) + Z4 * Xi - Z3 * (Eta + Xi)))
    dEtadz = (2 * (Y1 + Y2(-1 + Eta) - Y1 * Eta + (Y3 - Y4)(1 + Eta))) / \
             (-Y3 * Z1 - (Y1 - Y4) * (Z2 - Z3) + Y3 * Z4 + Y4 * Z1 * Eta + Y1 * Z2 * Eta - Y3 * Z2 * Eta - Y4 * Z3 * Eta - Y1 * Z4 * Eta + Y3 * Z4 * Eta + (Y3 - Y4) * (Z1 - Z2) * Xi + Y1 * (-Z3 + Z4) * Xi + Y2 * (Z1 - Z1 * Eta - Z4 * (1 + Xi) + Z3 * (Eta + Xi)))
    dXidz = (2 * (Y1 + Y2 - Y3 - Y4 + (-Y1 + Y2 + Y3 - Y4) * Xi)) / \
            ((Y1 - Y4) * (Z2 - Z3) - Y4 * Z1 * Eta - Y1 * Z2 * Eta + Y4 * Z3 * Eta + Y1 * Z4 * Eta + Y4 * Z1 * Xi - Y4 * Z2 * Xi + Y1 * Z3 * Xi - Y1 * Z4 * Xi + Y3 * (Z1 - Z4 * (1 + Eta) - Z1 * Xi + Z2 * (Eta + Xi)) + Y2 * (Z4 + Z1(-1 + Eta) + Z4 * Xi - Z3 * (Eta + Xi)))
    dN1dEta = (-1 + Xi) / 4
    dN1dXi = (-1 + Eta) / 4
    dN2dEta = (-1 - Xi) / 4
    dN2dXi = (1 - Eta) / 4
    dN3dEta = (1 - Xi) / 4
    dN3dXi = (-1 - Eta) / 4
    dN4dEta = (1 + Xi) / 4
    dN4dXi = (1 + Eta) / 4
    MtxB1 = np.array([[1, 0, 0, 0],
                      [0, 0, 0, 1],
                      [0, 1, 1, 0]])
    MtxB2 = np.array([[dXidz, dEtadz, 0, 0],
                      [dXidy, dEtady, 0, 0],
                      [0, 0, dXidz, dEtadz],
                      [0, 0, dXidy, dEtady]])
    MtxB3 = np.array([[dN1dXi, 0, dN2dXi, 0, dN3dXi, 0, dN4dXi, 0],
                      [dN1dEta, 0, dN2dEta, 0, dN3dEta, 0, dN4dEta, 0],
                      [0, dN1dXi, 0, dN2dXi, 0, dN3dXi, 0, dN4dXi],
                      [0, dN1dEta, 0, dN2dEta, 0, dN3dEta, 0, dN4dEta]])
    MtxB = MtxB1 * MtxB2 * MtxB3
    return MtxB


def GetMtxJ(Eta, Xi, Y, Z):
    Y1 = Y[0]
    Y2 = Y[1]
    Y3 = Y[2]
    Y4 = Y[3]
    Z1 = Z[0]
    Z2 = Z[1]
    Z3 = Z[2]
    Z4 = Z[3]
    MtxJ = np.array([[Z2 * (-1 / 4 - Xi / 4) + Z3 * (1 / 4 - Xi / 4) + Z1 * (-1 / 4 + Xi / 4) + Z4 * (1 / 4 + Xi / 4), Y2 * (-1 / 4 - Xi / 4) + Y3 * (1 / 4 - Xi / 4) + Y1 * (-1 / 4 + Xi / 4) + Y4 * (1 / 4 + Xi / 4)],
                     [Z3 * (-1 / 4 - Eta / 4) + Z2 * (1 / 4 - Eta / 4) + Z1 * (-1 / 4 + Eta / 4) + Z4 * (1 / 4 + Eta / 4), Y3 * (-1 / 4 - Eta / 4) + Y2 * (1 / 4 - Eta / 4) + Y1 * (-1 / 4 + Eta / 4) + Y4 * (1 / 4 + Eta / 4)]])
    return MtxJ