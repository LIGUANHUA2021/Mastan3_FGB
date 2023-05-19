# Form implementation generated from reading ui file 'General.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_General_Dialog(object):
    def setupUi(self, General_Dialog):
        General_Dialog.setObjectName("General_Dialog")
        General_Dialog.resize(467, 384)
        General_Dialog.setStyleSheet("*{    \n"
"    font: 10pt \"Times New Roman\";\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(General_Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.General_groupBox = QtWidgets.QGroupBox(General_Dialog)
        self.General_groupBox.setMinimumSize(QtCore.QSize(0, 80))
        self.General_groupBox.setObjectName("General_groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.General_groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 451, 61))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.General_groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.General_graphicsView = QtWidgets.QGraphicsView(General_Dialog)
        self.General_graphicsView.setObjectName("General_graphicsView")
        self.horizontalLayout_2.addWidget(self.General_graphicsView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ModelingType_groupBox = QtWidgets.QGroupBox(General_Dialog)
        self.ModelingType_groupBox.setObjectName("ModelingType_groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ModelingType_groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Centerline_radioButton = QtWidgets.QRadioButton(self.ModelingType_groupBox)
        self.Centerline_radioButton.setObjectName("Centerline_radioButton")
        self.horizontalLayout_4.addWidget(self.Centerline_radioButton)
        self.Outline_radioButton = QtWidgets.QRadioButton(self.ModelingType_groupBox)
        self.Outline_radioButton.setObjectName("Outline_radioButton")
        self.horizontalLayout_4.addWidget(self.Outline_radioButton)
        self.verticalLayout_2.addWidget(self.ModelingType_groupBox)
        self.Dimension_groupBox = QtWidgets.QGroupBox(General_Dialog)
        self.Dimension_groupBox.setObjectName("Dimension_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Dimension_groupBox)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(6, 4, 6, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.ID_label = QtWidgets.QLabel(self.Dimension_groupBox)
        self.ID_label.setObjectName("ID_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ID_label)
        self.ID_inputlineEdit = QtWidgets.QLineEdit(self.Dimension_groupBox)
        self.ID_inputlineEdit.setObjectName("ID_inputlineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ID_inputlineEdit)
        self.YCoor_label = QtWidgets.QLabel(self.Dimension_groupBox)
        self.YCoor_label.setObjectName("YCoor_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.YCoor_label)
        self.YCoor_inputlineEdit = QtWidgets.QLineEdit(self.Dimension_groupBox)
        self.YCoor_inputlineEdit.setObjectName("YCoor_inputlineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.YCoor_inputlineEdit)
        self.ZCoor_label = QtWidgets.QLabel(self.Dimension_groupBox)
        self.ZCoor_label.setObjectName("ZCoor_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ZCoor_label)
        self.ZCoor_inputlineEdit = QtWidgets.QLineEdit(self.Dimension_groupBox)
        self.ZCoor_inputlineEdit.setObjectName("ZCoor_inputlineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ZCoor_inputlineEdit)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.Dimension_groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Import_pushButton = QtWidgets.QPushButton(General_Dialog)
        self.Import_pushButton.setObjectName("Import_pushButton")
        self.horizontalLayout_3.addWidget(self.Import_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(260, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.OK_button = QtWidgets.QPushButton(General_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OK_button.sizePolicy().hasHeightForWidth())
        self.OK_button.setSizePolicy(sizePolicy)
        self.OK_button.setObjectName("OK_button")
        self.horizontalLayout.addWidget(self.OK_button)
        self.Cancel_pushButton = QtWidgets.QPushButton(General_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_pushButton.sizePolicy().hasHeightForWidth())
        self.Cancel_pushButton.setSizePolicy(sizePolicy)
        self.Cancel_pushButton.setObjectName("Cancel_pushButton")
        self.horizontalLayout.addWidget(self.Cancel_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(General_Dialog)
        QtCore.QMetaObject.connectSlotsByName(General_Dialog)

    def retranslateUi(self, General_Dialog):
        _translate = QtCore.QCoreApplication.translate
        General_Dialog.setWindowTitle(_translate("General_Dialog", "General - Template"))
        self.General_groupBox.setTitle(_translate("General_Dialog", "Material"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("General_Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("General_Dialog", "Color"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("General_Dialog", "E"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("General_Dialog", "G"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("General_Dialog", "fy"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("General_Dialog", "eu"))
        self.ModelingType_groupBox.setTitle(_translate("General_Dialog", "Modeling Type"))
        self.Centerline_radioButton.setText(_translate("General_Dialog", "Centerline"))
        self.Outline_radioButton.setText(_translate("General_Dialog", "Outline"))
        self.Dimension_groupBox.setTitle(_translate("General_Dialog", "Dimension"))
        self.ID_label.setText(_translate("General_Dialog", "ID = "))
        self.YCoor_label.setText(_translate("General_Dialog", "Y-Coor = "))
        self.ZCoor_label.setText(_translate("General_Dialog", "Z-Coor = "))
        self.Import_pushButton.setText(_translate("General_Dialog", "Import"))
        self.OK_button.setText(_translate("General_Dialog", "OK"))
        self.Cancel_pushButton.setText(_translate("General_Dialog", "Cancel"))
