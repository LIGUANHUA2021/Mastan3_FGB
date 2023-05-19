'''
Open a data file and plot the model on GUI
'''
from gui.gui_function.Node_ConstantSize import Node_ConstantSize
import numpy as np
import pyqtgraph.opengl as gl
import gui.mastan3.base.models as model
import gui.mastan3.base.io as io

def OpenModel(w,FileName):
    io.ImportDataFile(FileName)
    Node = model.msaModel.Node
    tNpos = np.empty((Node.Count, 3))
    tNsize = np.empty((Node.Count))
    tNcolor = np.empty((Node.Count, 4))
    for ii in range(Node.Count):
        tID = Node.ID[ii]
        tNpos[ii] = [Node.x[tID], Node.y[tID], Node.z[tID]]
        tNsize[ii] = 0.08
        tNcolor[ii] = [255, 255, 255, 1]
        tPlottedNode = Node_ConstantSize(tNpos[ii])
        w.addItem(tPlottedNode)
    # tPlottedNode = gl.GLScatterPlotItem(pos=tNpos, size=tNsize, color=tNcolor, pxMode=False)
    # tPlottedNode = Node_ConstantSize(tNpos)
    # w.addItem(tPlottedNode
    Mem = model.msaModel.Member
    for ii in range(Mem.Count):
        tID = Mem.ID[ii]
        tNI, tNJ = Mem.NodeI[tID], Mem.NodeJ[tID]
        tpos = np.empty((2, 3))
        tcolor = np.empty((2, 4))
        tpos[0] = [Node.x[tNI], Node.y[tNI], Node.z[tNI]]
        tpos[1] = [Node.x[tNJ], Node.y[tNJ], Node.z[tNJ]]
        width = 0.15
        tcolor[0] = [255, 255, 255, 1]
        tcolor[1] = [255, 255, 255, 1]
        tPlottedMem = gl.GLLinePlotItem(pos=tpos, width=width, color=tcolor, antialias=False, mode='lines')
        w.addItem(tPlottedMem)
    return