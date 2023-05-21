# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 648)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(750, 648))
        Dialog.setMaximumSize(QtCore.QSize(750, 6480))
        Dialog.setStyleSheet("*{    \n"
"    background-color: rgb(43, 43, 43);\n"
"    color: white\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"     border: 4px solid rgb(240, 240, 240);\n"
"     background: solid rgb(240, 240, 240);\n"
"     width: 15px;\n"
"     margin: 16px 0 16px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: rgb(128, 128, 128);\n"
"     min-height: 18px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 3px solid rgb(240, 240, 240);\n"
"     background: solid rgb(240, 240, 240);\n"
"     height: 14px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 3px solid rgb(240, 240, 240);\n"
"     background: solid rgb(240, 240, 240);\n"
"     height: 14px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 3px solid rgb(240, 240, 240);\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: rgb(240, 240, 240);\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: solid rgb(240, 240, 240);\n"
" }\n"
"")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(156, 156))
        self.label.setMaximumSize(QtCore.QSize(156, 156))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: none;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(6, 16, 6, 6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_Version = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Version.sizePolicy().hasHeightForWidth())
        self.lineEdit_Version.setSizePolicy(sizePolicy)
        self.lineEdit_Version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit_Version.setFont(font)
        self.lineEdit_Version.setStyleSheet("*{    \n"
"    font: 10pt \"Microsoft YaHei UI\";\n"
"    color: rgb(237, 237, 237);\n"
"    background: rgb(127, 127, 127);\n"
"border-width:0;border-style:outset\n"
"}\n"
"")
        self.lineEdit_Version.setObjectName("lineEdit_Version")
        self.horizontalLayout.addWidget(self.lineEdit_Version)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_LastUpdateDate = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_LastUpdateDate.sizePolicy().hasHeightForWidth())
        self.label_LastUpdateDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_LastUpdateDate.setFont(font)
        self.label_LastUpdateDate.setObjectName("label_LastUpdateDate")
        self.horizontalLayout.addWidget(self.label_LastUpdateDate)
        self.lineEdit_lastUpdatedDate = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_lastUpdatedDate.sizePolicy().hasHeightForWidth())
        self.lineEdit_lastUpdatedDate.setSizePolicy(sizePolicy)
        self.lineEdit_lastUpdatedDate.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_lastUpdatedDate.setStyleSheet("*{    \n"
"    font: 10pt \"Microsoft YaHei UI\";\n"
"    color: rgb(237, 237, 237);\n"
"    background: rgb(127, 127, 127);\n"
"border-width:0;border-style:outset\n"
"}\n"
"")
        self.lineEdit_lastUpdatedDate.setObjectName("lineEdit_lastUpdatedDate")
        self.horizontalLayout.addWidget(self.lineEdit_lastUpdatedDate)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.textBrowser.setStyleSheet("*{background-color:rgb(43, 43, 43);\n"
"color:rgb(255, 255, 255);\n"
"font: 9pt \"Microsoft YaHei UI\";}\n"
"")
        self.textBrowser.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setContentsMargins(0, 4, 2, 4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.About_OKpushbutton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.About_OKpushbutton.sizePolicy().hasHeightForWidth())
        self.About_OKpushbutton.setSizePolicy(sizePolicy)
        self.About_OKpushbutton.setMinimumSize(QtCore.QSize(75, 22))
        self.About_OKpushbutton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.About_OKpushbutton.setFont(font)
        self.About_OKpushbutton.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.About_OKpushbutton.setDefault(True)
        self.About_OKpushbutton.setFlat(False)
        self.About_OKpushbutton.setObjectName("About_OKpushbutton")
        self.horizontalLayout_5.addWidget(self.About_OKpushbutton)
        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.retranslateUi(Dialog)
        self.About_OKpushbutton.clicked.connect(Dialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About MSASECT2"))
        self.label_3.setText(_translate("Dialog", "Version:"))
        self.label_LastUpdateDate.setText(_translate("Dialog", "Last Updated Date:"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Developed by:</span></p><p>Siwei Liu - Assistant Professor, The Hong Kong Polytechnic University, <a href=\"si-wei.liu@polyu.edu.hk\"><span style=\" text-decoration: underline; color:#ffffff;\">si-wei.liu@polyu.edu.hk</span></a></p><p>Ronald D. Ziemian - Professor, Bucknell University, <a href=\"ziemian@bucknell.edu\"><span style=\" text-decoration: underline; color:#ffffff;\">ziemian@bucknell.edu</span></a></p><p><span style=\" font-weight:700;\">Contributed by (surnames in alphabetical order):</span></p><p>Liang Chen, Wenlong Gao, Guanhua Li, Weihang Ouyang and Haoyi Zhang</p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'sans-serif\'; font-weight:700;\">Disclaimer:</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'sans-serif\'; font-weight:700;\"> </span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">Considerable care has been taken to ensure the accuracy of this software. However, the user assumes full responsibility for its use, and the developers or distributors will not be liable for any damage caused by the use or misuse of this software. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">The user should have a thorough understanding of the software\'s modeling, analysis, and design algorithms, and should compensate for any aspects that are not addressed. We recommend that a qualified and experienced engineer be appointed to check the input and verify the results produced by the software. The engineer should take professional responsibility for the information that is used. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">By using this software, you agree to these terms and conditions:</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\';\">·</span><span style=\" font-family:\'Times New Roman\';\">       </span><span style=\" font-family:\'Times New Roman\',\'serif\';\">LICENSE AND OWNERSHIP</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">This software is owned and licensed by Developers. Developers grants you a limited, non-exclusive, non-transferable license to use the software solely for educational purposes. You may not use the software for commercial purposes or for any illegal or unauthorized purpose. All rights, title, and interest in and to the software, including all intellectual property rights, remain with Developers.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\';\">·</span><span style=\" font-family:\'Times New Roman\';\">       </span><span style=\" font-family:\'Times New Roman\',\'serif\';\">WARRANTY DISCLAIMER</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">This software is provided &quot;as is&quot; without warranty of any kind, either express or implied, including but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Developers does not warrant that the software will meet your requirements or that the operation of the software will be uninterrupted or error-free.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\';\">·</span><span style=\" font-family:\'Times New Roman\';\">       </span><span style=\" font-family:\'Times New Roman\',\'serif\';\">LIMITATION OF LIABILITY</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">In no event shall Developers be liable for any direct, indirect, incidental, special, or consequential damages arising out of or in connection with the use or inability to use this software, even if [Developer Name] has been advised of the possibility of such damages. Some jurisdictions do not allow the exclusion or limitation of incidental or consequential damages, so the above limitation or exclusion may not apply to you.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\';\">·</span><span style=\" font-family:\'Times New Roman\';\">       </span><span style=\" font-family:\'Times New Roman\',\'serif\';\">INDEMNIFICATION</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">You agree to indemnify, defend, and hold harmless Developers, its officers, directors, employees, agents, licensors, and suppliers from and against all claims, losses, expenses, damages, and costs, including reasonable attorneys\' fees, arising out of or in connection with your use of the software or your breach of these Terms.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\';\">·</span><span style=\" font-family:\'Times New Roman\';\">       </span><span style=\" font-family:\'Times New Roman\',\'serif\';\">TERMINATION</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">Developers may terminate this license at any time if you fail to comply with these Terms. Upon termination, you must immediately stop using the software and destroy all copies of the software in your possession.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\';\">·</span><span style=\" font-family:\'Times New Roman\';\">       </span><span style=\" font-family:\'Times New Roman\',\'serif\';\">ENTIRE AGREEMENT</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">These Terms constitute the entire agreement between you and Developers with respect to the use of the software and supersede all prior or contemporaneous communications and proposals, whether oral or written, between you and Developers. If any provision of these Terms is found to be invalid or unenforceable, the remaining provisions shall be enforced to the fullest extent possible, and the remaining provisions shall remain in full force and effect.</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'sans-serif\'; font-weight:700;\">Third-party Libraries:</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'sans-serif\'; font-weight:700;\"> </span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">This software includes open source and third-party software components, including the following:</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• gmsh: A 3D finite element grid generator with a built-in CAD engine and post-processor, licensed under the GPL license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• matplotlib: A library for creating static, animated, and interactive visualizations in Python, licensed under the Python Software Foundation license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• numpy: The fundamental package for scientific computing with Python, licensed under the BSD license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• openpyxl: A library for reading and writing Excel files, licensed under the MIT license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• PyOpenGL: A Python wrapper for OpenGL, licensed under the BSD license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• PySide6: A Python binding for the Qt application framework, licensed under the LGPL version 3. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• pyqtgraph: A pure-python graphics and GUI library built on PyQt5/PySide2 and numpy, licensed under the MIT license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• scipy: A library for scientific computing and technical computing, licensed under the BSD license. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">• vispy: A high-performance interactive 2D/3D visualization library, licensed under the BSD license.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">We acknowledge the valuable contributions of the developers and communities behind these libraries. The terms of their respective licenses apply to the use of these components in this software.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\';\">For more information on the licenses used by these components, please refer to the documentation provided with the software or the websites of the respective projects.</span> </p></body></html>"))
        self.label_4.setText(_translate("Dialog", "  Copyright © 2023 Siwei Liu and Ronald D. Ziemian, All Right Reserved."))
        self.About_OKpushbutton.setText(_translate("Dialog", "OK"))