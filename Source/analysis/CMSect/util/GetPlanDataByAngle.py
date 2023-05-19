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
# Import internal functions
from analysis.CMSect.variables import Model as CMModel
from analysis.FESect.variables import Model as FEModel
from analysis.CMSect.util.IsVectorBetweentwoOtherVectors import is_vector_between_two_vectors
from analysis.CMSect.util.IsPxMyMzPlan import IsPxMyMzPlan
# from analysis.CMSect.util import GetIntersectantPoint
from analysis.CMSect.util.GetIntersectantPoint import GetInterPoints
#from analysis.CMSect.util.GetIntersectantPoint import GetInterPoints as GetInterP
# ####Only for test!!!
# import pandas as pd


def GetPDataByAng(listSpatialpoints, dMy, dMz, dPx, tFlag):
    # Initialization
    if tFlag == 1:
        MStep = CMModel.YieldSurfaceAnalInfo.MStep         # Momentstep = 36;
        PosNStep = CMModel.YieldSurfaceAnalInfo.PosNStep   # Loadstep = 25;
    elif tFlag == 2:
        MStep = FEModel.YieldSurfaceAnalInfo.MStep  # Momentstep = 36;
        PosNStep = FEModel.YieldSurfaceAnalInfo.PosNStep  # Loadstep = 25;
    ### For testing
    # MStep = 20
    # PosNStep = 10
    listPlan2DPoints = np.zeros((PosNStep*2*2, 2))
    listPlan3DPoints = np.zeros((PosNStep*2*2, 3))
    tempInsertPoint = np.zeros(2)
    # dMy = 0.1
    # dMz = 0.1
    dAngle = math.atan2(dMy, dMz)
    # Set values for tempInsertPoint based on the angle
    FLAG = IsPxMyMzPlan(dAngle)
    if FLAG == 1:
        # if abs(dAngle - np.pi) < 1e-6 or abs(dAngle - (-np.pi)) < 1e-6:
        #     dMz = -dMz
        tempInsertPoint[0] = dMz  # Mz
        tempInsertPoint[1] = 0.0  # My
    elif FLAG == 2:
        # if abs(dAngle - (-np.pi/2.0)) < 1e-6:
        #     dMy = -dMy
        tempInsertPoint[0] = 0.0
        tempInsertPoint[1] = dMy
    else:
        # dMy = np.tan(dAngle) * dMz
        tempInsertPoint[0] = dMz
        tempInsertPoint[1] = dMy
    ##
    ##
    # Get the plan point
    tempListPlan = np.zeros((PosNStep*2*2, 2))
    ind_k = 0
    t_listPlan2DPoints = np.zeros((PosNStep*2*2+2, 2))
    t_listPlan3DPoints = np.zeros((PosNStep*2*2+2, 3))
    IntersectPoint_Coor1 = [0.0, 0.0]
    IntersectPoint_Coor2 = [0.0, 0.0]

    ### For testing
    # YSData01 = pd.DataFrame(Plan2DPts)
    # YSData02 = pd.DataFrame(listSpatialpoints)
    # with pd.ExcelWriter('C:/Users/gaowl/PycharmProjects/Mastan3/Source/gui/msasect/examples/TestPost_3DYS.xlsx') as writer:
    #     # 将 DataFrame 写入 Excel 文件
    #     YSData02.to_excel(writer, sheet_name='Sheet1', index=False)
    # with pd.ExcelWriter('C:/Users/gaowl/PycharmProjects/Mastan3/Source/gui/msasect/examples/TestPost3D_3DData.xlsx') as writer:
    #     # 将 DataFrame 写入 Excel 文件
    #     YSData01.to_excel(writer, sheet_name='Sheet1', index=False)
    ## angle = 0.0; math.pi; -math.pi
    if abs(dPx) < 1e-3:
        tPi_MyMz = listSpatialpoints[PosNStep * (MStep + 1):(PosNStep + 1) * (MStep + 1), :2]
        tPi_PMyMz = listSpatialpoints[PosNStep * (MStep + 1):(PosNStep + 1) * (MStep + 1), :3]
        t_listPlan2DPoints = tPi_MyMz
        t_listPlan3DPoints = tPi_PMyMz
    else:
        if FLAG == 1:
            tPTo_arr = listSpatialpoints[:, 2]
            tMzTo_arr = listSpatialpoints[:, 0]
            tPi_arr = tPTo_arr[::(MStep+1)]
            tempPi_arr1 = tPTo_arr[int(MStep/2)::(MStep+1)]
            tMzi_arr = tMzTo_arr[::(MStep+1)]
            tempMzi_arr1 = tMzTo_arr[int(MStep/2)::(MStep+1)]
            tempPi_list1 = list(tempPi_arr1)
            tPi_list1 = tempPi_list1[::-1]
            # tPi_list1 = tempPi_list1.reverse()
            tempMzi_list1 = list(tempMzi_arr1)
            tMzi_list1 = tempMzi_list1[::-1]
            # tMzi_list1 = tempMzi_list1.reverse()
            ##
            tPi_list = list(tPi_arr)
            tMzi_list = list(tMzi_arr)
            tP_list = tPi_list + tPi_list1
            tMz_list = tMzi_list + tMzi_list1
            ##
            t_listPlan2DPoints[:, 0] = tMz_list
            t_listPlan2DPoints[:, 1] = tP_list
            ##
            t_listPlan3DPoints[:, 0] = tMz_list
            t_listPlan3DPoints[:, 2] = tP_list
            ##
            t_listPlan2DPoints = np.delete(t_listPlan2DPoints, int(PosNStep*2), axis=0)
            t_listPlan3DPoints = np.delete(t_listPlan3DPoints, int(PosNStep*2), axis=0)
            ##
        elif FLAG == 2: ## angle = math.pi / 2.0; -math.pi / 2.0
            tPTo_arr = listSpatialpoints[:, 2]
            tMyTo_arr = listSpatialpoints[:, 1]
            tPi_arr = tPTo_arr[int(MStep / 4)::(MStep + 1)]
            tempPi_arr1 = tPTo_arr[int(3 * MStep / 4)::(MStep + 1)]
            tMyi_arr = tMyTo_arr[int(MStep / 4)::(MStep + 1)]
            tempMyi_arr1 = tMyTo_arr[int(3 * MStep / 4)::(MStep + 1)]
            ##
            tempPi_list1 = list(tempPi_arr1)
            tPi_list1 = tempPi_list1[::-1]
            # tPi_list1 = tempPi_list1.reverse()
            tempMyi_list1 = list(tempMyi_arr1)
            tMyi_list1 = tempMyi_list1[::-1]
            ##
            tPi_list = list(tPi_arr)
            tMyi_list = list(tMyi_arr)
            tP_list = tPi_list + tPi_list1
            tMy_list = tMyi_list + tMyi_list1
            ##
            t_listPlan2DPoints[:, 0] = tMy_list
            t_listPlan2DPoints[:, 1] = tP_list
            ##
            t_listPlan3DPoints[:, 1] = tMy_list
            t_listPlan3DPoints[:, 2] = tP_list
            ##
            t_listPlan2DPoints = np.delete(t_listPlan2DPoints, int(PosNStep*2), axis=0)
            t_listPlan3DPoints = np.delete(t_listPlan3DPoints, int(PosNStep*2), axis=0)
        else:
            # tlistSpatialpoints = listSpatialpoints[MStep+1:]
            # editorlistSpatialpoints = tlistSpatialpoints[:-MStep-1]
            for ii in np.arange(PosNStep * 2 + 1):
                if ii == 0:
                    IntersectPoint_Coor1[0] = 0.0
                    IntersectPoint_Coor1[1] = 0.0
                    IntersectPoint_Coor2[0] = -0.0
                    IntersectPoint_Coor2[1] = -0.0
                elif ii == PosNStep * 2:
                    IntersectPoint_Coor1[0] = -0.0
                    IntersectPoint_Coor1[1] = -0.0
                    IntersectPoint_Coor2[0] = 0.0
                    IntersectPoint_Coor2[1] = 0.0
                else:
                    tPi_MyMz = listSpatialpoints[ii * (MStep+1):(ii+1) * (MStep+1), :2]
                    dInsect_My_z1 = np.array([dMy, dMz])
                    dInsect_My_z2 = np.array([-dMy, -dMz])
                    tbvalue1, tind_Loc1 = is_vector_between_two_vectors(tPi_MyMz, dInsect_My_z1)
                    tbvalue2, tind_Loc2 = is_vector_between_two_vectors(tPi_MyMz, dInsect_My_z2)
                    #
                    if tbvalue1:
                        IntersectPoint_Coor1 = GetInterPoints().Locatelineintersections(tind_Loc1, tPi_MyMz, dInsect_My_z1)
                    if tbvalue2:
                        IntersectPoint_Coor2 = GetInterPoints().Locatelineintersections(tind_Loc2, tPi_MyMz, dInsect_My_z2)
                #
                t_listPlan3DPoints[ii, 0] = IntersectPoint_Coor1[0]
                t_listPlan3DPoints[ii, 1] = IntersectPoint_Coor1[1]
                t_listPlan3DPoints[ii, 2] = listSpatialpoints[ii * (MStep+1), 2]
                ##
                t_listPlan3DPoints[PosNStep * 2 + 1 + ii, 0] = IntersectPoint_Coor2[0]
                t_listPlan3DPoints[PosNStep * 2 + 1 + ii, 1] = IntersectPoint_Coor2[1]
                ## For testing
                # print("MStep = ", MStep)
                # print("PosNStep = ", PosNStep)
                # print("size of t_listPlan3DPoints = ", t_listPlan3DPoints.size)

                t_listPlan3DPoints[PosNStep * 2 + 1 + ii, 2] = listSpatialpoints[(MStep+1) * (PosNStep * 2 - ii), 2]
                ##
                if IntersectPoint_Coor1[1] >= 0.0:
                    t_listPlan2DPoints[ii, 0] = np.sqrt(IntersectPoint_Coor1[0]**2+IntersectPoint_Coor1[1]**2)
                    t_listPlan2DPoints[ii, 1] = listSpatialpoints[ii * (MStep+1), 2]
                    ##
                    t_listPlan2DPoints[PosNStep * 2 + 1 + ii, 0] = -np.sqrt(IntersectPoint_Coor2[0]**2+IntersectPoint_Coor2[1]**2)
                    t_listPlan2DPoints[PosNStep * 2 + 1 +ii, 1] = listSpatialpoints[(MStep+1) * (PosNStep * 2 - ii), 2]
                else:
                    t_listPlan2DPoints[ii, 0] = -np.sqrt(IntersectPoint_Coor1[0] ** 2 + IntersectPoint_Coor1[1] ** 2)
                    t_listPlan2DPoints[ii, 1] = listSpatialpoints[ii * (MStep + 1), 2]
                    ##
                    t_listPlan2DPoints[PosNStep * 2 + 1 + ii, 0] = np.sqrt(
                        IntersectPoint_Coor2[0] ** 2 + IntersectPoint_Coor2[1] ** 2)
                    t_listPlan2DPoints[PosNStep * 2 + 1 + ii, 1] = listSpatialpoints[
                        (MStep + 1) * (PosNStep * 2 - ii), 2]
            ##
            t_listPlan2DPoints = np.delete(t_listPlan2DPoints, PosNStep * 2, axis=0)
            t_listPlan3DPoints = np.delete(t_listPlan3DPoints, PosNStep * 2, axis=0)

    ListPlan2DPoints = t_listPlan2DPoints
    ListPlan3DPoints = t_listPlan3DPoints
    return ListPlan2DPoints, ListPlan3DPoints

def GetLinearInterpolation(x1, list_y1, x2, list_y2, X3):
    '''
    :param x1:
    :param list_y1: list
    :param x2:
    :param list_y2: list
    :param X3: inputted value
    :return: list_y3
    '''
    list_y3 = []
    for y1, y2 in zip(list_y1, list_y2):
        interpolated_value = np.interp(X3, [x1, x2], [y1, y2])
        list_y3.append(interpolated_value)

    return list_y3