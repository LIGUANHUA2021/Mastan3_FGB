# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowResultsYieldS.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ShowResultsYS_Dialog(object):
    def setupUi(self, ShowResultsYS_Dialog):
        if not ShowResultsYS_Dialog.objectName():
            ShowResultsYS_Dialog.setObjectName(u"ShowResultsYS_Dialog")
        ShowResultsYS_Dialog.resize(1350, 705)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShowResultsYS_Dialog.sizePolicy().hasHeightForWidth())
        ShowResultsYS_Dialog.setSizePolicy(sizePolicy)
        ShowResultsYS_Dialog.setMinimumSize(QSize(1350, 705))
        ShowResultsYS_Dialog.setMaximumSize(QSize(1350, 705))
        ShowResultsYS_Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.gridLayout_3 = QGridLayout(ShowResultsYS_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.YSView_groupBox = QGroupBox(ShowResultsYS_Dialog)
        self.YSView_groupBox.setObjectName(u"YSView_groupBox")
        self.YSView_groupBox.setMinimumSize(QSize(734, 669))
        self.YSView_groupBox.setMaximumSize(QSize(734, 669))
        self.YSView_groupBox.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout = QGridLayout(self.YSView_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(6, 4, 6, 6)
        self.ShowLines_checkBox = QCheckBox(self.YSView_groupBox)
        self.ShowLines_checkBox.setObjectName(u"ShowLines_checkBox")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.ShowLines_checkBox.setFont(font)
        self.ShowLines_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.ShowLines_checkBox, 0, 1, 1, 1)

        self.ShowPoints_checkBox = QCheckBox(self.YSView_groupBox)
        self.ShowPoints_checkBox.setObjectName(u"ShowPoints_checkBox")
        self.ShowPoints_checkBox.setFont(font)
        self.ShowPoints_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.ShowPoints_checkBox, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.FYSShow_verticalLayout = QVBoxLayout()
        self.FYSShow_verticalLayout.setSpacing(0)
        self.FYSShow_verticalLayout.setObjectName(u"FYSShow_verticalLayout")
        self.FYSShow_verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout.addLayout(self.FYSShow_verticalLayout, 5, 0, 1, 3)


        self.gridLayout_3.addWidget(self.YSView_groupBox, 0, 0, 1, 1)

        self.frame = QFrame(ShowResultsYS_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(734, 32))
        self.frame.setMaximumSize(QSize(734, 32))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 3, 4, 4)
        self.ExportSP_pushButton = QPushButton(self.frame)
        self.ExportSP_pushButton.setObjectName(u"ExportSP_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ExportSP_pushButton.sizePolicy().hasHeightForWidth())
        self.ExportSP_pushButton.setSizePolicy(sizePolicy1)
        self.ExportSP_pushButton.setMinimumSize(QSize(220, 22))
        self.ExportSP_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.ExportSP_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ExportSP_pushButton)

        self.horizontalSpacer = QSpacerItem(475, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)

        self.frame_2 = QFrame(ShowResultsYS_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(612, 32))
        self.frame_2.setMaximumSize(QSize(612, 32))
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
        self.Close_pushButton.setMinimumSize(QSize(80, 22))
        self.Close_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.Close_pushButton)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 1)

        self.TwoDPlot_groupBox = QGroupBox(ShowResultsYS_Dialog)
        self.TwoDPlot_groupBox.setObjectName(u"TwoDPlot_groupBox")
        self.TwoDPlot_groupBox.setMinimumSize(QSize(612, 669))
        self.TwoDPlot_groupBox.setMaximumSize(QSize(612, 669))
        self.TwoDPlot_groupBox.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.YS2DPlot_verticalLayout = QVBoxLayout(self.TwoDPlot_groupBox)
        self.YS2DPlot_verticalLayout.setObjectName(u"YS2DPlot_verticalLayout")
        self.YS2DPlot_verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.YS2DPlot_verticalLayout.setContentsMargins(2, 4, 2, 2)
        self.YS2DPlot_verticalLayout_2 = QVBoxLayout()
        self.YS2DPlot_verticalLayout_2.setObjectName(u"YS2DPlot_verticalLayout_2")
        self.YS2DPlot_verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.YS2DPlot_verticalLayout.addLayout(self.YS2DPlot_verticalLayout_2)

        self.groupBox = QGroupBox(self.TwoDPlot_groupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(606, 259))
        self.groupBox.setMaximumSize(QSize(606, 259))
        self.groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.LoadingP_tableWidget = QTableWidget(self.groupBox)
        if (self.LoadingP_tableWidget.columnCount() < 5):
            self.LoadingP_tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.LoadingP_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.LoadingP_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.LoadingP_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.LoadingP_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.LoadingP_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.LoadingP_tableWidget.rowCount() < 3):
            self.LoadingP_tableWidget.setRowCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.LoadingP_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.LoadingP_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.LoadingP_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.LoadingP_tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.LoadingP_tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.LoadingP_tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.LoadingP_tableWidget.setItem(0, 3, __qtablewidgetitem11)
        self.LoadingP_tableWidget.setObjectName(u"LoadingP_tableWidget")
        self.LoadingP_tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.LoadingP_tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Delete_pushButton = QPushButton(self.groupBox)
        self.Delete_pushButton.setObjectName(u"Delete_pushButton")
        self.Delete_pushButton.setMinimumSize(QSize(80, 22))
        self.Delete_pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.Delete_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.YS2DPlot_verticalLayout.addWidget(self.groupBox)

        self.YS2DPlot_verticalLayout.setStretch(0, 3)
        self.YS2DPlot_verticalLayout.setStretch(1, 2)

        self.gridLayout_3.addWidget(self.TwoDPlot_groupBox, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 6)
        self.gridLayout_3.setColumnStretch(1, 5)

        self.retranslateUi(ShowResultsYS_Dialog)

        QMetaObject.connectSlotsByName(ShowResultsYS_Dialog)
    # setupUi

    def retranslateUi(self, ShowResultsYS_Dialog):
        ShowResultsYS_Dialog.setWindowTitle(QCoreApplication.translate("ShowResultsYS_Dialog", u"Full Yield Suface Results", None))
        self.YSView_groupBox.setTitle(QCoreApplication.translate("ShowResultsYS_Dialog", u"Yield Surface View", None))
        self.ShowLines_checkBox.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Show Lines", None))
        self.ShowPoints_checkBox.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Show Points", None))
        self.ExportSP_pushButton.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Export Surface Points", None))
        self.ClearInput_pushButton.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Clear Input", None))
        self.Close_pushButton.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Close", None))
        self.TwoDPlot_groupBox.setTitle(QCoreApplication.translate("ShowResultsYS_Dialog", u"2D Plot", None))
        self.groupBox.setTitle(QCoreApplication.translate("ShowResultsYS_Dialog", u"Loading Points", None))
        ___qtablewidgetitem = self.LoadingP_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.LoadingP_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Px", None));
        ___qtablewidgetitem2 = self.LoadingP_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"My", None));
        ___qtablewidgetitem3 = self.LoadingP_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Mz", None));
        ___qtablewidgetitem4 = self.LoadingP_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"SCF", None));
        ___qtablewidgetitem5 = self.LoadingP_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"1", None));

        __sortingEnabled = self.LoadingP_tableWidget.isSortingEnabled()
        self.LoadingP_tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.LoadingP_tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"1", None));
        ___qtablewidgetitem7 = self.LoadingP_tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"kN", None));
        ___qtablewidgetitem8 = self.LoadingP_tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"kN*m", None));
        ___qtablewidgetitem9 = self.LoadingP_tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"kN*m", None));
        self.LoadingP_tableWidget.setSortingEnabled(__sortingEnabled)

        self.Delete_pushButton.setText(QCoreApplication.translate("ShowResultsYS_Dialog", u"Delete", None))
    # retranslateUi

