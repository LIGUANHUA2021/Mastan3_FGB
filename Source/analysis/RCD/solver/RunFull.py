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
# from Variables import *
# from SystemVariables import *
from analysis.RCD.variables import Model
from analysis.RCD.util import CalMaxAxialForce
from analysis.RCD.util import CalMinAxialForce
from analysis.RCD.solver.CalSectionCapacity import CalSectCapacity
import numpy as np

# ## Only for testing
# import pandas as pd

def RunFullYS():
    # global ResOut, NumResults, bRun_Analysis

    # Variable Initialization
    # NxStep = 0
    # tNumRes = 0
    # NumResults = 0
    ##
    AnalInfo = Model.AnalysisInfo
    GenInfo = Model.GeneralInfo
    PosNStep = GenInfo.PosNStep
    NegNStep = GenInfo.NegNStep
    MomentStep = GenInfo.MomentStep
    ##
    MaxAxial = CalMaxAxialForce.CalSectionMaxP()
    MinAxial = CalMinAxialForce.CalSectionMinP()
    ##
    print('   Run full yield surface analysis ...')

    # Calculate number of required memory to store results
    NumResults = (PosNStep + NegNStep + 2) * (GenInfo.MomentStep + 1)
    ResOut = np.empty(shape=[NumResults,3], dtype=float)

    # For Positive axial load
    NxStep = MaxAxial / PosNStep
    bRun_Analysis = True
    dA = 2 * np.pi / MomentStep
    ##
    Model.YieldSAnalResults.Reset()
    tNumRes = 1  ## Record the number of results data
    ##
    for ii in np.arange(PosNStep):
        InNx = MaxAxial - ii * NxStep
        IsConvergence = True
        # temResOut = np.empty(MomentStep + 1, dtype=typeResults)

        for jj in np.arange(MomentStep + 1):
            InAngle = jj * dA
            IsSubConvergence = 1
            OutMy, OutMz, Dn, IsSubConvergence = CalSectCapacity(InNx, InAngle, MaxAxial, MinAxial)

            if IsSubConvergence:
                # Input results
                Model.YieldSAnalResults.ONx.setdefault(tNumRes, InNx)
                Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
                tNumRes += 1
            else:
                IsConvergence = False
                # break

        # if IsConvergence:
        print(f'    >>> Analysis under axial load = {InNx /1000:.2f} kN, Convergence = {IsConvergence}')

    # For Negative axial load
    NxStep = MinAxial / NegNStep
    bRun_Analysis = True
    dA = 2 * np.pi / MomentStep

    for ii in np.arange(NegNStep + 1):
        InNx = ii * NxStep
        IsConvergence = True
        # tNumRes = 0
        # temResOut = np.empty(MomentStep + 1, dtype=typeResults)

        for jj in np.arange(MomentStep + 1):
            InAngle = jj * dA
            IsSubConvergence = True
            OutMy, OutMz, Dn, IsSubConvergence = CalSectCapacity(InNx, InAngle, MaxAxial, MinAxial)

            if IsSubConvergence:
                # Input results
                Model.YieldSAnalResults.ONx.setdefault(tNumRes, InNx)
                Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
                tNumRes += 1
            else:
                IsConvergence = False
                # break

        # if IsConvergence:
        print(f'    >>> Analysis under axial load = {InNx/1000:.2f} kN, Converge = {IsConvergence}')

    # df1 = pd.DataFrame.from_dict(list(Model.YieldSAnalResults.ONx.values()))
    # df2 = pd.DataFrame.from_dict(list(Model.YieldSAnalResults.OMy.values()))
    # df3 = pd.DataFrame.from_dict(list(Model.YieldSAnalResults.OMz.values()))
    #
    # with pd.ExcelWriter('output_Nx.xlsx') as writer:
    #     # 将 DataFrame 写入 Excel 文件
    #     df1.to_excel(writer, sheet_name='Sheet1', index=False)
    #
    # with pd.ExcelWriter('output_My.xlsx') as writer:
    #     # 将 DataFrame 写入 Excel 文件
    #     df2.to_excel(writer, sheet_name='Sheet1', index=False)
    #
    # with pd.ExcelWriter('output_Mz.xlsx') as writer:
    #     # 将 DataFrame 写入 Excel 文件
    #     df3.to_excel(writer, sheet_name='Sheet1', index=False)


    return