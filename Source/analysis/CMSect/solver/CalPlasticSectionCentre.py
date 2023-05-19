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
# Import internal functions
from analysis.CMSect.variables import Model
from analysis.CMSect.variables.Model import SectProperty


def GetPlaticSectCent():
    yu = max(Model.Point.Yo.values())
    yl = min(Model.Point.Yo.values())
    # EAcu = 0
    # EAcl = SectProperty.Area
    Acu = 0
    Acl = SectProperty.Area
    yn = (yu + yl) / 2
    # EAcn, EAtn = GetCTEA(Model.Segment.eCorner_y, Model.Segment.eCorner_z, yn)
    Acn, Atn = GetCTEA(Model.Segment.eCorner_y, Model.Segment.eCorner_z, yn)
    SectProperty.cyp = quasi_Newton(Model.Segment.eCorner_y, Model.Segment.eCorner_z, yu, yl, yn, Acu, Acl, Acn, Atn)
    zu = max(Model.Point.Zo.values())
    zl = min(Model.Point.Zo.values())
    # EAcu = 0
    # EAcl = SectProperty.Area
    Acu = 0
    Acl = SectProperty.Area
    zn = (zu + zl) / 2
    # EAcn, EAtn = GetCTEA(Model.Segment.eCorner_z, Model.Segment.eCorner_y, zn)
    Acn, Atn = GetCTEA(Model.Segment.eCorner_z, Model.Segment.eCorner_y, zn)
    SectProperty.czp = quasi_Newton(Model.Segment.eCorner_z, Model.Segment.eCorner_y, zu, zl, zn, Acu, Acl, Acn, Atn)
    ## -------------------------------------------------------------------------------------------------------------
    vu = max(Model.Point.Vo.values())
    vl = min(Model.Point.Vo.values())
    Acu_p = 0
    Acl_p = SectProperty.Area
    vn = (vu + vl) / 2
    Acn_p, Atn_p = GetCTEA(Model.Segment.eCorner_v, Model.Segment.eCorner_w, vn)
    SectProperty.cvp = quasi_Newton(Model.Segment.eCorner_v, Model.Segment.eCorner_w, vu, vl, vn, Acu_p, Acl_p, Acn_p, Atn_p)
    wu = max(Model.Point.Wo.values())
    wl = min(Model.Point.Wo.values())
    Acu_p = 0
    Acl_p = SectProperty.Area
    wn = (wu + wl) / 2
    Acn_p, Atn_p = GetCTEA(Model.Segment.eCorner_w, Model.Segment.eCorner_v, wn)
    SectProperty.cwp = quasi_Newton(Model.Segment.eCorner_w, Model.Segment.eCorner_v, wu, wl, wn, Acu_p, Acl_p, Acn_p, Atn_p)


def quasi_Newton(y_dict, z_dict, yu, yl, yn, Acu, Acl, Acn, Atn):
    while abs(Acn - Atn) >= SectProperty.Area * 0.001:
        # yn = yl + (yu - yl) / (Acu - Acl) * (SectProperty.Area * 0.5 - Acl)
        yn = yl + (yu - yl) / (Acu - Acl) * (SectProperty.Area * 0.5 - Acl)
        Acn, Atn = GetCTEA(y_dict, z_dict, yn)

        if Acn > Atn:
            yl = yn
        elif Acn < Atn:
            yu = yn
        elif Acn == Atn:
            break

        Acu = GetCTEA(y_dict, z_dict, yu)[0]
        Acl = GetCTEA(y_dict, z_dict, yl)[0]
    return yn

def GetCTEA(y_dict, z_dict, y_ax):
    # EAc = 0
    # EAt = 0
    Ac = 0
    At = 0
    for i in Model.Segment.ID:
        # E = Mat().E[Segment().mat_id[i]]
        # MID = Model.Segment.MatID[i]
        # E = Model.Material.E[MID]
        if min(y_dict[i]) >= y_ax:
            #EAc += E * Model.Segment.eArea[i]
            Ac += Model.Segment.eArea[i]
        elif max(y_dict[i]) <= y_ax:
            # EAt += E * Model.Segment.eArea[i]
            At += Model.Segment.eArea[i]
        else:
            tAc, tAt = get_CT_area(y_dict[i], z_dict[i], Model.Segment.eArea[i], y_ax)
            # EAc += E * Ac
            # EAt += E * At
            Ac += tAc
            At += tAt
    return Ac, At

def get_CT_area(y_list, z_list, area, y_ax):
    """
    Calculate areas of compression and tension zones when the segment crosses the PNA.

    Args:
        y_list: (list[float]) List of nodal y-coordinates in a certain sequence.
        z_list: (list[float]) List of nodal z-coordinates in a certain sequence.
        area: (float) Elemental area.
        y_ax: (float) y-coordinate of the PNA.

    Returns:
        tuple:
            Area of compression zone --(float).
            Area of tension zone --(float).
    """
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
        Ac = (max(z_intsc) - min(z_intsc)) * (yc[0] - y_ax) * 0.5
        At = area - Ac
    # When only 1 point below PNA
    elif len(yt) == 1:
        z_intsc = [zt[0] + (i - zt[0]) * (y_ax - yt[0]) / (j - yt[0]) for i, j in zip(zc, yc)] + zn
        At = (max(z_intsc) - min(z_intsc)) * (y_ax - yt[0]) * 0.5
        Ac = area - At
    # When 2 points at each side of PNA
    else:
        z_intsc = []
        for i in range(len(zc)):
            z_intsc += [zc[i] + (j - zc[i]) * (yc[i] - y_ax) / (yc[i] - k) for j, k in zip(zt, yt)]
        z1 = min(zc)
        z2 = max(zc)
        Ac = get_area([yc[zc.index(z1)], yc[zc.index(z2)], y_ax, y_ax], [z1, z2, max(z_intsc), min(z_intsc)])
        At = area - Ac
    return Ac, At

def get_area(y_list, z_list):
    """
    Calculate the area of a polygon using the shoelace formula.

    Args:
        y_list: (list[float]) List of nodal y-coordinates in a certain sequence.
        z_list: (list[float]) List of nodal z-coordinates in a certain sequence.

    Returns:
        Area of the polygon --(float).
    """
    area = 0
    if y_list[0] != y_list[-1] or z_list[0] != z_list[-1]:
        y_list.append(y_list[0])
        z_list.append(z_list[0])

    # shoelace formula
    for i in range(len(z_list) - 1):
        area += (y_list[i + 1] * z_list[i] - y_list[i] * z_list[i + 1]) * 0.5

    area = abs(area)
    return area