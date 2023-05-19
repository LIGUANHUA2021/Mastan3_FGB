# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowResultsMCurv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_ShowResultsMCurv_Dialog(object):
    def setupUi(self, ShowResultsMCurv_Dialog):
        if not ShowResultsMCurv_Dialog.objectName():
            ShowResultsMCurv_Dialog.setObjectName(u"ShowResultsMCurv_Dialog")
        ShowResultsMCurv_Dialog.resize(816, 598)
        ShowResultsMCurv_Dialog.setMinimumSize(QSize(592, 380))
        ShowResultsMCurv_Dialog.setStyleSheet(u"QDialog\n"
"{\n"
"	background-color: rgb(43, 43, 43);\n"
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
"}")
        self.gridLayout_3 = QGridLayout(ShowResultsMCurv_Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setContentsMargins(0, 2, 0, 2)
        self.frame = QFrame(ShowResultsMCurv_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 32))
        self.frame.setMaximumSize(QSize(16777215, 32))
        self.frame.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 3, 4, 4)
        self.ExportMCurv_pushButton = QPushButton(self.frame)
        self.ExportMCurv_pushButton.setObjectName(u"ExportMCurv_pushButton")
        self.ExportMCurv_pushButton.setMinimumSize(QSize(120, 22))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.ExportMCurv_pushButton.setFont(font)
        self.ExportMCurv_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ExportMCurv_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Close_pushButton = QPushButton(self.frame)
        self.Close_pushButton.setObjectName(u"Close_pushButton")
        self.Close_pushButton.setMinimumSize(QSize(70, 22))
        self.Close_pushButton.setFont(font)
        self.Close_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.Close_pushButton)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 12)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 2)

        self.Curves_tabWidget = QTabWidget(ShowResultsMCurv_Dialog)
        self.Curves_tabWidget.setObjectName(u"Curves_tabWidget")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setKerning(True)
        self.Curves_tabWidget.setFont(font1)
        self.Curves_tabWidget.setToolTipDuration(-1)
        self.Curves_tabWidget.setAutoFillBackground(False)
        self.Curves_tabWidget.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.Curves_tabWidget.setTabShape(QTabWidget.Rounded)
        self.MC_tab = QWidget()
        self.MC_tab.setObjectName(u"MC_tab")
        self.verticalLayout = QVBoxLayout(self.MC_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MCurvPlot_verticalLayout = QVBoxLayout()
        self.MCurvPlot_verticalLayout.setSpacing(0)
        self.MCurvPlot_verticalLayout.setObjectName(u"MCurvPlot_verticalLayout")

        self.verticalLayout.addLayout(self.MCurvPlot_verticalLayout)

        self.Curves_tabWidget.addTab(self.MC_tab, "")
        self.MStrn_tab = QWidget()
        self.MStrn_tab.setObjectName(u"MStrn_tab")
        self.verticalLayout_4 = QVBoxLayout(self.MStrn_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.MStrnPlot_verticalLayout = QVBoxLayout()
        self.MStrnPlot_verticalLayout.setObjectName(u"MStrnPlot_verticalLayout")

        self.verticalLayout_4.addLayout(self.MStrnPlot_verticalLayout)

        self.Curves_tabWidget.addTab(self.MStrn_tab, "")
        self.MStrs_tab = QWidget()
        self.MStrs_tab.setObjectName(u"MStrs_tab")
        self.verticalLayout_6 = QVBoxLayout(self.MStrs_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.MStrsPlot_verticalLayout = QVBoxLayout()
        self.MStrsPlot_verticalLayout.setObjectName(u"MStrsPlot_verticalLayout")

        self.verticalLayout_6.addLayout(self.MStrsPlot_verticalLayout)

        self.Curves_tabWidget.addTab(self.MStrs_tab, "")
        self.MTS_tab = QWidget()
        self.MTS_tab.setObjectName(u"MTS_tab")
        self.verticalLayout_8 = QVBoxLayout(self.MTS_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.MTSPlot_verticalLayout = QVBoxLayout()
        self.MTSPlot_verticalLayout.setObjectName(u"MTSPlot_verticalLayout")

        self.verticalLayout_8.addLayout(self.MTSPlot_verticalLayout)

        self.Curves_tabWidget.addTab(self.MTS_tab, "")
        self.MSS_tab = QWidget()
        self.MSS_tab.setObjectName(u"MSS_tab")
        self.verticalLayout_10 = QVBoxLayout(self.MSS_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.MSSPlot_verticalLayout = QVBoxLayout()
        self.MSSPlot_verticalLayout.setObjectName(u"MSSPlot_verticalLayout")

        self.verticalLayout_10.addLayout(self.MSSPlot_verticalLayout)

        self.Curves_tabWidget.addTab(self.MSS_tab, "")

        self.gridLayout_3.addWidget(self.Curves_tabWidget, 0, 0, 1, 2)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setColumnStretch(0, 3)

        self.retranslateUi(ShowResultsMCurv_Dialog)

        self.Curves_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ShowResultsMCurv_Dialog)
    # setupUi

    def retranslateUi(self, ShowResultsMCurv_Dialog):
        ShowResultsMCurv_Dialog.setWindowTitle(QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Moment Curvature Curve", None))
        self.ExportMCurv_pushButton.setText(QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Export Curve Points", None))
        self.Close_pushButton.setText(QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Close", None))
        self.Curves_tabWidget.setTabText(self.Curves_tabWidget.indexOf(self.MC_tab), QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Moment Curvature", None))
        self.Curves_tabWidget.setTabText(self.Curves_tabWidget.indexOf(self.MStrn_tab), QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Moment vs. Strain", None))
        self.Curves_tabWidget.setTabText(self.Curves_tabWidget.indexOf(self.MStrs_tab), QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Moment vs. Stress", None))
        self.Curves_tabWidget.setTabText(self.Curves_tabWidget.indexOf(self.MTS_tab), QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Moment vs. Tangent Slope", None))
        self.Curves_tabWidget.setTabText(self.Curves_tabWidget.indexOf(self.MSS_tab), QCoreApplication.translate("ShowResultsMCurv_Dialog", u"Moment vs. Secant Slope", None))
    # retranslateUi

