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
## ......
# Import internal functions
from analysis.CMSect.variables import Model
from analysis.CMSect.variables.Model import SectProperty
#
# def CalStaMoment(Point, Segment):
#     # Initialization
#     Qy = 0.0
#     Qz = 0.0
#     for ii in Segment.ID:
#         ti = Segment.PointI[ii]
#         tj = Segment.PointJ[ii]
#         tY1 = Point.V[ti]
#         tY2 = Point.V[tj]
#         tZ1 = Point.W[ti]
#         tZ2 = Point.W[tj]
#         tth = Segment.SegThick[ii]
#         tlen = Segment.eLen[ii]
#         tlambdai = (tY2-tY1)/tlen  # lamdai
#         tmu = (tZ2-tZ1)/tlen       # mui
#         if tlambdai < 0.000001:    # tY1 - tY2= 0
#             if ((tY1-tth/2.0) >=0 and (tY1+tth/2.0) >=0):
#                 eQz1 = tth * tY1 * (tZ2 - tZ1)
#                 eQz2 = 0
#             elif ((tY1 - tth/2.0) <=0 and (tY1+tth/2.0) >=0):
#                 eQz1 = 1 / 8.0 * (tth + 2 * tY1) ** 2 * (tZ2 - tZ1)
#                 eQz2 = 1 / 8.0 * (tth - 2 * tY1) ** 2 * (tZ1 - tZ2)
#             elif ((tY1 - tth/2.0) <=0 and (tY1+tth/2.0) <=0):
#                 eQz1 = 0.0
#                 eQz2 = tth * tY1 * (tZ1 - tZ2)
#             Segment.eQzi = eQz1
#             Segment.eQzj = eQz2
#             #
#             if (tZ1 >= 0 and tZ2 >= 0):
#                 eQy1 = 1 / 2 * tth * (tZ2 ** 2 - tZ1 ** 2)
#                 eQy2 = 0.0
#             elif (tZ1 <= 0 and tZ2 >= 0):
#                 eQy1 = (tth * tZ2 ** 2) / 2
#                 eQy2 = -(tth * tZ1 ** 2) / 2
#             elif (tZ1 <= 0 and tZ2 <= 0):
#                 eQy1 = 0.0
#                 eQy2 = 1 / 2 * tth * (tZ1 ** 2 - tZ2 ** 2)
#             Segment.eQyi = eQy1
#             Segment.eQyj = eQy2
#         elif tmu < 0.000001: #tZ1 - tZ2=0
#             if (tY1 >= 0 and tY2 >= 0):
#                 eQz1 = 1 / 2 * tth * (tY2 ** 2 - tY1 ** 2)
#                 eQz2 = 0.0
#             elif (tY1 <= 0 and tY2 >= 0):
#                 eQz1 = (tth * tY2 ** 2) / 2
#                 eQz2 = -((tth * tY1 ** 2) / 2)
#             elif (tY1 <= 0 and tY2 <= 0):
#                 eQz1 = 0.0
#                 eQz2 = 1 / 2 * tth * (tY1 ** 2 - tY2 ** 2)
#             Segment.eQzi = eQz1
#             Segment.eQzj = eQz2
#             #
#             if ((tZ1-tth/2.0) >=0 and (tZ1+tth/2.0) >=0):
#                 eQy1 = tth * (tY2 - tY1) * tZ2
#                 eQy2 = 0.0
#             elif ((tZ1-tth/2.0) <=0 and (tZ1+tth/2.0) >=0):
#                 eQy1 = 1 / 8.0 * (tY2 - tY1) * (tth + 2 * tZ2) ** 2
#                 eQy2 = 1 / 8.0 * (tY1 - tY2) * (tth - 2 * tZ1) ** 2
#             elif ((tZ1-tth/2.0) <=0 and (tZ1+tth/2.0) <=0):
#                 eQy1 = 0.0
#                 eQy2 = tth * (tY1 - tY2) * tZ2
#             Segment.eQyi = eQy1
#             Segment.eQyj = eQy2
#         else:
#             if (tY1 >= 0 and tY2 >= 0):
#                 eQz1 = (tth * (tY2 ** 2 - tY1 ** 2)) / (2 * tlambdai)
#                 eQz2 = 0.0
#             elif (tY1 <= 0 and tY2 >= 0):
#                 eQz1 = (tth * tY2 ** 2) / (2 * tlambdai)
#                 eQz2 = -((tth * tY1 ** 2) / (2 * tlambdai))
#             elif (tY1 <= 0 and tY2 <= 0):
#                 eQz1 = 0.0
#                 eQz2 = (tth * (tY1 ** 2 - tY2 ** 2)) / (2 * tlambdai)
#             Segment.eQzi = eQz1
#             Segment.eQzj = eQz2
#             #
#             if (tZ1 >= 0 and tZ2 >= 0):
#                 eQy1 = (tth * (tZ2 ** 2 - tZ1 ** 2)) / (2 * tmu)
#                 eQy2 = 0.0
#             elif (tZ1 <= 0 and tZ2 >= 0):
#                 eQy1 = (tth * tZ2 ** 2) / (2 * tmu)
#                 eQy2 = -((tth * tZ1 ** 2) / (2 * tmu))
#             elif (tZ1 <= 0 and tZ2 <= 0):
#                 eQy1 = 0.0
#                 eQy2 = (tth * (tZ1 ** 2 - tZ2 ** 2)) / (2 * tmu)
#             Segment.eQyi = eQy1
#             Segment.eQyj = eQy2
#         #
#         Qy += eQy1
#         Qz += eQz1
#         eQy1 = 0.0
#         eQy2 = 0.0
#         eQz1 = 0.0
#         eQz2 = 0.0
#         #
#     Model.SectProperty.Qv = Qy
#     Model.SectProperty.Qw = Qz
#     #
#     return
def CalStaMoment():
    ##
    Qy = 0.0
    Qz = 0.0
    Qv = 0.0
    Qw = 0.0
    # tygc = SectProperty.ygc
    # tzgc = SectProperty.zgc
    for ii in Model.Segment.ID:
        teA = Model.Segment.eArea[ii]
        tdis_y = Model.Segment.ecy[ii]# - tygc
        tdis_z = Model.Segment.ecz[ii]# - tzgc
        #
        tdis_v = Model.Segment.ecv[ii]# - tygc
        tdis_w = Model.Segment.ecw[ii]# - tzgc
        #
        eQy = teA * tdis_y
        eQz = teA * tdis_z
        #
        eQv = teA * tdis_v
        eQw = teA * tdis_w
        #
        Qy += eQy
        Qz += eQz
        #
        Qv += eQv
        Qw += eQw
    SectProperty.Qy = Qy
    SectProperty.Qz = Qz
    SectProperty.Qv = Qv
    SectProperty.Qw = Qw
    return

