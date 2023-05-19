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

def CalSectArea(Point, Segment):
    # Initialization
    Area = 0.0
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tY1 = Point.Yo[ti]
        tY2 = Point.Yo[tj]
        tZ1 = Point.Zo[ti]
        tZ2 = Point.Zo[tj]
        tthick = Segment.SegThick[ii]
        tlen= np.sqrt((tY1-tY2)**2+(tZ1-tZ2)**2)
        tmui = (tZ2-tZ1)/tlen # mu
        tlambdai = (tY2-tY1)/tlen # lambdaa
        Model.Segment.eLen[ii] = tlen
        eA = tlen*tthick
        Model.Segment.eArea[ii] = eA
        Model.Segment.emu[ii] = tmui
        Model.Segment.elambda[ii] = tlambdai
        Area += eA
    #
    Model.SectProperty.Area = Area
    #
    return
