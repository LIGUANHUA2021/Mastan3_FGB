###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu   -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Wenlong Gao -   The Hong Kong Polytechnic University
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import numpy as np
import math

def IsPxMyMzPlan(dAngle):
    # Function of MASTAN2
    # dAngle == coordinate of x-axis
    # Output information
    # FLAG == 1   % Indicates the point located in Px-Mz plan
    # FLAG == 2   % Indicates the point located in Px-My plan
    # FLAG == 666 % Indicates the point located in arbitrary plan

    if abs(dAngle) < 1e-3 or abs(dAngle - math.pi) < 1e-3 or abs(dAngle - (-math.pi)) < 1e-3:
        FLAG = 1  # indicate the plan in Px-Mz
    elif abs(dAngle - math.pi / 2.0) < 1e-3 or abs(dAngle - (-math.pi / 2.0)) < 1e-3:
        FLAG = 2  # indicate the plan in Px-My
    else:
        FLAG = 666  # indicate the plan in arbitrary

    return FLAG
