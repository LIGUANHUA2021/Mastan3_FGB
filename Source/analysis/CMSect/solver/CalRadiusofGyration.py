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

def CalRadiGyration():
    ##
    A = Model.SectProperty.Area
    Iyy = Model.SectProperty.Iyy
    Izz = Model.SectProperty.Izz
    Ivv = Model.SectProperty.Ivv
    Iww = Model.SectProperty.Iww
    t_ry = np.sqrt(Iyy/A)
    t_rz = np.sqrt(Izz/A)
    t_rv = np.sqrt(Ivv/A)
    t_rw = np.sqrt(Iww/A)

    Model.SectProperty.ry = t_ry
    Model.SectProperty.rz = t_rz
    Model.SectProperty.rv = t_rv
    Model.SectProperty.rw = t_rw
    #
    return
