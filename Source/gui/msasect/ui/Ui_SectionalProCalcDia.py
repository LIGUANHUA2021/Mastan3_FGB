# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SectionalProCalcDia.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SectPropCal_Dialog(object):
    def setupUi(self, SectPropCal_Dialog):
        if not SectPropCal_Dialog.objectName():
            SectPropCal_Dialog.setObjectName(u"SectPropCal_Dialog")
        SectPropCal_Dialog.resize(354, 431)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SectPropCal_Dialog.sizePolicy().hasHeightForWidth())
        SectPropCal_Dialog.setSizePolicy(sizePolicy)
        SectPropCal_Dialog.setMinimumSize(QSize(354, 431))
        SectPropCal_Dialog.setMaximumSize(QSize(354, 431))
        SectPropCal_Dialog.setStyleSheet(u"*{\n"
                                         "font: 9pt \"Segoe UI\";\n"
                                         "}\n"
                                         "\n"
                                         "QDialog\n"
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
                                         "	border-radius: 3px;\n"
                                         "}        \n"
                                         "QComboBox\n"
                                         "{\n"
                                         "	border-radius: 3px;\n"
                                         "}\n"
                                         "QComboBox:hover\n"
                                         "{\n"
                                         "	background-color: rgb(244, 244, 244);\n"
                                         "}\n"
                                         "QComboBox::drop-down\n"
                                         "{\n"
                                         "	width: 20px;\n"
                                         "	border-left: 1px solid rgb(192, 192, 192);\n"
                                         "	border-top-right-radius: 3px;\n"
                                         "	border-bottom-right-radius: 3px;\n"
                                         "}\n"
                                         "QComboBox::down-arrow\n"
                                         "{\n"
                                         "	image:url(ui/ico/DownArrow.png);\n"
                                         "	width: 10px;\n"
                                         "}\n"
                                         "QComboBox:disabled\n"
                                         "{\n"
                                         "	background-color: rgb(160, 160, 160);\n"
                                         "}\n"
                                         "QComboBox::drop-down:disabled\n"
                                         "{\n"
                                         "	border-left: 1px solid rgb(128, 128, 128);\n"
                                         "}\n"
                                         "QGroupBox\n"
                                         "{\n"
                                         "	background-color: rgb(128, 128, 128);\n"
                                         "	color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "QL"
                                         "abel\n"
                                         "{\n"
                                         "	color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "QLabel:disabled\n"
                                         "{\n"
                                         "	color: rgb(80, 80, 80);\n"
                                         "}\n"
                                         "QLineEdit\n"
                                         "{\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "	border-radius: 3px;\n"
                                         "}\n"
                                         "QLineEdit:hover\n"
                                         "{\n"
                                         "	background-color: rgb(244, 244, 244);\n"
                                         "}\n"
                                         "QLineEdit:disabled\n"
                                         "{\n"
                                         "	background-color: rgb(160, 160, 160);\n"
                                         "	color: rgb(80, 80, 80);\n"
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
                                         "QRadioButton\n"
                                         "{\n"
                                         "	color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "QRadioButton:disabled\n"
                                         "{\n"
                                         "	color: rgb(80, 80, 80);\n"
                                         "}\n"
                                         "QRadioButton::indicator:disabled\n"
                                         "{\n"
                                         "	height: 13px;\n"
                                         "	width: 13px;\n"
                                         "	background-color: rgb(160, 160, 160);\n"
                                         "	border-radius: 6px;\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(SectPropCal_Dialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(2, 2, 2, 1)
        self.groupBox = QGroupBox(SectPropCal_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(350, 50))
        self.groupBox.setMaximumSize(QSize(350, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 4, 50, 4)
        self.CM_radioButton = QRadioButton(self.groupBox)
        self.CM_radioButton.setObjectName(u"CM_radioButton")
        sizePolicy.setHeightForWidth(self.CM_radioButton.sizePolicy().hasHeightForWidth())
        self.CM_radioButton.setSizePolicy(sizePolicy)
        self.CM_radioButton.setMinimumSize(QSize(125, 0))
        self.CM_radioButton.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_2.addWidget(self.CM_radioButton)

        self.FE_radioButton = QRadioButton(self.groupBox)
        self.FE_radioButton.setObjectName(u"FE_radioButton")
        sizePolicy.setHeightForWidth(self.FE_radioButton.sizePolicy().hasHeightForWidth())
        self.FE_radioButton.setSizePolicy(sizePolicy)
        self.FE_radioButton.setMinimumSize(QSize(140, 0))
        self.FE_radioButton.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_2.addWidget(self.FE_radioButton)

        self.verticalLayout.addWidget(self.groupBox)

        self.Mat_groupBox = QGroupBox(SectPropCal_Dialog)
        self.Mat_groupBox.setObjectName(u"Mat_groupBox")
        sizePolicy.setHeightForWidth(self.Mat_groupBox.sizePolicy().hasHeightForWidth())
        self.Mat_groupBox.setSizePolicy(sizePolicy)
        self.Mat_groupBox.setMinimumSize(QSize(350, 160))
        self.Mat_groupBox.setMaximumSize(QSize(350, 160))
        self.gridLayout_3 = QGridLayout(self.Mat_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setContentsMargins(25, 4, 4, 4)
        self.EquivPR_lineEdit = QLineEdit(self.Mat_groupBox)
        self.EquivPR_lineEdit.setObjectName(u"EquivPR_lineEdit")
        sizePolicy.setHeightForWidth(self.EquivPR_lineEdit.sizePolicy().hasHeightForWidth())
        self.EquivPR_lineEdit.setSizePolicy(sizePolicy)
        self.EquivPR_lineEdit.setMinimumSize(QSize(80, 20))
        self.EquivPR_lineEdit.setMaximumSize(QSize(80, 20))

        self.gridLayout_3.addWidget(self.EquivPR_lineEdit, 3, 2, 1, 1)

        self.EquivE_lineEdit = QLineEdit(self.Mat_groupBox)
        self.EquivE_lineEdit.setObjectName(u"EquivE_lineEdit")
        self.EquivE_lineEdit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.EquivE_lineEdit.sizePolicy().hasHeightForWidth())
        self.EquivE_lineEdit.setSizePolicy(sizePolicy)
        self.EquivE_lineEdit.setMinimumSize(QSize(80, 20))
        self.EquivE_lineEdit.setMaximumSize(QSize(80, 20))

        self.gridLayout_3.addWidget(self.EquivE_lineEdit, 2, 2, 1, 1)

        self.Refmat_comboBox = QComboBox(self.Mat_groupBox)
        self.Refmat_comboBox.setObjectName(u"Refmat_comboBox")
        sizePolicy.setHeightForWidth(self.Refmat_comboBox.sizePolicy().hasHeightForWidth())
        self.Refmat_comboBox.setSizePolicy(sizePolicy)
        self.Refmat_comboBox.setMinimumSize(QSize(80, 20))
        self.Refmat_comboBox.setMaximumSize(QSize(80, 20))

        self.gridLayout_3.addWidget(self.Refmat_comboBox, 0, 2, 1, 1)

        self.UseDefValues_radioButton = QRadioButton(self.Mat_groupBox)
        self.UseDefValues_radioButton.setObjectName(u"UseDefValues_radioButton")

        self.gridLayout_3.addWidget(self.UseDefValues_radioButton, 1, 0, 1, 1)

        self.label_2 = QLabel(self.Mat_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setIndent(25)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.Mat_groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setIndent(25)

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.Mat_groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setIndent(25)

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.UseRefMat_radioButton = QRadioButton(self.Mat_groupBox)
        self.UseRefMat_radioButton.setObjectName(u"UseRefMat_radioButton")
        self.UseRefMat_radioButton.setChecked(True)

        self.gridLayout_3.addWidget(self.UseRefMat_radioButton, 0, 0, 1, 1)

        self.EquivDesiStrs_lineEdit = QLineEdit(self.Mat_groupBox)
        self.EquivDesiStrs_lineEdit.setObjectName(u"EquivDesiStrs_lineEdit")
        sizePolicy.setHeightForWidth(self.EquivDesiStrs_lineEdit.sizePolicy().hasHeightForWidth())
        self.EquivDesiStrs_lineEdit.setSizePolicy(sizePolicy)
        self.EquivDesiStrs_lineEdit.setMinimumSize(QSize(80, 21))
        self.EquivDesiStrs_lineEdit.setMaximumSize(QSize(80, 20))

        self.gridLayout_3.addWidget(self.EquivDesiStrs_lineEdit, 4, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.verticalLayout.addWidget(self.Mat_groupBox)

        self.Mesh_groupBox = QGroupBox(SectPropCal_Dialog)
        self.Mesh_groupBox.setObjectName(u"Mesh_groupBox")
        sizePolicy.setHeightForWidth(self.Mesh_groupBox.sizePolicy().hasHeightForWidth())
        self.Mesh_groupBox.setSizePolicy(sizePolicy)
        self.Mesh_groupBox.setMinimumSize(QSize(350, 100))
        self.Mesh_groupBox.setMaximumSize(QSize(350, 100))
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
        self.lineEdit.setMinimumSize(QSize(80, 20))
        self.lineEdit.setMaximumSize(QSize(80, 20))
        self.lineEdit.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.verticalLayout.addWidget(self.Mesh_groupBox)

        self.ESMS_groupBox = QGroupBox(SectPropCal_Dialog)
        self.ESMS_groupBox.setObjectName(u"ESMS_groupBox")
        self.ESMS_groupBox.setMinimumSize(QSize(350, 80))
        self.ESMS_groupBox.setMaximumSize(QSize(350, 80))
        self.gridLayout_2 = QGridLayout(self.ESMS_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setContentsMargins(25, 4, 4, 4)
        self.StrainatMaxiStress_radioButton = QRadioButton(self.ESMS_groupBox)
        self.StrainatMaxiStress_radioButton.setObjectName(u"StrainatMaxiStress_radioButton")
        self.StrainatMaxiStress_radioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.StrainatMaxiStress_radioButton, 0, 0, 1, 1)

        self.StrainatValue_radioButton = QRadioButton(self.ESMS_groupBox)
        self.StrainatValue_radioButton.setObjectName(u"StrainatValue_radioButton")
        self.StrainatValue_radioButton.setMinimumSize(QSize(200, 0))
        self.StrainatValue_radioButton.setMaximumSize(QSize(210, 16777215))

        self.gridLayout_2.addWidget(self.StrainatValue_radioButton, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.StrainValue_lineEdit = QLineEdit(self.ESMS_groupBox)
        self.StrainValue_lineEdit.setObjectName(u"StrainValue_lineEdit")
        sizePolicy.setHeightForWidth(self.StrainValue_lineEdit.sizePolicy().hasHeightForWidth())
        self.StrainValue_lineEdit.setSizePolicy(sizePolicy)
        self.StrainValue_lineEdit.setMinimumSize(QSize(80, 20))
        self.StrainValue_lineEdit.setMaximumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.StrainValue_lineEdit, 1, 2, 1, 1)

        self.verticalLayout.addWidget(self.ESMS_groupBox)

        self.groupBox_2 = QGroupBox(SectPropCal_Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(350, 30))
        self.groupBox_2.setMaximumSize(QSize(350, 30))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 4, 4, 4)
        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Run_pushButton = QPushButton(self.groupBox_2)
        self.Run_pushButton.setObjectName(u"Run_pushButton")
        sizePolicy.setHeightForWidth(self.Run_pushButton.sizePolicy().hasHeightForWidth())
        self.Run_pushButton.setSizePolicy(sizePolicy)
        self.Run_pushButton.setMinimumSize(QSize(75, 20))
        self.Run_pushButton.setMaximumSize(QSize(75, 20))

        self.horizontalLayout.addWidget(self.Run_pushButton)

        self.Cancel_pushButton = QPushButton(self.groupBox_2)
        self.Cancel_pushButton.setObjectName(u"Cancel_pushButton")
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setMinimumSize(QSize(75, 20))
        self.Cancel_pushButton.setMaximumSize(QSize(75, 20))

        self.horizontalLayout.addWidget(self.Cancel_pushButton)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 3)

        self.retranslateUi(SectPropCal_Dialog)

        QMetaObject.connectSlotsByName(SectPropCal_Dialog)

    # setupUi

    def retranslateUi(self, SectPropCal_Dialog):
        SectPropCal_Dialog.setWindowTitle(
            QCoreApplication.translate("SectPropCal_Dialog", u"Calculation of section properties", None))
        self.groupBox.setTitle(QCoreApplication.translate("SectPropCal_Dialog", u"Analysis Method", None))
        self.CM_radioButton.setText(QCoreApplication.translate("SectPropCal_Dialog", u"Coordinate Method", None))
        self.FE_radioButton.setText(QCoreApplication.translate("SectPropCal_Dialog", u"Finite-Element Method", None))
        self.Mat_groupBox.setTitle(
            QCoreApplication.translate("SectPropCal_Dialog", u"Equivalent Section Properties", None))
        self.EquivPR_lineEdit.setText(QCoreApplication.translate("SectPropCal_Dialog", u"0.3", None))
        self.EquivE_lineEdit.setText(QCoreApplication.translate("SectPropCal_Dialog", u"205000", None))
        self.UseDefValues_radioButton.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"Use Defined Values:", None))
        self.label_2.setText(QCoreApplication.translate("SectPropCal_Dialog", u"E (Equivalent Young's Modulus):", None))
        self.label_3.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"\u03bc (Equivalent Poisson 's Ratio):", None))
        self.label_4.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"fy (Equivalent Design Strength):", None))
        self.UseRefMat_radioButton.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"Use Reference Material ID:", None))
        self.EquivDesiStrs_lineEdit.setText(QCoreApplication.translate("SectPropCal_Dialog", u"355", None))
        self.Mesh_groupBox.setTitle(QCoreApplication.translate("SectPropCal_Dialog", u"Mesh Setting", None))
        self.MeshSize_radioButton.setText(QCoreApplication.translate("SectPropCal_Dialog", u"Mesh Size", None))
        self.UseExistingMesh_radioButton.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"Use the Existing Mesh", None))
        self.AutoMesh_radioButton.setText(QCoreApplication.translate("SectPropCal_Dialog", u"Auto Mesh ", None))
        self.ESMS_groupBox.setTitle(
            QCoreApplication.translate("SectPropCal_Dialog", u"Elastic Section Modulus Setting", None))
        self.StrainatMaxiStress_radioButton.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"Strain at the onset of Maximum Stress ", None))
        self.StrainatValue_radioButton.setText(
            QCoreApplication.translate("SectPropCal_Dialog", u"Strain at the Value of", None))
        self.StrainValue_lineEdit.setText(QCoreApplication.translate("SectPropCal_Dialog", u"0.001", None))
        self.groupBox_2.setTitle("")
        self.Run_pushButton.setText(QCoreApplication.translate("SectPropCal_Dialog", u"Run", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("SectPropCal_Dialog", u"Cancel", None))
