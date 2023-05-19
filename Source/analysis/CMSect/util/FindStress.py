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

def FindSteelStress(CurStrn, MatID):
    if CurStrn >= 0.0: ## Compression
        if Model.Material.MatProperty[MatID] == 1: ## Simple property
            tE = Model.Material.E[MatID]
            CurStress = CurStrn * tE
            if CurStress > Model.Material.Fy[MatID]:
                CurStress = Model.Material.Fy[MatID]
        #else:
    else: ## Tension
        if Model.Material.MatProperty[MatID] == 1:  ## Simple property
            CurStress = CurStrn * Model.Material.E[MatID]
            if abs(CurStress) > Model.Material.Fy[MatID]: ## Assuming the steel's compressive stress equal to tensional stress
                CurStress = - Model.Material.Fy[MatID]
    return CurStress