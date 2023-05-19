# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnalStressAnalysis.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
                               QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

class Ui_StressAnal_Dialog(object):
    def setupUi(self, StressAnal_Dialog):
        if not StressAnal_Dialog.objectName():
            StressAnal_Dialog.setObjectName(u"StressAnal_Dialog")
        StressAnal_Dialog.resize(330, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StressAnal_Dialog.sizePolicy().hasHeightForWidth())
        StressAnal_Dialog.setSizePolicy(sizePolicy)
        StressAnal_Dialog.setMinimumSize(QSize(330, 320))
        StressAnal_Dialog.setMaximumSize(QSize(330, 320))
        StressAnal_Dialog.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
                                        "font: 9pt \"Segoe UI\";\n"
                                        "background-color: rgb(43, 43, 43);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border: 1 px solid;\n"
                                        "	border-radius: 3px;\n"
                                        "}\n"
                                        "QPushButton::hover\n"
                                        "{\n"
                                        "	background-color: rgb(144, 200, 246);\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    padding-left: 3px;\n"
                                        "    padding-top: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border: 1 px solid;\n"
                                        "	border-radius: 3px;\n"
                                        "}\n"
                                        "QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
                                        "\n"
                                        "")
        StressAnal_Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(StressAnal_Dialog)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.groupBox_9 = QGroupBox(StressAnal_Dialog)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 49))
        self.groupBox_9.setMaximumSize(QSize(16777215, 49))
        self.groupBox_9.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(25, 4, 4, 6)
        self.PrinAxis_radioButton = QRadioButton(self.groupBox_9)
        self.PrinAxis_radioButton.setObjectName(u"PrinAxis_radioButton")
        self.PrinAxis_radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.PrinAxis_radioButton)

        self.GeoAxis_radioButton = QRadioButton(self.groupBox_9)
        self.GeoAxis_radioButton.setObjectName(u"GeoAxis_radioButton")

        self.horizontalLayout_3.addWidget(self.GeoAxis_radioButton)

        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_7 = QGroupBox(StressAnal_Dialog)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 110))
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_7.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.gridLayout = QGridLayout(self.groupBox_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(25, 4, 4, 6)
        self.Compression_radioButton2 = QRadioButton(self.groupBox_7)
        self.Compression_radioButton2.setObjectName(u"Compression_radioButton2")

        self.gridLayout.addWidget(self.Compression_radioButton2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.Compression_radioButton1 = QRadioButton(self.groupBox_7)
        self.Compression_radioButton1.setObjectName(u"Compression_radioButton1")

        self.gridLayout.addWidget(self.Compression_radioButton1, 0, 0, 1, 1)

        self.EquiE_lineEdit = QLineEdit(self.groupBox_7)
        self.EquiE_lineEdit.setObjectName(u"EquiE_lineEdit")
        self.EquiE_lineEdit.setMinimumSize(QSize(0, 20))
        self.EquiE_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.EquiE_lineEdit.setStyleSheet(u"*{	\n"
                                          "	font: 9pt \"Segoe UI\";\n"
                                          "	color: rgb(0, 0, 0);\n"
                                          "	background: rgb(255, 255, 255);\n"
                                          "}")

        self.gridLayout.addWidget(self.EquiE_lineEdit, 2, 1, 1, 1)

        self.EquivPR_lineEdit = QLineEdit(self.groupBox_7)
        self.EquivPR_lineEdit.setObjectName(u"EquivPR_lineEdit")
        self.EquivPR_lineEdit.setMinimumSize(QSize(0, 20))
        self.EquivPR_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.EquivPR_lineEdit.setStyleSheet(u"*{	\n"
                                            "	font: 9pt \"Segoe UI\";\n"
                                            "	color: rgb(0, 0, 0);\n"
                                            "	background: rgb(255, 255, 255);\n"
                                            "}")

        self.gridLayout.addWidget(self.EquivPR_lineEdit, 3, 1, 1, 1)

        self.Equify_lineEdit = QLineEdit(self.groupBox_7)
        self.Equify_lineEdit.setObjectName(u"Equify_lineEdit")
        self.Equify_lineEdit.setMinimumSize(QSize(0, 20))
        self.Equify_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.Equify_lineEdit.setStyleSheet(u"*{	\n"
                                           "	font: 9pt \"Segoe UI\";\n"
                                           "	color: rgb(0, 0, 0);\n"
                                           "	background: rgb(255, 255, 255);\n"
                                           "}")

        self.gridLayout.addWidget(self.Equify_lineEdit, 4, 1, 1, 1)

        self.RefMat_comboBox = QComboBox(self.groupBox_7)
        self.RefMat_comboBox.setObjectName(u"RefMat_comboBox")
        self.RefMat_comboBox.setStyleSheet(u"*{	\n"
                                           "	font: 9pt \"Segoe UI\";\n"
                                           "	color: rgb(0, 0, 0);\n"
                                           "	background: rgb(255, 255, 255);\n"
                                           "}")

        self.gridLayout.addWidget(self.RefMat_comboBox, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_3 = QGroupBox(StressAnal_Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(25, 4, 4, 6)
        self.Mz_lineEdit = QLineEdit(self.groupBox_3)
        self.Mz_lineEdit.setObjectName(u"Mz_lineEdit")
        self.Mz_lineEdit.setMinimumSize(QSize(50, 0))
        self.Mz_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.Mz_lineEdit.setStyleSheet(u"*{	\n"
                                       "	font: 9pt \"Segoe UI\";\n"
                                       "	color: rgb(0, 0, 0);\n"
                                       "	background: rgb(255, 255, 255);\n"
                                       "}")

        self.gridLayout_2.addWidget(self.Mz_lineEdit, 1, 4, 1, 1)

        self.Px_label = QLabel(self.groupBox_3)
        self.Px_label.setObjectName(u"Px_label")

        self.gridLayout_2.addWidget(self.Px_label, 0, 0, 1, 1)

        self.Mz_label = QLabel(self.groupBox_3)
        self.Mz_label.setObjectName(u"Mz_label")

        self.gridLayout_2.addWidget(self.Mz_label, 1, 3, 1, 1)

        self.Px_lineEdit = QLineEdit(self.groupBox_3)
        self.Px_lineEdit.setObjectName(u"Px_lineEdit")
        self.Px_lineEdit.setMinimumSize(QSize(50, 0))
        self.Px_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.Px_lineEdit.setStyleSheet(u"*{	\n"
                                       "	font: 9pt \"Segoe UI\";\n"
                                       "	color: rgb(0, 0, 0);\n"
                                       "	background: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "")

        self.gridLayout_2.addWidget(self.Px_lineEdit, 0, 1, 1, 1)

        self.B_label = QLabel(self.groupBox_3)
        self.B_label.setObjectName(u"B_label")

        self.gridLayout_2.addWidget(self.B_label, 0, 3, 1, 1)

        self.My_label = QLabel(self.groupBox_3)
        self.My_label.setObjectName(u"My_label")

        self.gridLayout_2.addWidget(self.My_label, 1, 0, 1, 1)

        self.My_lineEdit = QLineEdit(self.groupBox_3)
        self.My_lineEdit.setObjectName(u"My_lineEdit")
        self.My_lineEdit.setMinimumSize(QSize(50, 0))
        self.My_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.My_lineEdit.setStyleSheet(u"*{	\n"
                                       "	font: 9pt \"Segoe UI\";\n"
                                       "	color: rgb(0, 0, 0);\n"
                                       "	background: rgb(255, 255, 255);\n"
                                       "}")

        self.gridLayout_2.addWidget(self.My_lineEdit, 1, 1, 1, 1)

        self.B_lineEdit = QLineEdit(self.groupBox_3)
        self.B_lineEdit.setObjectName(u"B_lineEdit")
        self.B_lineEdit.setMinimumSize(QSize(50, 0))
        self.B_lineEdit.setMaximumSize(QSize(16777215, 21))
        self.B_lineEdit.setStyleSheet(u"*{	\n"
                                      "	font: 9pt \"Segoe UI\";\n"
                                      "	color: rgb(0, 0, 0);\n"
                                      "	background: rgb(255, 255, 255);\n"
                                      "}")

        self.gridLayout_2.addWidget(self.B_lineEdit, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(StressAnal_Dialog)
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
        self.ShowResults_pushButton = QPushButton(self.groupBox)
        self.ShowResults_pushButton.setObjectName(u"ShowResults_pushButton")
        self.ShowResults_pushButton.setMinimumSize(QSize(85, 24))
        self.ShowResults_pushButton.setMaximumSize(QSize(85, 24))
        self.ShowResults_pushButton.setStyleSheet(u"*{	\n"
                                                  "	font: 9pt \"Segoe UI\";\n"
                                                  "	color: rgb(0, 0, 0);\n"
                                                  "	background: rgb(255, 255, 255);\n"
                                                  "}\n"
                                                  "QPushButton::disabled{color:rgb(153, 153, 153)}\n"
                                                  "QPushButton{	\n"
                                                  "	font: 9pt \"Segoe UI\";\n"
                                                  "	color: rgb(0, 0, 0);\n"
                                                  "	background: rgb(255, 255, 255);\n"
                                                  "}")

        self.horizontalLayout.addWidget(self.ShowResults_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Run_pushButton = QPushButton(self.groupBox)
        self.Run_pushButton.setObjectName(u"Run_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Run_pushButton.sizePolicy().hasHeightForWidth())
        self.Run_pushButton.setSizePolicy(sizePolicy1)
        self.Run_pushButton.setMinimumSize(QSize(75, 24))
        self.Run_pushButton.setMaximumSize(QSize(75, 24))
        self.Run_pushButton.setStyleSheet(u"*{	\n"
                                          "	font: 9pt \"Segoe UI\";\n"
                                          "	color: rgb(0, 0, 0);\n"
                                          "	background: rgb(255, 255, 255);\n"
                                          "}")

        self.horizontalLayout.addWidget(self.Run_pushButton)

        self.Cancel_pushButton = QPushButton(self.groupBox)
        self.Cancel_pushButton.setObjectName(u"Cancel_pushButton")
        sizePolicy1.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy1)
        self.Cancel_pushButton.setMinimumSize(QSize(75, 24))
        self.Cancel_pushButton.setMaximumSize(QSize(75, 24))
        self.Cancel_pushButton.setStyleSheet(u"*{	\n"
                                             "	font: 9pt \"Segoe UI\";\n"
                                             "	color: rgb(0, 0, 0);\n"
                                             "	background: rgb(255, 255, 255);\n"
                                             "}")

        self.horizontalLayout.addWidget(self.Cancel_pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addWidget(self.groupBox)

        QWidget.setTabOrder(self.PrinAxis_radioButton, self.GeoAxis_radioButton)
        QWidget.setTabOrder(self.GeoAxis_radioButton, self.Compression_radioButton1)
        QWidget.setTabOrder(self.Compression_radioButton1, self.Compression_radioButton2)
        QWidget.setTabOrder(self.Compression_radioButton2, self.Run_pushButton)
        QWidget.setTabOrder(self.Run_pushButton, self.ShowResults_pushButton)
        QWidget.setTabOrder(self.ShowResults_pushButton, self.Cancel_pushButton)

        self.retranslateUi(StressAnal_Dialog)

        QMetaObject.connectSlotsByName(StressAnal_Dialog)

    # setupUi

    def retranslateUi(self, StressAnal_Dialog):
        StressAnal_Dialog.setWindowTitle(
            QCoreApplication.translate("StressAnal_Dialog", u"Caculation of Stress (Under developing)",
                                       None))
        self.groupBox_9.setTitle(QCoreApplication.translate("StressAnal_Dialog", u"Axis Settings", None))
        self.PrinAxis_radioButton.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"Principal axis", None))
        self.GeoAxis_radioButton.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"Geometric axis", None))
        self.groupBox_7.setTitle(
            QCoreApplication.translate("StressAnal_Dialog", u"Equivalent Section Properties", None))
        self.Compression_radioButton2.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"Use defined values:", None))
        self.label_6.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"\u03bc (Equivalent Poisson 's ratio):", None))
        self.label_5.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"E (Equivalent elastic modulus ):", None))
        self.label_7.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"fy (Equivalent design strength):", None))
        self.Compression_radioButton1.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"Use reference material ID:", None))
        self.groupBox_3.setTitle(
            QCoreApplication.translate("StressAnal_Dialog", u"Compression and Bending", None))
        self.Px_label.setText(QCoreApplication.translate("StressAnal_Dialog", u"Px:", None))
        self.Mz_label.setText(QCoreApplication.translate("StressAnal_Dialog", u"Mz:", None))
        self.B_label.setText(QCoreApplication.translate("StressAnal_Dialog", u"B:", None))
        self.My_label.setText(QCoreApplication.translate("StressAnal_Dialog", u"My:", None))
        self.groupBox.setTitle("")
        self.ShowResults_pushButton.setText(
            QCoreApplication.translate("StressAnal_Dialog", u"Show Results", None))
        self.Run_pushButton.setText(QCoreApplication.translate("StressAnal_Dialog", u"Run", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("StressAnal_Dialog", u"Cancel", None))
