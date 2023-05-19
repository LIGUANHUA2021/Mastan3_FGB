#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import scipy.linalg as spl
from numpy.linalg import solve

def CalEigenSubIter(K, M, num_vecs, num_iters=1000, tol=1e-6):
    Totalndof = len(K)
    X = np.zeros((Totalndof, num_vecs))
    X[:, 0] = 1.0
    X[1:num_vecs, 1:num_vecs] = np.eye(num_vecs - 1)

    Y = solve(K, M @ X)

    K_s = Y.T @ K @ Y
    M_s = Y.T @ M @ Y

    omega2, Z = spl.eigh(K_s, M_s)
    X = Y @ Z

    omega2_n = omega2[-1]

    for i in range(num_iters - 1):
        Y = solve(K, M @ X)

        K_s = Y.T @ K @ Y
        M_s = Y.T @ M @ Y

        omega2, Z = spl.eigh(K_s, M_s)
        X = Y @ Z

        error = abs(omega2_n - omega2[-1]) / omega2[-1]
        if error < tol:
            break
        omega2_n = omega2[-1]

    # omega = np.sqrt(omega2)
    omega = omega2
    # period = 2.0 * np.pi / omega
    phi = X
    return omega, phi