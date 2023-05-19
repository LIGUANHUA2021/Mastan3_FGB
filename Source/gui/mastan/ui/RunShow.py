# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback, os, sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import QDialog

import analysis.frame.Main
from gui.mastan.ui.Ui_RunShow import Ui_Dialog
from gui.mastan.base.model import msaModel
from gui.mastan.file import io, GenerateAnaFile
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.slotfunc import SlotFuncInMainWindow

class RunShowDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(RunShowDialog, self).__init__(parent)
        self.setupUi(self)
        self.initDialog()

    def initDialog(self):
        doubleValidator = QDoubleValidator(bottom=-999,top=999)
        intValidator = QIntValidator(bottom=0,top=999)
        self.LoadFactor.setValidator(doubleValidator)
        self.LoadStep.setValidator(intValidator)
        self.ErrorTolerance.setValidator(doubleValidator)
        self.MaxIterationTime.setValidator(intValidator)


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            if msaModel.FileInfo.FileName == "":
                FileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", "/")
                io.SaveDataFile(FileName)
                SlotFuncInMainWindow.FileInfo.FileName = FileName
                tFilelName = FileName.split("/")
                msaModel.FileInfo.FileName = tFilelName[len(tFilelName) - 1]
            LoadFactor = float(self.LoadFactor.text())
            LoadStep = int(self.LoadStep.text())
            ErrorTolerance = float(self.ErrorTolerance.text())
            MaxIterationTime = int(self.MaxIterationTime.text())
            AnalysisType='staticLinear' if self.comboBox.currentIndex() == 0 else 'staticNonlinear'
            msaModel.IterationInfo.Modify(tMaxIter=MaxIterationTime,tTOL=ErrorTolerance,tLoadStep=LoadStep,
                                          tLF=LoadFactor,tAnalysisType=AnalysisType)
            tAnaFileName = sys.path[1] + "\\Source\\analysis\\frame\\examples\\" + msaModel.FileInfo.FileName
            #print(tAnaFileName)
            GenerateAnaFile.GenerateAnaFile(tAnaFileName)
            #print(tAnaFileName)
            analysis.frame.Main.Run(tAnaFileName)



        except:
            traceback.print_exc()

    
    @Slot()
    def on_CancelButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.reject()
