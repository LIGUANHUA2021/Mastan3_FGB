from gui.gui_function.Node_ConstantSize import Node_ConstantSize, gui_setting
import numpy as np
import pyqtgraph.opengl as gl
import gui.gui_function.PlotArrow as PlotArrow
import gui.mastan3.base.models as model


def AddNode(w, tNodeID: int, tLocation:list):
    model.msaModel.Node.Add(tNodeID, tLocation[0], tLocation[1], tLocation[2])
    tNodeColor = gui_setting.gui_setting.NodeColor
    tPlottedNode = Node_ConstantSize(tLocation)
    w.addItem(tPlottedNode)
    return

def AddMem(w,tMemID: int, tSectionID: int, tNI: int, tNJ: int):
    model.msaModel.Member.Add(tMemID, tSectionID, tNI, tNJ)
    tpos = np.empty((2,3)); tcolor = np.empty((2,4))
    tpos[0] = [model.msaModel.Node.x[tNI], model.msaModel.Node.y[tNI], model.msaModel.Node.z[tNI]]
    tpos[1] = [model.msaModel.Node.x[tNJ], model.msaModel.Node.y[tNJ], model.msaModel.Node.z[tNJ]]
    width = gui_setting.gui_setting.LineWidth
    tcolor[0] = gui_setting.gui_setting.MemberColor
    tcolor[1] = gui_setting.gui_setting.MemberColor
    tPlottedMem = gl.GLLinePlotItem(pos=tpos, width=width, color=tcolor, antialias=False, mode='lines')
    w.addItem(tPlottedMem)
    return


def AddLoad(w, tNodeID: int, tLoadVector: list):
    model.msaModel.Load.Add(tNodeID, tLoadVector)
    PlotArrow.PlotArrow_x(w,tNodeID, tLoadVector[0])
    PlotArrow.PlotArrow_y(w,tNodeID, tLoadVector[1])
    PlotArrow.PlotArrow_z(w,tNodeID, tLoadVector[2])
    if tLoadVector[3] != 0:
        PlotArrow.PlotMx(w, tNodeID)
    if tLoadVector[4] != 0:
        PlotArrow.PlotMy(w, tNodeID)
    if tLoadVector[5] != 0:
        PlotArrow.PlotMz(w, tNodeID)
    return

def CreatBound(tNodeID: int, tBound: list):
    model.msaModel.Bound.Add(tNodeID,tBound)
    return

def AddBoundToNode(tID: int, tNodeID: list):
    model.msaModel.Bound.AddBoundToNode(tID,tNodeID)
    return