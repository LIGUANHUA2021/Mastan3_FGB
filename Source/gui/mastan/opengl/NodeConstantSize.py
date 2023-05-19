"""
Demonstrate using QPainter on a subclass of GLGraphicsItem.
"""

import pyqtgraph as pg
import pyqtgraph.opengl
from pyqtgraph.Qt import QtCore, QtGui
from PyQt6.QtGui import QPainter,QColor,QFont
import OpenGL.GL as GL
import gui.gui_function.gui_setting as gui_setting

SIZE = gui_setting.gui_setting.NodeSize
class GLPainterItem(pg.opengl.GLGraphicsItem.GLGraphicsItem):
    def __init__(self, POS, **kwds):
        super().__init__()
        self.POS = POS
        glopts = kwds.pop('glOptions', 'additive')
        self.setGLOptions(glopts)

    def compute_projection(self):
        modelview = GL.glGetDoublev(GL.GL_MODELVIEW_MATRIX)
        projection = GL.glGetDoublev(GL.GL_PROJECTION_MATRIX)
        mvp = projection.T @ modelview.T
        mvp = QtGui.QMatrix4x4(mvp.ravel().tolist())

        # note that QRectF.bottom() != QRect.bottom()
        rect = QtCore.QRectF(self.view().rect())
        ndc_to_viewport = QtGui.QMatrix4x4()
        ndc_to_viewport.viewport(rect.left(), rect.bottom(), rect.width(), -rect.height())

        return ndc_to_viewport * mvp

    def paint(self):
        self.setupGLState()

        painter = QtGui.QPainter(self.view())
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        painter.setPen(QtCore.Qt.GlobalColor.white)
        painter.setRenderHints(QtGui.QPainter.RenderHint.Antialiasing | QtGui.QPainter.RenderHint.TextAntialiasing)

        rect = self.view().rect()
        af = QtCore.Qt.AlignmentFlag

        project = self.compute_projection()

        xi, yi, zi = self.POS
        vec3 = QtGui.QVector3D(xi, yi, zi)
        pos = project.map(vec3).toPointF()
        painter.drawEllipse(pos, 2.5, 2.5)


# pg.mkQApp("GLPainterItem Example")
def Node_ConstantSize(POS):
    paintitem = GLPainterItem(POS=POS)
    return paintitem
