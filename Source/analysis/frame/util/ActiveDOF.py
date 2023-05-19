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

def ActiveWarpingDOF(status, data):
    if status == True:
        return data
    else:
        if len(data.shape) == 2:
            return ActiveWarpingDOFinMatrix(data)
        else:
            return ActiveWarpingDOFinVector(data)

def ActiveWarpingDOFinMatrix(Matrix):
    for ii in range(int(len(Matrix) / 7)):
        Matrix[ii * 7 + 6, :] = Matrix[:, ii * 7 + 6] = 0
        Matrix[ii * 7 + 6, ii * 7 + 6] = 1
    return Matrix

def ActiveWarpingDOFinVector(Vector):
    for ii in range(int(len(Vector) / 7)):
        Vector[ii * 7 + 6] = 0
    return Vector

