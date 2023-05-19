###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu   -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Wenlong Gao -   The Hong Kong Polytechnic University
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import numpy as np
import math
## ......
# Import internal functions
from analysis.CMSect.variables import Model


def GetMCoord():
    OptCoordbyComp = dict() ## {'MatID',{'MaxY', val,'MinY', val,'MaxZ', val,'MinZ', val,'MaxV', val,'MinV', val,'MaxW', val,'MinW', val}}
    for ii in Model.Material.ID:
        for jj in Model.Fiber.FiberID:
            FiberMatID = Model.Fiber.FiberMatID[jj]
            if ii == FiberMatID:
                tY = Model.Fiber.FiberCoorYgo[jj]
                tZ = Model.Fiber.FiberCoorZgo[jj]
                tV = Model.Fiber.FiberCoorV[jj]
                tW = Model.Fiber.FiberCoorW[jj]
                ## Find the maximum and minimum coordinate of & Y & Z &V & W
                if tY >= Model.Fiber.MaxY: Model.Fiber.MaxY = tY
                if tY <= Model.Fiber.MinY: Model.Fiber.MinY = tY
                if tZ >= Model.Fiber.MaxZ: Model.Fiber.MaxZ = tZ
                if tZ <= Model.Fiber.MinZ: Model.Fiber.MinZ = tZ
                #
                if tV >= Model.Fiber.MaxV: Model.Fiber.MaxV = tV
                if tV <= Model.Fiber.MinV: Model.Fiber.MinV = tV
                if tW >= Model.Fiber.MaxW: Model.Fiber.MaxW = tW
                if tW <= Model.Fiber.MinW: Model.Fiber.MinW = tW
        Add2DDict(OptCoordbyComp, ii, 'MaxY', Model.Fiber.MaxY)
        Add2DDict(OptCoordbyComp, ii, 'MinY', Model.Fiber.MinY)
        Add2DDict(OptCoordbyComp, ii, 'MaxZ', Model.Fiber.MaxZ)
        Add2DDict(OptCoordbyComp, ii, 'MinZ', Model.Fiber.MinZ)
        Add2DDict(OptCoordbyComp, ii, 'MaxV', Model.Fiber.MaxV)
        Add2DDict(OptCoordbyComp, ii, 'MinV', Model.Fiber.MinV)
        Add2DDict(OptCoordbyComp, ii, 'MaxW', Model.Fiber.MaxW)
        Add2DDict(OptCoordbyComp, ii, 'MinW', Model.Fiber.MinW)
    return OptCoordbyComp ## 2D Dictionary

def Add2DDict(EditDict, key_a, key_b, val):
    if key_a in EditDict:
        EditDict[key_a].update({key_b: val})
    else:
        EditDict.update({key_a: {key_b: val}})