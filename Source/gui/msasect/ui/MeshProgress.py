# -*- coding: utf-8 -*-

"""
Module implementing MeshProgressDialog.
"""
import gmsh
from gui.msasect.ui.msgBox import showMesbox
from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from analysis.FESect.util.MeshGen import FEMesh
from gui.msasect.base.Model import msaFEModel, Status
from gui.msasect.base.MultiThreadSetting import MultiThread

from .Ui_MeshProgress import Ui_MeshProgress_Dialog


class MeshProgress_Dialog(QDialog, Ui_MeshProgress_Dialog):
    """
    Class documentation goes here.
    """
    meshProgress_Signal = Signal(int)
    meshFinish_Signal = Signal()
    meshIter_Signal = Signal(int)
    meshText_Signal = Signal(str)
    OK_Signal = Signal()
    proceed_Signal = Signal()

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/Mesh.png'))
        self.OK_pushButton.setText("Stop")
        self.mw = parent

    def UpdateText(self, p_str):
        self.TextLabel2.setText(p_str)

    def UpdateProgress(self, p_int):
        self.progressBar.setValue(p_int)

    def UpdateIter(self, p_int):
        if p_int:
            self.TextLabel.setText("Refining iteration: {}".format(p_int))
        else:
            self.TextLabel.setText("Generating initial mesh")

    @Slot()
    def on_OK_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.OK_Signal.emit()
        if self.NewThread.isRunning():
            self.NewThread.terminate()
            self._FEMesh.text_Signal.disconnect(self.UpdateText)
            self._FEMesh.progress_Signal.disconnect(self.UpdateProgress)
            self._FEMesh.iter_Signal.disconnect(self.UpdateIter)
            self._FEMesh.finish_Signal.disconnect(self.FEMeshFinish)
            self._FEMesh.finish_Signal.disconnect(self.mw.FEMeshFinish)
            self.OK_Signal.disconnect(self.mw.FEMeshCancel)
        QDialog.close(self)

    def GetMeshSize(self, p_float):
        self.meshSize = p_float

    def StartMeshGenFE(self):
        self._FEMesh = FEMesh(self.meshProgress_Signal, self.meshFinish_Signal,
                         self.meshIter_Signal, self.meshText_Signal)
        self._FEMesh.text_Signal.connect(self.UpdateText)
        self._FEMesh.progress_Signal.connect(self.UpdateProgress)
        self._FEMesh.iter_Signal.connect(self.UpdateIter)
        self._FEMesh.finish_Signal.connect(self.FEMeshFinish)
        self._FEMesh.finish_Signal.connect(self.mw.FEMeshFinish)
        self.OK_Signal.connect(self.mw.FEMeshCancel)
        self.NewThread = MultiThread(label="Mesh", parameter={"meshSize": self.meshSize,
                                                              "msaFEModel": msaFEModel,
                                                              "FEMesh": self._FEMesh})
        self.NewThread.start()

    def FEMeshFinish(self):
        gmsh.finalize()
        self.NewThread.quit()
        self.TextLabel2.setText("The mesh generation process is completed!")
        self.OK_pushButton.setText("OK")
        self._FEMesh.text_Signal.disconnect(self.UpdateText)
        self._FEMesh.progress_Signal.disconnect(self.UpdateProgress)
        self._FEMesh.iter_Signal.disconnect(self.UpdateIter)
        self._FEMesh.finish_Signal.disconnect(self.FEMeshFinish)
        self._FEMesh.finish_Signal.disconnect(self.mw.FEMeshFinish)
        self.OK_Signal.disconnect(self.mw.FEMeshCancel)

    def closeEvent(self, event):
        if Status.Meshed:
            self.proceed_Signal.emit()
