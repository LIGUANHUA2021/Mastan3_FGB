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
from analysis.RCD.variables import Model
from analysis.RCD.util import CalMaxAxialForce
from analysis.RCD.util import CalMinAxialForce
from analysis.RCD.solver.CalSectionCapacity import CalSectCapacity
from analysis.FESect.variables.Result import SectionProperties

def RunSectModulus():
    ## OutPut ---------------------------------------------------------------
    Zyy = 0.0
    Zzz = 0.0
    Syy = 0.0
    Szz = 0.0
    ## ---------------------------------------------------------------------
    AnalInfo = Model.AnalysisInfo
    PosNStep = AnalInfo.AxialStep
    NegNStep = AnalInfo.AxialStep
    MomentStep = AnalInfo.MomentStep
    MatIn = Model.Material
    #
    MaxAxial = CalMaxAxialForce.CalSectionMaxP()
    MinAxial = CalMinAxialForce.CalSectionMinP()
    #
    print('   Calculate Section Modulus ...')
    ## ----------------------------------------------------------------------
    in_angle = [np.pi / 2, 3 * np.pi / 2]
    tMomentCapacity_Myp = [0.0, 0.0]
    tMomentCapacity_Mys = [0.0, 0.0]
    in_nx = 0.0
    is_convergence = True
    ##
    strnContT = AnalInfo.StrnContType
    strnatVal = AnalInfo.StrnatVal
    ## Reset previous results
    Model.CompositeSectionModulus.ResetCompSectMod()
    ##
    for ii in range(len(np.array(in_angle))):
        out_myp, out_mzp, Dn_p, is_sub_convergence_p = CalSectCapacity(in_nx, in_angle[ii], MaxAxial, MinAxial, 0, 999)
        out_mys, out_mzs, Dn_s, is_sub_convergence_s = CalSectCapacity(in_nx, in_angle[ii], MaxAxial, MinAxial,
                                                                       strnContT, strnatVal)
        if is_sub_convergence_p:
            tMomentCapacity_Myp[ii] = out_myp
        if is_sub_convergence_s:
            tMomentCapacity_Mys[ii] = out_mys
    ##
    MomentCapacity_Myp = max(tMomentCapacity_Myp)
    MomentCapacity_Mys = max(tMomentCapacity_Mys)
    ## ----------------------------------------------------------------------
    in_angle2 = [0, np.pi]
    tMomentCapacity_Mzp = [0.0, 0.0]
    tMomentCapacity_Mzs = [0.0, 0.0]
    in_nx = 0.0
    is_convergence = True
    for ii in range(len(np.array(in_angle2))):
        out_myp, out_mzp, Dn_p, is_sub_convergence_p = CalSectCapacity(in_nx, in_angle2[ii], MaxAxial, MinAxial, 0, 999)
        out_mys, out_mzs, Dn_s, is_sub_convergence_s = CalSectCapacity(in_nx, in_angle2[ii], MaxAxial, MinAxial,
                                                                       strnContT, strnatVal)
        if is_sub_convergence_p:
            tMomentCapacity_Mzp[ii] = out_mzp
        if is_sub_convergence_s:
            tMomentCapacity_Mzs[ii] = out_mzs
    ##
    MomentCapacity_Mzp = max(tMomentCapacity_Mzp)
    MomentCapacity_Mzs = max(tMomentCapacity_Mzs)
    ## ----------------------------------------------------------------------
    RefMatID = AnalInfo.RefMatID
    if RefMatID == -99999:
        tfy = AnalInfo.UDfy
    else:
        tfy = MatIn.Fc[RefMatID]
    ## ----------------------------------------------------------------------
    tZyy = MomentCapacity_Myp / tfy
    tZzz = MomentCapacity_Mzp / tfy
    tSyy = MomentCapacity_Mys / tfy
    tSzz = MomentCapacity_Mzs / tfy
    ## ----------------------------------------------------------------------
    ## Rotate to principal axis
    dA = Model.Section.Phi
    # tv = tz * np.sin(dA) - ty * np.cos(dA)
    # tw = tz * np.cos(dA) + ty * np.sin(dA)
    tZvv = abs(tZzz * np.sin(dA) - tZyy * np.cos(dA))
    tZww = abs(tZzz * np.cos(dA) + tZyy * np.sin(dA))
    tSvv = abs(tSzz * np.sin(dA) - tSyy * np.cos(dA))
    tSww = abs(tSzz * np.cos(dA) + tSyy * np.sin(dA))
    ## ----------------------------------------------------------------------
    Model.CompositeSectionModulus.Zyy = tZyy
    Model.CompositeSectionModulus.Zzz = tZzz
    Model.CompositeSectionModulus.Syy = tSyy
    Model.CompositeSectionModulus.Szz = tSzz
    Model.CompositeSectionModulus.Zvv = tZvv
    Model.CompositeSectionModulus.Zww = tZww
    Model.CompositeSectionModulus.Svv = tSvv
    Model.CompositeSectionModulus.Sww = tSww
    SectionProperties.Zy = tZyy
    SectionProperties.Zz = tZzz
    SectionProperties.Sy = tSyy
    SectionProperties.Sz = tSzz
    SectionProperties.Zv = tZvv
    SectionProperties.Zw = tZww
    SectionProperties.Sv = tSvv
    SectionProperties.Sw = tSww
    ## ----------------------------------------------------------------------
    # print("Zyy = ", tZyy)
    # print("Zzz = ", tZzz)
    # print("Syy = ", tSyy)
    # print("Szz = ", tSzz)
    # print("Zvv = ", tZvv)
    # print("Zww = ", tZww)
    # print("Svv = ", tSvv)
    # print("Sww = ", tSww)
    return
