# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SPAnalMessageBox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
                               QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
                               QToolButton, QWidget)
from gui.msasect.base.OutputRedir import CallableEvent
from PySide6.QtWidgets import QTextBrowser

class CustomTextBrowser(QTextBrowser):
    def event(self, event):
        if isinstance(event, CallableEvent):
            event.execute()
            return True
        return super().event(event)


class Ui_SPAnalMessageBox_Dialog(object):
    def setupUi(self, SPAnalMessageBox_Dialog):
        if not SPAnalMessageBox_Dialog.objectName():
            SPAnalMessageBox_Dialog.setObjectName(u"SPAnalMessageBox_Dialog")
        SPAnalMessageBox_Dialog.resize(621, 548)
        SPAnalMessageBox_Dialog.setStyleSheet(u"QDialog\n"
                                              "{\n"
                                              " background-color: rgb(43, 43, 43);\n"
                                              "}\n"
                                              "QComboBox\n"
                                              "{\n"
                                              "	border-radius: 3px;\n"
                                              "}\n"
                                              "QComboBox::hover\n"
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
                                              "QGroupBox\n"
                                              "{\n"
                                              "	background-color: rgb(128, 128, 128);\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "QLabel\n"
                                              "{\n"
                                              "	background-color: rgb(255, 255, 255);\n"
                                              "	color: rgb(0, 0, 0);\n"
                                              "	border-radius: 3px;\n"
                                              "}\n"
                                              "QPushButton\n"
                                              "{\n"
                                              "	background-color: rgb(255, 255, 255);\n"
                                              "	border-radius: 3px;\n"
                                              "}\n"
                                              "QPushButton::hover\n"
                                              "{\n"
                                              "	background-color: rgb(144, 200, 246);\n"
                                              "}\n"
                                              "QPushButton:pressed\n"
                                              "{\n"
                                              " padding-left: 3px;\n"
                                              " padding-top: 3px;\n"
                                              "}\n"
                                              "QPushButton::disabled\n"
                                              "{\n"
                                              "	background-color: rgb(160, 160, 160);\n"
                                              "	color: rgb(80, 80, 80);\n"
                                              "}\n"
                                              ""
                                              "QTextBrowser\n"
                                              "{\n"
                                              "	background-color: rgb(43, 43, 43);\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "QToolButton\n"
                                              "{\n"
                                              "	border-radius: 5px;\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "QToolButton:hover\n"
                                              "{\n"
                                              "	background-color: rgba(255, 255, 255, 20%);\n"
                                              "}\n"
                                              "QToolButton:pressed\n"
                                              "{\n"
                                              "	background-color: rgba(0, 0, 0, 20%);\n"
                                              "	border-top: 1px solid rgba(0, 0, 0, 50%);\n"
                                              "	border-left: 1px solid rgba(0, 0, 0, 50%);\n"
                                              "	padding: 0;\n"
                                              "}")
        SPAnalMessageBox_Dialog.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(SPAnalMessageBox_Dialog)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.YSMessageBox_textBrowser = CustomTextBrowser(SPAnalMessageBox_Dialog)
        self.YSMessageBox_textBrowser.setObjectName(u"YSMessageBox_textBrowser")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.YSMessageBox_textBrowser.setFont(font)

        self.gridLayout.addWidget(self.YSMessageBox_textBrowser, 1, 0, 2, 2)

        self.groupBox_4 = QGroupBox(SPAnalMessageBox_Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 34))
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.STime_label = QLabel(self.groupBox_4)
        self.STime_label.setObjectName(u"STime_label")
        self.STime_label.setMinimumSize(QSize(80, 22))
        self.STime_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.STime_label.setMargin(6)
        self.STime_label.setIndent(1)

        self.horizontalLayout.addWidget(self.STime_label)

        self.StartTimeDay_label = QLabel(self.groupBox_4)
        self.StartTimeDay_label.setObjectName(u"StartTimeDay_label")
        self.StartTimeDay_label.setMinimumSize(QSize(70, 22))
        self.StartTimeDay_label.setMargin(2)

        self.horizontalLayout.addWidget(self.StartTimeDay_label)

        self.StartTimer_label = QLabel(self.groupBox_4)
        self.StartTimer_label.setObjectName(u"StartTimer_label")
        self.StartTimer_label.setMinimumSize(QSize(70, 22))
        self.StartTimer_label.setMargin(2)

        self.horizontalLayout.addWidget(self.StartTimer_label)

        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Stop_pushButton = QPushButton(self.groupBox_4)
        self.Stop_pushButton.setObjectName(u"Stop_pushButton")
        self.Stop_pushButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stop_pushButton.sizePolicy().hasHeightForWidth())
        self.Stop_pushButton.setSizePolicy(sizePolicy)
        self.Stop_pushButton.setMinimumSize(QSize(56, 22))
        self.Stop_pushButton.setStyleSheet(u"QPushButton\n"
                                           "{\n"
                                           "	background-color: rgb(255, 0, 0);\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "	border-radius: 3px;\n"
                                           "}\n"
                                           "QPushButton::disabled\n"
                                           "{\n"
                                           "	background-color: rgb(160, 160, 160);\n"
                                           "	color: rgb(80, 80, 80);\n"
                                           "}")

        self.horizontalLayout.addWidget(self.Stop_pushButton)

        self.OK_pushButton = QPushButton(self.groupBox_4)
        self.OK_pushButton.setObjectName(u"OK_pushButton")
        sizePolicy.setHeightForWidth(self.OK_pushButton.sizePolicy().hasHeightForWidth())
        self.OK_pushButton.setSizePolicy(sizePolicy)
        self.OK_pushButton.setMinimumSize(QSize(56, 22))

        self.horizontalLayout.addWidget(self.OK_pushButton)

        self.gridLayout.addWidget(self.groupBox_4, 3, 0, 1, 2)

        self.groupBox = QGroupBox(SPAnalMessageBox_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 34))
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
        self.ExportMessage_label.setMinimumSize(QSize(80, 22))
        self.ExportMessage_label.setMaximumSize(QSize(160000, 16777215))
        self.ExportMessage_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.ExportMessage_label.setMargin(6)
        self.ExportMessage_label.setIndent(1)

        self.horizontalLayout_2.addWidget(self.ExportMessage_label)

        self.ExportFileFormat_comboBox = QComboBox(self.groupBox)
        self.ExportFileFormat_comboBox.addItem("")
        self.ExportFileFormat_comboBox.setObjectName(u"ExportFileFormat_comboBox")
        self.ExportFileFormat_comboBox.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_2.addWidget(self.ExportFileFormat_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(180, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.SaveText_toolButton = QToolButton(self.groupBox)
        self.SaveText_toolButton.setObjectName(u"SaveText_toolButton")
        self.SaveText_toolButton.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_2.addWidget(self.SaveText_toolButton)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 14)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(SPAnalMessageBox_Dialog)

        QMetaObject.connectSlotsByName(SPAnalMessageBox_Dialog)

    # setupUi

    def retranslateUi(self, SPAnalMessageBox_Dialog):
        SPAnalMessageBox_Dialog.setWindowTitle(
            QCoreApplication.translate("SPAnalMessageBox_Dialog", u"Analysis is running, please wait patiently ...",
                                       None))
        self.groupBox_4.setTitle("")
        self.STime_label.setText(QCoreApplication.translate("SPAnalMessageBox_Dialog", u"Start Time\uff1a", None))
        self.StartTimeDay_label.setText("")
        self.StartTimer_label.setText("")
        self.Stop_pushButton.setText(QCoreApplication.translate("SPAnalMessageBox_Dialog", u"Stop", None))
        self.OK_pushButton.setText(QCoreApplication.translate("SPAnalMessageBox_Dialog", u"OK", None))
        self.groupBox.setTitle("")
        self.ExportMessage_label.setText(
            QCoreApplication.translate("SPAnalMessageBox_Dialog", u"Export message to:", None))
        self.ExportFileFormat_comboBox.setItemText(0, QCoreApplication.translate("SPAnalMessageBox_Dialog",
                                                                                 u"Text File Format", None))

        self.SaveText_toolButton.setText("")
