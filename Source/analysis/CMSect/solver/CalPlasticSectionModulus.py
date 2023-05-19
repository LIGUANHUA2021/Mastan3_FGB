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
from analysis.CMSect.variables import Model
from analysis.CMSect.variables.Model import SectProperty
# from analysis.CMSect.solver.CalStaticMoment import GetPSM


def CalPlasticSectModu(Segment):
    ##
    # Qy
    y_dict = Segment.eCorner_y
    z_dict = Segment.eCorner_z
    z_ax = SectProperty.czp
    y_ax = SectProperty.cyp
    tZy = GetPSM_z(z_dict, y_dict, Model.Segment.ecz, Model.Segment.eQyg, SectProperty.czp)
    # # Qz
    tZz = GetPSM_y(y_dict, z_dict, Model.Segment.ecy, Model.Segment.eQzg, SectProperty.cyp)
    ##
    SectProperty.Zyy = tZy
    SectProperty.Zzz = tZz
    ## ---------------------------------------------------------------
    v_dict = Segment.eCorner_v
    w_dict = Segment.eCorner_w
    w_ax = SectProperty.cwp
    v_ax = SectProperty.cvp
    tZv = GetPSM_z(w_dict, v_dict, Model.Segment.ecw, Model.Segment.eQv, SectProperty.cwp)
    # # Qz
    tZw = GetPSM_y(v_dict, w_dict, Model.Segment.ecv, Model.Segment.eQw, SectProperty.cvp)
    ##
    SectProperty.Zvv = tZv
    SectProperty.Zww = tZw
    return


def GetPSM_z(z_dict, y_dict, ecz, eQyg, z_ax):
    Zyy = 0
    for i in Model.Segment.ID:
        if min(z_dict[i]) >= z_ax or max(z_dict[i]) <= z_ax:
            Zy_tmp = abs(Model.Segment.eArea[i] * (z_ax - ecz[i]))
        else:
            Zy_tmp = get_e_1st_momnt(z_dict[i], y_dict[i], Model.Segment.eArea[i], eQyg[i], z_ax)
        Zyy += Zy_tmp
    return Zyy


def GetPSM_y(y_dict, z_dict, ecy, eQzg, y_ax):
    Zzz = 0
    for i in Model.Segment.ID:
        if min(y_dict[i]) >= y_ax or max(y_dict[i]) <= y_ax:
            Zz_tmp = abs(Model.Segment.eArea[i] * (y_ax - ecy[i]))
        else:
            Zz_tmp = get_e_1st_momnt(y_dict[i], z_dict[i], Model.Segment.eArea[i], eQzg[i], y_ax)
        Zzz += Zz_tmp
    return Zzz


def get_e_1st_momnt(y_list, z_list, Ae, Qze, y_ax):
    """
    Calculate elemental plastic section modulus when the segment crosses the PNA.

    Args:
        y_list: (list[float]) List of nodal y-coordinates in a certain sequence.
        z_list: (list[float]) List of nodal z-coordinates in a certain sequence.
        Ae: (float) Area of the segment.
        Qze: (float) 1st moment of area of the segment.
        y_ax: (float) y-coordinate of the PNA.

    Returns:
        Plastic section modulus of the segment --(float).
    """
    Qzpe = Qze - Ae * y_ax

    yc = []
    yt = []
    yn = []
    zc = []
    zt = []
    zn = []

    for i in range(len(y_list)):
        if y_list[i] > y_ax:
            yc.append(y_list[i])
            zc.append(z_list[i])
        elif y_list[i] < y_ax:
            yt.append(y_list[i])
            zt.append(z_list[i])
        else:
            yn.append(y_list[i])
            zn.append(z_list[i])

    # When only 1 point above PNA
    if len(yc) == 1:
        z_intsc = [zc[0] + (i - zc[0]) * (yc[0] - y_ax) / (yc[0] - j) for i, j in zip(zt, yt)] + zn
        Qc = (max(z_intsc) - min(z_intsc)) * (yc[0] - y_ax) * 0.5 * (yc[0] - y_ax) / 3
        Qt = Qzpe - Qc
    # When only 1 point below PNA
    elif len(yt) == 1:
        z_intsc = [zt[0] + (i - zt[0]) * (y_ax - yt[0]) / (j - yt[0]) for i, j in zip(zc, yc)] + zn
        Qt = (max(z_intsc) - min(z_intsc)) * (y_ax - yt[0]) * 0.5 * (yt[0] - y_ax) / 3
        Qc = Qzpe - Qt
    # When 2 points at each side of PNA
    else:
        z_intsc = []
        for i in range(len(zc)):
            z_intsc += [zc[i] + (j - zc[i]) * (yc[i] - y_ax) / (yc[i] - k) for j, k in zip(zt, yt)]
        z1 = min(zc)
        z2 = max(zc)
        Qc, _ = get_GC([yc[zc.index(z1)] - y_ax, yc[zc.index(z2)] - y_ax, 0, 0], [z1, z2, max(z_intsc), min(z_intsc)],
                       1)
        Qt = Qzpe - Qc
    return abs(Qc) + abs(Qt)

def get_GC(y_list, z_list, area):
    """
    Calculate the coordinate of the elemental centroid.

    Args:
        y_list: (list[float]) List of nodal y-coordinates in a certain sequence.
        z_list: (list[float]) List of nodal z-coordinates in a certain sequence.
        area: (float) Elemental area.

    Returns:
        tuple:
            The y-coordinate of the elemental centroid --(float).
            The z-coordinate of the elemental centroid --(float).
    """
    cy = 0
    cz = 0
    if y_list[0] != y_list[-1] or z_list[0] != z_list[-1]:
        y_list.append(y_list[0])
        z_list.append(z_list[0])

    if area == 0:
        cy = 0
        cz = 0
    else:
        # Shoelace function
        for i in range(len(y_list) - 1):
            tmp = (y_list[i + 1] * z_list[i] - y_list[i] * z_list[i + 1]) / (6 * area)
            cy += (y_list[i] + y_list[i + 1]) * tmp
            cz += (z_list[i] + z_list[i + 1]) * tmp
    return cy, cz
