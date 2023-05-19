# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowResultsYieldS2D.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ShowResultsYS2D_Dialog(object):
    def setupUi(self, ShowResultsYS2D_Dialog):
        if not ShowResultsYS2D_Dialog.objectName():
            ShowResultsYS2D_Dialog.setObjectName(u"ShowResultsYS2D_Dialog")
        ShowResultsYS2D_Dialog.resize(950, 525)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShowResultsYS2D_Dialog.sizePolicy().hasHeightForWidth())
        ShowResultsYS2D_Dialog.setSizePolicy(sizePolicy)
        ShowResultsYS2D_Dialog.setMinimumSize(QSize(950, 525))
        ShowResultsYS2D_Dialog.setMaximumSize(QSize(950, 525))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        ShowResultsYS2D_Dialog.setFont(font)
        ShowResultsYS2D_Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.gridLayout_3 = QGridLayout(ShowResultsYS2D_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.YSView_groupBox = QGroupBox(ShowResultsYS2D_Dialog)
        self.YSView_groupBox.setObjectName(u"YSView_groupBox")
        self.YSView_groupBox.setMinimumSize(QSize(631, 489))
        self.YSView_groupBox.setMaximumSize(QSize(631, 489))
        self.YSView_groupBox.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.YSView_groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 4, 6, 6)
        self.YS2DPlot_verticalLayout = QVBoxLayout()
        self.YS2DPlot_verticalLayout.setSpacing(0)
        self.YS2DPlot_verticalLayout.setObjectName(u"YS2DPlot_verticalLayout")
        self.YS2DPlot_verticalLayout.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout.addLayout(self.YS2DPlot_verticalLayout)


        self.gridLayout_3.addWidget(self.YSView_groupBox, 0, 0, 1, 1)

        self.TwoDPlot_groupBox = QGroupBox(ShowResultsYS2D_Dialog)
        self.TwoDPlot_groupBox.setObjectName(u"TwoDPlot_groupBox")
        self.TwoDPlot_groupBox.setMinimumSize(QSize(315, 489))
        self.TwoDPlot_groupBox.setMaximumSize(QSize(315, 489))
        self.verticalLayout_2 = QVBoxLayout(self.TwoDPlot_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 4, 6, 6)
        self.LoadingP_2D_tableWidget = QTableWidget(self.TwoDPlot_groupBox)
        if (self.LoadingP_2D_tableWidget.columnCount() < 4):
            self.LoadingP_2D_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.LoadingP_2D_tableWidget.rowCount() < 3):
            self.LoadingP_2D_tableWidget.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.LoadingP_2D_tableWidget.setItem(2, 0, __qtablewidgetitem11)
        self.LoadingP_2D_tableWidget.setObjectName(u"LoadingP_2D_tableWidget")
        self.LoadingP_2D_tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.LoadingP_2D_tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Delete_pushButton = QPushButton(self.TwoDPlot_groupBox)
        self.Delete_pushButton.setObjectName(u"Delete_pushButton")
        self.Delete_pushButton.setMinimumSize(QSize(80, 22))
        self.Delete_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.Delete_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 2)

        self.gridLayout_3.addWidget(self.TwoDPlot_groupBox, 0, 1, 1, 1)

        self.frame = QFrame(ShowResultsYS2D_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(631, 32))
        self.frame.setMaximumSize(QSize(631, 32))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 3, 4, 4)
        self.ExportSP_pushButton = QPushButton(self.frame)
        self.ExportSP_pushButton.setObjectName(u"ExportSP_pushButton")
        self.ExportSP_pushButton.setMinimumSize(QSize(0, 22))
        self.ExportSP_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ExportSP_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 12)

        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)

        self.frame_2 = QFrame(ShowResultsYS2D_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(315, 32))
        self.frame_2.setMaximumSize(QSize(315, 32))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 3, 4, 4)
        self.horizontalSpacer_2 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.ClearInput_pushButton = QPushButton(self.frame_2)
        self.ClearInput_pushButton.setObjectName(u"ClearInput_pushButton")
        self.ClearInput_pushButton.setMinimumSize(QSize(80, 22))
        self.ClearInput_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ClearInput_pushButton)

        self.Close_pushButton = QPushButton(self.frame_2)
        self.Close_pushButton.setObjectName(u"Close_pushButton")
        self.Close_pushButton.setMinimumSize(QSize(70, 22))
        self.Close_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Close_pushButton)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 4)
        self.gridLayout_3.setColumnStretch(1, 2)

        self.retranslateUi(ShowResultsYS2D_Dialog)

        QMetaObject.connectSlotsByName(ShowResultsYS2D_Dialog)
    # setupUi

    def retranslateUi(self, ShowResultsYS2D_Dialog):
        ShowResultsYS2D_Dialog.setWindowTitle(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Two Dimensional Yield Curve", None))
        self.YSView_groupBox.setTitle(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Strength Interaction Curve", None))
        self.TwoDPlot_groupBox.setTitle(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Loading Points", None))
        ___qtablewidgetitem = self.LoadingP_2D_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.LoadingP_2D_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Px", None));
        ___qtablewidgetitem2 = self.LoadingP_2D_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"My", None));
        ___qtablewidgetitem3 = self.LoadingP_2D_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"SCF", None));
        ___qtablewidgetitem4 = self.LoadingP_2D_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"1", None));

        __sortingEnabled = self.LoadingP_2D_tableWidget.isSortingEnabled()
        self.LoadingP_2D_tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.LoadingP_2D_tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"1", None));
        ___qtablewidgetitem6 = self.LoadingP_2D_tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"kN", None));
        ___qtablewidgetitem7 = self.LoadingP_2D_tableWidget.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"kN*m", None));
        self.LoadingP_2D_tableWidget.setSortingEnabled(__sortingEnabled)

        self.Delete_pushButton.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Delete", None))
        self.ExportSP_pushButton.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Export Curve Points", None))
        self.ClearInput_pushButton.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Clear Input", None))
        self.Close_pushButton.setText(QCoreApplication.translate("ShowResultsYS2D_Dialog", u"Close", None))
    # retranslateUi

