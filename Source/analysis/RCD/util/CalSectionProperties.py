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
from analysis.RCD.util.FindStress import FindStress

def CalSectProp():
    ##
    CalSectionArea()
    ##
    CalSectionGC()
    ##
    CalSectionPC()
    ##
    CalOrienAngle()
    ##
    return

def CalSectionArea():
    SecTotalArea = 0
    SecConcArea = 0
    SecSteelArea = 0
    SecSteelRatio = 0
    SecRebarArea = 0
    SecRebarRatio = 0
    ComIn = Model.Component
    SectionIn = Model.Section
    for ii in ComIn.ID:
        if ComIn.ComType[ii] == 1:    # Steel
            SecSteelArea += ComIn.Area[ii]
        elif ComIn.ComType[ii] == 2:  # Concrete
            SecConcArea += ComIn.Area[ii]
        elif ComIn.ComType[ii] == 3:  # Rebar
            SecRebarArea += ComIn.Area[ii]
    SecTotalArea = SecConcArea + SecSteelArea + SecRebarArea
    ##
    Model.Section.SecTotalArea = SecTotalArea
    Model.Section.SecSteelArea = SecSteelArea
    Model.Section.SecRebarArea = SecRebarArea
    Model.Section.SecConcArea = SecConcArea
    return

def CalSectionGC():
    #global gcy, gcz
    gcy = 0
    gcz = 0
    ##
    ComIn = Model.Component
    SectionIn = Model.Section
    ##
    for ii in ComIn.ID:
        gcy += ComIn.Area[ii] * ComIn.cy[ii]
        gcz += ComIn.Area[ii] * ComIn.cz[ii]
    SecTotalArea = SectionIn.SecTotalArea
    gcy = gcy / SecTotalArea
    gcz = gcz / SecTotalArea
    ##
    Model.Section.gcy = gcy
    Model.Section.gcz = gcz
    ##
    return

def CalSectionPC():
    """
    Calculates the centroid (y, z) of the section's compressive force.

    Returns:
        None
    """
    yield_stress = 0
    pcy = 0
    pcz = 0
    tcy = 0
    tcz = 0
    ##
    ComIn = Model.Component
    MatIn = Model.Material
    ##
    for ii in ComIn.ID:
        #ActMatID = FindMatID(ComIn.MatID[ii])
        ActMatID = ComIn.MatID[ii]
        MaxComStrn = Model.GlobalViariables.MaxComStrn
        yield_stress = FindStress(MaxComStrn, ActMatID)

        pcy += ComIn.Area[ii] * ComIn.cy[ii] * yield_stress
        pcz += ComIn.Area[ii] * ComIn.cz[ii] * yield_stress

        tcy += ComIn.Area[ii] * yield_stress
        tcz += ComIn.Area[ii] * yield_stress

    pcy /= tcy
    pcz /= tcz

# def FindMatID(CurMatID):
#     MatIn = Model.Material
#     for ii in MatIn.ID:
#         if CurMatID == MatIn.ID[ii]:
#             return ii
#     return

def CalOrienAngle():
    ##-----------------------------------------------------------------------
    tSIy = 0.0
    tSIz = 0.0
    tSIyz = 0.0
    ##-----------------------------------------------------------------------
    ComIn = Model.Component
    SectionIn = Model.Section
    for ii in ComIn.ID:
        cy = ComIn.cy[ii]
        cz = ComIn.cz[ii]
        tIy = 0.0
        tIz = 0.0
        tIyz = 0.0
        tCompSFibers = ComIn.CompFibersInfo[ii]
        tFibers = np.array(tCompSFibers["Fibers"])
        for jj in np.arange(len(tFibers)):
            ty = tFibers[jj, 1]
            tz = tFibers[jj, 2]
            teA = tFibers[jj, 3]
            tIy = tIy + teA * (tz - cz) * (tz - cz)
            tIz = tIz + teA * (ty - cy) * (ty - cy)
            tIyz = tIyz + teA * (ty - cy) * (tz - cz)
        ComIn.Iy[ii] = tIy
        ComIn.Iz[ii] = tIz
        ComIn.Iyz[ii] = tIyz
    ##
    for ii in ComIn.ID:
        tSIy += ComIn.Iy[ii]
        tSIz += ComIn.Iz[ii]
        tSIyz += ComIn.Iyz[ii]
    SectionIn.Iy = tSIy
    SectionIn.Iy = tSIz
    SectionIn.Iyz = tSIyz
    ##
    if np.abs(tSIyz) < 1.0e-8:
        phi = 0.0
    else:
        phi = -(0.5 * math.atan2((-2 * tSIyz), (tSIz - tSIy)))
    SectionIn.Phi = phi
    ##
    return