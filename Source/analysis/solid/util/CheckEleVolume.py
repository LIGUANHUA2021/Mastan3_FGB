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

# ===========================================================================
# Import internal functions
from analysis.solid.variables import Model
from analysis.solid.element import FourNodeTetrahedron
# ===========================================================================
def CheckEleVol():
    for ii in Model.Element.ID:
        tI = Model.Element.I[ii]
        tJ = Model.Element.J[ii]
        tK = Model.Element.K[ii]
        tN = Model.Element.N[ii]
        X1 = Model.Node.X0[tI]
        Y1 = Model.Node.Y0[tI]
        Z1 = Model.Node.Z0[tI]
        X2 = Model.Node.X0[tJ]
        Y2 = Model.Node.Y0[tJ]
        Z2 = Model.Node.Z0[tJ]
        X3 = Model.Node.X0[tK]
        Y3 = Model.Node.Y0[tK]
        Z3 = Model.Node.Z0[tK]
        X4 = Model.Node.X0[tN]
        Y4 = Model.Node.Y0[tN]
        Z4 = Model.Node.Z0[tN]
        Model.Element.V0[ii] = FourNodeTetrahedron.GetEleVol(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, X4, Y4, Z4)
        print(f"Volume {ii} = ", Model.Element.V0[ii])
    #
    return
