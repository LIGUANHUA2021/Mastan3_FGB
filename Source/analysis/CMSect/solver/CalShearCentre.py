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


def CalShearCent(Point, Segment):
    G = 1.0
    tNumP = Point.Count
    Kse = np.zeros((tNumP, tNumP))
    Fse = np.zeros((tNumP, 1))
    ##  form ke & fe
    ke = np.zeros((2, 2))  #  coordinate wi & wj
    fe = np.zeros((2, 1))  #  forces of two nodes
    #
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tY1 = Point.Yc[ti]
        tY2 = Point.Yc[tj]
        tZ1 = Point.Zc[ti]
        tZ2 = Point.Zc[tj]
        teL = Segment.eLen[ii]
        tth = Segment.SegThick[ii]
        ke[0, 0] = G * tth / teL
        ke[1, 1] = ke[0, 0]
        ke[0, 1] = -G * tth / teL
        ke[1, 0] = ke[0, 1]
        #
        # tPointdict = {v: k for k, v in Point.ID.items()}
        # Reverse Dictionary
        tinxi = Point.ID[ti]
        tinxj = Point.ID[tj]
        # ele_indice = np.array([np.array([tinxi, tinxj])]).T
        Kse[tinxi, tinxi] += ke[0, 0]
        Kse[tinxj, tinxj] += ke[1, 1]
        Kse[tinxi, tinxj] += ke[0, 1]
        Kse[tinxj, tinxi] += ke[1, 0]
        ## Form fe
        crt = 1 / teL * (tY1 * tZ2 - tY2 * tZ1)
        fe[0, 0] = -G * tth * crt
        fe[1, 0] = G * tth * crt
        Fse[tinxi] += fe[0, 0]
        Fse[tinxj] += fe[1, 0]
    #
    ## Applied boundary: assume w1 = 0.0
    tKse = Kse[1:, 1:]
    tFse = Fse[1:]
    tw = np.linalg.solve(tKse, tFse)
    w = np.insert(tw,0,values = 0.0, axis=0)
    ## Store warping coordinate refer to geo center
    # Initialization - Aw & Ayw & Azw
    Aw = 0.0
    Ayw = 0.0
    Azw = 0.0
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tInxi = Point.ID[ti]
        tInxj = Point.ID[tj]
        w1 = w[tInxi, 0]
        w2 = w[tInxj, 0]
        Point.w[ti] = w1
        Point.w[tj] = w2
        tY1 = Point.Yc[ti]
        tY2 = Point.Yc[tj]
        tZ1 = Point.Zc[ti]
        tZ2 = Point.Zc[tj]
        teA = Model.Segment.eArea[ii]
        Ayw += 1 / 6.0 * ((2 * tY1 + tY2) * w1 + (tY1 + 2 * tY2) * w2) * teA
        Azw += 1 / 6.0 * ((2 * tZ1 + tZ2) * w1 + (tZ1 + 2 * tZ2) * w2) * teA
        Aw += 1 / 2.0 * (w1 + w2) * teA
    #
    # Position of the shear centre
    Izz = Model.SectProperty.Izz
    Iyy = Model.SectProperty.Iyy
    Iyz = Model.SectProperty.Iyz
    Ysc = (Izz * Azw - Iyz * Ayw) / (Iyy * Izz - Iyz ** 2)
    Zsc = - (Iyy * Ayw - Iyz * Azw) / (Iyy * Izz - Iyz ** 2)
    Model.SectProperty.ysc = Ysc
    Model.SectProperty.zsc = Zsc
    #
    # Transformation constant for the warping ordinate
    Aear = Model.SectProperty.Area
    wk = Aw / Aear
    # Normalized warping coordinate
    for ii in Point.ID:
        wo = Point.w[ii]
        y0 = Point.Yc[ii]
        z0 = Point.Zc[ii]
        Point.w[ii] = wo - wk - z0 * (Ysc) + y0 * (Zsc)
    #
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        Segment.wi[ii] = Point.w[ti]
        Segment.wj[ii] = Point.w[tj]
    return
