# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PointAdd.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PointAdd_Dialog(object):
    def setupUi(self, PointAdd_Dialog):
        if not PointAdd_Dialog.objectName():
            PointAdd_Dialog.setObjectName(u"PointAdd_Dialog")
        PointAdd_Dialog.resize(214, 149)
        PointAdd_Dialog.setMinimumSize(QSize(200, 140))
        PointAdd_Dialog.setMaximumSize(QSize(16777215, 16777215))
        PointAdd_Dialog.setStyleSheet(u"*{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(PointAdd_Dialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(2, 2, 2, 1)
        self.groupBox = QGroupBox(PointAdd_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(210, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setContentsMargins(4, 9, 4, 9)
        self.PointID_Label = QLabel(self.groupBox)
        self.PointID_Label.setObjectName(u"PointID_Label")
        self.PointID_Label.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.PointID_Label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.PointID_Label)

        self.PointIDInput = QLineEdit(self.groupBox)
        self.PointIDInput.setObjectName(u"PointIDInput")
        self.PointIDInput.setMinimumSize(QSize(0, 22))
        self.PointIDInput.setMaximumSize(QSize(16777215, 22))
        self.PointIDInput.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.PointIDInput)

        self.YCoord_Label = QLabel(self.groupBox)
        self.YCoord_Label.setObjectName(u"YCoord_Label")
        self.YCoord_Label.setMinimumSize(QSize(60, 0))
        self.YCoord_Label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.YCoord_Label)

        self.Y_CoordInput = QLineEdit(self.groupBox)
        self.Y_CoordInput.setObjectName(u"Y_CoordInput")
        self.Y_CoordInput.setMinimumSize(QSize(0, 22))
        self.Y_CoordInput.setMaximumSize(QSize(16777215, 22))
        self.Y_CoordInput.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Y_CoordInput)

        self.ZCoord_Label = QLabel(self.groupBox)
        self.ZCoord_Label.setObjectName(u"ZCoord_Label")
        self.ZCoord_Label.setMinimumSize(QSize(60, 0))
        self.ZCoord_Label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ZCoord_Label)

        self.Z_CoordInput = QLineEdit(self.groupBox)
        self.Z_CoordInput.setObjectName(u"Z_CoordInput")
        self.Z_CoordInput.setMinimumSize(QSize(0, 22))
        self.Z_CoordInput.setMaximumSize(QSize(16777215, 22))
        self.Z_CoordInput.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Z_CoordInput)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(PointAdd_Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(210)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(210, 35))
        self.groupBox_2.setMaximumSize(QSize(210, 35))
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(2, 1, 1, 1)
        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PointAdd_button = QPushButton(self.groupBox_2)
        self.PointAdd_button.setObjectName(u"PointAdd_button")
        self.PointAdd_button.setMinimumSize(QSize(75, 24))
        self.PointAdd_button.setMaximumSize(QSize(75, 24))
        self.PointAdd_button.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.PointAdd_button)

        self.PointAddCancel_pushButton = QPushButton(self.groupBox_2)
        self.PointAddCancel_pushButton.setObjectName(u"PointAddCancel_pushButton")
        self.PointAddCancel_pushButton.setMinimumSize(QSize(75, 24))
        self.PointAddCancel_pushButton.setMaximumSize(QSize(75, 24))
        self.PointAddCancel_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.PointAddCancel_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(PointAdd_Dialog)

        QMetaObject.connectSlotsByName(PointAdd_Dialog)
    # setupUi

    def retranslateUi(self, PointAdd_Dialog):
        PointAdd_Dialog.setWindowTitle(QCoreApplication.translate("PointAdd_Dialog", u"Add Point", None))
        self.groupBox.setTitle("")
        self.PointID_Label.setText(QCoreApplication.translate("PointAdd_Dialog", u"Point ID:", None))
        self.YCoord_Label.setText(QCoreApplication.translate("PointAdd_Dialog", u"Y-Coord.:", None))
        self.ZCoord_Label.setText(QCoreApplication.translate("PointAdd_Dialog", u"Z-Coord.:", None))
        self.groupBox_2.setTitle("")
        self.PointAdd_button.setText(QCoreApplication.translate("PointAdd_Dialog", u"OK", None))
        self.PointAddCancel_pushButton.setText(QCoreApplication.translate("PointAdd_Dialog", u"Cancel", None))
    # retranslateUi

