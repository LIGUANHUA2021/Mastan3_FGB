import numpy as np
import gui.gui_function.gui_setting as gui_setting
import gui.mastan3.base.models as model
import pyqtgraph.opengl as gl

def PlotArrow_x(w,NodeID: int,length: float):
    if length == 0:
        return
    Arrowcolor = gui_setting.gui_setting.LoadColor
    Linewidth = gui_setting.gui_setting.LineWidth
    ArrowSize = gui_setting.gui_setting.ArrowSize
    NodeLocation = np.empty(3)
    tx,ty,tz = model.msaModel.Node.x[NodeID], model.msaModel.Node.y[NodeID], model.msaModel.Node.z[NodeID]
    NodeLocation = [tx,ty,tz]
    xz_Arrow = np.empty((3,3))
    xz_Arrow[0] = [tx - ArrowSize, ty, tz - ArrowSize / 2]
    xz_Arrow[1] = [tx - ArrowSize/3, ty, tz]
    xz_Arrow[2] = [tx - ArrowSize, ty, tz + ArrowSize / 2]
    if length < 0:
        xz_Arrow[0] = [tx + ArrowSize, ty, tz - ArrowSize / 2]
        xz_Arrow[1] = [tx + ArrowSize / 3, ty, tz]
        xz_Arrow[2] = [tx + ArrowSize, ty, tz + ArrowSize / 2]
    PlotArrowHead(w,NodeLocation,xz_Arrow,Arrowcolor,Linewidth)
    xy_Arrow = np.empty((3,3))
    xy_Arrow[0] = [tx - ArrowSize, ty - ArrowSize / 2, tz]
    xy_Arrow[1] = [tx - ArrowSize / 3, ty, tz]
    xy_Arrow[2] = [tx - ArrowSize, ty + ArrowSize / 2, tz]
    if length < 0:
        xy_Arrow[0] = [tx + ArrowSize, ty - ArrowSize / 2, tz]
        xy_Arrow[1] = [tx + ArrowSize / 3, ty, tz]
        xy_Arrow[2] = [tx + ArrowSize, ty + ArrowSize / 2, tz]
    PlotArrowHead(w,NodeLocation, xy_Arrow,Arrowcolor,Linewidth)
    PlotLineSegment(w,NodeLocation, [tx - length,ty,tz],Arrowcolor,Linewidth)
    return

def PlotArrow_y(w,NodeID: int,length: float):
    Arrowcolor = gui_setting.gui_setting.LoadColor
    Linewidth = gui_setting.gui_setting.LineWidth
    ArrowSize = gui_setting.gui_setting.ArrowSize
    NodeLocation = np.empty(3)
    tx,ty,tz = model.msaModel.Node.x[NodeID], model.msaModel.Node.y[NodeID], model.msaModel.Node.z[NodeID]
    NodeLocation = [tx,ty,tz]
    yz_Arrow = np.empty((3,3))
    yz_Arrow[0] = [tx, ty - ArrowSize, tz - ArrowSize / 2]
    yz_Arrow[1] = [tx, ty - ArrowSize/3, tz]
    yz_Arrow[2] = [tx, ty - ArrowSize/3, tz + ArrowSize / 2]
    if length < 0:
        yz_Arrow[0] = [tx, ty + ArrowSize, tz - ArrowSize / 2]
        yz_Arrow[1] = [tx, ty + ArrowSize / 3, tz]
        yz_Arrow[2] = [tx, ty + ArrowSize / 3, tz + ArrowSize / 2]
    PlotArrowHead(w,NodeLocation,yz_Arrow,Arrowcolor,Linewidth)
    yx_Arrow = np.empty((3,3))
    yx_Arrow[0] = [tx - ArrowSize /2, ty - ArrowSize, tz]
    yx_Arrow[1] = [tx, ty - ArrowSize / 3, tz]
    yx_Arrow[2] = [tx + ArrowSize / 2, ty - ArrowSize, tz]
    if length < 0:
        yx_Arrow[0] = [tx - ArrowSize / 2, ty + ArrowSize, tz]
        yx_Arrow[1] = [tx, ty + ArrowSize / 3, tz]
        yx_Arrow[2] = [tx + ArrowSize / 2, ty + ArrowSize, tz]
    PlotArrowHead(w,NodeLocation, yx_Arrow,Arrowcolor,Linewidth)
    PlotLineSegment(w,NodeLocation, [tx,ty  - length,tz],Arrowcolor,Linewidth)
    return

def PlotArrow_z(w,NodeID: int,length: float):
    Arrowcolor = gui_setting.gui_setting.LoadColor
    Linewidth = gui_setting.gui_setting.LineWidth
    ArrowSize = gui_setting.gui_setting.ArrowSize
    NodeLocation = np.empty(3)
    tx,ty,tz = model.msaModel.Node.x[NodeID], model.msaModel.Node.y[NodeID], model.msaModel.Node.z[NodeID]
    NodeLocation = [tx,ty,tz]
    zx_Arrow = np.empty((3,3))
    zx_Arrow[0] = [tx - ArrowSize / 2, ty, tz - ArrowSize]
    zx_Arrow[1] = [tx, ty, tz - ArrowSize/3]
    zx_Arrow[2] = [tx + ArrowSize / 2, ty, tz - ArrowSize]
    if length < 0:
        zx_Arrow[0] = [tx - ArrowSize / 2, ty, tz + ArrowSize]
        zx_Arrow[1] = [tx, ty, tz + ArrowSize / 3]
        zx_Arrow[2] = [tx + ArrowSize / 2, ty, tz + ArrowSize]
    PlotArrowHead(w,NodeLocation,zx_Arrow,Arrowcolor,Linewidth)
    zy_Arrow = np.empty((3,3))
    zy_Arrow[0] = [tx, ty - ArrowSize / 2, tz - ArrowSize]
    zy_Arrow[1] = [tx, ty, tz - ArrowSize / 3]
    zy_Arrow[2] = [tx, ty + ArrowSize / 2, tz - ArrowSize]
    if length < 0:
        zy_Arrow[0] = [tx, ty - ArrowSize / 2, tz + ArrowSize]
        zy_Arrow[1] = [tx, ty, tz + ArrowSize / 3]
        zy_Arrow[2] = [tx, ty + ArrowSize / 2, tz + ArrowSize]
    PlotArrowHead(w,NodeLocation, zy_Arrow,Arrowcolor,Linewidth)
    PlotLineSegment(w,NodeLocation, [tx,ty,tz - length],Arrowcolor,Linewidth)
    return

def PlotMz(w,NodeID: int):
    Arrowcolor = gui_setting.gui_setting.LoadColor
    Linewidth = gui_setting.gui_setting.LineWidth
    ArrowSize = gui_setting.gui_setting.ArrowSize / 2
    tpos = np.empty((8,3))
    tx, ty, tz = model.msaModel.Node.x[NodeID], model.msaModel.Node.y[NodeID], model.msaModel.Node.z[NodeID]
    tpos[0] = [tx + 2 * ArrowSize, ty, tz]
    tpos[1] = [tx + 3 * ArrowSize, ty + 2 * ArrowSize, tz]
    tpos[2] = [tx + 2 * ArrowSize, ty + 4 * ArrowSize, tz]
    tpos[3] = [tx + 1 * ArrowSize, ty + 5 * ArrowSize, tz]
    tpos[4] = [tx - 1 * ArrowSize, ty + 5 * ArrowSize, tz]
    tpos[5] = [tx - 2 * ArrowSize, ty + 4 * ArrowSize, tz]
    tpos[6] = [tx - 3 * ArrowSize, ty + 2 * ArrowSize, tz]
    tpos[7] = [tx - 2 * ArrowSize, ty, tz]
    for ii in range(7):
        PlotLineSegment(w, tpos[ii], tpos[ii + 1], Arrowcolor, Linewidth)
    tpos1 = [tx - 2.3 * ArrowSize, ty + 1 * ArrowSize, tz]
    tpos2 = [tx - 2.7 * ArrowSize, ty + 0.8 * ArrowSize, tz]
    PlotLineSegment(w, tpos1, tpos[7], Arrowcolor, Linewidth)
    PlotLineSegment(w, tpos[7], tpos2, Arrowcolor, Linewidth)
    return

def PlotMy(w,NodeID: int):
    Arrowcolor = gui_setting.gui_setting.LoadColor
    Linewidth = gui_setting.gui_setting.LineWidth
    ArrowSize = gui_setting.gui_setting.ArrowSize / 2
    tpos = np.empty((8,3))
    tx, ty, tz = model.msaModel.Node.x[NodeID], model.msaModel.Node.y[NodeID], model.msaModel.Node.z[NodeID]
    tpos[0] = [tx + 2 * ArrowSize, ty, tz]
    tpos[1] = [tx + 3 * ArrowSize, ty, tz + 2 * ArrowSize]
    tpos[2] = [tx + 2 * ArrowSize, ty, tz + 4 * ArrowSize]
    tpos[3] = [tx + 1 * ArrowSize, ty, tz + 5 * ArrowSize]
    tpos[4] = [tx - 1 * ArrowSize, ty, tz + 5 * ArrowSize]
    tpos[5] = [tx - 2 * ArrowSize, ty, tz + 4 * ArrowSize]
    tpos[6] = [tx - 3 * ArrowSize, ty, tz + 2 * ArrowSize]
    tpos[7] = [tx - 2 * ArrowSize, ty, tz]
    for ii in range(7):
        PlotLineSegment(w, tpos[ii], tpos[ii + 1], Arrowcolor, Linewidth)
    tpos1 = [tx + 2.3 * ArrowSize, ty, tz + 1 * ArrowSize]
    tpos2 = [tx + 2.7 * ArrowSize, ty, tz + 0.8 * ArrowSize]
    PlotLineSegment(w, tpos1, tpos[0], Arrowcolor, Linewidth)
    PlotLineSegment(w, tpos2, tpos[0], Arrowcolor, Linewidth)
    return

def PlotMx(w,NodeID: int):
    Arrowcolor = gui_setting.gui_setting.LoadColor
    Linewidth = gui_setting.gui_setting.LineWidth
    ArrowSize = gui_setting.gui_setting.ArrowSize / 2
    tpos = np.empty((8,3))
    tx, ty, tz = model.msaModel.Node.x[NodeID], model.msaModel.Node.y[NodeID], model.msaModel.Node.z[NodeID]
    tpos[0] = [tx, ty + 2 * ArrowSize, tz]
    tpos[1] = [tx, ty + 3 * ArrowSize, tz + 2 * ArrowSize]
    tpos[2] = [tx, ty + 2 * ArrowSize, tz + 4 * ArrowSize]
    tpos[3] = [tx, ty + 1 * ArrowSize, tz + 5 * ArrowSize]
    tpos[4] = [tx, ty - 1 * ArrowSize, tz + 5 * ArrowSize]
    tpos[5] = [tx, ty - 2 * ArrowSize, tz + 4 * ArrowSize]
    tpos[6] = [tx, ty - 3 * ArrowSize, tz + 2 * ArrowSize]
    tpos[7] = [tx, ty - 2 * ArrowSize, tz]
    for ii in range(7):
        PlotLineSegment(w, tpos[ii], tpos[ii + 1], Arrowcolor, Linewidth)
    tpos1 = [tx, ty - 2.3 * ArrowSize, tz + 1 * ArrowSize]
    tpos2 = [tx, ty - 2.7 * ArrowSize, tz + 0.8 * ArrowSize]
    PlotLineSegment(w, tpos1, tpos[7], Arrowcolor, Linewidth)
    PlotLineSegment(w, tpos[7], tpos2, Arrowcolor, Linewidth)
    return

def PlotLineSegment(w, Startpos,Endpos,Arrowcolor,Linewidth):
    tpos = np.empty((2, 3))
    tpos[0] = Startpos; tpos[1] = Endpos
    tcolor = np.empty((2, 4))
    tcolor[0] = tcolor[1] = Arrowcolor
    tPlotline = gl.GLLinePlotItem(pos=tpos, width=Linewidth, color=tcolor, antialias=False, mode='lines')
    w.addItem(tPlotline)
    return

def PlotArrowHead(w, HeadLocation, ArrowPoint,Arrowcolor,Linewidth):
    PlotLineSegment(w, HeadLocation, ArrowPoint[0], Arrowcolor, Linewidth)
    PlotLineSegment(w, HeadLocation, ArrowPoint[2], Arrowcolor, Linewidth)
    PlotLineSegment(w, ArrowPoint[1], ArrowPoint[0], Arrowcolor, Linewidth)
    PlotLineSegment(w, ArrowPoint[1], ArrowPoint[2], Arrowcolor, Linewidth)
    return