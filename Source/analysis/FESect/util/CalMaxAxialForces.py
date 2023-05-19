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
from analysis.FESect.variables import Model
from analysis.FESect.util import FindStress

def CalSectMaxP():
    MaxAxial = 0.0
    for ii in Model.Material.ID:
        for jj in Model.Fiber.ID:
            FiberMatID = Model.Fiber.MaterialID[jj]
            if ii == FiberMatID:
                eArea = Model.Fiber.Area[jj]
                MaxComStrn = float(Model.Material.MaxComStrn[ii])
                MaxComStress = FindStress.FindSteelStress(MaxComStrn, ii)
                MaxAxial += eArea*MaxComStress

    return MaxAxial