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
def CalMomofInertia(Point, Segment):
    # Initilization
    Iz = 0.0
    Iy = 0.0
    Iyz = 0.0
    for ii in Segment.ID:
        ti = Segment.PointI[ii]
        tj = Segment.PointJ[ii]
        tY1 = Point.Yc[ti]
        tY2 = Point.Yc[tj]
        tZ1 = Point.Zc[ti]
        tZ2 = Point.Zc[tj]
        teA = Segment.eArea[ii]
        tth = Segment.SegThick[ii]
        tmu = Segment.mu[ii]
        tlambdai = Segment.lambdaa[ii]
        ## Improved CM
        Iz += 1 / 3 * (tY1 ** 2 + tY1 * tY2 + tY2 ** 2) * teA + 1 / 3 * teA * (tth ** 2 / 4 * tmu ** 2)
        Iy += 1 / 3 * (tZ1 ** 2 + tZ1 * tZ2 + tZ2 ** 2) * teA + 1 / 3 * teA * (tth ** 2 / 4 * tlambdai ** 2)
        Iyz += 1 / 6 * teA * (2 * tZ1 * tY1 + tZ1 * tY2 + tZ2 * tY1 + 2 * tZ2 * tY2) + 1 / 6 * teA * (
                    -0.5 * tth ** 2 * tlambdai * tmu)
        Model.SectProperty.Iyy = Iy
        Model.SectProperty.Izz = Iz
        Model.SectProperty.Iyz = Iyz
    #
    if np.abs(Iyz) < 1.0e-8:
        phi = 0.0
    else:
        phi = -(0.5 * math.atan2((-2 * Iyz), (Iz - Iy)))
    Model.SectProperty.phi = phi
    # Moment of inertia in Principle axis
    Iv = (Iy + Iz) / 2 + (Iy - Iz) / 2 * np.cos(2 * phi) - Iyz * np.sin(2 * phi)
    Iw = (Iy + Iz) / 2 - (Iy - Iz) / 2 * np.cos(2 * phi) + Iyz * np.sin(2 * phi)
    Model.SectProperty.Ivv = Iv
    Model.SectProperty.Iww = Iw
    ## transform nodes coordinate to principle axis
    for ii in Point.ID:
        tY = Point.Yc[ii]
        tZ = Point.Zc[ii]
        tV = np.sin(phi) * tZ - np.cos(phi) * tY
        tW = np.cos(phi) * tZ + np.sin(phi) * tY
        Point.V[ii] = tV
        Point.W[ii] = tW

    ## Update conner point
    cos_theta = math.cos(phi)
    sin_theta = math.sin(phi)
    tYgo = Model.SectProperty.ygc
    tZgo = Model.SectProperty.zgc
    # # for i in Model.Segment.ID:
    # #     zip_tmp = zip(Model.Segment.eCorner_y[i], Model.Segment.eCorner_z[i])
    # #     Model.Segment.eCorner_v[i] = [-y * cos_theta + z * sin_theta for y, z in zip_tmp]
    # #     Model.Segment.eCorner_w[i] = [y * sin_theta + z * cos_theta for y, z in zip_tmp]
    for i in Model.Segment.ID:
        teCorner_y_list = Model.Segment.eCorner_y[i]
        teCorner_z_list = Model.Segment.eCorner_z[i]
        teCorner_v_list = [0.0, 0.0, 0.0, 0.0]
        teCorner_w_list = [0.0, 0.0, 0.0, 0.0]
        #
        for index, tyi in enumerate(teCorner_y_list):
            tzi = teCorner_z_list[index]
            ty = -(tyi-tYgo) * cos_theta + (tzi-tZgo) * sin_theta
            tz = (tyi-tYgo) * sin_theta + (tzi-tZgo) * cos_theta
            teCorner_v_list[index] = ty
            teCorner_w_list[index] = tz
        ##
        Model.Segment.eCorner_v[i] = teCorner_v_list
        Model.Segment.eCorner_w[i] = teCorner_w_list
    ## Update point
    for i in Model.Point.ID:
        ty = Model.Point.Yo[i]
        tz = Model.Point.Zo[i]
        # zip_tmp = zip(Model.Point.Yo[i], Model.Point.Zo[i])
        Model.Point.Vo[i] = -(ty-tYgo) * cos_theta + (tz-tZgo) * sin_theta
        Model.Point.Wo[i] = (ty-tYgo) * sin_theta + (tz-tZgo) * cos_theta
    ## Update segment centre point
    for ii in Model.Segment.ID:
        tecy = Model.Segment.ecy[ii]
        tecz = Model.Segment.ecz[ii]
        Model.Segment.ecv[ii] = -(tecy-tYgo) * cos_theta + (tecz-tZgo) * sin_theta
        Model.Segment.ecw[ii] = (tecy-tYgo) * sin_theta + (tecz-tZgo) * cos_theta
    Model.SectProperty.Syy = Model.SectProperty.Iyy / max(Model.Point.Zc.values())
    Model.SectProperty.Szz = Model.SectProperty.Izz / max(Model.Point.Yc.values())
    Model.SectProperty.Svv = Model.SectProperty.Ivv / max(Model.Point.W.values())
    Model.SectProperty.Sww = Model.SectProperty.Iww / max(Model.Point.V.values())
    ## Update segment Q
    for ii in Model.Segment.ID:
        Model.Segment.eQv[ii] = Model.Segment.eArea[ii] * Model.Segment.ecw[ii]
        Model.Segment.eQw[ii] = Model.Segment.eArea[ii] * Model.Segment.ecv[ii]
    return
