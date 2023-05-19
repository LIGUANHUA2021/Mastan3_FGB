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
# Function purpose:
# =========================================================================================
# Import standard libraries
from itertools import zip_longest  # For establishing dictionary
import numpy as np
import math


# ==========================================================================================
# Import internal functions

# ==========================================================================================
def initialize():
    ##
    Segment.initialize()
    ##
    return


class Information:
    Version = ""
    EDate = ""
    LastRevised = ""
    Description = ""

    @classmethod
    def ReadModelGenlInfo(self, ModelGenlInfo):
        # print("ModelGenlInfo = ", ModelGenlInfo)
        # ModelGenlInfo = dict(ModelGenlInfo)
        Information.Version = ModelGenlInfo[0, 0]
        Information.EDate = ModelGenlInfo[2, 0]
        Information.LastRevised = ModelGenlInfo[3, 0]
        Information.Description = ModelGenlInfo[4, 0]
        return


class Point:
    Count = 0
    ID = []
    Yo = {}  # Point's coordinate in user-defined (global) axis
    Zo = {}  # Point's coordinate in user-defined (global) axis
    Vo = {}  # Point's coordinate in user-defined (global) axis
    Wo = {}  # Point's coordinate in user-defined (global) axis
    nC = {}  # number of segments connected
    Yc = {}  # Point's coordinate refer to geometry centre in global axis
    Zc = {}  # Point's coordinate refer to geometry centre in global axis
    w = {}  # w coordinate of nodes
    V = {}  # V coordinate refer to geo center in principle axis
    W = {}  # W coordinate refer to geo center in principle axis

    def __init__(self):
        self.Count = 0
        self.ID = {}
        self.Yo = {}
        self.Zo = {}
        self.Vo = {}
        self.Wo = {}
        self.nC = {}
        self.Yc = {}
        self.Zc = {}
        self.w = {}
        self.V = {}
        self.W = {}

    def ReadPoint(self, PointInfo) -> object:
        self.Count = len(PointInfo)
        self.ID = dict(zip_longest(PointInfo[:, 0], np.arange(Point.Count)))
        self.Yo = dict(zip_longest(PointInfo[:, 0], PointInfo[:, 1]))
        self.Zo = dict(zip_longest(PointInfo[:, 0], PointInfo[:, 2]))
        # self.nC = dict(zip_longest(PointInfo[:, 0], PointInfo[:, 3]))
        self.Vo = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        self.Wo = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        self.Yc = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        self.Zc = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        self.w = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        self.V = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        self.W = dict(zip_longest(PointInfo[:, 0], np.zeros(self.Count)))  # Initialization
        return


# --------------------------------------------------------------------------
class Segment:
    Count = 0
    ID = {}
    MatID = {}
    PointI = {}
    PointJ = {}
    SegThick = {}
    eLen = {}
    eArea = {}
    emu = {}
    elambda = {}
    ecy = {}
    ecz = {}
    ecv = {}
    ecw = {}
    eQyg = {}
    eQzg = {}
    eQv = {}
    eQw = {}
    eCorner_y = {}
    eCorner_z = {}
    eCorner_v = {}
    eCorner_w = {}

    def __init__(self):
        self.Count = 0
        self.ID = {}
        self.MatID = {}
        self.PointI = {}
        self.PointJ = {}
        self.SegThick = {}
        self.eLen = {}
        self.eArea = {}
        self.emu = {}
        self.elambda = {}
        self.ecy = {}
        self.ecz = {}
        self.ecv = {}
        self.ecw = {}
        self.eQyg = {}
        self.eQzg = {}
        self.eQv = {}
        self.eQw = {}
        self.wi = {}
        self.wj = {}
        self.Slp = {}
        self.mu = {}
        self.lambdaa = {}
        self.eQyi = {}
        self.eQyj = {}
        self.eQzi = {}
        self.eQzj = {}
        self.eCorner_y = {}
        self.eCorner_z = {}
        self.eCorner_v = {}
        self.eCorner_w = {}

    def ReadSegment(SegmInfo):
        Segment.Count = len(SegmInfo)
        Segment.ID = dict(zip_longest(SegmInfo[:, 0], np.arange(Segment.Count)))
        Segment.MatID = dict(zip_longest(SegmInfo[:, 0], SegmInfo[:, 1]))
        Segment.PointI = dict(zip_longest(SegmInfo[:, 0], SegmInfo[:, 2]))
        Segment.PointJ = dict(zip_longest(SegmInfo[:, 0], SegmInfo[:, 3]))
        Segment.SegThick = dict(zip_longest(SegmInfo[:, 0], SegmInfo[:, 4]))
        # Segment.L0 = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))
        Segment.eLen = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eArea = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.emu = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.elambda = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.ecy = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.ecz = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.ecv = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.ecw = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQyg = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQzg = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQv = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQw = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.wi = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.wj = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.Slp = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.mu = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.lambdaa = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQyi = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQyj = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQzi = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eQzj = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization

        Segment.eCorner_y = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eCorner_z = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eCorner_v = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        Segment.eCorner_w = dict(zip_longest(SegmInfo[:, 0], np.zeros(Segment.Count)))  # Initialization
        return

    @staticmethod
    def initialize():
        ## Get conner point for per segment
        for ii in Segment.ID:
            Segment.GetConnerPoint(ii)
        ## Get centre point and Qy and Qz for per segment based on user-defined axis
        Segment.GeteProp()
        return

    @staticmethod
    def GetConnerPoint(ID):
        y1 = Point.Yo[Segment.PointI[ID]]
        y2 = Point.Yo[Segment.PointJ[ID]]
        z1 = Point.Zo[Segment.PointI[ID]]
        z2 = Point.Zo[Segment.PointJ[ID]]
        Segment.eLen[ID] = math.sqrt((y2 - y1) ** 2 + (z2 - z1) ** 2)
        Segment.eCorner_y[ID] = [y1 - Segment.SegThick[ID] * 0.5 * (z2 - z1) / Segment.eLen[ID],
                                 y1 + Segment.SegThick[ID] * 0.5 * (z2 - z1) / Segment.eLen[ID],
                                 y2 + Segment.SegThick[ID] * 0.5 * (z2 - z1) / Segment.eLen[ID],
                                 y2 - Segment.SegThick[ID] * 0.5 * (z2 - z1) / Segment.eLen[ID]]
        Segment.eCorner_z[ID] = [z1 + Segment.SegThick[ID] * 0.5 * (y2 - y1) / Segment.eLen[ID],
                                 z1 - Segment.SegThick[ID] * 0.5 * (y2 - y1) / Segment.eLen[ID],
                                 z2 - Segment.SegThick[ID] * 0.5 * (y2 - y1) / Segment.eLen[ID],
                                 z2 + Segment.SegThick[ID] * 0.5 * (y2 - y1) / Segment.eLen[ID]]


    ##
    @staticmethod
    def GeteProp():
        for i in Segment.ID:
            Segment.eArea[i] = Segment.eLen[i] * Segment.SegThick[i]
            Segment.ecy[i] = (Point.Yo[Segment.PointI[i]] + Point.Yo[Segment.PointJ[i]]) * 0.5
            Segment.ecz[i] = (Point.Zo[Segment.PointI[i]] + Point.Zo[Segment.PointJ[i]]) * 0.5
            Segment.eQyg[i] = Segment.eArea[i] * Segment.ecz[i]
            Segment.eQzg[i] = Segment.eArea[i] * Segment.ecy[i]

class Material:
    Count = 0
    ID = {}
    E = {}
    G = {}
    nu = {}
    Fy = {}  ## Yield Stress
    MaxTenStrn = {}  ## Maximum tension strain
    MaxComStrn = {}  ## Maximum Compressive strain
    Density = {}
    MatProperty = {}  ## 1 for simple  properties; 2 for advanced properties
    Type = "S"  ## "S" for steel; "C" for concret; "R" for rebar; "UD" for user-defined

    # Epscu = {}
    # StressStrain = {}

    def __init__(self):
        self.Count = 0
        self.ID = {}
        self.E = {}
        self.G = {}
        self.nu = {}
        self.Fy = {}
        self.Density = {}
        self.MaxTenStrn = {}  ## -0.2 for steel -0.12 for concret (Constant parameteries)
        self.MaxComStrn = {}  ## 0.2 for steel 0.12 for concret (Constant parameteries)
        self.MatProperty = {}
        self.Type = "S"
        # self.Epscu = {}
        # self.StressStrain = {}
        return

    def ReadMaterial(MaterialInfo):
        Material.Count = len(MaterialInfo)
        tID = np.fromiter(MaterialInfo[:, 0], int).tolist()
        Material.ID = dict(zip_longest(tID, np.arange(Material.Count)))
        Material.E = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 1], float).tolist()))
        Material.G = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 2], float).tolist()))
        Material.nu = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 3], float).tolist()))
        Material.Fy = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 4], float).tolist()))
        tMaxTenStrn = np.fromiter(MaterialInfo[:, 5], float).tolist()
        # print("tMaxTenStrn = ", tMaxTenStrn)
        # print("type tMaxTenStrn = ", type(tMaxTenStrn))
        tMaxTenStrn = [i*(-1) for i in tMaxTenStrn]
        # print("tMaxTenStrn_2nd = ", tMaxTenStrn)
        Material.MaxTenStrn = dict(zip_longest(tID, tMaxTenStrn))
        # print("Material.MaxTenStrn = ", Material.MaxTenStrn)
        Material.MaxComStrn = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 5], float).tolist()))
        Material.Density = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 6], float).tolist()))
        Material.Type = dict(zip_longest(tID, MaterialInfo[:, 7]))
        Material.MatProperty = dict(zip_longest(tID, [1]*len(MaterialInfo))) ## 1 for simple  properties; 2 for advanced properties
        # print("Material.MatProperty", Material.MatProperty)
        # Material.Epscu = dict(zip_longest(MaterialInfo[:, 0], MaterialInfo[:, 6]))
        # Material.StressStrain = dict(zip_longest(MaterialInfo[:, 0], MaterialInfo[:, 7]))
        # Material.MatType = dict(zip_longest(MaterialInfo[:, 0], MaterialInfo[:, 8]))
        return


class SectProperty:
    Area = 0.0
    Iyy = 0.0
    Izz = 0.0
    Iyz = 0.0
    Ivv = 0.0  # refer to Iyy
    Iww = 0.0  # refer to Izz
    phi = 0.0  # inclined angle
    Qy = 0.0  # Static Moment in user-defined axis
    Qz = 0.0  # Static Moment in user-defined axis
    Qv = 0.0  # Static Moment in Principle axis
    Qw = 0.0  # Static Moment in Principle axis
    J = 0.0  # Torsion Constant
    Cw = 0.0  # Warping Constant
    ysc = 0.0  # shear centre y
    zsc = 0.0  # shear centre z
    vsc = 0.0  # shear centre v
    wsc = 0.0  # shear centre w
    ygc = 0.0  # geometry centre y
    zgc = 0.0  # geometry centre z
    vgc = 0.0  # geometry centre v
    wgc = 0.0  # geometry centre w
    Betay = 0.0  # Wagner coefficient about y-axis
    Betaz = 0.0  # Wagner coefficient about z-axis
    Betav = 0.0  # Wagner coefficient about v-axis
    Betaw = 0.0  # Wagner coefficient about w-axis
    Betaω = 0.0  # Wagner coefficient
    Ayy = 0.0  # Shear Area about y-axis
    Azz = 0.0  # Shear Area about z-axis
    Avv = 0.0  # Shear Area about v-axis
    Aww = 0.0  # Shear Area about w-axis
    Zyy = 0.0  # Plastic section module about y-axis
    Zzz = 0.0  # Plastic section module about z-axis
    Zvv = 0.0  # Plastic section module about v-axis
    Zww = 0.0  # Plastic section module about w-axis
    St = 0.0  # Elastic Torsion Modulus
    Zt = 0.0  # Plastic Torsion Modulus
    Svv = 0.0
    Sww = 0.0
    rv = 0.0
    rw = 0.0
    Syy = 0.0
    Szz = 0.0
    ry = 0.0
    rz = 0.0
    St = 0.0
    Zt = 0.0
    kv = 0.0
    kw = 0.0
    ky = 0.0
    kz = 0.0
    ##
    cyp = 0.0  # Plastic section centre
    czp = 0.0  # Plastic section centre
    cvp = 0.0  # Plastic section centre
    cwp = 0.0  # Plastic section centre

    ## To be continue

    @classmethod
    def Reset(cls):
        SectProperty.Area = 0.0
        SectProperty.Iyy = 0.0
        SectProperty.Izz = 0.0
        SectProperty.Iyz = 0.0
        SectProperty.Ivv = 0.0
        SectProperty.Iww = 0.0
        SectProperty.phi = 0.0
        SectProperty.Qy = 0.0
        SectProperty.Qz = 0.0
        SectProperty.Qv = 0.0
        SectProperty.Qw = 0.0
        SectProperty.J = 0.0
        SectProperty.Cw = 0.0
        SectProperty.ysc = 0.0
        SectProperty.zsc = 0.0
        SectProperty.vsc = 0.0
        SectProperty.wsc = 0.0
        SectProperty.ygc = 0.0
        SectProperty.zgc = 0.0
        SectProperty.vgc = 0.0
        SectProperty.wgc = 0.0
        SectProperty.Betay = 0.0
        SectProperty.Betaz = 0.0
        SectProperty.Betav = 0.0
        SectProperty.Betaw = 0.0
        SectProperty.Betaω = 0.0
        SectProperty.Ayy = 0.0
        SectProperty.Azz = 0.0
        SectProperty.Avv = 0.0
        SectProperty.Aww = 0.0
        SectProperty.Zyy = 0.0
        SectProperty.Zzz = 0.0
        SectProperty.Zvv = 0.0
        SectProperty.Zww = 0.0
        SectProperty.St = 0.0
        SectProperty.Zt = 0.0
        SectProperty.Svv = 0.0
        SectProperty.Sww = 0.0
        SectProperty.rv = 0.0
        SectProperty.rw = 0.0
        SectProperty.Syy = 0.0
        SectProperty.Szz = 0.0
        SectProperty.ry = 0.0
        SectProperty.rz = 0.0
        SectProperty.St = 0.0
        SectProperty.Zt = 0.0
        SectProperty.kv = 0.0
        SectProperty.kw = 0.0
        SectProperty.ky = 0.0
        SectProperty.kz = 0.0
        SectProperty.cyp = 0.0
        SectProperty.czp = 0.0
        SectProperty.cvp = 0.0
        SectProperty.cwp = 0.0

class Fiber:
    FiberCount = 0.0
    FiberID = {}
    FiberCoorY = {}  ## Based on user-defined axis (global)
    FiberCoorZ = {}  ## Based on user-defined axis (global)
    FiberCoorYgo = {}  ## Refer to Geometry center (global)
    FiberCoorZgo = {}  ## Refer to Geometry center (global)
    FiberCoorV = {}  ##
    FiberCoorW = {}  ##
    MaxY = -9999.0   ##
    MinY = 9999.0    ##
    MaxZ = -9999.0   ##
    MinZ = 9999.0    ##
    MaxV = -9999.0   ##
    MinV = 9999.0    ##
    MaxW = -9999.0   ##
    MinW = 9999.0    ##
    FiberArea = {}
    FiberMatID = {}  ## the material type of each fiber
    ##
    # Calculate section yield surface
    Idn_limt = 0.0
    MaxComStr = 0.0
    MaxComV = 0.0
    MaxTenStr = 0.0
    MinTenV = 0.0
    NumAxialLoad = 10
    Dn = 0.0  ## sectional neutral axis position

    def __init__(self):
        self.FiberCount = 0
        self.FiberID = {}
        self.FiberCoorY = {}
        self.FiberCoorZ = {}
        self.FiberCoorYgo = {}
        self.FiberCoorZgo = {}
        self.FiberCoorV = {}
        self.FiberCoorW = {}
        self.FiberArea = {}
        self.FiberMatID = {}
        self.MaxY = -9999.0  ##
        self.MinY = 9999.0  ##
        self.MaxZ = -9999.0  ##
        self.MinZ = 9999.0  ##
        self.MaxV = -9999.0  ##
        self.MinV = 9999.0  ##
        self.MaxW = -9999.0  ##
        self.MinW = 9999.0  ##
        return

    @classmethod
    def ReadFiber(self, FiberInfo):
        # print("FiberInfo = ", FiberInfo)
        # print("FiberInfo Variables type = ", type(FiberInfo))
        if FiberInfo.any():
            self.FiberCount = len(FiberInfo)
            self.FiberID = dict(zip_longest(FiberInfo[:, 0], np.arange(Point.Count)))
            self.FiberCoorY = dict(zip_longest(FiberInfo[:, 0], FiberInfo[:, 1]))
            self.FiberCoorZ = dict(zip_longest(FiberInfo[:, 0], FiberInfo[:, 2]))
            self.FiberArea = dict(zip_longest(FiberInfo[:, 0], FiberInfo[:, 3]))
            self.FiberMatID = dict(zip_longest(FiberInfo[:, 0], FiberInfo[:, 4]))
        return


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

    SubAnalType = 1     ## 1: Full Yield Surfaces (P-My-Mz); 2: Planar Yield Surfaces (P-My or P-Mv);
                        ## 3: Planar Yield Surfaces (My-Mz or Mv-Mw); 4: Planar Yield Surfaces (P-Mz or P-Mw);

    AxisSlctn = 1       ## 1: User-defined Axis; 2: Principal Axis


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

    @classmethod
    def ReadYSurfAnalInfo(self, YSAnalInfo):
        # print("YSAnalInfo = ", YSAnalInfo)
        # print("YSAnalInfo type = ", type(YSAnalInfo))
        # YSAnalInfo = dict(YSAnalInfo)
        # # print("YSAnalInfo = ", YSAnalInfo)
        # # print("YSAnalInfo type = ", type(YSAnalInfo))

        if YSAnalInfo.size != 0:
            YSAnalInfo = dict(zip_longest(YSAnalInfo[:, 0], YSAnalInfo[:, 1]))
            # print("YSAnalInfo = ", YSAnalInfo)
            # print("YSAnalInfo type = ", type(YSAnalInfo))
            self.PosNStep = int(YSAnalInfo.get('PosNStep', 50))
            self.NegNStep = int(YSAnalInfo.get('NegNStep', 50))
            self.MStep = int(YSAnalInfo.get('MomentStep', 120))
            self.MaxNumIter = int(YSAnalInfo.get('MaxNumIter', 300))
            self.ConvTol = float(YSAnalInfo.get('ConvTol', 0.001))
            self.StrainAtValue = float(YSAnalInfo.get('StrainAtValue', 0.001))
            self.BStrainControl = int(YSAnalInfo.get('BStrainControl', 0))
            self.SubAnalType = int(YSAnalInfo.get('SubAnalType', 1))
            self.AxisSlctn = int(YSAnalInfo.get('AxisSlctn', 1))
            # self.NegNStep = int(float(YSAnalInfo[1, 0]))
            # self.MStep = int(float(YSAnalInfo[2, 0]))
            # self.MaxNumIter = int(float(YSAnalInfo[3, 0]))
            # self.ConvTol = float(YSAnalInfo[4, 0])
            # self.StrainAtValue = float(YSAnalInfo[5, 0])
            # self.BStrainControl = int(float(YSAnalInfo[6, 0]))
            # self.SubAnalType = int(float(YSAnalInfo[7, 0]))
            # self.AxisSlctn = int(float(YSAnalInfo[8, 0]))
        return
class YieldSAnalResults:

    ONx = dict()
    OMy = dict() ## My or Mv
    OMz = dict() ## Mz or Mw
    OAngle = dict()
    ODn = dict()
    StrnContlType = 0
    ##
    ONx_y = dict() ## Px vs. My or Px vs. Mv
    OMy_x = dict() ## Px vs. My or Px vs. Mv
    PMy_StrnContlType = 0
    ONx_z = dict()  ## Px vs. Mz or Px vs. Mw
    OMz_x = dict()  ## Px vs. Mz or Px vs. Mw
    PMz_StrnContlType = 0
    ONx_yz = dict()  ## My vs. Mz or Mv vs. Mw
    OMy_z = dict()  ## My vs. Mz or Mv vs. Mw
    OMz_y = dict()  ## My vs. Mz or Mv vs. Mw
    MyMz_StrnContlType = 0

    ## {'P',{'0', val,'1', val},'My',{'0', val,'1', val},'Mz',{'0', val,'1', val}, 'InAngle',{'0', val,'1', val}, 'InAngle',{'0', val,'1', val}}
    @classmethod
    def Reset(cls):
        YieldSAnalResults.ONx = {}
        YieldSAnalResults.OMy = {}
        YieldSAnalResults.OMz = {}
        YieldSAnalResults.OAngle = {}
        YieldSAnalResults.ODn = {}
        YieldSAnalResults.StrnContlType = 0
        ##
    @classmethod
    def ResetONxMy(cls):
        YieldSAnalResults.ONx_y = {}
        YieldSAnalResults.OMy_x = {}
        YieldSAnalResults.PMy_StrnContlType = 0

    @classmethod
    def ResetONxMz(cls):
        YieldSAnalResults.ONx_z = {}
        YieldSAnalResults.OMz_x = {}
        YieldSAnalResults.PMz_StrnContlType = 0

    @classmethod
    def ResetOMyMz(cls):
        YieldSAnalResults.OMy_z = {}
        YieldSAnalResults.OMz_y = {}
        YieldSAnalResults.ONx_yz = {}
        YieldSAnalResults.MyMz_StrnContlType = 0
    @classmethod
    def ResetAllResults(cls):
        YieldSAnalResults.Reset()
        YieldSAnalResults.ResetONxMy()
        YieldSAnalResults.ResetOMyMz()
        YieldSAnalResults.ResetONxMz()


class OutResult:
    FileName = ""
    Folder = ""
    ModelName = ""
    ModelInfo = ""
