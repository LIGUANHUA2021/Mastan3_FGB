# -*- coding: utf-8 -*-

"""
Module implementing MatAddDialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator, QRegularExpressionValidator
from PySide6.QtGui import QIntValidator

import traceback
from gui.msasect.ui.MaterialDb import MaterialDb_Dialog
from gui.msasect.ui.Ui_MaterialAdd import Ui_MatAddDialog
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.msgBox import showMesbox

class MatAdd_Dialog(QDialog, Ui_MatAddDialog):
    """
    Class documentation goes here.
    """

    def __init__(self, mw, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.mw = mw
        self.tMatType='S'
        self.initDialog()
        self.Law = 0
        self.Gra_Type = 0
        self.comboBox.currentIndexChanged.connect(self.Law_add)
        self.DirType_comboBox.currentIndexChanged.connect(self.Type_add)
        # self.MatType_comboBox.currentIndexChanged.connect(self.refresh_Material)

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)

        MatIdDictol = msaFEModel.Mat.ID
        if self.mw.Centerline_radioButton.isChecked() == True:
            MatIdDict = msaModel.Mat.ID
            if not MatIdDict :
                AddId = 1
            elif MatIdDict:
                maxId = max(MatIdDict.keys(), key=(lambda x:x))
                AddId = maxId + 1
        elif self.mw.Outline_radioButton.isChecked() == True:
            MatIdDictol = msaFEModel.Mat.ID
            if not MatIdDictol:
                AddId = 1
            else:
                maxId = max(MatIdDictol.keys(), key=(lambda x: x))
                AddId = maxId + 1
        self.MatIDInput.setText(str(int(AddId)))
        intValidator = QIntValidator()
        self.MatIDInput.setValidator(intValidator)
        self.E_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.Mu_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.fy_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.eu_input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.E_begin_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.E_end_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.Gra_ang_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        self.k_lineEdit.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))

        self.E_Input.setText(str(205000.0))
        self.Mu_Input.setText(str(0.3))
        self.fy_Input.setText(str(345.0))
        self.eu_input.setText(str(0.15))
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

    def Law_add(self):
        if self.comboBox.currentText() == "Power law":
            self.Law = 0
        elif self.comboBox.currentText() == "Exponential law":
            self.Law = 1
        elif self.comboBox.currentText() == "Sigmoid law":
            self.Law = 2
        elif self.comboBox.currentText() == "Power law1":
            self.Law = 3

    def Type_add(self):
        if self.DirType_comboBox.currentText() == "Single direction":
            self.Gra_Type = 0
        elif self.DirType_comboBox.currentText() == "Radial":
            self.Gra_Type = 1

    @Slot()
    def on_MaterialAdd_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        try:
            if len(self.E_Input.text()) == 0 or len(self.Mu_Input.text()) == 0 or len(self.fy_Input.text()) == 0 or\
                    len(self.E_begin_lineEdit.text()) == 0 or len(self.E_end_lineEdit.text()) == 0 or len(self.Gra_ang_lineEdit.text()) == 0 or len(self.k_lineEdit.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
                tE = float(self.E_Input.text())
                tμ = float(self.Mu_Input.text())
                tfy = float(self.fy_Input.text())
                id = int(self.MatIDInput.text())
                teu = float(self.eu_input.text())
                E_begin = float(self.E_begin_lineEdit.text())
                E_end = float(self.E_end_lineEdit.text())
                Gra_ang = float(self.Gra_ang_lineEdit.text())
                k = float(self.k_lineEdit.text())
                # print("teu = ", teu)
                MatIdDict = msaModel.Mat.ID
                # Reasonable checking
                if tE < 0.1:
                    showMesbox(self, 'Please check your input, the elastic modulus of material is toooo small!'); return
                if tμ < 0.0001:
                    showMesbox(self, "Please check your input, the Poisson's ratio of material is toooo small!"); return
                if tfy < 0.1:
                    showMesbox(self, 'Please check your input, the fy of material is toooo small!'); return
                if teu < 0.00001:
                    showMesbox(self, 'Please check your input, the limit strain of material is toooo small!'); return
                #
                if id in MatIdDict:
                    showMesbox(self, 'Material ID has been used!')
                else:
                    if self.mw.Centerline_radioButton.isChecked():
                        msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu, tType=self.tMatType, tColor='#aaffff')
                    elif self.mw.Outline_radioButton.isChecked():
                        msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu, tType=self.tMatType, tColor='#aaffff')
                        msaFEModel.Mat.Add_gra(GID=1, E_ref=1, E_begin=E_begin, E_end=E_end, Gra_ang=Gra_ang, Gra_law=self.Law,Gra_Type = self.Gra_Type, GColor='#aaffff', k= k)
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
            self.tMatType=connect['tMatType']