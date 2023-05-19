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
from PySide6.QtCore import QObject

# Import internal functions
from analysis.CMSect.variables import Model
from analysis.CMSect.util.IsPxMyMzPlan import IsPxMyMzPlan
from analysis.CMSect.util.GetPlanDataByAngle import GetPDataByAng
from analysis.CMSect.util.GetIntersectantPoint import GetInterPoints

class GetSCF(QObject):

    def __init__(self):
        super().__init__()

    def GetSectCapacityFactor(self, P, My, Mz, YldSurfData):
        ## Output value
        SCF = []
        PYldSurfData = []
        # Initialazition
        # YldSurfData = YldSurfData{1}(:, 1: 3); # Section full yield surface database
        #
        MStep = Model.YieldSurfaceAnalInfo.MStep #  Momentstep = 36;
        PosNStep = Model.YieldSurfaceAnalInfo.PosNStep #  Loadstep = 25;
        dPx = P
        dMy = My
        dMz = Mz
        dAngle = math.atan2(dMy, dMz)
        dplanPoint = np.array([0.0, 0.0])  # % dplanPoint(0) = P or Mz; dplanPoint(1) = My
        IntersectPoints = np.array([0.0, 0.0, 0.0])
        ###
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        if math.isnan(dPx):
            dPx = 0
        if math.isnan(dMy):
            dMy = 0
        if math.isnan(dMz):
            dMz = 0
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # Convert 3D point to 2D point
        if abs(dPx - 0) < 1e-3 and abs(dMy - 0) < 1e-3 and abs(dMz - 0) < 1e-3:
            SCF = 0.0
            INTERSECTPOINT3D_COOR = []
            PYldSurfData = []
            return SCF, PYldSurfData, INTERSECTPOINT3D_COOR
        elif abs(dMy - 0) < 1e-3 and abs(dMz - 0) < 1e-3:
            dplanPoint[1] = dPx
        else:
            if abs(dPx - 0) < 1e-3:
                dplanPoint[0] = dMz
                dplanPoint[1] = dMy
            else:
                FLAG = IsPxMyMzPlan(dAngle)
                if FLAG == 1:  # This indicates that the point is in the plane Nx-Mz
                    dplanPoint[0] = dMz
                    dplanPoint[1] = dPx
                elif FLAG == 2:  # This indicates that the point is in the plane Nx-My
                    dplanPoint[0] = dMy
                    dplanPoint[1] = dPx
                elif FLAG == 666:
                    if dMy > 0:
                        dplanPoint[0] = math.sqrt(dMy * dMy + dMz * dMz)
                    else:
                        dplanPoint[0] = -math.sqrt(dMy * dMy + dMz * dMz)
                    dplanPoint[1] = dPx
        ##
        [ListPlan2DPoints, ListPlan3DPoints] = GetPDataByAng(YldSurfData, dAngle, dMy, dMz, dPx)
        IntersectPoints_Coor = GetInterPoints.GetIntersectantPoints(dplanPoint, ListPlan2DPoints)

        if IntersectPoints_Coor.shape[0] >= 2:
            tIntpoint_x1 = IntersectPoints_Coor[0, 0]
            tIntpoint_y1 = IntersectPoints_Coor[0, 1]
            td1 = dplanPoint[0] * tIntpoint_x1 + dplanPoint[1] * tIntpoint_y1
            IntersectPoints[0, 0:2] = IntersectPoints_Coor[0, 0:2]
            if td1 < 0:
                IntersectPoints[0, 0:2] = IntersectPoints_Coor[1, 0:2]

        ################################################################################################################
        td2 = 1000
        td3 = 0.001

        if abs(dMy - 0) < 1e-4 and abs(dMz - 0) < 1e-4:
            t_LenInsert = dplanPoint[1]
            if t_LenInsert >= 0:
                t_LenIntersect = max(YldSurfData[:, 0])
            else:
                t_LenIntersect = min(YldSurfData[:, 0])
            IntersectPoint3D_Coor = [t_LenIntersect, 0.0, 0.0]
        elif FLAG == 1 or FLAG == 2:
            t_LenInsert = np.sqrt(dplanPoint[0] ** 2 + dplanPoint[1] ** 2)
            t_LenIntersect = np.sqrt(IntersectPoints[0] ** 2 + IntersectPoints[1] ** 2)
            if FLAG == 1:
                IntersectPoint3D_Coor = [IntersectPoints[1], 0.0, IntersectPoints[0]]  # IntersectPoints[0] = Mz
            else:
                IntersectPoint3D_Coor = [IntersectPoints[1], IntersectPoints[0], 0.0]  # IntersectPoints[1] = My
        elif FLAG == 666:
            if abs(dPx) <= 1e-6:
                t_LenInsert = np.sqrt(dplanPoint[0] ** 2 + dplanPoint[1] ** 2)
                t_LenIntersect = np.sqrt(IntersectPoints[0] ** 2 + IntersectPoints[1] ** 2)
                IntersectPoint3D_Coor = [0.0, IntersectPoints[1], IntersectPoints[0]]  # IntersectPoints[1] = My
            elif abs(dPx) > 1e-6:
                t_LenInsert = np.sqrt(dPx ** 2 + dMy ** 2 + dMz ** 2)
                t_LenIntersect = np.sqrt(IntersectPoints[0] ** 2 + IntersectPoints[1] ** 2)
                tdx = np.cos(dAngle) * IntersectPoints[0]
                tdy = np.sin(dAngle) * IntersectPoints[0]
                IntersectPoint3D_Coor = [IntersectPoints[1], tdy, tdx]

        if t_LenIntersect != 0:
            dSCF = round((t_LenInsert / t_LenIntersect) * td2) * td3

        SCF = dSCF
        PYldSurfData = ListPlan2DPoints
        INTERSECTPOINT3D_COOR = IntersectPoint3D_Coor

        if 't_LenIntersect' not in locals():
            Temp = 1.0

        if t_LenIntersect != 0:
            dSCF = round((t_LenInsert / t_LenIntersect) * td2) * td3

        if 'dSCF' not in locals():
            temp = 1.0

        SCF = dSCF
        PYldSurfData = ListPlan2DPoints
        INTERSECTPOINT3D_COOR = IntersectPoint3D_Coor
        return SCF, PYldSurfData

