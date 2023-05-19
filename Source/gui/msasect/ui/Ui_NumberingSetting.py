# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NumberingSetting.ui'
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
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_NumberSetting_Dialog(object):
    def setupUi(self, NumberSetting_Dialog):
        if not NumberSetting_Dialog.objectName():
            NumberSetting_Dialog.setObjectName(u"NumberSetting_Dialog")
        NumberSetting_Dialog.resize(327, 110)
        NumberSetting_Dialog.setMinimumSize(QSize(0, 110))
        NumberSetting_Dialog.setMaximumSize(QSize(16777215, 16777215))
        NumberSetting_Dialog.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(43, 43, 43);}\n"
"\n"
"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"\n"
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
"\n"
"\n"
"")
        NumberSetting_Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(NumberSetting_Dialog)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.InteractiveOptions_groupBox = QGroupBox(NumberSetting_Dialog)
        self.InteractiveOptions_groupBox.setObjectName(u"InteractiveOptions_groupBox")
        self.InteractiveOptions_groupBox.setMinimumSize(QSize(260, 72))
        self.InteractiveOptions_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.InteractiveOptions_groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout_3 = QVBoxLayout(self.InteractiveOptions_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 0, 4, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(16)
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setContentsMargins(2, 0, 4, 0)
        self.Decimal_radioButton = QRadioButton(self.InteractiveOptions_groupBox)
        self.Decimal_radioButton.setObjectName(u"Decimal_radioButton")

        self.gridLayout_3.addWidget(self.Decimal_radioButton, 0, 0, 1, 1)

        self.Scientific_radioButton = QRadioButton(self.InteractiveOptions_groupBox)
        self.Scientific_radioButton.setObjectName(u"Scientific_radioButton")

        self.gridLayout_3.addWidget(self.Scientific_radioButton, 1, 0, 1, 1)

        self.Decimal_spinBox = QSpinBox(self.InteractiveOptions_groupBox)
        self.Decimal_spinBox.setObjectName(u"Decimal_spinBox")
        self.Decimal_spinBox.setMinimumSize(QSize(0, 20))
        self.Decimal_spinBox.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.Decimal_spinBox, 0, 1, 1, 1)

        self.Scientific_spinBox = QSpinBox(self.InteractiveOptions_groupBox)
        self.Scientific_spinBox.setObjectName(u"Scientific_spinBox")
        self.Scientific_spinBox.setMinimumSize(QSize(0, 20))
        self.Scientific_spinBox.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.Scientific_spinBox, 1, 1, 1, 1)

        self.label = QLabel(self.InteractiveOptions_groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.InteractiveOptions_groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 3)

        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_2.addWidget(self.InteractiveOptions_groupBox)

        self.groupBox = QGroupBox(NumberSetting_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 30))
        self.groupBox.setMaximumSize(QSize(16777215, 32))
        self.groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 3, 2, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Reset_pushButton = QPushButton(self.groupBox)
        self.Reset_pushButton.setObjectName(u"Reset_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Reset_pushButton.sizePolicy().hasHeightForWidth())
        self.Reset_pushButton.setSizePolicy(sizePolicy)
        self.Reset_pushButton.setMinimumSize(QSize(75, 22))
        self.Reset_pushButton.setMaximumSize(QSize(75, 22))
        self.Reset_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.Reset_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.OK_pushButton = QPushButton(self.groupBox)
        self.OK_pushButton.setObjectName(u"OK_pushButton")
        sizePolicy.setHeightForWidth(self.OK_pushButton.sizePolicy().hasHeightForWidth())
        self.OK_pushButton.setSizePolicy(sizePolicy)
        self.OK_pushButton.setMinimumSize(QSize(75, 22))
        self.OK_pushButton.setMaximumSize(QSize(75, 22))
        self.OK_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.OK_pushButton)

        self.Cancel_pushButton = QPushButton(self.groupBox)
        self.Cancel_pushButton.setObjectName(u"Cancel_pushButton")
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setMinimumSize(QSize(75, 22))
        self.Cancel_pushButton.setMaximumSize(QSize(75, 22))
        self.Cancel_pushButton.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.Cancel_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        QWidget.setTabOrder(self.OK_pushButton, self.Cancel_pushButton)

        self.retranslateUi(NumberSetting_Dialog)

        QMetaObject.connectSlotsByName(NumberSetting_Dialog)
    # setupUi

    def retranslateUi(self, NumberSetting_Dialog):
        NumberSetting_Dialog.setWindowTitle(QCoreApplication.translate("NumberSetting_Dialog", u"Numbering Setting", None))
        self.InteractiveOptions_groupBox.setTitle("")
        self.Decimal_radioButton.setText(QCoreApplication.translate("NumberSetting_Dialog", u"Decimal", None))
        self.Scientific_radioButton.setText(QCoreApplication.translate("NumberSetting_Dialog", u"Scientific", None))
        self.label.setText(QCoreApplication.translate("NumberSetting_Dialog", u"Decimal Places", None))
        self.label_2.setText(QCoreApplication.translate("NumberSetting_Dialog", u"Significant Figures", None))
        self.groupBox.setTitle("")
        self.Reset_pushButton.setText(QCoreApplication.translate("NumberSetting_Dialog", u"Reset", None))
        self.OK_pushButton.setText(QCoreApplication.translate("NumberSetting_Dialog", u"OK", None))
        self.Cancel_pushButton.setText(QCoreApplication.translate("NumberSetting_Dialog", u"Cancel", None))
    # retranslateUi

