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
class GetInterPoints:

    def GetInterPt(self, StartCoor_xy, EndCoor_xy, InsertPoint_xy):
        # Function of MASTAN2
        #   StartCoor_xy         == Start point coordinate X & Y
        #   EndCoor_xy           == End point coordinate X & Y
        #   InsertPoint_xy       == InsertPoint coordinate X & Y
        #######################################################################
        #
        #   Function purpose:
        #       This function calculate to intersect point coordinate between
        #       two line segments
        #   Output Information:
        #       FLAG                 == indicate two lines intersect or not,
        #                                = 1, intersection; = 0, not intersection
        #       IntersectPoint_Coor  == Coordinate of intersectpoint
        #   Initialazition

        IntersectPoint_Coor = []
        FLAG = 0
        dX1, dY1 = StartCoor_xy
        dX2, dY2 = EndCoor_xy
        InPX1, InPY1 = InsertPoint_xy

        # Determine whether two line segments intersect
        ##*************************************************************************
        #
        if np.abs(InPX1 - 0) < 1e-4 and np.abs(InPY1 - 0) < 1e-4:
            # IntersectPoint_Coor=[np.nan,np.nan]
            # return
            InPX1 = 0.1
        vect1 = [dX1, dY1]
        vect2 = [dX2, dY2]
        vect3 = [InPX1, InPY1]
        #
        t_re1 = np.cross(vect1, vect3)
        t_re2 = np.cross(vect2, vect3)
        #
        t_Re1 = t_re1 * t_re2
        #
        # vect_1 = [-dX1,-dY1]
        # vect_2 = [InPX1-dX1,InPY1-dY1]
        # vect_3 = [dX2-dX1,dY2-dY1]
        # #
        # t_re_1 = np.cross(vect_1,vect_3)
        # t_re_2 = np.cross(vect_2,vect_3)
        # t_Re2 = t_re_1*t_re_2
        if t_Re1 < 0 or abs(t_Re1) < 1e-6:
            FLAG = 1  # There is intersection between a line and a segment
        elif t_Re1 > 0:
            FLAG = 0  # There is no intersection between a line and a segment
        # Calculate to intersect point's coordinate-X&Y
        # The line equation: l1:a1 x + b1 y + c1 = 0
        #                    l2:y =(InPY1/InPX1)*x

        # For testing
        # temp = 0
        # if 'FLAG' not in locals():
        #     temp = 1
        if FLAG == 0:
            # IntersectPoint_Coor=[NaN,NaN]
            pass
        else:
            if abs(dX1 - dX2) < 1e-8 and abs(dY1 - dY2) < 1e-8:
                c1 = round((dX1 + dX2) / 2.0, 2)
                d1 = round((dY1 + dY2) / 2.0, 2)
                IntersectPoint_Coor = [c1, d1]
            elif abs(dX1 - dX2) < 1e-8:
                c1 = -dX1  # b1 = 0, a1 = 1.0
                # if abs(InPX1) < 1e-8:
                #     IntersectPoint_Coor = [0.0, c1]  # FLAG == 1 or 0, InPX1!=0
                # else:
                IntersectPoint_Coor = [c1, c1 * (InPY1 / InPX1)]  # FLAG == 1 or 0, InPX1!=0
            elif abs(dY1 - dY2) < 1e-8:
                c1 = -dY1  # b1 = 1.0, a1 = 0.0
                if abs(InPX1) < 1e-8:
                    IntersectPoint_Coor = [0.0, c1]  # FLAG == 1 or 0, InPX1!=0
                else:
                    IntersectPoint_Coor = [c1 / (InPY1 / InPX1), c1]  # FLAG == 1 or 0, InPY1!=0, InPX1!=0
            elif abs(InPX1) < 1e-8:
                IntersectPoint_Coor = [0.0, -(dY2 - dY1) / (dX2 - dX1) * dX1 + dY1]  # FLAG == 1 or 0, InPX1!=0
            else:
                t_k1 = (dY2 - dY1) / (dX2 - dX1)
                t_k2 = (InPY1 / InPX1)  # InPX1!=0
                tx1 = (dY1 - t_k1 * dX1) / (t_k2 - t_k1)
                IntersectPoint_Coor.append(tx1)
                ty1 = IntersectPoint_Coor[0] * t_k2
                IntersectPoint_Coor.append(ty1)
        ##
        return IntersectPoint_Coor, FLAG

    import numpy as np

    def GetInterPts(self, InsertPoint_xy, listplanepoints):
        # Initialization
        IntersectPoints_Coor = np.zeros((listplanepoints.shape[0], 2))
        dIns_X1, dIns_Y1 = InsertPoint_xy

        # Find all intersection points
        for ii in range(listplanepoints.shape[0]):
            dspoint = listplanepoints[ii, :]
            if ii == listplanepoints.shape[0] - 1:
                depoint = listplanepoints[0, :]
            else:
                depoint = listplanepoints[ii + 1, :]
            t_IntersectPoint_Coor, FLAG = self.GetIntersectantPoint(dspoint, depoint, InsertPoint_xy)

            if FLAG == 0:
                IntersectPoints_Coor[ii, :] = np.nan
            else:
                IntersectPoints_Coor[ii, :] = t_IntersectPoint_Coor

        IntersectPoints_Coor = IntersectPoints_Coor[~np.isnan(IntersectPoints_Coor).any(axis=1)]

        tx1 = np.where(np.isinf(IntersectPoints_Coor[:, 0]))[0]
        tx2 = np.where(np.isinf(IntersectPoints_Coor[:, 1]))[0]
        IntersectPoints_Coor = np.delete(IntersectPoints_Coor, np.concatenate((tx1, tx2)))

        # Remove the same points
        IntersectPoints_Coor = np.unique(np.round(IntersectPoints_Coor, 2), axis=0)

        if IntersectPoints_Coor.shape[0] >= 2:
            tIntpoint_x1, tIntpoint_y1 = IntersectPoints_Coor[0, :]
            td1 = dIns_X1 * tIntpoint_x1 + dIns_Y1 * tIntpoint_y1
            if td1 < 0:
                IntersectPoints_Coor[0, :] = IntersectPoints_Coor[1, :]
                IntersectPoints_Coor[1, :] = np.array([tIntpoint_x1, tIntpoint_y1])

        # Remove the same points again
        if IntersectPoints_Coor.shape[0] > 2:
            t_IntersectPoints_Coor = IntersectPoints_Coor.copy()
            _, ia, _ = np.unique(np.floor(t_IntersectPoints_Coor), axis=0, return_index=True)
            IntersectPoints_Coor = IntersectPoints_Coor[ia, :]

        if IntersectPoints_Coor.shape[0] == 2:
            tIntpoint_x1, tIntpoint_y1 = IntersectPoints_Coor[0, :]
            td1 = dIns_X1 * tIntpoint_x1 + dIns_Y1 * tIntpoint_y1
            if td1 < 0:
                IntersectPoints_Coor[0, :] = IntersectPoints_Coor[1, :]
                IntersectPoints_Coor[1, :] = np.array([tIntpoint_x1, tIntpoint_y1])

        return IntersectPoints_Coor

    def Locatelineintersections(self, tind_Loc1, tPi_MyMz, dInsect_My_z):
        if tind_Loc1 == tPi_MyMz.shape[0]-1:
            tx1 = tPi_MyMz[tind_Loc1, 0]
            ty1 = tPi_MyMz[tind_Loc1, 1]
            tx2 = tPi_MyMz[0, 0]
            ty2 = tPi_MyMz[0, 1]
        else:
            tx1 = tPi_MyMz[tind_Loc1, 0]
            ty1 = tPi_MyMz[tind_Loc1, 1]
            tx2 = tPi_MyMz[tind_Loc1 + 1, 0]
            ty2 = tPi_MyMz[tind_Loc1 + 1, 1]
        ## find the interaction point
        tStartP = np.array([tx1, ty1])
        tEndP = np.array([tx2, ty2])
        IntersectPoint_Coor, FLAG = self.GetInterPt(tStartP, tEndP, dInsect_My_z)
        return IntersectPoint_Coor
