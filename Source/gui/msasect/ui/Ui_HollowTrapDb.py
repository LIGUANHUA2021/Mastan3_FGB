# Form implementation generated from reading ui file 'HollowTrapDb.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_HollowTrapDb_Dialog(object):
    def setupUi(self, HollowTrapDb_Dialog):
        HollowTrapDb_Dialog.setObjectName("HollowTrapDb_Dialog")
        HollowTrapDb_Dialog.resize(447, 561)
        HollowTrapDb_Dialog.setStyleSheet("*{    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 9pt \"Segoe UI\";\n"
"    background-color: rgb(43, 43, 43);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(HollowTrapDb_Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HollowTrapDb_groupBox = QtWidgets.QGroupBox(HollowTrapDb_Dialog)
        self.HollowTrapDb_groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.HollowTrapDb_groupBox.setObjectName("HollowTrapDb_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.HollowTrapDb_groupBox)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ComboBox = QtWidgets.QComboBox(self.HollowTrapDb_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy)
        self.ComboBox.setMinimumSize(QtCore.QSize(0, 22))
        self.ComboBox.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.ComboBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.HollowTrapDb_groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Section_tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.Section_tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Section_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Section_tableWidget.setObjectName("Section_tableWidget")
        self.Section_tableWidget.setColumnCount(0)
        self.Section_tableWidget.setRowCount(0)
        self.Section_tableWidget.horizontalHeader().setVisible(False)
        self.Section_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.Section_tableWidget)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.HollowTrapDb_groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 220))
        self.label.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.groupBox_2 = QtWidgets.QGroupBox(self.HollowTrapDb_groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Dimensions_tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.Dimensions_tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Dimensions_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Dimensions_tableWidget.setObjectName("Dimensions_tableWidget")
        self.Dimensions_tableWidget.setColumnCount(0)
        self.Dimensions_tableWidget.setRowCount(0)
        self.Dimensions_tableWidget.horizontalHeader().setVisible(False)
        self.Dimensions_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.Dimensions_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.Dimensions_tableWidget)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addWidget(self.HollowTrapDb_groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(HollowTrapDb_Dialog)
        self.groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setContentsMargins(0, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.OK_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OK_button.sizePolicy().hasHeightForWidth())
        self.OK_button.setSizePolicy(sizePolicy)
        self.OK_button.setMinimumSize(QtCore.QSize(75, 24))
        self.OK_button.setMaximumSize(QtCore.QSize(75, 24))
        self.OK_button.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.OK_button.setObjectName("OK_button")
        self.horizontalLayout_4.addWidget(self.OK_button)
        self.Cancel_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.Cancel_pushButton.setStyleSheet("*{    \n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.Cancel_pushButton.setObjectName("Cancel_pushButton")
        self.horizontalLayout_4.addWidget(self.Cancel_pushButton)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(HollowTrapDb_Dialog)
        QtCore.QMetaObject.connectSlotsByName(HollowTrapDb_Dialog)

    def retranslateUi(self, HollowTrapDb_Dialog):
        _translate = QtCore.QCoreApplication.translate
        HollowTrapDb_Dialog.setWindowTitle(_translate("HollowTrapDb_Dialog", "Hollow Trapezoid - Database"))
        self.HollowTrapDb_groupBox.setTitle(_translate("HollowTrapDb_Dialog", "Database"))
        self.ComboBox.setItemText(0, _translate("HollowTrapDb_Dialog", "User-Trap(mm)"))
        self.ComboBox.setItemText(1, _translate("HollowTrapDb_Dialog", "User-Trap(in)"))
        self.groupBox_3.setTitle(_translate("HollowTrapDb_Dialog", "Section name:"))
        self.groupBox_2.setTitle(_translate("HollowTrapDb_Dialog", "Dimensions:"))
        self.OK_button.setText(_translate("HollowTrapDb_Dialog", "OK"))
        self.Cancel_pushButton.setText(_translate("HollowTrapDb_Dialog", "Cancel"))
