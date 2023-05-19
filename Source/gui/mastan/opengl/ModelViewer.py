from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import pyqtgraph.opengl.GLViewWidget as GLViewWidget

class TDViewer:

    def __init__(self):
        w = gl.GLViewWidget()
        TDViewer.w.setCameraPosition(distance=5)
        g = gl.GLGridItem()
        g.scale(2, 2, 1)
        TDViewer.w.addItem(g)
        md = gl.MeshData.sphere(rows=40, cols=80)
        m = gl.GLMeshItem(meshdata=md, smooth=False, drawFaces=False, drawEdges=True, edgeColor=(1, 1, 1, 1))
        m.translate(0, 0, 0)
        TDViewer.w.addItem(m)

