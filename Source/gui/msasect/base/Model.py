import datetime
import numpy as np
from itertools import zip_longest  # For establishing dictionary
from copy import copy
##
from analysis.FESect.variables.Model import ResetMesh
from analysis.CMSect.variables.Model import YieldSAnalResults


class msaModel:
    # Model information
    class FileInfo:
        FileName = ""

    class Information:
        ModelName = ''
        Version = ''
        Description = ''
        CreatT = ''
        LastSavedT = ''

        # Creat File
        def Create(tModelName: str):
            msaModel.Information.ModelName = tModelName
            msaModel.Information.Version = "Msasect v1.0.0 - Python based Cross-section analysis software"
            CurrentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msaModel.Information.CreatT = CurrentT
            msaModel.Information.LastSavedT = CurrentT

        # Save model
        @classmethod
        def Save(cls):
            CurrentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msaModel.LastSavedT = CurrentT

        # Reset
        @classmethod
        def Reset(cls):
            msaModel.Information.ModelName = ''
            msaModel.Information.Version = ''
            msaModel.Information.Description = ''
            msaModel.Information.CreatT = ''
            msaModel.Information.LastSavedT = ''

    # Material Properties
    class Mat:
        Count = 0
        ID = {}
        E = {}
        G = {}
        Fy = {}
        nu = {}
        Density = {}
        eu = {}
        Color = {}
        ## 20230105: GWL
        Type = {}

        # Add Material
        def Add(tID: int, tE: float, tnu: float, tFy: float, tDensity: float, teu: float, tType: str, tColor: str):
            msaModel.Mat.Count += 1
            msaModel.Mat.ID[tID] = msaModel.Mat.Count - 1
            msaModel.Mat.E[tID] = tE
            msaModel.Mat.nu[tID] = tnu
            msaModel.Mat.Fy[tID] = tFy
            msaModel.Mat.Density[tID] = tDensity
            msaModel.Mat.eu[tID] = teu
            msaModel.Mat.Color[tID] = tColor
            msaModel.Mat.G[tID] = tE / (2.0 * (1.0 + tnu))
            msaModel.Mat.Type[tID] = tType

        # Remove Material
        def Remove(tID: int):
            if msaModel.CheckID(tID, msaModel.Mat.ID) == 0:
                print('Warning! Please input the correct material ID.')
                return
            # msaModel.Mat.ID.remove(tID)
            del msaModel.Mat.ID[tID]
            msaModel.Mat.Count -= 1
            del msaModel.Mat.E[tID]
            del msaModel.Mat.G[tID]
            del msaModel.Mat.Fy[tID]
            del msaModel.Mat.nu[tID]
            del msaModel.Mat.Density[tID]
            del msaModel.Mat.eu[tID]
            del msaModel.Mat.Color[tID]
            del msaModel.Mat.Type[tID]

        # Modify Material
        def Modify(tID: int, tE: float, tnu: float, tFy: float, teu: float, tType: str):
            if msaModel.CheckID(tID, msaModel.Mat.ID) == 0:
                print('Warning! Please input the correct material ID.')
                return
            msaModel.Mat.E[tID] = tE
            msaModel.Mat.nu[tID] = tnu
            msaModel.Mat.Fy[tID] = tFy
            msaModel.Mat.eu[tID] = teu
            msaModel.Mat.Type[tID] = tType
            msaModel.Mat.G[tID] = tE / (2.0 * (1.0 + tnu))

        # Reset Material
        @classmethod
        def Reset(cls):
            msaModel.Mat.Count = 0
            msaModel.Mat.E = {}
            msaModel.Mat.G = {}
            msaModel.Mat.nu = {}
            msaModel.Mat.Fy = {}
            msaModel.Mat.ID = {}
            msaModel.Mat.Density = {}
            msaModel.Mat.eu = {}
            msaModel.Mat.Color = {}
            msaModel.Mat.Type = {}

    class Point:
        Count = 0
        ID = {}
        Yo, Zo = {}, {}  # Coordinate of the point (in Yo-Zo plane)
        xDof, yDof, zDof, qDof = {}, {}, {}, {}
        stress = {}

        # Add Node
        # def Add(tID:int, ty:float, tz:float,txDof:int, tyDof:int, tzDof:int, tqDof:int,tstress:float):
        def Add(tID: int, ty: float, tz: float, tstress: float):
            if msaModel.CheckID(tID, msaModel.Point.ID) == 1:
                print('Please input the correct node ID.')
                return
            msaModel.Point.Count += 1
            # CurrentPointCount = msaModel.Point.Count
            msaModel.Point.ID[tID] = msaModel.Point.Count - 1
            msaModel.Point.Yo[tID] = ty
            msaModel.Point.Zo[tID] = tz
            # msaModel.Point.xDof[tID] = txDof
            # msaModel.Point.yDof[tID] = tyDof
            # msaModel.Point.zDof[tID] = tzDof
            # msaModel.Point.qDof[tID] = tqDof
            msaModel.Point.stress[tID] = tstress

        # Remove Node
        def Remove(tID):
            if msaModel.CheckID(tID, msaModel.Point.ID) == 0:
                print('Warning! Please input the correct node ID.')
                return
            msaModel.Point.Count -= 1
            del msaModel.Point.Yo[tID]
            del msaModel.Point.Zo[tID]
            del msaModel.Point.ID[tID]
            # del msaModel.Point.xDof[tID]
            # del msaModel.Point.yDof[tID]
            # del msaModel.Point.zDof[tID]
            # del msaModel.Point.qDof[tID]
            del msaModel.Point.stress[tID]
            tRemoved_SegmentID = []
            for ii in msaModel.Segment.ID:
                # tSegID = msaModel.Segment.ID[ii]
                if tID == msaModel.Segment.PointI[ii] or tID == msaModel.Segment.PointJ[ii]:
                    tRemoved_SegmentID.append(ii)
            for ii in tRemoved_SegmentID:
                msaModel.Segment.Remove(ii)
            if msaModel.CheckID(tID, msaModel.Point.ID) == 1:
                # msaModel.Point.Remove(tID)
                del msaModel.Point.ID[tID]

        # Modify Node property
        # def Modify(tID:int, ty:float, tz:float,txDof:int, tyDof:int, tzDof:int, tqDof:int,tstress:float):
        def Modify(tID: int, ty: float, tz: float, tstress: float):
            if msaModel.CheckID(tID, msaModel.Point.ID) == 0:
                print('Warning! Please input the correct node ID.')
                return
            msaModel.Point.Yo[tID] = ty
            msaModel.Point.Zo[tID] = tz
            # msaModel.Point.xDof[tID] = txDof
            # msaModel.Point.yDof[tID] = tyDof
            # msaModel.Point.zDof[tID] = tzDof
            # msaModel.Point.qDof[tID] = tqDof
            msaModel.Point.stress[tID] = tstress

        # Reset
        @classmethod
        def Reset(cls):
            msaModel.Point.Count = 0
            msaModel.Point.ID = {}
            msaModel.Point.Yo = {}
            msaModel.Point.Zo = {}
            msaModel.Point.xDof = {}
            msaModel.Point.yDof = {}
            msaModel.Point.zDof = {}
            msaModel.Point.qDof = {}
            msaModel.Point.stress = {}
        ###

    class Segment:
        Count = 0
        ID = {}
        MatID = {}
        PointI = {}
        PointJ = {}
        SegThick = {}
        FiberNumT = {}
        FiberNumL = {}
        NodeNum = {}
        FiberNumL3D = {}
        NodeNum3D = {}

        def __init__(self):
            self.Count = 0
            self.ID = {}
            self.MatID = {}
            self.PointI = {}
            self.PointJ = {}
            self.SegThick = {}
            self.eLen = {}
            self.eArea = {}
            self.wi = {}
            self.wj = {}
            self.Slp = {}
            self.mu = {}
            self.lambdaa = {}
            self.eQyi = {}
            self.eQyj = {}
            self.eQzi = {}
            self.eQzj = {}
            self.FiberNumT = {}
            self.FiberNumL = {}
            self.NodeNum = {}
            self.FiberNumL3D = {}
            self.NodeNum3D = {}

        # Add Segment
        def Add(tID: int, tMaterialID: int, tPSID: int,
                tPEID: int, tSegThick: float):  # PSID and PEID: the indices of segment's start and end points
            if (msaModel.CheckID(tPSID, msaModel.Point.ID) == 0 or msaModel.CheckID(tPEID, msaModel.Point.ID) == 0):
                print('Please input the existing point ID.')
                return
            if msaModel.CheckID(tMaterialID, msaModel.Mat.ID) == 0:
                print("Please input the existing Material ID")
                return
            msaModel.Segment.Count += 1
            msaModel.Segment.ID[tID] = msaModel.Segment.Count - 1
            msaModel.Segment.MatID[tID] = tMaterialID
            msaModel.Segment.PointI[tID] = tPSID
            msaModel.Segment.PointJ[tID] = tPEID
            msaModel.Segment.SegThick[tID] = tSegThick
            msaModel.Segment.FiberNumT[tID] = 0
            msaModel.Segment.FiberNumL[tID] = 0
            msaModel.Segment.NodeNum[tID] = 0
            msaModel.Segment.FiberNumL3D[tID] = 0
            msaModel.Segment.NodeNum3D[tID] = 0

        # Remove member
        def Remove(tID: int):
            if msaModel.CheckID(tID, msaModel.Segment.ID) == 0:
                print('Warning! Please input the correct member ID.')
                return
            msaModel.Segment.Count -= 1
            del msaModel.Segment.MatID[tID]
            del msaModel.Segment.PointI[tID]
            del msaModel.Segment.PointJ[tID]
            del msaModel.Segment.SegThick[tID]
            del msaModel.Segment.FiberNumT[tID]
            del msaModel.Segment.FiberNumL[tID]
            del msaModel.Segment.NodeNum[tID]
            del msaModel.Segment.FiberNumL3D[tID]
            del msaModel.Segment.NodeNum3D[tID]
            del msaModel.Segment.ID[tID]

        # Modify member property
        def Modify(tID: int, tMaterialID: int, tPSID: int, tPEID: int, tSegThick: float):
            if msaModel.CheckID(tID, msaModel.Segment.ID) == 0:
                print('Warning! Please input the correct member ID.')
                return
            msaModel.Segment.MatID[tID] = tMaterialID
            msaModel.Segment.PointI[tID] = tPSID
            msaModel.Segment.PointJ[tID] = tPEID
            msaModel.Segment.SegThick[tID] = tSegThick
            msaModel.Segment.NodeNum[tID] = 0

        # Reset
        @classmethod
        def Reset(cls):
            msaModel.Segment.Count = 0
            msaModel.Segment.ID = {}
            msaModel.Segment.MatID = {}
            msaModel.Segment.PointI = {}
            msaModel.Segment.PointJ = {}
            msaModel.Segment.SegThick = {}
            msaModel.Segment.FiberNumT = {}
            msaModel.Segment.FiberNumL = {}
            msaModel.Segment.NodeNum = {}
            msaModel.Segment.FiberNumL3D = {}
            msaModel.Segment.NodeNum3D = {}

    class YieldSurfaceAnalInfo:
        PosNStep = 50  # P/25
        NegNStep = 50  # -P/25
        MStep = 120  # 360/3
        MaxNumIter = 300
        ConvTol = 0.001
        StrainAtValue = 0.001
        BStrainControl = 0  ## 0: default, Strain reaches ultimate strain;
        ## 1: Strain at the onset of maximum stress;
        ## 2: Strin at the value of

        SubAnalType = 1  ## 1: Full Yield Surfaces (P-My-Mz); 2: Planar Yield Surfaces (P-My or P-Mv);
        ## 3: Planar Yield Surfaces (My-Mz or Mv-Mw); 4: Planar Yield Surfaces (P-Mz or P-Mw);

        AxisSlctn = 1  ## 1: User-defined Axis; 2: Principal Axis

        # SectYSPx = {}
        # SectYSMy = {}
        # SectYSMz = {}
        def InitSectYSurf(self):
            # Initialization
            TotalNumData = (self.PosNStep * 2 + 1) * (self.MStep + 1)
            self.SectYSPx = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
            self.SectYSMy = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
            self.SectYSMz = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
            #
            return

        def AddInfo(self, tLimitStrain: float, tBStrainControl: int, tNumALoad: int, tNumIncldAng: int,
                    tMaxNumIter: int, tConvTol: float):
            msaModel.YieldSurfaceAnalInfo.StrainAtValue = tLimitStrain
            msaModel.YieldSurfaceAnalInfo.BStrainControl = tBStrainControl
            msaModel.YieldSurfaceAnalInfo.PosNStep = tNumALoad
            msaModel.YieldSurfaceAnalInfo.NegNStep = tNumALoad
            msaModel.YieldSurfaceAnalInfo.MStep = tNumIncldAng
            msaModel.YieldSurfaceAnalInfo.MaxNumIter = tMaxNumIter
            msaModel.YieldSurfaceAnalInfo.ConvTol = tConvTol
            return

    class MomentCurvaAnalInfo:
        Anap = 0.0  ## Inputted Axial load
        MomentStep = 36  ## Moment step in analysis
        AxisSlctn = 1  ## 1: Principle axis; 2: Geometric axis;
        SubAnalType = 1  ## 1: Run My Curvature; 2: Run Mz Curvature;
        MaxNumIter = 300
        ConvTol = 0.001
        AxialLoadType = 0  # 0 for absolute value of applied axial load; 1 for percentage of Py

        @classmethod
        def AddInfo(cls, tAnap: float, tLoadType: int, tMomentStep: int, tMaxNumIter: int, tConvTol: float):
            msaModel.MomentCurvaAnalInfo.Anap = tAnap
            msaModel.MomentCurvaAnalInfo.AxialLoadType = tLoadType
            msaModel.MomentCurvaAnalInfo.MomentStep = tMomentStep
            msaModel.MomentCurvaAnalInfo.MaxNumIter = tMaxNumIter
            msaModel.MomentCurvaAnalInfo.ConvTol = tConvTol

    class YieldSAnalResults:
        ONx = dict()
        OMy = dict()  ## My or Mv
        OMz = dict()  ## Mz or Mw
        OAngle = dict()
        ODn = dict()

        # print()

        @classmethod
        def Reset(cls):
            msaModel.YieldSAnalResults.ONx = {}
            msaModel.YieldSAnalResults.OMy = {}
            msaModel.YieldSAnalResults.OMz = {}
            msaModel.YieldSAnalResults.OAngle = {}
            msaModel.YieldSAnalResults.ODn = {}
            ##
            YieldSAnalResults.ONx = {}
            YieldSAnalResults.OMy = {}
            YieldSAnalResults.OMz = {}
            YieldSAnalResults.OAngle = {}
            YieldSAnalResults.ODn = {}

    class Node:
        Count = 0
        ID = {}
        Yo, Zo = {}, {}  # Coordinate of the point (in Yo-Zo plane)

        # Add Node
        def Add(tID: int, ty: float, tz: float):
            msaModel.Node.Count += 1
            # CurrentPointCount = msaModel.Point.Count
            msaModel.Node.ID[tID] = msaModel.Node.Count - 1
            msaModel.Node.Yo[tID] = ty
            msaModel.Node.Zo[tID] = tz

        @classmethod
        # Reset
        def Reset(cls):
            msaModel.Node.Count = 0
            msaModel.Node.ID = {}
            msaModel.Node.Yo = {}
            msaModel.Node.Zo = {}

    class Fiber:
        Count = 0
        ID = {}
        NodeI, NodeJ, NodeK, NodeL = {}, {}, {}, {}
        Yc = {}
        Zc = {}
        FArea = {}
        FMatID = {}

        # Add Fiber
        def Add(tID: int, tNodeI: int, tNodeJ: int, tNodeK: int, tNodeL: int, tFMatID: int):
            msaModel.Fiber.Count += 1
            # CurrentPointCount = msaModel.Point.Count
            msaModel.Fiber.ID[tID] = msaModel.Fiber.Count - 1
            msaModel.Fiber.NodeI[tID] = tNodeI
            msaModel.Fiber.NodeJ[tID] = tNodeJ
            msaModel.Fiber.NodeK[tID] = tNodeK
            msaModel.Fiber.NodeL[tID] = tNodeL
            msaModel.Fiber.FMatID[tID] = tFMatID
            msaModel.Fiber.Yc[tID] = 0
            msaModel.Fiber.Zc[tID] = 0
            msaModel.Fiber.FArea[tID] = 0

        @classmethod
        # Reset
        def Reset(cls):
            msaModel.Fiber.Count = 0
            msaModel.Fiber.ID = {}
            msaModel.Fiber.NodeI = {}
            msaModel.Fiber.NodeJ = {}
            msaModel.Fiber.NodeK = {}
            msaModel.Fiber.NodeL = {}
            msaModel.Fiber.Yc = {}
            msaModel.Fiber.Zc = {}
            msaModel.Fiber.FArea = {}
            msaModel.Fiber.FMatID = {}


    class Node3D:
        Count = 0
        ID = {}
        Yo, Zo = {}, {}  # Coordinate of the point (in Yo-Zo plane)

        # Add Node
        def Add(tID: int, ty: float, tz: float):
            msaModel.Node3D.Count += 1
            # CurrentPointCount = msaModel.Point.Count
            msaModel.Node3D.ID[tID] = msaModel.Node3D.Count - 1
            msaModel.Node3D.Yo[tID] = ty
            msaModel.Node3D.Zo[tID] = tz

        @classmethod
        # Reset
        def Reset(cls):
            msaModel.Node3D.Count = 0
            msaModel.Node3D.ID = {}
            msaModel.Node3D.Yo = {}
            msaModel.Node3D.Zo = {}

    class Fiber3D:
        Count = 0
        ID = {}
        NodeI, NodeJ, NodeK, NodeL = {}, {}, {}, {}
        Yc = {}
        Zc = {}
        FArea = {}
        FMatID = {}

        # Add Fiber
        def Add(tID: int, tNodeI: int, tNodeJ: int, tNodeK: int, tNodeL: int, tFMatID: int):
            msaModel.Fiber3D.Count += 1
            # CurrentPointCount = msaModel.Point.Count
            msaModel.Fiber3D.ID[tID] = msaModel.Fiber3D.Count - 1
            msaModel.Fiber3D.NodeI[tID] = tNodeI
            msaModel.Fiber3D.NodeJ[tID] = tNodeJ
            msaModel.Fiber3D.NodeK[tID] = tNodeK
            msaModel.Fiber3D.NodeL[tID] = tNodeL
            msaModel.Fiber3D.FMatID[tID] = tFMatID
            msaModel.Fiber3D.Yc[tID] = 0
            msaModel.Fiber3D.Zc[tID] = 0
            msaModel.Fiber3D.FArea[tID] = 0

        @classmethod
        # Reset
        def Reset(cls):
            msaModel.Fiber3D.Count = 0
            msaModel.Fiber3D.ID = {}
            msaModel.Fiber3D.NodeI = {}
            msaModel.Fiber3D.NodeJ = {}
            msaModel.Fiber3D.NodeK = {}
            msaModel.Fiber3D.NodeL = {}
            msaModel.Fiber3D.Yc = {}
            msaModel.Fiber3D.Zc = {}
            msaModel.Fiber3D.FArea = {}
            msaModel.Fiber3D.FMatID = {}


    # if tID is an element in tIDList, return 1; else, return 0
    @classmethod
    def ResetAll(cls):
        msaModel.Information.Reset()
        msaModel.Mat.Reset()
        msaModel.Point.Reset()
        msaModel.Segment.Reset()
        msaModel.Node.Reset()
        msaModel.Fiber.Reset()
        msaModel.Node3D.Reset()
        msaModel.Fiber3D.Reset()
        msaModel.YieldSAnalResults.Reset()

    def CheckID(tID, tIDList):
        if tID in tIDList:
            return 1
        else:
            return 0


class msaFEModel:
    # Model information
    class FileInfo:
        FileName = ""

    class Information:
        ModelName = ''
        Version = ''
        Description = ''
        CreatT = ''
        LastSavedT = ''

        # Creat File
        def Create(tModelName: str):
            msaFEModel.Information.ModelName = tModelName
            msaFEModel.Information.Version = "Msasect v1.0.0 - Python based Cross-section analysis software"
            CurrentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msaFEModel.Information.CreatT = CurrentT
            msaFEModel.Information.LastSavedT = CurrentT

        # Save model
        @classmethod
        def Save(cls):
            CurrentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msaFEModel.LastSavedT = CurrentT

        # Reset
        @classmethod
        def Reset(cls):
            msaFEModel.Information.ModelName = ''
            msaFEModel.Information.Version = ''
            msaFEModel.Information.Description = ''
            msaFEModel.Information.CreatT = ''
            msaFEModel.Information.LastSavedT = ''

    # Material Properties
    class Mat:
        Count = 0
        ID = {}
        E = {}
        nu = {}
        G = {}
        Fy = {}
        Density = {}
        eu = {}
        Color = {}
        Type = {}
        #
        Gra = 0
        Gra_ID = {}
        E_ref = {}
        E_begin ={}
        E_end = {}
        Gra_ang = {}
        Gra_law = {}
        Gra_Type = {}
        GColor = {}
        k = {}
        #
        # Add Material
        def Add(tID: int, tE: float, tnu: float, tFy: float, tDensity: float, teu: float, tType: str, tColor: str):
            msaFEModel.Mat.Count += 1
            msaFEModel.Mat.ID[tID] = msaFEModel.Mat.Count - 1
            msaFEModel.Mat.E[tID] = tE
            msaFEModel.Mat.nu[tID] = tnu
            msaFEModel.Mat.Fy[tID] = tFy
            msaFEModel.Mat.Density[tID] = tDensity
            msaFEModel.Mat.eu[tID] = teu
            msaFEModel.Mat.Type[tID] = tType
            msaFEModel.Mat.Color[tID] = tColor
            msaFEModel.Mat.G[tID] = tE / (2.0 * (1.0 + tnu))

        def Add_gra(GID: int, E_ref: float, E_begin: float, E_end: float, Gra_ang: float, Gra_law: int, Gra_Type: int, GColor: str, k: float):
            msaFEModel.Mat.Gra += 1
            msaFEModel.Mat.Gra_ID[GID] = msaFEModel.Mat.Gra - 1
            msaFEModel.Mat.E_ref[GID] = E_ref
            msaFEModel.Mat.E_begin[GID] = E_begin
            msaFEModel.Mat.E_end[GID] = E_end
            msaFEModel.Mat.Gra_ang[GID] = Gra_ang
            msaFEModel.Mat.Gra_law[GID] = Gra_law
            msaFEModel.Mat.Gra_Type[GID] = Gra_Type
            msaFEModel.Mat.GColor[GID] = GColor
            msaFEModel.Mat.k[GID] = k

        # Remove Material
        def Remove(tID: int):
            if msaFEModel.CheckID(tID, msaFEModel.Mat.ID) == 0:
                print('Warning! Please input the correct material ID.')
                return
            del msaFEModel.Mat.ID[tID]
            msaFEModel.Mat.Count -= 1
            del msaFEModel.Mat.E[tID]
            del msaFEModel.Mat.nu[tID]
            del msaFEModel.Mat.Fy[tID]
            del msaFEModel.Mat.Density[tID]
            del msaFEModel.Mat.eu[tID]
            del msaFEModel.Mat.Color[tID]
            del msaFEModel.Mat.Type[tID]

        def Remove_gra(GID: int):
            if msaFEModel.CheckID(GID, msaFEModel.Mat.Gra_ID) == 0:
                print('Warning! Please input the correct grade ID.')
                return
            del msaFEModel.Mat.Gra_ID[GID]
            msaFEModel.Mat.Gra -= 1
            del msaFEModel.Mat.E_ref[GID]
            del msaFEModel.Mat.E_begin[GID]
            del msaFEModel.Mat.E_end[GID]
            del msaFEModel.Mat.Gra_ang[GID]
            del msaFEModel.Mat.Gra_law[GID]
            del msaFEModel.Mat.GColor[GID]

        # Modify Material
        def Modify(tID: int, tE: float, tnu: float, tFy: float, teu: float, tType: str):
            # if msaFEModel.CheckID(tID, msaFEModel.Mat.Gra_ID) == 0:
            #     print('Warning! Please input the correct material ID.')
            #     return
            msaFEModel.Mat.E[tID] = tE
            msaFEModel.Mat.nu[tID] = tnu
            msaFEModel.Mat.Fy[tID] = tFy
            msaFEModel.Mat.eu[tID] = teu
            msaFEModel.Mat.Type[tID] = tType

        def Modify_gra(GID: int, E_ref: float, E_begin: float, E_end: float, Gra_ang: float, Gra_law: int,Gra_Type: int, k: float):
            # if msaFEModel.CheckID(GID, msaFEModel.Mat.ID) == 0:
            #     print('Warning! Please input the correct material ID.')
            #     return
            msaFEModel.Mat.E_ref[GID] = E_ref
            msaFEModel.Mat.E_begin[GID] = E_begin
            msaFEModel.Mat.E_end[GID] = E_end
            msaFEModel.Mat.Gra_ang[GID] = Gra_ang
            msaFEModel.Mat.Gra_law[GID] = Gra_law
            msaFEModel.Mat.Gra_Type[GID] = Gra_Type
            msaFEModel.Mat.k[GID] = k

        # Reset Material
        @classmethod
        def Reset(cls):
            msaFEModel.Mat.Count = 0
            msaFEModel.Mat.E = {}
            msaFEModel.Mat.nu = {}
            msaFEModel.Mat.Fy = {}
            msaFEModel.Mat.ID = {}
            msaFEModel.Mat.Density = {}
            msaFEModel.Mat.eu = {}
            msaFEModel.Mat.Color = {}
            msaFEModel.Mat.Type = {}
            msaFEModel.Mat.Gra = 0
            msaFEModel.Mat.Gra_ID = {}
            msaFEModel.Mat.E_ref = {}
            msaFEModel.Mat.E_begin = {}
            msaFEModel.Mat.E_end = {}
            msaFEModel.Mat.Gra_ang = {}
            msaFEModel.Mat.Gra_law = {}
            msaFEModel.Mat.Gra_Type = {}
            msaFEModel.Mat.GColor = {}
            msaFEModel.Mat.k = {}

    class Point:
        Count = 0
        ID = {}
        Yo, Zo = {}, {}  # Coordinate of the point (in Yo-Zo plane)

        # Add Point
        def Add(tID: int, ty: float, tz: float):
            if msaFEModel.CheckID(tID, msaFEModel.Point.ID) == 1:
                print('Please input the correct node ID.')
                return
            msaFEModel.Point.Count += 1
            msaFEModel.Point.ID[tID] = msaFEModel.Point.Count - 1
            msaFEModel.Point.Yo[tID] = ty
            msaFEModel.Point.Zo[tID] = tz

        # Remove Point
        def Remove(tID):
            if msaFEModel.CheckID(tID, msaFEModel.Point.ID) == 0:
                print('Warning! Please input the correct node ID.')
                return
            msaFEModel.Point.Count -= 1
            del msaFEModel.Point.Yo[tID]
            del msaFEModel.Point.Zo[tID]
            del msaFEModel.Point.ID[tID]
            tRemoved_OutlineID = []
            for ii in msaFEModel.Outline.ID:
                if tID == msaFEModel.Outline.PointI[ii] or tID == msaFEModel.Outline.PointJ[ii]:
                    tRemoved_OutlineID.append(ii)
            for ii in tRemoved_OutlineID:
                msaFEModel.Outline.Remove(ii)
            if msaFEModel.CheckID(tID, msaFEModel.Point.ID) == 1:
                del msaFEModel.Point.ID[tID]

        # Modify Point Property
        def Modify(tID: int, ty: float, tz: float):
            if msaFEModel.CheckID(tID, msaFEModel.Point.ID) == 0:
                print('Warning! Please input the correct node ID.')
                return
            msaFEModel.Point.Yo[tID] = ty
            msaFEModel.Point.Zo[tID] = tz

        # Reset
        @classmethod
        def Reset(cls):
            msaFEModel.Point.Count = 0
            msaFEModel.Point.ID = {}
            msaFEModel.Point.Yo = {}
            msaFEModel.Point.Zo = {}

    class Outline:
        Count = 0
        ID = {}
        GroupID = {}
        LoopID = {}
        Type = {}
        PointI = {}
        PointJ = {}

        def __init__(self):
            self.Count = 0
            self.ID = {}
            self.GroupID = {}
            self.LoopID = {}
            self.Type = {}
            self.PointI = {}
            self.PointJ = {}

        # Add outline
        def Add(tID: int, tGID: int, tType: str, tLID: int, tPSID: int,
                tPEID: int):  # PSID and PEID: the indices of outline's start and end points
            if (msaFEModel.CheckID(tPSID, msaFEModel.Point.ID) == 0 or msaFEModel.CheckID(tPEID,
                                                                                          msaFEModel.Point.ID) == 0):
                print('Please input the existing point ID.')
                return
            msaFEModel.Outline.Count += 1
            msaFEModel.Outline.ID[tID] = msaFEModel.Outline.Count - 1
            msaFEModel.Outline.GroupID[tID] = tGID
            msaFEModel.Outline.LoopID[tID] = tLID
            msaFEModel.Outline.Type[tID] = tType
            msaFEModel.Outline.PointI[tID] = tPSID
            msaFEModel.Outline.PointJ[tID] = tPEID

        # Remove outline
        def Remove(tID: int):
            if msaFEModel.CheckID(tID, msaFEModel.Outline.ID) == 0:
                print('Warning! Please input the correct outline ID.')
                return
            msaFEModel.Outline.Count -= 1
            del msaFEModel.Outline.GroupID[tID]
            del msaFEModel.Outline.LoopID[tID]
            del msaFEModel.Outline.Type[tID]
            del msaFEModel.Outline.PointI[tID]
            del msaFEModel.Outline.PointJ[tID]
            del msaFEModel.Outline.ID[tID]

        # Modify outline property
        def Modify(tID: int, tGID: int, tLID: int, tType: str, tPSID: int, tPEID: int):
            if msaFEModel.CheckID(tID, msaFEModel.Outline.ID) == 0:
                print('Warning! Please input the correct outline ID.')
                return
            msaFEModel.Outline.GroupID[tID] = tGID
            msaFEModel.Outline.LoopID[tID] = tLID
            msaFEModel.Outline.Type[tID] = tType
            msaFEModel.Outline.PointI[tID] = tPSID
            msaFEModel.Outline.PointJ[tID] = tPEID

        # Reset
        @classmethod
        def Reset(cls):
            msaFEModel.Outline.Count = 0
            msaFEModel.Outline.ID = {}
            msaFEModel.Outline.GroupID = {}
            msaFEModel.Outline.LoopID = {}
            msaFEModel.Outline.Type = {}
            msaFEModel.Outline.PointI = {}
            msaFEModel.Outline.PointJ = {}

    class Loop:
        Count = 0
        ID = {}
        PointID = {}
        OutlineID = {}

        def __init__(self):
            self.Count = 0
            self.ID = {}
            self.PointID = {}
            self.OutlineID = {}

        def Add(tID: int, tOID: list):
            msaFEModel.Loop.Count += 1
            msaFEModel.Loop.ID[tID] = msaFEModel.Loop.Count - 1
            msaFEModel.Loop.OutlineID[tID] = tOID
            msaFEModel.GetLoopPointID(tID)

        # Remove loop
        def Remove(tID: int):
            msaFEModel.Loop.Count -= 1
            del msaFEModel.Loop.PointID[tID]
            del msaFEModel.Loop.OutlineID[tID]
            del msaFEModel.Loop.ID[tID]

        # Modify loop property
        def Modify(tID: int, tOID: list):
            msaFEModel.Loop.ID[tID] = tID
            msaFEModel.Loop.OutlineID[tID] = tOID
            msaFEModel.GetLoopPointID(tID)

        # Reset
        @classmethod
        def Reset(cls):
            msaFEModel.Loop.Count = 0
            msaFEModel.Loop.ID = {}
            msaFEModel.Loop.PointID = {}
            msaFEModel.Loop.OutlineID = {}

    class Group:
        Count = 0
        ID = {}
        MatID = {}
        LoopID = {}

        def __init__(self):
            self.Count = 0
            self.ID = {}
            self.MatID = {}
            self.LoopID = {}

        # Add group
        def Add(tID: int, tMID: int, tLID: list):
            if msaFEModel.CheckID(tMID, msaFEModel.Mat.ID) == 0:
                print('Please input the existing material ID.')
                return
            msaFEModel.Group.Count += 1
            msaFEModel.Group.ID[tID] = msaFEModel.Outline.Count - 1
            msaFEModel.Group.MatID[tID] = tMID
            msaFEModel.Group.LoopID[tID] = tLID

        # Remove group
        def Remove(tID: int):
            if msaFEModel.CheckID(tID, msaFEModel.Group.ID) == 0:
                print('Warning! Please select the correct group ID.')
                return
            msaFEModel.Group.Count -= 1
            del msaFEModel.Group.ID[tID]
            del msaFEModel.Group.LoopID[tID]
            del msaFEModel.Group.MatID[tID]

        # Modify group property
        def Modify(tID: int, tMID: int, tLID: list):
            if msaFEModel.CheckID(tID, msaFEModel.Group.ID) == 0:
                print('Warning! Please select the correct group ID.')
                return
            msaFEModel.Group.MatID[tID] = tMID
            msaFEModel.Group.LoopID[tID] = tLID

        # Reset
        @classmethod
        def Reset(cls):
            msaFEModel.Group.Count = 0
            msaFEModel.Group.ID = {}
            msaFEModel.Group.MatID = {}
            msaFEModel.Group.LoopID = {}

    # if tID is an element in tIDList, return 1; else, return 0
    @classmethod
    def ResetAll(cls):
        msaFEModel.Information.Reset()
        msaFEModel.Mat.Reset()
        msaFEModel.Point.Reset()
        msaFEModel.Outline.Reset()
        msaFEModel.Loop.Reset()
        msaFEModel.Group.Reset()
        ResetMesh()

    def CheckID(tID, tIDList):
        if tID in tIDList:
            return 1
        else:
            return 0

    def GetLoopPointID(tID):
        tPointID = []
        tOutlineID = copy(msaFEModel.Loop.OutlineID[tID])
        while tOutlineID:
            for i in tOutlineID:
                if not tPointID:
                    tPointID.append(msaFEModel.Outline.PointI[i])
                    tOutlineID.remove(i)
                else:
                    if tPointID[-1] == msaFEModel.Outline.PointI[i]:
                        tPointID.append(msaFEModel.Outline.PointJ[i])
                        tOutlineID.remove(i)
                    elif tPointID[-1] == msaFEModel.Outline.PointJ[i]:
                        tPointID.append(msaFEModel.Outline.PointI[i])
                        tOutlineID.remove(i)
        msaFEModel.Loop.PointID[tID] = tPointID

    ##
    class YieldSurfaceAnalInfo:
        PosNStep = 50  # P/25
        NegNStep = 50  # -P/25
        MStep = 120  # 360/3
        MaxNumIter = 300
        ConvTol = 0.001
        StrainAtValue = 0.001
        BStrainControl = 0  ## 0: default, Strain reaches ultimate strain;
        ## 1: Strain at the onset of maximum stress;
        ## 2: Strin at the value of

        SubAnalType = 1  ## 1: Full Yield Surfaces (P-My-Mz); 2: Planar Yield Surfaces (P-My or P-Mv);
        ## 3: Planar Yield Surfaces (My-Mz or Mv-Mw); 4: Planar Yield Surfaces (P-Mz or P-Mw);

        AxisSlctn = 1  ## 1: User-defined Axis; 2: Principal Axis

        # SectYSPx = {}
        # SectYSMy = {}
        # SectYSMz = {}
        def InitSectYSurf(self):
            # Initialization
            TotalNumData = (self.PosNStep * 2 + 1) * (self.MStep + 1)
            self.SectYSPx = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
            self.SectYSMy = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
            self.SectYSMz = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
            #
            return

        @staticmethod
        def AddInfo(tLimitStrain: float, tBStrainControl: int, tNumALoad: int, tNumIncldAng: int, tMaxNumIter: int,
                    tConvTol: float):
            msaFEModel.YieldSurfaceAnalInfo.StrainAtValue = tLimitStrain
            msaFEModel.YieldSurfaceAnalInfo.BStrainControl = tBStrainControl
            msaFEModel.YieldSurfaceAnalInfo.PosNStep = tNumALoad
            msaFEModel.YieldSurfaceAnalInfo.NegNStep = tNumALoad
            msaFEModel.YieldSurfaceAnalInfo.MStep = tNumIncldAng
            msaFEModel.YieldSurfaceAnalInfo.MaxNumIter = tMaxNumIter
            msaFEModel.YieldSurfaceAnalInfo.ConvTol = tConvTol
            return

    ##
    class MomentCurvaAnalInfo:
        Anap = 0.0  ## Inputted Axial load
        MomentStep = 36  ## Moment step in analysis
        AxisSlctn = 1  ## 1: Principle axis; 2: Geometric axis;
        SubAnalType = 1  ## 1: Run My Curvature; 2: Run Mz Curvature;
        MaxNumIter = 300
        ConvTol = 0.001
        AxialLoadType = 0  ## 0 for absolute value of applied axial load; 1 for percentage of Py

        @classmethod
        def AddInfo(cls, tAnap: float, tLoadType: int, tMomentStep: int, tMaxNumIter: int, tConvTol: float):
            msaFEModel.MomentCurvaAnalInfo.Anap = tAnap
            msaFEModel.MomentCurvaAnalInfo.AxialLoadType = tLoadType
            msaFEModel.MomentCurvaAnalInfo.MomentStep = tMomentStep
            msaFEModel.MomentCurvaAnalInfo.MaxNumIter = tMaxNumIter
            msaFEModel.MomentCurvaAnalInfo.ConvTol = tConvTol

    class SectPAnalInfo:
        RefMatID = -99999    ## Default: Reference Material ID (user-inputted material properties) - Calculating composite section's elastic section modulus
                             ## Reference Material ID (existed material group) - Calculating composite section's elastic section modulus
        UDE = 200000.0       ## User-inputted Material Young's Modulus
        UDPR = 0.3           ## User-inputted Material Poisson's Ratio
        UDfy = 345           ## User-inputted Material Characteristic Strength, fy
        UDeu = 0.20          ## User-inputted Material Maximum Tensile Strain, eu
        StrnConT = 0         ## Only for elastic section modulus, 0 for Strain at the Onset of Maximum Stress; 1 for Strain at the Value of
        StrnatVal = 0.001    ## User-inputted Maximum Strain
        @classmethod
        def AddInfo(cls, tRefMatID: int, tUDE: float, tUDPR: float, tUDfy: float, tUDeu: float, tStrnConT: int, tStrnatVal: float):
            msaFEModel.SectPAnalInfo.RefMatID = tRefMatID
            msaFEModel.SectPAnalInfo.UDE = tUDE
            msaFEModel.SectPAnalInfo.UDPR = tUDPR
            msaFEModel.SectPAnalInfo.UDfy = tUDfy
            msaFEModel.SectPAnalInfo.UDeu = tUDeu
            msaFEModel.SectPAnalInfo.StrnConT = tStrnConT
            msaFEModel.SectPAnalInfo.StrnatVal = tStrnatVal

    class Fiber:
        Count = 0
        ID = {}
        NodeI, NodeJ, NodeK, NodeL = {}, {}, {}, {}
        Yc = {}
        Zc = {}
        FArea = {}
        FMatID = {}

        # Add Fiber
        def Add(tID: int, tNodeI: int, tNodeJ: int, tNodeK: int, tNodeL: int, tFMatID: int):
            msaModel.Fiber.Count += 1
            # CurrentPointCount = msaModel.Point.Count
            msaModel.Fiber.ID[tID] = msaModel.Fiber.Count - 1
            msaModel.Fiber.NodeI[tID] = tNodeI
            msaModel.Fiber.NodeJ[tID] = tNodeJ
            msaModel.Fiber.NodeK[tID] = tNodeK
            msaModel.Fiber.NodeL[tID] = tNodeL
            msaModel.Fiber.FMatID[tID] = tFMatID
            msaModel.Fiber.Yc[tID] = 0
            msaModel.Fiber.Zc[tID] = 0
            msaModel.Fiber.FArea[tID] = 0


class Status:
    NewFile = 1
    Saved = 0
    Meshed = 0
    SP = 0
    YS = 0
    MC = 0
    res_form = ["e", 4]

    @classmethod
    def Reset(cls):
        Status.NewFile = 1
        Status.Saved = 0
        Status.Meshed = 0
        Status.SP = 0
        Status.YS = 0
        Status.MC = 0


class GlobalBuckling:
    Buckling_data = {}
    Buckling_data1 = {}
    Lamuda_max = 0
    Lamuda_min = 0
    Lateraltorsional_Buckling_Axis = ""

    @classmethod
    def Reset(cls):
        GlobalBuckling.Buckling_data = {}
        GlobalBuckling.Buckling_data1 = {}
        GlobalBuckling.Lamuda_max = 0
        GlobalBuckling.Lamuda_min = 0
        GlobalBuckling.Lateraltorsional_Buckling_Axis = ""
