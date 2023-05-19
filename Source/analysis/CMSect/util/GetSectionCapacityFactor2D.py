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
from analysis.CMSect.util.IsVectorBetweentwoOtherVectors import is_vector_between_two_vectors
from analysis.CMSect.util.GetIntersectantPoint import GetInterPoints as GetInterP
import numpy as np
# ####Only for test!!!
# import pandas as pd


def GetSCF2D(MomInterCurve, LP):
    SCF = 999
    bool_value, index = is_vector_between_two_vectors(MomInterCurve, LP)
    if bool_value:
        ## find the interaction lines
        if index == MomInterCurve.shape[0]-1:
            tx1 = MomInterCurve[index, 0]
            ty1 = MomInterCurve[index, 1]
            tx2 = MomInterCurve[0, 0]
            ty2 = MomInterCurve[0, 1]
        else:
            tx1 = MomInterCurve[index, 0]
            ty1 = MomInterCurve[index, 1]
            tx2 = MomInterCurve[index + 1, 0]
            ty2 = MomInterCurve[index + 1, 1]
        ## find the interaction point
        tStartP = np.array([tx1, ty1])
        tEndP = np.array([tx2, ty2])
        IntersectPoint_Coor, FLAG = GetInterP.GetInterPt(GetInterP, tStartP, tEndP, LP)
        # print("LP=", LP)
        # print("IntersectPoint_Coor=", IntersectPoint_Coor)
        if FLAG:
            try:
                tx11 = LP[0]; tx12 = LP[1]
                tDLP = np.sqrt(tx11*tx11+tx12*tx12)
                tx21 = IntersectPoint_Coor[0]; tx22 = IntersectPoint_Coor[1]
                tDInterP = np.sqrt(tx21*tx21+tx22*tx22)
                # SCF = np.sqrt(tDLP) / np.sqrt(tDInterP)
                SCF = tDLP / tDInterP
            except ZeroDivisionError:
                print("Please be careful with your input as there may be something wrong.")
        # else:
            # YSData01 = pd.DataFrame(MomInterCurve)
            # with pd.ExcelWriter(
            #         'C:/Users/gaowl/PycharmProjects/Mastan3/Source/gui/msasect/examples/Test SCF/Test_PlanarData.xlsx') as writer:
            #     # 将 DataFrame 写入 Excel 文件
            #     YSData01.to_excel(writer, sheet_name='Sheet1', index=False)
            # print("tStartP=", tStartP)
            # print("tEndP=", tEndP)
            # print("LP=", LP)
            # print("index=", index)
    else:
        print("Please be careful with your input as there may be something wrong.")
    return SCF
