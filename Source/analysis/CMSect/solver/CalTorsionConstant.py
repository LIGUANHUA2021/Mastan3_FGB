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
#
def CalTorsionConst(Point, Segment):
    # Initialization
    Jo = 0.0
    Jc = 0.0
    for ii in Segment.ID:
        tth = Segment.SegThick[ii]
        teL = Segment.eLen[ii]
        alpha = 1.0 - 0.63 * tth / teL * math.tanh(math.pi * teL / 2.0 / tth)
        eJo = 1 / 3.0 * teL * tth ** 3 * alpha
        Jo += eJo
    #
    if Segment.Count >= Point.Count:
        for ii in Segment.ID:
            ti = Segment.PointI[ii]
            tj = Segment.PointJ[ii]
            tY1 = Point.Yc[ti]
            tY2 = Point.Yc[tj]
            tZ1 = Point.Zc[ti]
            tZ2 = Point.Zc[tj]
            w1 = Segment.wi[ii]
            w2 = Segment.wj[ii]
            tth = Segment.SegThick[ii]
            teL = Segment.eLen[ii]
            tLy = tY2 - tY1
            tLz = tZ2 - tZ1
            Zsc = Model.SectProperty.zsc
            Ysc = Model.SectProperty.ysc
            rti = - (tZ1 - Zsc) * (tLy / teL) + (tY1 - Ysc) * (tLz / teL)
            eJc = rti * tth * (rti * teL + w1 - w2)
            Jc += eJc
    #
    # Torsion Constant
    J = Jo + Jc
    Model.SectProperty.J = J
    return
