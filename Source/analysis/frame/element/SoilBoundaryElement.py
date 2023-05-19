# External library
import math
import numpy as np
import scipy


class SoilBoundaryElement():
    # ---------------------------------------------------------------------------
    # Element stiffness matrix
    def GetEleK(MemID, Material, Section, Node, Member, SoilParameter, Buried):
        mL = Member.L0[MemID]
        GaussPointCurUL0 = SoilBoundaryElement.GetGaussPointCurUL0(MemID, Member, Node, Section, Material)
        tkSY, tkSZ = SoilBoundaryElement.GetLateralSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        if Buried.Shear[MemID] == 0:
            tkSX = SoilBoundaryElement.GetAxialSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
            tkSthx = SoilBoundaryElement.GetTorsionalSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        else:
            tkSX, tkSthx = SoilBoundaryElement.GetFictionalSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        tPSY, tPSZ = SoilBoundaryElement.GetLateralResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        if Buried.Shear[MemID] == 0:
            tTX = SoilBoundaryElement.GetAxialResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
            tTthX = SoilBoundaryElement.GetTorsionalResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        else:
            tTX, tTthX = SoilBoundaryElement.GetShearResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        tEleK = np.zeros([14, 14])
        tEleKLats = SoilBoundaryElement.GetEleKsLat(tkSY, tkSZ, tPSY, tPSZ, GaussPointCurUL0, mL)  # Lateral soil stiffness matrix
        tEleKFris = SoilBoundaryElement.GetEleKsFri(tkSX, tkSthx, tTX, tTthX, GaussPointCurUL0, mL, Buried.R[MemID])  # Frictional soil stiffness matrix
        tEleK = tEleK + tEleKLats + tEleKFris
        return tEleK

    def GetEleKsLat(kSY, kSZ, PSY, PSZ, GaussPointCurUL0, L):
        """
        PSY = np.array(PSY)
        PSZ = np.array(PSZ)
        P = np.sqrt(np.square(PSY) + np.square(PSZ))
        GaussPointCurUL0 = np.array(GaussPointCurUL0)
        y0 = GaussPointCurUL0[:, 1]
        z0 = GaussPointCurUL0[:, 2]
        sL = np.sqrt(np.square(y0) + np.square(z0))

        ShapeFunc = SoilBoundaryElement.GetLateralShapeFunc(L)
        GaussWeight = [0.064742483,	0.139852696,	0.190915025,	0.208979592,	0.190915025,	0.139852696,	0.064742483]
        GaussWeight = np.array(GaussWeight)
        if not np.any(sL):
            tkyy = GaussWeight * kSY
        else:
            tkyy = GaussWeight * (kSY + P * (1 / sL - y0 ** 2 / (sL) ** 3))
        kyy = np.zeros([4, 4])
        for ii in range(len(GaussWeight)):
            tShapeFunc = ShapeFunc[ii]
            ShapeMat = np.outer(tShapeFunc, tShapeFunc)
            kyy += ShapeMat * tkyy[ii]
        kyy = np.insert(kyy, 0, 0, axis=0)
        kyy = np.insert(kyy, [2, 2, 2], 0, axis=0)
        kyy = np.insert(kyy, 6, 0, axis=0)
        kyy = np.insert(kyy, [8, 8, 8], 0, axis=0)
        kyy = np.insert(kyy, 0, 0, axis=1)
        kyy = np.insert(kyy, [2, 2, 2], 0, axis=1)
        kyy = np.insert(kyy, 6, 0, axis=1)
        kyy = np.insert(kyy, [8, 8, 8], 0, axis=1)

        if not np.any(sL):
            tkzz = GaussWeight * kSZ
        else:
            tkzz = GaussWeight * (kSZ + P * (1 / sL - z0 ** 2 / (sL) ** 3))
        kzz = np.zeros([4, 4])
        for ii in range(len(GaussWeight)):
            tShapeFunc = ShapeFunc[ii]
            ShapeMat = np.outer(tShapeFunc, tShapeFunc)
            kzz += ShapeMat * tkzz[ii]
        kzz = np.insert(kzz, [0, 0], 0, axis=0)
        kzz = np.insert(kzz, [3, 3], 0, axis=0)
        kzz = np.insert(kzz, [6, 6], 0, axis=0)
        kzz = np.insert(kzz, [9, 9], 0, axis=0)
        kzz = np.insert(kzz, [0, 0], 0, axis=1)
        kzz = np.insert(kzz, [3, 3], 0, axis=1)
        kzz = np.insert(kzz, [6, 6], 0, axis=1)
        kzz = np.insert(kzz, [9, 9], 0, axis=1)

        kyz = np.zeros([4, 4])
        if not np.any(sL):
            tkyz = GaussWeight * kSZ
        else:
            tkyz = GaussWeight * (kSZ * y0 * z0 / (sL) ** 2 - P * y0 * z0 / (sL) ** 3)
        for ii in range(len(GaussWeight)):
            tShapeFunc = ShapeFunc[ii]
            ShapeMat = np.outer(tShapeFunc, tShapeFunc)
            kyz += ShapeMat * tkyz[ii]

        kyz = np.insert(kyz, [0, 0], 0, axis=0)
        kyz = np.insert(kyz, [3, 3], 0, axis=0)
        kyz = np.insert(kyz, [6, 6], 0, axis=0)
        kyz = np.insert(kyz, [9, 9], 0, axis=0)
        kyz = np.insert(kyz, 0, 0, axis=1)
        kyz = np.insert(kyz, [2, 2, 2], 0, axis=1)
        kyz = np.insert(kyz, 6, 0, axis=1)
        kyz = np.insert(kyz, [8, 8, 8], 0, axis=1)
        kyz = kyz + kyz.T

        tMp = kyy + kzz + kyz
        ttMp = np.zeros([14, 14])
        ttMp[0: 6, 0: 6] = tMp[0: 6, 0: 6]
        ttMp[7: 13, 0: 6] = tMp[6: 12, 0: 6]
        ttMp[0: 6, 7: 13] = tMp[0: 6, 6: 12]
        ttMp[7: 13, 7: 13] = tMp[6: 12, 6: 12]
        return ttMp
        """
        PSY = np.array(PSY)
        PSZ = np.array(PSZ)
        P = np.sqrt(np.square(PSY) + np.square(PSZ))
        GaussPointCurUL0 = np.array(GaussPointCurUL0)
        y0 = GaussPointCurUL0[:, 1]
        z0 = GaussPointCurUL0[:, 2]
        sL = np.sqrt(np.square(y0) + np.square(z0))
        # y-direction
        CoefficientMatrix = np.zeros([10, 7])
        CoefficientMatrix[0] = [0.064496, 0.127339, 0.118449, 0.052245, 0.008607, 0.000293, 0.000000]
        CoefficientMatrix[1] = [0.001562, 0.013077, 0.022074, 0.013061, 0.002515, 0.000093, 0.000000]
        CoefficientMatrix[2] = [0.000123, 0.006110, 0.031930, 0.052245, 0.031930, 0.006110, 0.000123]
        CoefficientMatrix[3] = [-0.000041, -0.001941, -0.009329, -0.013061, -0.005950, -0.000627, -0.000003]
        CoefficientMatrix[4] = [0.000038, 0.001343, 0.004113, 0.003265, 0.000735, 0.000030, 0.000000]
        CoefficientMatrix[5] = [0.000003, 0.000627, 0.005950, 0.013061, 0.009329, 0.001941, 0.000041]
        CoefficientMatrix[6] = [-0.000001, -0.000199, -0.001738, -0.003265, -0.001738, -0.000199, -0.000001]
        CoefficientMatrix[7] = [0.000000, 0.000293, 0.008607, 0.052245, 0.118449, 0.127339, 0.064496]
        CoefficientMatrix[8] = [0.000000, -0.000093, -0.002515, -0.013061, -0.022074, -0.013077, -0.001562]
        CoefficientMatrix[9] = [0.000000, 0.000030, 0.000735, 0.003265, 0.004113, 0.001343, 0.000038]
        tMty = np.zeros((12, 12))
        # Coefficients: a1 to a10
        if not np.any(sL):
            a = np.dot(CoefficientMatrix, kSY)
        else:
            a = np.dot(CoefficientMatrix, (kSY * y0 ** 2 / (sL) ** 2 ) + P * (1 / sL - y0 ** 2 / (sL) ** 3))
        # Non-diagonal
        tMty[1, 5] = a[1] * L ** 2
        tMty[1, 7] = a[2] * L
        tMty[1, 11] = a[3] * L ** 2
        tMty[5, 7] = a[5] * L ** 2
        tMty[5, 11] = a[6] * L ** 3
        tMty[7, 11] = a[8] * L ** 2
        tMty += tMty.transpose()
        # Diagonal
        tMty[1, 1] = a[0] * L
        tMty[5, 5] = a[4] * L ** 3
        tMty[7, 7] = a[7] * L
        tMty[11, 11] = a[9] * L ** 3
        # z-direction
        # z-direction
        tMtz = np.zeros((12, 12))
        # Coefficients: a1 to a10
        # Coefficients: a1 to a10
        if not np.any(sL):
            a = np.dot(CoefficientMatrix, kSZ)
        else:
            a = np.dot(CoefficientMatrix, kSZ * (z0 ** 2 / (sL) ** 2)+ P * (1 / sL - z0 ** 2 / (sL) ** 3))
        # a = np.dot(CoefficientMatrix, kSZ)
        # Non-diagonal
        tMtz[2, 4] = -a[1] * L ** 2
        tMtz[2, 8] = a[2] * L
        tMtz[2, 10] = -a[3] * L ** 2
        tMtz[4, 8] = -a[5] * L ** 2
        tMtz[4, 10] = a[6] * L ** 3
        tMtz[8, 10] = -a[8] * L ** 2
        tMtz += tMtz.transpose()
        # Diagonal
        tMtz[2, 2] = a[0] * L
        tMtz[4, 4] = a[4] * L ** 3
        tMtz[8, 8] = a[7] * L
        tMtz[10, 10] = a[9] * L ** 3

        ShapeFunc = SoilBoundaryElement.GetLateralShapeFunc(L)
        GaussWeight = [0.064742483, 0.139852696, 0.190915025, 0.208979592, 0.190915025, 0.139852696, 0.064742483]
        GaussWeight = np.array(GaussWeight)
        kyz = np.zeros([4, 4])
        if not np.any(sL):
            tkyz = GaussWeight * kSZ
        else:
            tkyz = GaussWeight * (kSZ * y0 * z0 / (sL) ** 2 - P * y0 * z0 / (sL) ** 3)
        for ii in range(len(GaussWeight)):
            tShapeFunc = ShapeFunc[ii]
            ShapeMat = np.outer(tShapeFunc, tShapeFunc)
            kyz += ShapeMat * tkyz[ii]
        kyz = np.insert(kyz, [0, 0], 0, axis=0)
        kyz = np.insert(kyz, [3, 3], 0, axis=0)
        kyz = np.insert(kyz, [6, 6], 0, axis=0)
        kyz = np.insert(kyz, [9, 9], 0, axis=0)
        kyz = np.insert(kyz, 0, 0, axis=1)
        kyz = np.insert(kyz, [2, 2, 2], 0, axis=1)
        kyz = np.insert(kyz, 6, 0, axis=1)
        kyz = np.insert(kyz, [8, 8, 8], 0, axis=1)
        kyz = kyz + kyz.T

        tMp = tMty + tMtz + kyz
        ttMp = np.zeros([14, 14])
        ttMp[0: 6, 0: 6] = tMp[0: 6, 0: 6]
        ttMp[7: 13, 0: 6] = tMp[6: 12, 0: 6]
        ttMp[0: 6, 7: 13] = tMp[0: 6, 6: 12]
        ttMp[7: 13, 7: 13] = tMp[6: 12, 6: 12]
        return ttMp

    def GetEleKsFri(kSX, kSthx, TX, TthX, GaussPointCurUL0, L, R):
        TX = np.array(TX)
        TthX = np.array(TthX)
        T = np.sqrt(np.square(TX) + np.square(TthX))
        GaussPointCurUL0 = np.array(GaussPointCurUL0)
        u0 = GaussPointCurUL0[:, 1]
        theta0 = GaussPointCurUL0[:, 2]
        st = np.sqrt(np.square(u0) + R ** 2 * np.square(theta0))
        # y-direction

        tMtx = np.zeros((12, 12))
        # Coefficients: a1 to a3
        CoefficientMatrix = np.zeros([3, 7])
        CoefficientMatrix[0] = [0.061490, 0.106041, 0.094331, 0.052245, 0.016849, 0.002336, 0.000042]
        CoefficientMatrix[1] = [0.001605, 0.015738, 0.039867, 0.052245, 0.039867, 0.015738, 0.001606]
        CoefficientMatrix[2] = [0.000042, 0.002336, 0.016849, 0.052245, 0.094331, 0.106041, 0.061490]
        if not np.any(st):
            a = np.dot(CoefficientMatrix, kSX)
        else:
            a = np.dot(CoefficientMatrix, (kSX * u0 ** 2 / st ** 2) + T * (1 / st - u0 ** 2 / (st) ** 3))
        # Non-diagonal
        tMtx[0, 6] = a[1] * L
        tMtx += tMtx.transpose()
        # Diagonal
        tMtx[0, 0] = a[0] * L
        tMtx[6, 6] = a[2] * L
        tMthx = np.zeros((12, 12))
        # Coefficients: a1 to a3
        if not np.any(st):
            a = np.dot(CoefficientMatrix, kSthx)
        else:
            a = np.dot(CoefficientMatrix, (kSthx * R ** 2 * theta0 ** 2 / st ** 2) + T * R ** 2 * (1 / st - R ** 2 * theta0 ** 2  / (st) ** 3))
        # Non-diagonal
        tMthx[3, 9] = a[1] * L
        tMthx += tMthx.transpose()
        # Diagonal
        tMthx[3, 3] = a[0] * L
        tMthx[9, 9] = a[2] * L
        tMt = tMtx + tMthx
        ttMt = np.zeros([14, 14])
        ttMt[0: 6, 0: 6] = tMt[0: 6, 0: 6]
        ttMt[7: 13, 0: 6] = tMt[6: 12, 0: 6]
        ttMt[0: 6, 7: 13] = tMt[0: 6, 6: 12]
        ttMt[7: 13, 7: 13] = tMt[6: 12, 6: 12]
        return ttMt

    # ---------------------------------------------------------------------------
    # Get Rg from Soil Resistance
    def GetRgs(MemID, Material, Section, Node, Member, SoilParameter, Buried):
        mL = Member.L0[MemID]
        GaussPointCurUL0 = SoilBoundaryElement.GetGaussPointCurUL0(MemID, Member, Node, Section, Material)
        tPSY, tPSZ = SoilBoundaryElement.GetLateralResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        if Buried.Shear[MemID] == 0:
            tTX = SoilBoundaryElement.GetAxialResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
            tTthX = SoilBoundaryElement.GetTorsionalResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        else:
            tTX, tTthX = SoilBoundaryElement.GetShearResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0)
        tRgsLat = SoilBoundaryElement.GetLateralResistanceVector(tPSY, tPSZ, mL)
        tRgsFic = SoilBoundaryElement.GetFictionalResistanceVector(tTX, tTthX, mL)
        Rgs = tRgsLat + tRgsFic
        return Rgs

    def GetLateralResistanceVector(PSY, PSZ, L):
        Fy1 = L * (0.064619 * PSY[0] + 0.133449 * PSY[1] + 0.150379 * PSY[2] + 0.104490 * PSY[3] + 0.040536 * PSY[
            4] + 0.006404 * PSY[5] + 0.000124 * PSY[6])
        Fy2 = L * (0.000124 * PSY[0] + 0.006404 * PSY[1] + 0.040536 * PSY[2] + 0.104490 * PSY[3] + 0.150379 * PSY[
            4] + 0.133449 * PSY[5] + 0.064619 * PSY[6])
        Fz1 = L * (0.064619 * PSZ[0] + 0.133449 * PSZ[1] + 0.150379 * PSZ[2] + 0.104490 * PSZ[3] + 0.040536 * PSZ[
            4] + 0.006404 * PSZ[5] + 0.000124 * PSZ[6])
        Fz2 = L * (0.000124 * PSZ[0] + 0.006404 * PSZ[1] + 0.040536 * PSZ[2] + 0.104490 * PSZ[3] + 0.150379 * PSZ[
            4] + 0.133449 * PSZ[5] + 0.064619 * PSZ[6])
        My1 = -(L ** 2) * (
                    0.001565 * PSZ[0] + 0.013704 * PSZ[1] + 0.028024 * PSZ[2] + 0.026122 * PSZ[3] + 0.011844 * PSZ[
                4] + 0.002034 * PSZ[5] + 0.000041 * PSZ[6])
        My2 = (L ** 2) * (
                    0.000041 * PSZ[0] + 0.002034 * PSZ[1] + 0.011844 * PSZ[2] + 0.026122 * PSZ[3] + 0.028024 * PSZ[
                4] + 0.013704 * PSZ[5] + 0.001565 * PSZ[6])
        Mz1 = (L ** 2) * (
                    0.001565 * PSY[0] + 0.013704 * PSY[1] + 0.028024 * PSY[2] + 0.026122 * PSY[3] + 0.011844 * PSY[
                4] + 0.002034 * PSY[5] + 0.000041 * PSY[6])
        Mz2 = -(L ** 2) * (
                    0.000041 * PSY[0] + 0.002034 * PSY[1] + 0.011844 * PSY[2] + 0.026122 * PSY[3] + 0.028024 * PSY[
                4] + 0.013704 * PSY[5] + 0.001565 * PSY[6])
        RgsLat = [0, Fy1, Fz1, 0, My1, Mz1, 0, 0, Fy2, Fz2, 0, My2, Mz2, 0]
        return np.array(RgsLat)

    def GetFictionalResistanceVector(TX, TthX, L):
        Fx1 = L * (0.063095 * TX[0] + 0.121779 * TX[1] + 0.134198 * TX[2] + 0.104490 * TX[3] + 0.056717 * TX[
            4] + 0.018074 * TX[5] + 0.001647 * TX[6])
        Fx2 = L * (0.001647 * TX[0] + 0.018074 * TX[1] + 0.056717 * TX[2] + 0.104490 * TX[3] + 0.134198 * TX[
            4] + 0.121779 * TX[5] + 0.063095 * TX[6])
        Mx1 = L * (0.063095 * TthX[0] + 0.121779 * TthX[1] + 0.134198 * TthX[2] + 0.104490 * TthX[3] + 0.056717 * TthX[
            4] + 0.018074 * TthX[5] + 0.001647 * TthX[6])
        Mx2 = L * (0.001647 * TthX[0] + 0.018074 * TthX[1] + 0.056717 * TthX[2] + 0.104490 * TthX[3] + 0.134198 * TthX[
            4] + 0.121779 * TthX[5] + 0.063095 * TthX[6])
        RgsFic = [Fx1, 0, 0, Mx1, 0, 0, 0, Fx2, 0, 0, Mx2, 0, 0, 0]
        return np.array(RgsFic)

    # ---------------------------------------------------------------------------
    # Get soil stiffness on the Gauss point at the given depth with the certain deflection
    def GetLateralSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        Dely = 1e-7
        tID = Buried.Lateral[MemID]
        tPY = SoilParameter.LateralCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tky = np.zeros(7)
        tkz = np.zeros(7)
        for ii in range(7):
            tv = GaussPointCurUL0[ii][1]
            tw = GaussPointCurUL0[ii][2]
            ty = (tv ** 2 + tw ** 2) ** 0.5
            tP1 = SoilBoundaryElement.GetLateralResistance(tPY, GPDepth[ii], ty)
            tP2 = SoilBoundaryElement.GetLateralResistance(tPY, GPDepth[ii], ty + Dely)
            tk = (tP2 - tP1) / Dely
            tky[ii] = tk * 2 * R[ii]
            tkz[ii] = tk * 2 * R[ii]
        return tky, tkz

    def GetAxialSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        pi = math.pi
        Delx = 1e-7
        tID = Buried.Axial[MemID]
        tTZ = SoilParameter.AxialCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tkx = np.zeros(7)
        for ii in range(7):
            tu = GaussPointCurUL0[ii][0]
            tT1 = SoilBoundaryElement.GetAxialResistance(tTZ, GPDepth[ii], tu)
            tT2 = SoilBoundaryElement.GetAxialResistance(tTZ, GPDepth[ii], tu + Delx)
            tk = (tT2 - tT1) / Delx
            tkx[ii] = abs(tk) * 2 * pi * R[ii]
        return tkx

    def GetTorsionalSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        Delthx = 1e-7
        tID = Buried.Torsion[MemID]
        tTZ = SoilParameter.TorsionCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tkthx = np.zeros(7)
        for ii in range(7):
            tthx = GaussPointCurUL0[ii][3]
            tT1 = SoilBoundaryElement.GetTorsionalResistance(tTZ, GPDepth[ii], tthx, R[ii])
            tT2 = SoilBoundaryElement.GetTorsionalResistance(tTZ, GPDepth[ii], tthx + Delthx, R[ii])
            tk = (tT2 - tT1) / Delthx
            tkthx[ii] = abs(tk)
        return tkthx

    def GetFictionalSoilStiffness(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        pi = math.pi
        Delz = 1e-7
        tID = Buried.Shear[MemID]
        tTZ = SoilParameter.ShearCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tkx, tkthx = np.zeros(7), np.zeros(7)
        for ii in range(7):
            tu, tthx = GaussPointCurUL0[ii][0], GaussPointCurUL0[ii][3]
            tz = (tu ** 2 + (tthx * R[ii]) ** 2) ** 0.5  # Tangential displacement on the pile-soil interface
            tT1 = SoilBoundaryElement.GetFictionalResistance(tTZ, GPDepth[ii], tz)
            tT2 = SoilBoundaryElement.GetFictionalResistance(tTZ, GPDepth[ii], tz + Delz)
            tk = (tT2 - tT1) / Delz
            tkx[ii] = tk * 2 * pi * R[ii]
            tkthx[ii] = tk * 2 * pi * (R[ii] ** 3)
        return tkx, tkthx

    # ---------------------------------------------------------------------------
    # Get soil resistance on the Gauss point
    def GetLateralResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        tID = Buried.Lateral[MemID]
        tPY = SoilParameter.LateralCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tPy, tPz = np.zeros(7), np.zeros(7)
        for ii in range(7):
            tv = GaussPointCurUL0[ii][1]
            tw = GaussPointCurUL0[ii][2]
            ty = (tv ** 2 + tw ** 2) ** 0.5
            tP = SoilBoundaryElement.GetLateralResistance(tPY, GPDepth[ii], ty)
            if ty == 0:
                tPy[ii], tPz[ii] = 0, 0
            else:
                tPy[ii] = tv / ty * tP * 2 * R[ii]
                tPz[ii] = tw / ty * tP * 2 * R[ii]
        return tPy, tPz

    def GetAxialResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        pi = math.pi
        tID = Buried.Axial[MemID]
        tTZ = SoilParameter.AxialCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tTx = np.zeros(7)
        for ii in range(7):
            tu = GaussPointCurUL0[ii][0]
            tT = SoilBoundaryElement.GetAxialResistance(tTZ, GPDepth[ii], abs(tu)) * np.sign(tu)
            tTx[ii] = tT * 2 * pi * R[ii]
        return tTx

    def GetTorsionalResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        tID = Buried.Torsion[MemID]
        tTZ = SoilParameter.TorsionCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tTthx = np.zeros(7)
        for ii in range(7):
            tthx = GaussPointCurUL0[ii][3]
            tT = SoilBoundaryElement.GetTorsionalResistance(tTZ, GPDepth[ii], abs(tthx), R[ii]) * np.sign(tthx)
            tTthx[ii] = tT
        return tTthx

    def GetShearResistanceList(MemID, Member, SoilParameter, Buried, GaussPointCurUL0):
        R = Buried.R[MemID]
        pi = math.pi
        tID = Buried.Shear[MemID]
        tTZ = SoilParameter.ShearCurve[tID]
        GPDepth = Member.GaussPointLocation[Member.ID[MemID], :, 0]  # Depth of the Gauss points
        tTx, tTthx = np.zeros(7), np.zeros(7)
        for ii in range(7):
            tu = GaussPointCurUL0[ii][0]
            tthx = GaussPointCurUL0[ii][3]
            tz = (tu ** 2 + (tthx * R[ii]) ** 2) ** 0.5  # Tangential displacement on the pile-soil interface
            tT = SoilBoundaryElement.GetFictionalResistance(tTZ, GPDepth[ii], tz)
            if tz == 0:
                tTx[ii], tTthx[ii] = 0, 0
            else:
                tTx[ii] = tu / tz * tT * 2 * pi * R[ii]
                tTthx[ii] = (tthx * R[ii]) / tz * tT * R[ii] * 2 * pi * R[ii]
        return tTx, tTthx

    # ---------------------------------------------------------------------------
    # Get soil resistance curve at the given depth
    def GetSoilResistanceCurveAtDepth(SSICurve, Depth):
        DepthList = SSICurve[0, 1:]
        Deflection = SSICurve[1:, 0]
        if Depth >= DepthList[0]:
            return Deflection, SSICurve[1:, 1]
        if Depth <= DepthList[len(DepthList) - 1]:
            return Deflection, SSICurve[1:, len(DepthList)]
        Resistance = np.zeros(len(Deflection))
        for ii in range(len(DepthList) - 1):
            if (Depth - DepthList[ii + 1]) * (Depth - DepthList[ii]) <= 0:
                tDepth1, tDepth2 = DepthList[ii], DepthList[ii + 1]
                for jj in range(len(Deflection)):
                    tResistance1 = SSICurve[jj + 1][ii + 1]
                    tResistance2 = SSICurve[jj + 1][ii + 2]
                    tResistance = tResistance1 + (tResistance2 - tResistance1) / (tDepth2 - tDepth1) * (Depth - tDepth1)
                    Resistance[jj] = tResistance
                break
        return Deflection, Resistance

    # ---------------------------------------------------------------------------
    # Get soil resistance on the Gauss point at the given depth with the certain deflection
    def GetLateralResistance(PY, Depth, y):
        tpy = SoilBoundaryElement.GetSoilResistanceCurveAtDepth(PY, Depth)  # Generate the p-y curve ar the given depth
        f = scipy.interpolate.interp1d(tpy[0], tpy[1])
        return f(y)

    def GetAxialResistance(TZ, Depth, u):
        ttz = SoilBoundaryElement.GetSoilResistanceCurveAtDepth(TZ, Depth)
        f = scipy.interpolate.interp1d(ttz[0], ttz[1])
        return f(u)

    def GetTorsionalResistance(TZ, Depth, thx, R):
        ttz = SoilBoundaryElement.GetSoilResistanceCurveAtDepth(TZ, Depth)
        f = scipy.interpolate.interp1d(ttz[0], ttz[1])
        return f(thx * R) * R * (2 * math.pi * R)

    def GetFictionalResistance(TZ, Depth, u):
        ttz = SoilBoundaryElement.GetSoilResistanceCurveAtDepth(TZ, Depth)
        f = scipy.interpolate.interp1d(ttz[0], ttz[1])
        return f(u)

# =========================================================================================
    # Get Gauss point deflection GPCurU, 7X4 (x/y/z/thx)
    def GetGaussPointCurUL0(tMemID, Member, Node, Section, Material):
        GaussPointCoefficients = [0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]
        GaussPointNum = 7
        tI, tJ = Member.I[tMemID], Member.J[tMemID]
        tSectID = Member.SectID[tMemID]
        tMatID = Section.MatID[tSectID]
        ky, kz = Section.ky[tSectID], Section.kz[tSectID]
        Iy, Iz = Section.Iy[tSectID], Section.Iz[tSectID]
        A = Section.A[tSectID]
        E, G = Material.E[tMatID], Material.G[tMatID]
        L0 = Member.L0[tMemID]
        tEleMtxL0 = Member.EleMtxL0[Member.ID[tMemID] * 3: (Member.ID[tMemID] + 1) * 3, :]
        X01, Y01, Z01 = SoilBoundaryElement.TransferFromGlobalToLocal(tEleMtxL0, np.array([Node.X0[tI], Node.Y0[tI], Node.Z0[tI]]))
        X1, Y1, Z1 = SoilBoundaryElement.TransferFromGlobalToLocal(tEleMtxL0, np.array([Node.X[tI], Node.Y[tI], Node.Z[tI]]))
        X02, Y02, Z02 = SoilBoundaryElement.TransferFromGlobalToLocal(tEleMtxL0, np.array([Node.X0[tJ], Node.Y0[tJ], Node.Z0[tJ]]))
        X2, Y2, Z2 = SoilBoundaryElement.TransferFromGlobalToLocal(tEleMtxL0, np.array([Node.X[tJ], Node.Y[tJ], Node.Z[tJ]]))
        tID = Member.ID[tMemID]
        thX1, thY1, thZ1 = Member.thx1[tID], Member.thy1[tID], Member.thz1[tID]
        thX2, thY2, thZ2 = Member.thx2[tID], Member.thy2[tID], Member.thz2[tID]
        u1, u2 = X1 - X01, X2 - X02
        v1, v2 = Y1 - Y01, Y2 - Y02
        w1, w2 = Z1 - Z01, Z2 - Z02
        tCurUL0 = np.zeros((7, 4))
        # Axial settlement & Torsion
        for ii in range(GaussPointNum):
            tGPC = GaussPointCoefficients[ii] # this coefficient can also stand for the dimensionless location, x/L, used in the shape functions
            tCurUL0[ii][0] = tGPC * (u2 - u1) + u1
            tCurUL0[ii][3] = tGPC * (thX2 - thX1) + thX1
        # Lateral deflection
        for ii in range(GaussPointNum):
            tGPC = GaussPointCoefficients[ii] # this coefficient can also stand for the dimensionless location, x/L, used in the shape functions
            if kz <= 100:
                bz = 12.0 * E * Iz / (kz * G * A * L0 ** 2.0)
                kapaz = 1.0 / (1.0 + bz)
                tCurUL0[ii][1] = (1 - bz * kapaz * tGPC - 3 * kapaz * tGPC ** 2 + 2 * kapaz * tGPC ** 3) * v1 \
                                 + (bz * kapaz * tGPC + 3 * kapaz * tGPC ** 2 - 2 * kapaz * tGPC ** 3) * v2 \
                                 + ((2 + bz) * kapaz / 2 * tGPC - (4 + bz) * kapaz / 2 * tGPC ** 2 + kapaz * tGPC ** 3) * thZ1 * L0 \
                                 - (bz * kapaz / 2 * tGPC + (2 - bz) * kapaz / 2 * tGPC ** 2 - kapaz * tGPC ** 3) * thZ2 * L0
            else:
                tCurUL0[ii][1] = (1 - 3 * tGPC ** 2 + 2 * tGPC ** 3) * v1 \
                                 + (3 * tGPC ** 2 - 2 * tGPC ** 3) * v2 \
                                 + (tGPC - 2 * tGPC ** 2 + tGPC ** 3) * thZ1 * L0 \
                                 - (tGPC ** 2 - tGPC ** 3) * thZ2 * L0
            if ky <= 100:
                by = 12.0 * E * Iy / (ky * G * A * L0 ** 2.0)
                kapay = 1.0 / (1.0 + by)
                tCurUL0[ii][2] = (1 - by * kapay * tGPC - 3 * kapay * tGPC ** 2 + 2 * kapay * tGPC ** 3) * w1 \
                                 + (by * kapay * tGPC + 3 * kapay * tGPC ** 2 - 2 * kapay * tGPC ** 3) * w2 \
                                 - ((2 + by) * kapay / 2 * tGPC - (4 + by) * kapay / 2 * tGPC ** 2 + kapay * tGPC ** 3) * L0 * thY1 \
                                 + (by * kapay / 2 * tGPC + (2 - by) * kapay / 2 * tGPC ** 2 - kapay * tGPC ** 3) * L0 * thY2
            else:
                tCurUL0[ii][2] = (1 - 3 * tGPC ** 2 + 2 * tGPC ** 3) * w1 \
                                 + (3 * tGPC ** 2 - 2 * tGPC ** 3) * w2 \
                                 - (tGPC - 2 * tGPC ** 2 + tGPC ** 3) * thY1 * L0 \
                                 + (tGPC ** 2 - tGPC ** 3) * thY2 * L0
        return tCurUL0


    def GetLateralShapeFunc(L):
        GaussPointCoefficients = np.array([0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]).T
        ShapeFunc = np.zeros([7, 4])
        ShapeFunc[:,0] = 1 - 3 * GaussPointCoefficients ** 2 + 2 * GaussPointCoefficients ** 3
        ShapeFunc[:,1] = 3 * GaussPointCoefficients ** 2 - 2 * GaussPointCoefficients ** 3
        ShapeFunc[:,2] = (1 - 3 * GaussPointCoefficients ** 2 + 2 * GaussPointCoefficients ** 3) * L
        ShapeFunc[:,3] = (1 - 3 * GaussPointCoefficients ** 2 + 2 * GaussPointCoefficients ** 3) * L
        return ShapeFunc
    # Transfer from the global coordinate to the local coordinate
    def TransferFromGlobalToLocal(EleMtxL0, Ug):
        return np.dot(EleMtxL0.transpose(), Ug).tolist()



if __name__ == '__main__':
    import numpy as np

    # # 定义一个一维张量
    # a = np.array([1, 2])
    #
    # # 定义一个三维张量
    # b = np.array([[[1, 1], [1, 1]], [[2, 2], [2, 3]]])
    #
    # # 计算它们的乘积
    # c = np.tensordot(a , b, axes=0)
    #
    # print(c)
    # print(np.sum(c, axis=0))
    a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    a = a + a.T
    print(a)
    # tkyy = np.zeros((4, 4))
    # print(tkyy)