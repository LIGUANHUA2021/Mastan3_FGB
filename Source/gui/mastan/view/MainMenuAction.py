# Internal
#import gui.Menu as view
import gui.mastan.base.model as model
import gui.mastan.file.io as io

# External
import pyqtgraph.opengl as gl
import numpy as np

##
class mainMenuAction():
    def openFileAction(self, w):
        io.ImportDataFile("Test_Import02.json")
        Node = model.msaModel.Node
        tNpos = np.empty((Node.Count, 3))
        tNsize = np.empty((Node.Count))
        tNcolor = np.empty((Node.Count, 4))
        for ii in range(Node.Count):
            tID = Node.ID[ii]
            tNpos[ii] = [Node.x[tID], Node.y[tID], Node.z[tID]]
            tNsize[ii] = 0.08
            tNcolor[ii] = [255, 255, 255, 1]
        tPlottedNode = gl.GLScatterPlotItem(pos=tNpos, size=tNsize, color=tNcolor, pxMode=False)
        w.addItem(tPlottedNode)

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