# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ISection.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ISection_Dialog(object):
    def setupUi(self, ISection_Dialog):
        if not ISection_Dialog.objectName():
            ISection_Dialog.setObjectName(u"ISection_Dialog")
        ISection_Dialog.resize(540, 533)
        ISection_Dialog.setMinimumSize(QSize(540, 533))
        ISection_Dialog.setMaximumSize(QSize(540, 533))
        ISection_Dialog.setStyleSheet(u"*{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(ISection_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 2, 1, 2)
        self.label = QLabel(ISection_Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"t3.jpg"))

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 0, -1)
        self.ModelingType_groupBox = QGroupBox(ISection_Dialog)
        self.ModelingType_groupBox.setObjectName(u"ModelingType_groupBox")
        self.ModelingType_groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout = QVBoxLayout(self.ModelingType_groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.Centerline_radioButton = QRadioButton(self.ModelingType_groupBox)
        self.Centerline_radioButton.setObjectName(u"Centerline_radioButton")

        self.verticalLayout.addWidget(self.Centerline_radioButton)

        self.Outline_radioButton = QRadioButton(self.ModelingType_groupBox)
        self.Outline_radioButton.setObjectName(u"Outline_radioButton")
        self.Outline_radioButton.setEnabled(True)

        self.verticalLayout.addWidget(self.Outline_radioButton)


        self.verticalLayout_2.addWidget(self.ModelingType_groupBox)

        self.Dimension_groupBox = QGroupBox(ISection_Dialog)
        self.Dimension_groupBox.setObjectName(u"Dimension_groupBox")
        self.Dimension_groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout_3 = QVBoxLayout(self.Dimension_groupBox)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(4, 4, 6, 4)
        self.B_label = QLabel(self.Dimension_groupBox)
        self.B_label.setObjectName(u"B_label")

        self.gridLayout_4.addWidget(self.B_label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.Dimension_groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.D_label = QLabel(self.Dimension_groupBox)
        self.D_label.setObjectName(u"D_label")

        self.gridLayout_4.addWidget(self.D_label, 2, 0, 1, 1)

        self.D_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.D_inputlineEdit.setObjectName(u"D_inputlineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.D_inputlineEdit.setSizePolicy(sizePolicy)
        self.D_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.D_inputlineEdit, 2, 1, 1, 1)

        self.B1_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.B1_inputlineEdit.setObjectName(u"B1_inputlineEdit")
        sizePolicy.setHeightForWidth(self.B1_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.B1_inputlineEdit.setSizePolicy(sizePolicy)
        self.B1_inputlineEdit.setMinimumSize(QSize(78, 0))
        self.B1_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.B1_inputlineEdit, 0, 1, 1, 1)

        self.B2_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.B2_inputlineEdit.setObjectName(u"B2_inputlineEdit")
        sizePolicy.setHeightForWidth(self.B2_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.B2_inputlineEdit.setSizePolicy(sizePolicy)
        self.B2_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.B2_inputlineEdit, 1, 1, 1, 1)

        self.tf_label = QLabel(self.Dimension_groupBox)
        self.tf_label.setObjectName(u"tf_label")

        self.gridLayout_4.addWidget(self.tf_label, 3, 0, 1, 1)

        self.t1_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.t1_inputlineEdit.setObjectName(u"t1_inputlineEdit")
        sizePolicy.setHeightForWidth(self.t1_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.t1_inputlineEdit.setSizePolicy(sizePolicy)
        self.t1_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.t1_inputlineEdit, 3, 1, 1, 1)

        self.k_label = QLabel(self.Dimension_groupBox)
        self.k_label.setObjectName(u"k_label")

        self.gridLayout_4.addWidget(self.k_label, 5, 0, 1, 1)

        self.k_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.k_inputlineEdit.setObjectName(u"k_inputlineEdit")
        sizePolicy.setHeightForWidth(self.k_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.k_inputlineEdit.setSizePolicy(sizePolicy)
        self.k_inputlineEdit.setMinimumSize(QSize(0, 19))
        self.k_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.k_inputlineEdit, 6, 1, 1, 1)

        self.t3_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.t3_inputlineEdit.setObjectName(u"t3_inputlineEdit")
        sizePolicy.setHeightForWidth(self.t3_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.t3_inputlineEdit.setSizePolicy(sizePolicy)
        self.t3_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.t3_inputlineEdit, 5, 1, 1, 1)

        self.label_4 = QLabel(self.Dimension_groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 7, 0, 1, 1)

        self.tw_label = QLabel(self.Dimension_groupBox)
        self.tw_label.setObjectName(u"tw_label")

        self.gridLayout_4.addWidget(self.tw_label, 4, 0, 1, 1)

        self.label_3 = QLabel(self.Dimension_groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 6, 0, 1, 1)

        self.t2_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.t2_inputlineEdit.setObjectName(u"t2_inputlineEdit")
        sizePolicy.setHeightForWidth(self.t2_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.t2_inputlineEdit.setSizePolicy(sizePolicy)
        self.t2_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.t2_inputlineEdit, 4, 1, 1, 1)

        self.k1_inputlineEdit = QLineEdit(self.Dimension_groupBox)
        self.k1_inputlineEdit.setObjectName(u"k1_inputlineEdit")
        sizePolicy.setHeightForWidth(self.k1_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.k1_inputlineEdit.setSizePolicy(sizePolicy)
        self.k1_inputlineEdit.setMinimumSize(QSize(0, 19))
        self.k1_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.k1_inputlineEdit, 7, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 8, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_4)


        self.verticalLayout_2.addWidget(self.Dimension_groupBox)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.ISection_groupBox = QGroupBox(ISection_Dialog)
        self.ISection_groupBox.setObjectName(u"ISection_groupBox")
        sizePolicy.setHeightForWidth(self.ISection_groupBox.sizePolicy().hasHeightForWidth())
        self.ISection_groupBox.setSizePolicy(sizePolicy)
        self.ISection_groupBox.setMinimumSize(QSize(0, 80))
        self.ISection_groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.gridLayout_2 = QGridLayout(self.ISection_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(9, 4, 9, 6)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.G_label = QLabel(self.ISection_groupBox)
        self.G_label.setObjectName(u"G_label")
        self.G_label.setMinimumSize(QSize(0, 19))

        self.gridLayout.addWidget(self.G_label, 0, 4, 1, 1)

        self.ID_label = QLabel(self.ISection_groupBox)
        self.ID_label.setObjectName(u"ID_label")
        self.ID_label.setMinimumSize(QSize(0, 19))

        self.gridLayout.addWidget(self.ID_label, 0, 0, 1, 1)

        self.E_label = QLabel(self.ISection_groupBox)
        self.E_label.setObjectName(u"E_label")
        self.E_label.setMinimumSize(QSize(0, 19))

        self.gridLayout.addWidget(self.E_label, 0, 2, 1, 1)

        self.fy_label = QLabel(self.ISection_groupBox)
        self.fy_label.setObjectName(u"fy_label")
        self.fy_label.setMinimumSize(QSize(0, 19))

        self.gridLayout.addWidget(self.fy_label, 1, 2, 1, 1)

        self.Color_label = QLabel(self.ISection_groupBox)
        self.Color_label.setObjectName(u"Color_label")
        self.Color_label.setMinimumSize(QSize(0, 19))

        self.gridLayout.addWidget(self.Color_label, 1, 0, 1, 1)

        self.eu_inputlineEdit = QLineEdit(self.ISection_groupBox)
        self.eu_inputlineEdit.setObjectName(u"eu_inputlineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.eu_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.eu_inputlineEdit.setSizePolicy(sizePolicy1)
        self.eu_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.eu_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.eu_inputlineEdit, 1, 5, 1, 1)

        self.fy_inputlineEdit = QLineEdit(self.ISection_groupBox)
        self.fy_inputlineEdit.setObjectName(u"fy_inputlineEdit")
        sizePolicy1.setHeightForWidth(self.fy_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.fy_inputlineEdit.setSizePolicy(sizePolicy1)
        self.fy_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.fy_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.fy_inputlineEdit, 1, 3, 1, 1)

        self.eu_label = QLabel(self.ISection_groupBox)
        self.eu_label.setObjectName(u"eu_label")
        self.eu_label.setMinimumSize(QSize(0, 19))

        self.gridLayout.addWidget(self.eu_label, 1, 4, 1, 1)

        self.G_inputlineEdit = QLineEdit(self.ISection_groupBox)
        self.G_inputlineEdit.setObjectName(u"G_inputlineEdit")
        sizePolicy1.setHeightForWidth(self.G_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.G_inputlineEdit.setSizePolicy(sizePolicy1)
        self.G_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.G_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.G_inputlineEdit, 1, 1, 1, 1)

        self.E_inputlineEdit = QLineEdit(self.ISection_groupBox)
        self.E_inputlineEdit.setObjectName(u"E_inputlineEdit")
        sizePolicy1.setHeightForWidth(self.E_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.E_inputlineEdit.setSizePolicy(sizePolicy1)
        self.E_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.E_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.E_inputlineEdit, 0, 5, 1, 1)

        self.ID_inputlineEdit = QLineEdit(self.ISection_groupBox)
        self.ID_inputlineEdit.setObjectName(u"ID_inputlineEdit")
        sizePolicy1.setHeightForWidth(self.ID_inputlineEdit.sizePolicy().hasHeightForWidth())
        self.ID_inputlineEdit.setSizePolicy(sizePolicy1)
        self.ID_inputlineEdit.setMinimumSize(QSize(0, 20))
        self.ID_inputlineEdit.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ID_inputlineEdit, 0, 3, 1, 1)

        self.ColorButton = QPushButton(self.ISection_groupBox)
        self.ColorButton.setObjectName(u"ColorButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ColorButton.sizePolicy().hasHeightForWidth())
        self.ColorButton.setSizePolicy(sizePolicy2)
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


        self.gridLayout_3.addWidget(self.ISection_groupBox, 0, 0, 1, 1)

        self.button_GroupBox = QGroupBox(ISection_Dialog)
        self.button_GroupBox.setObjectName(u"button_GroupBox")
        self.button_GroupBox.setMinimumSize(QSize(0, 0))
        self.button_GroupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.horizontalLayout_3 = QHBoxLayout(self.button_GroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 2, 2, 2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, -1, -1, -1)
        self.Import_pushButton = QPushButton(self.button_GroupBox)
        self.Import_pushButton.setObjectName(u"Import_pushButton")
        self.Import_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.Import_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.OK_button = QPushButton(self.button_GroupBox)
        self.OK_button.setObjectName(u"OK_button")
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
        QWidget.setTabOrder(self.Outline_radioButton, self.B1_inputlineEdit)
        QWidget.setTabOrder(self.B1_inputlineEdit, self.B2_inputlineEdit)
        QWidget.setTabOrder(self.B2_inputlineEdit, self.D_inputlineEdit)
        QWidget.setTabOrder(self.D_inputlineEdit, self.t1_inputlineEdit)
        QWidget.setTabOrder(self.t1_inputlineEdit, self.t2_inputlineEdit)
        QWidget.setTabOrder(self.t2_inputlineEdit, self.t3_inputlineEdit)
        QWidget.setTabOrder(self.t3_inputlineEdit, self.k_inputlineEdit)
        QWidget.setTabOrder(self.k_inputlineEdit, self.k1_inputlineEdit)
        QWidget.setTabOrder(self.k1_inputlineEdit, self.ColorButton)
        QWidget.setTabOrder(self.ColorButton, self.Import_pushButton)
        QWidget.setTabOrder(self.Import_pushButton, self.OK_button)
        QWidget.setTabOrder(self.OK_button, self.Cancel_pushButton)

        self.retranslateUi(ISection_Dialog)

        QMetaObject.connectSlotsByName(ISection_Dialog)
    # setupUi

    def retranslateUi(self, ISection_Dialog):
        ISection_Dialog.setWindowTitle(QCoreApplication.translate("ISection_Dialog", u"I-Section - Template", None))
        self.label.setText("")
        self.ModelingType_groupBox.setTitle(QCoreApplication.translate("ISection_Dialog", u"Modeling Type", None))
        self.Centerline_radioButton.setText(QCoreApplication.translate("ISection_Dialog", u"Centerline", None))
        self.Outline_radioButton.setText(QCoreApplication.translate("ISection_Dialog", u"Outline", None))
        self.Dimension_groupBox.setTitle(QCoreApplication.translate("ISection_Dialog", u"Dimension", None))
        self.B_label.setText(QCoreApplication.translate("ISection_Dialog", u"B1 = ", None))
        self.label_2.setText(QCoreApplication.translate("ISection_Dialog", u"B2 =", None))
        self.D_label.setText(QCoreApplication.translate("ISection_Dialog", u"D = ", None))
        self.tf_label.setText(QCoreApplication.translate("ISection_Dialog", u"t1 = ", None))
        self.k_label.setText(QCoreApplication.translate("ISection_Dialog", u"t3 = ", None))
        self.label_4.setText(QCoreApplication.translate("ISection_Dialog", u"k1 = ", None))
        self.tw_label.setText(QCoreApplication.translate("ISection_Dialog", u"t2 = ", None))
        self.label_3.setText(QCoreApplication.translate("ISection_Dialog", u"k = ", None))
        self.ISection_groupBox.setTitle(QCoreApplication.translate("ISection_Dialog", u"Material", None))
        self.G_label.setText(QCoreApplication.translate("ISection_Dialog", u" E  = ", None))
        self.ID_label.setText(QCoreApplication.translate("ISection_Dialog", u"Color = ", None))
        self.E_label.setText(QCoreApplication.translate("ISection_Dialog", u"ID = ", None))
        self.fy_label.setText(QCoreApplication.translate("ISection_Dialog", u"fy  = ", None))
        self.Color_label.setText(QCoreApplication.translate("ISection_Dialog", u"     \u03bc   = ", None))
        self.eu_label.setText(QCoreApplication.translate("ISection_Dialog", u"eu = ", None))
        self.ColorButton.setText("")
        self.Import_pushButton.setText(QCoreApplication.translate("ISection_Dialog", u"Import", None))
        self.OK_button.setText(QCoreApplication.translate("ISection_Dialog", u"OK", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("ISection_Dialog", u"Cancel", None))
    # retranslateUi

