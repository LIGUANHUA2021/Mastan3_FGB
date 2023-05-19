#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
# ===========================================================================
import numpy as np
from analysis.RCD.variables import Model
from analysis.RCD.util import CalMaxAxialForce
from analysis.RCD.util import CalMinAxialForce
from analysis.RCD.solver.CalSectionCapacity import CalSectCapacity

def RunPxMzYS():
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
    res_out = []

    print('   Run Nx vs. Mz analysis ...')

    # For positive axial load
    nx_step = MaxAxial / PosNStep
    is_convergence = True
    tNumRes = 1  ## Record the number of results data

    for jj in np.arange(PosNStep):
        in_angle = 0.0
        in_nx = MaxAxial - jj * nx_step
        out_my, out_mz, Dn, is_sub_convergence = CalSectCapacity(in_nx, in_angle, MaxAxial, MinAxial)

        if is_sub_convergence:
            # Input results
            Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, in_nx)
            Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, out_mz)
            tNumRes += 1

        else:
            is_convergence = False
            break
        if is_convergence:
            print(f"    >>> Analysis under axial load = {in_nx / 1000:.2f} kN, Converge = {'Ture' if is_sub_convergence else 'False'}")

    ## ===================================================================================
    ## For negative axial load
    nx_step = MinAxial / NegNStep
    is_convergence = True

    for jj in np.arange(NegNStep):
        in_angle = 0.0
        in_nx = jj * nx_step
        out_my, out_mz, Dn, is_sub_convergence = CalSectCapacity(in_nx, in_angle, MaxAxial, MinAxial)

        if is_sub_convergence:
            # Input results
            Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, in_nx)
            Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, out_mz)
            tNumRes += 1
        else:
            is_convergence = False
            break
        if is_convergence:
            print(f"    >>> Analysis under axial load = {in_nx / 1000:.2f} kN, Converge = {'Ture' if is_sub_convergence else 'False'}")
    ## ----------------------------------------------------------------------------------
    ## For negative axial load
    nx_step = MinAxial / NegNStep
    is_convergence = True
    for jj in np.arange(NegNStep):
        in_angle = np.pi
        in_nx = MinAxial-jj * nx_step
        out_my, out_mz, Dn, is_sub_convergence = CalSectCapacity(in_nx, in_angle, MaxAxial, MinAxial)

        if is_sub_convergence:
            # Input results
            Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, in_nx)
            Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, out_mz)
            tNumRes += 1
        else:
            is_convergence = False
            break
        if is_convergence:
            print(f"    >>> Analysis under axial load = {in_nx / 1000:.2f} kN, Converge = {'Ture' if is_sub_convergence else 'False'}")

    ## ---------------------------------------------------------------------------------
    ## for positive load
    nx_step = MaxAxial / PosNStep
    is_convergence = True
    for jj in np.arange(PosNStep + 1):
        in_angle = np.pi
        in_nx = jj * nx_step
        out_my, out_mz, Dn, is_sub_convergence = CalSectCapacity(in_nx, in_angle, MaxAxial, MinAxial)

        if is_sub_convergence:
            # Input results
            Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, in_nx)
            Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, out_mz)
            tNumRes += 1
        else:
            is_convergence = False
            break
        if is_convergence:
            print(
                f"    >>> Analysis under axial load = {in_nx / 1000:.2f} kN, Converge = {'Ture' if is_sub_convergence else 'False'}")

    return