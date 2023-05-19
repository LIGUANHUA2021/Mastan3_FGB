# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
                               QFrame, QGridLayout, QGroupBox, QHBoxLayout,
                               QHeaderView, QLabel, QLayout, QLineEdit,
                               QMainWindow, QPushButton, QRadioButton, QSizePolicy,
                               QSpacerItem, QSplitter, QStatusBar, QTabWidget,
                               QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
                               QToolButton, QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget
from gui.msasect.base.OutputRedir import CallableEvent


class CustomTextBrowser(QTextBrowser):
    def event(self, event):
        if isinstance(event, CallableEvent):
            event.execute()
            return True
        return super().event(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setStyleSheet(u"\n"
                                 "QMainWindow\n"
                                 "{\n"
                                 "	background-color: rgb(43, 43, 43);\n"
                                 "}\n"
                                 "QCheckBox\n"
                                 "{\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QCheckBox:disabled\n"
                                 "{\n"
                                 "	color: rgb(80, 80, 80);\n"
                                 "}\n"
                                 "QCheckBox::indicator:disabled\n"
                                 "{\n"
                                 "	background-color: rgb(160, 160, 160);\n"
                                 "    border-radius: 3px;\n"
                                 "}\n"
                                 "QGroupBox\n"
                                 "{\n"
                                 "	background-color: rgb(128, 128, 128);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "	border-radius: 3px;\n"
                                 "}\n"
                                 "QLineEdit:hover\n"
                                 "{\n"
                                 "	background-color: rgb(244, 244, 244);\n"
                                 "}\n"
                                 "QLabel\n"
                                 "{\n"
                                 "	color: rgb(250, 250, 250);\n"
                                 "}\n"
                                 "QPushButton\n"
                                 "{\n"
                                 "	background-color: rgb(255, 255, 255);\n"
                                 "	border-radius: 3px;\n"
                                 "}\n"
                                 "QPushButton:hover\n"
                                 "{\n"
                                 "	background-color: rgb(144, 200, 246);\n"
                                 "}\n"
                                 "QPushButton:pressed\n"
                                 "{\n"
                                 "    padding-left: 3px;\n"
                                 "    padding-top: 3px;\n"
                                 "}\n"
                                 "QPushButton:disabled\n"
                                 "{\n"
                                 "	background-color: rgb(160, 160, 160);\n"
                                 "	color: rgb(80, 80, 80);\n"
                                 "}\n"
                                 "QSplitter::handle\n"
                                 "{\n"
                                 "	background-color: transparent;\n"
                                 ""
                                 "}\n"
                                 "QSplitter::handle:hover\n"
                                 "{\n"
                                 "	background-color: rgb(80, 80, 80);\n"
                                 "}\n"
                                 "QSplitter::handle:pressed\n"
                                 "{\n"
                                 "	background-color: rgb(180, 180, 180);\n"
                                 "}\n"
                                 "QTextBrowser\n"
                                 "{\n"
                                 "	background-color: rgb(43, 43, 43);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QTabWidget::pane\n"
                                 "{\n"
                                 "	background: rgb(128, 128, 128);\n"
                                 "    border: None;\n"
                                 "}\n"
                                 "QTabWidget>QTabBar::tab\n"
                                 "{\n"
                                 "	background: rgb(244, 244, 244);\n"
                                 "	border-top-left-radius: 5px;\n"
                                 "	border-top-right-radius: 5px;\n"
                                 "	padding-left: 6px;\n"
                                 "	padding-right: 6px;\n"
                                 "	padding-top: 3px;\n"
                                 "	padding-bottom: 3px;\n"
                                 "}\n"
                                 "QTabWidget>QTabBar::tab:!selected\n"
                                 "{\n"
                                 "	border-right: 1px solid rgb(196, 196, 196);\n"
                                 "}\n"
                                 "QTabWidget>QTabBar::tab:selected\n"
                                 "{\n"
                                 "	background: rgb(128, 128, 128);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "	padding-left: 8px;\n"
                                 "	padding-right: 8px;\n"
                                 "}\n"
                                 "QToolButton\n"
                                 "{\n"
                                 "	border-radius: 5px;\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QToolButton:hover\n"
                                 "{\n"
                                 "	background-color: rgba(255, 255, 255,"
                                 " 20%);\n"
                                 "}\n"
                                 "QToolButton:pressed\n"
                                 "{\n"
                                 "	background-color: rgba(0, 0, 0, 20%);\n"
                                 "	border-top: 1px solid rgba(0, 0, 0, 50%);\n"
                                 "	border-left: 1px solid rgba(0, 0, 0, 50%);\n"
                                 "	padding: 0;\n"
                                 "}\n"
                                 "#line, #line_2, #line_3, #line_4, #line_5, #line_6, #line_7\n"
                                 "{\n"
                                 "	background-color: rgb(255, 255, 255);\n"
                                 "	border: None;\n"
                                 "}")
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionInfo.setCheckable(True)
        font = QFont()
        self.actionInfo.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setCheckable(True)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionNew_2 = QAction(MainWindow)
        self.actionNew_2.setObjectName(u"actionNew_2")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionLine_ID = QAction(MainWindow)
        self.actionLine_ID.setObjectName(u"actionLine_ID")
        self.actionMaterial_ID = QAction(MainWindow)
        self.actionMaterial_ID.setObjectName(u"actionMaterial_ID")
        self.actionCoordinates = QAction(MainWindow)
        self.actionCoordinates.setObjectName(u"actionCoordinates")
        self.actionPrinciple_Axis = QAction(MainWindow)
        self.actionPrinciple_Axis.setObjectName(u"actionPrinciple_Axis")
        self.actionResidual_Stress = QAction(MainWindow)
        self.actionResidual_Stress.setObjectName(u"actionResidual_Stress")
        self.actionOrigin = QAction(MainWindow)
        self.actionOrigin.setObjectName(u"actionOrigin")
        self.actionShear_Center = QAction(MainWindow)
        self.actionShear_Center.setObjectName(u"actionShear_Center")
        self.actionYield_Surface = QAction(MainWindow)
        self.actionYield_Surface.setObjectName(u"actionYield_Surface")
        self.actionLocal_Bucklling = QAction(MainWindow)
        self.actionLocal_Bucklling.setObjectName(u"actionLocal_Bucklling")
        self.actionMoment_Curvature = QAction(MainWindow)
        self.actionMoment_Curvature.setObjectName(u"actionMoment_Curvature")
        self.actionExport_to_Mastan2 = QAction(MainWindow)
        self.actionExport_to_Mastan2.setObjectName(u"actionExport_to_Mastan2")
        self.actionExport_to_Mastan3 = QAction(MainWindow)
        self.actionExport_to_Mastan3.setObjectName(u"actionExport_to_Mastan3")
        self.actionSection_Properties_2 = QAction(MainWindow)
        self.actionSection_Properties_2.setObjectName(u"actionSection_Properties_2")
        self.actionYield_Surface_2 = QAction(MainWindow)
        self.actionYield_Surface_2.setObjectName(u"actionYield_Surface_2")
        self.actionMoment_Curvature_2 = QAction(MainWindow)
        self.actionMoment_Curvature_2.setObjectName(u"actionMoment_Curvature_2")
        self.actionGlobal_Buckling_2 = QAction(MainWindow)
        self.actionGlobal_Buckling_2.setObjectName(u"actionGlobal_Buckling_2")
        self.actionLocal_Bucklling_2 = QAction(MainWindow)
        self.actionLocal_Bucklling_2.setObjectName(u"actionLocal_Bucklling_2")
        self.actionLine_ID_2 = QAction(MainWindow)
        self.actionLine_ID_2.setObjectName(u"actionLine_ID_2")
        self.actionLine_ID_3 = QAction(MainWindow)
        self.actionLine_ID_3.setObjectName(u"actionLine_ID_3")
        self.actionMaterial_ID_2 = QAction(MainWindow)
        self.actionMaterial_ID_2.setObjectName(u"actionMaterial_ID_2")
        self.actionShow_Fiber = QAction(MainWindow)
        self.actionShow_Fiber.setObjectName(u"actionShow_Fiber")
        self.actionGeometric_Center = QAction(MainWindow)
        self.actionGeometric_Center.setObjectName(u"actionGeometric_Center")
        self.actionShear_Center_2 = QAction(MainWindow)
        self.actionShear_Center_2.setObjectName(u"actionShear_Center_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.VerticalLayout = QVBoxLayout(self.centralwidget)
        self.VerticalLayout.setObjectName(u"VerticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 90))
        self.tabWidget.setMaximumSize(QSize(16777215, 90))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.tabWidget.setFont(font1)
        self.Hometab = QWidget()
        self.Hometab.setObjectName(u"Hometab")
        self.horizontalLayout_5 = QHBoxLayout(self.Hometab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 1, -1, 1)
        self.New_toolButton = QToolButton(self.Hometab)
        self.New_toolButton.setObjectName(u"New_toolButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.New_toolButton.sizePolicy().hasHeightForWidth())
        self.New_toolButton.setSizePolicy(sizePolicy1)
        self.New_toolButton.setMinimumSize(QSize(40, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        self.New_toolButton.setFont(font2)
        self.New_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.New_toolButton)

        self.Open_toolButton = QToolButton(self.Hometab)
        self.Open_toolButton.setObjectName(u"Open_toolButton")
        sizePolicy1.setHeightForWidth(self.Open_toolButton.sizePolicy().hasHeightForWidth())
        self.Open_toolButton.setSizePolicy(sizePolicy1)
        self.Open_toolButton.setMinimumSize(QSize(40, 40))
        self.Open_toolButton.setFont(font2)
        self.Open_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Open_toolButton.setAutoRaise(False)

        self.horizontalLayout_5.addWidget(self.Open_toolButton)

        self.Save_toolButton = QToolButton(self.Hometab)
        self.Save_toolButton.setObjectName(u"Save_toolButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.Save_toolButton.sizePolicy().hasHeightForWidth())
        self.Save_toolButton.setSizePolicy(sizePolicy2)
        self.Save_toolButton.setMinimumSize(QSize(40, 40))
        self.Save_toolButton.setFont(font2)
        self.Save_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.Save_toolButton)

        self.SaveAs_toolButton = QToolButton(self.Hometab)
        self.SaveAs_toolButton.setObjectName(u"SaveAs_toolButton")
        sizePolicy1.setHeightForWidth(self.SaveAs_toolButton.sizePolicy().hasHeightForWidth())
        self.SaveAs_toolButton.setSizePolicy(sizePolicy1)
        self.SaveAs_toolButton.setMinimumSize(QSize(40, 40))
        self.SaveAs_toolButton.setFont(font2)
        self.SaveAs_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.SaveAs_toolButton)

        self.line = QFrame(self.Hometab)
        self.line.setObjectName(u"line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setMinimumSize(QSize(1, 55))
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_5.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.ShowMatID_checkBox = QCheckBox(self.Hometab)
        self.ShowMatID_checkBox.setObjectName(u"ShowMatID_checkBox")
        self.ShowMatID_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowMatID_checkBox, 0, 2, 1, 1)

        self.ShowPointID_checkBox = QCheckBox(self.Hometab)
        self.ShowPointID_checkBox.setObjectName(u"ShowPointID_checkBox")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.ShowPointID_checkBox.setFont(font3)

        self.gridLayout.addWidget(self.ShowPointID_checkBox, 0, 0, 1, 1)

        self.ShowCoord_checkBox = QCheckBox(self.Hometab)
        self.ShowCoord_checkBox.setObjectName(u"ShowCoord_checkBox")
        self.ShowCoord_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowCoord_checkBox, 0, 3, 1, 1)

        self.ShowLineID_checkBox = QCheckBox(self.Hometab)
        self.ShowLineID_checkBox.setObjectName(u"ShowLineID_checkBox")
        self.ShowLineID_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowLineID_checkBox, 0, 1, 1, 1)

        self.ShowPrincipleAxis_checkBox = QCheckBox(self.Hometab)
        self.ShowPrincipleAxis_checkBox.setObjectName(u"ShowPrincipleAxis_checkBox")
        self.ShowPrincipleAxis_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowPrincipleAxis_checkBox, 0, 4, 1, 1)

        self.ShowGrid_checkBox = QCheckBox(self.Hometab)
        self.ShowGrid_checkBox.setObjectName(u"ShowGrid_checkBox")
        self.ShowGrid_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowGrid_checkBox, 1, 0, 1, 1)

        self.ShowOrigin_checkBox = QCheckBox(self.Hometab)
        self.ShowOrigin_checkBox.setObjectName(u"ShowOrigin_checkBox")
        self.ShowOrigin_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowOrigin_checkBox, 1, 1, 1, 1)

        self.ShowGC_checkBox = QCheckBox(self.Hometab)
        self.ShowGC_checkBox.setObjectName(u"ShowGC_checkBox")
        self.ShowGC_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowGC_checkBox, 1, 2, 1, 1)

        self.ShowSC_checkBox = QCheckBox(self.Hometab)
        self.ShowSC_checkBox.setObjectName(u"ShowSC_checkBox")
        self.ShowSC_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowSC_checkBox, 1, 3, 1, 1)

        self.ShowFiber_checkBox = QCheckBox(self.Hometab)
        self.ShowFiber_checkBox.setObjectName(u"ShowFiber_checkBox")
        self.ShowFiber_checkBox.setFont(font2)

        self.gridLayout.addWidget(self.ShowFiber_checkBox, 1, 4, 1, 1)

        self.horizontalLayout_5.addLayout(self.gridLayout)

        self.Mesh_toolButton = QToolButton(self.Hometab)
        self.Mesh_toolButton.setObjectName(u"Mesh_toolButton")
        sizePolicy1.setHeightForWidth(self.Mesh_toolButton.sizePolicy().hasHeightForWidth())
        self.Mesh_toolButton.setSizePolicy(sizePolicy1)
        self.Mesh_toolButton.setMinimumSize(QSize(40, 40))
        self.Mesh_toolButton.setFont(font2)
        self.Mesh_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.Mesh_toolButton)

        self.Model3DView_toolButton = QToolButton(self.Hometab)
        self.Model3DView_toolButton.setObjectName(u"Model3DView_toolButton")
        sizePolicy1.setHeightForWidth(self.Model3DView_toolButton.sizePolicy().hasHeightForWidth())
        self.Model3DView_toolButton.setSizePolicy(sizePolicy1)
        self.Model3DView_toolButton.setMinimumSize(QSize(40, 40))
        self.Model3DView_toolButton.setFont(font2)
        self.Model3DView_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.Model3DView_toolButton)

        self.Fit2Screen_toolButton = QToolButton(self.Hometab)
        self.Fit2Screen_toolButton.setObjectName(u"Fit2Screen_toolButton")
        sizePolicy1.setHeightForWidth(self.Fit2Screen_toolButton.sizePolicy().hasHeightForWidth())
        self.Fit2Screen_toolButton.setSizePolicy(sizePolicy1)
        self.Fit2Screen_toolButton.setMinimumSize(QSize(40, 40))
        self.Fit2Screen_toolButton.setFont(font2)
        self.Fit2Screen_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.Fit2Screen_toolButton)

        self.line_2 = QFrame(self.Hometab)
        self.line_2.setObjectName(u"line_2")
        sizePolicy3.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy3)
        self.line_2.setMinimumSize(QSize(1, 55))
        self.line_2.setMaximumSize(QSize(1, 16777215))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.SPAnal_toolButton = QToolButton(self.Hometab)
        self.SPAnal_toolButton.setObjectName(u"SPAnal_toolButton")
        sizePolicy1.setHeightForWidth(self.SPAnal_toolButton.sizePolicy().hasHeightForWidth())
        self.SPAnal_toolButton.setSizePolicy(sizePolicy1)
        self.SPAnal_toolButton.setMinimumSize(QSize(40, 40))
        self.SPAnal_toolButton.setFont(font2)
        self.SPAnal_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.SPAnal_toolButton)

        self.YSAnal_toolButton = QToolButton(self.Hometab)
        self.YSAnal_toolButton.setObjectName(u"YSAnal_toolButton")
        sizePolicy1.setHeightForWidth(self.YSAnal_toolButton.sizePolicy().hasHeightForWidth())
        self.YSAnal_toolButton.setSizePolicy(sizePolicy1)
        self.YSAnal_toolButton.setMinimumSize(QSize(40, 40))
        self.YSAnal_toolButton.setFont(font2)
        self.YSAnal_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.YSAnal_toolButton)

        self.MomentCurvature_toolButton = QToolButton(self.Hometab)
        self.MomentCurvature_toolButton.setObjectName(u"MomentCurvature_toolButton")
        sizePolicy1.setHeightForWidth(self.MomentCurvature_toolButton.sizePolicy().hasHeightForWidth())
        self.MomentCurvature_toolButton.setSizePolicy(sizePolicy1)
        self.MomentCurvature_toolButton.setMinimumSize(QSize(40, 40))
        self.MomentCurvature_toolButton.setFont(font2)
        self.MomentCurvature_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.MomentCurvature_toolButton)

        self.GlobalBuckling_toolButton = QToolButton(self.Hometab)
        self.GlobalBuckling_toolButton.setObjectName(u"GlobalBuckling_toolButton")
        sizePolicy1.setHeightForWidth(self.GlobalBuckling_toolButton.sizePolicy().hasHeightForWidth())
        self.GlobalBuckling_toolButton.setSizePolicy(sizePolicy1)
        self.GlobalBuckling_toolButton.setMinimumSize(QSize(40, 40))
        self.GlobalBuckling_toolButton.setFont(font2)
        self.GlobalBuckling_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.GlobalBuckling_toolButton)

        self.LocalBuckling_toolButton = QToolButton(self.Hometab)
        self.LocalBuckling_toolButton.setObjectName(u"LocalBuckling_toolButton")
        sizePolicy1.setHeightForWidth(self.LocalBuckling_toolButton.sizePolicy().hasHeightForWidth())
        self.LocalBuckling_toolButton.setSizePolicy(sizePolicy1)
        self.LocalBuckling_toolButton.setMinimumSize(QSize(40, 40))
        self.LocalBuckling_toolButton.setFont(font2)
        self.LocalBuckling_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.LocalBuckling_toolButton)

        self.StressAnalysis_toolButton = QToolButton(self.Hometab)
        self.StressAnalysis_toolButton.setObjectName(u"StressAnalysis_toolButton")
        sizePolicy1.setHeightForWidth(self.StressAnalysis_toolButton.sizePolicy().hasHeightForWidth())
        self.StressAnalysis_toolButton.setSizePolicy(sizePolicy1)
        self.StressAnalysis_toolButton.setMinimumSize(QSize(40, 40))
        self.StressAnalysis_toolButton.setFont(font2)
        self.StressAnalysis_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.StressAnalysis_toolButton, 0, Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.line_7 = QFrame(self.Hometab)
        self.line_7.setObjectName(u"line_7")
        sizePolicy3.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy3)
        self.line_7.setMinimumSize(QSize(1, 55))
        self.line_7.setMaximumSize(QSize(1, 16777215))
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.VLine)

        self.horizontalLayout_5.addWidget(self.line_7)

        self.About_toolButton = QToolButton(self.Hometab)
        self.About_toolButton.setObjectName(u"About_toolButton")
        sizePolicy1.setHeightForWidth(self.About_toolButton.sizePolicy().hasHeightForWidth())
        self.About_toolButton.setSizePolicy(sizePolicy1)
        self.About_toolButton.setMinimumSize(QSize(40, 40))
        self.About_toolButton.setFont(font2)
        self.About_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.About_toolButton)

        self.tabWidget.addTab(self.Hometab, "")
        self.New_toolButton.raise_()
        self.Open_toolButton.raise_()
        self.Save_toolButton.raise_()
        self.SaveAs_toolButton.raise_()
        self.line.raise_()
        self.Mesh_toolButton.raise_()
        self.Fit2Screen_toolButton.raise_()
        self.line_2.raise_()
        self.SPAnal_toolButton.raise_()
        self.YSAnal_toolButton.raise_()
        self.LocalBuckling_toolButton.raise_()
        self.GlobalBuckling_toolButton.raise_()
        self.MomentCurvature_toolButton.raise_()
        self.Model3DView_toolButton.raise_()
        self.StressAnalysis_toolButton.raise_()
        self.About_toolButton.raise_()
        self.line_7.raise_()
        self.Templatetab = QWidget()
        self.Templatetab.setObjectName(u"Templatetab")
        self.horizontalLayout_7 = QHBoxLayout(self.Templatetab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(3, 1, -1, 1)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 3, -1, -1)
        self.ISection_toolButton = QToolButton(self.Templatetab)
        self.ISection_toolButton.setObjectName(u"ISection_toolButton")
        sizePolicy1.setHeightForWidth(self.ISection_toolButton.sizePolicy().hasHeightForWidth())
        self.ISection_toolButton.setSizePolicy(sizePolicy1)
        self.ISection_toolButton.setMinimumSize(QSize(40, 40))
        self.ISection_toolButton.setFont(font1)

        self.horizontalLayout_11.addWidget(self.ISection_toolButton)

        self.ZSection_toolButton = QToolButton(self.Templatetab)
        self.ZSection_toolButton.setObjectName(u"ZSection_toolButton")
        sizePolicy1.setHeightForWidth(self.ZSection_toolButton.sizePolicy().hasHeightForWidth())
        self.ZSection_toolButton.setSizePolicy(sizePolicy1)
        self.ZSection_toolButton.setMinimumSize(QSize(40, 40))
        self.ZSection_toolButton.setFont(font1)

        self.horizontalLayout_11.addWidget(self.ZSection_toolButton)

        self.TSection_toolButton = QToolButton(self.Templatetab)
        self.TSection_toolButton.setObjectName(u"TSection_toolButton")
        sizePolicy1.setHeightForWidth(self.TSection_toolButton.sizePolicy().hasHeightForWidth())
        self.TSection_toolButton.setSizePolicy(sizePolicy1)
        self.TSection_toolButton.setMinimumSize(QSize(40, 40))
        self.TSection_toolButton.setFont(font1)

        self.horizontalLayout_11.addWidget(self.TSection_toolButton)

        self.CSection_toolButton = QToolButton(self.Templatetab)
        self.CSection_toolButton.setObjectName(u"CSection_toolButton")
        sizePolicy1.setHeightForWidth(self.CSection_toolButton.sizePolicy().hasHeightForWidth())
        self.CSection_toolButton.setSizePolicy(sizePolicy1)
        self.CSection_toolButton.setMinimumSize(QSize(40, 40))
        self.CSection_toolButton.setFont(font1)

        self.horizontalLayout_11.addWidget(self.CSection_toolButton)

        self.LSection_toolButton = QToolButton(self.Templatetab)
        self.LSection_toolButton.setObjectName(u"LSection_toolButton")
        sizePolicy1.setHeightForWidth(self.LSection_toolButton.sizePolicy().hasHeightForWidth())
        self.LSection_toolButton.setSizePolicy(sizePolicy1)
        self.LSection_toolButton.setMinimumSize(QSize(40, 40))
        self.LSection_toolButton.setFont(font1)

        self.horizontalLayout_11.addWidget(self.LSection_toolButton)

        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.label_3 = QLabel(self.Templatetab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 16))
        self.label_3.setMaximumSize(QSize(16777215, 16))
        self.label_3.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_3)

        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.line_3 = QFrame(self.Templatetab)
        self.line_3.setObjectName(u"line_3")
        sizePolicy3.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy3)
        self.line_3.setMinimumSize(QSize(1, 55))
        self.line_3.setMaximumSize(QSize(1, 16777215))
        self.line_3.setLayoutDirection(Qt.LeftToRight)
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.VLine)

        self.horizontalLayout_7.addWidget(self.line_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 3, -1, -1)
        self.HollowCircle_toolButton = QToolButton(self.Templatetab)
        self.HollowCircle_toolButton.setObjectName(u"HollowCircle_toolButton")
        sizePolicy1.setHeightForWidth(self.HollowCircle_toolButton.sizePolicy().hasHeightForWidth())
        self.HollowCircle_toolButton.setSizePolicy(sizePolicy1)
        self.HollowCircle_toolButton.setMinimumSize(QSize(40, 40))
        self.HollowCircle_toolButton.setFont(font1)

        self.horizontalLayout_12.addWidget(self.HollowCircle_toolButton)

        self.HollowRec_toolButton = QToolButton(self.Templatetab)
        self.HollowRec_toolButton.setObjectName(u"HollowRec_toolButton")
        sizePolicy1.setHeightForWidth(self.HollowRec_toolButton.sizePolicy().hasHeightForWidth())
        self.HollowRec_toolButton.setSizePolicy(sizePolicy1)
        self.HollowRec_toolButton.setMinimumSize(QSize(40, 40))
        self.HollowRec_toolButton.setFont(font1)

        self.horizontalLayout_12.addWidget(self.HollowRec_toolButton)

        self.HollowTrap_toolButton = QToolButton(self.Templatetab)
        self.HollowTrap_toolButton.setObjectName(u"HollowTrap_toolButton")
        sizePolicy1.setHeightForWidth(self.HollowTrap_toolButton.sizePolicy().hasHeightForWidth())
        self.HollowTrap_toolButton.setSizePolicy(sizePolicy1)
        self.HollowTrap_toolButton.setMinimumSize(QSize(40, 40))
        self.HollowTrap_toolButton.setFont(font1)

        self.horizontalLayout_12.addWidget(self.HollowTrap_toolButton)

        self.HollowTri_toolButton = QToolButton(self.Templatetab)
        self.HollowTri_toolButton.setObjectName(u"HollowTri_toolButton")
        sizePolicy1.setHeightForWidth(self.HollowTri_toolButton.sizePolicy().hasHeightForWidth())
        self.HollowTri_toolButton.setSizePolicy(sizePolicy1)
        self.HollowTri_toolButton.setMinimumSize(QSize(40, 40))
        self.HollowTri_toolButton.setFont(font1)

        self.horizontalLayout_12.addWidget(self.HollowTri_toolButton)

        self.HollowPoly_toolButton = QToolButton(self.Templatetab)
        self.HollowPoly_toolButton.setObjectName(u"HollowPoly_toolButton")
        sizePolicy1.setHeightForWidth(self.HollowPoly_toolButton.sizePolicy().hasHeightForWidth())
        self.HollowPoly_toolButton.setSizePolicy(sizePolicy1)
        self.HollowPoly_toolButton.setMinimumSize(QSize(40, 40))
        self.HollowPoly_toolButton.setFont(font1)

        self.horizontalLayout_12.addWidget(self.HollowPoly_toolButton)

        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.label_4 = QLabel(self.Templatetab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 16))
        self.label_4.setMaximumSize(QSize(16777215, 16))
        self.label_4.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_4)

        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.line_4 = QFrame(self.Templatetab)
        self.line_4.setObjectName(u"line_4")
        sizePolicy3.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy3)
        self.line_4.setMinimumSize(QSize(1, 55))
        self.line_4.setMaximumSize(QSize(1, 16777215))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.VLine)

        self.horizontalLayout_7.addWidget(self.line_4)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 3, -1, -1)
        self.SolidPoly_toolButton = QToolButton(self.Templatetab)
        self.SolidPoly_toolButton.setObjectName(u"SolidPoly_toolButton")
        self.SolidPoly_toolButton.setMinimumSize(QSize(40, 40))
        self.SolidPoly_toolButton.setFont(font1)

        self.horizontalLayout_13.addWidget(self.SolidPoly_toolButton)

        self.SolidTri_toolButton = QToolButton(self.Templatetab)
        self.SolidTri_toolButton.setObjectName(u"SolidTri_toolButton")
        self.SolidTri_toolButton.setMinimumSize(QSize(40, 40))
        self.SolidTri_toolButton.setFont(font1)

        self.horizontalLayout_13.addWidget(self.SolidTri_toolButton)

        self.SolidTrap_toolButton = QToolButton(self.Templatetab)
        self.SolidTrap_toolButton.setObjectName(u"SolidTrap_toolButton")
        self.SolidTrap_toolButton.setMinimumSize(QSize(40, 40))
        self.SolidTrap_toolButton.setFont(font1)

        self.horizontalLayout_13.addWidget(self.SolidTrap_toolButton)

        self.SolidRec_toolButton = QToolButton(self.Templatetab)
        self.SolidRec_toolButton.setObjectName(u"SolidRec_toolButton")
        self.SolidRec_toolButton.setMinimumSize(QSize(40, 40))
        self.SolidRec_toolButton.setFont(font1)

        self.horizontalLayout_13.addWidget(self.SolidRec_toolButton)

        self.SolidCircle_toolButton = QToolButton(self.Templatetab)
        self.SolidCircle_toolButton.setObjectName(u"SolidCircle_toolButton")
        self.SolidCircle_toolButton.setMinimumSize(QSize(40, 40))
        self.SolidCircle_toolButton.setFont(font1)

        self.horizontalLayout_13.addWidget(self.SolidCircle_toolButton)

        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.label_5 = QLabel(self.Templatetab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 16))
        self.label_5.setMaximumSize(QSize(16777215, 16))
        self.label_5.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_5)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.line_5 = QFrame(self.Templatetab)
        self.line_5.setObjectName(u"line_5")
        sizePolicy3.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy3)
        self.line_5.setMinimumSize(QSize(1, 55))
        self.line_5.setMaximumSize(QSize(1, 16777215))
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QFrame.VLine)

        self.horizontalLayout_7.addWidget(self.line_5)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 3, -1, -1)
        self.BuldTee_toolButton = QToolButton(self.Templatetab)
        self.BuldTee_toolButton.setObjectName(u"BuldTee_toolButton")
        self.BuldTee_toolButton.setMinimumSize(QSize(40, 40))
        self.BuldTee_toolButton.setFont(font1)

        self.horizontalLayout_14.addWidget(self.BuldTee_toolButton)

        self.BoxGirder_toolButton = QToolButton(self.Templatetab)
        self.BoxGirder_toolButton.setObjectName(u"BoxGirder_toolButton")
        self.BoxGirder_toolButton.setMinimumSize(QSize(40, 40))
        self.BoxGirder_toolButton.setFont(font1)

        self.horizontalLayout_14.addWidget(self.BoxGirder_toolButton)

        self.TaperedI_toolButton = QToolButton(self.Templatetab)
        self.TaperedI_toolButton.setObjectName(u"TaperedI_toolButton")
        self.TaperedI_toolButton.setMinimumSize(QSize(40, 40))
        self.TaperedI_toolButton.setFont(font1)

        self.horizontalLayout_14.addWidget(self.TaperedI_toolButton)

        self.TaperedTee_toolButton = QToolButton(self.Templatetab)
        self.TaperedTee_toolButton.setObjectName(u"TaperedTee_toolButton")
        self.TaperedTee_toolButton.setMinimumSize(QSize(40, 40))
        self.TaperedTee_toolButton.setFont(font1)

        self.horizontalLayout_14.addWidget(self.TaperedTee_toolButton)

        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.Templatetab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 16))
        self.label_6.setMaximumSize(QSize(16777215, 16))
        self.label_6.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_6)

        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.line_6 = QFrame(self.Templatetab)
        self.line_6.setObjectName(u"line_6")
        sizePolicy3.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy3)
        self.line_6.setMinimumSize(QSize(1, 55))
        self.line_6.setMaximumSize(QSize(1, 16777215))
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QFrame.VLine)

        self.horizontalLayout_7.addWidget(self.line_6)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 3, -1, -1)
        self.FGCircle_toolButton = QToolButton(self.Templatetab)
        self.FGCircle_toolButton.setObjectName(u"FGCircle_toolButton")
        self.FGCircle_toolButton.setMinimumSize(QSize(40, 40))
        self.FGCircle_toolButton.setFont(font1)

        self.horizontalLayout_15.addWidget(self.FGCircle_toolButton)

        self.FGRec_toolButton = QToolButton(self.Templatetab)
        self.FGRec_toolButton.setObjectName(u"FGRec_toolButton")
        self.FGRec_toolButton.setMinimumSize(QSize(40, 40))
        self.FGRec_toolButton.setFont(font1)

        self.horizontalLayout_15.addWidget(self.FGRec_toolButton)

        self.FGI_toolButton = QToolButton(self.Templatetab)
        self.FGI_toolButton.setObjectName(u"FGI_toolButton")
        self.FGI_toolButton.setMinimumSize(QSize(40, 40))
        self.FGI_toolButton.setFont(font1)

        self.horizontalLayout_15.addWidget(self.FGI_toolButton)

        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.label_7 = QLabel(self.Templatetab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 16))
        self.label_7.setMaximumSize(QSize(16777215, 16))
        self.label_7.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_7)

        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.tabWidget.addTab(self.Templatetab, "")
        self.Toolstab = QWidget()
        self.Toolstab.setObjectName(u"Toolstab")
        self.horizontalLayout_10 = QHBoxLayout(self.Toolstab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(3, 1, -1, 1)
        self.UserManual_toolButton = QToolButton(self.Toolstab)
        self.UserManual_toolButton.setObjectName(u"UserManual_toolButton")
        sizePolicy1.setHeightForWidth(self.UserManual_toolButton.sizePolicy().hasHeightForWidth())
        self.UserManual_toolButton.setSizePolicy(sizePolicy1)
        self.UserManual_toolButton.setMinimumSize(QSize(40, 40))
        self.UserManual_toolButton.setFont(font1)
        self.UserManual_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_10.addWidget(self.UserManual_toolButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.tabWidget.addTab(self.Toolstab, "")

        self.VerticalLayout.addWidget(self.tabWidget)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy4)
        self.splitter.setOrientation(Qt.Vertical)
        self.DesignInfogroupBox = QGroupBox(self.splitter)
        self.DesignInfogroupBox.setObjectName(u"DesignInfogroupBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.DesignInfogroupBox.sizePolicy().hasHeightForWidth())
        self.DesignInfogroupBox.setSizePolicy(sizePolicy5)
        self.DesignInfogroupBox.setMinimumSize(QSize(0, 0))
        self.DesignInfogroupBox.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.DesignInfogroupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(12)
        self.SectNamelabel = QLabel(self.DesignInfogroupBox)
        self.SectNamelabel.setObjectName(u"SectNamelabel")
        self.SectNamelabel.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.SectNamelabel.setFont(font4)

        self.gridLayout_2.addWidget(self.SectNamelabel, 0, 0, 1, 1)

        self.SectIDInput_lineEdit = QLineEdit(self.DesignInfogroupBox)
        self.SectIDInput_lineEdit.setObjectName(u"SectIDInput_lineEdit")
        self.SectIDInput_lineEdit.setMinimumSize(QSize(100, 20))
        self.SectIDInput_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.SectIDInput_lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.SectIDInput_lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.DesignInfogroupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setFont(font4)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.SectNameInput_lineEdit = QLineEdit(self.DesignInfogroupBox)
        self.SectNameInput_lineEdit.setObjectName(u"SectNameInput_lineEdit")
        self.SectNameInput_lineEdit.setMinimumSize(QSize(100, 20))
        self.SectNameInput_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.SectNameInput_lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.SectNameInput_lineEdit, 1, 1, 1, 1)

        self.Datelabel = QLabel(self.DesignInfogroupBox)
        self.Datelabel.setObjectName(u"Datelabel")
        self.Datelabel.setMinimumSize(QSize(0, 20))
        self.Datelabel.setFont(font1)

        self.gridLayout_2.addWidget(self.Datelabel, 2, 0, 1, 1)

        self.DateInput_lineEdit = QLineEdit(self.DesignInfogroupBox)
        self.DateInput_lineEdit.setObjectName(u"DateInput_lineEdit")
        self.DateInput_lineEdit.setMinimumSize(QSize(100, 20))
        self.DateInput_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.DateInput_lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.DateInput_lineEdit, 2, 1, 1, 1)

        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.DesignInfogroupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(80, 20))
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.label_2.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.Centerline_radioButton = QRadioButton(self.DesignInfogroupBox)
        self.Centerline_radioButton.setObjectName(u"Centerline_radioButton")
        sizePolicy3.setHeightForWidth(self.Centerline_radioButton.sizePolicy().hasHeightForWidth())
        self.Centerline_radioButton.setSizePolicy(sizePolicy3)
        self.Centerline_radioButton.setMinimumSize(QSize(25, 20))
        self.Centerline_radioButton.setFont(font1)
        self.Centerline_radioButton.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_9.addWidget(self.Centerline_radioButton)

        self.Centerline_label = QLabel(self.DesignInfogroupBox)
        self.Centerline_label.setObjectName(u"Centerline_label")
        sizePolicy3.setHeightForWidth(self.Centerline_label.sizePolicy().hasHeightForWidth())
        self.Centerline_label.setSizePolicy(sizePolicy3)
        self.Centerline_label.setMinimumSize(QSize(32, 20))
        self.Centerline_label.setMaximumSize(QSize(32, 20))

        self.horizontalLayout_9.addWidget(self.Centerline_label)

        self.Centerline_label_2 = QLabel(self.DesignInfogroupBox)
        self.Centerline_label_2.setObjectName(u"Centerline_label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Centerline_label_2.sizePolicy().hasHeightForWidth())
        self.Centerline_label_2.setSizePolicy(sizePolicy6)
        self.Centerline_label_2.setMinimumSize(QSize(60, 0))
        self.Centerline_label_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_9.addWidget(self.Centerline_label_2)

        self.Outline_radioButton = QRadioButton(self.DesignInfogroupBox)
        self.Outline_radioButton.setObjectName(u"Outline_radioButton")
        sizePolicy3.setHeightForWidth(self.Outline_radioButton.sizePolicy().hasHeightForWidth())
        self.Outline_radioButton.setSizePolicy(sizePolicy3)
        self.Outline_radioButton.setMinimumSize(QSize(25, 20))
        self.Outline_radioButton.setFont(font1)
        self.Outline_radioButton.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_9.addWidget(self.Outline_radioButton)

        self.Outline_label = QLabel(self.DesignInfogroupBox)
        self.Outline_label.setObjectName(u"Outline_label")
        sizePolicy3.setHeightForWidth(self.Outline_label.sizePolicy().hasHeightForWidth())
        self.Outline_label.setSizePolicy(sizePolicy3)
        self.Outline_label.setMinimumSize(QSize(32, 22))
        self.Outline_label.setMaximumSize(QSize(32, 22))

        self.horizontalLayout_9.addWidget(self.Outline_label)

        self.Outline_label_2 = QLabel(self.DesignInfogroupBox)
        self.Outline_label_2.setObjectName(u"Outline_label_2")
        sizePolicy6.setHeightForWidth(self.Outline_label_2.sizePolicy().hasHeightForWidth())
        self.Outline_label_2.setSizePolicy(sizePolicy6)
        self.Outline_label_2.setMinimumSize(QSize(45, 0))
        self.Outline_label_2.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_9.addWidget(self.Outline_label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.splitter.addWidget(self.DesignInfogroupBox)
        self.MatgroupBox = QGroupBox(self.splitter)
        self.MatgroupBox.setObjectName(u"MatgroupBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.MatgroupBox.sizePolicy().hasHeightForWidth())
        self.MatgroupBox.setSizePolicy(sizePolicy7)
        self.MatgroupBox.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.MatgroupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.MattableWidget = QTableWidget(self.MatgroupBox)
        if (self.MattableWidget.columnCount() < 6):
            self.MattableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.MattableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.MattableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.MattableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.MattableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.MattableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.MattableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.MattableWidget.setObjectName(u"MattableWidget")
        font5 = QFont()
        font5.setPointSize(10)
        self.MattableWidget.setFont(font5)
        self.MattableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.MattableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.MattableWidget.horizontalHeader().setDefaultSectionSize(65)
        self.MattableWidget.horizontalHeader().setStretchLastSection(True)
        self.MattableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.MattableWidget.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout_6.addWidget(self.MattableWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.MatAddpushButton = QPushButton(self.MatgroupBox)
        self.MatAddpushButton.setObjectName(u"MatAddpushButton")
        sizePolicy1.setHeightForWidth(self.MatAddpushButton.sizePolicy().hasHeightForWidth())
        self.MatAddpushButton.setSizePolicy(sizePolicy1)
        self.MatAddpushButton.setMinimumSize(QSize(0, 20))
        self.MatAddpushButton.setMaximumSize(QSize(16777215, 20))
        self.MatAddpushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.MatAddpushButton)

        self.MatDeletepushButton = QPushButton(self.MatgroupBox)
        self.MatDeletepushButton.setObjectName(u"MatDeletepushButton")
        sizePolicy1.setHeightForWidth(self.MatDeletepushButton.sizePolicy().hasHeightForWidth())
        self.MatDeletepushButton.setSizePolicy(sizePolicy1)
        self.MatDeletepushButton.setMinimumSize(QSize(0, 20))
        self.MatDeletepushButton.setMaximumSize(QSize(16777215, 20))
        self.MatDeletepushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.MatDeletepushButton)

        self.MatModifypushButton = QPushButton(self.MatgroupBox)
        self.MatModifypushButton.setObjectName(u"MatModifypushButton")
        sizePolicy1.setHeightForWidth(self.MatModifypushButton.sizePolicy().hasHeightForWidth())
        self.MatModifypushButton.setSizePolicy(sizePolicy1)
        self.MatModifypushButton.setMinimumSize(QSize(0, 20))
        self.MatModifypushButton.setMaximumSize(QSize(16777215, 20))
        self.MatModifypushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.MatModifypushButton)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.MatgroupBox)
        self.PointgroupBox = QGroupBox(self.splitter)
        self.PointgroupBox.setObjectName(u"PointgroupBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(2)
        sizePolicy8.setHeightForWidth(self.PointgroupBox.sizePolicy().hasHeightForWidth())
        self.PointgroupBox.setSizePolicy(sizePolicy8)
        self.PointgroupBox.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.PointgroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.PointtableWidget = QTableWidget(self.PointgroupBox)
        if (self.PointtableWidget.columnCount() < 4):
            self.PointtableWidget.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.PointtableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.PointtableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font6);
        self.PointtableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.PointtableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.PointtableWidget.setObjectName(u"PointtableWidget")
        self.PointtableWidget.setFont(font2)
        self.PointtableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.PointtableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.PointtableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.PointtableWidget.horizontalHeader().setStretchLastSection(True)
        self.PointtableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.PointtableWidget.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout_5.addWidget(self.PointtableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.PointAddpushButton = QPushButton(self.PointgroupBox)
        self.PointAddpushButton.setObjectName(u"PointAddpushButton")
        sizePolicy1.setHeightForWidth(self.PointAddpushButton.sizePolicy().hasHeightForWidth())
        self.PointAddpushButton.setSizePolicy(sizePolicy1)
        self.PointAddpushButton.setMinimumSize(QSize(0, 20))
        self.PointAddpushButton.setMaximumSize(QSize(16777215, 20))
        self.PointAddpushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.PointAddpushButton)

        self.PointDeletepushButton = QPushButton(self.PointgroupBox)
        self.PointDeletepushButton.setObjectName(u"PointDeletepushButton")
        sizePolicy1.setHeightForWidth(self.PointDeletepushButton.sizePolicy().hasHeightForWidth())
        self.PointDeletepushButton.setSizePolicy(sizePolicy1)
        self.PointDeletepushButton.setMinimumSize(QSize(0, 20))
        self.PointDeletepushButton.setMaximumSize(QSize(16777215, 20))
        self.PointDeletepushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.PointDeletepushButton)

        self.PointModifypushButton = QPushButton(self.PointgroupBox)
        self.PointModifypushButton.setObjectName(u"PointModifypushButton")
        sizePolicy1.setHeightForWidth(self.PointModifypushButton.sizePolicy().hasHeightForWidth())
        self.PointModifypushButton.setSizePolicy(sizePolicy1)
        self.PointModifypushButton.setMinimumSize(QSize(0, 20))
        self.PointModifypushButton.setMaximumSize(QSize(16777215, 20))
        self.PointModifypushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.PointModifypushButton)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.PointgroupBox)
        self.SegmentgroupBox = QGroupBox(self.splitter)
        self.SegmentgroupBox.setObjectName(u"SegmentgroupBox")
        sizePolicy7.setHeightForWidth(self.SegmentgroupBox.sizePolicy().hasHeightForWidth())
        self.SegmentgroupBox.setSizePolicy(sizePolicy7)
        self.SegmentgroupBox.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.SegmentgroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.SegmenttableWidget = QTableWidget(self.SegmentgroupBox)
        if (self.SegmenttableWidget.columnCount() < 5):
            self.SegmenttableWidget.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.SegmenttableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.SegmenttableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.SegmenttableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.SegmenttableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.SegmenttableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.SegmenttableWidget.setObjectName(u"SegmenttableWidget")
        self.SegmenttableWidget.setFont(font1)
        self.SegmenttableWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.SegmenttableWidget.setFrameShadow(QFrame.Plain)
        self.SegmenttableWidget.setAutoScroll(False)
        self.SegmenttableWidget.setAutoScrollMargin(22)
        self.SegmenttableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.SegmenttableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.SegmenttableWidget.horizontalHeader().setDefaultSectionSize(56)
        self.SegmenttableWidget.horizontalHeader().setStretchLastSection(True)
        self.SegmenttableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.SegmenttableWidget.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout_4.addWidget(self.SegmenttableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.SegAddpushButton = QPushButton(self.SegmentgroupBox)
        self.SegAddpushButton.setObjectName(u"SegAddpushButton")
        sizePolicy1.setHeightForWidth(self.SegAddpushButton.sizePolicy().hasHeightForWidth())
        self.SegAddpushButton.setSizePolicy(sizePolicy1)
        self.SegAddpushButton.setMinimumSize(QSize(0, 20))
        self.SegAddpushButton.setMaximumSize(QSize(16777215, 20))
        self.SegAddpushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.SegAddpushButton)

        self.SegDeletepushButton = QPushButton(self.SegmentgroupBox)
        self.SegDeletepushButton.setObjectName(u"SegDeletepushButton")
        sizePolicy1.setHeightForWidth(self.SegDeletepushButton.sizePolicy().hasHeightForWidth())
        self.SegDeletepushButton.setSizePolicy(sizePolicy1)
        self.SegDeletepushButton.setMinimumSize(QSize(0, 20))
        self.SegDeletepushButton.setMaximumSize(QSize(16777215, 20))
        self.SegDeletepushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.SegDeletepushButton)

        self.SegModifypushButton = QPushButton(self.SegmentgroupBox)
        self.SegModifypushButton.setObjectName(u"SegModifypushButton")
        sizePolicy1.setHeightForWidth(self.SegModifypushButton.sizePolicy().hasHeightForWidth())
        self.SegModifypushButton.setSizePolicy(sizePolicy1)
        self.SegModifypushButton.setMinimumSize(QSize(0, 20))
        self.SegModifypushButton.setMaximumSize(QSize(16777215, 20))
        self.SegModifypushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.SegModifypushButton)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.SegmentgroupBox)
        self.splitter_3.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(5)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy9)
        self.splitter_2.setOrientation(Qt.Vertical)
        self.graphicsView = GraphicsLayoutWidget(self.splitter_2)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(15)
        sizePolicy10.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy10)
        self.graphicsView.setFrameShadow(QFrame.Plain)
        self.splitter_2.addWidget(self.graphicsView)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(1)
        sizePolicy11.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy11)
        self.groupBox.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.StatusOutput = CustomTextBrowser(self.groupBox)
        self.StatusOutput.setObjectName(u"StatusOutput")
        self.StatusOutput.setFrameShape(QFrame.NoFrame)
        self.StatusOutput.setFrameShadow(QFrame.Plain)
        self.StatusOutput.setLineWidth(0)
        self.StatusOutput.setMidLineWidth(0)
        self.StatusOutput.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.StatusOutput.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_10.addWidget(self.StatusOutput)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.FontSize_label = QLabel(self.groupBox)
        self.FontSize_label.setObjectName(u"FontSize_label")
        sizePolicy1.setHeightForWidth(self.FontSize_label.sizePolicy().hasHeightForWidth())
        self.FontSize_label.setSizePolicy(sizePolicy1)
        self.FontSize_label.setMinimumSize(QSize(0, 20))
        self.FontSize_label.setMaximumSize(QSize(16777215, 20))
        self.FontSize_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.FontSize_label)

        self.FontSize_lineEdit = QLineEdit(self.groupBox)
        self.FontSize_lineEdit.setObjectName(u"FontSize_lineEdit")
        sizePolicy1.setHeightForWidth(self.FontSize_lineEdit.sizePolicy().hasHeightForWidth())
        self.FontSize_lineEdit.setSizePolicy(sizePolicy1)
        self.FontSize_lineEdit.setMinimumSize(QSize(24, 20))
        self.FontSize_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.FontSize_lineEdit.setFont(font1)

        self.horizontalLayout_6.addWidget(self.FontSize_lineEdit)

        self.SmallFontSize_pushButton = QPushButton(self.groupBox)
        self.SmallFontSize_pushButton.setObjectName(u"SmallFontSize_pushButton")
        sizePolicy1.setHeightForWidth(self.SmallFontSize_pushButton.sizePolicy().hasHeightForWidth())
        self.SmallFontSize_pushButton.setSizePolicy(sizePolicy1)
        self.SmallFontSize_pushButton.setMinimumSize(QSize(50, 20))
        self.SmallFontSize_pushButton.setMaximumSize(QSize(16777215, 20))
        self.SmallFontSize_pushButton.setFont(font1)

        self.horizontalLayout_6.addWidget(self.SmallFontSize_pushButton)

        self.NormalFontSize_pushButton = QPushButton(self.groupBox)
        self.NormalFontSize_pushButton.setObjectName(u"NormalFontSize_pushButton")
        sizePolicy1.setHeightForWidth(self.NormalFontSize_pushButton.sizePolicy().hasHeightForWidth())
        self.NormalFontSize_pushButton.setSizePolicy(sizePolicy1)
        self.NormalFontSize_pushButton.setMinimumSize(QSize(50, 20))
        self.NormalFontSize_pushButton.setMaximumSize(QSize(16777215, 20))
        self.NormalFontSize_pushButton.setFont(font1)

        self.horizontalLayout_6.addWidget(self.NormalFontSize_pushButton)

        self.LargeFontSize_pushButton = QPushButton(self.groupBox)
        self.LargeFontSize_pushButton.setObjectName(u"LargeFontSize_pushButton")
        sizePolicy1.setHeightForWidth(self.LargeFontSize_pushButton.sizePolicy().hasHeightForWidth())
        self.LargeFontSize_pushButton.setSizePolicy(sizePolicy1)
        self.LargeFontSize_pushButton.setMinimumSize(QSize(50, 20))
        self.LargeFontSize_pushButton.setMaximumSize(QSize(16777215, 20))
        self.LargeFontSize_pushButton.setFont(font1)

        self.horizontalLayout_6.addWidget(self.LargeFontSize_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.Savetext_pushButton = QPushButton(self.groupBox)
        self.Savetext_pushButton.setObjectName(u"Savetext_pushButton")
        sizePolicy1.setHeightForWidth(self.Savetext_pushButton.sizePolicy().hasHeightForWidth())
        self.Savetext_pushButton.setSizePolicy(sizePolicy1)
        self.Savetext_pushButton.setMinimumSize(QSize(60, 20))
        self.Savetext_pushButton.setMaximumSize(QSize(16777215, 20))
        self.Savetext_pushButton.setFont(font1)

        self.horizontalLayout_6.addWidget(self.Savetext_pushButton)

        self.Cleartext_pushButton = QPushButton(self.groupBox)
        self.Cleartext_pushButton.setObjectName(u"Cleartext_pushButton")
        sizePolicy1.setHeightForWidth(self.Cleartext_pushButton.sizePolicy().hasHeightForWidth())
        self.Cleartext_pushButton.setSizePolicy(sizePolicy1)
        self.Cleartext_pushButton.setMinimumSize(QSize(60, 20))
        self.Cleartext_pushButton.setMaximumSize(QSize(16777215, 20))
        self.Cleartext_pushButton.setFont(font1)

        self.horizontalLayout_6.addWidget(self.Cleartext_pushButton)

        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 2)
        self.horizontalLayout_6.setStretch(4, 2)
        self.horizontalLayout_6.setStretch(5, 18)
        self.horizontalLayout_6.setStretch(6, 2)
        self.horizontalLayout_6.setStretch(7, 2)

        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.splitter_2.addWidget(self.groupBox)
        self.splitter_3.addWidget(self.splitter_2)
        self.SPgroupBox = QGroupBox(self.splitter_3)
        self.SPgroupBox.setObjectName(u"SPgroupBox")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(4)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.SPgroupBox.sizePolicy().hasHeightForWidth())
        self.SPgroupBox.setSizePolicy(sizePolicy12)
        self.SPgroupBox.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.SPgroupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.SPtableWidget = QTableWidget(self.SPgroupBox)
        if (self.SPtableWidget.columnCount() < 3):
            self.SPtableWidget.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.SPtableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.SPtableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.SPtableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        self.SPtableWidget.setObjectName(u"SPtableWidget")
        self.SPtableWidget.setFont(font5)

        self.verticalLayout_8.addWidget(self.SPtableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Export_pushButton = QPushButton(self.SPgroupBox)
        self.Export_pushButton.setObjectName(u"Export_pushButton")
        self.Export_pushButton.setMinimumSize(QSize(0, 20))
        self.Export_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.Export_pushButton)

        self.Clear_pushButton = QPushButton(self.SPgroupBox)
        self.Clear_pushButton.setObjectName(u"Clear_pushButton")
        self.Clear_pushButton.setMinimumSize(QSize(0, 20))
        self.Clear_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.Clear_pushButton)

        self.Setting_pushButton = QPushButton(self.SPgroupBox)
        self.Setting_pushButton.setObjectName(u"Setting_pushButton")
        self.Setting_pushButton.setMinimumSize(QSize(0, 20))
        self.Setting_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.Setting_pushButton)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.splitter_3.addWidget(self.SPgroupBox)

        self.VerticalLayout.addWidget(self.splitter_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.tabWidget, self.New_toolButton)
        QWidget.setTabOrder(self.New_toolButton, self.Open_toolButton)
        QWidget.setTabOrder(self.Open_toolButton, self.Save_toolButton)
        QWidget.setTabOrder(self.Save_toolButton, self.SaveAs_toolButton)
        QWidget.setTabOrder(self.SaveAs_toolButton, self.ShowPointID_checkBox)
        QWidget.setTabOrder(self.ShowPointID_checkBox, self.ShowLineID_checkBox)
        QWidget.setTabOrder(self.ShowLineID_checkBox, self.ShowMatID_checkBox)
        QWidget.setTabOrder(self.ShowMatID_checkBox, self.ShowCoord_checkBox)
        QWidget.setTabOrder(self.ShowCoord_checkBox, self.ShowPrincipleAxis_checkBox)
        QWidget.setTabOrder(self.ShowPrincipleAxis_checkBox, self.ShowGrid_checkBox)
        QWidget.setTabOrder(self.ShowGrid_checkBox, self.ShowOrigin_checkBox)
        QWidget.setTabOrder(self.ShowOrigin_checkBox, self.ShowGC_checkBox)
        QWidget.setTabOrder(self.ShowGC_checkBox, self.ShowSC_checkBox)
        QWidget.setTabOrder(self.ShowSC_checkBox, self.ShowFiber_checkBox)
        QWidget.setTabOrder(self.ShowFiber_checkBox, self.Mesh_toolButton)
        QWidget.setTabOrder(self.Mesh_toolButton, self.Model3DView_toolButton)
        QWidget.setTabOrder(self.Model3DView_toolButton, self.Fit2Screen_toolButton)
        QWidget.setTabOrder(self.Fit2Screen_toolButton, self.SPAnal_toolButton)
        QWidget.setTabOrder(self.SPAnal_toolButton, self.YSAnal_toolButton)
        QWidget.setTabOrder(self.YSAnal_toolButton, self.MomentCurvature_toolButton)
        QWidget.setTabOrder(self.MomentCurvature_toolButton, self.GlobalBuckling_toolButton)
        QWidget.setTabOrder(self.GlobalBuckling_toolButton, self.LocalBuckling_toolButton)
        QWidget.setTabOrder(self.LocalBuckling_toolButton, self.SectIDInput_lineEdit)
        QWidget.setTabOrder(self.SectIDInput_lineEdit, self.SectNameInput_lineEdit)
        QWidget.setTabOrder(self.SectNameInput_lineEdit, self.DateInput_lineEdit)
        QWidget.setTabOrder(self.DateInput_lineEdit, self.Centerline_radioButton)
        QWidget.setTabOrder(self.Centerline_radioButton, self.Outline_radioButton)
        QWidget.setTabOrder(self.Outline_radioButton, self.MattableWidget)
        QWidget.setTabOrder(self.MattableWidget, self.MatAddpushButton)
        QWidget.setTabOrder(self.MatAddpushButton, self.MatDeletepushButton)
        QWidget.setTabOrder(self.MatDeletepushButton, self.MatModifypushButton)
        QWidget.setTabOrder(self.MatModifypushButton, self.PointtableWidget)
        QWidget.setTabOrder(self.PointtableWidget, self.PointAddpushButton)
        QWidget.setTabOrder(self.PointAddpushButton, self.PointDeletepushButton)
        QWidget.setTabOrder(self.PointDeletepushButton, self.PointModifypushButton)
        QWidget.setTabOrder(self.PointModifypushButton, self.SegmenttableWidget)
        QWidget.setTabOrder(self.SegmenttableWidget, self.SegAddpushButton)
        QWidget.setTabOrder(self.SegAddpushButton, self.SegDeletepushButton)
        QWidget.setTabOrder(self.SegDeletepushButton, self.SegModifypushButton)
        QWidget.setTabOrder(self.SegModifypushButton, self.StatusOutput)
        QWidget.setTabOrder(self.StatusOutput, self.FontSize_lineEdit)
        QWidget.setTabOrder(self.FontSize_lineEdit, self.SmallFontSize_pushButton)
        QWidget.setTabOrder(self.SmallFontSize_pushButton, self.NormalFontSize_pushButton)
        QWidget.setTabOrder(self.NormalFontSize_pushButton, self.LargeFontSize_pushButton)
        QWidget.setTabOrder(self.LargeFontSize_pushButton, self.Savetext_pushButton)
        QWidget.setTabOrder(self.Savetext_pushButton, self.Cleartext_pushButton)
        QWidget.setTabOrder(self.Cleartext_pushButton, self.SPtableWidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionNew_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionLine_ID.setText(QCoreApplication.translate("MainWindow", u"Line ID", None))
        self.actionMaterial_ID.setText(QCoreApplication.translate("MainWindow", u"Material ID", None))
        self.actionCoordinates.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.actionPrinciple_Axis.setText(QCoreApplication.translate("MainWindow", u"Principle Axis", None))
        self.actionResidual_Stress.setText(QCoreApplication.translate("MainWindow", u"Residual Stress", None))
        self.actionOrigin.setText(QCoreApplication.translate("MainWindow", u"Origin", None))
        self.actionShear_Center.setText(QCoreApplication.translate("MainWindow", u"Shear Center", None))
        self.actionYield_Surface.setText(QCoreApplication.translate("MainWindow", u"Yield Surface", None))
        self.actionLocal_Bucklling.setText(QCoreApplication.translate("MainWindow", u"Local Bucklling", None))
        self.actionMoment_Curvature.setText(QCoreApplication.translate("MainWindow", u"Moment - Curvature", None))
        self.actionExport_to_Mastan2.setText(QCoreApplication.translate("MainWindow", u"Export to Mastan2", None))
        self.actionExport_to_Mastan3.setText(QCoreApplication.translate("MainWindow", u"Export to Mastan3", None))
        self.actionSection_Properties_2.setText(QCoreApplication.translate("MainWindow", u"Section Properties", None))
        self.actionYield_Surface_2.setText(QCoreApplication.translate("MainWindow", u"Yield Surface", None))
        self.actionMoment_Curvature_2.setText(QCoreApplication.translate("MainWindow", u"Moment - Curvature", None))
        self.actionGlobal_Buckling_2.setText(QCoreApplication.translate("MainWindow", u"Global Buckling ", None))
        self.actionLocal_Bucklling_2.setText(QCoreApplication.translate("MainWindow", u"Local Bucklling", None))
        self.actionLine_ID_2.setText(QCoreApplication.translate("MainWindow", u"Point ID", None))
        self.actionLine_ID_3.setText(QCoreApplication.translate("MainWindow", u"Line ID", None))
        self.actionMaterial_ID_2.setText(QCoreApplication.translate("MainWindow", u"Material ID", None))
        self.actionShow_Fiber.setText(QCoreApplication.translate("MainWindow", u"Show Fiber", None))
        self.actionGeometric_Center.setText(QCoreApplication.translate("MainWindow", u"Geometric Center", None))
        self.actionShear_Center_2.setText(QCoreApplication.translate("MainWindow", u"Shear Center", None))
        self.New_toolButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.Open_toolButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.Save_toolButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.SaveAs_toolButton.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.ShowMatID_checkBox.setText(QCoreApplication.translate("MainWindow", u"Material ID", None))
        self.ShowPointID_checkBox.setText(QCoreApplication.translate("MainWindow", u"Point ID", None))
        self.ShowCoord_checkBox.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.ShowLineID_checkBox.setText(QCoreApplication.translate("MainWindow", u"Line ID", None))
        self.ShowPrincipleAxis_checkBox.setText(QCoreApplication.translate("MainWindow", u"Principle Axis", None))
        self.ShowGrid_checkBox.setText(QCoreApplication.translate("MainWindow", u"Show Grid", None))
        self.ShowOrigin_checkBox.setText(QCoreApplication.translate("MainWindow", u"Origin", None))
        self.ShowGC_checkBox.setText(QCoreApplication.translate("MainWindow", u"Geometric Center", None))
        self.ShowSC_checkBox.setText(QCoreApplication.translate("MainWindow", u"Shear Center", None))
        self.ShowFiber_checkBox.setText(QCoreApplication.translate("MainWindow", u"Show Fiber", None))
        self.Mesh_toolButton.setText(QCoreApplication.translate("MainWindow", u"Mesh", None))
        self.Model3DView_toolButton.setText(QCoreApplication.translate("MainWindow", u"3D View", None))
        self.Fit2Screen_toolButton.setText(QCoreApplication.translate("MainWindow", u"Fit to Screen", None))
        self.SPAnal_toolButton.setText(QCoreApplication.translate("MainWindow", u"Section Properties", None))
        self.YSAnal_toolButton.setText(QCoreApplication.translate("MainWindow", u"Yield Surfaces", None))
        self.MomentCurvature_toolButton.setText(QCoreApplication.translate("MainWindow", u"Moment Curvature", None))
        self.GlobalBuckling_toolButton.setText(QCoreApplication.translate("MainWindow", u"Global Buckling", None))
        self.LocalBuckling_toolButton.setText(QCoreApplication.translate("MainWindow", u"Local Buckling", None))
        self.StressAnalysis_toolButton.setText(QCoreApplication.translate("MainWindow", u"Stress Analysis", None))
        self.About_toolButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hometab),
                                  QCoreApplication.translate("MainWindow", u"Home", None))
        self.ISection_toolButton.setText(QCoreApplication.translate("MainWindow", u"I-Section", None))
        self.ZSection_toolButton.setText(QCoreApplication.translate("MainWindow", u"Z-Section", None))
        self.TSection_toolButton.setText(QCoreApplication.translate("MainWindow", u"T-Section", None))
        self.CSection_toolButton.setText(QCoreApplication.translate("MainWindow", u"C-Section", None))
        self.LSection_toolButton.setText(QCoreApplication.translate("MainWindow", u"L-Section", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">Open Section</p></body></html>",
                                                        None))
        self.HollowCircle_toolButton.setText(QCoreApplication.translate("MainWindow", u"Hollow Circle", None))
        self.HollowRec_toolButton.setText(QCoreApplication.translate("MainWindow", u"Hollow Rec", None))
        self.HollowTrap_toolButton.setText(QCoreApplication.translate("MainWindow", u"Hollow Trap", None))
        self.HollowTri_toolButton.setText(QCoreApplication.translate("MainWindow", u"Hollow Tri", None))
        self.HollowPoly_toolButton.setText(QCoreApplication.translate("MainWindow", u"Hollow Poly", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">Closed Section</p></body></html>",
                                                        None))
        self.SolidPoly_toolButton.setText(QCoreApplication.translate("MainWindow", u"Solid Poly", None))
        self.SolidTri_toolButton.setText(QCoreApplication.translate("MainWindow", u"Solid Tri", None))
        self.SolidTrap_toolButton.setText(QCoreApplication.translate("MainWindow", u"Solid Trap", None))
        self.SolidRec_toolButton.setText(QCoreApplication.translate("MainWindow", u"Solid Rec", None))
        self.SolidCircle_toolButton.setText(QCoreApplication.translate("MainWindow", u"Solid Circle", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">Solid Section</p></body></html>",
                                                        None))
        self.BuldTee_toolButton.setText(QCoreApplication.translate("MainWindow", u"Buld Tee", None))
        self.BoxGirder_toolButton.setText(QCoreApplication.translate("MainWindow", u"Box Girder", None))
        self.TaperedI_toolButton.setText(QCoreApplication.translate("MainWindow", u"Tapered I", None))
        self.TaperedTee_toolButton.setText(QCoreApplication.translate("MainWindow", u"Tapered Tee", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">Girder Section</p></body></html>",
                                                        None))
        self.FGCircle_toolButton.setText(QCoreApplication.translate("MainWindow", u"FG-Circle", None))
        self.FGRec_toolButton.setText(QCoreApplication.translate("MainWindow", u"FG-Rec", None))
        self.FGI_toolButton.setText(QCoreApplication.translate("MainWindow", u"FG-I", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">Functionally Graded Section</p></body></html>",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Templatetab),
                                  QCoreApplication.translate("MainWindow", u"Template", None))
        self.UserManual_toolButton.setText(QCoreApplication.translate("MainWindow", u"User Manual", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Toolstab),
                                  QCoreApplication.translate("MainWindow", u"Help", None))
        self.DesignInfogroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Design Information", None))
        self.SectNamelabel.setText(QCoreApplication.translate("MainWindow", u"Section ID:", None))
        self.SectIDInput_lineEdit.setText(QCoreApplication.translate("MainWindow", u"Section01", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Section Name:", None))
        self.SectNameInput_lineEdit.setText(QCoreApplication.translate("MainWindow", u"MsaSect Section", None))
        self.Datelabel.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Modeling by:", None))
        self.Centerline_label_2.setText(QCoreApplication.translate("MainWindow", u"Centerline", None))
        self.Outline_label_2.setText(QCoreApplication.translate("MainWindow", u"Outline", None))
        self.MatgroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Material", None))
        ___qtablewidgetitem = self.MattableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.MattableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Color", None));
        ___qtablewidgetitem2 = self.MattableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"E", None));
        ___qtablewidgetitem3 = self.MattableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u03bc", None));
        ___qtablewidgetitem4 = self.MattableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"fy", None));
        ___qtablewidgetitem5 = self.MattableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"eu", None));
        self.MatAddpushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.MatDeletepushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.MatModifypushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.PointgroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Point", None))
        ___qtablewidgetitem6 = self.PointtableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.PointtableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem8 = self.PointtableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitem9 = self.PointtableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Residual Stress", None));
        self.PointAddpushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.PointDeletepushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.PointModifypushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.SegmentgroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Centerline", None))
        ___qtablewidgetitem10 = self.SegmenttableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.SegmenttableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem12 = self.SegmenttableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"I", None));
        ___qtablewidgetitem13 = self.SegmenttableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"J", None));
        ___qtablewidgetitem14 = self.SegmenttableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Thickness", None));
        self.SegAddpushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.SegDeletepushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.SegModifypushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.FontSize_label.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.SmallFontSize_pushButton.setText(QCoreApplication.translate("MainWindow", u"Smaller", None))
        self.NormalFontSize_pushButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.LargeFontSize_pushButton.setText(QCoreApplication.translate("MainWindow", u"Larger", None))
        self.Savetext_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Text", None))
        self.Cleartext_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Text", None))
        self.SPgroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Section Properties", None))
        ___qtablewidgetitem15 = self.SPtableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem16 = self.SPtableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem17 = self.SPtableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"    Value", None));
        self.Export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.Clear_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Setting_pushButton.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
