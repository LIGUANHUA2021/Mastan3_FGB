import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QPointF
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainterPath, QPen, QBrush, QColor
from PySide6.QtWidgets import QGraphicsPathItem
from gui.msasect.base.Model import msaModel, msaFEModel
from matplotlib.colors import hex2color
from analysis.FESect.variables.Model import Node as MeshNode
from analysis.FESect.variables.Model import Segment as MeshSegment
from analysis.CMSect.variables.Model import SectProperty as CMSP
from analysis.FESect.variables.Result import SectionProperties as FESP


def CenterlinePlot(ViewBox):
    SectPlot = pg.GraphItem()
    ViewBox.addItem(SectPlot)
    ## Define positions of nodes
    PointID = list(msaModel.Point.ID)
    CenterlineID = list(msaModel.Segment.ID)

    if PointID:
        ValidClID = list(msaModel.Segment.ID)
        ValidClCount = msaModel.Segment.Count
        for i in msaModel.Segment.ID:
            if not msaModel.Segment.SegThick[i]:
                ValidClID.remove(i)
                ValidClCount -= 1
        Points = np.zeros((msaModel.Point.Count + ValidClCount * 4, 2))
        for i in range(msaModel.Point.Count):
            Points[i][0] = msaModel.Point.Zo[PointID[i]]
            Points[i][1] = msaModel.Point.Yo[PointID[i]]
        ## Define the set of connections in the graph
        if CenterlineID:
            Lines = np.zeros((msaModel.Segment.Count + ValidClCount * 4, 2), dtype=int)
            LType = np.full(msaModel.Segment.Count + ValidClCount * 4, 1, dtype=[('red', np.ubyte),
                                                                                 ('green', np.ubyte),
                                                                                 ('blue', np.ubyte),
                                                                                 ('alpha', np.ubyte),
                                                                                 ('width', float)])
            for i in range(msaModel.Segment.Count):
                Lines[i][0] = msaModel.Point.ID[msaModel.Segment.PointI[CenterlineID[i]]]
                Lines[i][1] = msaModel.Point.ID[msaModel.Segment.PointJ[CenterlineID[i]]]
                ColorName = hex2color(msaModel.Mat.Color[msaModel.Segment.MatID[CenterlineID[i]]])
                if msaModel.Segment.SegThick[CenterlineID[i]]:
                    LType[i] = (ColorName[0] * 255, ColorName[1] * 255, ColorName[2] * 255, 200, 1)
                else:
                    LType[i] = (ColorName[0] * 255, ColorName[1] * 255, ColorName[2] * 255, 200, 2)
            for i in range(ValidClCount):
                t = msaModel.Segment.SegThick[ValidClID[i]]
                Z1 = Points[msaModel.Point.ID[msaModel.Segment.PointI[ValidClID[i]]]][0]
                Y1 = Points[msaModel.Point.ID[msaModel.Segment.PointI[ValidClID[i]]]][1]
                Z2 = Points[msaModel.Point.ID[msaModel.Segment.PointJ[ValidClID[i]]]][0]
                Y2 = Points[msaModel.Point.ID[msaModel.Segment.PointJ[ValidClID[i]]]][1]
                L = np.sqrt((Z2 - Z1) ** 2 + (Y2 - Y1) ** 2)
                Points[msaModel.Point.Count + i * 4][0] = Z1 + t / 2 / L * (Y2 - Y1)
                Points[msaModel.Point.Count + i * 4][1] = Y1 - t / 2 / L * (Z2 - Z1)
                Points[msaModel.Point.Count + i * 4 + 1][0] = Z1 - t / 2 / L * (Y2 - Y1)
                Points[msaModel.Point.Count + i * 4 + 1][1] = Y1 + t / 2 / L * (Z2 - Z1)
                Points[msaModel.Point.Count + i * 4 + 2][0] = Z2 + t / 2 / L * (Y2 - Y1)
                Points[msaModel.Point.Count + i * 4 + 2][1] = Y2 - t / 2 / L * (Z2 - Z1)
                Points[msaModel.Point.Count + i * 4 + 3][0] = Z2 - t / 2 / L * (Y2 - Y1)
                Points[msaModel.Point.Count + i * 4 + 3][1] = Y2 + t / 2 / L * (Z2 - Z1)
                Lines[msaModel.Segment.Count + i * 4][0] = msaModel.Point.Count + i * 4
                Lines[msaModel.Segment.Count + i * 4][1] = msaModel.Point.Count + i * 4 + 1
                Lines[msaModel.Segment.Count + i * 4 + 1][0] = msaModel.Point.Count + i * 4 + 1
                Lines[msaModel.Segment.Count + i * 4 + 1][1] = msaModel.Point.Count + i * 4 + 3
                Lines[msaModel.Segment.Count + i * 4 + 2][0] = msaModel.Point.Count + i * 4 + 2
                Lines[msaModel.Segment.Count + i * 4 + 2][1] = msaModel.Point.Count + i * 4 + 3
                Lines[msaModel.Segment.Count + i * 4 + 3][0] = msaModel.Point.Count + i * 4
                Lines[msaModel.Segment.Count + i * 4 + 3][1] = msaModel.Point.Count + i * 4 + 2
                ## Define the line style for each connection (this is optional)
                ColorName = hex2color(msaModel.Mat.Color[msaModel.Segment.MatID[ValidClID[i]]])
                LType[msaModel.Segment.Count + i * 4] = LType[msaModel.Segment.Count + i * 4 + 1] =\
                LType[msaModel.Segment.Count + i * 4 + 2] = LType[msaModel.Segment.Count + i * 4 + 3] =\
                (ColorName[0] * 255, ColorName[1] * 255, ColorName[2] * 255, 250, 2)
                FillBorder1 = ViewBox.plot(x=(Points[msaModel.Point.Count + i * 4][0], Points[msaModel.Point.Count + i * 4 + 2][0]),
                                           y=(Points[msaModel.Point.Count + i * 4][1], Points[msaModel.Point.Count + i * 4 + 2][1]), pen=(0, 0, 0, 0))
                FillBorder2 = ViewBox.plot(x=(Points[msaModel.Point.Count + i * 4 + 1][0], Points[msaModel.Point.Count + i * 4 + 3][0]),
                                           y=(Points[msaModel.Point.Count + i * 4 + 1][1], Points[msaModel.Point.Count + i * 4 + 3][1]), pen=(0, 0, 0, 0))
                Filling = pg.FillBetweenItem(FillBorder1, FillBorder2, brush=(ColorName[0] * 255, ColorName[1] * 255, ColorName[2] * 255, 150))
                ViewBox.addItem(Filling)
            ## Update the graph
            SectPlot.setData(pos=Points, adj=Lines, pen=LType,
                             size=[6] * msaModel.Point.Count + [1] * (ValidClCount * 4),
                             symbol=['o'] * (msaModel.Point.Count + ValidClCount * 4), brush=pg.mkColor('r'),
                             pxMode=True)
        else:
            ## Update the graph
            SectPlot.setData(pos=Points, size=6, symbol=['o'] * msaModel.Point.Count, brush=pg.mkColor('r'),
                             pxMode=True)
    return


def OutlinePlot(ViewBox):
    SectPlot = pg.GraphItem()
    ViewBox.addItem(SectPlot)
    ## Define positions of points
    PointID = list(msaFEModel.Point.ID)
    OutlineID = list(msaFEModel.Outline.ID)
    valid_ol_ID = []
    valid_group_ID = []
    for i in msaFEModel.Group.ID:
        ol_type = []
        for j in msaFEModel.Group.LoopID[i]:
            ol_type += [msaFEModel.Outline.Type[k] for k in msaFEModel.Loop.OutlineID[j]]
        if "S" in ol_type:
            for j in msaFEModel.Group.LoopID[i]:
                valid_ol_ID += msaFEModel.Loop.OutlineID[j]
            valid_group_ID += [i]

    if PointID:
        Points = np.zeros((msaFEModel.Point.Count, 2))
        for i in range(msaFEModel.Point.Count):
            Points[i][0] = msaFEModel.Point.Zo[PointID[i]]
            Points[i][1] = msaFEModel.Point.Yo[PointID[i]]
        ## Define the set of connections in the graph
        if OutlineID:
            Lines = np.zeros((msaFEModel.Outline.Count, 2), dtype=int)
            LType = np.full(msaFEModel.Outline.Count, 1, dtype=[('red', np.ubyte),
                                                                ('green', np.ubyte),
                                                                ('blue', np.ubyte),
                                                                ('alpha', np.ubyte),
                                                                ('width', float)])
            for i in range(msaFEModel.Outline.Count):
                if OutlineID[i] in valid_ol_ID:
                    Lines[i][0] = msaFEModel.Point.ID[msaFEModel.Outline.PointI[OutlineID[i]]]
                    Lines[i][1] = msaFEModel.Point.ID[msaFEModel.Outline.PointJ[OutlineID[i]]]
                    ## Define the line style for each connection (this is optional)
                    ColorName = hex2color(msaFEModel.Mat.Color[msaFEModel.Group.MatID[msaFEModel.Outline.GroupID[OutlineID[i]]]])
                    LType[i] = (ColorName[0] * 0,
                                ColorName[1] * 0,
                                ColorName[2] * 0,
                                255, 3)
                ## Update the graph
                SectPlot.setData(pos=Points,
                                 adj=Lines,
                                 pen=LType,
                                 size=6,
                                 symbol=['o'] * msaFEModel.Point.Count,
                                 brush=pg.mkColor('r'),
                                 pxMode=True)
            FillPen = QPen()
            FillPen.setWidth(0)
            FillPen.setBrush(QBrush(QColor(0, 0, 0, 0)))
            for i in msaFEModel.Group.ID:
                if i in valid_group_ID:
                    ColorName = hex2color(msaFEModel.Mat.Color[msaFEModel.Group.MatID[i]])
                    Filling = QGraphicsPathItem()
                    Filling.setBrush(QBrush(QColor(ColorName[0] * 255, ColorName[1] * 255, ColorName[2] * 255, 150)))
                    Filling.setPen(FillPen)
                    FillBorders = QPainterPath()
                    for j in msaFEModel.Group.LoopID[i]:
                        FillBorder = tuple(QPointF(msaFEModel.Point.Zo[tPoint], msaFEModel.Point.Yo[tPoint]) for tPoint in msaFEModel.Loop.PointID[j])
                        FillBorders.addPolygon(FillBorder)
                    Filling.setPath(FillBorders)
                    ViewBox.addItem(Filling)
        else:
            ## Update the graph
            SectPlot.setData(pos=Points,
                             size=6,
                             symbol=['o'] * msaFEModel.Point.Count,
                             brush=pg.mkColor('r'),
                             pxMode=True)
    return


def OriginPlot(ViewBox):
    OrigPlot = pg.GraphItem()
    ViewBox.addItem(OrigPlot)
    OrigPlot.setData(pos=np.zeros((1, 2)), size=5, symbol='o', symbolPen=pg.mkPen('b'), brush=pg.mkColor('b'),
                     pxMode=True)
    return


def MatIDPlot(ViewBox, ClChecked):
    Font = QFont()
    Font.setPointSize(12)
    if ClChecked:
        LineID = msaModel.Segment.ID
        if LineID:
            for i in LineID:
                Label = pg.TargetItem(pos=((msaModel.Point.Zo[msaModel.Segment.PointI[i]] +
                                            msaModel.Point.Zo[msaModel.Segment.PointJ[i]]) / 2,
                                           (msaModel.Point.Yo[msaModel.Segment.PointI[i]] +
                                            msaModel.Point.Yo[msaModel.Segment.PointJ[i]]) / 2),
                                            size=0, symbol='o', pen=pg.mkPen('m'), brush=pg.mkColor('m'),
                                            movable=False, label=str(msaModel.Segment.MatID[i]),
                                            labelOpts={"offset": (2, -7), "color": pg.mkColor('m')})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    else:
        if msaFEModel.Group.ID:
            for i in msaFEModel.Group.ID:
                ZList = [msaFEModel.Point.Zo[msaFEModel.Outline.PointI[j]] for j in msaFEModel.Outline.ID
                         if msaFEModel.Outline.Type[j] == "S" and msaFEModel.Outline.GroupID[j] == i]
                YList = [msaFEModel.Point.Yo[msaFEModel.Outline.PointI[j]] for j in msaFEModel.Outline.ID
                         if msaFEModel.Outline.Type[j] == "S" and msaFEModel.Outline.GroupID[j] == i]
                if ZList:
                    Label = pg.TargetItem(pos=(sum(ZList) / len(ZList), sum(YList) / len(YList)),
                                              size=0, symbol='o', pen=pg.mkPen('m'), brush=pg.mkColor('m'),
                                              movable=False, label=str(msaFEModel.Group.MatID[i]),
                                              labelOpts={"offset": (10, 0), "color": pg.mkColor('m')})
                    Label.label().setFont(Font)
                    ViewBox.addItem(Label)
    return


def PointIDPlot(ViewBox, ClChecked):
    Font = QFont()
    Font.setPointSize(12)
    if ClChecked:
        PointID = msaModel.Point.ID
        if PointID:
            for i in PointID:
                Label = pg.TargetItem(pos=(msaModel.Point.Zo[i], msaModel.Point.Yo[i]), size=0,
                                      symbol='o', pen=pg.mkPen('black'), brush=pg.mkColor('black'),
                                      movable=False, label=str(i),
                                      labelOpts={"offset": (-5, 7), "color": pg.mkColor('black')})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    else:
        PointID = msaFEModel.Point.ID
        if PointID:
            for i in PointID:
                Label = pg.TargetItem(pos=(msaFEModel.Point.Zo[i], msaFEModel.Point.Yo[i]), size=0,
                                      symbol='o', pen=pg.mkPen('black'), brush=pg.mkColor('black'),
                                      movable=False, label=str(i),
                                      labelOpts={"offset": (-5, 7), "color": pg.mkColor('black')})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    return


def LineIDPlot(ViewBox, ClChecked):
    Font = QFont()
    Font.setPointSize(12)
    if ClChecked:
        LineID = msaModel.Segment.ID
        if LineID:
            for i in LineID:
                Label = pg.TargetItem(pos=((msaModel.Point.Zo[msaModel.Segment.PointI[i]] + msaModel.Point.Zo[msaModel.Segment.PointJ[i]]) / 2,
                                           (msaModel.Point.Yo[msaModel.Segment.PointI[i]] + msaModel.Point.Yo[msaModel.Segment.PointJ[i]]) / 2),
                                           size=0, symbol='o', pen=pg.mkPen('r'), brush=pg.mkColor('r'), movable=False,
                                           label=str(i), labelOpts={"offset": (2, 7), "color": pg.mkColor('r')})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    else:
        LoopID = msaFEModel.Loop.ID
        if LoopID:
            for i in LoopID:
                Label = pg.TargetItem(pos=((msaFEModel.Point.Zo[msaFEModel.Loop.PointID[i][0]] + msaFEModel.Point.Zo[msaFEModel.Loop.PointID[i][1]]) / 2,
                                           (msaFEModel.Point.Yo[msaFEModel.Loop.PointID[i][0]] + msaFEModel.Point.Yo[msaFEModel.Loop.PointID[i][1]]) / 2),
                                           size=0, symbol='o', pen=pg.mkPen('r'), brush=pg.mkColor('r'), movable=False,
                                           label=str(i), labelOpts={"offset": (2, 0), "color": pg.mkColor('r')})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    return


def FiberPlot(ViewBox, ClChecked):
    if ClChecked:
        FiberPlot = pg.GraphItem()
        ViewBox.addItem(FiberPlot)
        ## Define positions of points
        NodeID = list(msaModel.Node.ID)
        FiberID = list(msaModel.Fiber.ID)

        if NodeID:
            Points = np.zeros((msaModel.Node.Count, 2))
            for i in range(msaModel.Node.Count):
                Points[i][0] = msaModel.Node.Zo[NodeID[i]]
                Points[i][1] = msaModel.Node.Yo[NodeID[i]]
            ## Define the set of connections in the graph
            if FiberID:
                Lines = np.zeros((msaModel.Fiber.Count * 4, 2), dtype=int)
                LType = np.full(msaModel.Fiber.Count * 4, 1, dtype=[('red', np.ubyte),
                                                                ('green', np.ubyte),
                                                                ('blue', np.ubyte),
                                                                ('alpha', np.ubyte),
                                                                ('width', float)])
                for i in range(msaModel.Fiber.Count):
                    Lines[i * 4][0] = msaModel.Node.ID[msaModel.Fiber.NodeI[FiberID[i]]]
                    Lines[i * 4][1] = msaModel.Node.ID[msaModel.Fiber.NodeJ[FiberID[i]]]
                    Lines[i * 4 + 1][0] = msaModel.Node.ID[msaModel.Fiber.NodeJ[FiberID[i]]]
                    Lines[i * 4 + 1][1] = msaModel.Node.ID[msaModel.Fiber.NodeK[FiberID[i]]]
                    Lines[i * 4 + 2][0] = msaModel.Node.ID[msaModel.Fiber.NodeK[FiberID[i]]]
                    Lines[i * 4 + 2][1] = msaModel.Node.ID[msaModel.Fiber.NodeL[FiberID[i]]]
                    Lines[i * 4 + 3][0] = msaModel.Node.ID[msaModel.Fiber.NodeL[FiberID[i]]]
                    Lines[i * 4 + 3][1] = msaModel.Node.ID[msaModel.Fiber.NodeI[FiberID[i]]]
                for i in range(msaModel.Fiber.Count * 4):
                    LType[i] = (0, 0, 0, 100, 1)
                ## Update the graph
                FiberPlot.setData(pos=Points,
                                  adj=Lines,
                                  pen=LType,
                                  size=0,
                                  symbol=['o'] * msaModel.Node.Count,
                                  brush=pg.mkColor('r'),
                                  pxMode=True)
    else:
        FiberPlot = pg.GraphItem()
        ViewBox.addItem(FiberPlot)
        ## Define positions of points
        NodeID = list(MeshNode.ID)
        FiberID = list(MeshSegment.ID)
        if MeshNode.Count:
            Points = np.zeros((MeshNode.Count, 2))
            for i in range(MeshNode.Count):
                Points[i][0] = MeshNode.Z[NodeID[i]]
                Points[i][1] = MeshNode.Y[NodeID[i]]
            if MeshSegment.Count:
                Lines = np.zeros((MeshSegment.Count, 2), dtype=int)
                LType = np.full(MeshSegment.Count, 1, dtype=[('red', np.ubyte),
                                                             ('green', np.ubyte),
                                                             ('blue', np.ubyte),
                                                             ('alpha', np.ubyte),
                                                             ('width', float)])
                for i in range(MeshSegment.Count):
                    Lines[i][0] = MeshNode.ID[MeshSegment.NodeI[FiberID[i]]]
                    Lines[i][1] = MeshNode.ID[MeshSegment.NodeJ[FiberID[i]]]
                    LType[i] = (0, 0, 0, 100, 2)
                # Update the graph
                FiberPlot.setData(pos=Points, adj=Lines, pen=LType, size=0, symbol=['o'] * MeshNode.Count, brush=pg.mkColor('r'), pxMode=True)


def PAPlot(ViewBox, ClChecked):
    if ClChecked:
        Deg = -np.rad2deg(CMSP.phi)
        GC = QPointF(CMSP.zgc, CMSP.ygc)
    else:
        Deg = np.rad2deg(FESP.Theta)
        GC = QPointF(FESP.cz, FESP.cy)
    PAPen1 = QPen()
    PAPen2 = QPen()
    PAPen1.setStyle(Qt.DashLine)
    PAPen2.setStyle(Qt.DashDotLine)
    PAPen1.setBrush(QBrush(QColor(0, 0, 0, 200)))
    PAPen2.setBrush(QBrush(QColor(0, 0, 0, 200)))
    PAPen1.setWidth(3)
    PAPen2.setWidth(3)
    PAPen1.setCosmetic(True)
    PAPen2.setCosmetic(True)
    PA1 = pg.InfiniteLine(pos=GC, pen=PAPen1, movable=False, angle=Deg)
    PA2 = pg.InfiniteLine(pos=GC, pen=PAPen2, movable=False, angle=Deg + 90)
    ViewBox.addItem(PA1)
    ViewBox.addItem(PA2)


def CoordPlot(ViewBox, ClChecked):
    Font = QFont()
    Font.setPointSize(10)
    if ClChecked:
        PointID = msaModel.Point.ID
        if PointID:
            for i in PointID:
                Label = pg.TargetItem(pos=(msaModel.Point.Zo[i], msaModel.Point.Yo[i]), size=0,
                                      symbol='o', pen=pg.mkPen(0, 255, 255, 150), brush=pg.mkColor(0, 255, 255, 150), movable=False,
                                      label="({:.2f}, {:.2f})".format(msaModel.Point.Yo[i], msaModel.Point.Zo[i]),
                                      labelOpts={"offset": (-5, -7), "color": pg.mkColor(0, 255, 255, 255)})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    else:
        PointID = msaFEModel.Point.ID
        if PointID:
            for i in PointID:
                Label = pg.TargetItem(pos=(msaFEModel.Point.Zo[i], msaFEModel.Point.Yo[i]), size=0,
                                      symbol='o', pen=pg.mkPen(0, 255, 255, 150), brush=pg.mkColor(0, 255, 255, 150), movable=False,
                                      label="({:.2f}, {:.2f})".format(msaFEModel.Point.Yo[i], msaFEModel.Point.Zo[i]),
                                      labelOpts={"offset": (-5, -7), "color": pg.mkColor(0, 255, 255, 255)})
                Label.label().setFont(Font)
                ViewBox.addItem(Label)
    return


def GCPlot(ViewBox, ClChecked):
    GCPlot = pg.GraphItem()
    ViewBox.addItem(GCPlot)
    if ClChecked:
        GC = np.array([[CMSP.zgc, CMSP.ygc]])
    else:
        GC = np.array([[FESP.cz, FESP.cy]])
    GCPlot.setData(pos=GC, size=10, symbol='+', symbolPen=pg.mkPen('w'), brush=pg.mkColor('r'), pxMode=True)


def SCPlot(ViewBox, ClChecked):
    SCPlot = pg.GraphItem()
    ViewBox.addItem(SCPlot)
    if ClChecked:
        SC = np.array([[CMSP.zsc + CMSP.zgc, CMSP.ysc + CMSP.ygc]])
    else:
        SC = np.array([[FESP.czs, FESP.cys]])
    SCPlot.setData(pos=SC, size=10, symbol='x', symbolPen=pg.mkPen('w'), brush=pg.mkColor('b'), pxMode=True)
