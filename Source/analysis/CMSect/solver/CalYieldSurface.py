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
import math
## ......
# Import internal functions
from analysis.CMSect.variables import Model
from analysis.CMSect.util import FindComponetMaxMinCoord
from analysis.CMSect.util import FindStress
from analysis.CMSect.util import CalMaxAxialForces
from analysis.CMSect.util import CalMinAxialForces
from analysis.CMSect.solver.CalGeoCentre import CalGeoC
from analysis.CMSect.solver.CalSectionArea import CalSectArea
from analysis.CMSect.solver.CalMomentofInertia import CalMomofInertia
#
from analysis.CMSect.util.PrintLog import PrintLog as pl


# ## Only for testing
# import pandas as pd


class CalYieldS:

    # def __init__(self):
    #     self.plogger = pl(Model.OutResult.FileName, Model.OutResult.ModelName)

    def Initialize(self):
        ## Transform Fiber central coordinate from user-defined to Geometry center
        # Assuming the geometry center and Inclined angle have been obtained
        Model.initialize()
        CalSectArea(Model.Point, Model.Segment)
        ## Calculate section geometry centre
        CalGeoC(Model.Point, Model.Segment, Model.SectProperty.Area)
        ## Calculate section geometry centre
        CalMomofInertia(Model.Point, Model.Segment)
        ##
        Ygc = Model.SectProperty.ygc
        Zgc = Model.SectProperty.zgc
        # print("Ygc = ", Ygc)
        # print("Zgc = ", Zgc)
        for ii in Model.Fiber.FiberID:
            YCoor = Model.Fiber.FiberCoorY[ii]
            ZCoor = Model.Fiber.FiberCoorZ[ii]
            Model.Fiber.FiberCoorYgo[ii] = YCoor - Ygc
            Model.Fiber.FiberCoorZgo[ii] = ZCoor - Zgc
        ##
        ### For testing
        # df1 = pd.DataFrame.from_dict(list(Model.Fiber.FiberCoorYgo.values()))
        # df2 = pd.DataFrame.from_dict(list(Model.Fiber.FiberCoorZgo.values()))
        # filepath1 = "C:/Users/gaowl/PycharmProjects/Mastan3/Source/analysis/CMSect/CMSectFiberTest_cy.xlsx"
        # with pd.ExcelWriter(filepath1) as writer:
        #     # 将 DataFrame 写入 Excel 文件
        #     df1.to_excel(writer, sheet_name='Sheet1', index=False)
        # filepath2 = "C:/Users/gaowl/PycharmProjects/Mastan3/Source/analysis/CMSect/CMSectFiberTest_cz.xlsx"
        # with pd.ExcelWriter(filepath2) as writer:
        #     # 将 DataFrame 写入 Excel 文件
        #     df2.to_excel(writer, sheet_name='Sheet1', index=False)

    def CalSecCapacity(self, InNx, InAngle, MaxAxial, MinAxial):
        ## Initialized Output value
        OutNx = 0.0
        OutMy = 0.0
        OutMz = 0.0
        Dn = 0.0
        IsSubConvergence = 1
        ## ============================================================================
        MaxIter = Model.YieldSurfaceAnalInfo.MaxNumIter
        CurMaxIter = MaxIter
        ## Pre - processing
        if InNx > MaxAxial:
            InNx = min(MaxAxial * 0.995, InNx)
        if InNx < MinAxial:
            InNx = max(MinAxial * 0.995, InNx)
        if InNx > 0.9 * MaxAxial:
            CurMaxIter = MaxIter * 100
        if InNx < 0.9 * MinAxial:
            CurMaxIter = MaxIter * 100
        if abs(InNx) < 100:
            CurMaxIter = MaxIter * 100
        CurAngle = InAngle
        tAng = -1 * CurAngle
        ## Rotate to current angle
        self.RotateToAngle(tAng)
        ## -------------------------------------------------------------------------------
        ## Find initial neutral axis height
        MaxComStr = 0.0035  # Defalut value
        MaxComV = 0.035
        MaxTenStr = 0.02  # Defalut value
        MinTenV = 0.2
        ##
        ## Strain Controling Setting (Only for singal material)
        if Model.YieldSurfaceAnalInfo.BStrainControl == 1:
            for j in Model.Material.ID:
                Model.Material.MaxComStrn[j] = Model.Material.Fy[j] / Model.Material.E[j]
                Model.Material.MaxTenStrn[j] = -Model.Material.Fy[j] / Model.Material.E[j]
        if Model.YieldSurfaceAnalInfo.BStrainControl == 2:
            for j in Model.Material.ID:
                Model.Material.MaxComStrn[j] = Model.YieldSurfaceAnalInfo.StrainAtValue
                Model.Material.MaxTenStrn[j] = -Model.YieldSurfaceAnalInfo.StrainAtValue
        ##
        # OptCoordbyComp = FindComponetMaxMinCoord.GetMCoord() ## 2D Dictionary
        for ii in Model.Material.ID:
            ## Maximum Compressive Strain and Location
            # MaxV = OptCoordbyComp[ii]['MaxV']
            MaxV = Model.Fiber.MaxV
            if MaxV > 0:
                TempComStr = Model.Material.MaxComStrn[ii]
                if abs(TempComStr / MaxV) < abs(MaxComStr / MaxComV):
                    MaxComStr = TempComStr
                    MaxComV = MaxV

            ## Minimum Tensile Strain and Location
            # MinV = OptCoordbyComp[ii]['MinV']
            MinV = Model.Fiber.MinV
            if MinV < 0:
                TempTenStr = Model.Material.MaxTenStrn[ii]
                if abs(TempTenStr / MinV) < abs(MaxTenStr / MinTenV):
                    MaxTenStr = TempTenStr
                    MinTenV = MinV
        ## ============================================================================
        Idn_limt = (MaxTenStr * MaxComV - MaxComStr * MinTenV) / (MaxTenStr - MaxComStr)
        Model.Fiber.Idn_limt = Idn_limt  ## Record the limit value as global variable
        Model.Fiber.MaxComStr = MaxComStr
        Model.Fiber.MaxComV = MaxComV
        Model.Fiber.MaxTenStr = MaxTenStr
        Model.Fiber.MinTenV = MinTenV
        ## ============================================================================
        Counter = 0
        tDn = 0
        CurN = InNx
        ## PreN is the tolerence of the iteration 0.01% of the axial force
        PreN = abs(InNx / 10000000)
        if PreN == 0.0: PreN = 0.00001
        Idn = Idn_limt
        ## Cal. the limit neutral axis position
        TN1, TMy, TMz = self.CalComponentCapacity(Idn)
        MoN = TN1
        Mdn = Idn
        ## ============================================================================
        if CurN >= MoN:  ## Compressive strain control
            ## To store lower bound
            LoN = MoN
            Ldn = Mdn
            ## To find upper bound
            TempStr = MaxTenStr
            MaxTenStr = 0.9999 * MaxComStr
            Idn = MinTenV - MaxTenStr * (MaxComV - MinTenV) / (MaxComStr - MaxTenStr)
            TN2, TMy, TMz = self.CalComponentCapacity(Idn)
            MaxTenStr = TempStr
            ##
            Model.Fiber.MaxTenStr = MaxTenStr
            ##
            MoN = TN2
            Mdn = Idn
        else:  ## Tensile strain control
            ## To find lower bound
            TempStr = MaxComStr
            MaxComStr = 0.9999 * MaxTenStr
            Idn = MinTenV - MaxTenStr * (MaxComV - MinTenV) / (MaxComStr - MaxTenStr)
            TN2, TMy, TMz = self.CalComponentCapacity(Idn)
            MaxComStr = TempStr
            ##
            Model.Fiber.MaxComStr = MaxComStr
            ##
            LoN = TN2
            Ldn = Idn
        ## ============================================================================
        tDn = TN2 - InNx
        TN = 0.0
        #
        if abs(tDn) <= PreN:
            # Model.Fiber.Dn = Idn
            Dn = Idn
            OutMy = TMy * math.cos(InAngle) - TMz * math.sin(InAngle)
            OutMz = TMy * math.sin(InAngle) + TMz * math.cos(InAngle)
            OutNx = InNx
        else:
            while abs(tDn) > PreN:
                if abs(MoN - LoN) > 0.001:
                    Idn = (Mdn - Ldn) / (MoN - LoN) * (InNx - LoN) + Ldn
                    TN, TMy, TMz = self.CalComponentCapacity(Idn)
                    tDn = TN - InNx
                    #
                    if TN > InNx: MoN = TN; Mdn = Idn
                    if TN < InNx: LoN = TN; Ldn = Idn
                    Counter = Counter + 1
                    if Counter >= CurMaxIter: IsSubConvergence = 0; break
                    if abs(Mdn - Ldn) <= 0.005: tDn = 0.0; IsSubConvergence = 1  ## Converged result
                else:
                    IsSubConvergence = 0
                    break
            # print("Counter=", Counter)
        ## ============================================================================
        ## Save the neutral axis
        if IsSubConvergence:
            Dn = Idn
            # OutMy = TMy * math.cos(InAngle) - TMz * math.sin(InAngle)
            # OutMz = TMy * math.sin(InAngle) + TMz * math.cos(InAngle)
            OutMy = TMy * math.cos(InAngle) - TMz * math.sin(InAngle)
            OutMz = TMy * math.sin(InAngle) + TMz * math.cos(InAngle)
            OutNx = InNx
        ##
        return OutNx, OutMy, OutMz, Dn, IsSubConvergence

    def RotateToAngle(self, tdA):
        ##
        Model.Fiber.MaxV = -9999
        Model.Fiber.MinV = 9999
        Model.Fiber.MaxW = -9999
        Model.Fiber.MinW = 9999
        ##
        for ii in Model.Fiber.FiberID:
            YCoor = Model.Fiber.FiberCoorYgo[ii]
            ZCoor = Model.Fiber.FiberCoorZgo[ii]
            Model.Fiber.FiberCoorV[ii] = - YCoor * math.cos(tdA) + ZCoor * math.sin(tdA)
            Model.Fiber.FiberCoorW[ii] = YCoor * math.sin(tdA) + ZCoor * math.cos(tdA)
            tV = Model.Fiber.FiberCoorV[ii]
            tW = Model.Fiber.FiberCoorW[ii]
            ## Find the maximum coordinate of V & W
            if tV >= Model.Fiber.MaxV: Model.Fiber.MaxV = tV
            if tV <= Model.Fiber.MinV: Model.Fiber.MinV = tV
            if tW >= Model.Fiber.MaxW: Model.Fiber.MaxW = tW
            if tW <= Model.Fiber.MinW: Model.Fiber.MinW = tW
        return

    def CalComponentCapacity(self, tIdn):
        MaxComStr = Model.Fiber.MaxComStr
        MaxTenStr = Model.Fiber.MaxTenStr
        MaxComV = Model.Fiber.MaxComV
        MinTenV = Model.Fiber.MinTenV
        tOutStrn = MaxComStr
        Idn_limt = Model.Fiber.Idn_limt
        ##--------------------------------------------------------------------
        oNx = 0.0
        oMy = 0.0
        oMz = 0.0
        ##--------------------------------------------------------------------
        if tIdn < Idn_limt:
            tOutStrn = MaxComStr
        else:
            tOutStrn = MaxTenStr * (tIdn - MaxComV) / (tIdn - MinTenV)
        ##--------------------------------------------------------------------
        for ii in Model.Material.ID:
            temNx = 0.0
            temMy = 0.0
            temMz = 0.0
            if Model.Material.Type[ii] == "S":
                temNx, temMy, temMz = self.CalSteelCapacity(tIdn, tOutStrn)
            elif Model.Material.Type[ii] == "C":
                temNx, temMy, temMz = self.CalConcreteCapacity(tIdn, tOutStrn)
            elif Model.Material.Type[ii] == "R":
                temNx, temMy, temMz = self.CalRebarCapacity(tIdn, tOutStrn)
            else:
                return
            ##
            oNx = oNx + temNx
            oMy = oMy + temMy
            oMz = oMz + temMz
        ##--------------------------------------------------------------------
        return oNx, oMy, oMz

    def CalSteelCapacity(self, tIdn, tOutStrn):
        temNx = 0.0
        temMy = 0.0
        temMz = 0.0
        ##--------------------------------------------------------------------
        for ii in Model.Fiber.FiberID:
            tV = Model.Fiber.FiberCoorV[ii]
            tW = Model.Fiber.FiberCoorW[ii]
            # tV = Model.Fiber.FiberCoorY[ii]
            # tW = Model.Fiber.FiberCoorZ[ii]
            eArea = Model.Fiber.FiberArea[ii]
            MaxComV = Model.Fiber.MaxComV
            ## Linear portion
            eStrain = tOutStrn * (tV - tIdn) / (MaxComV - tIdn)
            # Add residual strain
            # ......eStrain = eStrain + rStrain
            tMatID = Model.Fiber.FiberMatID[ii]
            eStress = FindStress.FindSteelStress(eStrain, tMatID)
            eNx = eArea * eStress
            #
            temNx += eNx
            temMy += eNx * tW
            temMz += eNx * tV
            # temMy += eNx * tV
            # temMz += eNx * tW
        return temNx, temMy, temMz

    def CalConcreteCapacity(self, tIdn, tOutStrn):
        temNx = 0.0
        temMy = 0.0
        temMz = 0.0

        return temNx, temMy, temMz

    def CalRebarCapacity(self, tIdn, tOutStrn):
        temNx = 0.0
        temMy = 0.0
        temMz = 0.0

        return temNx, temMy, temMz

    def CalFullYSurfacePMyMz(self, AxisSlctn):
        ## AxisSlctn: Flag value, 1 for Uer-defined axis; 2 for Principal axis

        ## Transform Fiber central coordinate from user-defined to Geometry center
        # Assuming the geometry center and Inclined angle have been obtained
        # Ygc = Model.SectProperty.ygc
        # Zgc = Model.SectProperty.zgc
        self.Initialize()
        Phi = Model.SectProperty.phi
        #
        if AxisSlctn == 2:
            for ii in Model.Fiber.FiberID:
                YCoor = Model.Fiber.FiberCoorYgo[ii]
                ZCoor = Model.Fiber.FiberCoorZgo[ii]
                Model.Fiber.FiberCoorYgo[ii] = -YCoor * math.cos(Phi) + ZCoor * math.sin(Phi)
                Model.Fiber.FiberCoorZgo[ii] = YCoor * math.sin(Phi) + ZCoor * math.cos(Phi)
        pl().Print(" >>>  Run full yield surface analysis ...")
        ## Calculate Maximum Axial Forces
        MaxAxial = CalMaxAxialForces.CalSectMaxP()
        MinAxial = CalMinAxialForces.CalSectMinP()
        ## For Positive axial load
        PosNStep = Model.YieldSurfaceAnalInfo.PosNStep
        NxStep = MaxAxial / PosNStep
        MStep = Model.YieldSurfaceAnalInfo.MStep
        dAng = 2 * math.pi / MStep
        tNumRes = 1  ## Record the number of results data
        # self.Initialize()
        Model.YieldSAnalResults.Reset()
        ## Record Strain Contorling Type
        tStrnContlType = 0
        if Model.YieldSurfaceAnalInfo.BStrainControl == 0:
            tStrnContlType = 0
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 1:
            tStrnContlType = 1
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 2:
            tStrnContlType = 2
        Model.YieldSAnalResults.StrnContlType = tStrnContlType
        ##
        for ii in range(PosNStep):
            InNx = MaxAxial - ii * NxStep
            IsConvergence = 1
            for jj in range(MStep + 1):
                InAngle = jj * dAng
                # CalYS = CalYieldSurface.CalYieldS()  ## Instantiated Class: CalYieldS
                # CalYS.Initialize()
                OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
                #
                if IsSubConvergence:
                    Model.YieldSAnalResults.ONx.setdefault(tNumRes, OutNx)
                    Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                    Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                    Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                    Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
                else:
                    IsConvergence = 0
                    #
                tNumRes += 1
                #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        ##========================================================================================
        ## For negative axial load
        NegNStep = Model.YieldSurfaceAnalInfo.NegNStep
        NxStep = MinAxial / NegNStep
        MStep = Model.YieldSurfaceAnalInfo.MStep
        dAng = 2 * math.pi / MStep
        ## tNumRes = 0  ## Record the number of results data
        for ii in range(NegNStep + 1):
            InNx = ii * NxStep
            IsConvergence = 1
            for jj in range(MStep + 1):
                InAngle = jj * dAng
                # CalYS = CalYieldSurface.CalYieldS()  ## Instantiated Class: CalYieldS
                # CalYS.Initialize()
                OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
                #
                if IsSubConvergence:
                    Model.YieldSAnalResults.ONx.setdefault(tNumRes, OutNx)
                    Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                    Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                    Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                    Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
                else:
                    IsConvergence = 0
                #
                tNumRes += 1
                #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
            #
        return

    ##
    def CalPlanarYSurfaceMyMz(self, AxisSlctn):
        self.Initialize()
        Phi = Model.SectProperty.phi
        #
        if AxisSlctn == 2:
            for ii in Model.Fiber.FiberID:
                # Model.Fiber.FiberCoorYgo[ii] = Model.Fiber.FiberCoorYgo[ii] - Model.SectProperty.ygc
                # Model.Fiber.FiberCoorZgo[ii] = Model.Fiber.FiberCoorZgo[ii] - Model.SectProperty.zgc
                YCoor = Model.Fiber.FiberCoorYgo[ii]
                ZCoor = Model.Fiber.FiberCoorZgo[ii]
                Model.Fiber.FiberCoorYgo[ii] = -YCoor * math.cos(Phi) + ZCoor * math.sin(Phi)
                Model.Fiber.FiberCoorZgo[ii] = YCoor * math.sin(Phi) + ZCoor * math.cos(Phi)
            pl().Print(" >>>  Run Mv vs. Mw analysis ...")
        else:
            pl().Print(" >>>  Run My vs. Mz analysis ...")
        ## Calculate Maximum Axial Forces
        MaxAxial = CalMaxAxialForces.CalSectMaxP()
        MinAxial = CalMinAxialForces.CalSectMinP()
        ## --------------------------------------------------------------------------------
        NumAxialLoad = Model.Fiber.NumAxialLoad  ## This value mean that the number of the analysis axial load.
        MStep = Model.YieldSurfaceAnalInfo.MStep
        dAng = 2 * np.pi / MStep
        tNumRes = 1  ## Record the number of results data
        # self.Initialize()
        Model.YieldSAnalResults.ResetOMyMz()
        ## Record Strain Contorling Type
        tStrnContlType = 0
        if Model.YieldSurfaceAnalInfo.BStrainControl == 0:
            tStrnContlType = 0
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 1:
            tStrnContlType = 1
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 2:
            tStrnContlType = 2
        Model.YieldSAnalResults.MyMz_StrnContlType = tStrnContlType
        ##
        # for ii in range(NumAxialLoad):
        InNx = 0.0 * MaxAxial / NumAxialLoad  ## 0.0P ~ 0.9P
        IsConvergence = 1
        for jj in np.arange(MStep + 1):
            InAngle = jj * dAng
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_yz.setdefault(tNumRes, OutNx)
                Model.YieldSAnalResults.OMy_z.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz_y.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
                tNumRes += 1
            else:
                IsConvergence = 0
                ## For testing

            # print(" >>>  Analysis under axial load = ".ljust(50, ' ') + str(
            #     str("%.3f" % (InNx / 1000)) + " kN, Convergence = " + str(bool(IsSubConvergence))).rjust(30, ' '))
            #
            #
        if IsConvergence:
            # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
            # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
            # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
            if abs(InNx) < 1e-6: InNx = 0.0
            pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
            #
        return

    ##
    def CalPlanarYSurfacePMy(self, AxisSlctn):
        ##
        self.Initialize()
        Phi = Model.SectProperty.phi
        #
        if AxisSlctn == 2:
            for ii in Model.Fiber.FiberID:
                # Model.Fiber.FiberCoorYgo[ii] = Model.Fiber.FiberCoorYgo[ii] - Model.SectProperty.ygc
                # Model.Fiber.FiberCoorZgo[ii] = Model.Fiber.FiberCoorZgo[ii] - Model.SectProperty.zgc
                YCoor = Model.Fiber.FiberCoorYgo[ii]
                ZCoor = Model.Fiber.FiberCoorZgo[ii]
                Model.Fiber.FiberCoorYgo[ii] = -YCoor * math.cos(Phi) + ZCoor * math.sin(Phi)
                Model.Fiber.FiberCoorZgo[ii] = YCoor * math.sin(Phi) + ZCoor * math.cos(Phi)
            pl().Print(" >>>  Run Px vs. Mv analysis ...")
        else:
            pl().Print(" >>>  Run Px vs. My analysis ...")
        ## Calculate Maximum Axial Forces
        MaxAxial = CalMaxAxialForces.CalSectMaxP()
        MinAxial = CalMinAxialForces.CalSectMinP()
        # self.plogger.Print(" Maximum Axial Load = ".ljust(50,' ') +str(str("%.3f" % (MaxAxial/1000)) + " kN ").rjust(30,' '), 2)
        # self.plogger.Print(" Minimum Axial Load = ".ljust(50, ' ') + str(str("%.3f" % (MinAxial / 1000)) + " kN ").rjust(30, ' '), 2)
        ## ===================================================================================
        ## For Positive axial load
        PosNStep = Model.YieldSurfaceAnalInfo.PosNStep
        NxStep = MaxAxial / PosNStep
        MStep = Model.YieldSurfaceAnalInfo.MStep
        dAng = 2 * math.pi / MStep
        tNumRes = 1  ## Record the number of results data
        # self.Initialize()
        Model.YieldSAnalResults.ResetONxMy()
        ## Record Strain Contorling Type
        tStrnContlType = 0
        if Model.YieldSurfaceAnalInfo.BStrainControl == 0:
            tStrnContlType = 0
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 1:
            tStrnContlType = 1
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 2:
            tStrnContlType = 2
        Model.YieldSAnalResults.PMy_StrnContlType = tStrnContlType
        ## ----------------------------------------------------------------------------------
        ## Angle = PI/2 ##
        for ii in np.arange(PosNStep):
            InNx = MaxAxial - ii * NxStep
            InAngle = math.pi / 2
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_y.setdefault(tNumRes, OutNx)
                Model.YieldSAnalResults.OMy_x.setdefault(tNumRes, OutMy)
                # Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))

        ## ===================================================================================
        ## For negative axial load
        NegNStep = Model.YieldSurfaceAnalInfo.NegNStep
        NxStep = MinAxial / NegNStep
        MStep = Model.YieldSurfaceAnalInfo.MStep
        dAng = 2 * math.pi / MStep
        for ii in np.arange(NegNStep):
            InNx = ii * NxStep
            InAngle = math.pi / 2
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_y.setdefault(tNumRes, OutNx)
                Model.YieldSAnalResults.OMy_x.setdefault(tNumRes, OutMy)
                # Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        ## ---------------------------------------------------------------------------------
        for ii in np.arange(NegNStep):
            InNx = MinAxial - ii * NxStep
            InAngle = 3 * math.pi / 2
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_y.setdefault(tNumRes, OutNx)
                Model.YieldSAnalResults.OMy_x.setdefault(tNumRes, OutMy)
                # Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        ## ---------------------------------------------------------------------------------
        ## for positive load
        NxStep = MaxAxial / PosNStep
        for ii in np.arange(PosNStep + 1):
            InNx = ii * NxStep
            InAngle = 3 * math.pi / 2
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_y.setdefault(tNumRes, OutNx)
                Model.YieldSAnalResults.OMy_x.setdefault(tNumRes, OutMy)
                # Model.YieldSAnalResults.OMz.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        return

    ##
    def CalPlanarYSurfacePMz(self, AxisSlctn):
        # pl().Print(" >>>  Model.YieldSAnalResults.PMz_StrnContlType = ..."+f"{Model.YieldSAnalResults.PMz_StrnContlType}")
        self.Initialize()
        Phi = Model.SectProperty.phi
        # print("Phi = ", Phi)
        ##
        if AxisSlctn == 2:
            for ii in Model.Fiber.FiberID:
                # Model.Fiber.FiberCoorYgo[ii] = Model.Fiber.FiberCoorYgo[ii] - Model.SectProperty.ygc
                # Model.Fiber.FiberCoorZgo[ii] = Model.Fiber.FiberCoorZgo[ii] - Model.SectProperty.zgc
                YCoor = Model.Fiber.FiberCoorYgo[ii]
                ZCoor = Model.Fiber.FiberCoorZgo[ii]
                Model.Fiber.FiberCoorYgo[ii] = - YCoor * math.cos(Phi) + ZCoor * math.sin(Phi)
                Model.Fiber.FiberCoorZgo[ii] = YCoor * math.sin(Phi) + ZCoor * math.cos(Phi)
            pl().Print(" >>>  Run Px vs. Mw analysis ...")
        else:
            pl().Print(" >>>  Run Px vs. Mz analysis ...")
        ##
        ## Calculate Maximum Axial Forces
        MaxAxial = CalMaxAxialForces.CalSectMaxP()
        MinAxial = CalMinAxialForces.CalSectMinP()
        ## ===================================================================================
        ## For Positive axial load
        PosNStep = Model.YieldSurfaceAnalInfo.PosNStep
        NxStep = MaxAxial / PosNStep
        MStep = Model.YieldSurfaceAnalInfo.MStep
        dAng = 2 * math.pi / MStep
        tNumRes = 1  ## Record the number of results data
        # self.Initialize()
        Model.YieldSAnalResults.ResetONxMz()
        ## Record Strain Contorling Type
        tStrnContlType = 0
        if Model.YieldSurfaceAnalInfo.BStrainControl == 0:
            tStrnContlType = 0
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 1:
            tStrnContlType = 1
        elif Model.YieldSurfaceAnalInfo.BStrainControl == 2:
            tStrnContlType = 2
        Model.YieldSAnalResults.PMz_StrnContlType = tStrnContlType
        ##
        ## ----------------------------------------------------------------------------------
        ## Angle = 0.0 ##
        for ii in np.arange(PosNStep):
            InNx = MaxAxial - ii * NxStep
            InAngle = 0.0
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, OutNx)
                # Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))

        ## ===================================================================================
        ## For negative axial load
        NegNStep = Model.YieldSurfaceAnalInfo.NegNStep
        NxStep = MinAxial / NegNStep
        # MStep = Model.YieldSurfaceAnalInfo.MStep
        # dAng = 2 * math.pi / MStep
        ## ----------------------------------------------------------------------------------
        ## Angle = 0.0 ##
        for ii in np.arange(NegNStep):
            InNx = ii * NxStep
            InAngle = 0.0
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, OutNx)
                # Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        ## ----------------------------------------------------------------------------------
        for ii in np.arange(NegNStep):
            InNx = MinAxial - ii * NxStep
            InAngle = math.pi
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, OutNx)
                # Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        ## ----------------------------------------------------------------------------------
        ## for positive load
        NxStep = MaxAxial / PosNStep
        for ii in np.arange(PosNStep + 1):
            InNx = ii * NxStep
            InAngle = math.pi
            IsConvergence = 1
            OutNx, OutMy, OutMz, Dn, IsSubConvergence = self.CalSecCapacity(InNx, InAngle, MaxAxial, MinAxial)
            #
            if IsSubConvergence:
                Model.YieldSAnalResults.ONx_z.setdefault(tNumRes, OutNx)
                # Model.YieldSAnalResults.OMy.setdefault(tNumRes, OutMy)
                Model.YieldSAnalResults.OMz_x.setdefault(tNumRes, OutMz)
                # Model.YieldSAnalResults.ODn.setdefault(tNumRes, Dn)
                # Model.YieldSAnalResults.OAngle.setdefault(tNumRes, InAngle)
            else:
                IsConvergence = 0
            #
            tNumRes += 1
            #
            if IsConvergence:
                # print("Model.YieldSAnalResults.ONx = ", Model.YieldSAnalResults.ONx)
                # # print("Model.YieldSAnalResults.OMy = ", Model.YieldSAnalResults.OMy)
                # print("Model.YieldSAnalResults.OMz = ", Model.YieldSAnalResults.OMz)
                if abs(InNx) < 1e-6: InNx = 0.0
                pl().Print(" >>>  Analysis under axial load = ".ljust(30, ' ') + str(
                    str("%.3f" % (InNx)) + ", Convergence = " + str(bool(IsConvergence))).rjust(48, ' '))
        return

    ##################################### Run function ###############################
    ###################################################################################
    def Run(self):
        tAnalType = Model.YieldSurfaceAnalInfo.SubAnalType
        tAxisSlctn = Model.YieldSurfaceAnalInfo.AxisSlctn
        if tAnalType == 1:
            self.CalFullYSurfacePMyMz(tAxisSlctn)
        if tAnalType == 2:
            self.CalPlanarYSurfacePMy(tAxisSlctn)
        if tAnalType == 3:
            self.CalPlanarYSurfaceMyMz(tAxisSlctn)
        if tAnalType == 4:
            self.CalPlanarYSurfacePMz(tAxisSlctn)
        return
