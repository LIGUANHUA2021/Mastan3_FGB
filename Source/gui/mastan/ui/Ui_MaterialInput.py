# Form implementation generated from reading ui file 'F:\Mastan3\Mastan3\Source\gui\mastan\ui\MaterialInput.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(207, 119)
        Dialog.setSizeGripEnabled(True)
        self.OKButton = QtWidgets.QToolButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(116, 86, 81, 21))
        self.OKButton.setObjectName("OKButton")
        self.E_Input = QtWidgets.QLineEdit(Dialog)
        self.E_Input.setGeometry(QtCore.QRect(84, 34, 113, 21))
        self.E_Input.setObjectName("E_Input")
        self.G_Input = QtWidgets.QLineEdit(Dialog)
        self.G_Input.setGeometry(QtCore.QRect(84, 60, 113, 21))
        self.G_Input.setObjectName("G_Input")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 34, 73, 16))
        self.label_2.setObjectName("label_2")
        self.MatID_Input = QtWidgets.QLineEdit(Dialog)
        self.MatID_Input.setGeometry(QtCore.QRect(84, 8, 113, 21))
        self.MatID_Input.setObjectName("MatID_Input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(8, 8, 81, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 25, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.MatID_Input, self.E_Input)
        Dialog.setTabOrder(self.E_Input, self.G_Input)
        Dialog.setTabOrder(self.G_Input, self.OKButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Material"))
        self.OKButton.setText(_translate("Dialog", "OK"))
        self.label_2.setText(_translate("Dialog", "E :"))
        self.label.setText(_translate("Dialog", "Macterial ID:"))
        self.label_3.setText(_translate("Dialog", "G :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
