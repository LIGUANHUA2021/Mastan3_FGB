'''
Open a data file and plot the model on GUI
'''
#from gui.gui_function.Node_ConstantSize import Node_ConstantSize
import numpy as np
import pyqtgraph.opengl as gl
import gui.msasect.base.Model as model
import gui.msasect.file.IO as io

def OpenModel(w,FileName):
    io.ImportDataFile(FileName)
    Point = model.Point
    tPpos = np.empty((Point.Count, 3))
    tPsize = np.empty((Point.Count))
    tPcolor = np.empty((Point.Count, 4))
    for ii in range(Point.Count):
        tID = Point.ID[ii]
        tPpos[ii] = [Point.x[tID], Point.y[tID], Point.z[tID]]
        tPsize[ii] = 0.08
        tPcolor[ii] = [255, 255, 255, 1]
        #tPlottedNode = Node_ConstantSize(tNpos[ii])
        #w.addItem(tPlottedNode)

    Seg = model.Segment
    for ii in range(Seg.Count):
        tID = Seg.ID[ii]
        tPI, tPJ = Seg.PointI[tID], Seg.PointJ[tID]
        tpos = np.empty((2, 3))
        tcolor = np.empty((2, 4))
        tpos[0] = [Point.x[tPI], Point.y[tPI], Point.z[tPI]]
        tpos[1] = [Point.x[tPJ], Point.y[tPJ], Point.z[tPJ]]
        width = 0.15
        tcolor[0] = [255, 255, 255, 1]
        tcolor[1] = [255, 255, 255, 1]
        tPlottedMem = gl.GLLinePlotItem(pos=tpos, width=width, color=tcolor, antialias=False, mode='lines')
        w.addItem(tPlottedMem)
    return