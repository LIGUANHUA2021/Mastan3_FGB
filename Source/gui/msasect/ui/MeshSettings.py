# -*- coding: utf-8 -*-

"""
Module implementing MeshSettingDialog.
"""

from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator, QIcon

from .Ui_MeshSettings import Ui_meshSettings_Dialog

from gui.msasect.ui.msgBox import showMesbox
from analysis.FESect.variables import Model
from gui.msasect.base.Model import msaFEModel

import traceback


class meshSettings_Dialog(QDialog, Ui_meshSettings_Dialog):
    """
    Class documentation goes here.
    """
    OK_Signal = Signal(float)
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/Mesh.png'))
        self.initDialog()

    def initDialog(self):
        try:
            doubleValidator = QDoubleValidator(bottom=0, top=999)
            self.maxSizeInput_lineEdit.setValidator(doubleValidator)
            self.maxSizeInput_lineEdit.setText("10")
        except:
            traceback.print_exc()

    @Slot()
    def on_userDefined_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.maxSizeInput_lineEdit.setEnabled(True)

    @Slot()
    def on_auto_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.maxSizeInput_lineEdit.setEnabled(False)

    @Slot()
    def on_apply_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.userDefined_radioButton.isChecked():
            if not self.maxSizeInput_lineEdit.text():
                showMesbox(self, 'Please input correct data!')
            else:
                self.OK_Signal.emit(float(self.maxSizeInput_lineEdit.text()))
                self.accept()
        elif self.auto_radioButton.isChecked():
            self.OK_Signal.emit(0)
            self.accept()
        Model.Analysis.mat_ref = list(msaFEModel.Mat.ID)[0]

    @Slot()
    def on_cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        QDialog.close(self)
