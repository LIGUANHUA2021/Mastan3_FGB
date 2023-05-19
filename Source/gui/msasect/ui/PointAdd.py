# -*- coding: utf-8 -*-

"""
Module implementing PointAdd_Dialog.
"""


from PySide6.QtCore import Slot, QTimer, QSize
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator
from PySide6.QtGui import QIntValidator

import traceback

from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.Ui_PointAdd import Ui_PointAdd_Dialog

class PointAddDialog(QDialog, Ui_PointAdd_Dialog):
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
        self.setFixedSize(self.width(), self.height()) ### Fix the size of window
        self.mw = mw
        self.initDialog()

        # QTimer.singleShot(0, self.Stress_label.deleteLater)
        # QTimer.singleShot(0, self.Stress_input.deleteLater)
        self.resize(214, 152)
        self.setMinimumSize(QSize(214, 152))
        self.setMaximumSize(QSize(214, 152))
        self.groupBox.setMinimumSize(QSize(210, 112))
        self.groupBox.setMaximumSize(QSize(210, 112))

    def initDialog(self):
        try:
            if self.mw.Centerline_radioButton.isChecked() == True:
                PointIDDict=msaModel.Point.ID
                if not PointIDDict:
                    AddId = 1
                else:
                    maxId = max(PointIDDict.keys(), key=(lambda x:x))
                    AddId = maxId + 1
                self.PointIDInput.setText(str(int(AddId)))
                ###设置validator
                doubleValidator = QDoubleValidator(bottom=-999,top=999)
                intValidator = QIntValidator()
                self.PointIDInput.setValidator(intValidator)
                self.Y_CoordInput.setValidator(doubleValidator)
                self.Z_CoordInput.setValidator(doubleValidator)
                # self.Stress_input.setValidator(doubleValidator)
            elif self.mw.Outline_radioButton.isChecked() == True:
                # self.Stress_input.setEnabled(False)
                # self.Stress_input.setStyleSheet("*{    \n"
                #                                 "    font: 9pt \"Segoe UI\";\n"
                #                                 "    color: rgb(128, 128, 128);\n"
                #                                 "    background: rgb(255, 255, 255);\n"
                #                                 "}\n"
                #                                 "")
                PointIDDict = msaFEModel.Point.ID
                if not PointIDDict:
                    AddId = 1
                else:
                    maxId = max(PointIDDict.keys(), key=(lambda x: x))
                    AddId = maxId + 1
                self.PointIDInput.setText(str(int(AddId)))
                # Set validator
                doubleValidator = QDoubleValidator(bottom=-999, top=999)
                intValidator = QIntValidator()
                self.PointIDInput.setValidator(intValidator)
                self.Y_CoordInput.setValidator(doubleValidator)
                self.Z_CoordInput.setValidator(doubleValidator)
                # self.Stress_input.setValidator(doubleValidator)
        except:
            traceback.print_exc()

    @Slot()
    def on_PointAdd_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            if len(self.Y_CoordInput.text()) == 0 or len(self.Z_CoordInput.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
                Y_CoordInput = float(self.Y_CoordInput.text())
                Z_CoordInput = float(self.Z_CoordInput.text())
                id = int(self.PointIDInput.text())
                Stress_input = 0.0
                #Stress_input = float(self.Stress_input.text())
                PointIDDict = msaModel.Point.ID
                if id in PointIDDict:
                    showMesbox(self, 'Point ID has been used!')
                else:
                    if self.mw.Centerline_radioButton.isChecked() == True:
                        msaModel.Point.Add(tID=id, ty=Y_CoordInput, tz=Z_CoordInput, tstress=Stress_input)
                    elif self.mw.Outline_radioButton.isChecked() == True:
                        msaFEModel.Point.Add(tID=id, ty=Y_CoordInput, tz=Z_CoordInput)
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
        QDialog.close(self)
