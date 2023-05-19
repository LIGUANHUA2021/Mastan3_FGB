###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Liang Chen, Wenlong Gao
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import numpy as np
## ......
# Import internal functions
from analysis.CMSect.variables import Model
from analysis.CMSect.solver.CalSectionArea import CalSectArea
from analysis.CMSect.solver.CalShearArea import CalShearA
from analysis.CMSect.solver.CalGeoCentre import CalGeoC
from analysis.CMSect.solver.CalMomentofInertia import CalMomofInertia
from analysis.CMSect.solver.CalStaticMoment import CalStaMoment
from analysis.CMSect.solver.CalShearCentre import CalShearCent
from analysis.CMSect.solver.CalWarpingConstant import CalWarpingConst
from analysis.CMSect.solver.CalTorsionConstant import CalTorsionConst
from analysis.CMSect.solver.CalWagnerCoefficients import CalWagnerCoeffs
from analysis.CMSect.solver.CalRadiusofGyration import CalRadiGyration
from analysis.CMSect.solver.CalPlasticSectionCentre import GetPlaticSectCent
from analysis.CMSect.solver.CalPlasticSectionModulus import CalPlasticSectModu
#from analysis.CMSect.solver.CalSectionYieldSurface import CalSectYieldSurf
#
def CalSectProps(Model):
    ## Initialize Model
    Model.initialize()
    ## Calculate section Area
    CalSectArea(Model.Point, Model.Segment)
    ## Calculate section Shear Area (Only valid for project-used)
    CalShearA(Model.Segment)
    ## Calculate section geometry centre
    CalGeoC(Model.Point, Model.Segment, Model.SectProperty.Area)
    ## Calculate section moment of inertia (Iyy, Izz, Iyz, Ivv, Iww)
    CalMomofInertia(Model.Point, Model.Segment)
    ## Calculate section static moment
    CalStaMoment()
    ## Calculate section shear centre
    CalShearCent(Model.Point, Model.Segment)
    ## Calculate warping constant
    CalWarpingConst(Model.Segment)
    ## Calculate Torsion constant
    CalTorsionConst(Model.Point, Model.Segment)
    ## Calculate wagner coefficients, Betay,Betaz,Betaω
    CalWagnerCoeffs(Model.Point, Model.Segment)
    ## Calculate radius of Gyration
    CalRadiGyration()
    ## Calculate plastic section centre
    GetPlaticSectCent()
    # Calculate plastic section modulus
    CalPlasticSectModu(Model.Segment)
    ## Calculate Section Yield Surface
    #CalSectYieldSurf(Model.Point, Model.Segment, Model.Material)
    ## ......
    ## For testing
    #Temp = 1.0
    # To be continue ......
    return
