from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QAction
import sys

def iniMenu(self):
    # popup view of file
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    main_menu = self.menuBar()
    fileMenu = main_menu.addMenu("File")

    Info_SoftwereAction = QAction(QIcon('images/Info_Softwere.png'), "Info", self)
    fileMenu.addAction(Info_SoftwereAction)

    OpenAction = QAction(QIcon('images/Open.png'), "Open ...", self)
    fileMenu.addAction(OpenAction)

    fileMenu.addSeparator()

    saveAction = QAction(QIcon('images/save.png'), "Save", self)
    saveAction.setShortcut("Ctrl+S")
    fileMenu.addAction(saveAction)

    saveasAction = QAction(QIcon('images/save as.png'), "Save As ...", self)
    saveAction.setShortcut("Ctrl+Shift+S")
    fileMenu.addAction(saveasAction)

    fileMenu.addSeparator()

    newAction = QAction(QIcon('images/new.png'), "New", self)
    newAction.setShortcut("Ctrl+N")
    fileMenu.addAction(newAction)

    fileMenu.addSeparator()

    DeftitleAction = QAction(QIcon('images/DefineTitle.png'), "Define Title", self)
    fileMenu.addAction(DeftitleAction)

    fileMenu.addSeparator()

    #PrintPhotoAction = QAction(QIcon('images/PrintPhoto.png'), "Print Photo ...", self)
    #fileMenu.addAction(PrintPhotoAction)

    # File submenu - Print Photo ...
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    PrintPhotoMenu = fileMenu.addMenu("Print Photo ...")

    ToPrinterAction = QAction("To Printer ...", self)
    PrintPhotoMenu.addAction(ToPrinterAction)

    ToFile_TiffAction = QAction("To File (tiff) ...", self)
    PrintPhotoMenu.addAction(ToFile_TiffAction)

    ToFile_pdfAction = QAction("To File (pdf) ...", self)
    PrintPhotoMenu.addAction(ToFile_pdfAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    fileMenu.addSeparator()

    CreateReportAction = QAction(QIcon('images/CreateReport.png'), "Create Report ...", self)
    fileMenu.addAction(CreateReportAction)

    #copyAction = QAction(QIcon('images/copy.png'), "Copy", self)
    #copyAction.setShortcut("Ctrl+C")
    #fileMenu.addAction(copyAction)

    quitAction = QAction(QIcon('images/quit.png'), "Quit", self)
    quitAction.triggered.connect(self.close_window)
    fileMenu.addAction(quitAction)
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # popup view of View
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # main_menu = self.menuBar()
    viewMenu = main_menu.addMenu("View")

    DynamicZoomAction = QAction(QIcon('images/Dynamic_Zoom.png'), "Dynamic Zoom", self)
    DynamicZoomAction.setShortcut("Ctrl+Z")
    viewMenu.addAction(DynamicZoomAction)

    DynamicRotateAction = QAction(QIcon('images/Dynamic_Rotate.png'), "Dynamic Rotate", self)
    DynamicRotateAction.setShortcut("Ctrl+R")
    viewMenu.addAction(DynamicRotateAction)

    DynamicPanAction = QAction(QIcon('images/Dynamic_Pan.png'), "Dynamic Pan", self)
    DynamicPanAction.setShortcut("Ctrl+P")
    viewMenu.addAction(DynamicPanAction)

    viewMenu.addSeparator()

    ZoomBoxAction = QAction(QIcon('images/Zoom_Box.png'), "Zoom Box", self)
    viewMenu.addAction(ZoomBoxAction)

    CenterAction = QAction(QIcon('images/Center.png'), "Center", self)
    viewMenu.addAction(CenterAction)

    FitAction = QAction(QIcon('images/Fit.png'), "Fit", self)
    FitAction.setShortcut("Ctrl+F")
    viewMenu.addAction(FitAction)

    PanorZoomAction = QAction(QIcon('images/Pan_or_Zoom.png'), "Pan / Zoom", self)
    viewMenu.addAction(PanorZoomAction)

    RotateAction = QAction(QIcon('images/Rotate.png'), "Rotate", self)
    viewMenu.addAction(RotateAction)

    viewMenu.addSeparator()

    #DefineViewAction = QAction(QIcon('images/Define_View.png'), "Define View", self)
    #viewMenu.addAction(DefineViewAction)

    # Define View submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    DefineViewmenu = viewMenu.addMenu("Define View")
    FrontviewAction = QAction("Front view:x-y", self)
    DefineViewmenu.addAction(FrontviewAction)

    DefineViewmenu.addSeparator()

    SideviewAction = QAction("Side view:x-y", self)
    DefineViewmenu.addAction(SideviewAction)

    DefineViewmenu.addSeparator()

    TopviewAction = QAction("Top view:x-y", self)
    DefineViewmenu.addAction(TopviewAction)

    DefineViewmenu.addSeparator()

    IsometricviewAction = QAction("Isometric view:x-y-z", self)
    DefineViewmenu.addAction(IsometricviewAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    #LabelsAction = QAction(QIcon('images/Labels.png'), "Labels", self)
    #viewMenu.addAction(LabelsAction)

    # Labels submenu
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Labelsmenu = viewMenu.addMenu("Labels")
    AxisAction = QAction("Axis", self)
    Labelsmenu.addAction(AxisAction)

    Labelsmenu.addSeparator()

    NumNodeAction = QAction("Node #s", self)
    Labelsmenu.addAction(NumNodeAction)

    Labelsmenu.addSeparator()

    NumElementAction = QAction("Element #s", self)
    Labelsmenu.addAction(NumElementAction)

    Labelsmenu.addSeparator()

    EleLocalAxesAction = QAction("Element local x'-y'-z' axes", self)
    Labelsmenu.addAction(EleLocalAxesAction)

    Labelsmenu.addSeparator()

    EleConnectionsAction = QAction("Element Connections", self)
    Labelsmenu.addAction(EleConnectionsAction)

    Labelsmenu.addSeparator()

    LoadsAction = QAction("Loads", self)
    Labelsmenu.addAction(LoadsAction)

    Labelsmenu.addSeparator()

    FixitiesAction = QAction("Fixities", self)
    Labelsmenu.addAction(FixitiesAction)

    Labelsmenu.addSeparator()

    SettlementsAction = QAction("Settlements", self)
    Labelsmenu.addAction(SettlementsAction)

    Labelsmenu.addSeparator()

    ScaleAction = QAction("Scale Actions (S,M,L,XL)", self)
    Labelsmenu.addAction(ScaleAction)

    Labelsmenu.addSeparator()

    DiaValuesAction = QAction("Diagram Values", self)
    Labelsmenu.addAction(DiaValuesAction)

    Labelsmenu.addSeparator()

    UndeflectedGeoAction = QAction("Undeflected Geometry", self)
    Labelsmenu.addAction(UndeflectedGeoAction)

    #FrontviewAction = QAction("Front view:x-y", self)
    #viewMenu.addAction(FrontviewAction)

    RestackObjectsAction = QAction(QIcon('images/Restack_Objects.png'), "Restack Objects", self)
    viewMenu.addAction(RestackObjectsAction)

    DisplaySettingsAction = QAction(QIcon('images/Display_Settings.png'), "Display Settings", self)
    viewMenu.addAction(DisplaySettingsAction)
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # popup view of Geometry
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    GeometryMenu = main_menu.addMenu("Geometry")

    DefNodeAction = QAction(QIcon('images/DefNode.png'), "Define Node", self)
    GeometryMenu.addAction(DefNodeAction)

    MovNodesAction = QAction(QIcon('images/MovNodes.png'), "Move Node(s)", self)
    GeometryMenu.addAction(MovNodesAction)

    ScaNodesAction = QAction(QIcon('images/ScaNode.png'), "Scale Node(s)", self)
    GeometryMenu.addAction(ScaNodesAction)

    DuplNodesAction = QAction(QIcon('images/DupNodes.png'), "Duplicate Node(s)", self)
    GeometryMenu.addAction(DuplNodesAction)

    RemovNodesAction = QAction(QIcon('images/RemovNodesAction.png'), "Remove Node(s)", self)
    GeometryMenu.addAction(RemovNodesAction)

    MerNodesAction = QAction(QIcon('images/MerNodesAction.png'), "Merge Node(s)", self)
    GeometryMenu.addAction(MerNodesAction)

    RenumNodesAction = QAction(QIcon('images/RenumNodesAction.png'), "Renumber Nodes", self)
    GeometryMenu.addAction(RenumNodesAction)

    GeometryMenu.addSeparator()

    DefElementAction = QAction(QIcon('images/DefElementAction.png'), "Define Element", self)
    GeometryMenu.addAction(DefElementAction)

    ExtrElementAction = QAction(QIcon('images/ExtrElementAction.png'), "Extrude Element", self)
    GeometryMenu.addAction(ExtrElementAction)

    DuplElementAction = QAction(QIcon('images/DuplElementAction.png'), "Duplicate Element(s)", self)
    GeometryMenu.addAction(DuplElementAction)

    RemovElementAction = QAction(QIcon('images/RemovElementAction.png'), "Remove Element(s)", self)
    GeometryMenu.addAction(RemovElementAction)

    SubdivElementAction = QAction(QIcon('images/SubdivElementAction.png'), "Subdivide Element(s)", self)
    GeometryMenu.addAction(SubdivElementAction)

    ReoriElementAction = QAction(QIcon('images/ReoriElementAction.png'), "Re-orient Element(s)", self)
    GeometryMenu.addAction(ReoriElementAction)

    RenumElementAction = QAction(QIcon('images/RenumElementAction.png'), "Renumber Element(s)", self)
    GeometryMenu.addAction(RenumElementAction)

    GeometryMenu.addSeparator()

    # Define Connections submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    DefConnectionsMenu = GeometryMenu.addMenu("Define Connections")

    FlexureConnectAction = QAction("Flexure", self)
    DefConnectionsMenu.addAction(FlexureConnectAction)

    DefConnectionsMenu.addSeparator()

    TorsionConnectAction = QAction("Torsion", self)
    DefConnectionsMenu.addAction(TorsionConnectAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    DefFrameAction = QAction(QIcon('images/DefFrameAction.png'), "Define Frame", self)
    GeometryMenu.addAction(DefFrameAction)

    InputGeoAction = QAction(QIcon('images/InputGeoAction.png'), "Input Geometry", self)
    GeometryMenu.addAction(InputGeoAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    GeometryMenu.addSeparator()

    # Information-Geometry submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    InfoGeomMenu = GeometryMenu.addMenu("Information")

    NodeInfoAction = QAction("Node", self)
    InfoGeomMenu.addAction(NodeInfoAction)

    InfoGeomMenu.addSeparator()

    EleInfoAction = QAction("Element", self)
    InfoGeomMenu.addAction(EleInfoAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # popup view of Properties
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    PropertiesMenu = main_menu.addMenu("Properties")

    DefSectAction = QAction(QIcon('images/DefSectAction.png'), "Define Section", self)
    PropertiesMenu.addAction(DefSectAction)

    ModSectAction = QAction(QIcon('images/ModSectAction.png'), "Modify Section", self)
    PropertiesMenu.addAction(ModSectAction)

    RemovSectAction = QAction(QIcon('images/RemovSectAction.png'), "Remove Section", self)
    PropertiesMenu.addAction(RemovSectAction)

    AttachSectAction = QAction(QIcon('images/AttachSectAction.png'), "Attach Section", self)
    PropertiesMenu.addAction(AttachSectAction)

    PropertiesMenu.addSeparator()

    YdSurfControlAction = QAction(QIcon('images/YdSurfControlAction.png'), "Yield Surface Control", self)
    PropertiesMenu.addAction(YdSurfControlAction)

    PropertiesMenu.addSeparator()

    DefMatAction = QAction(QIcon('images/DefMatAction.png'), "Define Material", self)
    PropertiesMenu.addAction(DefMatAction)

    RemovMatAction = QAction(QIcon('images/RemovMatAction.png'), "Remove Material", self)
    PropertiesMenu.addAction(RemovMatAction)

    AttachMatAction = QAction(QIcon('images/AttachMatAction.png'), "Attach Material", self)
    PropertiesMenu.addAction(AttachMatAction)

    PropertiesMenu.addSeparator()

    InputPropAction = QAction(QIcon('images/InputPropAction.png'), "Input Properties", self)
    PropertiesMenu.addAction(InputPropAction)

    PropertiesMenu.addSeparator()

    # Information-Properties submenu
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    InfoPropMenu = PropertiesMenu.addMenu("Information")

    SectInfoAction = QAction("Section", self)
    InfoPropMenu.addAction(SectInfoAction)

    InfoPropMenu.addSeparator()

    MatInfoAction = QAction("Material", self)
    InfoPropMenu.addAction(MatInfoAction)
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # popup view of Conditions
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ConditionsMenu = main_menu.addMenu("Conditions")

    DefFixitiesAction = QAction(QIcon('images/DefFixitiesAction.png'), "Define Fixities", self)
    ConditionsMenu.addAction(DefFixitiesAction)

    ConditionsMenu.addSeparator()

    DefForcesAction = QAction(QIcon('images/DefForcesAction.png'), "Define Forces", self)
    ConditionsMenu.addAction(DefForcesAction)

    DefMomentsAction = QAction(QIcon('images/DefMomentsAction.png'), "Define Moments", self)
    ConditionsMenu.addAction(DefMomentsAction)

    ConditionsMenu.addSeparator()

    DefUnifLoadAction = QAction(QIcon('images/DefUnifLoadAction.png'), "Define Uniform Loads", self)
    ConditionsMenu.addAction(DefUnifLoadAction)

    ConditionsMenu.addSeparator()

    InpLoadsAction = QAction(QIcon('images/DefUnifLoadAction.png'), "Input Loads", self)
    ConditionsMenu.addAction(InpLoadsAction)

    ConditionsMenu.addSeparator()

    PrescribeDispAction = QAction(QIcon('images/PrescribeDispAction.png'), "Prescribe Displacements", self)
    ConditionsMenu.addAction(PrescribeDispAction)

    PrescribeRotaAction = QAction(QIcon('images/PrescribeRotaAction.png'), "Prescribe Rotations", self)
    ConditionsMenu.addAction(PrescribeRotaAction)

    ConditionsMenu.addSeparator()

    DefTempEffectsAction = QAction(QIcon('images/DefTempEffectsAction.png'), "Define Temperature Effects", self)
    ConditionsMenu.addAction(DefTempEffectsAction)

    ConditionsMenu.addSeparator()

    DefTimeHistoryFunAction = QAction(QIcon('images/DefTimeHistoryFunAction.png'), "Define Time-History Function", self)
    ConditionsMenu.addAction(DefTimeHistoryFunAction)

    # popup view of Analysis
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    AnalysisMenu = main_menu.addMenu("Analysis")

    # Analysis-Static submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    StaticMenu = AnalysisMenu.addMenu("Static")

    Mas_1elAction = QAction("1st-Order Elastic", self)
    StaticMenu.addAction(Mas_1elAction)

    Mas_2elAction = QAction("2nd-Order Elastic", self)
    StaticMenu.addAction(Mas_2elAction)\

    Mas_1inAction = QAction("1st-Order Inelastic", self)
    StaticMenu.addAction(Mas_1inAction)

    Mas_2inAction = QAction("2nd-Order Inelastic", self)
    StaticMenu.addAction(Mas_2inAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # Analysis-Eigen_Buckling submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    EigenBucklingMenu = AnalysisMenu.addMenu("Eigen-Buckling")

    Mas_eclAction = QAction("Elastic Critical Load", self)
    EigenBucklingMenu.addAction(Mas_eclAction)

    Mas_ineclAction = QAction("Inelastic Critical Load", self)
    EigenBucklingMenu.addAction(Mas_ineclAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # Analysis-Modal submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    ModalMenu = AnalysisMenu.addMenu("Modal")

    Mas_npAction = QAction("Natural Period", self)
    ModalMenu.addAction(Mas_npAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # Analysis-Time_History submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    TimeHisMenu = AnalysisMenu.addMenu("Time-History")

    Mas_1dyAction = QAction("1st-Order Elastic", self)
    TimeHisMenu.addAction(Mas_1dyAction)

    Mas_2dyAction = QAction("2nd-Order Elastic", self)
    TimeHisMenu.addAction(Mas_2dyAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # Analysis-User Defined submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    UserDefMenu = AnalysisMenu.addMenu("User Defined")

    Mas_UDef_1elAction = QAction("1st-Order Elastic", self)
    UserDefMenu.addAction(Mas_UDef_1elAction)

    Mas_UDef_2elAction = QAction("2nd-Order Elastic", self)
    UserDefMenu.addAction(Mas_UDef_2elAction)

    Mas_UDef_1inAction = QAction("1st-Order inelastic", self)
    UserDefMenu.addAction(Mas_UDef_1inAction)

    Mas_UDef_2inAction = QAction("2nd-Order inelastic", self)
    UserDefMenu.addAction(Mas_UDef_2inAction)

    UserDefMenu.addSeparator()

    Mas_UDef_eclAction = QAction("Elastic Critical Load", self)
    UserDefMenu.addAction(Mas_UDef_eclAction)

    Mas_UDef_ineclAction = QAction("Inelastic Critical Load", self)
    UserDefMenu.addAction(Mas_UDef_ineclAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # popup view of Results
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ResultsMenu = main_menu.addMenu("Results")

    # Results-Diagrams submenu
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    DiagramsMenu = ResultsMenu.addMenu("Diagrams")

    NoneAction = QAction("None", self)
    DiagramsMenu.addAction(NoneAction)

    DiagramsMenu.addSeparator()

    DeflectedShapeAction = QAction("Deflected Shape", self)
    DiagramsMenu.addAction(DeflectedShapeAction)

    DiagramsMenu.addSeparator()

    AxialForcePAction = QAction("Axial Force P", self)
    DiagramsMenu.addAction(AxialForcePAction)

    ShearForceVyAction = QAction("Shear Force Vy", self)
    DiagramsMenu.addAction(ShearForceVyAction)

    ShearForceVzAction = QAction("Shear Force Vz", self)
    DiagramsMenu.addAction(ShearForceVzAction)

    DiagramsMenu.addSeparator()

    TorqueTAction = QAction("Torque T", self)
    DiagramsMenu.addAction(TorqueTAction)

    MomentMyAction = QAction("Moment My", self)
    DiagramsMenu.addAction(MomentMyAction)

    MomentMzAction = QAction("Moment Mz", self)
    DiagramsMenu.addAction(MomentMzAction)

    BimomentBAction = QAction("Bimoment B", self)
    DiagramsMenu.addAction(BimomentBAction)

    DiagramsMenu.addSeparator()

    NormRespIncrAction = QAction("Norm Resp Incr", self)
    DiagramsMenu.addAction(NormRespIncrAction)

    DiagramsMenu.addSeparator()

    ViewKffAction = QAction("View [Kff]", self)
    DiagramsMenu.addAction(ViewKffAction)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    NodeDispAction = QAction(QIcon('images/NodeDispAction.png'), "Node Displacements", self)
    ResultsMenu.addAction(NodeDispAction)

    NodeReactAction = QAction(QIcon('images/NodeReactAction.png'), "Node Reactions", self)
    ResultsMenu.addAction(NodeReactAction)

    NodeVeloAction = QAction(QIcon('images/NodeVeloAction.png'), "Node Velocity", self)
    ResultsMenu.addAction(NodeVeloAction)

    NodeAccAction = QAction(QIcon('images/NodeAccAction.png'), "Node Acceleration", self)
    ResultsMenu.addAction(NodeAccAction)

    ResultsMenu.addSeparator()

    ElementForcAction = QAction(QIcon('images/ElementForcAction.png'), "Element Forces", self)
    ResultsMenu.addAction(ElementForcAction)

    PlaDeformationsAction = QAction(QIcon('images/PlaDeformationsAction.png'), "Plastic Deformations", self)
    ResultsMenu.addAction(PlaDeformationsAction)

    ResultsMenu.addSeparator()

    UpdateGeomAction = QAction(QIcon('images/UpdateGeomAction.png'), "Update Geometry", self)
    ResultsMenu.addAction(UpdateGeomAction)

    ResultsMenu.addSeparator()

    MSAPlotAction = QAction(QIcon('images/MSAPlotAction.png'), "MSAPlot", self)
    ResultsMenu.addAction(MSAPlotAction)

    ResultsMenu.addSeparator()

    EraseResAction = QAction(QIcon('images/EraseResAction.png'), "Erase Results", self)
    ResultsMenu.addAction(EraseResAction)
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%