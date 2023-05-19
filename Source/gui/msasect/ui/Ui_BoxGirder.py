# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BoxGirder.ui'
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

class Ui_BoxGirder_Dialog(object):
    def setupUi(self, BoxGirder_Dialog):
        if not BoxGirder_Dialog.objectName():
            BoxGirder_Dialog.setObjectName(u"BoxGirder_Dialog")
        BoxGirder_Dialog.resize(540, 533)
        BoxGirder_Dialog.setMinimumSize(QSize(540, 529))
        BoxGirder_Dialog.setMaximumSize(QSize(540, 533))
        BoxGirder_Dialog.setStyleSheet(u"*{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(BoxGirder_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 2, 1, 2)
        self.label = QLabel(BoxGirder_Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"t3.jpg"))

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 0, -1)
        self.ModelingType_groupBox = QGroupBox(BoxGirder_Dialog)
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

        self.Dimension_groupBox = QGroupBox(BoxGirder_Dialog)
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

        self.B1_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.B1_inputlineEdit.setObjectName(u"B1_inputlineEdit")
        self.B1_inputlineEdit.setMinimumSize(QSize(78, 0))
        self.B1_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.B1_inputlineEdit)

        self.tw_label = QLabel(self.Dimension_groupBox)
        self.tw_label.setObjectName(u"tw_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.tw_label)

        self.B2_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.B2_inputlineEdit.setObjectName(u"B2_inputlineEdit")
        self.B2_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.B2_inputlineEdit)

        self.D1_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.D1_lineEdit.setObjectName(u"D1_lineEdit")
        self.D1_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.D1_lineEdit)

        self.D2_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.D2_lineEdit.setObjectName(u"D2_lineEdit")
        self.D2_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.D2_lineEdit)

        self.tf_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tf_lineEdit.setObjectName(u"tf_lineEdit")
        self.tf_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.tf_lineEdit)

        self.tw1_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tw1_lineEdit.setObjectName(u"tw1_lineEdit")
        self.tw1_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.tw1_lineEdit)

        self.tw2_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tw2_lineEdit.setObjectName(u"tw2_lineEdit")
        self.tw2_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.tw2_lineEdit)

        self.tw3_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.tw3_lineEdit.setObjectName(u"tw3_lineEdit")
        self.tw3_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.tw3_lineEdit)

        self.label_2 = QLabel(self.Dimension_groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.Dimension_groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.Dimension_groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.Dimension_groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.Dimension_groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.Dimension_groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.D3_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.D3_lineEdit.setObjectName(u"D3_lineEdit")
        self.D3_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.D3_lineEdit)

        self.D4_lineEdit = QLineEdit(self.Dimension_groupBox)
        self.D4_lineEdit.setObjectName(u"D4_lineEdit")
        self.D4_lineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.D4_lineEdit)

        self.label_8 = QLabel(self.Dimension_groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.Dimension_groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(10, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(10, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.Dimension_groupBox)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.IShape_groupBox = QGroupBox(BoxGirder_Dialog)
        self.IShape_groupBox.setObjectName(u"IShape_groupBox")
        self.IShape_groupBox.setMinimumSize(QSize(0, 80))
        self.IShape_groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.gridLayout_2 = QGridLayout(self.IShape_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setContentsMargins(9, 4, 9, 6)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(2, 2, 2, 4)
        self.G_label = QLabel(self.IShape_groupBox)
        self.G_label.setObjectName(u"G_label")

        self.gridLayout.addWidget(self.G_label, 0, 4, 1, 1)

        self.ID_label = QLabel(self.IShape_groupBox)
        self.ID_label.setObjectName(u"ID_label")

        self.gridLayout.addWidget(self.ID_label, 0, 0, 1, 1)

        self.E_label = QLabel(self.IShape_groupBox)
        self.E_label.setObjectName(u"E_label")

        self.gridLayout.addWidget(self.E_label, 0, 2, 1, 1)

        self.fy_label = QLabel(self.IShape_groupBox)
        self.fy_label.setObjectName(u"fy_label")

        self.gridLayout.addWidget(self.fy_label, 1, 2, 1, 1)

        self.Color_label = QLabel(self.IShape_groupBox)
        self.Color_label.setObjectName(u"Color_label")

        self.gridLayout.addWidget(self.Color_label, 1, 0, 1, 1)

        self.eu_inputlineEdit = QLineEdit(self.IShape_groupBox)
        self.eu_inputlineEdit.setObjectName(u"eu_inputlineEdit")
        self.eu_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.eu_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.eu_inputlineEdit, 1, 5, 1, 1)

        self.fy_inputlineEdit = QLineEdit(self.IShape_groupBox)
        self.fy_inputlineEdit.setObjectName(u"fy_inputlineEdit")
        self.fy_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.fy_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.fy_inputlineEdit, 1, 3, 1, 1)

        self.eu_label = QLabel(self.IShape_groupBox)
        self.eu_label.setObjectName(u"eu_label")

        self.gridLayout.addWidget(self.eu_label, 1, 4, 1, 1)

        self.G_inputlineEdit = QLineEdit(self.IShape_groupBox)
        self.G_inputlineEdit.setObjectName(u"G_inputlineEdit")
        self.G_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.G_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.G_inputlineEdit, 1, 1, 1, 1)

        self.E_inputlineEdit = QLineEdit(self.IShape_groupBox)
        self.E_inputlineEdit.setObjectName(u"E_inputlineEdit")
        self.E_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.E_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.E_inputlineEdit, 0, 5, 1, 1)

        self.ID_inputlineEdit = QLineEdit(self.IShape_groupBox)
        self.ID_inputlineEdit.setObjectName(u"ID_inputlineEdit")
        self.ID_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.ID_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ID_inputlineEdit, 0, 3, 1, 1)

        self.ColorButton = QPushButton(self.IShape_groupBox)
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


        self.gridLayout_3.addWidget(self.IShape_groupBox, 0, 0, 1, 1)

        self.button_GroupBox = QGroupBox(BoxGirder_Dialog)
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
        self.OK_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OK_button.sizePolicy().hasHeightForWidth())
        self.OK_button.setSizePolicy(sizePolicy)
        self.OK_button.setStyleSheet(u"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{	\n"
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
        self.Cancel_pushButton.setStyleSheet(u"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.Cancel_pushButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addWidget(self.button_GroupBox, 3, 0, 1, 1)

        QWidget.setTabOrder(self.ID_inputlineEdit, self.E_inputlineEdit)
        QWidget.setTabOrder(self.E_inputlineEdit, self.G_inputlineEdit)
        QWidget.setTabOrder(self.G_inputlineEdit, self.fy_inputlineEdit)
        QWidget.setTabOrder(self.fy_inputlineEdit, self.eu_inputlineEdit)
        QWidget.setTabOrder(self.eu_inputlineEdit, self.Centerline_radioButton)
        QWidget.setTabOrder(self.Centerline_radioButton, self.Outline_radioButton)
        QWidget.setTabOrder(self.Outline_radioButton, self.B1_inputlineEdit)
        QWidget.setTabOrder(self.B1_inputlineEdit, self.B2_inputlineEdit)
        QWidget.setTabOrder(self.B2_inputlineEdit, self.D1_lineEdit)
        QWidget.setTabOrder(self.D1_lineEdit, self.D2_lineEdit)
        QWidget.setTabOrder(self.D2_lineEdit, self.D3_lineEdit)
        QWidget.setTabOrder(self.D3_lineEdit, self.D4_lineEdit)
        QWidget.setTabOrder(self.D4_lineEdit, self.tf_lineEdit)
        QWidget.setTabOrder(self.tf_lineEdit, self.tw1_lineEdit)
        QWidget.setTabOrder(self.tw1_lineEdit, self.tw2_lineEdit)
        QWidget.setTabOrder(self.tw2_lineEdit, self.tw3_lineEdit)
        QWidget.setTabOrder(self.tw3_lineEdit, self.ColorButton)
        QWidget.setTabOrder(self.ColorButton, self.OK_button)
        QWidget.setTabOrder(self.OK_button, self.Cancel_pushButton)

        self.retranslateUi(BoxGirder_Dialog)

        QMetaObject.connectSlotsByName(BoxGirder_Dialog)
    # setupUi

    def retranslateUi(self, BoxGirder_Dialog):
        BoxGirder_Dialog.setWindowTitle(QCoreApplication.translate("BoxGirder_Dialog", u"Box Girder - Template", None))
        self.label.setText("")
        self.ModelingType_groupBox.setTitle(QCoreApplication.translate("BoxGirder_Dialog", u"Modeling Type", None))
        self.Centerline_radioButton.setText(QCoreApplication.translate("BoxGirder_Dialog", u"Centerline", None))
        self.Outline_radioButton.setText(QCoreApplication.translate("BoxGirder_Dialog", u"Outline", None))
        self.Dimension_groupBox.setTitle(QCoreApplication.translate("BoxGirder_Dialog", u"Dimension", None))
        self.B_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"B1 = ", None))
        self.tw_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"B2 = ", None))
        self.label_2.setText(QCoreApplication.translate("BoxGirder_Dialog", u"D1 = ", None))
        self.label_3.setText(QCoreApplication.translate("BoxGirder_Dialog", u"D2 = ", None))
        self.label_4.setText(QCoreApplication.translate("BoxGirder_Dialog", u"tf = ", None))
        self.label_5.setText(QCoreApplication.translate("BoxGirder_Dialog", u"tw1 = ", None))
        self.label_6.setText(QCoreApplication.translate("BoxGirder_Dialog", u"tw2 = ", None))
        self.label_7.setText(QCoreApplication.translate("BoxGirder_Dialog", u"tw3 = ", None))
        self.label_8.setText(QCoreApplication.translate("BoxGirder_Dialog", u"D3 =", None))
        self.label_9.setText(QCoreApplication.translate("BoxGirder_Dialog", u"D4 = ", None))
        self.IShape_groupBox.setTitle(QCoreApplication.translate("BoxGirder_Dialog", u"Material", None))
        self.G_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u" E  = ", None))
        self.ID_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"Color = ", None))
        self.E_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"ID = ", None))
        self.fy_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"fy  = ", None))
        self.Color_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"     \u03bc   = ", None))
        self.eu_label.setText(QCoreApplication.translate("BoxGirder_Dialog", u"eu = ", None))
        self.ColorButton.setText("")
        self.OK_button.setText(QCoreApplication.translate("BoxGirder_Dialog", u"OK", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("BoxGirder_Dialog", u"Cancel", None))
    # retranslateUi

