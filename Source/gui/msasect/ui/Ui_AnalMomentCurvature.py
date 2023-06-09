# Form implementation generated from reading ui file 'AnalMomentCurvature.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MomentCurAnal_Dialog(object):
    def setupUi(self, MomentCurAnal_Dialog):
        MomentCurAnal_Dialog.setObjectName("MomentCurAnal_Dialog")
        MomentCurAnal_Dialog.resize(400, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MomentCurAnal_Dialog.sizePolicy().hasHeightForWidth())
        MomentCurAnal_Dialog.setSizePolicy(sizePolicy)
        MomentCurAnal_Dialog.setMinimumSize(QtCore.QSize(400, 414))
        MomentCurAnal_Dialog.setMaximumSize(QtCore.QSize(400, 414))
        MomentCurAnal_Dialog.setStyleSheet("*{\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1 px solid;\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(144, 200, 246);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1 px solid;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"")
        MomentCurAnal_Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MomentCurAnal_Dialog)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AxisSetting_groupBox = QtWidgets.QGroupBox(MomentCurAnal_Dialog)
        self.AxisSetting_groupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.AxisSetting_groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.AxisSetting_groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.AxisSetting_groupBox.setObjectName("AxisSetting_groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.AxisSetting_groupBox)
        self.horizontalLayout_3.setContentsMargins(25, 4, 4, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PrinAxis_radioButton = QtWidgets.QRadioButton(self.AxisSetting_groupBox)
        self.PrinAxis_radioButton.setMinimumSize(QtCore.QSize(0, 18))
        self.PrinAxis_radioButton.setChecked(True)
        self.PrinAxis_radioButton.setObjectName("PrinAxis_radioButton")
        self.horizontalLayout_3.addWidget(self.PrinAxis_radioButton)
        self.GeoAxis_radioButton = QtWidgets.QRadioButton(self.AxisSetting_groupBox)
        self.GeoAxis_radioButton.setMinimumSize(QtCore.QSize(0, 18))
        self.GeoAxis_radioButton.setObjectName("GeoAxis_radioButton")
        self.horizontalLayout_3.addWidget(self.GeoAxis_radioButton)
        self.verticalLayout_2.addWidget(self.AxisSetting_groupBox)
        self.AnalysisOptions_groupBox = QtWidgets.QGroupBox(MomentCurAnal_Dialog)
        self.AnalysisOptions_groupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.AnalysisOptions_groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.AnalysisOptions_groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.AnalysisOptions_groupBox.setObjectName("AnalysisOptions_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.AnalysisOptions_groupBox)
        self.horizontalLayout_2.setContentsMargins(25, 4, 4, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MzCur_radioButton = QtWidgets.QRadioButton(self.AnalysisOptions_groupBox)
        self.MzCur_radioButton.setMinimumSize(QtCore.QSize(0, 18))
        self.MzCur_radioButton.setChecked(False)
        self.MzCur_radioButton.setObjectName("MzCur_radioButton")
        self.horizontalLayout_2.addWidget(self.MzCur_radioButton)
        self.MyCur_radioButton = QtWidgets.QRadioButton(self.AnalysisOptions_groupBox)
        self.MyCur_radioButton.setMinimumSize(QtCore.QSize(0, 18))
        self.MyCur_radioButton.setChecked(True)
        self.MyCur_radioButton.setObjectName("MyCur_radioButton")
        self.horizontalLayout_2.addWidget(self.MyCur_radioButton)
        self.verticalLayout_2.addWidget(self.AnalysisOptions_groupBox)
        self.AnalysisInfo_groupBox = QtWidgets.QGroupBox(MomentCurAnal_Dialog)
        self.AnalysisInfo_groupBox.setMinimumSize(QtCore.QSize(300, 100))
        self.AnalysisInfo_groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.AnalysisInfo_groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.AnalysisInfo_groupBox.setObjectName("AnalysisInfo_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.AnalysisInfo_groupBox)
        self.gridLayout.setContentsMargins(25, 4, 4, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.InputtedPPy_lineEdit = QtWidgets.QLineEdit(self.AnalysisInfo_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputtedPPy_lineEdit.sizePolicy().hasHeightForWidth())
        self.InputtedPPy_lineEdit.setSizePolicy(sizePolicy)
        self.InputtedPPy_lineEdit.setMinimumSize(QtCore.QSize(70, 21))
        self.InputtedPPy_lineEdit.setMaximumSize(QtCore.QSize(70, 21))
        self.InputtedPPy_lineEdit.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::disabled{color:rgb(153, 153, 153)}")
        self.InputtedPPy_lineEdit.setObjectName("InputtedPPy_lineEdit")
        self.gridLayout.addWidget(self.InputtedPPy_lineEdit, 1, 1, 1, 1)
        self.AbsoluteValue_radioButton = QtWidgets.QRadioButton(self.AnalysisInfo_groupBox)
        self.AbsoluteValue_radioButton.setChecked(True)
        self.AbsoluteValue_radioButton.setObjectName("AbsoluteValue_radioButton")
        self.gridLayout.addWidget(self.AbsoluteValue_radioButton, 0, 0, 1, 1)
        self.InputtedPx_lineEdit = QtWidgets.QLineEdit(self.AnalysisInfo_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputtedPx_lineEdit.sizePolicy().hasHeightForWidth())
        self.InputtedPx_lineEdit.setSizePolicy(sizePolicy)
        self.InputtedPx_lineEdit.setMinimumSize(QtCore.QSize(70, 21))
        self.InputtedPx_lineEdit.setMaximumSize(QtCore.QSize(70, 21))
        self.InputtedPx_lineEdit.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::disabled{color:rgb(153, 153, 153)}")
        self.InputtedPx_lineEdit.setObjectName("InputtedPx_lineEdit")
        self.gridLayout.addWidget(self.InputtedPx_lineEdit, 0, 1, 1, 1)
        self.PercentageofMaxP_radioButton = QtWidgets.QRadioButton(self.AnalysisInfo_groupBox)
        self.PercentageofMaxP_radioButton.setObjectName("PercentageofMaxP_radioButton")
        self.gridLayout.addWidget(self.PercentageofMaxP_radioButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.AnalysisInfo_groupBox)
        self.label.setMinimumSize(QtCore.QSize(201, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("*{color: rgb(255, 255, 255);\n"
"font: 8pt \"Segoe UI\";\n"
"}")
        self.label.setIndent(20)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.AnalysisInfo_groupBox)
        self.AnalysisInfo_groupBox_2 = QtWidgets.QGroupBox(MomentCurAnal_Dialog)
        self.AnalysisInfo_groupBox_2.setMinimumSize(QtCore.QSize(327, 60))
        self.AnalysisInfo_groupBox_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.AnalysisInfo_groupBox_2.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.AnalysisInfo_groupBox_2.setObjectName("AnalysisInfo_groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.AnalysisInfo_groupBox_2)
        self.gridLayout_4.setContentsMargins(25, 4, 4, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.MomStep_lineEdit = QtWidgets.QLineEdit(self.AnalysisInfo_groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MomStep_lineEdit.sizePolicy().hasHeightForWidth())
        self.MomStep_lineEdit.setSizePolicy(sizePolicy)
        self.MomStep_lineEdit.setMinimumSize(QtCore.QSize(70, 21))
        self.MomStep_lineEdit.setMaximumSize(QtCore.QSize(70, 21))
        self.MomStep_lineEdit.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.MomStep_lineEdit.setObjectName("MomStep_lineEdit")
        self.gridLayout_4.addWidget(self.MomStep_lineEdit, 0, 1, 1, 1)
        self.MomStep_label = QtWidgets.QLabel(self.AnalysisInfo_groupBox_2)
        self.MomStep_label.setMinimumSize(QtCore.QSize(0, 22))
        self.MomStep_label.setObjectName("MomStep_label")
        self.gridLayout_4.addWidget(self.MomStep_label, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.AnalysisInfo_groupBox_2)
        self.InteractiveOptions_groupBox = QtWidgets.QGroupBox(MomentCurAnal_Dialog)
        self.InteractiveOptions_groupBox.setMinimumSize(QtCore.QSize(260, 90))
        self.InteractiveOptions_groupBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.InteractiveOptions_groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.InteractiveOptions_groupBox.setObjectName("InteractiveOptions_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.InteractiveOptions_groupBox)
        self.gridLayout_2.setContentsMargins(25, 4, 4, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MaxNumIntera_label = QtWidgets.QLabel(self.InteractiveOptions_groupBox)
        self.MaxNumIntera_label.setMinimumSize(QtCore.QSize(0, 22))
        self.MaxNumIntera_label.setIndent(-1)
        self.MaxNumIntera_label.setObjectName("MaxNumIntera_label")
        self.gridLayout_2.addWidget(self.MaxNumIntera_label, 0, 0, 1, 1)
        self.MaxNumIntera_lineEdit = QtWidgets.QLineEdit(self.InteractiveOptions_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MaxNumIntera_lineEdit.sizePolicy().hasHeightForWidth())
        self.MaxNumIntera_lineEdit.setSizePolicy(sizePolicy)
        self.MaxNumIntera_lineEdit.setMinimumSize(QtCore.QSize(70, 21))
        self.MaxNumIntera_lineEdit.setMaximumSize(QtCore.QSize(70, 21))
        self.MaxNumIntera_lineEdit.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.MaxNumIntera_lineEdit.setObjectName("MaxNumIntera_lineEdit")
        self.gridLayout_2.addWidget(self.MaxNumIntera_lineEdit, 0, 1, 1, 1)
        self.Tol_label = QtWidgets.QLabel(self.InteractiveOptions_groupBox)
        self.Tol_label.setMinimumSize(QtCore.QSize(0, 22))
        self.Tol_label.setObjectName("Tol_label")
        self.gridLayout_2.addWidget(self.Tol_label, 1, 0, 1, 1)
        self.Tol_lineEdit = QtWidgets.QLineEdit(self.InteractiveOptions_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tol_lineEdit.sizePolicy().hasHeightForWidth())
        self.Tol_lineEdit.setSizePolicy(sizePolicy)
        self.Tol_lineEdit.setMinimumSize(QtCore.QSize(70, 21))
        self.Tol_lineEdit.setMaximumSize(QtCore.QSize(70, 21))
        self.Tol_lineEdit.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.Tol_lineEdit.setObjectName("Tol_lineEdit")
        self.gridLayout_2.addWidget(self.Tol_lineEdit, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.InteractiveOptions_groupBox)
        self.groupBox = QtWidgets.QGroupBox(MomentCurAnal_Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 32))
        self.groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(2, 3, 2, 3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ShowResults_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowResults_pushButton.sizePolicy().hasHeightForWidth())
        self.ShowResults_pushButton.setSizePolicy(sizePolicy)
        self.ShowResults_pushButton.setMinimumSize(QtCore.QSize(86, 22))
        self.ShowResults_pushButton.setMaximumSize(QtCore.QSize(16777215, 22))
        self.ShowResults_pushButton.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.ShowResults_pushButton.setObjectName("ShowResults_pushButton")
        self.horizontalLayout.addWidget(self.ShowResults_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Run_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Run_pushButton.sizePolicy().hasHeightForWidth())
        self.Run_pushButton.setSizePolicy(sizePolicy)
        self.Run_pushButton.setMinimumSize(QtCore.QSize(75, 22))
        self.Run_pushButton.setMaximumSize(QtCore.QSize(75, 22))
        self.Run_pushButton.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.Run_pushButton.setObjectName("Run_pushButton")
        self.horizontalLayout.addWidget(self.Run_pushButton)
        self.Cancel_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setMinimumSize(QtCore.QSize(75, 22))
        self.Cancel_pushButton.setMaximumSize(QtCore.QSize(75, 22))
        self.Cancel_pushButton.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
"QPushButton::disabled{color:rgb(153, 153, 153)}\n"
"QPushButton{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.Cancel_pushButton.setObjectName("Cancel_pushButton")
        self.horizontalLayout.addWidget(self.Cancel_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(MomentCurAnal_Dialog)
        QtCore.QMetaObject.connectSlotsByName(MomentCurAnal_Dialog)
        MomentCurAnal_Dialog.setTabOrder(self.PrinAxis_radioButton, self.GeoAxis_radioButton)
        MomentCurAnal_Dialog.setTabOrder(self.GeoAxis_radioButton, self.Run_pushButton)
        MomentCurAnal_Dialog.setTabOrder(self.Run_pushButton, self.Cancel_pushButton)

    def retranslateUi(self, MomentCurAnal_Dialog):
        _translate = QtCore.QCoreApplication.translate
        MomentCurAnal_Dialog.setWindowTitle(_translate("MomentCurAnal_Dialog", "Calculation of Moment Curvature"))
        self.AxisSetting_groupBox.setTitle(_translate("MomentCurAnal_Dialog", "Axis Settings"))
        self.PrinAxis_radioButton.setText(_translate("MomentCurAnal_Dialog", "Principal Axis"))
        self.GeoAxis_radioButton.setText(_translate("MomentCurAnal_Dialog", "Geometric Axis"))
        self.AnalysisOptions_groupBox.setTitle(_translate("MomentCurAnal_Dialog", "Analysis Options"))
        self.MzCur_radioButton.setText(_translate("MomentCurAnal_Dialog", "Moment Curvature - Mz"))
        self.MyCur_radioButton.setText(_translate("MomentCurAnal_Dialog", "Moment Curvature - My"))
        self.AnalysisInfo_groupBox.setTitle(_translate("MomentCurAnal_Dialog", "Applied Axial Load:"))
        self.InputtedPPy_lineEdit.setText(_translate("MomentCurAnal_Dialog", "10"))
        self.AbsoluteValue_radioButton.setText(_translate("MomentCurAnal_Dialog", "Absolute Value"))
        self.InputtedPx_lineEdit.setText(_translate("MomentCurAnal_Dialog", "0.0"))
        self.PercentageofMaxP_radioButton.setText(_translate("MomentCurAnal_Dialog", "Percentage of Axial Capacity (%)"))
        self.label.setText(_translate("MomentCurAnal_Dialog", "<html><head/><body><p>Notes: Compression: Positive (+); Tension: Negative (-);</p></body></html>"))
        self.AnalysisInfo_groupBox_2.setTitle(_translate("MomentCurAnal_Dialog", "Analysis Parameters"))
        self.MomStep_lineEdit.setText(_translate("MomentCurAnal_Dialog", "100"))
        self.MomStep_label.setText(_translate("MomentCurAnal_Dialog", "Curvature Step:"))
        self.InteractiveOptions_groupBox.setTitle(_translate("MomentCurAnal_Dialog", "Interactive Options"))
        self.MaxNumIntera_label.setText(_translate("MomentCurAnal_Dialog", "Maximum Number of Iteration:"))
        self.MaxNumIntera_lineEdit.setText(_translate("MomentCurAnal_Dialog", "300"))
        self.Tol_label.setText(_translate("MomentCurAnal_Dialog", "Convergence Tolerance:"))
        self.Tol_lineEdit.setText(_translate("MomentCurAnal_Dialog", "0.001"))
        self.ShowResults_pushButton.setText(_translate("MomentCurAnal_Dialog", "Show Results"))
        self.Run_pushButton.setText(_translate("MomentCurAnal_Dialog", "Run"))
        self.Cancel_pushButton.setText(_translate("MomentCurAnal_Dialog", "Cancel"))
