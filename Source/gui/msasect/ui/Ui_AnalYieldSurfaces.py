# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnalYieldSurfaces.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_YieldSurfaces_Dialog(object):
    def setupUi(self, YieldSurfaces_Dialog):
        if not YieldSurfaces_Dialog.objectName():
            YieldSurfaces_Dialog.setObjectName(u"YieldSurfaces_Dialog")
        YieldSurfaces_Dialog.resize(420, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(YieldSurfaces_Dialog.sizePolicy().hasHeightForWidth())
        YieldSurfaces_Dialog.setSizePolicy(sizePolicy)
        YieldSurfaces_Dialog.setMinimumSize(QSize(420, 608))
        YieldSurfaces_Dialog.setMaximumSize(QSize(420, 608))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        YieldSurfaces_Dialog.setFont(font)
        YieldSurfaces_Dialog.setStyleSheet(u"*{\n"
                                           "	font: 9pt \"Segoe UI\";\n"
                                           "}\n"
                                           "QDialog\n"
                                           "{\n"
                                           "	background-color: rgb(43, 43, 43);\n"
                                           "}\n"
                                           "QGroupBox\n"
                                           "{\n"
                                           "	background-color: rgb(128, 128, 128);\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "QLabel\n"
                                           "{\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "QLineEdit\n"
                                           "{\n"
                                           "	border-radius: 3px;\n"
                                           "}\n"
                                           "QLineEdit::hover\n"
                                           "{\n"
                                           "	background-color: rgb(244, 244, 244);\n"
                                           "}\n"
                                           "QLineEdit:disabled\n"
                                           "{\n"
                                           "	background-color: rgb(160, 160, 160);\n"
                                           "}\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "	background-color: rgb(255, 255, 255);\n"
                                           "	border-radius: 3px;\n"
                                           "}\n"
                                           "QPushButton::hover\n"
                                           "{\n"
                                           "	background-color: rgb(144, 200, 246);\n"
                                           "}\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "	padding-left: 3px;\n"
                                           "	padding-top: 3px;\n"
                                           "}\n"
                                           "QPushButton::disabled\n"
                                           "{\n"
                                           "	background-color: rgb(160, 160, 160);\n"
                                           "	color: rgb(80, 80, 80);\n"
                                           "}\n"
                                           "QRadioButton\n"
                                           "{\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "QRadioButton::disabled\n"
                                           "{\n"
                                           "	color: rgb(80, 80, 80);\n"
                                           "}\n"
                                           "QRadioButton::indicator:disabled\n"
                                           "{\n"
                                           "	height: 13px;\n"
                                           ""
                                           "	width: 13px;\n"
                                           "	background-color: rgb(160, 160, 160);\n"
                                           "	border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "")
        YieldSurfaces_Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(YieldSurfaces_Dialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.AxisSelection_GroupBox = QGroupBox(YieldSurfaces_Dialog)
        self.AxisSelection_GroupBox.setObjectName(u"AxisSelection_GroupBox")
        self.AxisSelection_GroupBox.setMinimumSize(QSize(0, 50))
        self.AxisSelection_GroupBox.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.AxisSelection_GroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(25, 4, 4, 6)
        self.PrincipalAxis_radioButton = QRadioButton(self.AxisSelection_GroupBox)
        self.PrincipalAxis_radioButton.setObjectName(u"PrincipalAxis_radioButton")
        self.PrincipalAxis_radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.PrincipalAxis_radioButton)

        self.UsedefinedAxis_radioButton = QRadioButton(self.AxisSelection_GroupBox)
        self.UsedefinedAxis_radioButton.setObjectName(u"UsedefinedAxis_radioButton")
        self.UsedefinedAxis_radioButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.UsedefinedAxis_radioButton)

        self.verticalLayout.addWidget(self.AxisSelection_GroupBox)

        self.AnalysisOptions_groupBox = QGroupBox(YieldSurfaces_Dialog)
        self.AnalysisOptions_groupBox.setObjectName(u"AnalysisOptions_groupBox")
        self.AnalysisOptions_groupBox.setMinimumSize(QSize(0, 90))
        self.AnalysisOptions_groupBox.setMaximumSize(QSize(16777215, 90))
        self.AnalysisOptions_groupBox.setFont(font)
        self.gridLayout_5 = QGridLayout(self.AnalysisOptions_groupBox)
        self.gridLayout_5.setSpacing(4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(25, 4, 4, 4)
        self.FYSPMyMz_radioButton = QRadioButton(self.AnalysisOptions_groupBox)
        self.FYSPMyMz_radioButton.setObjectName(u"FYSPMyMz_radioButton")
        self.FYSPMyMz_radioButton.setChecked(True)

        self.gridLayout_5.addWidget(self.FYSPMyMz_radioButton, 0, 0, 1, 1)

        self.PYSMyMz_radioButton = QRadioButton(self.AnalysisOptions_groupBox)
        self.PYSMyMz_radioButton.setObjectName(u"PYSMyMz_radioButton")

        self.gridLayout_5.addWidget(self.PYSMyMz_radioButton, 2, 0, 1, 1)

        self.PYSPMy_radioButton = QRadioButton(self.AnalysisOptions_groupBox)
        self.PYSPMy_radioButton.setObjectName(u"PYSPMy_radioButton")

        self.gridLayout_5.addWidget(self.PYSPMy_radioButton, 0, 1, 1, 1)

        self.PYSPMz_radioButton = QRadioButton(self.AnalysisOptions_groupBox)
        self.PYSPMz_radioButton.setObjectName(u"PYSPMz_radioButton")

        self.gridLayout_5.addWidget(self.PYSPMz_radioButton, 2, 1, 1, 1)

        self.verticalLayout.addWidget(self.AnalysisOptions_groupBox)

        self.Mesh_groupBox = QGroupBox(YieldSurfaces_Dialog)
        self.Mesh_groupBox.setObjectName(u"Mesh_groupBox")
        self.Mesh_groupBox.setMinimumSize(QSize(0, 120))
        self.Mesh_groupBox.setMaximumSize(QSize(16777215, 120))
        self.gridLayout = QGridLayout(self.Mesh_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(25, 4, 4, 4)
        self.MeshSize_radioButton = QRadioButton(self.Mesh_groupBox)
        self.MeshSize_radioButton.setObjectName(u"MeshSize_radioButton")
        self.MeshSize_radioButton.setMinimumSize(QSize(208, 0))
        self.MeshSize_radioButton.setMaximumSize(QSize(180, 16777215))

        self.gridLayout.addWidget(self.MeshSize_radioButton, 2, 0, 1, 1)

        self.UseExistingMesh_radioButton = QRadioButton(self.Mesh_groupBox)
        self.UseExistingMesh_radioButton.setObjectName(u"UseExistingMesh_radioButton")

        self.gridLayout.addWidget(self.UseExistingMesh_radioButton, 0, 0, 1, 1)

        self.AutoMesh_radioButton = QRadioButton(self.Mesh_groupBox)
        self.AutoMesh_radioButton.setObjectName(u"AutoMesh_radioButton")

        self.gridLayout.addWidget(self.AutoMesh_radioButton, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.Mesh_groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(50, 20))
        self.lineEdit.setMaximumSize(QSize(50, 20))
        self.lineEdit.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.verticalLayout.addWidget(self.Mesh_groupBox)

        self.StrainControl_groupBox = QGroupBox(YieldSurfaces_Dialog)
        self.StrainControl_groupBox.setObjectName(u"StrainControl_groupBox")
        self.StrainControl_groupBox.setMinimumSize(QSize(0, 120))
        self.StrainControl_groupBox.setMaximumSize(QSize(16777215, 120))
        self.StrainControl_groupBox.setFont(font)
        self.gridLayout_4 = QGridLayout(self.StrainControl_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(25, 4, 4, 6)
        self.SOMS_radioButton = QRadioButton(self.StrainControl_groupBox)
        self.SOMS_radioButton.setObjectName(u"SOMS_radioButton")

        self.gridLayout_4.addWidget(self.SOMS_radioButton, 1, 0, 1, 1)

        self.LStrain_Input = QLineEdit(self.StrainControl_groupBox)
        self.LStrain_Input.setObjectName(u"LStrain_Input")
        sizePolicy.setHeightForWidth(self.LStrain_Input.sizePolicy().hasHeightForWidth())
        self.LStrain_Input.setSizePolicy(sizePolicy)
        self.LStrain_Input.setMinimumSize(QSize(50, 20))
        self.LStrain_Input.setMaximumSize(QSize(50, 20))

        self.gridLayout_4.addWidget(self.LStrain_Input, 2, 1, 1, 1)

        self.SRUS_radioButton = QRadioButton(self.StrainControl_groupBox)
        self.SRUS_radioButton.setObjectName(u"SRUS_radioButton")
        self.SRUS_radioButton.setChecked(True)

        self.gridLayout_4.addWidget(self.SRUS_radioButton, 0, 0, 1, 1)

        self.LStrainValue_radioButton = QRadioButton(self.StrainControl_groupBox)
        self.LStrainValue_radioButton.setObjectName(u"LStrainValue_radioButton")
        self.LStrainValue_radioButton.setChecked(False)

        self.gridLayout_4.addWidget(self.LStrainValue_radioButton, 2, 0, 1, 1)

        self.verticalLayout.addWidget(self.StrainControl_groupBox)

        self.DataPointIntensity_groupBox = QGroupBox(YieldSurfaces_Dialog)
        self.DataPointIntensity_groupBox.setObjectName(u"DataPointIntensity_groupBox")
        self.DataPointIntensity_groupBox.setMinimumSize(QSize(0, 90))
        self.DataPointIntensity_groupBox.setMaximumSize(QSize(16777215, 90))
        self.DataPointIntensity_groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.DataPointIntensity_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(25, 4, 4, 4)
        self.NumALoad_Inoput = QLineEdit(self.DataPointIntensity_groupBox)
        self.NumALoad_Inoput.setObjectName(u"NumALoad_Inoput")
        sizePolicy.setHeightForWidth(self.NumALoad_Inoput.sizePolicy().hasHeightForWidth())
        self.NumALoad_Inoput.setSizePolicy(sizePolicy)
        self.NumALoad_Inoput.setMinimumSize(QSize(50, 20))
        self.NumALoad_Inoput.setMaximumSize(QSize(50, 20))
        self.NumALoad_Inoput.setLayoutDirection(Qt.RightToLeft)
        self.NumALoad_Inoput.setCursorPosition(2)
        self.NumALoad_Inoput.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.NumALoad_Inoput, 0, 1, 1, 1)

        self.NumInclinedAngle_Input = QLineEdit(self.DataPointIntensity_groupBox)
        self.NumInclinedAngle_Input.setObjectName(u"NumInclinedAngle_Input")
        sizePolicy.setHeightForWidth(self.NumInclinedAngle_Input.sizePolicy().hasHeightForWidth())
        self.NumInclinedAngle_Input.setSizePolicy(sizePolicy)
        self.NumInclinedAngle_Input.setMinimumSize(QSize(50, 20))
        self.NumInclinedAngle_Input.setMaximumSize(QSize(50, 20))
        self.NumInclinedAngle_Input.setCursorPosition(2)

        self.gridLayout_2.addWidget(self.NumInclinedAngle_Input, 1, 1, 1, 1)

        self.NumInclinedAngle_label = QLabel(self.DataPointIntensity_groupBox)
        self.NumInclinedAngle_label.setObjectName(u"NumInclinedAngle_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NumInclinedAngle_label.sizePolicy().hasHeightForWidth())
        self.NumInclinedAngle_label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.NumInclinedAngle_label, 1, 0, 1, 1)

        self.NumAxialLoad_label = QLabel(self.DataPointIntensity_groupBox)
        self.NumAxialLoad_label.setObjectName(u"NumAxialLoad_label")
        sizePolicy1.setHeightForWidth(self.NumAxialLoad_label.sizePolicy().hasHeightForWidth())
        self.NumAxialLoad_label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.NumAxialLoad_label, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.DataPointIntensity_groupBox)

        self.InteractiveOptions_groupBox = QGroupBox(YieldSurfaces_Dialog)
        self.InteractiveOptions_groupBox.setObjectName(u"InteractiveOptions_groupBox")
        self.InteractiveOptions_groupBox.setMinimumSize(QSize(0, 90))
        self.InteractiveOptions_groupBox.setMaximumSize(QSize(16777215, 90))
        self.InteractiveOptions_groupBox.setFont(font)
        self.gridLayout_3 = QGridLayout(self.InteractiveOptions_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(25, 4, 4, 6)
        self.MaxNumIter_label = QLabel(self.InteractiveOptions_groupBox)
        self.MaxNumIter_label.setObjectName(u"MaxNumIter_label")
        sizePolicy1.setHeightForWidth(self.MaxNumIter_label.sizePolicy().hasHeightForWidth())
        self.MaxNumIter_label.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.MaxNumIter_label, 0, 0, 1, 1)

        self.ConvergenceTol_label = QLabel(self.InteractiveOptions_groupBox)
        self.ConvergenceTol_label.setObjectName(u"ConvergenceTol_label")
        sizePolicy1.setHeightForWidth(self.ConvergenceTol_label.sizePolicy().hasHeightForWidth())
        self.ConvergenceTol_label.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.ConvergenceTol_label, 1, 0, 1, 1)

        self.ConvergenceTol_Input = QLineEdit(self.InteractiveOptions_groupBox)
        self.ConvergenceTol_Input.setObjectName(u"ConvergenceTol_Input")
        sizePolicy.setHeightForWidth(self.ConvergenceTol_Input.sizePolicy().hasHeightForWidth())
        self.ConvergenceTol_Input.setSizePolicy(sizePolicy)
        self.ConvergenceTol_Input.setMinimumSize(QSize(50, 20))
        self.ConvergenceTol_Input.setMaximumSize(QSize(50, 20))

        self.gridLayout_3.addWidget(self.ConvergenceTol_Input, 1, 1, 1, 1)

        self.MaxNumIteration_Input = QLineEdit(self.InteractiveOptions_groupBox)
        self.MaxNumIteration_Input.setObjectName(u"MaxNumIteration_Input")
        sizePolicy.setHeightForWidth(self.MaxNumIteration_Input.sizePolicy().hasHeightForWidth())
        self.MaxNumIteration_Input.setSizePolicy(sizePolicy)
        self.MaxNumIteration_Input.setMinimumSize(QSize(50, 20))
        self.MaxNumIteration_Input.setMaximumSize(QSize(50, 20))

        self.gridLayout_3.addWidget(self.MaxNumIteration_Input, 0, 1, 1, 1)

        self.verticalLayout.addWidget(self.InteractiveOptions_groupBox)

        self.groupBox_4 = QGroupBox(YieldSurfaces_Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 4, 2, 4)
        self.ShowResults_pushButton = QPushButton(self.groupBox_4)
        self.ShowResults_pushButton.setObjectName(u"ShowResults_pushButton")
        sizePolicy.setHeightForWidth(self.ShowResults_pushButton.sizePolicy().hasHeightForWidth())
        self.ShowResults_pushButton.setSizePolicy(sizePolicy)
        self.ShowResults_pushButton.setMinimumSize(QSize(80, 22))
        self.ShowResults_pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.ShowResults_pushButton)

        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Run_pushButton = QPushButton(self.groupBox_4)
        self.Run_pushButton.setObjectName(u"Run_pushButton")
        sizePolicy.setHeightForWidth(self.Run_pushButton.sizePolicy().hasHeightForWidth())
        self.Run_pushButton.setSizePolicy(sizePolicy)
        self.Run_pushButton.setMinimumSize(QSize(65, 22))

        self.horizontalLayout.addWidget(self.Run_pushButton)

        self.Cancel_pushButton = QPushButton(self.groupBox_4)
        self.Cancel_pushButton.setObjectName(u"Cancel_pushButton")
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setMinimumSize(QSize(65, 22))

        self.horizontalLayout.addWidget(self.Cancel_pushButton)

        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)

        self.retranslateUi(YieldSurfaces_Dialog)

        QMetaObject.connectSlotsByName(YieldSurfaces_Dialog)

    # setupUi

    def retranslateUi(self, YieldSurfaces_Dialog):
        YieldSurfaces_Dialog.setWindowTitle(QCoreApplication.translate("YieldSurfaces_Dialog", u"Yield Surface", None))
        self.AxisSelection_GroupBox.setTitle(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Axis Selection", None))
        self.PrincipalAxis_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Principal Axis", None))
        self.UsedefinedAxis_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Geometric Axis", None))
        self.AnalysisOptions_groupBox.setTitle(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Analysis Options", None))
        self.FYSPMyMz_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Full Yield Surface (P-Mv-Mw)", None))
        self.PYSMyMz_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Planar Yield Surface (Mv-Mw)", None))
        self.PYSPMy_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Planar Yield Surface (P-Mv)", None))
        self.PYSPMz_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Planar Yield Surface (P-Mw)", None))
        self.Mesh_groupBox.setTitle(QCoreApplication.translate("YieldSurfaces_Dialog", u"Mesh Setting", None))
        self.MeshSize_radioButton.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"Mesh Size", None))
        self.UseExistingMesh_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Use the Existing Mesh", None))
        self.AutoMesh_radioButton.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"Auto Mesh ", None))
        self.StrainControl_groupBox.setTitle(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Strain Control", None))
        self.SOMS_radioButton.setText(QCoreApplication.translate("YieldSurfaces_Dialog",
                                                                 u"Strain at the onset of Maximum Stress (Initial Yield Suface)",
                                                                 None))
        self.LStrain_Input.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"0.001", None))
        self.SRUS_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Strain Reaches Ultimate Strain (Failure Surface)",
                                       None))
        self.LStrainValue_radioButton.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Strain at the Value of ", None))
        self.DataPointIntensity_groupBox.setTitle(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Data Point Intensity", None))
        self.NumALoad_Inoput.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"20", None))
        self.NumInclinedAngle_Input.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"20", None))
        self.NumInclinedAngle_label.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Number of Interval of Inclined Angle: ", None))
        self.NumAxialLoad_label.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Number of Interval of Axial Load: ", None))
        self.InteractiveOptions_groupBox.setTitle(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Interactive Options", None))
        self.MaxNumIter_label.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Maximum Number of Iteration:", None))
        self.ConvergenceTol_label.setText(
            QCoreApplication.translate("YieldSurfaces_Dialog", u"Convergence Tolerance:", None))
        self.ConvergenceTol_Input.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"0.001", None))
        self.MaxNumIteration_Input.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"300", None))
        self.groupBox_4.setTitle("")
        self.ShowResults_pushButton.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"Show Results", None))
        self.Run_pushButton.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"Run", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("YieldSurfaces_Dialog", u"Cancel", None))
