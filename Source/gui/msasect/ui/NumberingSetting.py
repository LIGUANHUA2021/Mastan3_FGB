# -*- coding: utf-8 -*-

"""
Module implementing NumberSetting_Dialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from gui.msasect.ui.Ui_NumberingSetting import Ui_NumberSetting_Dialog
from gui.msasect.base.Model import Status

class NumberSetting_Dialog(QDialog, Ui_NumberSetting_Dialog):
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
        ##
        if Status.res_form[0] == "e":
            self.Scientific_radioButton.setChecked(True)
            self.Decimal_spinBox.setEnabled(False)
            self.Scientific_spinBox.setValue(Status.res_form[1])
            self.Decimal_spinBox.setValue(2)
        elif Status.res_form[0] == "f":
            self.Decimal_radioButton.setChecked(True)
            self.Scientific_spinBox.setEnabled(False)
            self.Decimal_spinBox.setValue(Status.res_form[1])
            self.Scientific_spinBox.setValue(4)
        self.Decimal_spinBox.setMaximum(10)
        self.Scientific_spinBox.setMaximum(10)
        ##
        self.Decimal_radioButton.toggled.connect(self.Decimalonradio_changed)
        self.Scientific_radioButton.toggled.connect(self.Scieradio_changed)

    @Slot()
    def on_Reset_pushButton_clicked(self):
        self.Scientific_radioButton.setChecked(True)
        self.Decimal_spinBox.setValue(2)
        self.Scientific_spinBox.setValue(4)


    @Slot()
    def on_OK_pushButton_clicked(self):
        if self.Decimal_radioButton.isChecked():
            tValue = self.Decimal_spinBox.value()
            Status.res_form = ["f", tValue]
            self.mw.NumberSetting = "    {:<50." + str(tValue) + "f}"
        elif self.Scientific_radioButton.isChecked():
            tValue = self.Scientific_spinBox.value()
            Status.res_form = ["e", tValue]
            self.mw.NumberSetting = "{:>" + str(10 + tValue) + "." + str(tValue) + "e}"
        ##
        self.mw.OutSPtoMW()
        QDialog.close(self)
        # print("tValue=", tValue)
        # print("NumberSetting = ", self.mw.NumberSetting)


    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

    def Decimalonradio_changed(self):
        self.Scientific_spinBox.setEnabled(False)
        self.Decimal_spinBox.setEnabled(True)

    def Scieradio_changed(self):
        self.Decimal_spinBox.setEnabled(False)
        self.Scientific_spinBox.setEnabled(True)
