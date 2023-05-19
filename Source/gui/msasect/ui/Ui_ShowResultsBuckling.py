# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowResultsBuckling.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_GlobalBucklingPlot_Dialog(object):
    def setupUi(self, GlobalBucklingPlot_Dialog):
        if not GlobalBucklingPlot_Dialog.objectName():
            GlobalBucklingPlot_Dialog.setObjectName(u"GlobalBucklingPlot_Dialog")
        GlobalBucklingPlot_Dialog.resize(640, 704)
        GlobalBucklingPlot_Dialog.setMinimumSize(QSize(640, 580))
        GlobalBucklingPlot_Dialog.setMaximumSize(QSize(5000, 6700))
        GlobalBucklingPlot_Dialog.setStyleSheet(u"QDialog\n"
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
        GlobalBucklingPlot_Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(GlobalBucklingPlot_Dialog)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.tabWidget = QTabWidget(GlobalBucklingPlot_Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.Compression_Layout = QVBoxLayout()
        self.Compression_Layout.setObjectName(u"Compression_Layout")

        self.verticalLayout_4.addLayout(self.Compression_Layout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.PositiveBending_Layout = QVBoxLayout()
        self.PositiveBending_Layout.setObjectName(u"PositiveBending_Layout")

        self.verticalLayout_6.addLayout(self.PositiveBending_Layout)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.NegativeBending_Layout = QVBoxLayout()
        self.NegativeBending_Layout.setObjectName(u"NegativeBending_Layout")

        self.verticalLayout_8.addLayout(self.NegativeBending_Layout)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.groupBox = QGroupBox(GlobalBucklingPlot_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 32))
        self.groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ExportResults_pushButton = QPushButton(self.groupBox)
        self.ExportResults_pushButton.setObjectName(u"ExportResults_pushButton")
        self.ExportResults_pushButton.setMinimumSize(QSize(120, 24))
        self.ExportResults_pushButton.setMaximumSize(QSize(120, 24))
        self.ExportResults_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.ExportResults_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Close_pushButton = QPushButton(self.groupBox)
        self.Close_pushButton.setObjectName(u"Close_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Close_pushButton.sizePolicy().hasHeightForWidth())
        self.Close_pushButton.setSizePolicy(sizePolicy)
        self.Close_pushButton.setMinimumSize(QSize(75, 24))
        self.Close_pushButton.setMaximumSize(QSize(75, 24))
        self.Close_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.Close_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        QWidget.setTabOrder(self.ExportResults_pushButton, self.Close_pushButton)

        self.retranslateUi(GlobalBucklingPlot_Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GlobalBucklingPlot_Dialog)
    # setupUi

    def retranslateUi(self, GlobalBucklingPlot_Dialog):
        GlobalBucklingPlot_Dialog.setWindowTitle(QCoreApplication.translate("GlobalBucklingPlot_Dialog", u"Global Buckling Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("GlobalBucklingPlot_Dialog", u"Under Compression", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("GlobalBucklingPlot_Dialog", u"Under Positive Bending Moment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("GlobalBucklingPlot_Dialog", u"Under Negative Bending moment", None))
        self.groupBox.setTitle("")
        self.ExportResults_pushButton.setText(QCoreApplication.translate("GlobalBucklingPlot_Dialog", u"Export Curve Points", None))
        self.Close_pushButton.setText(QCoreApplication.translate("GlobalBucklingPlot_Dialog", u"Close", None))
    # retranslateUi

