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

def CalGeoC(Point,Segment,Area):
    # Initialization
    AY = 0.0
    AZ = 0.0
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tY1 = Point.Yo[ti]
        tY2 = Point.Yo[tj]
        tZ1 = Point.Zo[ti]
        tZ2 = Point.Zo[tj]
        teAy = Model.Segment.eArea[ii] * (tY1 + tY2) / 2.0
        teAz = Model.Segment.eArea[ii] * (tZ1 + tZ2) / 2.0
        AY += teAy
        AZ += teAz
    #
    Ygeo = AY / Area
    Zgeo = AZ / Area
    Model.SectProperty.ygc = Ygeo
    Model.SectProperty.zgc = Zgeo
    ## Transform points' coordinate refer to geometry centre
    for ii in Point.ID:
        Point.Yc[ii] = Point.Yo[ii] - Ygeo
        Point.Zc[ii] = Point.Zo[ii] - Zgeo
    return