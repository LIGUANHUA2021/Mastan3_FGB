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
def CalWagnerCoeffs(Point, Segment):
    # Initialization
    tBetay = 0.0
    tBetaz = 0.0
    tBetav = 0.0
    tBetaw = 0.0
    Betaω = 0.0
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tY1 = Point.Yc[ti]
        tY2 = Point.Yc[tj]
        tZ1 = Point.Zc[ti]
        tZ2 = Point.Zc[tj]
        w1 = Segment.wi[ii]
        w2 = Segment.wj[ii]
        teA = Segment.eArea[ii]
        Iyy = Model.SectProperty.Iyy
        Izz = Model.SectProperty.Izz
        Iw = Model.SectProperty.Cw
        tBetay += 1 / (12 * Iyy) * teA * (2 * tY1 * tY2 * (tZ1 + tZ2) + tY1 ** 2 * (tZ2 + 3 * tZ1)) \
                + 1 / (12 * Iyy) * teA * (tY2 ** 2 * (3 * tZ2 + tZ1) + 3 * (tZ1 + tZ2) * (tZ1 ** 2 + tZ2 ** 2))
        tBetaz += 1 / (12 * Izz) * teA * (2 * tZ1 * tZ2 * (tY1 + tY2) + tZ1 ** 2 * (tY2 + 3 * tY1)) \
                + 1 / (12 * Izz) * teA * (tZ2 ** 2 * (3 * tY2 + tY1) + 3 * (tY1 + tY2) * (tY1 ** 2 + tY2 ** 2))
        Betaω += 1 / (12 * Iw) * teA * w1 * (tY2 ** 2 + 2 * tY1 * tY2 + 3 * tY1 ** 2 + tZ2 ** 2 + 2 * tZ1 * tZ2 + 3 * tZ1 ** 2) \
                + 1 / (12 * Iw) * teA * w2 * (tY1 ** 2 + 2 * tY1 * tY2 + 3 * tY2 ** 2 + tZ1 ** 2 + 2 * tZ1 * tZ2 + 3 * tZ2 ** 2)
    Zsc = Model.SectProperty.zsc
    Ysc = Model.SectProperty.ysc
    Betaz = tBetaz - 2 * Ysc
    Betay = tBetay - 2 * Zsc
    Model.SectProperty.Betay = Betay
    Model.SectProperty.Betaz = Betaz
    Model.SectProperty.Betaω = Betaω
    ##
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tY1 = Point.V[ti]
        tY2 = Point.V[tj]
        tZ1 = Point.W[ti]
        tZ2 = Point.W[tj]
        # w1 = Segment.wi[ii]
        # w2 = Segment.wj[ii]
        teA = Segment.eArea[ii]
        Iyy = Model.SectProperty.Ivv
        Izz = Model.SectProperty.Iww
        # Iw = Model.SectProperty.Cw
        tBetav += 1 / (12 * Iyy) * teA * (2 * tY1 * tY2 * (tZ1 + tZ2) + tY1 ** 2 * (tZ2 + 3 * tZ1)) \
                + 1 / (12 * Iyy) * teA * (tY2 ** 2 * (3 * tZ2 + tZ1) + 3 * (tZ1 + tZ2) * (tZ1 ** 2 + tZ2 ** 2))
        tBetaw += 1 / (12 * Izz) * teA * (2 * tZ1 * tZ2 * (tY1 + tY2) + tZ1 ** 2 * (tY2 + 3 * tY1)) \
                + 1 / (12 * Izz) * teA * (tZ2 ** 2 * (3 * tY2 + tY1) + 3 * (tY1 + tY2) * (tY1 ** 2 + tY2 ** 2))
        # Betaω += 1 / (12 * Iw) * teA * w1 * (tY2 ** 2 + 2 * tY1 * tY2 + 3 * tY1 ** 2 + tZ2 ** 2 + 2 * tZ1 * tZ2 + 3 * tZ1 ** 2) \
        #         + 1 / (12 * Iw) * teA * w2 * (tY1 ** 2 + 2 * tY1 * tY2 + 3 * tY2 ** 2 + tZ1 ** 2 + 2 * tZ1 * tZ2 + 3 * tZ2 ** 2)
    Betaw = tBetaw - 2 * Ysc
    Betav = tBetav - 2 * Zsc
    Model.SectProperty.Betav = Betav
    Model.SectProperty.Betaw = Betaw
    return