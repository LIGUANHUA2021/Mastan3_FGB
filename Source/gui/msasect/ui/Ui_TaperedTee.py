# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaperedTee.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_TaperedTee_Dialog(object):
    def setupUi(self, TaperedTee_Dialog):
        if not TaperedTee_Dialog.objectName():
            TaperedTee_Dialog.setObjectName(u"TaperedTee_Dialog")
        TaperedTee_Dialog.resize(540, 533)
        TaperedTee_Dialog.setMinimumSize(QSize(540, 529))
        TaperedTee_Dialog.setMaximumSize(QSize(540, 533))
        TaperedTee_Dialog.setStyleSheet(u"*{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(TaperedTee_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 2, 1, 2)
        self.label = QLabel(TaperedTee_Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"t3.jpg"))

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 0, -1)
        self.ModelingType_groupBox = QGroupBox(TaperedTee_Dialog)
        self.ModelingType_groupBox.setObjectName(u"ModelingType_groupBox")
        self.ModelingType_groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout = QVBoxLayout(self.ModelingType_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.Centerline_radioButton = QRadioButton(self.ModelingType_groupBox)
        self.Centerline_radioButton.setObjectName(u"Centerline_radioButton")

        self.verticalLayout.addWidget(self.Centerline_radioButton)

        self.Outline_radioButton = QRadioButton(self.ModelingType_groupBox)
        self.Outline_radioButton.setObjectName(u"Outline_radioButton")
        self.Outline_radioButton.setEnabled(False)

        self.verticalLayout.addWidget(self.Outline_radioButton)


        self.verticalLayout_2.addWidget(self.ModelingType_groupBox)

        self.Dimension_groupBox = QGroupBox(TaperedTee_Dialog)
        self.Dimension_groupBox.setObjectName(u"Dimension_groupBox")
        self.Dimension_groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout_3 = QVBoxLayout(self.Dimension_groupBox)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(4, 4, 6, 4)
        self.B_label = QLabel(self.Dimension_groupBox)
        self.B_label.setObjectName(u"B_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.B_label)

        self.B_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.B_inputlineEdit.setObjectName(u"B_inputlineEdit")
        self.B_inputlineEdit.setMinimumSize(QSize(78, 0))
        self.B_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.B_inputlineEdit)

        self.tw_label = QLabel(self.Dimension_groupBox)
        self.tw_label.setObjectName(u"tw_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.tw_label)

        self.D_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.D_inputlineEdit.setObjectName(u"D_inputlineEdit")
        self.D_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.D_inputlineEdit)

        self.label_2 = QLabel(self.Dimension_groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.tf_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tf_lineEdit.setObjectName(u"tf_lineEdit")
        self.tf_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.tf_lineEdit)

        self.label_3 = QLabel(self.Dimension_groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.tw1_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tw1_lineEdit.setObjectName(u"tw1_lineEdit")
        self.tw1_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tw1_lineEdit)

        self.label_4 = QLabel(self.Dimension_groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.tw2_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tw2_lineEdit.setObjectName(u"tw2_lineEdit")
        self.tw2_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.tw2_lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.Dimension_groupBox)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.TaperedTee_groupBox = QGroupBox(TaperedTee_Dialog)
        self.TaperedTee_groupBox.setObjectName(u"TaperedTee_groupBox")
        self.TaperedTee_groupBox.setMinimumSize(QSize(0, 80))
        self.TaperedTee_groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.gridLayout_2 = QGridLayout(self.TaperedTee_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 4, 9, 4)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(2, 2, 2, 4)
        self.G_label = QLabel(self.TaperedTee_groupBox)
        self.G_label.setObjectName(u"G_label")

        self.gridLayout.addWidget(self.G_label, 0, 4, 1, 1)

        self.ID_label = QLabel(self.TaperedTee_groupBox)
        self.ID_label.setObjectName(u"ID_label")

        self.gridLayout.addWidget(self.ID_label, 0, 0, 1, 1)

        self.E_label = QLabel(self.TaperedTee_groupBox)
        self.E_label.setObjectName(u"E_label")

        self.gridLayout.addWidget(self.E_label, 0, 2, 1, 1)

        self.fy_label = QLabel(self.TaperedTee_groupBox)
        self.fy_label.setObjectName(u"fy_label")

        self.gridLayout.addWidget(self.fy_label, 1, 2, 1, 1)

        self.Color_label = QLabel(self.TaperedTee_groupBox)
        self.Color_label.setObjectName(u"Color_label")

        self.gridLayout.addWidget(self.Color_label, 1, 0, 1, 1)

        self.eu_inputlineEdit = QLineEdit(self.TaperedTee_groupBox)
        self.eu_inputlineEdit.setObjectName(u"eu_inputlineEdit")
        self.eu_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.eu_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.eu_inputlineEdit, 1, 5, 1, 1)

        self.fy_inputlineEdit = QLineEdit(self.TaperedTee_groupBox)
        self.fy_inputlineEdit.setObjectName(u"fy_inputlineEdit")
        self.fy_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.fy_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.fy_inputlineEdit, 1, 3, 1, 1)

        self.eu_label = QLabel(self.TaperedTee_groupBox)
        self.eu_label.setObjectName(u"eu_label")

        self.gridLayout.addWidget(self.eu_label, 1, 4, 1, 1)

        self.G_inputlineEdit = QLineEdit(self.TaperedTee_groupBox)
        self.G_inputlineEdit.setObjectName(u"G_inputlineEdit")
        self.G_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.G_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.G_inputlineEdit, 1, 1, 1, 1)

        self.E_inputlineEdit = QLineEdit(self.TaperedTee_groupBox)
        self.E_inputlineEdit.setObjectName(u"E_inputlineEdit")
        self.E_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.E_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.E_inputlineEdit, 0, 5, 1, 1)

        self.ID_inputlineEdit = QLineEdit(self.TaperedTee_groupBox)
        self.ID_inputlineEdit.setObjectName(u"ID_inputlineEdit")
        self.ID_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.ID_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ID_inputlineEdit, 0, 3, 1, 1)

        self.ColorButton = QPushButton(self.TaperedTee_groupBox)
        self.ColorButton.setObjectName(u"ColorButton")
        self.ColorButton.setMinimumSize(QSize(0, 19))
        self.ColorButton.setStyleSheet(u"*{	\n"
"	border:1px solid rgb(0,0,0);\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(170, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ColorButton, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.TaperedTee_groupBox, 0, 0, 1, 1)

        self.button_GroupBox = QGroupBox(TaperedTee_Dialog)
        self.button_GroupBox.setObjectName(u"button_GroupBox")
        self.button_GroupBox.setMinimumSize(QSize(0, 0))
        self.button_GroupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.horizontalLayout_3 = QHBoxLayout(self.button_GroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 2, 2, 2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.OK_button = QPushButton(self.button_GroupBox)
        self.OK_button.setObjectName(u"OK_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OK_button.sizePolicy().hasHeightForWidth())
        self.OK_button.setSizePolicy(sizePolicy)
        self.OK_button.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.OK_button)

        self.Cancel_pushButton = QPushButton(self.button_GroupBox)
        self.Cancel_pushButton.setObjectName(u"Cancel_pushButton")
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.Cancel_pushButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addWidget(self.button_GroupBox, 3, 0, 1, 1)

        QWidget.setTabOrder(self.ID_inputlineEdit, self.E_inputlineEdit)
        QWidget.setTabOrder(self.E_inputlineEdit, self.G_inputlineEdit)
        QWidget.setTabOrder(self.G_inputlineEdit, self.fy_inputlineEdit)
        QWidget.setTabOrder(self.fy_inputlineEdit, self.eu_inputlineEdit)
        QWidget.setTabOrder(self.eu_inputlineEdit, self.Centerline_radioButton)
        QWidget.setTabOrder(self.Centerline_radioButton, self.Outline_radioButton)
        QWidget.setTabOrder(self.Outline_radioButton, self.B_inputlineEdit)
        QWidget.setTabOrder(self.B_inputlineEdit, self.D_inputlineEdit)
        QWidget.setTabOrder(self.D_inputlineEdit, self.tf_lineEdit)
        QWidget.setTabOrder(self.tf_lineEdit, self.tw1_lineEdit)
        QWidget.setTabOrder(self.tw1_lineEdit, self.tw2_lineEdit)
        QWidget.setTabOrder(self.tw2_lineEdit, self.ColorButton)
        QWidget.setTabOrder(self.ColorButton, self.OK_button)
        QWidget.setTabOrder(self.OK_button, self.Cancel_pushButton)

        self.retranslateUi(TaperedTee_Dialog)

        QMetaObject.connectSlotsByName(TaperedTee_Dialog)
    # setupUi

    def retranslateUi(self, TaperedTee_Dialog):
        TaperedTee_Dialog.setWindowTitle(QCoreApplication.translate("TaperedTee_Dialog", u"Tapered Tee - Template", None))
        self.label.setText("")
        self.ModelingType_groupBox.setTitle(QCoreApplication.translate("TaperedTee_Dialog", u"Modeling Type", None))
        self.Centerline_radioButton.setText(QCoreApplication.translate("TaperedTee_Dialog", u"Centerline", None))
        self.Outline_radioButton.setText(QCoreApplication.translate("TaperedTee_Dialog", u"Outline", None))
        self.Dimension_groupBox.setTitle(QCoreApplication.translate("TaperedTee_Dialog", u"Dimension", None))
        self.B_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"B = ", None))
        self.tw_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"D = ", None))
        self.label_2.setText(QCoreApplication.translate("TaperedTee_Dialog", u"tf = ", None))
        self.label_3.setText(QCoreApplication.translate("TaperedTee_Dialog", u"tw1 = ", None))
        self.label_4.setText(QCoreApplication.translate("TaperedTee_Dialog", u"tw2 = ", None))
        self.TaperedTee_groupBox.setTitle(QCoreApplication.translate("TaperedTee_Dialog", u"Material", None))
        self.G_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u" E  = ", None))
        self.ID_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"Color = ", None))
        self.E_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"ID = ", None))
        self.fy_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"fy  = ", None))
        self.Color_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"     \u03bc   = ", None))
        self.eu_label.setText(QCoreApplication.translate("TaperedTee_Dialog", u"eu = ", None))
        self.ColorButton.setText("")
        self.OK_button.setText(QCoreApplication.translate("TaperedTee_Dialog", u"OK", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("TaperedTee_Dialog", u"Cancel", None))
    # retranslateUi

