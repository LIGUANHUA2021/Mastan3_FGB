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
import math
# Import internal functions
from analysis.CMSect.variables import Model

def CalShearA(Segment):
    # Initialization
    ShearAyy = 0.0
    ShearAzz = 0.0
    for ii in Segment.ID:
        teA = Model.Segment.eArea[ii]
        tmui = Model.Segment.emu[ii]
        tlambdai = Model.Segment.elambda[ii]
        teAyy = teA * tmui
        teAzz = teA * tlambdai
        ShearAyy += teAyy
        ShearAzz += teAzz
    ##
    Model.SectProperty.Ayy = abs(ShearAyy)
    Model.SectProperty.Azz = abs(ShearAzz)
    ##
    dA = Model.SectProperty.phi
    tAvv = ShearAyy * math.cos(dA) - ShearAzz * math.sin(dA)
    tAww = ShearAyy * math.sin(dA) + ShearAzz * math.cos(dA)
    Model.SectProperty.Avv = abs(tAvv)
    Model.SectProperty.Aww = abs(tAww)
    ##
    Model.SectProperty.ky = abs(ShearAyy) / Model.SectProperty.Area
    Model.SectProperty.kz = abs(ShearAzz) / Model.SectProperty.Area
    Model.SectProperty.kv = abs(tAvv) / Model.SectProperty.Area
    Model.SectProperty.kw = abs(tAww) / Model.SectProperty.Area
