# -*- coding: utf-8 -*-

"""
Module implementing Model3DView.
"""
from copy import deepcopy

from PySide6.QtCore import Slot, QSize
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator, QIcon

import traceback
import numpy as np
from pyqtgraph import opengl as gl
from pyqtgraph.Vector import Vector
from matplotlib.colors import hex2color

from .Ui_Model3DView import Ui_Model3DView_Dialog
from gui.msasect.base.Model import msaModel, msaFEModel
from analysis.FESect.util.MeshGen import FEMesh
from analysis.FESect.variables.Model import Node3D
from analysis.FESect.variables.Model import Segment3D
from analysis.FESect.variables.Model import Fiber3D
from analysis.FESect.variables.Model import TempNode
from analysis.FESect.variables.Model import TempFiber


class Mesh3DViewDialog(QDialog, Ui_Model3DView_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, mw, member_len, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__()
        self.parent = parent
        self.mw = mw
        self.setupUi(self)
        self.setWindowIcon(QIcon("ui/ico/Model3DView.png"))
        self.ClChecked = self.mw.Centerline_radioButton.isChecked()
        self.Ext = 0
        self.Transparency = 1
        self.member_len = member_len
        if not self.ClChecked:
            self.StartTempMeshGen()
        self.Scaling_toolButton.setIcon(QIcon('ui/ico/Scaling.png'))
        self.Scaling_toolButton.setIconSize(QSize(16, 16))
        self.Scaling_toolButton.setCheckable(True)
        self.Scaling_toolButton.toggled.connect(self.set_scaling)
        self.Scaling_toolButton.toggled.connect(self.switch_scaling)
        self.Panning_toolButton.setIcon(QIcon('ui/ico/Panning.png'))
        self.Panning_toolButton.setIconSize(QSize(16, 16))
        self.Panning_toolButton.setCheckable(True)
        self.Panning_toolButton.toggled.connect(self.set_panning)
        self.Panning_toolButton.toggled.connect(self.switch_panning)
        self.Tracking_toolButton.setIcon(QIcon('ui/ico/Tracking.png'))
        self.Tracking_toolButton.setIconSize(QSize(16, 16))
        self.Tracking_toolButton.setCheckable(True)
        self.Tracking_toolButton.toggled.connect(self.set_tracking)
        self.Tracking_toolButton.toggled.connect(self.switch_tracking)
        self.initDialog()

    def initDialog(self):
        IntValidator = QIntValidator(bottom=0, top=100)
        self.lineEdit.setValidator(IntValidator)
        if self.ClChecked:
            self.ExtY = max(msaModel.Point.Yo.values()) - min(msaModel.Point.Yo.values())
            self.ExtZ = max(msaModel.Point.Zo.values()) - min(msaModel.Point.Zo.values())
            self.Ext = max(self.ExtY, self.ExtZ)
            self.pos2 = (max(msaModel.Point.Zo.values()) + min(msaModel.Point.Zo.values())) * 0.5
            self.pos3 = (max(msaModel.Point.Yo.values()) + min(msaModel.Point.Yo.values())) * 0.5
        else:
            self.ExtY = max(msaFEModel.Point.Yo.values()) - min(msaFEModel.Point.Yo.values())
            self.ExtZ = max(msaFEModel.Point.Zo.values()) - min(msaFEModel.Point.Zo.values())
            self.Ext = max(self.ExtY, self.ExtZ)
            self.pos2 = (max(msaFEModel.Point.Zo.values()) + min(msaFEModel.Point.Zo.values())) * 0.5
            self.pos3 = (max(msaFEModel.Point.Yo.values()) + min(msaFEModel.Point.Yo.values())) * 0.5
        self.graphicsView.setCameraPosition(pos=Vector(0, self.pos2, self.pos3),
                                            distance=self.Ext * (3 + 0.3 * self.ExtY / self.Ext),
                                            elevation=15, azimuth=20)
        self.graphicsView.pan(dx=60 + 40 * self.ExtZ / self.Ext, dy=-(50 + 20 * self.ExtY / self.Ext),
                              dz=0, relative='view')
        self.cam_center = self.graphicsView.cameraParams()['center']
        self.cam_xcenter = self.cam_center[0]
        self.cam_ycenter = self.cam_center[1]
        self.cam_zcenter = self.cam_center[2]
        self.cam_dist = self.graphicsView.cameraParams()['distance']

        self.Model3DPlot()

    def Model3DPlot(self):
        self.graphicsView.clear()
        if self.Axis_checkBox.isChecked():
            ax = gl.GLAxisItem()
            ax.setSize(self.Ext * 5, self.Ext * 5, self.Ext * 5)
            self.graphicsView.addItem(ax)

        if self.Volume_checkBox.isChecked():
            if self.ClChecked:
                verts1 = np.zeros([msaModel.Segment.Count * 4, 3], dtype=float)
                faces = np.zeros([msaModel.Segment.Count * 2, 3], dtype=int)
                colors = np.zeros([msaModel.Segment.Count * 2, 4], dtype=float)
                SegID = list(msaModel.Segment.ID)
                PointY = list(msaModel.Point.Yo.values())
                PointZ = list(msaModel.Point.Zo.values())
                for i in range(msaModel.Segment.Count):
                    t = msaModel.Segment.SegThick[SegID[i]]
                    Z1 = PointZ[msaModel.Point.ID[msaModel.Segment.PointI[SegID[i]]]]
                    Y1 = PointY[msaModel.Point.ID[msaModel.Segment.PointI[SegID[i]]]]
                    Z2 = PointZ[msaModel.Point.ID[msaModel.Segment.PointJ[SegID[i]]]]
                    Y2 = PointY[msaModel.Point.ID[msaModel.Segment.PointJ[SegID[i]]]]
                    L = np.sqrt((Z2 - Z1) ** 2 + (Y2 - Y1) ** 2)
                    verts1[i * 4][1] = Z1 + t / 2 / L * (Y2 - Y1)
                    verts1[i * 4][2] = Y1 - t / 2 / L * (Z2 - Z1)
                    verts1[i * 4 + 1][1] = Z1 - t / 2 / L * (Y2 - Y1)
                    verts1[i * 4 + 1][2] = Y1 + t / 2 / L * (Z2 - Z1)
                    verts1[i * 4 + 2][1] = Z2 + t / 2 / L * (Y2 - Y1)
                    verts1[i * 4 + 2][2] = Y2 - t / 2 / L * (Z2 - Z1)
                    verts1[i * 4 + 3][1] = Z2 - t / 2 / L * (Y2 - Y1)
                    verts1[i * 4 + 3][2] = Y2 + t / 2 / L * (Z2 - Z1)
                    faces[i * 2, 0] = i * 4
                    faces[i * 2, 1] = i * 4 + 1
                    faces[i * 2, 2] = i * 4 + 2
                    faces[i * 2 + 1, 0] = i * 4 + 1
                    faces[i * 2 + 1, 1] = i * 4 + 2
                    faces[i * 2 + 1, 2] = i * 4 + 3
                    colors[i * 2:(i + 1) * 2, :3] = hex2color(msaModel.Mat.Color[msaModel.Segment.MatID[SegID[i]]])
                    colors[i * 2:(i + 1) * 2, 3] = self.Transparency
                verts2 = deepcopy(verts1)
                verts2[:, 0] = self.member_len
                ## Mesh item will automatically compute face normals.
                Front = gl.GLMeshItem(vertexes=verts1, faces=faces, faceColors=colors, smooth=False, antialias=True)
                Front.setGLOptions('translucent')
                self.graphicsView.addItem(Front)
                Back = gl.GLMeshItem(vertexes=verts2, faces=faces, faceColors=colors, smooth=False, antialias=True)
                Back.setGLOptions('translucent')
                self.graphicsView.addItem(Back)
                verts = np.concatenate((verts1, verts2), axis=0)
                faces = np.zeros([msaModel.Segment.Count * 8, 3], dtype=int)
                colors = np.zeros([msaModel.Segment.Count * 8, 4], dtype=float)
                for i in range(msaModel.Segment.Count):
                    faces[i * 8, 0] = i * 4
                    faces[i * 8, 1] = i * 4 + 1
                    faces[i * 8, 2] = i * 4 + msaModel.Segment.Count * 4
                    faces[i * 8 + 1, 0] = i * 4 + msaModel.Segment.Count * 4
                    faces[i * 8 + 1, 1] = i * 4 + 1 + msaModel.Segment.Count * 4
                    faces[i * 8 + 1, 2] = i * 4 + 1
                    faces[i * 8 + 2, 0] = i * 4
                    faces[i * 8 + 2, 1] = i * 4 + 2
                    faces[i * 8 + 2, 2] = i * 4 + msaModel.Segment.Count * 4
                    faces[i * 8 + 3, 0] = i * 4 + msaModel.Segment.Count * 4
                    faces[i * 8 + 3, 1] = i * 4 + 2 + msaModel.Segment.Count * 4
                    faces[i * 8 + 3, 2] = i * 4 + 2
                    faces[i * 8 + 4, 0] = i * 4 + 1
                    faces[i * 8 + 4, 1] = i * 4 + 3
                    faces[i * 8 + 4, 2] = i * 4 + 1 + msaModel.Segment.Count * 4
                    faces[i * 8 + 5, 0] = i * 4 + 1 + msaModel.Segment.Count * 4
                    faces[i * 8 + 5, 1] = i * 4 + 3 + msaModel.Segment.Count * 4
                    faces[i * 8 + 5, 2] = i * 4 + 3
                    faces[i * 8 + 6, 0] = i * 4 + 2
                    faces[i * 8 + 6, 1] = i * 4 + 3
                    faces[i * 8 + 6, 2] = i * 4 + 2 + msaModel.Segment.Count * 4
                    faces[i * 8 + 7, 0] = i * 4 + 2 + msaModel.Segment.Count * 4
                    faces[i * 8 + 7, 1] = i * 4 + 3 + msaModel.Segment.Count * 4
                    faces[i * 8 + 7, 2] = i * 4 + 3
                    ColorName = hex2color(msaModel.Mat.Color[msaModel.Segment.MatID[SegID[i]]])
                    colors[i * 8:(i + 1) * 8, 0] = max(ColorName[0] - 0.2, 0)
                    colors[i * 8:(i + 1) * 8, 1] = max(ColorName[1] - 0.2, 0)
                    colors[i * 8:(i + 1) * 8, 2] = max(ColorName[2] - 0.2, 0)
                    colors[i * 8:(i + 1) * 8, 3] = self.Transparency
                ## Mesh item will automatically compute face normals.
                Side = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors, smooth=False, antialias=True)
                Side.setGLOptions('translucent')
                self.graphicsView.addItem(Side)
            else:
                verts1 = np.zeros([TempNode.Count, 3], dtype=float)
                faces = np.zeros([TempFiber.Count, 3], dtype=int)
                colors = np.zeros([TempFiber.Count, 4], dtype=float)
                for i in range(TempNode.Count):
                    verts1[i, 1] = TempNode.Z[i]
                    verts1[i, 2] = TempNode.Y[i]
                for i in range(TempFiber.Count):
                    faces[i, 0] = TempFiber.PointI[i]
                    faces[i, 1] = TempFiber.PointJ[i]
                    faces[i, 2] = TempFiber.PointK[i]
                    colors[i, :3] = hex2color(msaFEModel.Mat.Color[TempFiber.MaterialID[i]])
                    colors[i, 3] = self.Transparency
                verts2 = deepcopy(verts1)
                verts2[:, 0] = self.member_len
                ## Mesh item will automatically compute face normals.
                Front = gl.GLMeshItem(vertexes=verts1, faces=faces, faceColors=colors, smooth=False, antialias=True)
                Front.setGLOptions('translucent')
                self.graphicsView.addItem(Front)
                ## Mesh item will automatically compute face normals.
                Back = gl.GLMeshItem(vertexes=verts2, faces=faces, faceColors=colors, smooth=False, antialias=True)
                Back.setGLOptions('translucent')
                self.graphicsView.addItem(Back)
                vertsf = np.full([msaFEModel.Point.Count, 3], 0)
                vertsb = np.full([msaFEModel.Point.Count, 3], self.member_len)
                PointY = list(msaFEModel.Point.Yo.values())
                PointZ = list(msaFEModel.Point.Zo.values())
                PointI = list(msaFEModel.Outline.PointI.values())
                PointJ = list(msaFEModel.Outline.PointJ.values())
                for i in range(msaFEModel.Point.Count):
                    vertsf[i, 1] = vertsb[i, 1] = PointZ[i]
                    vertsf[i, 2] = vertsb[i, 2] = PointY[i]
                verts = np.concatenate((vertsf, vertsb), axis=0)
                faces = np.zeros([msaFEModel.Outline.Count * 2, 3], dtype=int)
                colors = np.zeros([msaFEModel.Outline.Count * 2, 4], dtype=float)
                OID = list(msaFEModel.Outline.ID)
                for i in range(msaFEModel.Outline.Count):
                    faces[i * 2, 0] = msaFEModel.Point.ID[PointI[i]]
                    faces[i * 2, 1] = msaFEModel.Point.ID[PointJ[i]]
                    faces[i * 2, 2] = msaFEModel.Point.ID[PointI[i]] + msaFEModel.Point.Count
                    faces[i * 2 + 1, 0] = msaFEModel.Point.ID[PointI[i]] + msaFEModel.Point.Count
                    faces[i * 2 + 1, 1] = msaFEModel.Point.ID[PointJ[i]] + msaFEModel.Point.Count
                    faces[i * 2 + 1, 2] = msaFEModel.Point.ID[PointJ[i]]
                    ColorName = hex2color(msaFEModel.Mat.Color[msaFEModel.Group.MatID[msaFEModel.Outline.GroupID[OID[i]]]])
                    colors[i * 2:(i + 1) * 2, 0] = max(ColorName[0] - 0.2, 0)
                    colors[i * 2:(i + 1) * 2, 1] = max(ColorName[1] - 0.2, 0)
                    colors[i * 2:(i + 1) * 2, 2] = max(ColorName[2] - 0.2, 0)
                    colors[i * 2:(i + 1) * 2, 3] = self.Transparency
                ## Mesh item will automatically compute face normals.
                Side = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors, smooth=False, antialias=True)
                Side.setGLOptions('translucent')
                self.graphicsView.addItem(Side)

        if self.Edge_checkBox.isChecked():
            if self.ClChecked:
                if self.parent.FSM_radioButton.isChecked():
                    for i in msaModel.Fiber3D.ID:
                        pts = [i for i in range(int(self.parent.LengthTimes_lineEdit.text()) + 1)]
                        for j in range(int(self.parent.LengthTimes_lineEdit.text()) + 1):
                            pts[j] = np.zeros((5, 3))
                            pts[j][0, 1] = pts[j][4, 1] = msaModel.Node3D.Zo[msaModel.Fiber3D.NodeI[i]]
                            pts[j][0, 2] = pts[j][4, 2] = msaModel.Node3D.Yo[msaModel.Fiber3D.NodeI[i]]
                            pts[j][1, 1] = msaModel.Node3D.Zo[msaModel.Fiber3D.NodeJ[i]]
                            pts[j][1, 2] = msaModel.Node3D.Yo[msaModel.Fiber3D.NodeJ[i]]
                            pts[j][2, 1] = msaModel.Node3D.Zo[msaModel.Fiber3D.NodeK[i]]
                            pts[j][2, 2] = msaModel.Node3D.Yo[msaModel.Fiber3D.NodeK[i]]
                            pts[j][3, 1] = msaModel.Node3D.Zo[msaModel.Fiber3D.NodeL[i]]
                            pts[j][3, 2] = msaModel.Node3D.Yo[msaModel.Fiber3D.NodeL[i]]
                            pts[j][:, 0] = j * self.parent.unit_len
                            plt = gl.GLLinePlotItem(pos=pts[j], color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                            self.graphicsView.addItem(plt)


            else:
                verts1 = np.zeros([Node3D.Count, 3])
                faces = np.zeros([Fiber3D.Count, 3], dtype=int)
                colors = np.zeros([Fiber3D.Count, 4], dtype=float)
                for i in Node3D.ID:
                    verts1[i, 0] = Node3D.X[i]
                    verts1[i, 1] = Node3D.Z[i]
                    verts1[i, 2] = Node3D.Y[i]
                for i in Fiber3D.ID:
                    faces[i, 0] = Fiber3D.PointI[i]
                    faces[i, 1] = Fiber3D.PointJ[i]
                    faces[i, 2] = Fiber3D.PointK[i]
                    colors[i, :3] = hex2color(msaFEModel.Mat.Color[Fiber3D.MaterialID[i]])
                    colors[i, 3] = self.Transparency
                plot = gl.GLScatterPlotItem(pos=verts1, color=colors, size=4, pxMode=True)
                self.graphicsView.addItem(plot)

                pts = np.zeros((2, 3))
                for i in Segment3D.ID:
                    pts[0, 0] = Node3D.X[Segment3D.NodeI[i]]
                    pts[0, 1] = Node3D.Z[Segment3D.NodeI[i]]
                    pts[0, 2] = Node3D.Y[Segment3D.NodeI[i]]
                    pts[1, 0] = Node3D.X[Segment3D.NodeJ[i]]
                    pts[1, 1] = Node3D.Z[Segment3D.NodeJ[i]]
                    pts[1, 2] = Node3D.Y[Segment3D.NodeJ[i]]
                    plt = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt)

        '''
        if self.Edge_checkBox.isChecked():
            if self.ClChecked:
                SegID = list(msaModel.Segment.ID)
                PointY = list(msaModel.Point.Yo.values())
                PointZ = list(msaModel.Point.Zo.values())
                for i in range(msaModel.Segment.Count):
                    pts = np.zeros((5, 3))
                    t = msaModel.Segment.SegThick[SegID[i]]
                    Z1 = PointZ[msaModel.Point.ID[msaModel.Segment.PointI[SegID[i]]]]
                    Y1 = PointY[msaModel.Point.ID[msaModel.Segment.PointI[SegID[i]]]]
                    Z2 = PointZ[msaModel.Point.ID[msaModel.Segment.PointJ[SegID[i]]]]
                    Y2 = PointY[msaModel.Point.ID[msaModel.Segment.PointJ[SegID[i]]]]
                    L = np.sqrt((Z2 - Z1) ** 2 + (Y2 - Y1) ** 2)
                    pts[0, 1] = pts[4, 1] = Z1 + t / 2 / L * (Y2 - Y1)
                    pts[0, 2] = pts[4, 2] = Y1 - t / 2 / L * (Z2 - Z1)
                    pts[1, 1] = Z1 - t / 2 / L * (Y2 - Y1)
                    pts[1, 2] = Y1 + t / 2 / L * (Z2 - Z1)
                    pts[2, 1] = Z2 - t / 2 / L * (Y2 - Y1)
                    pts[2, 2] = Y2 + t / 2 / L * (Z2 - Z1)
                    pts[3, 1] = Z2 + t / 2 / L * (Y2 - Y1)
                    pts[3, 2] = Y2 - t / 2 / L * (Z2 - Z1)
                    pts[:, 0] = self.Ext * 2
                    plt = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt)
                    pts[:, 0] = self.Ext * -2
                    plt2 = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt2)
                    
                    tZ = Z1 + t / 2 / L * (Y2 - Y1)
                    tY = Y1 - t / 2 / L * (Z2 - Z1)
                    pts = np.array([[self.Ext * 2, tZ, tY],
                                    [self.Ext * -2, tZ, tY]])
                    plt3 = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt3)

                    tZ = Z1 - t / 2 / L * (Y2 - Y1)
                    tY = Y1 + t / 2 / L * (Z2 - Z1)
                    pts = np.array([[self.Ext * 2, tZ, tY],
                                    [self.Ext * -2, tZ, tY]])
                    plt4 = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt4)

                    tZ = Z2 - t / 2 / L * (Y2 - Y1)
                    tY = Y2 + t / 2 / L * (Z2 - Z1)
                    pts = np.array([[self.Ext * 2, tZ, tY],
                                    [self.Ext * -2, tZ, tY]])
                    plt5 = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt5)

                    tZ = Z2 + t / 2 / L * (Y2 - Y1)
                    tY = Y2 - t / 2 / L * (Z2 - Z1)
                    pts = np.array([[self.Ext * 2, tZ, tY],
                                    [self.Ext * -2, tZ, tY]])
                    plt6 = gl.GLLinePlotItem(pos=pts, color=(0.8, 0.8, 0.8, self.Transparency), width=1, antialias=True)
                    self.graphicsView.addItem(plt6)
            '''
    def StartTempMeshGen(self):
        _FEMesh = FEMesh()
        _FEMesh.MeshGenFE(msaFEModel, temp=True)

    @Slot()
    def on_Axis_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Model3DPlot()

    @Slot()
    def on_Edge_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Model3DPlot()

    @Slot()
    def on_Volume_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Model3DPlot()

    @Slot(int)
    def on_Transparency_horizontalSlider_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.lineEdit.setText(str(value))
        self.Transparency = 1 - value / 100
        self.Model3DPlot()

    @Slot(str)
    def on_lineEdit_textEdited(self, p0):
        """
        Slot documentation goes here.
        """
        value = int(p0)
        if value > 100:
            self.lineEdit.setText("100")
            self.Transparency = 0
        else:
            self.Transparency_horizontalSlider.setValue(value)
            self.Transparency = 1 - value / 100
        self.Model3DPlot()

    @Slot()
    def on_Close_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()

    @Slot()
    def on_Reset_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Transparency_horizontalSlider.setValue(0)
        self.lineEdit.setText("0")
        self.Axis_checkBox.setChecked(False)
        self.Volume_checkBox.setChecked(True)
        self.Edge_checkBox.setChecked(False)
        self.cam_center[0] = self.cam_xcenter
        self.cam_center[1] = self.cam_ycenter
        self.cam_center[2] = self.cam_zcenter
        self.graphicsView.setCameraPosition(pos=self.cam_center, distance=self.cam_dist,
                                            elevation=15, azimuth=20)
        self.Model3DPlot()

    def set_scaling(self, is_scaling):
        self.graphicsView._is_scaling = is_scaling

    def set_panning(self, is_panning):
        self.graphicsView._is_panning = is_panning

    def set_tracking(self, is_tracking):
        self.graphicsView._is_tracking = is_tracking

    def switch_scaling(self, toggled):
        if toggled:
            self.graphicsView.cam_dist = self.graphicsView.cameraParams()['distance']
            self.Panning_toolButton.setChecked(False)
            self.Tracking_toolButton.setChecked(False)

    def switch_panning(self, toggled):
        if toggled:
            self.Scaling_toolButton.setChecked(False)
            self.Tracking_toolButton.setChecked(False)

    def switch_tracking(self, toggled):
        params = self.graphicsView.cameraParams()
        pos = params["center"]
        dist = params["distance"]
        elev = params["elevation"]
        azim = params["azimuth"]
        if toggled:
            self.graphicsView.opts["rotationMethod"] = "quaternion"
            self.Scaling_toolButton.setChecked(False)
            self.Panning_toolButton.setChecked(False)
        else:
            self.graphicsView.opts["rotationMethod"] = "euler"
        self.graphicsView.setCameraPosition(pos=pos, distance=dist, elevation=elev, azimuth=azim)
