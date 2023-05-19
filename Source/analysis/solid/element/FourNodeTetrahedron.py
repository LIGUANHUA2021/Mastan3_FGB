#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
import numpy as np

def GetEleVol(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    xyz = np.array([[1, x1, y1, z1],
                    [1, x2, y2, z2],
                    [1, x3, y3, z3],
                    [1, x4, y4, z4]])
    volume = np.linalg.det(xyz) / 6.0
    return volume

def GetElekl(E, NU, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    xyz = np.array([[1, x1, y1, z1],
                    [1, x2, y2, z2],
                    [1, x3, y3, z3],
                    [1, x4, y4, z4]])

    V = np.linalg.det(xyz) / 6

    mbeta1 = np.array([[1, y2, z2],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta2 = np.array([[1, y1, z1],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta3 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y4, z4]])
    mbeta4 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y3, z3]])

    mgamma1 = np.array([[1, x2, z2],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma2 = np.array([[1, x1, z1],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma3 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x4, z4]])
    mgamma4 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x3, z3]])

    mdelta1 = np.array([[1, x2, y2],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta2 = np.array([[1, x1, y1],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta3 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x4, y4]])
    mdelta4 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x3, y3]])

    beta1 = -1 * np.linalg.det(mbeta1)
    beta2 = np.linalg.det(mbeta2)
    beta3 = -1 * np.linalg.det(mbeta3)
    beta4 = np.linalg.det(mbeta4)

    gamma1 = np.linalg.det(mgamma1)
    gamma2 = -1 * np.linalg.det(mgamma2)
    gamma3 = np.linalg.det(mgamma3)
    gamma4 = -1 * np.linalg.det(mgamma4)

    delta1 = -1 * np.linalg.det(mdelta1)
    delta2 = np.linalg.det(mdelta2)
    delta3 = -1 * np.linalg.det(mdelta3)
    delta4 = np.linalg.det(mdelta4)

    B = np.zeros((6, 12))
    for i, (beta, gamma, delta) in enumerate(
           [(beta1, gamma1, delta1), (beta2, gamma2, delta2), (beta3, gamma3, delta3), (beta4, gamma4, delta4)]):
        B[0:6, i * 3 : (i + 1) * 3] = np.array([[beta, 0, 0], [0, gamma, 0], [0, 0, delta],
                                                [gamma, beta, 0], [0, delta, gamma], [delta, 0, beta]])

    B /= (6 * V)

    D = (E / ((1 + NU) * (1 - 2 * NU))) * np.array([[1 - NU, NU, NU, 0, 0, 0],
    [NU, 1 - NU, NU, 0, 0, 0],
    [NU, NU, 1 - NU, 0, 0, 0],
    [0, 0, 0, (1 - 2 * NU) / 2, 0, 0],
    [0, 0, 0, 0, (1 - 2 * NU) / 2, 0],
    [0, 0, 0, 0, 0, (1 - 2 * NU) / 2]
    ])

    return V * B.T @ D @ B

def GetEleKLG(K, k, i, j, m, n):

    I = np.array([3 * i - 3, 3 * i - 2, 3 * i - 1])
    J = np.array([3 * j - 3, 3 * j - 2, 3 * j - 1])
    M = np.array([3 * m - 3, 3 * m - 2, 3 * m - 1])
    N = np.array([3 * n - 3, 3 * n - 2, 3 * n - 1])
    a = np.append(np.append(np.append(I, J), M), N)
    for p in range(0, 12):
        K[a[p], I[0]] += k[p, 0]
        K[a[p], I[1]] += k[p, 1]
        K[a[p], I[2]] += k[p, 2]
        K[a[p], J[0]] += k[p, 3]
        K[a[p], J[1]] += k[p, 4]
        K[a[p], J[2]] += k[p, 5]
        K[a[p], M[0]] += k[p, 6]
        K[a[p], M[1]] += k[p, 7]
        K[a[p], M[2]] += k[p, 8]
        K[a[p], N[0]] += k[p, 9]
        K[a[p], N[1]] += k[p, 10]
        K[a[p], N[2]] += k[p, 11]

    return K

#Get Mass Matrix, 12x12 - Consistent
def GetEleMM(rho, Ve):
    ## rho -> Density of Material
    MC = rho * Ve / 20
    tMtx = np.zeros((12, 12))
    # Non-diagonal
    tMtx[0, 3] = 1.0 * MC
    tMtx[0, 6] = 1.0 * MC
    tMtx[0, 9] = 1.0 * MC
    #
    tMtx[1, 4] = 1.0 * MC
    tMtx[1, 7] = 1.0 * MC
    tMtx[1, 10] = 1.0 * MC
    #
    tMtx[2, 5] = 1.0 * MC
    tMtx[2, 8] = 1.0 * MC
    tMtx[2, 11] = 1.0 * MC
    #
    tMtx[3, 6] = 1.0 * MC
    tMtx[3, 9] = 1.0 * MC
    #
    tMtx[4, 7] = 1.0 * MC
    tMtx[4, 10] = 1.0 * MC
    #
    tMtx[5, 8] = 1.0 * MC
    tMtx[5, 11] = 1.0 * MC
    #
    tMtx[6, 9] = 1.0 * MC
    #
    tMtx[7, 10] = 1.0 * MC
    #
    tMtx[8, 11] = 1.0 * MC
    tMtx += tMtx.transpose()
    ## Diagonal
    tMtx[0, 0] = 2.0 * MC
    tMtx[1, 1] = 2.0 * MC
    tMtx[2, 2] = 2.0 * MC
    tMtx[3, 3] = 2.0 * MC
    tMtx[4, 4] = 2.0 * MC
    tMtx[5, 5] = 2.0 * MC
    tMtx[6, 6] = 2.0 * MC
    tMtx[7, 7] = 2.0 * MC
    tMtx[8, 8] = 2.0 * MC
    tMtx[9, 9] = 2.0 * MC
    tMtx[10, 10] = 2.0 * MC
    tMtx[11, 11] = 2.0 * MC
    return tMtx


def GetElekgeo(E, NU, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, DELU):
    xyz = np.array([[1, x1, y1, z1],
                    [1, x2, y2, z2],
                    [1, x3, y3, z3],
                    [1, x4, y4, z4]])

    V = np.linalg.det(xyz) / 6

    mbeta1 = np.array([[1, y2, z2],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta2 = np.array([[1, y1, z1],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta3 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y4, z4]])
    mbeta4 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y3, z3]])

    mgamma1 = np.array([[1, x2, z2],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma2 = np.array([[1, x1, z1],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma3 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x4, z4]])
    mgamma4 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x3, z3]])

    mdelta1 = np.array([[1, x2, y2],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta2 = np.array([[1, x1, y1],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta3 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x4, y4]])
    mdelta4 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x3, y3]])

    beta1 = -1 * np.linalg.det(mbeta1)
    beta2 = np.linalg.det(mbeta2)
    beta3 = -1 * np.linalg.det(mbeta3)
    beta4 = np.linalg.det(mbeta4)

    gamma1 = np.linalg.det(mgamma1)
    gamma2 = -1 * np.linalg.det(mgamma2)
    gamma3 = np.linalg.det(mgamma3)
    gamma4 = -1 * np.linalg.det(mgamma4)

    delta1 = -1 * np.linalg.det(mdelta1)
    delta2 = np.linalg.det(mdelta2)
    delta3 = -1 * np.linalg.det(mdelta3)
    delta4 = np.linalg.det(mdelta4)
    ##
    tB = np.zeros((6, 12))
    ##
    # tB[0, 0] = tB[0, 1] = tB[0, 2] = 0.5 * beta1 * beta1
    # tB[0, 3] = tB[0, 4] = tB[0, 5] = 0.5 * beta1 * beta2
    # tB[0, 6] = tB[0, 7] = tB[0, 8] = 0.5 * beta1 * beta3
    # tB[0, 9] = tB[0, 10] = tB[0, 11] = 0.5 * beta1 * beta4
    # ##
    # tB[1, 0] = tB[1, 1] = tB[1, 2] = 0.5 * gamma1 * gamma1
    # tB[1, 3] = tB[1, 4] = tB[1, 5] = 0.5 * gamma1 * gamma2
    # tB[1, 6] = tB[1, 7] = tB[1, 8] = 0.5 * gamma1 * gamma3
    # tB[1, 9] = tB[1, 10] = tB[1, 11] = 0.5 * gamma1 * gamma4
    # ##
    # tB[2, 0] = tB[2, 1] = tB[2, 2] = 0.5 * delta1 * delta1
    # tB[2, 3] = tB[2, 4] = tB[2, 5] = 0.5 * delta1 * delta2
    # tB[2, 6] = tB[2, 7] = tB[2, 8] = 0.5 * delta1 * delta3
    # tB[2, 9] = tB[2, 10] = tB[2, 11] = 0.5 * delta1 * delta4
    # ##
    # tB[3, 0] = tB[3, 1] = tB[3, 2] = 2 * beta1 * gamma1
    # tB[3, 3] = tB[3, 4] = tB[3, 5] = beta2 * gamma1 + beta1 * gamma2
    # tB[3, 6] = tB[3, 7] = tB[3, 8] = beta3 * gamma1 + beta1 * gamma3
    # tB[3, 9] = tB[3, 10] = tB[3, 11] = beta4 * gamma1 + beta1 * gamma4
    # ##
    # tB[4, 0] = tB[4, 1] = tB[4, 2] = 2 * beta1 * delta1
    # tB[4, 3] = tB[4, 4] = tB[4, 5] = beta2 * delta1 + beta1 * delta2
    # tB[4, 6] = tB[4, 7] = tB[4, 8] = beta3 * delta1 + beta1 * delta3
    # tB[4, 9] = tB[4, 10] = tB[4, 11] = beta4 * delta1 + beta1 * delta4
    # ##
    # tB[5, 0] = tB[5, 1] = tB[5, 2] = 2 * gamma1 * delta1
    # tB[5, 3] = tB[5, 4] = tB[5, 5] = gamma2 * delta1 + gamma1 * delta2
    # tB[5, 6] = tB[5, 7] = tB[5, 8] = gamma3 * delta1 + gamma1 * delta3
    # tB[5, 9] = tB[5, 10] = tB[5, 11] = gamma4 * delta1 + gamma1 * delta4
    ##
    # for i, (beta, gamma, delta) in enumerate(
    #        [(beta1, gamma1, delta1), (beta2, gamma2, delta2), (beta3, gamma3, delta3), (beta4, gamma4, delta4)]):
    #     tB[0:6, i * 3 : (i + 1) * 3] = np.array([[0.5*beta*beta, 0.5*beta*beta, 0.5*beta*beta], [0.5*gamma*gamma, 0.5*gamma*gamma, 0.5*gamma*gamma], [0.5*delta*delta, 0.5*delta*delta, 0.5*delta*delta],
    #                                             [2*gamma*beta, 2*gamma*beta, 2*gamma*beta], [2*delta*gamma, 2*delta*gamma, 2*delta*gamma], [2*beta*delta, 2*beta*delta, 2*beta*delta]])
    u1 = DELU[0]
    v1 = DELU[1]
    w1 = DELU[2]
    u2 = DELU[3]
    v2 = DELU[4]
    w2 = DELU[5]
    u3 = DELU[6]
    v3 = DELU[7]
    w3 = DELU[8]
    u4 = DELU[9]
    v4 = DELU[10]
    w4 = DELU[11]
    ##
    uxx = beta1 * u1 + beta2 * u2 + beta3 * u3 + beta4 * u4
    uyx = beta1 * v1 + beta2 * v2 + beta3 * v3 + beta4 * v4
    uzx = beta1 * w1 + beta2 * w2 + beta3 * w3 + beta4 * w4
    #
    uxy = gamma1 * u1 + gamma2 * u2 + gamma3 * u3 + gamma4 * u4
    uyy = gamma1 * v1 + gamma2 * v2 + gamma3 * v3 + gamma4 * v4
    uzy = gamma1 * w1 + gamma2 * w2 + gamma3 * w3 + gamma4 * w4
    #
    uxz = delta1 * u1 + delta2 * u2 + delta3 * u3 + delta4 * u4
    uyz = delta1 * v1 + delta2 * v2 + delta3 * v3 + delta4 * v4
    uzz = delta1 * w1 + delta2 * w2 + delta3 * w3 + delta4 * w4
    #
    # for i, (beta, gamma, delta) in enumerate(
    #        [(beta1, gamma1, delta1), (beta2, gamma2, delta2), (beta3, gamma3, delta3), (beta4, gamma4, delta4)]):
    #     tB[0:6, i * 3 : (i + 1) * 3] = np.array([[beta+beta*uxx, beta*uyx, beta*uzx], [gamma*uxy, gamma+gamma*uyy, gamma*uzy], [delta*uxz, delta*uyz, delta+delta*uzz],
    #                                             [gamma+gamma*uxx+beta*uxy, gamma*uyx+beta+beta*uyy, gamma*uzx+beta*uzy],
    #                                              [delta+delta*uxx+beta*uxz, delta*uyx+beta*uyz, delta*uzx+beta+beta*uzz],
    #                                              [gamma*uxz+delta*uxy, delta+delta*uyz+delta*uyy, gamma*uzz+delta+delta*uzy]])
    for i, (beta, gamma, delta) in enumerate(
           [(beta1, gamma1, delta1), (beta2, gamma2, delta2), (beta3, gamma3, delta3), (beta4, gamma4, delta4)]):
        tB[0:6, i * 3 : (i + 1) * 3] = np.array([[beta+beta*uxx, beta*uyx, beta*uzx], [gamma*uxy, gamma+gamma*uyy, gamma*uzy], [delta*uxz, delta*uyz, delta+delta*uzz],
                                                [gamma+gamma*uxx+beta*uxy, gamma*uyx+beta+beta*uyy, gamma*uzx+beta*uzy],
                                                 [gamma*uxz+delta*uxy, delta+gamma*uyz+delta*uyy, gamma+gamma*uzz+delta*uzy],
                                                 [delta+delta*uxx+beta*uxz, delta*uyx+beta*uyz, beta+delta*uzx+beta*uzz]])
    tB /= (6 * V)
    ##
    tBb = np.zeros((6, 12))
    for i, (beta, gamma, delta) in enumerate(
           [(beta1, gamma1, delta1), (beta2, gamma2, delta2), (beta3, gamma3, delta3), (beta4, gamma4, delta4)]):
        tBb[0:6, i * 3 : (i + 1) * 3] = np.array([[beta+0.5*beta*uxx, 0.5*beta*uyx, 0.5*beta*uzx], [0.5*gamma*uxy, gamma+0.5*gamma*uyy, 0.5*gamma*uzy], [0.5*delta*uxz, 0.5*delta*uyz, delta+0.5*delta*uzz],
                                                [gamma+0.5*gamma*uxx+0.5*beta*uxy, 0.5*gamma*uyx+beta+0.5*beta*uyy, 0.5*gamma*uzx+0.5*beta*uzy],
                                                 [0.5*gamma*uxz+0.5*delta*uxy, delta+0.5*gamma*uyz+0.5*delta*uyy, gamma+0.5*gamma*uzz+0.5*delta*uzy],
                                                 [delta+0.5*delta*uxx+0.5*beta*uxz, 0.5*delta*uyx+0.5*beta*uyz, beta+0.5*delta*uzx+0.5*beta*uzz]])

    # tBb = tB * 0.5
    tBb /= (6 * V)
    ##
    D = (E / ((1 + NU) * (1 - 2 * NU))) * np.array([[1 - NU, NU, NU, 0, 0, 0],
    [NU, 1 - NU, NU, 0, 0, 0],
    [NU, NU, 1 - NU, 0, 0, 0],
    [0, 0, 0, (1 - 2 * NU) / 2, 0, 0],
    [0, 0, 0, 0, (1 - 2 * NU) / 2, 0],
    [0, 0, 0, 0, 0, (1 - 2 * NU) / 2]
    ])
    ##
    return V * tBb.T @ D @ tB

def GetElekgeoT(E, NU, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    xyz = np.array([[1, x1, y1, z1],
                    [1, x2, y2, z2],
                    [1, x3, y3, z3],
                    [1, x4, y4, z4]])

    V = np.linalg.det(xyz) / 6

    mbeta1 = np.array([[1, y2, z2],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta2 = np.array([[1, y1, z1],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta3 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y4, z4]])
    mbeta4 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y3, z3]])

    mgamma1 = np.array([[1, x2, z2],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma2 = np.array([[1, x1, z1],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma3 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x4, z4]])
    mgamma4 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x3, z3]])

    mdelta1 = np.array([[1, x2, y2],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta2 = np.array([[1, x1, y1],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta3 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x4, y4]])
    mdelta4 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x3, y3]])

    beta1 = -1 * np.linalg.det(mbeta1)
    beta2 = np.linalg.det(mbeta2)
    beta3 = -1 * np.linalg.det(mbeta3)
    beta4 = np.linalg.det(mbeta4)

    gamma1 = np.linalg.det(mgamma1)
    gamma2 = -1 * np.linalg.det(mgamma2)
    gamma3 = np.linalg.det(mgamma3)
    gamma4 = -1 * np.linalg.det(mgamma4)

    delta1 = -1 * np.linalg.det(mdelta1)
    delta2 = np.linalg.det(mdelta2)
    delta3 = -1 * np.linalg.det(mdelta3)
    delta4 = np.linalg.det(mdelta4)
    ##
    tB = np.zeros((6, 12))
    ##
    tB[0, 0] = 0.5 * beta1 * beta1 + 6 * V * beta1
    tB[0, 1] = tB[0, 2] = 0.5 * beta1 * beta1
    tB[0, 3] = 0.5 * beta1 * beta2 + 6 * V * beta2
    tB[0, 4] = tB[0, 5] = 0.5 * beta1 * beta2
    tB[0, 6] = 0.5 * beta1 * beta3 + 6 * V * beta3
    tB[0, 7] = tB[0, 8] = 0.5 * beta1 * beta3
    tB[0, 9] = 0.5 * beta1 * beta4 + 6 * V * beta4
    tB[0, 10] = tB[0, 11] = 0.5 * beta1 * beta4
    ##
    tB[1, 0] = tB[1, 2] = 0.5 * gamma1 * gamma1
    tB[1, 1] = 0.5 * gamma1 * gamma1 + 6 * V * gamma1
    tB[1, 3] = tB[1, 5] = 0.5 * gamma1 * gamma2
    tB[1, 4] = 0.5 * gamma1 * gamma2 + 6 * V * gamma2
    tB[1, 6] = tB[1, 8] = 0.5 * gamma1 * gamma3
    tB[1, 7] = 0.5 * gamma1 * gamma3 + 6 * V * gamma3
    tB[1, 9] = tB[1, 11] = 0.5 * gamma1 * gamma4
    tB[1, 10] = 0.5 * gamma1 * gamma4 + 6 * V * gamma4
    ##
    tB[2, 0] = tB[2, 1] = 0.5 * delta1 * delta1
    tB[2, 2] = 0.5 * delta1 * delta1 + 6 * V * delta1
    tB[2, 3] = tB[2, 4] = 0.5 * delta1 * delta2
    tB[2, 5] = 0.5 * delta1 * delta2 + 6 * V * delta2
    tB[2, 6] = tB[2, 7] = 0.5 * delta1 * delta3
    tB[2, 8] = 0.5 * delta1 * delta3 + 6 * V * delta3
    tB[2, 9] = tB[2, 10] = 0.5 * delta1 * delta4
    tB[2, 11] = 0.5 * delta1 * delta4 + 6 * V * delta4
    ##
    tB[3, 0] = 2*(3*V+beta1)*gamma1
    tB[3, 1] = 2*beta1*(3*V+gamma1)
    tB[3, 2] = 2 * beta1 * gamma1
    tB[3, 3] = beta2*gamma1+(6*V+beta1)*gamma2
    tB[3, 4] = 6*V*beta2+beta2*gamma1+beta1*gamma2
    tB[3, 5] = beta2 * gamma1 + beta1 * gamma2
    tB[3, 6] = beta3*gamma1+(6*V+beta1)*gamma3
    tB[3, 7] = 6*V*beta3+beta3*gamma1+beta1*gamma3
    tB[3, 8] = beta3 * gamma1 + beta1 * gamma3
    tB[3, 9] = beta4*gamma1+(6*V+beta1)*gamma4
    tB[3, 10] = 6*V*beta4+beta4*gamma1+beta1*gamma4
    tB[3, 11] = beta4 * gamma1 + beta1 * gamma4
    # tB[3, 0] = tB[3, 1] = tB[3, 2] = 2 * beta1 * gamma1
    # tB[3, 3] = tB[3, 4] = tB[3, 5] = beta2 * gamma1 + beta1 * gamma2
    # tB[3, 6] = tB[3, 7] = tB[3, 8] = beta3 * gamma1 + beta1 * gamma3
    # tB[3, 9] = tB[3, 10] = tB[3, 11] = beta4 * gamma1 + beta1 * gamma4
    ##
    tB[4, 0] = 2*(3*V+beta1)*delta1
    tB[4, 1] = 2 * beta1 * delta1
    tB[4, 2] = 2*beta1*(3*V+delta1)
    tB[4, 3] = beta2*delta1+(6*V+beta1)*delta2
    tB[4, 4] = beta2 * delta1 + beta1 * delta2
    tB[4, 5] = 6*V*beta2+beta2*delta1+beta1*delta2
    tB[4, 6] = beta3*delta1+(6*V+beta1)*delta3
    tB[4, 7] = beta3 * delta1 + beta1 * delta3
    tB[4, 8] = 6*V*beta3+beta3*delta1+beta1*delta3
    tB[4, 9] = beta4*delta1+(6*V+beta1)*delta4
    tB[4, 10] = beta4 * delta1 + beta1 * delta4
    tB[4, 11] = 6*V*beta4+beta4*delta1+beta1*delta4

    # tB[4, 0] = tB[4, 1] = tB[4, 2] = 2 * beta1 * delta1
    # tB[4, 3] = tB[4, 4] = tB[4, 5] = beta2 * delta1 + beta1 * delta2
    # tB[4, 6] = tB[4, 7] = tB[4, 8] = beta3 * delta1 + beta1 * delta3
    # tB[4, 9] = tB[4, 10] = tB[4, 11] = beta4 * delta1 + beta1 * delta4
    ##
    tB[5, 0] = 2 * gamma1 * delta1
    tB[5, 1] = 2*(3*V+gamma1)*delta1
    tB[5, 2] = 2*gamma1*(3*V+delta1)
    tB[5, 3] = gamma2 * delta1 + gamma1 * delta2
    tB[5, 4] = gamma2*delta1+(6*V+gamma1)*delta2
    tB[5, 5] = 6*V*gamma2+gamma2*delta1+gamma1*delta2
    tB[5, 6] = gamma3 * delta1 + gamma1 * delta3
    tB[5, 7] = gamma3*delta1+(6*V+gamma1)*delta3
    tB[5, 8] = 6*V*gamma3+gamma3*delta1+gamma1*delta3
    tB[5, 9] = gamma4 * delta1 + gamma1 * delta4
    tB[5, 10] = gamma4*delta1+(6*V+gamma1)*delta4
    tB[5, 11] = 6*V*gamma4+gamma4*delta1+gamma1*delta4

    # tB[5, 0] = tB[5, 1] = tB[5, 2] = 2 * gamma1 * delta1
    # tB[5, 3] = tB[5, 4] = tB[5, 5] = gamma2 * delta1 + gamma1 * delta2
    # tB[5, 6] = tB[5, 7] = tB[5, 8] = gamma3 * delta1 + gamma1 * delta3
    # tB[5, 9] = tB[5, 10] = tB[5, 11] = gamma4 * delta1 + gamma1 * delta4
    tB /= (6 * V)


def GetEleStrs(E, NU, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, u):
    xyz = np.array([[1, x1, y1, z1],
                    [1, x2, y2, z2],
                    [1, x3, y3, z3],
                    [1, x4, y4, z4]])
    V = np.linalg.det(xyz) / 6

    mbeta1 = np.array([[1, y2, z2],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta2 = np.array([[1, y1, z1],
                       [1, y3, z3],
                       [1, y4, z4]])
    mbeta3 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y4, z4]])
    mbeta4 = np.array([[1, y1, z1],
                       [1, y2, z2],
                       [1, y3, z3]])
    mgamma1 = np.array([[1, x2, z2],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma2 = np.array([[1, x1, z1],
                        [1, x3, z3],
                        [1, x4, z4]])
    mgamma3 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x4, z4]])
    mgamma4 = np.array([[1, x1, z1],
                        [1, x2, z2],
                        [1, x3, z3]])
    mdelta1 = np.array([[1, x2, y2],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta2 = np.array([[1, x1, y1],
                        [1, x3, y3],
                        [1, x4, y4]])
    mdelta3 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x4, y4]])
    mdelta4 = np.array([[1, x1, y1],
                        [1, x2, y2],
                        [1, x3, y3]])

    beta1 = -1 * np.linalg.det(mbeta1)
    beta2 = np.linalg.det(mbeta2)
    beta3 = -1 * np.linalg.det(mbeta3)
    beta4 = np.linalg.det(mbeta4)
    gamma1 = np.linalg.det(mgamma1)
    gamma2 = -1 * np.linalg.det(mgamma2)
    gamma3 = np.linalg.det(mgamma3)
    gamma4 = -1 * np.linalg.det(mgamma4)
    delta1 = -1 * np.linalg.det(mdelta1)
    delta2 = np.linalg.det(mdelta2)
    delta3 = -1 * np.linalg.det(mdelta3)
    delta4 = np.linalg.det(mdelta4)

    B1 = np.array([[beta1, 0, 0], [0, gamma1, 0], [0, 0, delta1],
                    [gamma1, beta1, 0], [0, delta1, gamma1], [delta1, 0, beta1]])
    B2 = np.array([[beta2, 0, 0], [0, gamma2, 0], [0, 0, delta2],
                    [gamma2, beta2, 0], [0, delta2, gamma2], [delta2, 0, beta2]])
    B3 = np.array([[beta3, 0, 0], [0, gamma3, 0], [0, 0, delta3],
                    [gamma3, beta3, 0], [0, delta3, gamma3], [delta3, 0, beta3]])
    B4 = np.array([[beta4, 0, 0], [0, gamma4, 0], [0, 0, delta4],
                    [gamma4, beta4, 0], [0, delta4, gamma4], [delta4, 0, beta4]])
    B = np.hstack((B1, B2, B3, B4)) / (6 * V)
    D = (E / ((1 + NU) * (1 - 2 * NU))) * np.array([[1 - NU, NU, NU, 0, 0, 0],
                                                    [NU, 1 - NU, NU, 0, 0, 0],
                                                    [NU, NU, 1 - NU, 0, 0, 0],
                                                    [0, 0, 0, (1 - 2 * NU) / 2, 0, 0],
                                                    [0, 0, 0, 0, (1 - 2 * NU) / 2, 0],
                                                    [0, 0, 0, 0, 0, (1 - 2 * NU) / 2]])

    y = np.dot(D, np.dot(B, u))
    return y

def GetElePStrs(sigma):
    """
    TetrahedronElementPStresses This function returns the three
    principal stresses for the element
    given the element stress vector.
    The principal angles are not returned.
    """
    s1 = sigma[0] + sigma[1] + sigma[2]
    s2 = sigma[0] * sigma[1] + sigma[0] * sigma[2] + sigma[1] * sigma[2] - sigma[3] * sigma[3] - sigma[4] * sigma[4] - sigma[5] * sigma[5]
    ms3 = np.array([[sigma[0], sigma[3], sigma[5]],
                    [sigma[3], sigma[1], sigma[4]],
                    [sigma[5], sigma[4], sigma[2]]])
    s3 = np.linalg.det(ms3)
    y = np.array([s1, s2, s3])
    return y


