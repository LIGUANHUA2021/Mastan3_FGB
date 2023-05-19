# -*- coding: utf-8 -*-

"""
Module implementing PointAdd_Dialog.
"""


from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator

import traceback

from gui.msasect.base.Model import msaModel,msaFEModel
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.Ui_PointAdd import Ui_PointAdd_Dialog

class PointModifyDialog(QDialog, Ui_PointAdd_Dialog):
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
        self.setFixedSize(self.width(), self.height()) ### Fix the size of window
        self.setWindowTitle("Edit Point")
        self.id = id
        self.mw = mw
        self.getPointInfo(id) #get id
        self.initDialog()

    def initDialog(self):
        self.PointIDInput.setEnabled(False)
        self.PointIDInput.setStyleSheet("*{    \n"
                                      "    font: 9pt \"Segoe UI\";\n"
                                      "    color: rgb(128, 128, 128);\n"
                                      "    background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        #设置validator
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        self.Y_CoordInput.setValidator(doubleValidator)
        self.Z_CoordInput.setValidator(doubleValidator)
        #if self.mw.Outline_radioButton.isChecked() == True:
            #self.Stress_input.hide()
            #self.Stress_label.hide()

    def getPointInfo(self, id):

        if self.mw.Centerline_radioButton.isChecked() == True:
            self.PointIDInput.setText(str(id))
            self.Y_CoordInput.setText(str(msaModel.Point.Yo[id]))
            self.Z_CoordInput.setText(str(msaModel.Point.Zo[id]))
        elif self.mw.Outline_radioButton.isChecked() == True:
            self.PointIDInput.setText(str(id))
            self.Y_CoordInput.setText(str(msaFEModel.Point.Yo[id]))
            self.Z_CoordInput.setText(str(msaFEModel.Point.Zo[id]))

    @Slot()
    def on_PointAdd_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            Y_CoordInput = float(self.Y_CoordInput.text())
            Z_CoordInput = float(self.Z_CoordInput.text())
            # xDof_input = int(self.xDof_input.text())
            # yDof_input = int(self.yDof_input.text())
            # zDof_input = int(self.zDof_input.text())
            # qDof_input = int(self.qDof_input.text())
            #Stress_input = float(self.Stress_input.text())
            id = int(self.PointIDInput.text())
            # PointIDList = msaModel.Point.ID
            # if id in PointIDList:
            #     showMesbox(self, 'Point ID has been used!')
            # else:

            # msaModel.Point.Modify(tID=id, ty=Y_CoordInput, tz=Z_CoordInput, txDof=xDof_input, tyDof=yDof_input,
            #                       tzDof=zDof_input, tqDof=qDof_input, tstress=Stress_input)
            if self.mw.Centerline_radioButton.isChecked() == True:
                msaModel.Point.Modify(tID=id, ty=Y_CoordInput, tz=Z_CoordInput, tstress=0)
            elif self.mw.Outline_radioButton.isChecked() == True:
                msaFEModel.Point.Modify(tID=id, ty=Y_CoordInput, tz=Z_CoordInput)
            self.mw.ResetTable()
            self.mw.View.autoRange()
            self.accept()

        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
    @Slot()
    def on_PointAddCancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        QDialog.close(self)