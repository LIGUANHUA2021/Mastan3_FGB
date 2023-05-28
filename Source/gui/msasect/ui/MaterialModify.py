# -*- coding: utf-8 -*-

"""
Module implementing MatAddDialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator

import traceback

from gui.msasect.ui.MaterialDb import MaterialDb_Dialog
from gui.msasect.ui.Ui_MaterialAdd import Ui_MatAddDialog
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.msgBox import showMesbox

class MatModifyDialog(QDialog, Ui_MatAddDialog):
    """
    Class documentation goes here.
    """

    def __init__(self, mw, id, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Edit Material")
        self.mw = mw
        self.getPointInfo(id)
        self.id = id
        self.initDialog()
        self.Law = 0
        self.comboBox.currentIndexChanged.connect(self.Law_add)

        # self.MatType_comboBox.currentIndexChanged.connect(self.refresh_Material)

    def refresh_Material(self):
        # if self.MatType_comboBox.currentText() == "Steel":
            self.E_Input.setText(str(205000))
            self.Mu_Input.setText(str(0.3))
            self.fy_Input.setText(str(345))
            self.eu_input.setText(str(0.15))

            self.E_begin_lineEdit.setText(str(70000.0))
            self.E_end_lineEdit.setText(str(205000.0))
            self.Gra_ang_lineEdit.setText(str(90))
            self.k_lineEdit.setText(str(2))
        # elif self.MatType_comboBox.currentText() == "Concrete":
        #     self.E_Input.setText(str(34500))
        #     self.Mu_Input.setText(str(0.2))
        #     self.fy_Input.setText(str(42.5))
        #     self.eu_input.setText(str(0.0033))
        # elif self.MatType_comboBox.currentText() == "Rebar":
        #     self.E_Input.setText(str(205000))
        #     self.Mu_Input.setText(str(0.3))
        #     self.fy_Input.setText(str(345))
        #     self.eu_input.setText(str(0.15))
        # elif self.MatType_comboBox.currentText() == "Aluminium":
        #     self.E_Input.setText(str(70000))
        #     self.Mu_Input.setText(str(0.3))
        #     self.fy_Input.setText(str(150))
        #     self.eu_input.setText(str(0.25))
        # elif self.MatType_comboBox.currentText() == "User-defined":
        #     self.E_Input.setText(str(''))
        #     self.Mu_Input.setText(str(''))
        #     self.fy_Input.setText(str(''))
        #     self.eu_input.setText(str(''))

    def Law_add(self):
        if self.comboBox.currentText() == "Power law":
            self.Law = 0
        elif self.comboBox.currentText() == "Exponential law":
            self.Law = 1
        elif self.comboBox.currentText() == "Sigmoid law":
            self.Law = 2


    def initDialog(self):
        self.MatIDInput.setEnabled(False)
        self.MatIDInput.setStyleSheet("*{    \n"
                                      "    font: 9pt \"Segoe UI\";\n"
                                      "    color: rgb(128, 128, 128);\n"
                                      "    background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        #
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        intValidator = QIntValidator()
        self.MatIDInput.setValidator(intValidator)
        # self.E_Input.setValidator(doubleValidator)
        # self.Mu_Input.setValidator(doubleValidator)
        # self.fy_Input.setValidator(doubleValidator)
        # self.eu_input.setValidator(doubleValidator)
        self.E_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.Mu_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.fy_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.eu_input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.E_begin_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.E_end_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.Gra_ang_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.k_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.E_begin_lineEdit.setText(str(70000.0))
        self.E_end_lineEdit.setText(str(205000.0))
        self.Gra_ang_lineEdit.setText(str(90))
        self.k_lineEdit.setText(str(2))

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = MaterialDb_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.OKsignal.connect(self.get_dialog_signal)
        Ui.exec()

    def getPointInfo(self, id):
        if self.mw.Centerline_radioButton.isChecked() == True:
            self.MatIDInput.setText(str(id))
            self.E_Input.setText(str(msaModel.Mat.E[id]))
            self.Mu_Input.setText(str(msaModel.Mat.nu[id]))
            self.fy_Input.setText(str(msaModel.Mat.Fy[id]))
            self.eu_input.setText(str(msaModel.Mat.eu[id]))
            print("Current mattype = ", msaModel.Mat.Type[id])
            # if msaModel.Mat.Type[id] == "S":
            #     TCurrMatTypeIndex = 0
            # elif msaModel.Mat.Type[id] == "C":
            #     TCurrMatTypeIndex = 1
            # elif msaModel.Mat.Type[id] == "R":
            #     TCurrMatTypeIndex = 2
            # elif msaModel.Mat.Type[id] == "A":
            #     TCurrMatTypeIndex = 3
            # elif msaModel.Mat.Type[id] == "UD":
            #     TCurrMatTypeIndex = 4
            #self.MatType_comboBox.setCurrentIndex(TCurrMatTypeIndex)

        elif self.mw.Outline_radioButton.isChecked() == True:
            self.MatIDInput.setText(str(id))
            self.E_Input.setText(str(msaFEModel.Mat.E[id]))
            self.Mu_Input.setText(str(msaFEModel.Mat.nu[id]))
            self.fy_Input.setText(str(msaFEModel.Mat.Fy[id]))
            self.eu_input.setText(str(msaFEModel.Mat.eu[id]))
            if msaFEModel.Mat.Type[id] == "S":
                TCurrMatTypeIndex = 0
            elif msaFEModel.Mat.Type[id] == "C":
                TCurrMatTypeIndex = 1
            elif msaFEModel.Mat.Type[id] == "R":
                TCurrMatTypeIndex = 2
            elif msaFEModel.Mat.Type[id] == "A":
                TCurrMatTypeIndex = 3
            elif msaFEModel.Mat.Type[id] == "UD":
                TCurrMatTypeIndex = 4
            #self.MatType_comboBox.setCurrentIndex(TCurrMatTypeIndex)

    @Slot()
    def on_MaterialAdd_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        try:
            tE = float(self.E_Input.text())
            tnu = float(self.Mu_Input.text())
            tfy = float(self.fy_Input.text())
            id = int(self.MatIDInput.text())
            teu = float(self.eu_input.text())
            E_begin = float(self.E_begin_lineEdit.text())
            E_end = float(self.E_end_lineEdit.text())
            Gra_ang = float(self.Gra_ang_lineEdit.text())
            k = float(self.k_lineEdit.text())
            tMatTypeIndex = "S"
            tCMatType = "S"
            # if tMatTypeIndex == 0:
            #     tCMatType = "S"
            # elif tMatTypeIndex == 1:
            #     tCMatType = "C"
            # elif tMatTypeIndex == 2:
            #     tCMatType = "R"
            # elif tMatTypeIndex == 3:
            #     tCMatType = "A"
            # elif tMatTypeIndex == 4:
            #     tCMatType = "UD"
            #
            # MatIdList = msaModel.Mat.ID
            # if id in MatIdList:
            #     showMesbox(self, 'Material ID has been used!')
            # else:
            # Reasonable checking
            if tE < 0.1: showMesbox(self,
                                    'Please check your input, the elastic modulus of material is toooo small!'); return
            if tnu < 0.0001: showMesbox(self,
                                       "Please check your input, the Poisson's ratio of material is toooo small!"); return
            if tfy < 0.1: showMesbox(self, 'Please check your input, the fy of material is toooo small!'); return
            if teu < 0.00001: showMesbox(self,
                                         'Please check your input, the limit strain of material is toooo small!'); return
            #
            if self.mw.Centerline_radioButton.isChecked() == True:
                msaModel.Mat.Modify(tID=id, tE=tE, tnu=tnu, tFy=tfy, teu=teu, tType=tCMatType)
            elif self.mw.Outline_radioButton.isChecked() == True:
                msaFEModel.Mat.Modify_gra(GID=1, E_ref=1, E_begin=E_begin, E_end=E_end, Gra_ang=Gra_ang, Gra_law=self.Law,k=k)
                msaFEModel.Mat.Modify(tID=id, tE=tE, tnu=tnu, tFy=tfy, teu=teu, tType=tCMatType)
            self.mw.ResetTable()
            self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
    @Slot()
    def on_MatchAddCancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

    def get_dialog_signal(self, connect):
        if connect!= {}:
            self.E_Input.setText(str(connect['E']))
            self.Mu_Input.setText(str(connect['u']))
            self.fy_Input.setText(str(connect['fy']))
            self.eu_input.setText(str(connect['eu']))
            # if connect['tMatType']=="S":
            #     self.MatType_comboBox.setCurrentIndex(0)
            # elif connect['tMatType']=="C":
            #     self.MatType_comboBox.setCurrentIndex(1)
            # elif connect['tMatType']=="R":
            #     self.MatType_comboBox.setCurrentIndex(2)
            # elif connect['tMatType']=="A":
            #     self.MatType_comboBox.setCurrentIndex(3)