# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeshSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QGridLayout,
                               QGroupBox, QHBoxLayout, QLineEdit, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)

class Ui_meshSettings_Dialog(object):
    def setupUi(self, meshSettings_Dialog):
        if not meshSettings_Dialog.objectName():
            meshSettings_Dialog.setObjectName(u"meshSettings_Dialog")
        meshSettings_Dialog.resize(265, 128)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(meshSettings_Dialog.sizePolicy().hasHeightForWidth())
        meshSettings_Dialog.setSizePolicy(sizePolicy)
        meshSettings_Dialog.setMinimumSize(QSize(265, 128))
        meshSettings_Dialog.setMaximumSize(QSize(265, 128))
        meshSettings_Dialog.setStyleSheet(u"*{\n"
                                          "	color: rgb(255, 255, 255);\n"
                                          "	font: 9pt \"Segoe UI\";\n"
                                          "	background-color: rgb(43, 43, 43)\n"
                                          "}")
        meshSettings_Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(meshSettings_Dialog)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(meshSettings_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(128, 128, 128);")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(25, 4, 6, 4)
        self.maxSizeInput_lineEdit = QLineEdit(self.groupBox)
        self.maxSizeInput_lineEdit.setObjectName(u"maxSizeInput_lineEdit")
        self.maxSizeInput_lineEdit.setEnabled(False)
        self.maxSizeInput_lineEdit.setMinimumSize(QSize(100, 20))
        self.maxSizeInput_lineEdit.setMaximumSize(QSize(100, 20))
        self.maxSizeInput_lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.maxSizeInput_lineEdit.setStyleSheet(u"QLineEdit::disabled{\n"
                                                 "	color: rgb(153, 153, 153)\n"
                                                 "}\n"
                                                 "QLineEdit{\n"
                                                 "	font: 9pt \"Segoe UI\";\n"
                                                 "	color: rgb(0, 0, 0);\n"
                                                 "	background-color: rgb(255, 255, 255)\n"
                                                 "}")
        self.maxSizeInput_lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.maxSizeInput_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.maxSizeInput_lineEdit, 0, 1, 1, 1)

        self.auto_radioButton = QRadioButton(self.groupBox)
        self.buttonGroup = QButtonGroup(meshSettings_Dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.auto_radioButton)
        self.auto_radioButton.setObjectName(u"auto_radioButton")
        self.auto_radioButton.setEnabled(True)
        self.auto_radioButton.setStyleSheet(u"QRadioButton::disabled{\n"
                                            "	font: 9pt \"Segoe UI\";\n"
                                            "	color: rgb(128, 128, 128)\n"
                                            "}")
        self.auto_radioButton.setChecked(True)

        self.gridLayout.addWidget(self.auto_radioButton, 1, 0, 1, 1)

        self.userDefined_radioButton = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.userDefined_radioButton)
        self.userDefined_radioButton.setObjectName(u"userDefined_radioButton")
        self.userDefined_radioButton.setEnabled(True)
        self.userDefined_radioButton.setStyleSheet(u"QRadioButton::disabled{\n"
                                                   "	font: 9pt \"Segoe UI\";\n"
                                                   "	color: rgb(128, 128, 128)\n"
                                                   "}")
        self.userDefined_radioButton.setChecked(False)

        self.gridLayout.addWidget(self.userDefined_radioButton, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(meshSettings_Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(261, 31))
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(128, 128, 128);")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 2, 2, 2)
        self.horizontalSpacer = QSpacerItem(61, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.apply_pushButton = QPushButton(self.groupBox_2)
        self.apply_pushButton.setObjectName(u"apply_pushButton")
        sizePolicy.setHeightForWidth(self.apply_pushButton.sizePolicy().hasHeightForWidth())
        self.apply_pushButton.setSizePolicy(sizePolicy)
        self.apply_pushButton.setMinimumSize(QSize(75, 24))
        self.apply_pushButton.setMaximumSize(QSize(75, 24))
        self.apply_pushButton.setStyleSheet(u"QPushButton::hover{\n"
                                            "background: rgb(144, 200, 246)\n"
                                            "}\n"
                                            "QPushButton::disabled{\n"
                                            "color: rgb(153, 153, 153)\n"
                                            "}\n"
                                            "QPushButton{\n"
                                            "	font: 9pt \"Segoe UI\";\n"
                                            "	color: rgb(0, 0, 0);\n"
                                            "	background-color: rgb(255, 255, 255);\n"
                                            "}")

        self.horizontalLayout_2.addWidget(self.apply_pushButton)

        self.cancel_pushButton = QPushButton(self.groupBox_2)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        sizePolicy.setHeightForWidth(self.cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.cancel_pushButton.setSizePolicy(sizePolicy)
        self.cancel_pushButton.setMinimumSize(QSize(75, 24))
        self.cancel_pushButton.setMaximumSize(QSize(75, 24))
        self.cancel_pushButton.setStyleSheet(u"QPushButton::hover{\n"
                                             "background: rgb(144, 200, 246)\n"
                                             "}\n"
                                             "QPushButton::disabled{\n"
                                             "color: rgb(153, 153, 153)\n"
                                             "}\n"
                                             "QPushButton{\n"
                                             "	font: 9pt \"Segoe UI\";\n"
                                             "	color: rgb(0, 0, 0);\n"
                                             "	background-color: rgb(255, 255, 255);\n"
                                             "}")

        self.horizontalLayout_2.addWidget(self.cancel_pushButton)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.retranslateUi(meshSettings_Dialog)

        QMetaObject.connectSlotsByName(meshSettings_Dialog)
    # setupUi

    def retranslateUi(self, meshSettings_Dialog):
        meshSettings_Dialog.setWindowTitle(QCoreApplication.translate("meshSettings_Dialog", u"Mesh Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("meshSettings_Dialog", u"Element Size", None))
        self.maxSizeInput_lineEdit.setText("")
        self.auto_radioButton.setText(QCoreApplication.translate("meshSettings_Dialog", u"Auto", None))
        self.userDefined_radioButton.setText(QCoreApplication.translate("meshSettings_Dialog", u"User Defined", None))
        self.groupBox_2.setTitle("")
        self.apply_pushButton.setText(QCoreApplication.translate("meshSettings_Dialog", u"Apply", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("meshSettings_Dialog", u"Cancel", None))
