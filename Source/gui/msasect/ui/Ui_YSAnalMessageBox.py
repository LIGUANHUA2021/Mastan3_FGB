# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YSAnalMessageBox.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QToolButton, QWidget)
from gui.msasect.base.OutputRedir import CallableEvent
from PySide6.QtWidgets import QTextBrowser

class CustomTextBrowser(QTextBrowser):
    def event(self, event):
        if isinstance(event, CallableEvent):
            event.execute()
            return True
        return super().event(event)


class Ui_YSAnalMessageBox_Dialog(object):
    def setupUi(self, YSAnalMessageBox_Dialog):
        if not YSAnalMessageBox_Dialog.objectName():
            YSAnalMessageBox_Dialog.setObjectName(u"YSAnalMessageBox_Dialog")
        YSAnalMessageBox_Dialog.resize(621, 548)
        YSAnalMessageBox_Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(43, 43, 43);\n"
"\n"
"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"\n"
"\n"
"\n"
"")
        YSAnalMessageBox_Dialog.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(YSAnalMessageBox_Dialog)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.YSMessageBox_textBrowser = CustomTextBrowser(YSAnalMessageBox_Dialog)
        self.YSMessageBox_textBrowser.setObjectName(u"YSMessageBox_textBrowser")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.YSMessageBox_textBrowser.setFont(font)
        self.YSMessageBox_textBrowser.setStyleSheet(u"*{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"	background: rgb(43, 43, 43);\n"
"}")

        self.gridLayout.addWidget(self.YSMessageBox_textBrowser, 1, 0, 2, 2)

        self.groupBox_4 = QGroupBox(YSAnalMessageBox_Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 34))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.STime_label = QLabel(self.groupBox_4)
        self.STime_label.setObjectName(u"STime_label")
        self.STime_label.setMinimumSize(QSize(80, 22))
        self.STime_label.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background: rgb(255, 255, 255);")
        self.STime_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.STime_label.setMargin(6)
        self.STime_label.setIndent(1)

        self.horizontalLayout.addWidget(self.STime_label)

        self.StartTimeDay_label = QLabel(self.groupBox_4)
        self.StartTimeDay_label.setObjectName(u"StartTimeDay_label")
        self.StartTimeDay_label.setMinimumSize(QSize(70, 22))
        self.StartTimeDay_label.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background: rgb(255, 255, 255);")
        self.StartTimeDay_label.setMargin(2)

        self.horizontalLayout.addWidget(self.StartTimeDay_label)

        self.StartTimer_label = QLabel(self.groupBox_4)
        self.StartTimer_label.setObjectName(u"StartTimer_label")
        self.StartTimer_label.setMinimumSize(QSize(70, 22))
        self.StartTimer_label.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background: rgb(255, 255, 255);")
        self.StartTimer_label.setMargin(2)

        self.horizontalLayout.addWidget(self.StartTimer_label)

        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Stop_pushButton = QPushButton(self.groupBox_4)
        self.Stop_pushButton.setObjectName(u"Stop_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stop_pushButton.sizePolicy().hasHeightForWidth())
        self.Stop_pushButton.setSizePolicy(sizePolicy)
        self.Stop_pushButton.setMinimumSize(QSize(56, 22))
        self.Stop_pushButton.setStyleSheet(u"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.Stop_pushButton)

        self.OK_pushButton = QPushButton(self.groupBox_4)
        self.OK_pushButton.setObjectName(u"OK_pushButton")
        sizePolicy.setHeightForWidth(self.OK_pushButton.sizePolicy().hasHeightForWidth())
        self.OK_pushButton.setSizePolicy(sizePolicy)
        self.OK_pushButton.setMinimumSize(QSize(56, 22))
        self.OK_pushButton.setStyleSheet(u"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.OK_pushButton)


        self.gridLayout.addWidget(self.groupBox_4, 3, 0, 1, 2)

        self.groupBox = QGroupBox(YSAnalMessageBox_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 34))
        self.groupBox.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.ExportMessage_label = QLabel(self.groupBox)
        self.ExportMessage_label.setObjectName(u"ExportMessage_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ExportMessage_label.sizePolicy().hasHeightForWidth())
        self.ExportMessage_label.setSizePolicy(sizePolicy1)
        self.ExportMessage_label.setMinimumSize(QSize(80, 24))
        self.ExportMessage_label.setMaximumSize(QSize(160000, 16777215))
        self.ExportMessage_label.setFont(font)
        self.ExportMessage_label.setToolTipDuration(0)
        self.ExportMessage_label.setStyleSheet(u"*{font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background: rgb(255, 255, 255);\n"
"}")
        self.ExportMessage_label.setFrameShadow(QFrame.Plain)
        self.ExportMessage_label.setLineWidth(1)
        self.ExportMessage_label.setMidLineWidth(0)
        self.ExportMessage_label.setScaledContents(True)
        self.ExportMessage_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ExportMessage_label.setMargin(6)
        self.ExportMessage_label.setIndent(1)

        self.horizontalLayout_2.addWidget(self.ExportMessage_label)

        self.ExportFileFormat_comboBox = QComboBox(self.groupBox)
        self.ExportFileFormat_comboBox.addItem("")
        self.ExportFileFormat_comboBox.setObjectName(u"ExportFileFormat_comboBox")
        self.ExportFileFormat_comboBox.setMinimumSize(QSize(0, 22))
        self.ExportFileFormat_comboBox.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ExportFileFormat_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(180, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.SaveText_toolButton = QToolButton(self.groupBox)
        self.SaveText_toolButton.setObjectName(u"SaveText_toolButton")
        self.SaveText_toolButton.setMinimumSize(QSize(0, 22))
        self.SaveText_toolButton.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(128, 128, 128);")

        self.horizontalLayout_2.addWidget(self.SaveText_toolButton)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 14)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(YSAnalMessageBox_Dialog)

        QMetaObject.connectSlotsByName(YSAnalMessageBox_Dialog)
    # setupUi

    def retranslateUi(self, YSAnalMessageBox_Dialog):
        YSAnalMessageBox_Dialog.setWindowTitle(QCoreApplication.translate("YSAnalMessageBox_Dialog", u"Analysis is running, please wait patiently ...", None))
        self.groupBox_4.setTitle("")
        self.STime_label.setText(QCoreApplication.translate("YSAnalMessageBox_Dialog", u"Start Time\uff1a", None))
        self.StartTimeDay_label.setText("")
        self.StartTimer_label.setText("")
        self.Stop_pushButton.setText(QCoreApplication.translate("YSAnalMessageBox_Dialog", u"Stop", None))
        self.OK_pushButton.setText(QCoreApplication.translate("YSAnalMessageBox_Dialog", u"OK", None))
        self.groupBox.setTitle("")
        self.ExportMessage_label.setText(QCoreApplication.translate("YSAnalMessageBox_Dialog", u"Export message to:", None))
        self.ExportFileFormat_comboBox.setItemText(0, QCoreApplication.translate("YSAnalMessageBox_Dialog", u"Text File Format", None))

        self.SaveText_toolButton.setText("")
    # retranslateUi

