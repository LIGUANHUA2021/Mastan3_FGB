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
from analysis.RCD.util import PreInitialzeComp
from analysis.RCD.util import InitializeMaterial
from analysis.RCD.util import InitializeFibers
from analysis.RCD.util import InitializeControlingStrain
from analysis.RCD.util import CalSectionProperties
def InitModel(tAnalF=1):
    ##
    PreInitialzeComp.PreIniComponet(tAnalF)
    ##
    InitializeMaterial.InitializeMat(tAnalF)
    ##
    InitializeFibers.InitFibers(tAnalF)
    ##
    InitializeControlingStrain.InitControlingStrain(tAnalF)
    ##
    CalSectionProperties.CalSectProp()
    ##
    return