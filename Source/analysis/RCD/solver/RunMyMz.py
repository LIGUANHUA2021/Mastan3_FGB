#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries

# ## Only for testing
# import pandas as pd
# ===========================================================================
import numpy as np
from analysis.RCD.variables import Model
from analysis.RCD.util import CalMaxAxialForce
from analysis.RCD.util import CalMinAxialForce
from analysis.RCD.solver.CalSectionCapacity import CalSectCapacity


def RunMyMzYS():
    ##
    # GenInfo = Model.GeneralInfo
    AnalInfo = Model.AnalysisInfo
    PosNStep = AnalInfo.AxialStep
    NegNStep = AnalInfo.AxialStep
    MomentStep = AnalInfo.MomentStep
    #
    MaxAxial = CalMaxAxialForce.CalSectionMaxP()
    MinAxial = CalMinAxialForce.CalSectionMinP()
    # Initializing variables
    dA = 2 * np.pi / MomentStep
    is_convergence = True
    tNumRes = 1  ## Record the number of results data

    print('   Run My vs. Mz analysis ...')

    # for ii in range(NumP):
    #     in_nx = AnaP[ii]
    #
    #     t_num_res = 0
    #     tem_res_out = []
    InNx = 0.0 * MaxAxial / (PosNStep+NegNStep)  ## 0.0P ~ 0.9P
    Model.YieldSAnalResults.Reset()
    for jj in np.arange(MomentStep + 1):
        in_angle = jj * dA
        is_sub_convergence = True
        out_my, out_mz, Dn, is_sub_convergence = CalSectCapacity(InNx, in_angle, MaxAxial, MinAxial)
        #
        if is_sub_convergence:
            # Input results
            Model.YieldSAnalResults.ONx_yz.setdefault(tNumRes, InNx)
            Model.YieldSAnalResults.OMy_z.setdefault(tNumRes, out_my)
            Model.YieldSAnalResults.OMz_y.setdefault(tNumRes, out_mz)
            tNumRes += 1
        else:
            is_convergence = False
            break

    if is_convergence:
        print(f"    >>> Analysis under axial load = {InNx / 1000:.2f} kN, Converge = {'True' if is_convergence else 'False'}")

    return
