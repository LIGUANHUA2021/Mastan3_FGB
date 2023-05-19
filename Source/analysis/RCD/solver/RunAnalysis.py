#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
#import numpy as np
#import math


# ===========================================================================
from analysis.RCD.variables import Model
from analysis.RCD.util import InitializeModel
from analysis.RCD.util import ComponentPanToCG as CPTCG
from analysis.RCD.solver.RunFull import RunFullYS
from analysis.RCD.solver.RunMyMz import RunMyMzYS
from analysis.RCD.solver.RunPxMy import RunPxMyYS
from analysis.RCD.solver.RunPxMz import RunPxMzYS
from analysis.RCD.solver.RunMyCurve import RunMyCurve
from analysis.RCD.solver.RunMzCurve import RunMzCurve
from analysis.RCD.solver.RunSectionModulus import RunSectModulus


def RunAnal(tAnalF=1):
    ## Initialize
    InitializeModel.InitModel(tAnalF)
    # Import required variables and modules
    # ...
    ComIn = Model.Component
    AnalInfoIn = Model.AnalysisInfo
    for ii in ComIn.ID:
        if ComIn.ComType[ii] == 1:  # Steel
            CPTCG.SteelPanToCG(tComID=ii)
        elif ComIn.ComType[ii] == 2:  # Concrete
            CPTCG.ConcretePanToCG(tComID=ii)
        elif ComIn.ComType[ii] == 3:  # Rebar
            CPTCG.RebarPanToCG(tComID=ii)
        if tAnalF == 1:
            print(f"    >>> Com. ID = {ComIn.ID[ii]:5} ; Name = {ComIn.Name[ii]:<24} ... Succeed!")

    # Select analysis type and start analysis
    if AnalInfoIn.AnaType == "Full-Yield Surface":
        RunFullYS()
    elif AnalInfoIn.AnaType == "My vs. Mz Chart":
        RunMyMzYS()
    elif AnalInfoIn.AnaType == "Px vs. My Chart":
        RunPxMyYS()
    elif AnalInfoIn.AnaType == "Px vs. Mz Chart":
        RunPxMzYS()
    elif AnalInfoIn.AnaType == "My Curvature":
        RunMyCurve()
    elif AnalInfoIn.AnaType == "Mz Curvature":
        RunMzCurve()
    elif AnalInfoIn.AnaType == "SP":
        RunSectModulus()
    # elif AnaType == 100:
    #     RunULS()
    # elif AnaType == 200:
    #     RunSLS()
    # elif AnaType == 1000:
    #     RunMyCurve()
    # elif AnaType == 2000:
    #     RunMzCurve()
    # elif AnaType == 10000:
    #     # Call function for analyzing sectional state
    #     pass
        return
