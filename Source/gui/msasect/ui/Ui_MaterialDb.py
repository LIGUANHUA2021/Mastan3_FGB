# Form implementation generated from reading ui file 'MaterialDb.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MaterialDb_Dialog(object):
    def setupUi(self, MaterialDb_Dialog):
        MaterialDb_Dialog.setObjectName("MaterialDb_Dialog")
        MaterialDb_Dialog.resize(360, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MaterialDb_Dialog.sizePolicy().hasHeightForWidth())
        MaterialDb_Dialog.setSizePolicy(sizePolicy)
        MaterialDb_Dialog.setMinimumSize(QtCore.QSize(360, 330))
        MaterialDb_Dialog.setMaximumSize(QtCore.QSize(360, 330))
        MaterialDb_Dialog.setStyleSheet("*{    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 9pt \"Segoe UI\";\n"
"    background-color: rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:vertical {\n"
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
" }")
        self.verticalLayout = QtWidgets.QVBoxLayout(MaterialDb_Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CSection_groupBox = QtWidgets.QGroupBox(MaterialDb_Dialog)
        self.CSection_groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(128, 128, 128);")
        self.CSection_groupBox.setObjectName("CSection_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.CSection_groupBox)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(4, 0, 0, 6)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ComboBox = QtWidgets.QComboBox(self.CSection_groupBox)
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
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        #self.ComboBox.addItem("")
        #self.ComboBox.addItem("")
        #self.ComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.ComboBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.CSection_groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Material_tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.Material_tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Material_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Material_tableWidget.setObjectName("Material_tableWidget")
        self.Material_tableWidget.setColumnCount(0)
        self.Material_tableWidget.setRowCount(0)
        self.Material_tableWidget.horizontalHeader().setVisible(False)
        self.Material_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.Material_tableWidget)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(4, 0, 4, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.CSection_groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Properties_tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.Properties_tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Properties_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Properties_tableWidget.setObjectName("Properties_tableWidget")
        self.Properties_tableWidget.setColumnCount(0)
        self.Properties_tableWidget.setRowCount(0)
        self.Properties_tableWidget.horizontalHeader().setVisible(False)
        self.Properties_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.Properties_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.Properties_tableWidget)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addWidget(self.CSection_groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(MaterialDb_Dialog)
        self.groupBox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setContentsMargins(0, 4, 4, 4)
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
        self.OK_button.setMaximumSize(QtCore.QSize(100, 100))
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

        self.retranslateUi(MaterialDb_Dialog)
        QtCore.QMetaObject.connectSlotsByName(MaterialDb_Dialog)

    def retranslateUi(self, MaterialDb_Dialog):
        _translate = QtCore.QCoreApplication.translate
        MaterialDb_Dialog.setWindowTitle(_translate("MaterialDb_Dialog", "Add Material - Database"))
        self.CSection_groupBox.setTitle(_translate("MaterialDb_Dialog", "Database"))
        self.ComboBox.setItemText(0, _translate("MaterialDb_Dialog", "Steel (ASTM)"))
        self.ComboBox.setItemText(1, _translate("MaterialDb_Dialog", "Steel (Australia AS)"))
        self.ComboBox.setItemText(2, _translate("MaterialDb_Dialog", "Steel (BS EN)"))
        self.ComboBox.setItemText(3, _translate("MaterialDb_Dialog", "Steel (GB50017-2017)"))
        self.ComboBox.setItemText(4, _translate("MaterialDb_Dialog", "Steel (JIS G 3136)"))
        #self.ComboBox.setItemText(5, _translate("MaterialDb_Dialog", "Concrete (BS8110-1997)"))
        #self.ComboBox.setItemText(6, _translate("MaterialDb_Dialog", "Concrete (GB50010-2010)"))
        #self.ComboBox.setItemText(7, _translate("MaterialDb_Dialog", "Concrete (HKCC-2013)"))
        self.ComboBox.setItemText(5, _translate("MaterialDb_Dialog", "Aluminum (BS 8118)"))
        self.groupBox_3.setTitle(_translate("MaterialDb_Dialog", "Material name:"))
        self.groupBox_2.setTitle(_translate("MaterialDb_Dialog", "Properties"))
        self.OK_button.setText(_translate("MaterialDb_Dialog", "OK"))
        self.Cancel_pushButton.setText(_translate("MaterialDb_Dialog", "Cancel"))
