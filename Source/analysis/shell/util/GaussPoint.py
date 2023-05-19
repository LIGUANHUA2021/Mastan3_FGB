# External library
import numpy as np
# Internal library
from analysis.shell.variables import Model

# --------------------------------------------------------------
# Initialize the Gauss point location on the member
def GetGaussPointLocation(MemID, I, J):
    MemGaussPointLocation = np.zeros([len(MemID), 7, 4])
    for ii in MemID:
        tMID = MemID[ii]
        tI= I[ii]
        tJ =J[ii]
        MemGaussPointLocation[tMID] = GetGaussPointLocationOnSingleMem(tI, tJ)
    return MemGaussPointLocation

# Get the Gauss point location on single member
def GetGaussPointLocationOnSingleMem(I, J):
    # Dimentionless Gauss point location
    # GaussPointCoefficients = [0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]
    GaussPointCoefficients = [0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]
    GPL = np.zeros([7, 4]) # GPL: Gauss point location
    for ii in range(7):
        tNI = [Model.Node.X0[I], Model.Node.Y0[I], Model.Node.Z0[I]]
        tNJ = [Model.Node.X0[J], Model.Node.Y0[J], Model.Node.Z0[J]]
        for jj in range(3):
            GPL[ii][jj] = tNI[jj] + (tNJ[jj] - tNI[jj]) * GaussPointCoefficients[ii]
        GPL[ii][3] = 0 # Torsion
    return GPL

