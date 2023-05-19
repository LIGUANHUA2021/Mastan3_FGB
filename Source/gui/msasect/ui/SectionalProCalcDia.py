# -*- coding: utf-8 -*-

"""
Module implementing SectPropCal_Dialog.
"""

from PySide6.QtCore import Slot, QTime, QFileInfo
from PySide6.QtWidgets import QDialog
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QFont
import traceback
import sys
from .Ui_SectionalProCalcDia import Ui_SectPropCal_Dialog
from gui.msasect.base.Model import msaModel, msaFEModel, Status
from gui.msasect.file import IO
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.SPAnalMessageBox import SPAnalMessageBox_Dialog
from gui.msasect.base.OutputRedir import ConsoleOutput
from analysis.FESect.variables import Model


class SectPropCal_Dialog(QDialog, Ui_SectPropCal_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/SectionProperties.png'))
        self.setWindowTitle('Calculating section properties ... ')
        ##
        self.parent = mw
        self.mw = mw
        self.NewThread = None
        self.mat_ref = None
        ##
        self.StrainatMaxiStress_radioButton.setEnabled(False)
        self.StrainValue_lineEdit.setEnabled(False)
        self.StrainatValue_radioButton.setEnabled(False)
        ##
        self.UseExistingMesh_radioButton.toggled.connect(self.on_changed)
        self.AutoMesh_radioButton.toggled.connect(self.on_changed)
        self.MeshSize_radioButton.toggled.connect(self.on_changed)
        self.StrainatMaxiStress_radioButton.toggled.connect(self.on_changed)
        self.StrainatValue_radioButton.toggled.connect(self.on_changed)

        if self.mw.Centerline_radioButton.isChecked():
            if msaModel.Segment.ID:
                MatIdDict = msaModel.Mat.ID
                MatIdDict = list(MatIdDict.keys())
                for i in range(len(MatIdDict)):
                    self.Refmat_comboBox.addItem(str(MatIdDict[i]))
            self.CM_radioButton.setChecked(True)
            self.FE_radioButton.setEnabled(False)
            self.UseExistingMesh_radioButton.setEnabled(False)
            self.AutoMesh_radioButton.setEnabled(False)
            self.MeshSize_radioButton.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.UseRefMat_radioButton.setEnabled(False)
            self.Refmat_comboBox.setEnabled(False)
            self.label_2.setEnabled(False)
            self.label_3.setEnabled(False)
            self.label_4.setEnabled(False)
            self.UseDefValues_radioButton.setEnabled(False)
            self.EquivE_lineEdit.setEnabled(False)
            self.EquivPR_lineEdit.setEnabled(False)
            self.EquivDesiStrs_lineEdit.setEnabled(False)
        elif self.mw.Outline_radioButton.isChecked():
            if msaFEModel.Loop.ID:
                MatIdDict = msaFEModel.Mat.ID
                MatIdDict = list(MatIdDict.keys())
                for i in range(len(MatIdDict)):
                    self.Refmat_comboBox.addItem(str(MatIdDict[i]))
            self.FE_radioButton.setChecked(True)
            self.CM_radioButton.setEnabled(False)
            self.lineEdit.setText("10")
            if Status.Meshed:
                self.UseExistingMesh_radioButton.setChecked(True)
                self.lineEdit.setEnabled(False)
            elif msaFEModel.Group.Count:
                self.UseExistingMesh_radioButton.setEnabled(False)
                self.AutoMesh_radioButton.setChecked(True)
                self.lineEdit.setEnabled(False)
            else:
                self.UseExistingMesh_radioButton.setEnabled(False)
                self.AutoMesh_radioButton.setEnabled(False)
                self.MeshSize_radioButton.setEnabled(False)
                self.lineEdit.setEnabled(False)
            self.UseRefMat_radioButton.setChecked(True)
            self.EquivE_lineEdit.setEnabled(False)
            self.EquivPR_lineEdit.setEnabled(False)
            self.EquivDesiStrs_lineEdit.setEnabled(False)
            self.StrainatMaxiStress_radioButton.setEnabled(True)
            self.StrainatValue_radioButton.setEnabled(True)

        if self.lineEdit.isEnabled():
            self.lineEdit.setText('10')

    @Slot()
    def on_Run_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #
        try:
            if self.mw.Centerline_radioButton.isChecked():
                MatIdDictcheck = msaModel.Mat.ID
                if msaModel.Point.Count == 0 and msaModel.Segment.Count == 0:
                    showMesbox(self, 'Centerline model required!')
                    return
                if not MatIdDictcheck:
                    showMesbox(self, 'Please input material first!')
                    return
                if Status.NewFile:
                    DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", self.mw.cwd,
                                                                                  "Json Files (*.Json)")
                    if DirFileName == "":
                        self.mw.StatusOutput.setFont(QFont("Courier", 9))
                        self.mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel Calculate!")
                        return
                    else:
                        fileinfo = QFileInfo(DirFileName)
                        tfilename = fileinfo.baseName()
                        msaModel.Information.ModelName = DirFileName ## absolute FilePath
                        msaModel.FileInfo.FileName = tfilename
                        self.mw.SectNameInput_lineEdit.setText(tfilename)
                        self.mw.setWindowTitle(
                            'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + tfilename)
                        IO.CMFile.SaveDataFile(DirFileName, 2)
                        Status.NewFile = 0
                        Status.Saved = 1
                tAnaFileName = msaModel.Information.ModelName ## absolute FilePath
                if not Status.Saved:
                    IO.CMFile.SaveDataFile(tAnaFileName, 2)
                    Status.Saved = 1
                QDialog.close(self)
                Ui = SPAnalMessageBox_Dialog(self, parent=self, CM=True)
                Ui.exec()
                self.mw.StatusOutput.append(QTime.currentTime().toString() + (": The calculation process has been successfully completed."))
                Status.SP = 1
                self.mw.OutSPtoMW()
                self.mw.ResetPanel()
            elif self.mw.Outline_radioButton.isChecked():
                if self.MeshSize_radioButton.isChecked() and not self.lineEdit.text():
                    showMesbox(self, 'Please input mesh size!')
                    return
                MatIdDictcheck = msaFEModel.Mat.ID
                if msaFEModel.Group.Count == 0:
                    showMesbox(self, 'Outline model required!')
                if not MatIdDictcheck:
                    showMesbox(self, 'Please input material first!')
                    return
                else:
                    if Status.NewFile:
                        DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", self.mw.cwd,
                                                                                   "Json Files (*.Json)")
                        if DirFileName == "":
                            self.mw.StatusOutput.setFont(QFont("Courier", 9))
                            self.mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel Calculate!")
                            return
                        else:
                            fileinfo = QFileInfo(DirFileName)
                            tfilename = fileinfo.baseName()
                            msaFEModel.Information.ModelName = DirFileName  ## absolute FilePath
                            msaFEModel.FileInfo.FileName = tfilename
                            self.mw.SectNameInput_lineEdit.setText(tfilename)
                            self.mw.setWindowTitle(
                                'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + tfilename)
                            IO.FEFile.SaveDataFile(DirFileName, 2)
                            Status.NewFile = 0
                            Status.Saved = 1
                    if self.UseRefMat_radioButton.isChecked():
                        Model.Analysis.mat_ref = float(self.Refmat_comboBox.currentText())
                        Model.Analysis.E_ref = -99999
                        Model.Analysis.nu_ref = -99999
                        Model.Analysis.G_ref = -99999
                        Model.Analysis.fy_ref = -99999
                        self.mat_ref = "id"
                        tMatID = int(self.Refmat_comboBox.currentText())
                    elif self.UseDefValues_radioButton.isChecked():
                        if self.EquivE_lineEdit.text() == '' or self.EquivPR_lineEdit.text() == '' \
                                or self.EquivDesiStrs_lineEdit.text() == '':
                            showMesbox(self, 'Please input equivalent property values!')
                            return
                        else:
                            Model.Analysis.mat_ref = -99999
                            Model.Analysis.E_ref = float(self.EquivE_lineEdit.text())
                            Model.Analysis.nu_ref = float(self.EquivPR_lineEdit.text())
                            Model.Analysis.G_ref = Model.Analysis.E_ref / (2 * (1 + Model.Analysis.nu_ref))
                            Model.Analysis.fy_ref = float(self.EquivDesiStrs_lineEdit.text())
                            self.mat_ref = "value"
                            tMatID = -99999 ## Default
                    ##
                    if self.StrainatMaxiStress_radioButton.isChecked():
                        tStrnConT = 1
                    elif self.StrainatValue_radioButton.isChecked():
                        tStrnConT = 2
                    tStrnatVal = float(self.StrainValue_lineEdit.text())

                    msaFEModel.SectPAnalInfo.AddInfo(tRefMatID=tMatID, tUDE=Model.Analysis.E_ref, tUDPR=Model.Analysis.nu_ref,
                                                     tUDfy=Model.Analysis.fy_ref, tUDeu=Model.Analysis.nu_ref, tStrnConT=tStrnConT, tStrnatVal=tStrnatVal)
                    ##
                    QDialog.close(self)
                    Ui = SPAnalMessageBox_Dialog(self, parent=self)
                    Ui.exec()
                    ##
            sys.stdout = ConsoleOutput(self.mw.StatusOutput)
        except:
            traceback.print_exc()

    @staticmethod
    def PrintOmega(x1, y1, z1, x2, y2, z2):
        import matplotlib.pyplot as plt
        plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter(x1, y1, z1)
        ax.scatter(x2, y2, z2)
        plt.show()


    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # QClose()
        if self.NewThread:
            self.NewThread.terminate()
        QDialog.close(self)
        self.mw.StatusOutput.append("Section properties calculation canceled!")

    @Slot()
    def on_UseRefMat_radioButton_toggled(self):
        self.EquivE_lineEdit.setEnabled(False)
        self.EquivPR_lineEdit.setEnabled(False)
        self.EquivDesiStrs_lineEdit.setEnabled(False)
        self.Refmat_comboBox.setEnabled(True)
        return

    @Slot()
    def on_UseDefValues_radioButton_toggled(self):
        self.EquivE_lineEdit.setEnabled(True)
        self.EquivPR_lineEdit.setEnabled(True)
        self.EquivDesiStrs_lineEdit.setEnabled(True)
        self.Refmat_comboBox.setEnabled(False)
        return

    def on_changed(self):
        if self.UseExistingMesh_radioButton.isChecked() or self.AutoMesh_radioButton.isChecked():
            self.lineEdit.setEnabled(False)
        elif self.MeshSize_radioButton.isChecked():
            self.lineEdit.setEnabled(True)
        if self.StrainatMaxiStress_radioButton.isChecked():
            self.StrainValue_lineEdit.setEnabled(False)
        elif self.StrainatValue_radioButton.isChecked():
            self.StrainValue_lineEdit.setEnabled(True)
        return

    def ConResiduaStrs_changed(self):
        self.StrainatMaxiStress_radioButton.setEnabled(False)
        self.StrainatValue_radioButton.setEnabled(False)
        return
