# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, QSize, Qt, QTime, QFileInfo
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QColorDialog
from PySide6.QtWidgets import QHeaderView, QMessageBox, QFontDialog, QLabel
from PySide6.QtGui import QIcon, QFont, QBrush, QColor, QTextCursor, QPixmap
from gui.msasect.base.Setting import Program
from gui.msasect.ui.Ui_MainWindow import Ui_MainWindow
import numpy as np
import pyqtgraph as pg
import sys, subprocess
import os, codecs
import datetime
import traceback
# import pdfkit
import webbrowser
from gui.msasect.base.Model import msaModel, msaFEModel, Status, GlobalBuckling
from gui.msasect.base.QtSignal import QtSignal
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.PointAdd import PointAddDialog
from gui.msasect.ui.MaterialAdd import MatAdd_Dialog
from gui.msasect.ui.SegmentAdd import SegmentAddDialog
from gui.msasect.ui.OutlineAdd import OutlineAdd_Dialog
from gui.msasect.slotfunc import SlotFuncInMainWindow
from gui.msasect.ui.PointModify import PointModifyDialog
from gui.msasect.ui.MaterialModify import MatModifyDialog
from gui.msasect.ui.SegmentModify import SegmentModifyDialog
from gui.msasect.ui.OutlineModify import OutlineModify_Dialog
from gui.msasect.ui.ISection import ISection_Dialog
from gui.msasect.ui.TSection import TSection_Dialog
from gui.msasect.ui.ZSection import ZSection_Dialog
from gui.msasect.ui.CSection import CSection_Dialog
from gui.msasect.ui.LSection import LSection_Dialog
from gui.msasect.ui.HollowCircle import HollowCircle_Dialog
from gui.msasect.ui.HollowRec import HollowRec_Dialog
from gui.msasect.ui.HollowTrap import HollowTrap_Dialog
from gui.msasect.ui.General import General_Dialog
from gui.msasect.ui.SolidCircle import SolidCircle_Dialog
from gui.msasect.ui.SolidRec import SolidRec_Dialog
from gui.msasect.ui.TaperedTee import TaperedTee_Dialog
from gui.msasect.ui.SolidTrap import SolidTrap_Dialog
from gui.msasect.ui.SolidTri import SolidTri_Dialog
from gui.msasect.ui.SolidPoly import SolidPoly_Dialog
from gui.msasect.ui.HollowTri import HollowTri_Dialog
from gui.msasect.ui.TaperedI import TaperedI_Dialog
from gui.msasect.ui.BuldTee import BuldTee_Dialog
from gui.msasect.ui.HollowPoly import HollowPoly_Dialog
from gui.msasect.ui.BoxGirder import BoxGirder_Dialog
from gui.msasect.ui.FGCircle import FGCircle_Dialog
from gui.msasect.ui.FGI import FGI_Dialog
from gui.msasect.ui.FGRec import FGRec_Dialog
from gui.msasect.ui.MeshProgress import MeshProgress_Dialog
from gui.msasect.ui.Model3DView import Model3DViewDialog
from gui.msasect.ui.AnalMomentCurvature import MomentCurvatureAnalDialog
from gui.msasect.file import WelcomeInfo
from gui.msasect.ui.About import AboutDialog
from gui.msasect.ui.GraphPlot import CenterlinePlot, OutlinePlot, OriginPlot, PointIDPlot, LineIDPlot, MatIDPlot,\
    FiberPlot, PAPlot, CoordPlot, GCPlot, SCPlot

from gui.msasect.ui.AnalYieldSurfaces import YieldSurfacesAnal_Dialog
from gui.msasect.ui.GlobalBucklingAnal import GlobalBucklingAnal_Dialog
from gui.msasect.ui.AnalLocalBuckling import LocalBucklingAnalDialog
from gui.msasect.ui.AnalStressAnalysis import StressAnalysisAnalDialog
from gui.msasect.ui.SectionalProCalcDia import SectPropCal_Dialog
from gui.msasect.ui.MeshSettings import meshSettings_Dialog
from gui.msasect.ui.NumberingSetting import NumberSetting_Dialog
from analysis.CMSect.util.MeshGen import MeshGenCM

from analysis.CMSect.variables import Model as CMSectModel
from analysis.CMSect.variables.Model import SectProperty, YieldSAnalResults
from analysis.FESect.variables import Model
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults
from analysis.RCD.variables.Model import MomentCurvatureResults, CompositeSectionModulus
from analysis.FESect.variables.Result import SectionProperties as FESectProperty
from gui.msasect.base.OutputRedir import ConsoleOutput
from analysis.CMSect.util.PrintLog import PrintLog as CMpl
from analysis.FESect.file.OutputResults import BPRes


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        #
        sys.stdout = ConsoleOutput(self.StatusOutput)
        #
        self.cwd = os.getcwd()
        self.NumberSetting = "{:>14.4e}" ## Default Numbering setting for sectional properties table
        #
        for i in range(self.splitter.count()):
            self.splitter.handle(i).setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        for i in range(self.splitter_2.count()):
            self.splitter_2.handle(i).setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        for i in range(self.splitter_3.count()):
            self.splitter_3.handle(i).setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        ## Set Mainwindow title
        self.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections')
        #
        self.StatusOutput.clear()
        tWelcomeInfo = WelcomeInfo.Welcome.PrintWelcomeInfo(self)
        self.StatusOutput.setFont(QFont('Courier', 9))
        self.StatusOutput.setText(tWelcomeInfo)
        self.StatusOutput.moveCursor(QTextCursor.Start)
        self.Centerline_radioButton.setChecked(True)
        self.Centerline_label.setPixmap(QPixmap('ui/ico/CM_2.png'))
        self.Outline_label.setPixmap(QPixmap('ui/ico/FE.png'))
        self.ShowOrigin_checkBox.setChecked(True)
        self.status = self.statusBar
        self.statusinfo = QLabel('Please visit '+'''<a style="color: #ffffff" href="http://www.mastan2.com">http://www.mastan2.com</a>'''+' for more details.' )
        self.statusinfo.setOpenExternalLinks(True)
        self.statusinfo_1=QLabel('Last Update:' + Program.Revised)
        self.statusBar_1 = QLabel('{:<40}'.format(' Educational and research use only.'))
        tdate = datetime.datetime.today()
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
        self.Centerline_label_2.setStyleSheet("*{    \n"
                                        "    color: rgb(80, 80, 80);\n"
                                        "}\n"
                                        "")
        self.statusBar_2 = QLabel(
            '{:^40}'.format(' Copyright © ' + str(tdate.year) + ' Siwei Liu and Ronald D. Ziemian, All Right Reserved.'))
        self.status.addWidget(self.statusBar_1, 1)
        self.status.addWidget(self.statusBar_2, 5)
        self.status.addPermanentWidget(self.statusinfo, stretch=0)
        self.status.addPermanentWidget(self.statusinfo_1, stretch=0)
        #
        self.DateInput_lineEdit.setText(str(datetime.date.today()))
        # self.PreparedbyInput_lineEdit.setText(str(socket.gethostname()))
        #
        # else:
        #     self.setWindowTitle(MWTitle)
        #
        self.SegmenttableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SegmenttableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.SegmenttableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SegmenttableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.SegmenttableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.SegmenttableWidget.itemDoubleClicked.connect(self.on_SegModifypushButton_clicked)
        # self.SegmenttableWidget.setColumnWidth(0, 30)
        #
        self.MattableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.MattableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.MattableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.MattableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.MattableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.MattableWidget.doubleClicked.connect(self.ModifyMatInfo())
        self.MattableWidget.itemDoubleClicked.connect(self.on_MatModifypushButton_clicked)
        # self.MattableWidget.setColumnWidth(0, 40)
        #
        self.PointtableWidget.setColumnCount(3)
        self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
        self.PointtableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.PointtableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.PointtableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.PointtableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PointtableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PointtableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PointtableWidget.itemDoubleClicked.connect(self.on_PointModifypushButton_clicked)
        # self.PointtableWidget.setGeometry(QRect(12, 12, 460, 400))
        # self.PointtableWidget.setColumnWidth(2, 105)

        self.SPtableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SPtableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.SPtableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.SPtableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.SPtableWidget.horizontalHeader().setStretchLastSection(True)
        self.SPtableWidget.verticalHeader().setVisible(False)
        self.SPtableWidget.horizontalHeader().setSectionsClickable(False)
        font = QFont()
        font.setBold(True)
        self.SPtableWidget.horizontalHeader().setFont(font)
        # font = self.SPtableWidget.horizontalHeader().font()
        # font.setBold(True)
        # self.SPtableWidget.horizontalHeader().setFont(font)
        # self.SPtableWidget.setColumnWidth(1, 50)
        #
        self.New_toolButton.setIcon(QIcon('ui/ico/New.png'))
        self.New_toolButton.setIconSize(QSize(36, 36))
        self.Open_toolButton.setIcon(QIcon('ui/ico/Open.png'))
        self.Open_toolButton.setIconSize(QSize(36, 36))
        self.Save_toolButton.setIcon(QIcon('ui/ico/Save.png'))
        self.Save_toolButton.setIconSize(QSize(36, 36))
        self.SaveAs_toolButton.setIcon(QIcon('ui/ico/SaveAs.png'))
        self.SaveAs_toolButton.setIconSize(QSize(36, 36))
        # self.Save_toolButton.setIcon(QIcon('ui/ico/save.ico'))
        # self.Save_toolButton.setIconSize(QSize(32, 32))
        # self.Plot_toolButton.setIcon(QIcon('ui/ico/plot.ico'))
        # self.Plot_toolButton.setIconSize(QSize(32, 32))
        self.SPAnal_toolButton.setIcon(QIcon('ui/ico/SectionProperties.png'))
        self.SPAnal_toolButton.setIconSize(QSize(36, 36))
        self.YSAnal_toolButton.setIcon(QIcon('ui/ico/YieldSurface.png'))
        self.YSAnal_toolButton.setIconSize(QSize(36, 36))
        self.MomentCurvature_toolButton.setIcon(QIcon('ui/ico/MomentCurvature.png'))
        self.MomentCurvature_toolButton.setIconSize(QSize(36, 36))
        self.GlobalBuckling_toolButton.setIcon(QIcon('ui/ico/GlobalBuckling.png'))
        self.GlobalBuckling_toolButton.setIconSize(QSize(36, 36))
        # self.GlobalBucklingAnal_toolButton.setIcon(QIcon('ui/ico/BucklingAnalysis.png'))
        # self.GlobalBucklingAnal_toolButton.setIconSize(QSize(36, 36))
        self.LocalBuckling_toolButton.setIcon(QIcon('ui/ico/LocalBuckling.png'))
        self.LocalBuckling_toolButton.setIconSize(QSize(36, 36))
        self.About_toolButton.setIcon(QIcon('ui/ico/About.png'))
        self.About_toolButton.setIconSize(QSize(36, 36))
        self.Fit2Screen_toolButton.setIcon(QIcon('ui/ico/Fit2Screen.png'))
        self.Fit2Screen_toolButton.setIconSize(QSize(36, 36))
        self.Mesh_toolButton.setIcon(QIcon('ui/ico/Mesh.png'))
        self.Mesh_toolButton.setIconSize(QSize(36, 36))
        self.Model3DView_toolButton.setIcon(QIcon('ui/ico/Model3DView.png'))
        self.Model3DView_toolButton.setIconSize(QSize(36, 36))
        self.StressAnalysis_toolButton.setIcon(QIcon('ui/ico/StressAnalysis.png'))
        self.StressAnalysis_toolButton.setIconSize(QSize(36, 36))
        self.UserManual_toolButton.setIcon(QIcon('ui/ico/UserManual.png'))
        self.UserManual_toolButton.setIconSize(QSize(36, 36))
        #
        self.ISection_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/I-Section.ico'))
        self.ISection_toolButton.setIconSize(QSize(32, 32))
        self.TSection_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/T-Section.ico'))
        self.TSection_toolButton.setIconSize(QSize(32, 32))
        self.ZSection_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Z-Section.ico'))
        self.ZSection_toolButton.setIconSize(QSize(32, 32))
        self.CSection_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/C-Section.ico'))
        self.CSection_toolButton.setIconSize(QSize(32, 32))
        self.LSection_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/L-Section.ico'))
        self.LSection_toolButton.setIconSize(QSize(32, 32))
        self.HollowCircle_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Hollow Circle.ico'))
        self.HollowCircle_toolButton.setIconSize(QSize(32, 32))
        self.HollowRec_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Hollow Rec.ico'))
        self.HollowRec_toolButton.setIconSize(QSize(32, 32))
        self.HollowTrap_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Hollow Trap.ico'))
        self.HollowTrap_toolButton.setIconSize(QSize(32, 32))
        self.SolidCircle_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Solid circle.ico'))
        self.SolidCircle_toolButton.setIconSize(QSize(32, 32))
        self.SolidRec_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Solid Rec.ico'))
        self.SolidRec_toolButton.setIconSize(QSize(32, 32))
        self.SolidTrap_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Solid Trap.ico'))
        self.SolidTrap_toolButton.setIconSize(QSize(32, 32))
        self.SolidTri_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Solid Tri.ico'))
        self.SolidTri_toolButton.setIconSize(QSize(32, 32))
        self.HollowTri_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Hollow Tri.ico'))
        self.HollowTri_toolButton.setIconSize(QSize(32, 32))
        self.SolidPoly_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Solid Poly.ico'))
        self.SolidPoly_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Solid Poly.ico'))
        self.SolidPoly_toolButton.setIconSize(QSize(32, 32))
        self.HollowPoly_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Hollow Poly.ico'))
        self.HollowPoly_toolButton.setIconSize(QSize(32, 32))
        self.TaperedTee_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Tapered Tee.ico'))
        self.TaperedTee_toolButton.setIconSize(QSize(32, 32))
        self.BuldTee_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Buld Tee.ico'))
        self.BuldTee_toolButton.setIconSize(QSize(32, 32))
        self.TaperedI_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Tapered I.ico'))
        self.TaperedI_toolButton.setIconSize(QSize(32, 32))
        self.BoxGirder_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/Box Girder.ico'))
        self.BoxGirder_toolButton.setIconSize(QSize(32, 32))
        self.FGCircle_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/FG-Circle.ico'))
        self.FGCircle_toolButton.setIconSize(QSize(32, 32))
        self.FGRec_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/FG-Rec.ico'))
        self.FGRec_toolButton.setIconSize(QSize(32, 32))
        self.FGI_toolButton.setIcon(QIcon('ui/ico/TemplateIcon/FG-I.ico'))
        self.FGI_toolButton.setIconSize(QSize(32, 32))
        #
        self.graphicsView.setBackground('white')
        self.UBorder = self.graphicsView.addPlot(row=0, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                                 title="<font size=3><b>MSASECT2</b><br>{}".format(
                                                     datetime.date.today().strftime('20%y-%m-%d')))
        self.UBorder.showAxes(selection=False)
        self.sect_type = self.graphicsView.addViewBox(row=1, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                                      defaultPadding=0)
        self.sect_type.autoRange()
        self.sect_type_label = pg.TargetItem(pos=(0.1, 0.5), size=0, movable=False, label="")
        self.sect_type.addItem(self.sect_type_label)

        self.LBorder = self.graphicsView.addViewBox(row=8, col=0, rowspan=1, enableMouse=False, enableMenu=False)
        HLine = pg.GraphItem()
        VLine = pg.GraphItem()
        HLine.setData(pos=np.array([[0, 0], [1, 0]]), adj=np.array([[0, 1]]), size=0, pxMode=True)
        VLine.setData(pos=np.array([[1, 0], [1, 1]]), adj=np.array([[0, 1]]), size=0, pxMode=True)
        self.LBorder.addItem(HLine)
        self.LBorder.addItem(VLine)
        self.LBorder.setLimits(xMin=0, minYRange=0)
        self.LBorder.addItem(
            pg.TargetItem(pos=(0, 0), size=0, movable=False, label="Z", labelOpts={"offset": (-4, 8)}))
        self.LBorder.addItem(pg.TargetItem(pos=(1, 1), size=0, movable=False, label="Y", labelOpts={"offset": (-13, -4)}))
        OrigLeg = self.graphicsView.addViewBox(row=2, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                               defaultPadding=0)
        OrigLeg.autoRange()
        OrigLeg.addItem(pg.TargetItem(pos=(0.1, 0.5), size=5, symbol='o', pen=pg.mkPen('w'), brush=pg.mkColor('w'),
                                      movable=False, label="ORIGIN", labelOpts={"offset": (5, -0.5)}))
        MIDLeg = self.graphicsView.addViewBox(row=3, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                              defaultPadding=0)
        MIDLeg.autoRange()
        MIDLeg.addItem(pg.TargetItem(pos=(0.1, 0.5), size=10, symbol='s', pen=pg.mkPen('g'), brush=pg.mkColor('g'),
                                     movable=False, label="MAT ID", labelOpts={"offset": (5, -0.5)}))
        PIDLeg = self.graphicsView.addViewBox(row=4, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                              defaultPadding=0)
        PIDLeg.autoRange()
        PIDLeg.addItem(pg.TargetItem(pos=(0.1, 0.5), size=10, symbol='s', pen=pg.mkPen('c'), brush=pg.mkColor('c'),
                                     movable=False, label="POINT ID", labelOpts={"offset": (5, -0.5)}))
        SIDLeg = self.graphicsView.addViewBox(row=5, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                              defaultPadding=0)
        SIDLeg.autoRange()
        SIDLeg.addItem(pg.TargetItem(pos=(0.1, 0.5), size=10, symbol='s', pen=pg.mkPen('y'), brush=pg.mkColor('y'),
                                     movable=False, label="LINE ID", labelOpts={"offset": (5, -0.5)}))
        GCLeg = self.graphicsView.addViewBox(row=6, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                             defaultPadding=0)
        GCLeg.autoRange()
        GCLeg.addItem(pg.TargetItem(pos=(0.1, 0.5), size=10, symbol='+', pen=pg.mkPen('w'), brush=pg.mkColor('r'),
                                    movable=False, label="GC", labelOpts={"offset": (5, -0.5)}))
        SCLeg = self.graphicsView.addViewBox(row=7, col=0, rowspan=1, enableMouse=False, enableMenu=False,
                                             defaultPadding=0)
        SCLeg.autoRange()
        SCLeg.addItem(pg.TargetItem(pos=(0.1, 0.5), size=10, symbol='x', pen=pg.mkPen('w'), brush=pg.mkColor('b'),
                                    movable=False, label="SC", labelOpts={"offset": (5, -0.5)}))
        self.View = self.graphicsView.addPlot(row=0, col=1, rowspan=9)
        OriginPlot(self.View)
        self.View.invertX(b=True)
        self.View.showAxes(selection=True)
        self.View.showGrid(x=True, y=True)
        self.View.setAspectLocked(lock=True, ratio=1)
        self.View.setRange(xRange=(-1, 1), yRange=(-1, 1), disableAutoRange=True)
        self.graphicsView.ci.layout.setColumnMaximumWidth(0, 70)
        self.graphicsView.ci.layout.setRowMaximumHeight(0, 50)
        self.graphicsView.ci.layout.setRowMaximumHeight(7, 65)
        self.LegendList = [0]
        ## Section Properties table
        SPType = {0: '',
                  1: '\u03b8', 2: 'A', 3: 'Y<SUB>gc</SUB>', 4: 'Z<SUB>gc</SUB>', 5: 'Y<SUB>sc</SUB>', 6: 'Z<SUB>sc</SUB>',
                  7: 'J', 8: 'I<SUB>\u03c9</SUB>',
                  9: ' ',
                  10: 'I<SUB>vv</SUB>', 11: 'I<SUB>ww</SUB>', 12: 'Q<SUB>v</SUB>', 13: 'Q<SUB>w</SUB>', 14: '\u03b2<SUB>v</SUB>', 15: '\u03b2<SUB>w</SUB>', 16: '\u03b2<SUB>\u03c9</SUB>', 17: 'A<SUB>vv</SUB>', 18: 'A<SUB>ww</SUB>',
                  19: 'v<SUB>sc</SUB>', 20: 'w<SUB>sc</SUB>', 21: 'S<SUB>vv</SUB>', 22: 'S<SUB>ww</SUB>', 23: 'Z<SUB>vv</SUB>', 24: 'Z<SUB>ww</SUB>', 25: 'r<SUB>v</SUB>', 26: 'r<SUB>w</SUB>', 27: 'k<SUB>v</SUB>',
                  28: 'k<SUB>w</SUB>',
                  29: ' ',
                  30: 'I<SUB>yy</SUB>', 31: 'I<SUB>zz</SUB>', 32: 'I<SUB>yz</SUB>', 33: 'Q<SUB>y</SUB>', 34: 'Q<SUB>z</SUB>', 35: '\u03b2<SUB>y</SUB>', 36: '\u03b2<SUB>z</SUB>', 37: '\u03b2<SUB>\u03c9</SUB>', 38: 'A<SUB>yy</SUB>',
                  39: 'A<SUB>zz</SUB>', 40: 'y<SUB>sc</SUB>',
                  41: 'z<SUB>sc</SUB>', 42: 'S<SUB>yy</SUB>', 43: 'S<SUB>zz</SUB>', 44: 'Z<SUB>yy</SUB>', 45: 'Z<SUB>zz</SUB>', 46: 'r<SUB>y</SUB>', 47: 'r<SUB>z</SUB>', 48: 'k<SUB>y</SUB>', 49: 'k<SUB>z</SUB>'}

        SPDescrip = {0: 'General', 1: 'Incline Angle (Deg.)', 2: 'Cross-Sectional Area', 3: 'Centroid of Y',
                     4: 'Centroid of Z', 5: 'Shear Centre of Y (Global)',
                     6: 'Shear Centre of Z (Global)', 7: 'Torsion Constant', 8: 'Warping Constant',
                     9: 'Principle Axis',
                     10: 'Moment of Inertia of v', 11: 'Moment of Inertia of w', 12: 'Static Moment of v',
                     13: 'Static Moment of w',
                     14: 'Wagner Coefficient of v', 15: 'Wagner Coefficient of w', 16: 'Wagner Coefficient of \u03c9',
                     17: 'Shear Area of v', 18: 'Shear Area of w', 19: 'Shear Centre of v', 20: 'Shear Centre of w',
                     21: 'Elastic Section Module of v', 22: 'Elastic Section Module of w',
                     23: 'Plastic Section Module of v', 24: 'Plastic Section Module of w',
                     25: 'Radius of Gyration of v', 26: 'Radius of Gyration of w', 27: 'Shear Coefficient of v',
                     28: 'Shear Coefficient of w',
                     29: 'Geometric Axis',
                     30: 'Moment of Inertia of y', 31: 'Moment of Inertia of z', 32: 'Product of Inertia',
                     33: 'Static Moment of y', 34: 'Static Moment of z', 35: 'Wagner Coefficient of y',
                     36: 'Wagner Coefficient of z', 37: 'Wagner Coefficient', 38: 'Shear Area of y',
                     39: 'Shear Area of z', 40: 'Shear Centre of y', 41: 'Shear Centre of z',
                     42: 'Elastic Section Module of y', 43: 'Elastic Section Module of z',
                     44: 'Plastic Section Module of y', 45: 'Plastic Section Module of z',
                     46: 'Radius of Gyration of y', 47: 'Radius of Gyration of z', 48: 'Shear Coefficient of y',
                     49: 'Shear Coefficient of z'}
        self.SPtableWidget.setRowCount(0)
        self.SPtableWidget.setRowCount(len(SPType))
        self.SPtableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.SPtableWidget.verticalHeader().setVisible(False)
        # item = QTableWidgetItem()
        self.SPtableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignLeft)

        for ii in range(len(SPType)):
            label = QLabel()
            # set alignment to center
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("QLabel {color: black}")
            label.setText(SPType[ii])
            self.SPtableWidget.setCellWidget(ii, 1, label)
            item = QTableWidgetItem()
            self.SPtableWidget.setItem(ii, 2, item)
        #
        for ii in range(len(SPDescrip)):
            item = QTableWidgetItem()
            item.setText(SPDescrip[ii])
            # print("item = ", item.text())
            if item.text() == 'General' or item.text() == 'Principle Axis' or item.text() == 'Geometric Axis':
                # print(item)
                item.setBackground(QBrush(QColor(240, 240, 240)))
                item.setFont(QFont('Courier', 10, QFont.Black))
                self.SPtableWidget.setItem(ii, 0, item)
                self.SPtableWidget.setSpan(ii, 0, 1, 3)
            else:
                self.SPtableWidget.setItem(ii, 0, item)
        #
        Fontsize = self.StatusOutput.fontPointSize()
        # print("output text =", self.StatusOutput.toPlainText())
        # print("Font size =", Fontsize)
        self.FontSize_lineEdit.setText(str(9))  # Default font size
        self.FontSize_lineEdit.setReadOnly(True)
        self.FontSize_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MeshSize = 0
        #
        self.ResetPanel()
        # Instantialize Qtsignal class
        self.QtSignal = QtSignal()
        QtCore.QTimer.singleShot(0, self.StressAnalysis_toolButton.deleteLater)

    def showEvent(self, event):
        self.anim_show = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.anim_show.setDuration(500)
        self.anim_show.setStartValue(0.0)
        self.anim_show.setEndValue(1.0)
        self.anim_show.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.anim_show.start()
        super().showEvent(event)


    def ResetTable(self):
        # self.DelAllBottomItem()
        self.SegmenttableWidget.setRowCount(0)
        self.importDataToLineTable()
        self.PointtableWidget.setRowCount(0)
        self.importDataToPointTable()
        self.MattableWidget.setRowCount(0)
        self.importDataToMatTable()
        # msaModel.Node.Reset()
        # msaModel.Fiber.Reset()
        # self.StatusOutput.clear()
        self.ResetSPTable()
        self.ResetPlot()
        GlobalBuckling.Reset()
        SectProperty.Reset()
        FESectProperty.Reset()
        YieldSAnalResults.ResetAllResults()
        FEYieldSAnalResults.ResetAllResults()
        MomentCurvatureResults.ResetMyCurva()
        MomentCurvatureResults.ResetMzCurva()
        CompositeSectionModulus.ResetCompSectMod()


    def importDataToMatTable(self):
        try:
            self.MattableWidget.verticalHeader().hide()
            # self.MattableWidget.setColumnWidth(0,100)
            # matIDDict=msaModel.Mat.ID
            # TempmatIDDict = {v : k for k, v in matIDDict.items()}
            # print(TempmatIDDict)
            self.MattableWidget.setRowCount(0)
            icount = 0
            if self.Centerline_radioButton.isChecked():
                self.MattableWidget.setRowCount(msaModel.Mat.Count)
                for i in msaModel.Mat.ID:
                    for j in range(6):
                        Item = QTableWidgetItem('')
                        Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.MattableWidget.setItem(icount, j, Item)
                        if j == 0:
                            # print(Model.msaModel.Mat.ID)
                            # Item.setText(str(Model.msaModel.Mat.ID[matIDDict[i]]))
                            Item.setText(str(int(i)))
                        elif j == 1:
                            self.ColorButton = QtWidgets.QPushButton()
                            self.MattableWidget.setCellWidget(icount, j, self.ColorButton)
                            self.ColorButton.setObjectName('MatTableColorButton')
                            # print(msaModel.Mat.Color)
                            # self.ColorButton.setStyleSheet("QPushButton{background:" + f"{msaModel.Mat.Color[i]}" + "}")
                            self.ColorButton.setStyleSheet("QPushButton{background:" + f"{msaModel.Mat.Color[i]}" + "}")
                            self.ColorButton.clicked.connect(self.ShowColorDialog)
                            # Item.setText(str(Model.msaModel.Mat.E[i]))
                        elif j == 2:
                            Item.setText(str(msaModel.Mat.E[i]))
                        elif j == 3:
                            Item.setText(str(msaModel.Mat.nu[i]))
                        elif j == 4:
                            Item.setText(str(msaModel.Mat.Fy[i]))
                            Item.setText(str(msaModel.Mat.Fy[i]))
                        elif j == 5:
                            Item.setText(str(msaModel.Mat.eu[i]))
                    #
                    icount += 1
                # else:
                #     msaModel.Mat.Reset()
                #     return
            #
            elif self.Outline_radioButton.isChecked():

                self.MattableWidget.setRowCount(msaFEModel.Mat.Count)
                for i in msaFEModel.Mat.ID:
                    for j in range(6):
                        Item = QTableWidgetItem('')
                        Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.MattableWidget.setItem(icount, j, Item)
                        if j == 0:
                            Item.setText(str(int(i)))
                        elif j == 1:
                            self.ColorButton = QtWidgets.QPushButton()
                            self.MattableWidget.setCellWidget(icount, j, self.ColorButton)
                            self.ColorButton.setObjectName('MatTableColorButton')
                            # print(msaFEModel.Mat.Color)
                            self.ColorButton.setStyleSheet(
                                "QPushButton{background:" + f"{msaFEModel.Mat.Color[i]}" + "}")
                            self.ColorButton.clicked.connect(self.ShowColorDialog)
                        elif j == 2:
                            Item.setText(str(msaFEModel.Mat.E[i]))
                        elif j == 3:
                            Item.setText(str(msaFEModel.Mat.nu[i]))
                        elif j == 4:
                            Item.setText(str(msaFEModel.Mat.Fy[i]))
                            Item.setText(str(msaFEModel.Mat.Fy[i]))
                        elif j == 5:
                            Item.setText(str(msaFEModel.Mat.eu[i]))
                    icount += 1
                # else:
                #     msaFEModel.Mat.Reset()
                #     return

            self.MattableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.MattableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        except:
            traceback.print_exc()

    def importDataToPointTable(self):
        try:
            self.PointtableWidget.verticalHeader().hide()
            self.PointtableWidget.setRowCount(0)
            icount = 0
            if self.Centerline_radioButton.isChecked():
                for i in msaModel.Point.ID:
                    # self.PointtableWidget.setColumnCount(4)
                    self.PointtableWidget.setColumnCount(3)
                    self.PointtableWidget.setRowCount(msaModel.Point.Count)
                    # self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z', 'Residual Stress'])
                    self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
                    for j in range(4):
                        Item = QTableWidgetItem()
                        Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.PointtableWidget.setItem(icount, j, Item)
                        if j == 0:
                            Item.setText(str(int(i)))
                        elif j == 1:
                            Item.setText(str(msaModel.Point.Yo[i]))
                        elif j == 2:
                            Item.setText(str(msaModel.Point.Zo[i]))
                        # elif j == 3:
                        #     Item.setText(str(msaModel.Point.stress[i]))
                    #
                    icount += 1
                # else:
                #     msaModel.Point.Reset()
                #     return
            elif self.Outline_radioButton.isChecked():
                for i in msaFEModel.Point.ID:
                    self.PointtableWidget.setColumnCount(3)
                    self.PointtableWidget.setRowCount(msaFEModel.Point.Count)
                    self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
                    for j in range(3):
                        Item = QTableWidgetItem()
                        Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.PointtableWidget.setItem(icount, j, Item)
                        if j == 0:
                            Item.setText(str(int(i)))
                        elif j == 1:
                            Item.setText(str(msaFEModel.Point.Yo[i]))
                        elif j == 2:
                            Item.setText(str(msaFEModel.Point.Zo[i]))
                    icount += 1
                # else:
                #     msaFEModel.Point.Reset()
                #     return
            # self.nodeTable.resizeColumnsToContents()
            # self.nodeTable.resizeRowsToContents()
            self.PointtableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.PointtableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        except:
            traceback.print_exc()

    def importDataToLineTable(self):
        try:
            self.SegmenttableWidget.verticalHeader().hide()
            # self.SegmenttableWidget.setColumnWidth(0, 100)
            # segmentIDDict = msaModel.Segment.ID
            # TempsegmentIDDict = {v: k for k, v in segmentIDDict.items()}
            # print(msaModel.Segment.MatID)
            # print(msaModel.Segment.PointI)
            self.SegmenttableWidget.setRowCount(0)
            icount = 0
            # colname = '#878787'  # default

            if self.Centerline_radioButton.isChecked():
                self.SegmenttableWidget.setColumnCount(5)
                self.SegmenttableWidget.setRowCount(msaModel.Segment.Count)
                self.SegmenttableWidget.setHorizontalHeaderLabels(['ID', 'Material', 'I', 'J', 'Thickness'])
                self.SegmentgroupBox.setTitle('Centerline')
                for i in msaModel.Segment.ID:
                    for j in range(5):
                        Item = QTableWidgetItem()
                        Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.SegmenttableWidget.setItem(icount, j, Item)
                        if j == 0:
                            # Item.setText(str(int(TempsegmentIDDict[i])))
                            Item.setText(str(int(i)))
                        elif j == 1:
                            # self.ColorButton = QtWidgets.QPushButton()
                            # self.SegmenttableWidget.setCellWidget(icount, j, self.ColorButton)
                            # self.ColorButton.setObjectName('ColorButton')
                            # self.ColorButton.setStyleSheet("QPushButton{background:" + f"{colname}" + "}")
                            # self.ColorButton.clicked.connect(self.ShowSegColorDialog)
                            Item.setText(str(int(msaModel.Segment.MatID[i])))
                        elif j == 2:
                            # Item.setText(str(int(msaModel.Segment.MatID[i])))
                            Item.setText(str(int(msaModel.Segment.PointI[i])))
                        elif j == 3:
                            # Item.setText(str(int(msaModel.Segment.PointI[i])))
                            Item.setText(str(int(msaModel.Segment.PointJ[i])))
                        elif j == 4:
                            # Item.setText(str(int(msaModel.Segment.PointJ[i])))
                            Item.setText(str(msaModel.Segment.SegThick[i]))
                        # elif j == 5:
                        #     Item.setText(str(msaModel.Segment.SegThick[i]))
                    #
                    icount += 1
            elif self.Outline_radioButton.isChecked():
                self.SegmenttableWidget.setColumnCount(5)
                self.SegmenttableWidget.setRowCount(msaFEModel.Loop.Count)
                self.SegmenttableWidget.setHorizontalHeaderLabels(['Group', 'Loop', 'Material', 'Type', 'Points'])
                self.SegmentgroupBox.setTitle('Outline')
                while icount < msaFEModel.Loop.Count:
                    for i in msaFEModel.Group.ID:
                        for j in msaFEModel.Group.LoopID[i]:
                            for k in range(5):
                                Item = QTableWidgetItem()
                                Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                self.SegmenttableWidget.setItem(icount, k, Item)
                                if k == 0:
                                    Item.setText(str(int(i)))
                                elif k == 1:
                                    Item.setText(str(int(j)))
                                elif k == 2:
                                    Item.setText(str(int(msaFEModel.Group.MatID[i])))
                                elif k == 3:
                                    if msaFEModel.Outline.Type[msaFEModel.Loop.OutlineID[j][0]] == "S":
                                        Item.setText("Solid")
                                    elif msaFEModel.Outline.Type[msaFEModel.Loop.OutlineID[j][0]] == "O":
                                        Item.setText("Opening")
                                elif k == 4:
                                    Loop = []
                                    Point = msaFEModel.Loop.PointID[j]
                                    Loop.append(Point[0])
                                    for ii in range(len(Point) - 1):
                                        Loop.append(Point[len(Point) - 1 - ii])
                                    Item.setText(",".join(str(int(i)) for i in Loop))
                            icount += 1
            self.SegmenttableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.SegmenttableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        except:
            traceback.print_exc()

    def ShowColorDialog(self):
        try:
            col = QColorDialog.getColor()
            if QColor.isValid(col) == False:
                pass
            else:
                colname = col.name()
                senderButton = self.sender()
                senderButtonName = senderButton.objectName()
                senderButton.setText('')
                senderButton.setStyleSheet(f"QPushButton#{senderButtonName}{{background:{colname}}}")
                if self.Centerline_radioButton.isChecked():
                    msaModel.Mat.Color[
                        int(self.MattableWidget.item(self.MattableWidget.currentRow(), 0).text())] = colname
                elif self.Outline_radioButton.isChecked():
                    msaFEModel.Mat.Color[
                        int(self.MattableWidget.item(self.MattableWidget.currentRow(), 0).text())] = colname
                self.ResetPlot()
        except:
            traceback.print_exc()

    @Slot()
    def on_PointgroupBox_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(str)
    def on_PointtableWidget_objectNameChanged(self, objectName):
        """
        Slot documentation goes here.

        @param objectName DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(str)
    def on_PointtableWidget_windowTitleChanged(self, title):
        """
        Slot documentation goes here.

        @param title DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(str)
    def on_PointtableWidget_windowIconTextChanged(self, iconText):
        """
        Slot documentation goes here.

        @param iconText DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot()
    def on_PointAddpushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        Ui = PointAddDialog(self)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
        self.ResetPanel()
        self.ResetPlot()

    @Slot()
    def on_PointModifypushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        currentRow = self.PointtableWidget.currentRow()
        RowIDitem = self.PointtableWidget.item(currentRow, 0)
        if RowIDitem is not None:
            id = int(self.PointtableWidget.item(currentRow, 0).text())
            Ui = PointModifyDialog(self, id)
            Signal = Ui.exec()
            if Signal:
                Status.Saved = 0
                Status.Meshed = 0
                Status.SP = 0
                Status.YS = 0
                Status.MC = 0
                self.ResetPanel()
                self.ResetPlot()
        else:
            self.StatusOutput.append(QTime.currentTime().toString() + ": Please select one row in Point table firstly!")
            return

    @Slot()
    def on_PointDeletepushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        currentRow = self.PointtableWidget.currentRow()
        if currentRow != -1:
            id = int(self.PointtableWidget.item(currentRow, 0).text())
            if (id in msaModel.Segment.PointI.values() or id in msaModel.Segment.PointJ.values()):
                showMesbox(self, 'Present Point has been used in existed Segment!')
                return
            elif (id in msaFEModel.Outline.PointI.values() or id in msaFEModel.Outline.PointJ.values() ):
                showMesbox(self, 'Present Point has been used in existed Outline!')
                return
            else:
                mesBox = QMessageBox()
                mesBox.setWindowTitle('Reminder')
                mesBox.setText(
                    'Are you sure you want to delete?')
                mesBox.setIcon(mesBox.Icon.Warning)
                mesBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
                buttonNo = mesBox.button(QMessageBox.StandardButton.No)
                mesBox.exec()
                if mesBox.clickedButton() == buttonYes:
                    if self.Centerline_radioButton.isChecked()== True:
                        id = int(self.PointtableWidget.item(currentRow, 0).text())
                        msaModel.Point.Remove(id)
                    elif self.Outline_radioButton.isChecked()== True:
                        id = int(self.PointtableWidget.item(currentRow, 0).text())
                        msaFEModel.Point.Remove(id)
                    self.ResetTable()
                    self.View.autoRange()
                    self.ResetPanel()
                    self.ResetPlot()

    @Slot()
    def on_MatAddpushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.Centerline_radioButton.isChecked() and msaModel.Mat.Count >= 1:
            showMesbox(self, 'Centerline model is restricted to single material only!')
        else:
            Ui = MatAdd_Dialog(self)
            # print(Model.msaModel.Mat.ID)
            if Ui.exec():
                Status.Saved = 0
            self.ResetPanel()

    @Slot()
    def on_SegAddpushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.Centerline_radioButton.isChecked() == True:
            Ui = SegmentAddDialog(self)
        elif self.Outline_radioButton.isChecked() == True:
            Ui = OutlineAdd_Dialog(self)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
        self.ResetPanel()
        self.ResetPlot()

    @Slot()
    def on_MatDeletepushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        currentRow = self.MattableWidget.currentRow()
        if currentRow != -1:
            id = int(self.MattableWidget.item(currentRow, 0).text())
            if self.Centerline_radioButton.isChecked() and id in msaModel.Segment.MatID.values():
                showMesbox(self, 'Present Material has been used in existed Segment!')
                return
            elif self.Outline_radioButton.isChecked() and id in msaFEModel.Group.MatID.values():
                showMesbox(self, 'Present Material has been used in existed Outline!')
                return
            mesBox = QMessageBox()
            mesBox.setWindowTitle('Reminder')
            mesBox.setText(
                'Are you sure you want to delete?')
            mesBox.setIcon(mesBox.Icon.Warning)
            mesBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
            buttonNo = mesBox.button(QMessageBox.StandardButton.No)
            mesBox.exec()
            if mesBox.clickedButton() == buttonYes:
                id = int(self.MattableWidget.item(currentRow, 0).text())
                if self.Centerline_radioButton.isChecked()== True:
                    msaModel.Mat.Remove(id)
                elif self.Outline_radioButton.isChecked()== True:
                    msaFEModel.Mat.Remove(id)
                self.ResetTable()
                self.View.autoRange()
                Status.Saved = 0
                self.ResetPanel()

    @Slot()
    def on_SegDeletepushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        currentRow = self.SegmenttableWidget.currentRow()
        if currentRow != -1:
            mesBox = QMessageBox()
            mesBox.setWindowTitle('Reminder')
            mesBox.setText(
                'Are you sure you want to delete?')
            mesBox.setIcon(mesBox.Icon.Warning)
            mesBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
            buttonNo = mesBox.button(QMessageBox.StandardButton.No)
            mesBox.exec()
            if mesBox.clickedButton() == buttonYes:
                if self.Centerline_radioButton.isChecked():
                    id = int(self.SegmenttableWidget.item(currentRow, 0).text())
                    msaModel.Segment.Remove(id)
                elif self.Outline_radioButton.isChecked():
                    idG = int(self.SegmenttableWidget.item(currentRow, 0).text())
                    idL = int(self.SegmenttableWidget.item(currentRow, 1).text())
                    OUT = msaFEModel.Loop.OutlineID[idL]
                    for i in range(len(OUT)):
                        msaFEModel.Outline.Remove(int(OUT[i]))
                    msaFEModel.Loop.Remove(idL)
                    msaFEModel.Group.LoopID[idG].remove(idL)
                    if not len(msaFEModel.Group.LoopID[idG]):
                        msaFEModel.Group.Remove(idG)
                self.ResetTable()
                self.View.autoRange()
                Status.Saved = 0
                Status.Meshed = 0
                Status.SP = 0
                Status.YS = 0
                Status.MC = 0
                self.ResetPanel()
                self.ResetPlot()

    @Slot()
    def on_Open_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        SlotFuncInMainWindow.OpenFile(self)
        Status.SP = 0
        Status.Meshed = 0
        Status.YS = 0
        Status.MC = 0
        self.ResetTable()
        self.View.autoRange()
        self.ResetPanel()
        self.ResetPlot()

    @Slot()
    def on_Save_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        SlotFuncInMainWindow.SaveFile(self, 2)

    @Slot()
    def on_New_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        SlotFuncInMainWindow.NewFile(self)

    def OutSPtoMW(self):
        if Status.SP:
            if self.Centerline_radioButton.isChecked():
                if abs(SectProperty.phi) < 0.0001: SectProperty.phi = 0.0
                self.SPtableWidget.item(1, 2).setText(self.NumberSetting.format(np.rad2deg(SectProperty.phi)))
                self.SPtableWidget.item(2, 2).setText(self.NumberSetting.format(SectProperty.Area))
                if abs(SectProperty.ygc) < 0.0001: SectProperty.ygc = 0.0
                self.SPtableWidget.item(3, 2).setText(self.NumberSetting.format(SectProperty.ygc))
                if abs(SectProperty.zgc) < 0.0001: SectProperty.zgc = 0.0
                self.SPtableWidget.item(4, 2).setText(self.NumberSetting.format(SectProperty.zgc))
                if abs(SectProperty.ysc) < 0.0001: SectProperty.ysc = 0.0
                self.SPtableWidget.item(5, 2).setText(self.NumberSetting.format(SectProperty.ysc + SectProperty.ygc))
                if abs(SectProperty.zsc) < 0.0001: SectProperty.zsc = 0.0
                self.SPtableWidget.item(6, 2).setText(self.NumberSetting.format(SectProperty.zsc + SectProperty.zgc))
                self.SPtableWidget.item(7, 2).setText(self.NumberSetting.format(SectProperty.J))
                self.SPtableWidget.item(8, 2).setText(self.NumberSetting.format(SectProperty.Cw))
                ##
                self.SPtableWidget.item(10, 2).setText(self.NumberSetting.format(SectProperty.Ivv))
                self.SPtableWidget.item(11, 2).setText(self.NumberSetting.format(SectProperty.Iww))
                self.SPtableWidget.item(12, 2).setText(self.NumberSetting.format(SectProperty.Qv))
                self.SPtableWidget.item(13, 2).setText(self.NumberSetting.format(SectProperty.Qw))
                if abs(SectProperty.Betav) < 0.0001: SectProperty.Betav = 0.0
                if abs(SectProperty.Betaw) < 0.0001: SectProperty.Betaw = 0.0
                if abs(SectProperty.Betaω) < 0.001: SectProperty.Betaω = 0.0
                self.SPtableWidget.item(14, 2).setText(self.NumberSetting.format(SectProperty.Betav))
                self.SPtableWidget.item(15, 2).setText(self.NumberSetting.format(SectProperty.Betaw))
                self.SPtableWidget.item(16, 2).setText(self.NumberSetting.format(SectProperty.Betaω))
                # self.SPtableWidget.item(17, 2).setText("    -")
                # self.SPtableWidget.item(18, 2).setText("    -")
                self.SPtableWidget.item(17, 2).setText(self.NumberSetting.format(SectProperty.Avv))
                self.SPtableWidget.item(18, 2).setText(self.NumberSetting.format(SectProperty.Aww))
                self.SPtableWidget.item(19, 2).setText(self.NumberSetting.format(SectProperty.vsc))
                self.SPtableWidget.item(20, 2).setText(self.NumberSetting.format(SectProperty.wsc))
                self.SPtableWidget.item(21, 2).setText(self.NumberSetting.format(SectProperty.Svv))
                self.SPtableWidget.item(22, 2).setText(self.NumberSetting.format(SectProperty.Sww))
                self.SPtableWidget.item(23, 2).setText(self.NumberSetting.format(SectProperty.Zvv))
                self.SPtableWidget.item(24, 2).setText(self.NumberSetting.format(SectProperty.Zww))
                self.SPtableWidget.item(25, 2).setText(self.NumberSetting.format(SectProperty.rv))
                self.SPtableWidget.item(26, 2).setText(self.NumberSetting.format(SectProperty.rw))
                # self.SPtableWidget.item(27, 2).setText("    -")
                # self.SPtableWidget.item(28, 2).setText("    -")
                self.SPtableWidget.item(27, 2).setText(self.NumberSetting.format(SectProperty.kv))
                self.SPtableWidget.item(28, 2).setText(self.NumberSetting.format(SectProperty.kw))
                ##
                self.SPtableWidget.item(30, 2).setText(self.NumberSetting.format(SectProperty.Iyy))
                self.SPtableWidget.item(31, 2).setText(self.NumberSetting.format(SectProperty.Izz))
                if abs(SectProperty.Iyz) < 0.0001: SectProperty.Iyz = 0.0
                self.SPtableWidget.item(32, 2).setText(self.NumberSetting.format(SectProperty.Iyz))
                self.SPtableWidget.item(33, 2).setText(self.NumberSetting.format(SectProperty.Qy))
                self.SPtableWidget.item(34, 2).setText(self.NumberSetting.format(SectProperty.Qz))
                if abs(SectProperty.Betay) < 0.0001: SectProperty.Betay = 0.0
                if abs(SectProperty.Betaz) < 0.0001: SectProperty.Betaz = 0.0
                self.SPtableWidget.item(35, 2).setText(self.NumberSetting.format(SectProperty.Betay))
                self.SPtableWidget.item(36, 2).setText(self.NumberSetting.format(SectProperty.Betaz))
                self.SPtableWidget.item(37, 2).setText(self.NumberSetting.format(SectProperty.Betaω))
                # self.SPtableWidget.item(38, 2).setText("    -")
                # self.SPtableWidget.item(39, 2).setText("    -")
                self.SPtableWidget.item(38, 2).setText(self.NumberSetting.format(SectProperty.Ayy))
                self.SPtableWidget.item(39, 2).setText(self.NumberSetting.format(SectProperty.Azz))
                self.SPtableWidget.item(40, 2).setText(self.NumberSetting.format(SectProperty.ysc))
                self.SPtableWidget.item(41, 2).setText(self.NumberSetting.format(SectProperty.zsc))
                self.SPtableWidget.item(42, 2).setText(self.NumberSetting.format(SectProperty.Syy))
                self.SPtableWidget.item(43, 2).setText(self.NumberSetting.format(SectProperty.Szz))
                self.SPtableWidget.item(44, 2).setText(self.NumberSetting.format(SectProperty.Zyy))
                self.SPtableWidget.item(45, 2).setText(self.NumberSetting.format(SectProperty.Zzz))
                self.SPtableWidget.item(46, 2).setText(self.NumberSetting.format(SectProperty.ry))
                self.SPtableWidget.item(47, 2).setText(self.NumberSetting.format(SectProperty.rz))
                # self.SPtableWidget.item(48, 2).setText("    -")
                # self.SPtableWidget.item(49, 2).setText("    -")
                self.SPtableWidget.item(48, 2).setText(self.NumberSetting.format(SectProperty.ky))
                self.SPtableWidget.item(49, 2).setText(self.NumberSetting.format(SectProperty.kz))
                ext_y = max(max(i) for i in CMSectModel.Segment.eCorner_y.values()) - \
                        min(min(i) for i in CMSectModel.Segment.eCorner_y.values())
                ext_z = max(max(i) for i in CMSectModel.Segment.eCorner_z.values()) - \
                        min(min(i) for i in CMSectModel.Segment.eCorner_z.values())
                ext_v = max(max(i) for i in CMSectModel.Segment.eCorner_v.values()) - \
                        min(min(i) for i in CMSectModel.Segment.eCorner_v.values())
                ext_w = max(max(i) for i in CMSectModel.Segment.eCorner_w.values()) - \
                        min(min(i) for i in CMSectModel.Segment.eCorner_w.values())
                if (abs(SectProperty.Betay) < 0.001 * ext_z and abs(SectProperty.Betaz) < 0.001 * ext_y or
                    abs(SectProperty.Betav) < 0.001 * ext_w and abs(SectProperty.Betaw) < 0.001 * ext_v) and \
                        SectProperty.Betaω == 0:
                    self.sect_type_label.setLabel("SS | DS", labelOpts={"offset": (0, -0.5)})
                elif (abs(SectProperty.Betay) >= 0.001 * ext_z and abs(SectProperty.Betaz) < 0.001 * ext_y or
                      abs(SectProperty.Betay) < 0.001 * ext_z and abs(SectProperty.Betaz) >= 0.001 * ext_y or
                      abs(SectProperty.Betav) >= 0.001 * ext_w and abs(SectProperty.Betaw) < 0.001 * ext_v or
                      abs(SectProperty.Betav) < 0.001 * ext_w and abs(SectProperty.Betaw) >= 0.001 * ext_v) and \
                        SectProperty.Betaω == 0:
                    self.sect_type_label.setLabel("SS | SS", labelOpts={"offset": (0, -0.5)})
                elif (abs(SectProperty.Betay) < 0.001 * ext_z and abs(SectProperty.Betaz) < 0.001 * ext_y or
                      abs(SectProperty.Betav) < 0.001 * ext_w and abs(SectProperty.Betaw) < 0.001 * ext_v) and \
                        SectProperty.Betaω != 0:
                    self.sect_type_label.setLabel("SS | RS", labelOpts={"offset": (0, -0.5)})
                else:
                    self.sect_type_label.setLabel("SS | NS", labelOpts={"offset": (0, -0.5)})

            elif self.Outline_radioButton.isChecked():
                if abs(FESectProperty.Theta) < 0.0001: FESectProperty.Theta = 0.0
                self.SPtableWidget.item(1, 2).setText(self.NumberSetting.format(np.rad2deg(FESectProperty.Theta)))
                self.SPtableWidget.item(2, 2).setText(self.NumberSetting.format(FESectProperty.Area))
                if abs(FESectProperty.cy) < 0.0001: FESectProperty.cy = 0.0
                if abs(FESectProperty.cz) < 0.0001: FESectProperty.cz = 0.0
                self.SPtableWidget.item(3, 2).setText(self.NumberSetting.format(FESectProperty.cy))
                self.SPtableWidget.item(4, 2).setText(self.NumberSetting.format(FESectProperty.cz))
                if abs(FESectProperty.cys) < 0.0001: FESectProperty.cys = 0.0
                if abs(FESectProperty.czs) < 0.0001: FESectProperty.czs = 0.0
                self.SPtableWidget.item(5, 2).setText(self.NumberSetting.format(FESectProperty.cys))
                self.SPtableWidget.item(6, 2).setText(self.NumberSetting.format(FESectProperty.czs))
                self.SPtableWidget.item(7, 2).setText(self.NumberSetting.format(FESectProperty.J))
                self.SPtableWidget.item(8, 2).setText(self.NumberSetting.format(FESectProperty.Iomg))
                ##
                self.SPtableWidget.item(10, 2).setText(self.NumberSetting.format(FESectProperty.Iv))
                self.SPtableWidget.item(11, 2).setText(self.NumberSetting.format(FESectProperty.Iw))
                self.SPtableWidget.item(12, 2).setText(self.NumberSetting.format(FESectProperty.Qv))
                self.SPtableWidget.item(13, 2).setText(self.NumberSetting.format(FESectProperty.Qw))
                if abs(FESectProperty.Betav) < 0.0001: FESectProperty.Betav = 0.0
                if abs(FESectProperty.Betaw) < 0.0001: FESectProperty.Betaw = 0.0
                if abs(FESectProperty.Betaomg) < 0.001: FESectProperty.Betaomg = 0.0
                self.SPtableWidget.item(14, 2).setText(self.NumberSetting.format(FESectProperty.Betav))
                self.SPtableWidget.item(15, 2).setText(self.NumberSetting.format(FESectProperty.Betaw))
                self.SPtableWidget.item(16, 2).setText(self.NumberSetting.format(FESectProperty.Betaomg))
                self.SPtableWidget.item(17, 2).setText(self.NumberSetting.format(FESectProperty.Avv))
                self.SPtableWidget.item(18, 2).setText(self.NumberSetting.format(FESectProperty.Aww))
                if abs(FESectProperty.cvs) < 0.0001: FESectProperty.cvs = 0.0
                if abs(FESectProperty.cws) < 0.0001: FESectProperty.cws = 0.0
                self.SPtableWidget.item(19, 2).setText(self.NumberSetting.format(FESectProperty.cvs))
                self.SPtableWidget.item(20, 2).setText(self.NumberSetting.format(FESectProperty.cws))
                if msaFEModel.Mat.Count == 1:
                    self.SPtableWidget.item(21, 2).setText(self.NumberSetting.format(FESectProperty.Sv))
                    self.SPtableWidget.item(22, 2).setText(self.NumberSetting.format(FESectProperty.Sw))
                    self.SPtableWidget.item(23, 2).setText(self.NumberSetting.format(FESectProperty.Zv))
                    self.SPtableWidget.item(24, 2).setText(self.NumberSetting.format(FESectProperty.Zw))
                else:
                    self.SPtableWidget.item(21, 2).setText(self.NumberSetting.format(FESectProperty.Sv))
                    self.SPtableWidget.item(22, 2).setText(self.NumberSetting.format(FESectProperty.Sw))
                    self.SPtableWidget.item(23, 2).setText(self.NumberSetting.format(FESectProperty.Zv))
                    self.SPtableWidget.item(24, 2).setText(self.NumberSetting.format(FESectProperty.Zw))
                self.SPtableWidget.item(25, 2).setText(self.NumberSetting.format(FESectProperty.rv))
                self.SPtableWidget.item(26, 2).setText(self.NumberSetting.format(FESectProperty.rw))
                self.SPtableWidget.item(27, 2).setText(self.NumberSetting.format(FESectProperty.kv))
                self.SPtableWidget.item(28, 2).setText(self.NumberSetting.format(FESectProperty.kw))
                ##
                self.SPtableWidget.item(30, 2).setText(self.NumberSetting.format(FESectProperty.Iyc))
                self.SPtableWidget.item(31, 2).setText(self.NumberSetting.format(FESectProperty.Izc))
                self.SPtableWidget.item(32, 2).setText(self.NumberSetting.format(FESectProperty.Iyzc))
                self.SPtableWidget.item(33, 2).setText(self.NumberSetting.format(FESectProperty.Qy))
                self.SPtableWidget.item(34, 2).setText(self.NumberSetting.format(FESectProperty.Qz))
                if abs(FESectProperty.Betay) < 0.0001: FESectProperty.Betay = 0.0
                if abs(FESectProperty.Betaz) < 0.0001: FESectProperty.Betaz = 0.0
                self.SPtableWidget.item(35, 2).setText(self.NumberSetting.format(FESectProperty.Betay))
                self.SPtableWidget.item(36, 2).setText(self.NumberSetting.format(FESectProperty.Betaz))
                self.SPtableWidget.item(37, 2).setText(self.NumberSetting.format(FESectProperty.Betaomg))
                self.SPtableWidget.item(38, 2).setText(self.NumberSetting.format(FESectProperty.Ayy))
                self.SPtableWidget.item(39, 2).setText(self.NumberSetting.format(FESectProperty.Azz))
                if abs(FESectProperty.ysc) < 0.0001: FESectProperty.ysc = 0.0
                if abs(FESectProperty.zsc) < 0.0001: FESectProperty.zsc = 0.0
                self.SPtableWidget.item(40, 2).setText(self.NumberSetting.format(FESectProperty.ysc))
                self.SPtableWidget.item(41, 2).setText(self.NumberSetting.format(FESectProperty.zsc))
                if msaFEModel.Mat.Count == 1:
                    self.SPtableWidget.item(42, 2).setText(self.NumberSetting.format(FESectProperty.Sy))
                    self.SPtableWidget.item(43, 2).setText(self.NumberSetting.format(FESectProperty.Sz))
                    self.SPtableWidget.item(44, 2).setText(self.NumberSetting.format(FESectProperty.Zy))
                    self.SPtableWidget.item(45, 2).setText(self.NumberSetting.format(FESectProperty.Zz))
                else:
                    self.SPtableWidget.item(42, 2).setText(self.NumberSetting.format(FESectProperty.Sy))
                    self.SPtableWidget.item(43, 2).setText(self.NumberSetting.format(FESectProperty.Sz))
                    self.SPtableWidget.item(44, 2).setText(self.NumberSetting.format(FESectProperty.Zy))
                    self.SPtableWidget.item(45, 2).setText(self.NumberSetting.format(FESectProperty.Zz))
                self.SPtableWidget.item(46, 2).setText(self.NumberSetting.format(FESectProperty.ry))
                self.SPtableWidget.item(47, 2).setText(self.NumberSetting.format(FESectProperty.rz))
                self.SPtableWidget.item(48, 2).setText(self.NumberSetting.format(FESectProperty.ky))
                self.SPtableWidget.item(49, 2).setText(self.NumberSetting.format(FESectProperty.kz))
                ext_y = max(Model.Point.Y.values()) - min(Model.Point.Y.values())
                ext_z = max(Model.Point.Z.values()) - min(Model.Point.Z.values())
                ext_v = max(Model.Node.V.values()) - min(Model.Node.V.values())
                ext_w = max(Model.Node.W.values()) - min(Model.Node.W.values())
                if len(set(msaFEModel.Group.MatID.values())) == 1:
                    if (abs(FESectProperty.Betay) < 0.001 * ext_z and abs(FESectProperty.Betaz) < 0.001 * ext_y or
                        abs(FESectProperty.Betav) < 0.001 * ext_w and abs(FESectProperty.Betaw) < 0.001 * ext_v) and \
                            FESectProperty.Betaomg == 0:
                        self.sect_type_label.setLabel("SS | DS", labelOpts={"offset": (0, -0.5)})
                    elif (abs(FESectProperty.Betay) >= 0.001 * ext_z and abs(FESectProperty.Betaz) < 0.001 * ext_y or
                          abs(FESectProperty.Betay) < 0.001 * ext_z and abs(FESectProperty.Betaz) >= 0.001 * ext_y or
                          abs(FESectProperty.Betav) >= 0.001 * ext_w and abs(FESectProperty.Betaw) < 0.001 * ext_v or
                          abs(FESectProperty.Betav) < 0.001 * ext_w and abs(FESectProperty.Betaw) >= 0.001 * ext_v) and \
                            FESectProperty.Betaomg == 0:
                        self.sect_type_label.setLabel("SS | SS", labelOpts={"offset": (0, -0.5)})
                    elif (abs(FESectProperty.Betay) < 0.001 * ext_z and abs(FESectProperty.Betaz) < 0.001 * ext_y or
                          abs(FESectProperty.Betav) < 0.001 * ext_w and abs(FESectProperty.Betaw) < 0.001 * ext_v) and \
                            FESectProperty.Betaomg != 0:
                        self.sect_type_label.setLabel("SS | RS", labelOpts={"offset": (0, -0.5)})
                    else:
                        self.sect_type_label.setLabel("SS | NS", labelOpts={"offset": (0, -0.5)})
                else:
                    if (abs(FESectProperty.Betay) < 0.001 * ext_z and abs(FESectProperty.Betaz) < 0.001 * ext_y or
                        abs(FESectProperty.Betav) < 0.001 * ext_w and abs(FESectProperty.Betaw) < 0.001 * ext_v) and \
                            FESectProperty.Betaomg == 0:
                        self.sect_type_label.setLabel("CS | DS", labelOpts={"offset": (0, -0.5)})
                    elif (abs(FESectProperty.Betay) >= 0.001 * ext_z and abs(FESectProperty.Betaz) < 0.001 * ext_y or
                          abs(FESectProperty.Betay) < 0.001 * ext_z and abs(FESectProperty.Betaz) >= 0.001 * ext_y or
                          abs(FESectProperty.Betav) >= 0.001 * ext_w and abs(FESectProperty.Betaw) < 0.001 * ext_v or
                          abs(FESectProperty.Betav) < 0.001 * ext_w and abs(FESectProperty.Betaw) >= 0.001 * ext_v) and \
                            FESectProperty.Betaomg == 0:
                        self.sect_type_label.setLabel("CS | SS", labelOpts={"offset": (0, -0.5)})
                    elif (abs(FESectProperty.Betay) < 0.001 * ext_z and abs(FESectProperty.Betaz) < 0.001 * ext_y or
                          abs(FESectProperty.Betav) < 0.001 * ext_w and abs(FESectProperty.Betaw) < 0.001 * ext_v) and \
                            FESectProperty.Betaomg != 0:
                        self.sect_type_label.setLabel("CS | RS", labelOpts={"offset": (0, -0.5)})
                    else:
                        self.sect_type_label.setLabel("CS | NS", labelOpts={"offset": (0, -0.5)})
        return

    def ModifyMatInfo(self):
        currentRow = self.MattableWidget.currentRow()
        RowIDitem = self.MattableWidget.item(currentRow, 0)
        # print("test item = ", RowIDitem)
        if RowIDitem is None:
            return
        else:
            row = RowIDitem.row()
            # print("Test row = ", row)

    def ResetSPTable(self):
        row_count = self.SPtableWidget.rowCount()
        for i in range(0, row_count):
            self.SPtableWidget.item(i, 2).setText("")
        return

    @Slot()
    def on_MatModifypushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        currentRow = self.MattableWidget.currentRow()
        RowIDitem = self.MattableWidget.item(currentRow, 0)
        # print("Test RowIDitem = ",RowIDitem.text())
        if RowIDitem is not None:
            id = int(RowIDitem.text())
            Ui = MatModifyDialog(self, id)
            Signal = Ui.exec()
            if Signal:
                Status.Saved = 0
                Status.SP = 0
                Status.YS = 0
                Status.MC = 0
                self.ResetPanel()
        else:
            self.StatusOutput.append(QTime.currentTime().toString() + ": Please select one row in Material table firstly!")
            return

    @Slot()
    def on_SegModifypushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        currentRow = self.SegmenttableWidget.currentRow()
        RowIDitem = self.SegmenttableWidget.item(currentRow, 0)
        if RowIDitem is not None:
            if self.Centerline_radioButton.isChecked()== True:
                id = int(self.SegmenttableWidget.item(currentRow, 0).text())
                Ui = SegmentModifyDialog(self, id)
                Signal = Ui.exec()
                if Signal:
                    Status.Saved = 0
                    Status.Meshed = 0
                    Status.SP = 0
                    Status.YS = 0
                    Status.MC = 0
                    self.ResetPanel()
                    self.ResetPlot()
            elif self.Outline_radioButton.isChecked()== True:
                idG = int(self.SegmenttableWidget.item(currentRow, 0).text())
                idL = int(self.SegmenttableWidget.item(currentRow, 1).text())
                Ui = OutlineModify_Dialog(self, idG, idL)
                Signal = Ui.exec()
                if Signal:
                    Status.Saved = 0
                    Status.Meshed = 0
                    Status.SP = 0
                    Status.YS = 0
                    Status.MC = 0
                    self.ResetPanel()
                    self.ResetPlot()
        else:
            self.StatusOutput.append(QTime.currentTime().toString() + ": Please select one row in Segment table firstly!")
            return

    @Slot()
    def on_Cleartext_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.StatusOutput.clear()
        tWelcomeInfo = WelcomeInfo.Welcome.PrintWelcomeInfo(self)
        self.StatusOutput.setText(tWelcomeInfo)

    def ResetPanel(self):
        self.ShowGrid_checkBox.setChecked(True)
        if self.Centerline_radioButton.isChecked():
            if msaModel.Mat.Count:
                self.ShowMatID_checkBox.setEnabled(True)
            else:
                self.ShowMatID_checkBox.setChecked(False)
                self.ShowMatID_checkBox.setEnabled(False)
            if msaModel.Point.Count:
                self.ShowPointID_checkBox.setEnabled(True)
                self.ShowCoord_checkBox.setEnabled(True)
            else:
                self.ShowPointID_checkBox.setChecked(False)
                self.ShowCoord_checkBox.setChecked(False)
                self.ShowPointID_checkBox.setEnabled(False)
                self.ShowCoord_checkBox.setEnabled(False)
            if msaModel.Segment.Count:
                self.ShowLineID_checkBox.setEnabled(True)
            else:
                self.ShowLineID_checkBox.setChecked(False)
                self.ShowLineID_checkBox.setEnabled(False)
        elif self.Outline_radioButton.isChecked():
            if msaFEModel.Mat.Count:
                self.ShowMatID_checkBox.setEnabled(True)
            else:
                self.ShowMatID_checkBox.setChecked(False)
                self.ShowMatID_checkBox.setEnabled(False)
            if msaFEModel.Point.Count:
                self.ShowPointID_checkBox.setEnabled(True)
                self.ShowCoord_checkBox.setEnabled(True)
            else:
                self.ShowPointID_checkBox.setChecked(False)
                self.ShowCoord_checkBox.setChecked(False)
                self.ShowPointID_checkBox.setEnabled(False)
                self.ShowCoord_checkBox.setEnabled(False)
            if msaFEModel.Outline.Count:
                self.ShowLineID_checkBox.setEnabled(True)
            else:
                self.ShowLineID_checkBox.setChecked(False)
                self.ShowLineID_checkBox.setEnabled(False)
        if Status.Meshed:
            self.ShowFiber_checkBox.setEnabled(True)
            self.ShowFiber_checkBox.setChecked(True)
        else:
            self.ShowFiber_checkBox.setChecked(False)
            self.ShowFiber_checkBox.setEnabled(False)
        if Status.SP:
            self.ShowGC_checkBox.setEnabled(True)
            self.ShowSC_checkBox.setEnabled(True)
            self.ShowPrincipleAxis_checkBox.setEnabled(True)
        else:
            self.ShowGC_checkBox.setChecked(False)
            self.ShowSC_checkBox.setChecked(False)
            self.ShowPrincipleAxis_checkBox.setChecked(False)
            self.ShowGC_checkBox.setEnabled(False)
            self.ShowSC_checkBox.setEnabled(False)
            self.ShowPrincipleAxis_checkBox.setEnabled(False)

    def ResetPlot(self):
        self.View.clear()
        if self.ShowGrid_checkBox.isChecked():
            self.View.showGrid(x=True, y=True, alpha=0.3)
        else:
            self.View.showGrid(x=False, y=False)
        if self.Centerline_radioButton.isChecked():
            CenterlinePlot(self.View)
        elif self.Outline_radioButton.isChecked():
            OutlinePlot(self.View)
        if self.ShowFiber_checkBox.isChecked():
            FiberPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowPrincipleAxis_checkBox.isChecked():
            PAPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowOrigin_checkBox.isChecked():
            OriginPlot(self.View)
        if self.ShowGC_checkBox.isChecked():
            GCPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowSC_checkBox.isChecked():
            SCPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowCoord_checkBox.isChecked():
            CoordPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowPointID_checkBox.isChecked():
            PointIDPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowLineID_checkBox.isChecked():
            LineIDPlot(self.View, self.Centerline_radioButton.isChecked())
        if self.ShowMatID_checkBox.isChecked():
            MatIDPlot(self.View, self.Centerline_radioButton.isChecked())
        if not Status.SP:
            self.sect_type_label.setLabel("")


    @Slot()
    def on_graphicsView_destroyed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(str)
    def on_graphicsView_objectNameChanged(self, objectName):
        """
        Slot documentation goes here.

        @param objectName DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(str)
    def on_graphicsView_windowTitleChanged(self, title):
        """
        Slot documentation goes here.

        @param title DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(QIcon)
    def on_graphicsView_windowIconChanged(self, icon):
        """
        Slot documentation goes here.

        @param icon DESCRIPTION
        @type QIcon
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot(str)
    def on_graphicsView_windowIconTextChanged(self, iconText):
        """
        Slot documentation goes here.

        @param iconText DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    # @Slot(QPoint)
    # def on_graphicsView_customContextMenuRequested(self, pos):
    #     """
    #     Slot documentation goes here.
    #
    #     @param pos DESCRIPTION
    #     @type QPoint
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError

    @Slot()
    def on_ISection_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = ISection_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_TSection_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = TSection_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_ZSection_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = ZSection_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_LSection_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = LSection_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_HollowRec_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowRec_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_HollowTrap_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowTrap_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_CSection_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = CSection_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_HollowCircle_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowCircle_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_SolidCircle_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet

        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = SolidCircle_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_SolidRec_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = SolidRec_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_TaperedTee_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = TaperedTee_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_SolidTrap_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = SolidTrap_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_SolidTri_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = SolidTri_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()


    @Slot()
    def on_SolidPoly_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = SolidPoly_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_HollowTri_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # self.Outline_radioButton.setChecked(True)
        Ui = HollowTri_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_TaperedI_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = TaperedI_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_BuldTee_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = BuldTee_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_HollowPoly_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        #self.Outline_radioButton.setChecked(True)
        Ui = HollowPoly_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_BoxGirder_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = BoxGirder_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_FGCircle_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = FGCircle_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_FGRec_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = FGRec_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_FGI_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        self.Outline_radioButton.setChecked(True)
        Ui = FGI_Dialog(self)
        Ui.Methodsignal.connect(self.get_dialog_signal)
        if Ui.exec():
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
            self.ResetPanel()
            self.ResetPlot()
            self.View.autoRange()

    @Slot()
    def on_SPAnal_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        Ui = SectPropCal_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.exec()
        self.ResetPanel()
        self.ResetPlot()

    def FEMeshCancel(self):
        Status.Meshed = 0
        Status.SP = 0
        Status.YS = 0
        Status.MC = 0
        Model.Material.Reset()
        Model.Point.Reset()
        Model.Outline.Reset()
        Model.Group.Reset()
        Model.Node.Reset()
        Model.Segment.Reset()
        Model.Fiber.Reset()
        Model.TempNode.Reset()
        Model.TempFiber.Reset()
        self.ResetPanel()
        self.ResetPlot()
        self.StatusOutput.append(QTime.currentTime().toString() + ": Mesh Generation Canceled!" + '\r\n')

    def FEMeshFinish(self):
        Status.Meshed = 1
        Status.SP = 0
        Status.YS = 0
        Status.MC = 0
        self.ResetPanel()
        self.ResetPlot()
        self.StatusOutput.append(QTime.currentTime().toString() + ": Mesh Generated Successfully!" + '\r\n')

    @Slot()
    def on_YSAnal_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # print("msaModel.Fiber.ID = ", msaModel.Fiber.ID)
        Ui = YieldSurfacesAnal_Dialog(self, parent=self)
        # print(Model.msaModel.Mat.ID)
        Ui.exec()

    @Slot()
    def on_GlobalBuckling_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # print("msaModel.Fiber.ID = ", msaModel.Fiber.ID)
        Ui = GlobalBucklingAnal_Dialog(self, parent=self)
        # print(Model.msaModel.Mat.ID)
        Ui.exec()

    @Slot()
    def on_ShowGrid_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowPointID_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowLineID_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowMatID_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowCoord_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowPrincipleAxis_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowSC_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowGC_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowOrigin_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_ShowFiber_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ResetPlot()

    @Slot()
    def on_LocalBuckling_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = LocalBucklingAnalDialog(self)
        Ui.exec()

    @Slot()
    def on_Centerline_radioButton_toggled(self):
        self.Centerline_label.setPixmap(QPixmap('ui/ico/CM_2.png'))
        self.Outline_label.setPixmap(QPixmap('ui/ico/FE.png'))

    @Slot()
    def on_Outline_radioButton_toggled(self):
        self.Centerline_label.setPixmap(QPixmap('ui/ico/CM.png'))
        self.Outline_label.setPixmap(QPixmap('ui/ico/FE_2.png'))

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if msaFEModel.Point.ID or msaFEModel.Outline.ID or msaFEModel.Mat.ID:
            # print("Test msaModel.Point =", msaModel.Point.ID)
            # print("Test msaModel.Segment =", msaModel.Segment.ID)
            # print("Type msaModel.Point =", type(msaModel.Point.ID))
            mesBox = QMessageBox()
            mesBox.setWindowTitle('Change Modeling Type')
            mesBox.setText('Existed data will be clear. <br> Are you sure you want to change modeling type?')
            mesBox.setWindowIcon(QIcon(r'ui/ico/Msa_Sect2.png'))
            mesBox.setIcon(mesBox.Icon.Question)
            mesBox.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            mesBox.setStyleSheet("QPushButton:hover{background-color: rgb(144, 200, 246);}\n"
                                 "QMessageBox {background: White;}\n"
                                 "QPushButton {background: White;border:1px solid;width:69px;height:22px}\n"
                                 "QPushButton:pressed{padding-left:3px;padding-top:3px;}")
            buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
            buttonNo = mesBox.button(QMessageBox.StandardButton.No)
            #buttonCancel = mesBox.button(QMessageBox.StandardButton.Cancel)
            mesBox.exec()
            if mesBox.clickedButton() == buttonYes:
                mesBox2 = QMessageBox()
                mesBox2.setWindowTitle('Confirmation')
                mesBox2.setText('Please confirm again, you want to change modeling type?')
                mesBox2.setWindowIcon(QIcon(r'ui/ico/Msa_Sect2.png'))
                mesBox2.setIcon(mesBox.Icon.Question)
                mesBox2.setStandardButtons(
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                mesBox2.setStyleSheet("QPushButton:hover{background-color: rgb(144, 200, 246);}\n"
                                      "QMessageBox {background: White;}\n"
                                      "QPushButton {background: White;border:1px solid;width:69px;height:22px}\n"
                                      "QPushButton:pressed{padding-left:3px;padding-top:3px;}")
                button2Yes = mesBox2.button(QMessageBox.StandardButton.Yes)
                button2No = mesBox2.button(QMessageBox.StandardButton.No)
                mesBox2.exec()
                if mesBox2.clickedButton() == button2Yes:
                    self.StatusOutput.append(QTime.currentTime().toString() + ': Change Modeling Type Successfully! Please mind your input data.')
                    # self.PointtableWidget.setColumnCount(4)
                    # self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z', 'Residual Stress'])
                    self.PointtableWidget.setColumnCount(3)
                    self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
                    self.SegmentgroupBox.setTitle('Centerline')
                    self.SegmenttableWidget.setColumnCount(5)
                    self.SegmenttableWidget.setHorizontalHeaderLabels(['ID', 'Material', 'I', 'J', 'Thickness'])
                    # Empty existed data
                    msaModel.ResetAll()
                    msaFEModel.ResetAll()
                    self.StatusOutput.clear()
                    tWelcomeInfo = WelcomeInfo.Welcome.PrintWelcomeInfo(self)
                    self.StatusOutput.setFont(QFont('Courier', 9))
                    self.StatusOutput.setText(tWelcomeInfo)
                    self.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections')
                    self.SectIDInput_lineEdit.setText("Section 01")
                    self.SectNameInput_lineEdit.setText("MsaSect Section")
                    Status.NewFile = 1
                    Status.Saved = 0
                    Status.Meshed = 0
                    Status.SP = 0
                    Status.YS = 0
                    Status.MC = 0
                    self.ResetPanel()
                    self.ResetTable()
                elif mesBox2.clickedButton() == button2No:
                    self.Outline_radioButton.setChecked(True)
                    return
                # self.ResetPlot()
                # self.StatusOutput.append('Change Modeling Type Successfully! Please mind your input data.')
            elif mesBox.clickedButton() == buttonNo:
                self.Outline_radioButton.setChecked(True)
                return
        ##
        else:
            # print("msaModel.Point=", "Test msaModel")
            self.Centerline_radioButton.setChecked(True)
            self.ResetPlot()
            # self.PointtableWidget.setColumnCount(4)
            # self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z', 'Residual Stress'])
            self.PointtableWidget.setColumnCount(3)
            self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
            self.SegmentgroupBox.setTitle('Centerline')
            self.SegmenttableWidget.setColumnCount(5)
            self.SegmenttableWidget.setHorizontalHeaderLabels(['ID', 'Material', 'I', 'J', 'Thickness'])
            Status.NewFile = 1
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
        return

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if msaModel.Point.ID or msaModel.Segment.ID or msaModel.Mat.ID:
            mesBox = QMessageBox()
            mesBox.setWindowTitle('Change Modeling Type')
            mesBox.setText('Existed data will be clear. <br> Are you sure you want to change modeling type?')
            mesBox.setWindowIcon(QIcon(r'ui/ico/Msa_Sect2.png'))
            mesBox.setIcon(mesBox.Icon.Question)
            mesBox.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            mesBox.setStyleSheet("QPushButton:hover{background-color: rgb(144, 200, 246);}\n"
                                 "QMessageBox {background: White;}\n"
                                 "QPushButton {background: White;border:1px solid;width:69px;height:22px}\n"
                                 "QPushButton:pressed{padding-left:3px;padding-top:3px;}")
            buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
            buttonNo = mesBox.button(QMessageBox.StandardButton.No)
            buttonCancel = mesBox.button(QMessageBox.StandardButton.Cancel)
            mesBox.exec()
            if mesBox.clickedButton() == buttonYes:
                mesBox2 = QMessageBox()
                mesBox2.setWindowTitle('Confirmation')
                mesBox2.setText('Please confirm again, you want to change modeling type?')
                mesBox2.setWindowIcon(QIcon(r'ui/ico/Msa_Sect2.png'))
                mesBox2.setIcon(mesBox.Icon.Question)
                mesBox2.setStandardButtons(
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                mesBox2.setStyleSheet("QPushButton:hover{background-color: rgb(144, 200, 246);}\n"
                                      "QMessageBox {background: White;}\n"
                                      "QPushButton {background: White;border:1px solid;width:69px;height:22px}\n"
                                      "QPushButton:pressed{padding-left:3px;padding-top:3px;}")
                button2Yes = mesBox2.button(QMessageBox.StandardButton.Yes)
                button2No = mesBox2.button(QMessageBox.StandardButton.No)
                mesBox2.exec()
                if mesBox2.clickedButton() == button2Yes:
                    self.StatusOutput.append(QTime.currentTime().toString() + ': Change Modeling Type Successfully! Please mind your input data.')
                    self.SegmenttableWidget.setColumnCount(5)
                    self.SegmenttableWidget.setHorizontalHeaderLabels(['Group', 'Loop', 'Material', 'Type', 'Points'])
                    self.PointtableWidget.setColumnCount(3)
                    self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
                    self.SegmentgroupBox.setTitle('Outline')
                    # Empty existed data
                    msaModel.ResetAll()
                    msaFEModel.ResetAll()
                    self.StatusOutput.clear()
                    tWelcomeInfo = WelcomeInfo.Welcome.PrintWelcomeInfo(self)
                    self.StatusOutput.setFont(QFont('Courier', 9))
                    self.StatusOutput.setText(tWelcomeInfo)
                    self.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections')
                    self.SectIDInput_lineEdit.setText("Section 01")
                    self.SectNameInput_lineEdit.setText("MsaSect Section")
                    Status.NewFile = 1
                    Status.Saved = 0
                    Status.Meshed = 0
                    Status.SP = 0
                    Status.YS = 0
                    Status.MC = 0
                    self.ResetPanel()
                    self.ResetTable()
                elif mesBox2.clickedButton() == button2No:
                    self.Centerline_radioButton.setChecked(True)
                    return
                # self.ResetPlot()
                # self.StatusOutput.append('Change Modeling Type Successfully! Please mind your input data.')
            elif mesBox.clickedButton() == buttonNo:
                self.Centerline_radioButton.setChecked(True)
                return
        else:
            # print("msaModel.Point=", "Test msaModel")
            self.Outline_radioButton.setChecked(True)
            self.ResetPlot()
            self.SegmenttableWidget.setColumnCount(5)
            self.SegmenttableWidget.setHorizontalHeaderLabels(['Group', 'Loop', 'Material', 'Type', 'Points'])
            self.PointtableWidget.setColumnCount(3)
            self.PointtableWidget.setHorizontalHeaderLabels(['ID', 'Y', 'Z'])
            self.SegmentgroupBox.setTitle('Outline')
            Status.NewFile = 1
            Status.Saved = 0
            Status.Meshed = 0
            Status.SP = 0
            Status.YS = 0
            Status.MC = 0
        return

    @Slot()
    def on_SaveAs_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        SlotFuncInMainWindow.SaveAsFile(self, 2)

    @Slot()
    def on_About_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        AboutUi = AboutDialog(WelcomeInfo.Welcome.LatestVersion)
        AboutUi.exec()

    @Slot()
    def on_Savetext_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        DirFile, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save Output Text", self.cwd, "Text Files (*.txt)")
        # print("Current Save DataFilePath=", DirFile)
        if DirFile == "":
            self.StatusOutput.append(QTime.currentTime().toString() + ": Cancel save output text file!")
            return
        else:
            fileinfo = QFileInfo(DirFile)
            tfilename = fileinfo.baseName()
            # tfilesuff = fileinfo.suffix()
            # print("File basename=", tfilename)
            # print("Filename suffix=", tfilesuff)
            # with open((str(tfilename) + '-Result output.txt'), 'w', encoding='utf-8') as f:
            with open((DirFile + '-Result output.txt'), 'w', encoding='utf-8') as f:
                f.write(self.StatusOutput.toPlainText())
            self.StatusOutput.append(QTime.currentTime().toString() + (': The log results have been successfully saved.'))

    @Slot()
    def on_SmallFontSize_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        tFontsize = self.FontSize_lineEdit.text()
        # print("Current font size = ", tFontsize)
        tCurFontsize = int(tFontsize) - 1
        # self.StatusOutput.setFont(QFont('Courier', tCurFontsize, QFont.Black))
        self.StatusOutput.setFont(QFont('Courier', tCurFontsize))
        self.FontSize_lineEdit.setText(str(tCurFontsize))

    @Slot()
    def on_NormalFontSize_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # self.StatusOutput.setFont(QFont('Courier', 9, QFont.Black))
        self.StatusOutput.setFont(QFont('Courier', 9))
        self.FontSize_lineEdit.setText(str(9))

    @Slot()
    def on_LargeFontSize_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        tFontsize = self.FontSize_lineEdit.text()
        # print("Current font size = ", tFontsize)
        tCurFontsize = int(tFontsize) + 1
        # self.StatusOutput.setFont(QFont('Courier', tCurFontsize, QFont.Black))
        self.StatusOutput.setFont(QFont('Courier', tCurFontsize))
        self.FontSize_lineEdit.setText(str(tCurFontsize))

    @Slot()
    def on_Fit2Screen_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.View.autoRange()

    @Slot()
    def on_Mesh_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            if self.Centerline_radioButton.isChecked():
                if msaModel.Segment.Count == 0:
                    showMesbox(self, 'Centerline model required!')
                else:
                    MeshGenCM()
                    Status.Meshed = 1
                    self.ResetPanel()
                    showMesbox(self, 'Meshing completed.')
                    self.ResetPlot()
                    ## For test Fiber
                    # TTTYc = [888] * len(msaModel.Fiber.ID)
                    # TTTZc = [888] * len(msaModel.Fiber.ID)
                    # TTTFMatID = [888] * len(msaModel.Fiber.ID)
                    # TTTFArea = [888] * len(msaModel.Fiber.ID)
                    # for ii in msaModel.Fiber.ID:
                    #     TTTYc[ii-1] = msaModel.Fiber.Yc[ii]
                    #     TTTZc[ii-1] = msaModel.Fiber.Zc[ii]
                    #     TTTFMatID[ii-1] = msaModel.Fiber.FMatID[ii]
                    #     TTTFArea[ii-1] = msaModel.Fiber.FArea[ii]
                    #
                    # print("msaModel.Fiber.Yc = ", TTTYc)
                    # print("msaModel.Fiber.Zc", TTTZc)
                    # print("msaModel.Fiber.FMatID", TTTFMatID)
                    # print("msaModel.Fiber.FArea", TTTFArea)
                    self.StatusOutput.append(QTime.currentTime().toString() + ": Mesh Generated Successfully!" + "\r\n")

            elif self.Outline_radioButton.isChecked():
                if msaFEModel.Group.Count == 0:
                    showMesbox(self, 'Outline model required!')
                else:
                    Ui = meshSettings_Dialog(self)
                    Ui_MP = MeshProgress_Dialog(self)
                    Ui.OK_Signal.connect(Ui_MP.GetMeshSize)
                    if Ui.exec():
                        Ui_MP.StartMeshGenFE()
                        Ui_MP.exec()
        except:
            traceback.print_exc()


    @Slot()
    def on_Model3DView_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if (self.Centerline_radioButton.isChecked() and msaModel.Segment.Count) or\
            (self.Outline_radioButton.isChecked() and msaFEModel.Group.Count):
            try:
                Ui = Model3DViewDialog(self)
                Ui.exec()
            except:
                showMesbox(self, "Please check the model!")
        else:
            showMesbox(self, "Please generate a model first!")

    @Slot()
    def on_StressAnalysis_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = StressAnalysisAnalDialog()
        Ui.exec()

    @Slot()
    def on_MomentCurvature_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = MomentCurvatureAnalDialog(parent=self)
        Ui.exec()

    def get_dialog_signal(self, connect):
        if not connect:
            self.Centerline_radioButton.setChecked(True)
        elif connect:
            self.Outline_radioButton.setChecked(True)

    @Slot()
    def on_UserManual_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            user_manual_path = os.path.join(os.getcwd(), "help", "Msasect2 User Manual-v1.0.pdf")
            if os.path.exists(user_manual_path):
                if sys.platform.startswith('darwin'):
                    subprocess.run(['open', user_manual_path])
                elif sys.platform.startswith('win32'):
                    webbrowser.open(user_manual_path, new=2)
                else:
                    showMesbox(self, 'Unsupported platform!')
            else:
                showMesbox(self, 'Please check whether the user manual exists!')
        except:
            traceback.print_exc()

    @Slot()
    def on_Export_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if Status.SP:
            output = ""
            try:
                fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", self.cwd, "Text Files (*.txt)")
                if self.Centerline_radioButton.isChecked():
                    output = CMpl().SectProps(CMSectModel)
                elif self.Outline_radioButton.isChecked():
                    output = BPRes.AddResult(FESectProperty)
                with codecs.open(fileName, 'w', 'utf-8') as f:
                    f.write(output)
                print("\nSection properties exported successfully!\n{}".format(fileName))
            except:
                showMesbox(self, "Please check your settings!")
        else:
            showMesbox(self, "Please calculate section properties first!")

    @Slot()
    def on_Clear_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.ResetSPTable()

    @Slot()
    def on_Setting_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = NumberSetting_Dialog(self, parent=self)
        Ui.exec()

