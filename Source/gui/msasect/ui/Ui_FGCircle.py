# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FGCircle.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FGCircle_Dialog(object):
    def setupUi(self, FGCircle_Dialog):
        if not FGCircle_Dialog.objectName():
            FGCircle_Dialog.setObjectName(u"FGCircle_Dialog")
        FGCircle_Dialog.resize(540, 555)
        FGCircle_Dialog.setMinimumSize(QSize(540, 555))
        FGCircle_Dialog.setMaximumSize(QSize(540, 555))
        FGCircle_Dialog.setStyleSheet(u"*{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(FGCircle_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 2, 1, 2)
        self.label = QLabel(FGCircle_Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"t3.jpg"))

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 0, -1)
        self.ModelingType_groupBox = QGroupBox(FGCircle_Dialog)
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

        self.Dimension_groupBox = QGroupBox(FGCircle_Dialog)
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

        self.Ri_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.Ri_inputlineEdit.setObjectName(u"Ri_inputlineEdit")
        self.Ri_inputlineEdit.setMinimumSize(QSize(78, 0))
        self.Ri_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Ri_inputlineEdit)

        self.tw_label = QLabel(self.Dimension_groupBox)
        self.tw_label.setObjectName(u"tw_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.tw_label)

        self.R0_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.R0_inputlineEdit.setObjectName(u"R0_inputlineEdit")
        self.R0_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.R0_inputlineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.Dimension_groupBox)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.FGCircle_groupBox = QGroupBox(FGCircle_Dialog)
        self.FGCircle_groupBox.setObjectName(u"FGCircle_groupBox")
        self.FGCircle_groupBox.setMinimumSize(QSize(0, 80))
        self.FGCircle_groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.gridLayout_2 = QGridLayout(self.FGCircle_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setContentsMargins(0, 0, 0, 4)
        self.label_3 = QLabel(self.FGCircle_groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.Color_label = QLabel(self.FGCircle_groupBox)
        self.Color_label.setObjectName(u"Color_label")

        self.gridLayout.addWidget(self.Color_label, 2, 0, 1, 1)

        self.Law_comboBox = QComboBox(self.FGCircle_groupBox)
        self.Law_comboBox.addItem("")
        self.Law_comboBox.addItem("")
        self.Law_comboBox.addItem("")
        self.Law_comboBox.setObjectName(u"Law_comboBox")
        self.Law_comboBox.setMinimumSize(QSize(110, 0))
        self.Law_comboBox.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.Law_comboBox, 0, 1, 1, 1)

        self.G_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.G_inputlineEdit.setObjectName(u"G_inputlineEdit")
        self.G_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.G_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.G_inputlineEdit, 2, 1, 1, 1)

        self.eu_label = QLabel(self.FGCircle_groupBox)
        self.eu_label.setObjectName(u"eu_label")

        self.gridLayout.addWidget(self.eu_label, 0, 4, 1, 1)

        self.eu_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.eu_inputlineEdit.setObjectName(u"eu_inputlineEdit")
        self.eu_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.eu_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.eu_inputlineEdit, 0, 5, 1, 1)

        self.E_label = QLabel(self.FGCircle_groupBox)
        self.E_label.setObjectName(u"E_label")

        self.gridLayout.addWidget(self.E_label, 1, 0, 1, 1)

        self.Ei_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.Ei_inputlineEdit.setObjectName(u"Ei_inputlineEdit")
        self.Ei_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.Ei_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.Ei_inputlineEdit, 1, 1, 1, 1)

        self.G_label = QLabel(self.FGCircle_groupBox)
        self.G_label.setObjectName(u"G_label")

        self.gridLayout.addWidget(self.G_label, 1, 2, 1, 1)

        self.E0_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.E0_inputlineEdit.setObjectName(u"E0_inputlineEdit")
        self.E0_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.E0_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.E0_inputlineEdit, 1, 3, 1, 1)

        self.fy_label = QLabel(self.FGCircle_groupBox)
        self.fy_label.setObjectName(u"fy_label")

        self.gridLayout.addWidget(self.fy_label, 1, 4, 1, 1)

        self.fy_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.fy_inputlineEdit.setObjectName(u"fy_inputlineEdit")
        self.fy_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.fy_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.fy_inputlineEdit, 1, 5, 1, 1)

        self.label_2 = QLabel(self.FGCircle_groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_4 = QLabel(self.FGCircle_groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.Num_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.Num_inputlineEdit.setObjectName(u"Num_inputlineEdit")
        self.Num_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.Num_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.Num_inputlineEdit, 0, 3, 1, 1)

        self.k_inputlineEdit = QLineEdit(self.FGCircle_groupBox)
        self.k_inputlineEdit.setObjectName(u"k_inputlineEdit")
        self.k_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.k_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.k_inputlineEdit, 2, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.FGCircle_groupBox, 0, 0, 1, 1)

        self.button_GroupBox = QGroupBox(FGCircle_Dialog)
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

        QWidget.setTabOrder(self.Law_comboBox, self.eu_inputlineEdit)
        QWidget.setTabOrder(self.eu_inputlineEdit, self.G_inputlineEdit)
        QWidget.setTabOrder(self.G_inputlineEdit, self.Centerline_radioButton)
        QWidget.setTabOrder(self.Centerline_radioButton, self.Outline_radioButton)
        QWidget.setTabOrder(self.Outline_radioButton, self.Ri_inputlineEdit)
        QWidget.setTabOrder(self.Ri_inputlineEdit, self.R0_inputlineEdit)
        QWidget.setTabOrder(self.R0_inputlineEdit, self.OK_button)
        QWidget.setTabOrder(self.OK_button, self.Cancel_pushButton)

        self.retranslateUi(FGCircle_Dialog)

        QMetaObject.connectSlotsByName(FGCircle_Dialog)
    # setupUi

    def retranslateUi(self, FGCircle_Dialog):
        FGCircle_Dialog.setWindowTitle(QCoreApplication.translate("FGCircle_Dialog", u"Functionally Graded Circular Hollow Section - Template", None))
        self.label.setText("")
        self.ModelingType_groupBox.setTitle(QCoreApplication.translate("FGCircle_Dialog", u"Modeling Type", None))
        self.Centerline_radioButton.setText(QCoreApplication.translate("FGCircle_Dialog", u"Centerline", None))
        self.Outline_radioButton.setText(QCoreApplication.translate("FGCircle_Dialog", u"Outline", None))
        self.Dimension_groupBox.setTitle(QCoreApplication.translate("FGCircle_Dialog", u"Dimension", None))
        self.B_label.setText(QCoreApplication.translate("FGCircle_Dialog", u"Ri = ", None))
        self.tw_label.setText(QCoreApplication.translate("FGCircle_Dialog", u"R0 = ", None))
        self.FGCircle_groupBox.setTitle(QCoreApplication.translate("FGCircle_Dialog", u"Material", None))
        self.label_3.setText(QCoreApplication.translate("FGCircle_Dialog", u"Gradation :", None))
        self.Color_label.setText(QCoreApplication.translate("FGCircle_Dialog", u"     \u03bc   = ", None))
        self.Law_comboBox.setItemText(0, QCoreApplication.translate("FGCircle_Dialog", u"Power law", None))
        self.Law_comboBox.setItemText(1, QCoreApplication.translate("FGCircle_Dialog", u"Exponential law", None))
        self.Law_comboBox.setItemText(2, QCoreApplication.translate("FGCircle_Dialog", u"Sigmoid law", None))

        self.eu_label.setText(QCoreApplication.translate("FGCircle_Dialog", u" eu = ", None))
        self.E_label.setText(QCoreApplication.translate("FGCircle_Dialog", u"     Ei = ", None))
        self.G_label.setText(QCoreApplication.translate("FGCircle_Dialog", u"     E0 = ", None))
        self.fy_label.setText(QCoreApplication.translate("FGCircle_Dialog", u" fy  = ", None))
        self.label_2.setText(QCoreApplication.translate("FGCircle_Dialog", u"Strip Num =", None))
        self.label_4.setText(QCoreApplication.translate("FGCircle_Dialog", u"     k =", None))
        self.OK_button.setText(QCoreApplication.translate("FGCircle_Dialog", u"OK", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("FGCircle_Dialog", u"Cancel", None))
    # retranslateUi

