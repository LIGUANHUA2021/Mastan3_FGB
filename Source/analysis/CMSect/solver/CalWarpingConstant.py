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
# Import standard libraries
import numpy as np
import math
## ......
# Import internal functions
from analysis.CMSect.variables import Model

def CalWarpingConst(Segment):
    # Initialization
    Iw = 0.0
    for ii in Segment.ID:
        w1 = Segment.wi[ii]
        w2 = Segment.wj[ii]
        tth = Segment.SegThick[ii]
        teL = Segment.eLen[ii]
        eIw = tth * teL / 3.0 * (w1 ** 2 + w1 * w2 + w2 ** 2)
        Iw += eIw
    Model.SectProperty.Cw = Iw
    return