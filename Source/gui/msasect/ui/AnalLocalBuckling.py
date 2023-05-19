# -*- coding: utf-8 -*-

"""
Module implementing LocalBucklingAnalDialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.Ui_AnalLocalBuckling import Ui_LocalBuckling_Dialog
from analysis.FESect.util.SolidMeshGen import FEMesh
from analysis.CMSect.util.MeshGen import MeshGenCM_FSM
from analysis.FESect.variables import Model as FEModel
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.Mesh3DView import Mesh3DViewDialog


class LocalBucklingAnalDialog(QDialog, Ui_LocalBuckling_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.meshed = False
        self.unit_len = 0
        self.member_len = 0
        self.parent = parent
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/LocalBuckling.ico'))
        self.ShowResults_pushButton.setDisabled(True)
        self.FEM_radioButton.setChecked(True)
        self.FSM_radioButton.setChecked(False)
        if self.parent.Outline_radioButton.isChecked():
            self.FSM_radioButton.setEnabled(False)
            self.FSM_radioButton.setStyleSheet("*{    \n"
                                                 "    color: rgb(80, 80, 80);\n"
                                                 "}\n"
                                                 "")
        self.Max_radioButton.setChecked(True)
        self.My_label.setText('Moment (Mv) :')
        self.Mz_label.setText('Moment (Mw) :')
        self.Px_lineEdit.setText(str(1))
        self.My_lineEdit.setText(str(0))
        self.Mz_lineEdit.setText(str(0))
        self.LengthTimes_lineEdit.setText(str(3))
        self.MeshSize_lineEdit.setText(str(10))
        self.ModesNum_lineEdit.setText(str(6))
        self.ShowMesh_pushButton.setDisabled(True)
        self.Run_pushButton.setDisabled(True)
        self.ClearMesh_pushButton.setDisabled(True)

        ##
        ## Under Developing
        self.ShowResults_pushButton.setEnabled(False)

    @Slot()
    def on_GenerateMesh_pushButton_clicked(self):
        if self.parent.Centerline_radioButton.isChecked():
            width = max(msaModel.Point.Zo.values()) - min(msaModel.Point.Zo.values())
            height = max(msaModel.Point.Yo.values()) - min(msaModel.Point.Yo.values())
            if self.Width_radioButton.isChecked():
                self.unit_len = width
            elif self.Height_radioButton.isChecked():
                self.unit_len = height
            else:
                self.unit_len = max(width, height)
            self.member_len = int(self.LengthTimes_lineEdit.text()) * self.unit_len
            MeshGenCM_FSM()
        elif self.parent.Outline_radioButton.isChecked():
            width = max(msaFEModel.Point.Zo.values()) - min(msaFEModel.Point.Zo.values())
            height = max(msaFEModel.Point.Yo.values()) - min(msaFEModel.Point.Yo.values())
            if self.Width_radioButton.isChecked():
                self.unit_len = width
            elif self.Height_radioButton.isChecked():
                self.unit_len = height
            else:
                self.unit_len = max(width, height)
            self.member_len = int(self.LengthTimes_lineEdit.text()) * self.unit_len
            FEMesh().MeshGenFE(msaFEModel, self.member_len, self.unit_len / int(self.MeshSize_lineEdit.text()))
        showMesbox(self, 'Mesh Generation is completed!')
        self.meshed = True
        self.ShowMesh_pushButton.setEnabled(True)
        self.GenerateMesh_pushButton.setEnabled(False)


    @Slot()
    def on_Run_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    @Slot()
    def on_LengthTimes_lineEdit_textChanged(self):
        """
        Slot documentation goes here.
        """
        self.meshed = False
        self.ShowMesh_pushButton.setEnabled(False)
        self.GenerateMesh_pushButton.setEnabled(True)

    @Slot()
    def on_MeshSize_lineEdit_textChanged(self):
        """
        Slot documentation goes here.
        """
        self.meshed = False
        self.ShowMesh_pushButton.setEnabled(False)
        self.GenerateMesh_pushButton.setEnabled(True)


    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

    @Slot()
    def on_ShowResults_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    @Slot()
    def on_ShowMesh_pushButton_clicked(self):
        Ui = Mesh3DViewDialog(parent=self, mw=self.parent, member_len=self.member_len)
        Ui.exec()

    @Slot()
    def on_GeoAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.My_label.setText('Moment (My) :')
        self.Mz_label.setText('Moment (Mz) :')

    @Slot()
    def on_PrinAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.My_label.setText('Moment (Mv) :')
        self.Mz_label.setText('Moment (Mw) :')

