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
# Import internal functions
from analysis.CMSect.variables import Model
from analysis.CMSect.util import FindStress

def CalSectMaxP():
    MaxAxial = 0.0
    for ii in Model.Material.ID:
        for jj in Model.Fiber.FiberID:
            FiberMatID = Model.Fiber.FiberMatID[jj]
            if ii == FiberMatID:
                eArea = Model.Fiber.FiberArea[jj]
                MaxComStrn = float(Model.Material.MaxComStrn[ii])
                MaxComStress = FindStress.FindSteelStress(MaxComStrn, ii)
                MaxAxial += eArea*MaxComStress

    return MaxAxial