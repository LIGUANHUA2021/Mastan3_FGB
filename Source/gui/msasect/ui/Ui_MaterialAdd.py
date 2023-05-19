# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MaterialAdd.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MatAddDialog(object):
    def setupUi(self, MatAddDialog):
        if not MatAddDialog.objectName():
            MatAddDialog.setObjectName(u"MatAddDialog")
        MatAddDialog.resize(335, 216)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MatAddDialog.sizePolicy().hasHeightForWidth())
        MatAddDialog.setSizePolicy(sizePolicy)
        MatAddDialog.setMinimumSize(QSize(335, 216))
        MatAddDialog.setMaximumSize(QSize(335, 216))
        MatAddDialog.setStyleSheet(u"*{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(MatAddDialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(MatAddDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(331, 176))
        self.groupBox.setMaximumSize(QSize(331, 176))
        self.groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setHorizontalSpacing(32)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(4, 10, 2, 10)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(169, 0))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.MatIDInput = QLineEdit(self.groupBox)
        self.MatIDInput.setObjectName(u"MatIDInput")
        self.MatIDInput.setMinimumSize(QSize(0, 22))
        self.MatIDInput.setMaximumSize(QSize(124, 22))
        self.MatIDInput.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.MatIDInput, 0, 1, 1, 1)

        self.OutlineID_Label = QLabel(self.groupBox)
        self.OutlineID_Label.setObjectName(u"OutlineID_Label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.OutlineID_Label.setFont(font)

        self.gridLayout.addWidget(self.OutlineID_Label, 1, 0, 1, 1)

        self.E_Input = QLineEdit(self.groupBox)
        self.E_Input.setObjectName(u"E_Input")
        self.E_Input.setMinimumSize(QSize(0, 22))
        self.E_Input.setMaximumSize(QSize(124, 22))
        self.E_Input.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.E_Input, 1, 1, 1, 1)

        self.MatID_Label = QLabel(self.groupBox)
        self.MatID_Label.setObjectName(u"MatID_Label")
        self.MatID_Label.setFont(font)

        self.gridLayout.addWidget(self.MatID_Label, 2, 0, 1, 1)

        self.Mu_Input = QLineEdit(self.groupBox)
        self.Mu_Input.setObjectName(u"Mu_Input")
        self.Mu_Input.setMinimumSize(QSize(0, 22))
        self.Mu_Input.setMaximumSize(QSize(124, 22))
        self.Mu_Input.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.Mu_Input, 2, 1, 1, 1)

        self.PointIID_label = QLabel(self.groupBox)
        self.PointIID_label.setObjectName(u"PointIID_label")

        self.gridLayout.addWidget(self.PointIID_label, 3, 0, 1, 1)

        self.fy_Input = QLineEdit(self.groupBox)
        self.fy_Input.setObjectName(u"fy_Input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fy_Input.sizePolicy().hasHeightForWidth())
        self.fy_Input.setSizePolicy(sizePolicy2)
        self.fy_Input.setMinimumSize(QSize(0, 22))
        self.fy_Input.setMaximumSize(QSize(124, 22))
        self.fy_Input.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.fy_Input, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.eu_input = QLineEdit(self.groupBox)
        self.eu_input.setObjectName(u"eu_input")
        self.eu_input.setMinimumSize(QSize(0, 22))
        self.eu_input.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.eu_input, 4, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(MatAddDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(2080, 34))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(4, 2, 0, 2)
        self.Import_pushButton = QPushButton(self.groupBox_2)
        self.Import_pushButton.setObjectName(u"Import_pushButton")
        self.Import_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Import_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.MaterialAdd_pushButton = QPushButton(self.groupBox_2)
        self.MaterialAdd_pushButton.setObjectName(u"MaterialAdd_pushButton")
        self.MaterialAdd_pushButton.setMaximumSize(QSize(75, 16777215))
        self.MaterialAdd_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.MaterialAdd_pushButton)

        self.MatchAddCancel_pushButton = QPushButton(self.groupBox_2)
        self.MatchAddCancel_pushButton.setObjectName(u"MatchAddCancel_pushButton")
        self.MatchAddCancel_pushButton.setMaximumSize(QSize(75, 16777215))
        self.MatchAddCancel_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.MatchAddCancel_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(MatAddDialog)

        QMetaObject.connectSlotsByName(MatAddDialog)
    # setupUi

    def retranslateUi(self, MatAddDialog):
        MatAddDialog.setWindowTitle(QCoreApplication.translate("MatAddDialog", u"Add Material", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MatAddDialog", u"Material ID:", None))
        self.OutlineID_Label.setText(QCoreApplication.translate("MatAddDialog", u"Young's Modulus of Elasticity, E:", None))
        self.MatID_Label.setText(QCoreApplication.translate("MatAddDialog", u"Poisson's Ratio, \u03bc:", None))
        self.PointIID_label.setText(QCoreApplication.translate("MatAddDialog", u"Characteristic Strength, fy:", None))
        self.label_2.setText(QCoreApplication.translate("MatAddDialog", u"Maximum Tensile Strain, eu:", None))
        self.groupBox_2.setTitle("")
        self.Import_pushButton.setText(QCoreApplication.translate("MatAddDialog", u"Import", None))
        self.MaterialAdd_pushButton.setText(QCoreApplication.translate("MatAddDialog", u"OK", None))
        self.MatchAddCancel_pushButton.setText(QCoreApplication.translate("MatAddDialog", u"Cancel", None))
    # retranslateUi

