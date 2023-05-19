#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
from itertools import zip_longest  # For establishing dictionary
from datetime import datetime
import numpy as np
import math, time

class SystemVariables:
    def __init__(self):
        # Input and output file
        self.FileExisted = False  # File existed or not
        self.sInputFile = ""    # Input file path & name
        self.sInput = 0
        self.sOutputFile = ""   # Output file path & name
        self.sOutput = 0
        self.sReportFile = ""   # Output report file path & name
        self.sReport = 0

class SystemDataSetting:
        # Constant values
        NMATCURVE = 200         # Maximum points of stress vs. strain curve
        NMATMAX = 50            # Maximum number of material inputted
        NCOMMAX = 2000          # Maximum number of component inputted
        NBCLOAD = 1000          # Maximum number of Basic Load inputted
        MAXLAYER = 100          # Maximum number of the layer
        MINLAYER = 10           # Minimum number of the layer
        LAYERLEN = 3            # Maximum length of each layer

class Material:
    # Inputed values
    Count = 0
    ID = {}  # To allocate the mat. to component.
    Name = {}  # Material Name (String)
    MatType = {}  # 1 for steel; 2 for concrete; 3 for rebar;
    MatProperty = {}  # 1 for simple properties; 2 for advanced properties.
    # Simplified properties
    MatSymmetry = {}  # 0 for symmetric, 1 for tension only, 2 for compression only
    E = {}  # Input E value
    PR = {}  # Input Possion's Ratio
    G = {}  # Input G value
    Fc = {}  # Input un-factored designed compressive strength
    Kc = {}  # Input max. compressive strain
    Ft = {}  # Input un-factored designed tensile strength
    Kt = {}  # Input max. tensile strain
    # Advanced properties
    CurNum = 0  # Input number of stress vs strain points
    CurStrain = np.zeros(SystemDataSetting.NMATCURVE, dtype=np.float64)  # Input curve strain
    CurStress = np.zeros(SystemDataSetting.NMATCURVE, dtype=np.float64)  # Input curve stress
    CurZero = 0  # Position of Zero Point
    MaxComStn = {}
    MaxTenStn = {}
    StnAtZero = 0.0
    MatCurveInfo = {}
    # For calculation values
    pc = {}  # Design compressive strength
    pt = {}  # Design tensile strength
    # For concrete only
    iniKc = {}  # Initial yield compressive strain
    kx = {}  # Stress Block Height
    ## ======================================================================================
    # Material Properties
    MaxComStrn = 0.0  # Maximum compressive strain for pure compression
    MaxTenStrn = -0.0  # Maximum Tensile strain for pure tension
    MaxComStr = {}   #
    MaxComV = {}     #
    MaxTenStr = {}   #
    MinTenV = {}     #
    ## ======================================================================================
    def __init__(self):
        # Inputed values
        self.Count = 0
        self.ID = {}             # To allocate the mat. to component.
        self.Name = {}           # Material Name (String)
        self.MatType = {}        # 1 for steel; 2 for concrete; 3 for rebar;
        self.MatProperty = {}    # 1 for simple properties; 2 for advanced properties.
        # Simplified properties
        self.MatSymmetry = {}    # 0 for symmetric, 1 for tension only, 2 for compression only
        self.E = {}              # Input E value
        self.PR = {}             # Input Possion's Ratio
        self.G = {}              # Input G value
        self.Fc = {}             # Input un-factored designed compressive value
        self.Kc = {}             # Input max. compressive strain
        self.Ft = {}             # Input un-factored designed tensile value
        self.Kt = {}             # Input max. tensile strain
        # Advanced properties
        self.CurNum = 0          # Input number of stress vs strain points
        self.CurStrain = np.zeros(SystemDataSetting.NMATCURVE, dtype=np.float64)  # Input curve strain
        self.CurStress = np.zeros(SystemDataSetting.NMATCURVE, dtype=np.float64)  # Input curve stress
        self.CurZero = 0         # Position of Zero Point
        self.MatCurveInfo = {}
        self.MaxComStn = {}
        self.MaxTenStn = {}
        self.StnAtZero = 0.0
        # For calculation values
        self.pc = {}             # Design compressive strength
        self.pt = {}             # Design tensile strength
        # For concrete only
        self.iniKc = {}          # Initial yield compressive strain
        self.kx = {}             # Stress Block Height

        # Material Properties
        ## ======================================================================================
        self.MaxComStrn = 0.0     # Maximum compressive strain for pure compression
        self.MaxTenStrn = -0.0     # Maximum Tensile strain for pure tension
        self.MaxComStr = {}      #
        self.MaxComV = {}        #
        self.MaxTenStr = {}      #
        self.MinTenV = {}        #
        ## ======================================================================================

    @classmethod
    def ReadMaterial(self, MaterialInfo, tAnalFlag=1):
        # print("MaterialInfo = ", MaterialInfo)
        self.Count = len(MaterialInfo)
        tID = np.fromiter(MaterialInfo[:, 0], int).tolist()
        self.ID = dict(zip_longest(tID, np.arange(len(MaterialInfo))))
        self.Name = dict(zip_longest(tID, MaterialInfo[:, 1]))
        self.MatType = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 2], int).tolist()))
        self.MatProperty = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 3], int).tolist()))
        self.MatSymmetry = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 4], int).tolist()))
        self.E = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 5], float).tolist()))
        self.PR = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 6], float).tolist()))
        self.G = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 7], float).tolist()))
        self.Fc = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 8], float).tolist()))
        self.Kc = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 9], float).tolist()))
        self.Ft = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 10], float).tolist()))
        self.Kt = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 11], float).tolist()))
        self.MatCurveInfo = dict(zip_longest(tID, MaterialInfo[:, 12]))
        if tAnalFlag == 1:
            print("Read Material Successfully")

class GlobalViariables:
    Idn_limt = 0.0
    MaxComStrn = 0.0  # The maximum compressive strain for pure compression of the entire section,
                      # taking into account all constituent materials. (min(Kc1,Kc2,,,))
    MaxTenStrn = 0.0  # The maximum compressive strain for pure tension of the entire section,
                      # taking into account all constituent materials. (max(Kt1,Kt2,,,))
    MaxComStr = 0.0   #
    MaxComV = 0.0     #
    MaxTenStr = 0.0   #
    MinTenV = 0.0     #

class Section:
    SecD = 0.0  # Depth of the section
    SecB = 0.0  # Width of the section
    SecMinY = 0.0  # Min. Y-coordinate of the section
    SecMaxY = 0.0  # Max. Y-coordinate of the section
    SecMaxZ = 0.0  # Max. Z-coordinate of the section
    SecMinZ = 0.0  # Min. Z-coordinate of the section

    SecTotalArea = 0.0  # Total area of the section
    SecConcArea = 0.0  # Total area of the concrete
    SecSteelArea = 0.0  # Total area of the steel
    SecSteelRatio = 0.0  # Area ratio of the steel
    SecRebarArea = 0.0  # Total area of the rebar
    SecRebarRatio = 0.0  # Area ratio of the rebar

    gcy = 0.0  # Geometrical centroid of y
    gcz = 0.0  # Geometrical centroid of z
    pcy = 0.0  # Plastic centroid of y
    pcz = 0.0  # Plastic centroid of z

    Iy = 0.0   # Whole section Iy
    Iz = 0.0   # Whole section Iz
    Iyz = 0.0  # Whole section Iyz
    Phi = 0.0  # The inclined angle between the geometrical axis and the principal axis.

    MaxAxial = 0.0  # Maximum axial force, compressive force
    MinAxial = 0.0  # Minimum axial force, tensile force
    def __init__(self):
        self.SecD = 0.0          # Depth of the section
        self.SecB = 0.0          # Width of the section
        self.SecMinY = 0.0       # Min. Y-coordinate of the section
        self.SecMaxY = 0.0       # Max. Y-coordinate of the section
        self.SecMaxZ = 0.0       # Max. Z-coordinate of the section
        self.SecMinZ = 0.0       # Min. Z-coordinate of the section

        self.SecTotalArea = 0.0   # Total area of the section
        self.SecConcArea = 0.0    # Total area of the concrete
        self.SecSteelArea = 0.0   # Total area of the steel
        self.SecSteelRatio = 0.0  # Area ratio of the steel
        self.SecRebarArea = 0.0   # Total area of the rebar
        self.SecRebarRatio = 0.0  # Area ratio of the rebar

        self.gcy = 0.0  # Geometrical centroid of y
        self.gcz = 0.0  # Geometrical centroid of z
        self.pcy = 0.0  # Plastic centroid of y
        self.pcz = 0.0  # Plastic centroid of z

        self.Iy = 0.0  # Whole section Iy
        self.Iz = 0.0  # Whole section Iz
        self.Iyz = 0.0  # Whole section Iyz
        self.Phi = 0.0  # The inclined angle between the geometrical axis and the principal axis.

        self.MaxAxial = 0.0  # Maximum axial force, compressive force
        self.MinAxial = 0.0  # Minimum axial force, tensile force

class Component:
    ID = {}    # Input component ID.
    Name = {}  # Component Name
    Area = {}  # Component Area
    cy = {}    # y-coordinate of geometrical centroid
    cz = {}    # z-coordinate of geometrical centroid
    Iy = {}    # Component Iy
    Iz = {}    # Component Iz
    Iyz = {}   # Component Iyz
    ComType = {}  # 1 for steel component; 2 for concrete component; 3 for rebar component.
    SteelType = {}  # 0 for other materials; 1 for Rolled Section; 2 for Frabricated Section; 3 for Cold-formed Section.
    MatID = {}  # Material ID for component
    # For modeling residual stress
    AlpStrs = 0.0  # Range from -1.0 to +1.0
    NExtPt = 0.0  # Number of external points
    # self.ExtPoints = []     # To store external points
    NOptPt = 0.0  # Number of opening points
    # self.OpPoints = []      # To store opening points
    NFibers = 0.0  # Number of fibers
    Fibers = []  # To store fibers
    # For internal use
    MaxY = {}  # Maximum coordinate of Y
    MinY = {}  # Minimum coordinate of Y
    MaxZ = {}  # Maximum coordinate of Z
    MinZ = {}  # Minimum coordinate of Z
    MaxV = {}  # Maximum coordinate of V
    MinV = {}  # Minimum coordinate of V
    MaxW = {}  # Maximum coordinate of U
    MinW = {}  # Minimum coordinate of U
    NumOpening = 0.0  # Number of opening part(s)
    Openings = []  # To store opening part(s)
    ##
    CompFibersInfo = {}  # Every component fibers are store here
    def __init__(self):
        self.ID = {}           # Input component ID.
        self.Name = {}         # Component Name
        self.Area = {}         # Component Area
        self.cy = {}           # y-coordinate of geometrical centroid
        self.cz = {}           # z-coordinate of geometrical centroid
        self.Iy = {}           # Component Iy
        self.Iz = {}           # Component Iz
        self.ComType = {}      # 1 for steel component; 2 for concrete component; 3 for rebar component.
        self.SteelType = {}    # 0 for other materials; 1 for Rolled Section; 2 for Frabricated Section; 3 for Cold-formed Section.
        self.MatID = {}        # Material ID for component
        # For modeling residual stress
        self.AlpStrs = 0.0       # Range from -1.0 to +1.0
        self.NExtPt = 0.0        # Number of external points
        #self.ExtPoints = []     # To store external points
        self.NOptPt = 0.0        # Number of opening points
        #self.OpPoints = []      # To store opening points
        self.NFibers = 0.0       # Number of fibers
        self.Fibers = []         # To store fibers
        # For internal use
        self.MaxY = {}           # Maximum coordinate of Y
        self.MinY = {}           # Minimum coordinate of Y
        self.MaxZ = {}           # Maximum coordinate of Z
        self.MinZ = {}           # Minimum coordinate of Z
        self.MaxV = {}           # Maximum coordinate of V
        self.MinV = {}           # Minimum coordinate of V
        self.MaxW = {}           # Maximum coordinate of U
        self.MinW = {}           # Minimum coordinate of U
        self.NumOpening = 0.0    # Number of opening part(s)
        self.Openings = []       # To store opening part(s)
        ##
        self.CompFibersInfo = {}  # Every component fibers, external points and opening points are store here

    @classmethod
    def ReadComponent(self, ComponentInfo, tAnalFlag=1):
        #print("ComponentInfo = ", ComponentInfo)
        self.Count = len(ComponentInfo)
        tID = np.fromiter(ComponentInfo[:, 0], int).tolist()
        self.ID = dict(zip_longest(tID, np.arange(len(ComponentInfo))))
        self.Name = dict(zip_longest(tID, ComponentInfo[:, 1]))
        # self.Area = dict(zip_longest(tID, np.fromiter(ComponentInfo[:, 2], float).tolist()))
        # self.Iy = dict(zip_longest(tID, np.fromiter(ComponentInfo[:, 3], float).tolist()))
        # self.Iz = dict(zip_longest(tID, np.fromiter(ComponentInfo[:, 4], float).tolist()))
        self.ComType = dict(zip_longest(tID, np.fromiter(ComponentInfo[:, 2], int).tolist()))
        self.MatID = dict(zip_longest(tID, np.fromiter(ComponentInfo[:, 3], int).tolist()))
        self.CompFibersInfo = dict(zip_longest(tID, ComponentInfo[:, 4]))
        ##
        self.Area = dict(zip_longest(tID, [0.0]*len(ComponentInfo)))
        self.Iy = dict(zip_longest(tID, [0.0]*len(ComponentInfo)))
        self.Iz = dict(zip_longest(tID, [0.0]*len(ComponentInfo)))
        self.cy = dict(zip_longest(tID, [0.0]*len(ComponentInfo)))
        self.cz = dict(zip_longest(tID, [0.0]*len(ComponentInfo)))
        ##
        if tAnalFlag == 1:
            print("Read Component Successfully")
        return

class Results:
    def __init__(self):
        self.dn = 0.0         # Neutral axis height
        self.an = 0.0         # Rotational angle
        self.Nx = 0.0         # Axial force
        self.My = 0.0         # My Bending Moments
        self.Mz = 0.0         # Mz Bending Moments

class GeneralInfo:

        temString = ''   # Input string
        StrTitle = ''    # Title of the command
        StrContent = ''  # Content of the command
        OutText = ''     # For output temp text

        # Control Output
        KOUT = 0  # 6 to print on screen

        # GENERAL
        Version = 0.0       # Version Number
        Unit = ""           # Unit, Default = N,mm
        # ProjectName = ''    # Project Name
        # ProjectNubmer = ''  # Project Number
        ModelFileName = ''    # The Name of created model
        SectionName = ''    # Section Name
        Engineer = ''       # Engineer Name

        SectionType = 0     # Section Type, 1 - Column, 2 - Wall, 3 - Beam

        Codes = 0           # Old, Reserved only, 0 - HK CoPSC 2004 (2nd), 1 - BS 8110 - 1997,
                                 # 2 - EuroCode 2, 3 - GB 50010 - 2002
        SteelCode = 0       # Steel Code,
                                 #             = 10	AISC 360-10:2010;
                                 #             = 20	BS 5950-1:2000;
                                 #             = 30	GB 50017: 2003;
                                 #             = 40	BS EN 1993-1-1:2005;
                                 #             = 50	CoPSC 2011.
        ConcreteCode = 0    # Concrete Code,
                                 #             = 10	ACI 318-05:2005;
                                 #             = 20	BS 8110-1:1997;
                                 #             = 30	GB50010:2010;
                                 #             = 40	BS EN 1992-1-1:2004;
                                 #             = 50	CoPCC 2004.
        CompositeCode = 0   # Composite Code,
                                 #             = 10	ACI 318-05:2005;
                                 #             = 20	BS 8110-1:1997;
                                 #             = 30	DL T5085:1999;
                                 #             = 40	BS EN 1992-1-1:2004;
                                 #             = 50	CoPSC 2011.

        AggrateSize = 0.0   # Max. AggrateSize for Concrete

        OutputControl = 10   # 1 for 10% of the output data
                             # 10 for 100% of the output data

        # Output Control Setting
        NAXIAL = 100        # Maximum count of axial load
        NANGEL = 240        # Maximum count of angel
        AxialStep = 0       # Current axial step according to the output control
        PosNStep = 25       # Positive axial load steps
        NegNStep = 25       # Negative axial load steps
        MomentStep = 36     # Current moment step according to the output control
        Dn = 0              # Neutral axis depth
        NStep = 0           # NStep
        Counter = 0         # Counter for iteration
        bConvergence = 0    # Converged or not
        bRun_Analysis = 0   # Analysis right or not
        Iter = 0            # Number of iteration
        CurN = 0            # Current Axial Force
        CurMx = 0           # Current moment
        CurMy = 0           # Current moment
        CurAngle = 0        # Current angle
        Idn = 0
        Idn_limt = 0
        tDn = 0
        TN = 0
        TMx = 0
        TMy = 0
        TMz = 0

        @classmethod
        def ReadGenlInfo(self, ModelGenlInfo, tAnalFlag=1):
            ## For testing
            self.Version = ModelGenlInfo[0, 1]
            self.Unit = ModelGenlInfo[1, 1]
            self.ModelFileName = ModelGenlInfo[2, 1]
            self.SectionName = ModelGenlInfo[3, 1]
            self.SectionType = ModelGenlInfo[4, 1]
            if tAnalFlag == 1:
                print("Read General Information Successfully")
            # self.Engineer = ModelGenlInfo[5, 1]

            # self.SteelCode = ModelGenlInfo[7, 1]
            # self.ConcreteCode = ModelGenlInfo[8, 1]
            # self.CompositeCode = ModelGenlInfo[9, 1]
            # self.AggrateSize = ModelGenlInfo[10, 1]
            # self.OutputControl = ModelGenlInfo[11, 1]

class AnalysisInfo:
    AnalysisName = ""      # Name for analysis case
    MaxIter = 0            # Maximum iteration times
    CurMaxIter = 0         # Maximum iteration times, current value
    ConvergenceTor = 0.0   # Convergence for iteration
    AnaType = 0            # 0 - Full yield surface, 1 - My vs. Mz Curve, 2 - Nx vs. My Curve, 3 - Nx vs. Mz Curve, 100 - ULS Check, 200 - SLS Check
    RunType = 0            # 0 for ULS, 1 for SLS
    CurveType = 0          # 0 for full diagram, 1 for half diagram, only valid for symmetric section
    NumP = 0               # Number of axial loads for analysis
    AxisSlctn = 0          # 0 for Geometrical axis, 1 for Principle axis
    AxialStep = 0          # Axial load step = Positive axial load steps = Negative axial load steps
    MomentStep = 0         # Current moment step according to the output control
    StrnContType = 0       ## 0 - the fracture/ultimate strain. (Ultimate Status); 1 - the strain at the oneset of maximum stress. (Elastic-Boundary Status);
                           ## 2 - (Inputted by user for GUI or datafile) - float the strain at the value of xxxx (valiad for all materials)

    StrnatVal = 0.001      ## float the strain at the value of xxxx (valiad for all materials)
    Anap = np.array([])    # Inputted axial load uased for moment curventure analysis (* It is a list variable, can be inputted from GUI or import by user *)
    AxialLoadType = 0      ## 0 for absolute value of applied axial load; 1 for percentage of Py
    RefMatID = -99999
    UDE = 200000.0
    UDPR = 0.3
    UDfy = 345
    UDeu = 0.20
    ## Material reaches
    ##* the fracture/ultimate strain. (Ultimate Status)
    ##* the strain at the oneset of maximum stress. (Elastic-Boundary Status)
    ##* the strain at the value of xxxx (valiad for all materials)

    def __init__(self):
        self.AnalysisName = ""     # Name for analysis case
        self.MaxIter = 0           # Maximum iteration times
        self.CurMaxIter = 0        # Maximum iteration times, current value
        self.ConvergenceTor = 0.0  # Convergence for iteration
        self.AnaType = 0           # 0 - Full yield surface, 1 - My vs. Mz Curve, 2 - Nx vs. My Curve, 3 - Nx vs. Mz Curve, 100 - ULS Check, 200 - SLS Check
        self.RunType = 0           # 0 for ULS, 1 for SLS
        self.CurveType = 0         # 0 for full diagram, 1 for half diagram, only valid for symmetric section
        self.NumP = 0              # Number of axial loads for analysis
        self.AxisSlctn = 0         # 0 for Geometrical axis, 1 for Principle axis
        self.AxialStep = 0         # Axial load step = Positive axial load steps = Negative axial load steps
        self.MomentStep = 0        # Current moment step according to the output control
        self.StrnContType = 0      # 0 - the fracture/ultimate strain. (Ultimate Status); 1 - the strain at the oneset of maximum stress. (Elastic-Boundary Status);
                                   # 0.002 (Inputted by user for GUI or datafile) - float the strain at the value of xxxx (valiad for all materials)
        self.StrnatVal = 0.001
        self.Anap = np.array([])
        self.AxialLoadType = 0     # 0 for absolute value of applied axial load; 1 for percentage of Py
        ##
        self.RefMatID = -99999     # Default: Reference Material ID (user-inputted material properties) - Calculating composite section's elastic section modulus
                                   # Reference Material ID (existed material group) - Calculating composite section's elastic section modulus
        self.UDE = 200000.0        ## User-inputted Material Young's Modulus
        self.UDPR = 0.3            ## User-inputted Material Poisson's Ratio
        self.UDfy = 345            ## User-inputted Material Characteristic Strength, fy
        self.UDeu = 0.20           ## User-inputted Material Maximum Tensile Strain, eu

    @classmethod
    def ReadAnalysisInfo(self, AnalysisInfo, tAnalFlag=1):
        ## For testing
        # print("AnalysisInfo = ", AnalysisInfo)
        AnalInfo = dict(zip_longest(AnalysisInfo[:, 0], AnalysisInfo[:, 1]))
        # self.AnalysisName = AnalysisInfo[0, 1]
        self.AnalysisName = AnalInfo.get("AnaName", "My Curvature")
        # self.MaxIter = int(AnalysisInfo[1, 1])
        self.MaxIter = int(AnalInfo.get("AnaIterTimes", 300))
        # self.ConvergenceTor = float(AnalysisInfo[2, 1])
        self.ConvergenceTor = float(AnalInfo.get("AnaConver", 0.001))
        #self.AnaType = int(AnalysisInfo[3, 1]) ##np.fromiter(AnalysisInfo[3, 1], int)
        # self.AnaType = AnalysisInfo[3, 1]  ##np.fromiter(AnalysisInfo[3, 1], int)
        self.AnaType = AnalInfo.get("AnaType", "My Curvature")
        # self.RunType = np.fromiter(AnalysisInfo[4, 1], int)
        self.RunType = int(AnalInfo.get("RunType", 0))
        # self.CurveType = np.fromiter(AnalysisInfo[5, 1], int)
        self.CurveType = int(AnalInfo.get("CurveType", 0))
        # self.AxisSlctn = np.fromiter(AnalysisInfo[6, 1], int)
        self.AxisSlctn = int(AnalInfo.get("AxisSlctn", 1))
        # self.AxialStep = int(AnalysisInfo[7, 1])                 ## np.fromiter(AnalysisInfo[7, 1], int)
        self.AxialStep = int(AnalInfo.get("AxialStep", 20))
        # self.MomentStep = int(AnalysisInfo[8, 1])                ## np.fromiter(AnalysisInfo[8, 1], int)
        self.MomentStep = int(AnalInfo.get("MomentStep", 100))
        # self.StainControl = np.fromiter(AnalysisInfo[9, 1], int)
        self.StrnContType = int(AnalInfo.get("StrainControlType", 0))
        self.Strnatval = float(AnalInfo.get("StrainatValue", 0.001))
        # self.Anap = float(AnalysisInfo[10, 1])
        self.Anap = float(AnalInfo.get("AnalysisAxialLoad", 0.0))
        # self.AxialLoadType = int(AnalysisInfo[11, 1])
        self.AxialLoadType = int(AnalInfo.get("AnalAxialLoadType", 0))
        ##
        self.RefMatID = int(AnalInfo.get('RefMatID', -99999))  ## AnalInfo.get('Control Node', 2)
        self.UDE = float(AnalInfo.get("User-Defined_E", 200000.0))
        # self.UDPR = float(AnalysisInfo[14, 1])
        self.UDPR = float(AnalInfo.get("User-Defined_PR", 0.3))
        # self.UDfy = float(AnalysisInfo[15, 1])
        self.UDfy = float(AnalInfo.get("User-Defined_fy", 345.0))
        # self.UDeu = float(AnalysisInfo[16, 1])
        self.UDeu = float(AnalInfo.get("User-Defined_eu", 0.15))
        if tAnalFlag == 1:
            print("Read Analysis Information Successfuly")


class YieldSAnalResults:

    ONx = dict()
    OMy = dict() ## My or Mv
    OMz = dict() ## Mz or Mw
    OAngle = dict()
    ODn = dict()
    ##
    ONx_y = dict() ## Px vs. My or Px vs. Mv
    OMy_x = dict() ## Px vs. My or Px vs. Mv
    ONx_z = dict()  ## Px vs. Mz or Px vs. Mw
    OMz_x = dict()  ## Px vs. Mz or Px vs. Mw
    ONx_yz = dict()  ## My vs. Mz or Mv vs. Mw
    OMy_z = dict()  ## My vs. Mz or Mv vs. Mw
    OMz_y = dict()  ## My vs. Mz or Mv vs. Mw
    ## {'P',{'0', val,'1', val},'My',{'0', val,'1', val},'Mz',{'0', val,'1', val}, 'InAngle',{'0', val,'1', val}, 'ODn',{'0', val,'1', val}}
    @classmethod
    # Reset
    def Reset(cls):
        YieldSAnalResults.ONx = {}
        YieldSAnalResults.OMy = {}
        YieldSAnalResults.OMz = {}
        YieldSAnalResults.OAngle = {}
        YieldSAnalResults.ODn = {}
        ##
        YieldSAnalResults.ONx_y = {}
        YieldSAnalResults.OMy_x = {}
        YieldSAnalResults.ONx_z = {}
        YieldSAnalResults.OMz_x = {}
        YieldSAnalResults.OMy_z = {}
        YieldSAnalResults.OMz_y = {}

class MomentCurvatureResults:
    ONx_y = dict()  ##
    Oan_y = dict()  ##
    OMy_y = dict()  ##
    OMz_y = dict()  ##
    Idn_y = dict()  ##
    OutStrn_y = dict()  ##
    OutStrs_y = dict()  ##
    ##
    ONx_z = dict()  ##
    Oan_z = dict()  ##
    OMy_z = dict()  ##
    OMz_z = dict()  ##
    Idn_z = dict()  ##
    OutStrn_z = dict()  ##
    OutStrs_z = dict()  ##
    @classmethod
    def ResetMyCurva(cls):
        MomentCurvatureResults.ONx_y = {}
        MomentCurvatureResults.Oan_y = {}
        MomentCurvatureResults.OMy_y = {}
        MomentCurvatureResults.OMz_y = {}
        MomentCurvatureResults.Idn_y = {}
        MomentCurvatureResults.OutStrn_y = {}
        MomentCurvatureResults.OutStrs_y = {}
        ##
    @classmethod
    def ResetMzCurva(cls):
        MomentCurvatureResults.ONx_z = {}
        MomentCurvatureResults.Oan_z = {}
        MomentCurvatureResults.OMz_z = {}
        MomentCurvatureResults.OMy_z = {}
        MomentCurvatureResults.Idn_z = {}
        MomentCurvatureResults.OutStrn_z = {}
        MomentCurvatureResults.OutStrs_z = {}

class CompositeSectionModulus:
    Zyy = 0.0
    Zzz = 0.0
    Syy = 0.0
    Szz = 0.0
    Zvv = 0.0
    Zww = 0.0
    Svv = 0.0
    Sww = 0.0
    @classmethod
    def ResetCompSectMod(cls):
        CompositeSectionModulus.Zyy = 0.0
        CompositeSectionModulus.Zzz = 0.0
        CompositeSectionModulus.Syy = 0.0
        CompositeSectionModulus.Szz = 0.0
        CompositeSectionModulus.Zvv = 0.0
        CompositeSectionModulus.Zww = 0.0
        CompositeSectionModulus.Svv = 0.0
        CompositeSectionModulus.Sww = 0.0





class OutResult:
    FileName = ""
    Folder = ""
    ModelName = ""
    ModelInfo = ""