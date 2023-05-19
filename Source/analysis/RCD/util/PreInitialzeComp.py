#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math
from itertools import zip_longest  # For establishing dictionary
# ===========================================================================
from analysis.RCD.variables import Model

def IniComSteel(tComID):
    # Importing Variables and SystemVariables modules
    # Acy and Acz initial values
    tAS = 0.0
    Acy = 0.0
    Acz = 0.0
    ComIn = Model.Component
    tFibers = np.array(ComIn.CompFibersInfo[tComID]["Fibers"])
    # Check if the number of fibers is not zero
    if len(tFibers) == 0:
        return
    #
    # # Loop over the fibers of the component
    for ii in np.arange(len(tFibers)):
        # Add the area of the fiber to the total area
        tAS += tFibers[ii, 3]  # Fiber Area = tFibers[ii, 3]
        # Add the area-weighted fiber y coordinate to the total y coordinate
        Acy += tFibers[ii, 3] * tFibers[ii, 1]  # Fiber y coordinate = tFibers[ii, 1]
        # Add the area-weighted fiber z coordinate to the total z coordinate
        Acz += tFibers[ii, 3] * tFibers[ii, 2]  # Fiber z coordinate = tFibers[ii, 2]
    #
    tSecMinY = 9999.0
    tSecMaxY = -9999.0
    tSecMinZ = 9999.0
    tSecMaxZ = -9999.0
    # Check if the fiber coordinates are within the sectional boundaries
    if np.min(tFibers[:, 1]) <= tSecMinY:
        tSecMinY = np.min(tFibers[:, 1])
    if np.max(tFibers[:, 1]) >= tSecMaxY:
        tSecMaxY = np.max(tFibers[:, 1])
    if np.min(tFibers[:, 2]) <= tSecMinZ:
        tSecMinZ = np.min(tFibers[:, 2])
    if np.max(tFibers[:, 2]) >= tSecMaxZ:
        tSecMaxZ = np.max(tFibers[:, 2])

    ## Store the max. and min. coordinate of fibers by Component
    ComIn.MinY[tComID] = tSecMinY
    ComIn.MaxY[tComID] = tSecMaxY
    ComIn.MinZ[tComID] = tSecMinZ
    ComIn.MaxZ[tComID] = tSecMaxZ
    #
    # Calculate the centroid coordinates of the component
    ComIn.Area[tComID] = tAS
    if ComIn.Area[tComID] != 0:
        ComIn.cy[tComID] = Acy / ComIn.Area[tComID]
        ComIn.cz[tComID] = Acz / ComIn.Area[tComID]
    else:
        ComIn.cy[tComID] = 0
        ComIn.cz[tComID] = 0

    return
def IniComRebar(tComID):
    ##
    ComIn = Model.Component
    tFibers = np.array(ComIn.CompFibersInfo[tComID]["Fibers"])
    ##
    if len(tFibers) == 0:
        return
    tAR = 0.0
    Acy = 0.0
    Acz = 0.0

    # Loop over all fibers in the composite object
    for ii in np.arange(len(tFibers)):
        # Calculate the total area of the composite object
        tAR += tFibers[ii, 3]  # Fiber Area =tFibers[ii, 3]
        # Calculate the weighted average of Y and Z coordinates of the fibers
        Acy += tFibers[ii, 3] * tFibers[ii, 1]  # Fiber y coordinate = tFibers[ii, 1]
        Acz += tFibers[ii, 3] * tFibers[ii, 2]  # Fiber z coordinate = tFibers[ii, 2]

    tSecMinY = 9999.0
    tSecMaxY = -9999.0
    tSecMinZ = 9999.0
    tSecMaxZ = -9999.0
    # Update the minimum and maximum Y and Z coordinates of the composite object
    SecMinY = min(tSecMinY, np.min(tFibers[:, 1]))
    SecMaxY = max(tSecMaxY, np.max(tFibers[:, 1]))
    SecMinZ = min(tSecMinZ, np.min(tFibers[:, 2]))
    SecMaxZ = max(tSecMaxZ, np.max(tFibers[:, 2]))
    ## Store the max. and min. coordinate of fibers by Component
    ComIn.MinY[tComID] = SecMinY
    ComIn.MaxY[tComID] = SecMaxY
    ComIn.MinZ[tComID] = SecMinZ
    ComIn.MaxZ[tComID] = SecMaxZ

    # Calculate the centroid of the composite object based on the centroid of the fibers
    ComIn.Area[tComID] = tAR
    if ComIn.Area[tComID] != 0:
        ComIn.cy[tComID] = Acy / ComIn.Area[tComID]
        ComIn.cz[tComID] = Acz / ComIn.Area[tComID]
    else:
        ComIn.cy[tComID] = 0
        ComIn.cz[tComID] = 0

    return

def IniComConcrete(tComID):
    ComIn = Model.Component
    tFibers = np.array(ComIn.CompFibersInfo[tComID]["Fibers"])
    ##
    if len(tFibers) == 0:
        return
    tAC = 0.0
    Acy = 0.0
    Acz = 0.0

    # Loop over all fibers in the composite object
    for ii in np.arange(len(tFibers)):
        # Calculate the total area of the composite object
        tAC += tFibers[ii, 3]  # Fiber Area =tFibers[ii, 3]
        # Calculate the weighted average of Y and Z coordinates of the fibers
        Acy += tFibers[ii, 3] * tFibers[ii, 1]  # Fiber y coordinate = tFibers[ii, 1]
        Acz += tFibers[ii, 3] * tFibers[ii, 2]  # Fiber z coordinate = tFibers[ii, 2]

    tSecMinY = 9999.0
    tSecMaxY = -9999.0
    tSecMinZ = 9999.0
    tSecMaxZ = -9999.0
    # Update the minimum and maximum Y and Z coordinates of the composite object
    SecMinY = min(tSecMinY, np.min(tFibers[:, 1]))
    SecMaxY = max(tSecMaxY, np.max(tFibers[:, 1]))
    SecMinZ = min(tSecMinZ, np.min(tFibers[:, 2]))
    SecMaxZ = max(tSecMaxZ, np.max(tFibers[:, 2]))
    ## Store the max. and min. coordinate of fibers by Component
    ComIn.MinY[tComID] = SecMinY
    ComIn.MaxY[tComID] = SecMaxY
    ComIn.MinZ[tComID] = SecMinZ
    ComIn.MaxZ[tComID] = SecMaxZ

    # Calculate the centroid of the composite object based on the centroid of the fibers
    ComIn.Area[tComID] = tAC
    if ComIn.Area[tComID] != 0:
        ComIn.cy[tComID] = Acy / ComIn.Area[tComID]
        ComIn.cz[tComID] = Acz / ComIn.Area[tComID]
    else:
        ComIn.cy[tComID] = 0
        ComIn.cz[tComID] = 0
    return

def PreIniComponet(tAnalF=1):
    NumConcrete = 0
    NumSteel = 0
    NumRebar = 0
    if tAnalF == 1:
        print("INITIALIZING COMPONENTS ...")
    ComIn = Model.Component
    for ii in ComIn.ID:

        # Initialize Area, cy, cz
        ComIn.Area[ii] = 0
        ComIn.cy[ii] = 0
        ComIn.cz[ii] = 0

        if ComIn.ComType[ii] == 1:
            tempout = 'Steel'
            NumSteel += 1
            IniComSteel(ii)

        elif ComIn.ComType[ii] == 2:
            tempout = 'Concrete'
            NumConcrete += 1
            IniComConcrete(ii)

        elif ComIn.ComType[ii] == 3:
            tempout = 'Rebar'
            NumRebar += 1
            IniComRebar(ii)
        if tAnalF == 1:
            print(f"    Com. ID = {ComIn.ID[ii]:5d} ; Type = {tempout:10s} ; Name = {ComIn.Name[ii]:20s}")
            print(f"    Area = {ComIn.Area[ii]:8.2f} ; Geo.Centroid: cy = {ComIn.cy[ii]:10.2f} ; cz = {ComIn.cz[ii]:10.2f}")
