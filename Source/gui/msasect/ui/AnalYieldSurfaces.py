# -*- coding: utf-8 -*-

"""
Module implementing YieldSurfacesAnal_Dialog.
"""
import traceback
import os, time, codecs, sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, QFileInfo, Signal, QTime
from PySide6.QtWidgets import QDialog, QTextEdit, QTextBrowser, QMessageBox
from PySide6.QtGui import QDoubleValidator, QIntValidator, QFont, QTextOption, QIcon, QTextCharFormat, Qt, QFontDatabase, QTextCursor
##
from gui.msasect.ui.Ui_AnalYieldSurfaces import Ui_YieldSurfaces_Dialog
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.file import IO
from gui.msasect.ui.CalYSurfaceProgress import CalYSProgress
from gui.msasect.ui.ShowResultsYieldS import ShowResultsYS_Dialog
from gui.msasect.ui.ShowResultsYieldS2D import ShowResultsYS2D_Dialog
from gui.msasect.ui.YSAnalMessageBox import YSAnalMessageBox_Dialog
from gui.msasect.file import WelcomeInfo
from gui.msasect.base.OutputRedir import ConsoleOutput
from gui.msasect.base.Model import Status
##
from analysis.CMSect import Main as CMMain
from analysis.FESect import Main as FEMain
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties as FESectProperty
from analysis.FESect.variables import Model as FEModel

### for testing
# import pandas as pd

class YieldSurfacesAnal_Dialog(QDialog, Ui_YieldSurfaces_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, mw, parent):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("ui/ico/YieldSurface.ico"))
        self.cwd = os.getcwd()
        self.mw = mw
        self.initDialog()
        ##
        self.FYSPMyMz_radioButton.toggled.connect(self.ShowResultsSetting)
        self.PYSPMy_radioButton.toggled.connect(self.ShowResultsSetting)
        self.PYSMyMz_radioButton.toggled.connect(self.ShowResultsSetting)
        self.PYSPMz_radioButton.toggled.connect(self.ShowResultsSetting)
        self.UseExistingMesh_radioButton.toggled.connect(self.on_changed)
        self.AutoMesh_radioButton.toggled.connect(self.on_changed)
        self.MeshSize_radioButton.toggled.connect(self.on_changed)
        ## Strain Controling
        self.SRUS_radioButton.toggled.connect(self.ShowResultsSetting)
        self.SOMS_radioButton.toggled.connect(self.ShowResultsSetting)
        self.LStrainValue_radioButton.toggled.connect(self.ShowResultsSetting)
        # self.YS_textBrowser.setFont(QFont('Courier', 9))
        ##
        self.LStrain_Input.textChanged.connect(self.on_textchanged)
        self.NumALoad_Inoput.textChanged.connect(self.on_textchanged)
        self.NumInclinedAngle_Input.textChanged.connect(self.on_textchanged)
        self.MaxNumIteration_Input.textChanged.connect(self.on_textchanged)
        self.ConvergenceTol_Input.textChanged.connect(self.on_textchanged)
        #

        self.CalYieldSProgressUi = CalYSProgress()
        self.ShowResults_pushButton.setDisabled(True)

        if self.mw.Centerline_radioButton.isChecked():
            YieldSAnalResults = CMYieldSAnalResults
            if Status.Meshed:
                self.UseExistingMesh_radioButton.setChecked(True)
                self.AutoMesh_radioButton.setEnabled(False)
                self.MeshSize_radioButton.setEnabled(False)
                self.lineEdit.setEnabled(False)
            elif msaModel.Segment.Count:
                self.UseExistingMesh_radioButton.setEnabled(False)
                self.AutoMesh_radioButton.setChecked(True)
                self.MeshSize_radioButton.setEnabled(False)
                self.lineEdit.setEnabled(False)
            else:
                self.UseExistingMesh_radioButton.setEnabled(False)
                self.AutoMesh_radioButton.setEnabled(False)
                self.MeshSize_radioButton.setEnabled(False)
                self.lineEdit.setEnabled(False)
        elif self.mw.Outline_radioButton.isChecked():
            YieldSAnalResults = FEYieldSAnalResults
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

        ##
        if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy)>0 and len(YieldSAnalResults.OMz)>0 and YieldSAnalResults.StrnContlType==0:
            self.ShowResults_pushButton.setDisabled(False)
            if self.mw.Centerline_radioButton.isChecked():
                self.LStrain_Input.setText(str(msaModel.YieldSurfaceAnalInfo.StrainAtValue))
                self.NumALoad_Inoput.setText(str(2*msaModel.YieldSurfaceAnalInfo.PosNStep))
                self.NumInclinedAngle_Input.setText(str(msaModel.YieldSurfaceAnalInfo.MStep))
                self.MaxNumIteration_Input.setText(str(msaModel.YieldSurfaceAnalInfo.MaxNumIter))
                self.ConvergenceTol_Input.setText(str(msaModel.YieldSurfaceAnalInfo.ConvTol))
            else:
                self.LStrain_Input.setText(str(msaFEModel.YieldSurfaceAnalInfo.StrainAtValue))
                self.NumALoad_Inoput.setText(str(2*msaFEModel.YieldSurfaceAnalInfo.PosNStep))
                self.NumInclinedAngle_Input.setText(str(msaFEModel.YieldSurfaceAnalInfo.MStep))
                self.MaxNumIteration_Input.setText(str(msaFEModel.YieldSurfaceAnalInfo.MaxNumIter))
                self.ConvergenceTol_Input.setText(str(msaFEModel.YieldSurfaceAnalInfo.ConvTol))
                return
        else:
            self.ShowResults_pushButton.setDisabled(True)

        self.SRUS_radioButton.setChecked(True)
        self.SRUS_radioButton.setEnabled(True)
        self.SOMS_radioButton.setEnabled(True)
        self.LStrainValue_radioButton.setEnabled(True)
        self.LStrain_Input.setEnabled(False)

        if self.lineEdit.isEnabled():
            self.lineEdit.setText('10')

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        # Setting validator
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        intValidator = QIntValidator()
        self.LStrain_Input.setValidator(doubleValidator)
        self.NumInclinedAngle_Input.setValidator(intValidator)
        self.NumALoad_Inoput.setValidator(intValidator)
        self.MaxNumIteration_Input.setValidator(intValidator)
        self.ConvergenceTol_Input.setValidator(doubleValidator)
        self.setFixedSize(self.width(), self.height())
        ##
        tYSInfo = WelcomeInfo.Welcome.PrintYieldSurfaceInfo(self)
        # self.YS_textBrowser.setFont(QFont('Courier', 9))
        # self.YS_textBrowser.setText(tYSInfo)
        ##
        ##
    def ShowResultsSetting(self):
        if self.LStrainValue_radioButton.isChecked():
            self.LStrain_Input.setEnabled(True)
        else:
            self.LStrain_Input.setEnabled(False)
        if Status.YS:
            if self.mw.Centerline_radioButton.isChecked():
                YieldSAnalResults = CMYieldSAnalResults
            else:
                YieldSAnalResults = FEYieldSAnalResults
            ##
            tStrnContlType = YieldSAnalResults.StrnContlType
            tPMyStrnContlType = YieldSAnalResults.PMy_StrnContlType
            tPMzStrnContlType = YieldSAnalResults.PMz_StrnContlType
            tMyMzStrnContlType = YieldSAnalResults.MyMz_StrnContlType
            # print("tStrnContlType=",tStrnContlType)
            # print("tPMyStrnContlType=", tPMyStrnContlType)
            if self.FYSPMyMz_radioButton.isChecked() and self.SRUS_radioButton.isChecked():
                if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy) > 0 and len(YieldSAnalResults.OMz) > 0 and tStrnContlType==0:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.FYSPMyMz_radioButton.isChecked() and self.SOMS_radioButton.isChecked():
                if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy) > 0 and len(YieldSAnalResults.OMz) > 0 and tStrnContlType==1:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.FYSPMyMz_radioButton.isChecked() and self.LStrainValue_radioButton.isChecked():
                if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy) > 0 and len(YieldSAnalResults.OMz) > 0 and tStrnContlType==2:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ###############################
            if self.PYSPMy_radioButton.isChecked() and self.SRUS_radioButton.isChecked():
                if len(YieldSAnalResults.ONx_y) > 0 and len(YieldSAnalResults.OMy_x) > 0 and tPMyStrnContlType == 0:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.PYSPMy_radioButton.isChecked() and self.SOMS_radioButton.isChecked():
                if len(YieldSAnalResults.ONx_y) > 0 and len(YieldSAnalResults.OMy_x) > 0 and tPMyStrnContlType == 1:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.PYSPMy_radioButton.isChecked() and self.LStrainValue_radioButton.isChecked():
                if len(YieldSAnalResults.ONx_y) > 0 and len(YieldSAnalResults.OMy_x) > 0 and tPMyStrnContlType == 2:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ###############################
            if self.PYSMyMz_radioButton.isChecked() and self.SRUS_radioButton.isChecked():
                if len(YieldSAnalResults.OMy_z) > 0 and len(YieldSAnalResults.OMz_y) > 0 and tMyMzStrnContlType==0:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.PYSMyMz_radioButton.isChecked() and self.SOMS_radioButton.isChecked():
                if len(YieldSAnalResults.OMy_z) > 0 and len(YieldSAnalResults.OMz_y) > 0 and tMyMzStrnContlType==1:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.PYSMyMz_radioButton.isChecked() and self.LStrainValue_radioButton.isChecked():
                if len(YieldSAnalResults.OMy_z) > 0 and len(YieldSAnalResults.OMz_y) > 0 and tMyMzStrnContlType==2:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ###############################
            if self.PYSPMz_radioButton.isChecked() and self.SRUS_radioButton.isChecked():
                if len(YieldSAnalResults.ONx_z) > 0 and len(YieldSAnalResults.OMz_x) > 0 and tPMzStrnContlType==0:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.PYSPMz_radioButton.isChecked() and self.SOMS_radioButton.isChecked():
                if len(YieldSAnalResults.ONx_z) > 0 and len(YieldSAnalResults.OMz_x) > 0 and tPMzStrnContlType==1:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.PYSPMz_radioButton.isChecked() and self.LStrainValue_radioButton.isChecked():
                if len(YieldSAnalResults.ONx_z) > 0 and len(YieldSAnalResults.OMz_x) > 0 and tPMzStrnContlType==2:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
        else:
            self.ShowResults_pushButton.setDisabled(True)

    def FYSPMyMz_radio_changed(self):
        if self.mw.Centerline_radioButton.isChecked():
            YieldSAnalResults = CMYieldSAnalResults
        else:
            YieldSAnalResults = FEYieldSAnalResults
        ##
        tStrnContlType = YieldSAnalResults.StrnContlType
        if self.SRUS_radioButton.isChecked():
            if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy) > 0 and len(YieldSAnalResults.OMz) > 0 and tStrnContlType==0:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        elif self.SOMS_radioButton.isChecked():
            if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy) > 0 and len(YieldSAnalResults.OMz) > 0 and tStrnContlType==1:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        else:
            if len(YieldSAnalResults.ONx) > 0 and len(YieldSAnalResults.OMy) > 0 and len(YieldSAnalResults.OMz) > 0 and tStrnContlType==2:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)


    def PYSPMy_radio_changed(self):
        if self.mw.Centerline_radioButton.isChecked():
            YieldSAnalResults = CMYieldSAnalResults
        else:
            YieldSAnalResults = FEYieldSAnalResults
        ##
        tStrnContlType = YieldSAnalResults.PMy_StrnContlType
        if self.SRUS_radioButton.isChecked():
            if len(YieldSAnalResults.ONx_y) > 0 and len(YieldSAnalResults.OMy_x) > 0 and tStrnContlType==0:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        elif self.SOMS_radioButton.isChecked():
            if len(YieldSAnalResults.ONx_y) > 0 and len(YieldSAnalResults.OMy_x) > 0 and tStrnContlType==1:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        else:
            if len(YieldSAnalResults.ONx_y) > 0 and len(YieldSAnalResults.OMy_x) > 0 and tStrnContlType==2:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)

    def PYSMyMz_radio_changed(self):
        if self.mw.Centerline_radioButton.isChecked():
            YieldSAnalResults = CMYieldSAnalResults
        else:
            YieldSAnalResults = FEYieldSAnalResults
        ##
        tStrnContlType = YieldSAnalResults.MyMz_StrnContlType
        if self.SRUS_radioButton.isChecked():
            if len(YieldSAnalResults.OMy_z) > 0 and len(YieldSAnalResults.OMz_y) > 0 and tStrnContlType==0:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        elif self.SOMS_radioButton.isChecked():
            if len(YieldSAnalResults.OMy_z) > 0 and len(YieldSAnalResults.OMz_y) > 0 and tStrnContlType==1:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        else:
            if len(YieldSAnalResults.OMy_z) > 0 and len(YieldSAnalResults.OMz_y) > 0 and tStrnContlType==2:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)

    def PYSPMz_radio_changed(self):
        if self.mw.Centerline_radioButton.isChecked():
            YieldSAnalResults = CMYieldSAnalResults
        else:
            YieldSAnalResults = FEYieldSAnalResults
        ##
        tStrnContlType = YieldSAnalResults.PMz_StrnContlType
        if self.SRUS_radioButton.isChecked():
            if len(YieldSAnalResults.ONx_z) > 0 and len(YieldSAnalResults.OMz_x) > 0 and tStrnContlType==0:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        elif self.SOMS_radioButton.isChecked():
            if len(YieldSAnalResults.ONx_z) > 0 and len(YieldSAnalResults.OMz_x) > 0 and tStrnContlType==1:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        else:
            if len(YieldSAnalResults.ONx_z) > 0 and len(YieldSAnalResults.OMz_x) > 0 and tStrnContlType==2:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)

    def SRUS_radio_changed(self):
        self.SRUS_radioButton.isChecked()

    def SOMS_radio_changed(self):
        self.SOMS_radioButton.isChecked()
    def LStrainValue_radio_changed(self):
        self.LStrainValue_radioButton.isChecked()

    @Slot()
    def on_Run_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            if self.mw.Centerline_radioButton.isChecked():
                if (not msaModel.Point.ID and not msaModel.Segment.ID) and (
                        not msaFEModel.Point.ID and not msaFEModel.Outline.ID):
                    showMesbox(self, "Cannot perform action until a model has been created.\nPlease create a model first and try again.")
                    return
                ## =========================================================================================================

                if len(self.LStrain_Input.text()) == 0 or len(self.NumInclinedAngle_Input.text()) == 0 or len(
                        self.NumALoad_Inoput.text()) == 0 \
                        or len(self.MaxNumIteration_Input.text()) == 0 or len(self.ConvergenceTol_Input.text()) == 0:
                    # print("Test length = ", len(self.LStrain_Input.text()))
                    showMesbox(self, 'Please input correct data!')
                else:
                    if self.SRUS_radioButton.isChecked():
                        tBStrainControl = 0
                    elif self.SOMS_radioButton.isChecked():
                        tBStrainControl = 1
                    elif self.LStrainValue_radioButton.isChecked():
                        tBStrainControl = 2
                    ##
                    tLStrain = float(self.LStrain_Input.text())
                    temp_NumIncAng = int(self.NumInclinedAngle_Input.text())
                    ##-----------------------------------------------------------------------------------------------
                    remainder = temp_NumIncAng % 4
                    if remainder == 0:
                        tNumIncAng = temp_NumIncAng
                    else:
                        tnum1 = (temp_NumIncAng // 4) * 4  # The next number less than or equal to num and divisible by 4
                        tNumIncAng = int(tnum1 + 4)  # The next number that is greater than num and divisible by 4
                    ##-----------------------------------------------------------------------------------------------
                    tempNumAL = int(self.NumALoad_Inoput.text())
                    tNumAL = int((tempNumAL+1)/2)
                    tMaxNumIter = int(self.MaxNumIteration_Input.text())
                    tConvTol = float(self.ConvergenceTol_Input.text())
                    if tNumAL < 5 or tNumIncAng < 16 or tConvTol > 0.2:  ## Analysis paramenteries default setting
                        showMesbox(self,
                                   'Please review your input data, as it may yield unreasonable or incorrect results.')
                        return
                    msaModel.YieldSurfaceAnalInfo().AddInfo(tLimitStrain=tLStrain, tBStrainControl=tBStrainControl,tNumALoad=tNumAL,
                                                            tNumIncldAng=tNumIncAng, tMaxNumIter=tMaxNumIter,
                                                            tConvTol=tConvTol)
                    if self.UsedefinedAxis_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.AxisSlctn = 1
                    else:
                        msaModel.YieldSurfaceAnalInfo.AxisSlctn = 2
                    ##
                    if self.SRUS_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.BStrainControl = 0
                    elif self.SOMS_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.BStrainControl = 1
                    elif self.LStrainValue_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.BStrainControl = 2
                    ##
                    if self.FYSPMyMz_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.SubAnalType = 1
                    elif self.PYSPMy_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.SubAnalType = 2
                    elif self.PYSMyMz_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.SubAnalType = 3
                    elif self.PYSPMz_radioButton.isChecked():
                        msaModel.YieldSurfaceAnalInfo.SubAnalType = 4

                    if msaModel.FileInfo.FileName == "":
                        DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", self.cwd,
                                                                                      "Json Files (*.Json)")
                        if DirFileName == "":
                            self.mw.StatusOutput.setFont(QFont("Courier", 9))
                            self.mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel save file!")
                            self.mw.View.autoRange()
                            return
                        else:
                            fileinfo = QFileInfo(DirFileName)
                            tfilename = fileinfo.baseName()
                            msaModel.Information.ModelName = DirFileName  ## absolute FilePath
                            msaModel.FileInfo.FileName = tfilename
                            IO.CMFile.SaveDataFile(DirFileName, 2)
                            self.mw.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections-' + tfilename)
                            ##
                            CMMain.Run(1, DirFileName)
                        # SlotFuncInMainWindow.SaveFile(self.mw, 2)
                    #
                    tAnaFileName = msaModel.Information.ModelName  ## absolute FilePath
                    IO.CMFile.SaveDataFile(tAnaFileName, 2)
                    Status.NewFile = 0
                    Status.Saved = 1
                    QDialog.close(self)
                    Ui = YSAnalMessageBox_Dialog(self, parent=self)
                    Ui.exec()

            elif self.mw.Outline_radioButton.isChecked():
                if (not msaFEModel.Point.ID and not msaFEModel.Outline.ID):
                    showMesbox(self, "There is no data in present model, please create a model firstly!")
                    return
                if self.MeshSize_radioButton.isChecked() and not self.lineEdit.text():
                    showMesbox(self, 'Please input mesh size!')
                    return
                ## =========================================================================================================

                if len(self.LStrain_Input.text()) == 0 or len(self.NumInclinedAngle_Input.text()) == 0 or len(
                        self.NumALoad_Inoput.text()) == 0 \
                        or len(self.MaxNumIteration_Input.text()) == 0 or len(self.ConvergenceTol_Input.text()) == 0:
                    # print("Test length = ", len(self.LStrain_Input.text()))
                    showMesbox(self, 'Please input correct data!')
                else:
                    ##
                    if self.SRUS_radioButton.isChecked():
                        tBStrainControl = 0
                    elif self.SOMS_radioButton.isChecked():
                        tBStrainControl = 1
                    elif self.LStrainValue_radioButton.isChecked():
                        tBStrainControl = 2
                    msaFEModel.YieldSurfaceAnalInfo.BStrainControl = tBStrainControl
                    print("msaFEModel.YieldSurfaceAnalInfo.BStrainControl = "+f"{msaFEModel.YieldSurfaceAnalInfo.BStrainControl}")
                    ##
                    tLStrain = float(self.LStrain_Input.text())
                    temp_NumIncAng = int(self.NumInclinedAngle_Input.text())
                    ##-----------------------------------------------------------------------------------------------
                    remainder = temp_NumIncAng % 4
                    if remainder == 0:
                        tNumIncAng = temp_NumIncAng
                    else:
                        tnum1 = (
                                            temp_NumIncAng // 4) * 4  # The next number less than or equal to num and divisible by 4
                        tNumIncAng = int(tnum1 + 4)  # The next number that is greater than num and divisible by 4
                    ##-----------------------------------------------------------------------------------------------
                    tempNumAL = int(self.NumALoad_Inoput.text())
                    tNumAL = int((tempNumAL+1) / 2)
                    tMaxNumIter = int(self.MaxNumIteration_Input.text())
                    tConvTol = float(self.ConvergenceTol_Input.text())
                    if tNumAL < 5 or tNumIncAng < 16 or tConvTol > 0.2:  ## Analysis paramenteries default setting
                        showMesbox(self,
                                   'Please review your input data, as it may yield unreasonable or incorrect results.')
                        return
                    msaFEModel.YieldSurfaceAnalInfo.AddInfo(tLimitStrain=tLStrain, tBStrainControl=tBStrainControl,tNumALoad=tNumAL,
                                                            tNumIncldAng=tNumIncAng, tMaxNumIter=tMaxNumIter,
                                                            tConvTol=tConvTol)
                    FEModel.YieldSurfaceAnalInfo.get_info([msaFEModel.YieldSurfaceAnalInfo.PosNStep,
                                                           msaFEModel.YieldSurfaceAnalInfo.NegNStep,
                                                           msaFEModel.YieldSurfaceAnalInfo.MStep,
                                                           msaFEModel.YieldSurfaceAnalInfo.MaxNumIter,
                                                           msaFEModel.YieldSurfaceAnalInfo.ConvTol,
                                                           msaFEModel.YieldSurfaceAnalInfo.StrainAtValue,
                                                           msaFEModel.YieldSurfaceAnalInfo.BStrainControl,
                                                           msaFEModel.YieldSurfaceAnalInfo.SubAnalType,
                                                           msaFEModel.YieldSurfaceAnalInfo.AxisSlctn])
                    ## Calling calculate procedure from calculate engineer
                    if self.UsedefinedAxis_radioButton.isChecked():
                        FEModel.YieldSurfaceAnalInfo.AxisSlctn = 1
                    else:
                        FEModel.YieldSurfaceAnalInfo.AxisSlctn = 2
                    ##
                    if self.FYSPMyMz_radioButton.isChecked():
                        FEModel.YieldSurfaceAnalInfo.SubAnalType = 1
                    elif self.PYSPMy_radioButton.isChecked():
                        FEModel.YieldSurfaceAnalInfo.SubAnalType = 2
                    elif self.PYSMyMz_radioButton.isChecked():
                        FEModel.YieldSurfaceAnalInfo.SubAnalType = 3
                    elif self.PYSPMz_radioButton.isChecked():
                        FEModel.YieldSurfaceAnalInfo.SubAnalType = 4

                    if msaFEModel.FileInfo.FileName == "" or msaFEModel.Information.ModelName == "":

                        DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", self.cwd,
                                                                                      "Json Files (*.Json)")
                        if DirFileName == "":
                            self.mw.StatusOutput.setFont(QFont("Courier", 9))
                            self.mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel save file!")
                            self.mw.View.autoRange()
                            return
                        else:
                            fileinfo = QFileInfo(DirFileName)
                            tfilename = fileinfo.baseName()
                            msaFEModel.Information.ModelName = DirFileName  ## absolute FilePath
                            msaFEModel.FileInfo.FileName = tfilename
                            IO.FEFile.SaveDataFile(DirFileName, 2)
                            self.mw.setWindowTitle(
                                'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections-' + tfilename)
                            FEModel.OutResult.ReadOutResult(msaFEModel.FileInfo.FileName,
                                                            os.path.dirname(msaFEModel.Information.ModelName))
                    tAnaFileName = msaFEModel.Information.ModelName  ## absolute FilePath
                    IO.FEFile.SaveDataFile(tAnaFileName, 2)
                    Status.NewFile = 0
                    Status.Saved = 1
                    tfilename = msaFEModel.FileInfo.FileName
                    FEModel.OutResult.ReadOutResult(tfilename, os.path.dirname(tAnaFileName))
                    #### For testing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # FEMain.Run(2)
                    ####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    QDialog.close(self)
                    Ui = YSAnalMessageBox_Dialog(self, parent=self)
                    Ui.exec()

            sys.stdout = ConsoleOutput(self.mw.StatusOutput)


        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
        ##
        # Ui = ShowResultsYS_Dialog(self)
        # Ui.exec()
        # self.close()

    class Runthread_Log(QtCore.QThread):
        #
        _signal = Signal(str)

        def __init__(self, YS_Dia):
            super().__init__()
            self.YS_Dia = YS_Dia

        def __del__(self):
            self.wait()

        def run(self):
            #if YieldSurfacesAnal_Dialog(Ui_MainWindow).mw.Centerline_radioButton.isChecked():
            if self.YS_Dia.Centerline_radioButton.isChecked():
                tAnaFileName = msaModel.Information.ModelName
                filename = msaModel.FileInfo.FileName
            else:
                tAnaFileName = msaFEModel.Information.ModelName
                filename = msaFEModel.FileInfo.FileName
            logger_path = tAnaFileName + '.rst/' + filename + '.Json.log'
            # f = codecs.open(logger_path, 'r', 'utf-8')
            # f = open(logger_path, 'r')
            with open(logger_path, 'r') as f:
                while 1:
                    where = f.tell()
                    line = f.readline()
                    if not line:
                        time.sleep(1)
                        f.seek(where)
                    else:
                        self._signal.emit(line)

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # try:
        #     self.NewThread.quit()
        # except AttributeError:
        #     print()
        try:
            if self.NewThread.isRunning():
                self.NewThread.terminate()
            else:
                self.NewThread.quit()
        except AttributeError:
            print()
        ##
        QDialog.close(self)

    @Slot()
    def on_ShowResults_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        QDialog.close(self)
        if self.FYSPMyMz_radioButton.isChecked():
            Ui = ShowResultsYS_Dialog(self, parent=self)
            Ui.exec()
        else:
            Ui = ShowResultsYS2D_Dialog(self, parent=self)
            Ui.exec()

    @Slot()
    def on_PrincipalAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.FYSPMyMz_radioButton.setText("Full Yield Surface (P-Mv-Mw)")
        self.PYSPMy_radioButton.setText("Planar Yield Surface (P-Mv)")
        self.PYSMyMz_radioButton.setText("Planar Yield Surface (Mv-Mw)")
        self.PYSPMz_radioButton.setText("Planar Yield Surface (P-Mw)")

    @Slot()
    def on_UsedefinedAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.FYSPMyMz_radioButton.setText("Full Yield Surface (P-My-Mz)")
        self.PYSPMy_radioButton.setText("Planar Yield Surface (P-My)")
        self.PYSMyMz_radioButton.setText("Planar Yield Surface (My-Mz)")
        self.PYSPMz_radioButton.setText("Planar Yield Surface (P-Mz)")

    @Slot()
    def on_OK_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        QDialog.close(self)
        if self.FYSPMyMz_radioButton.isChecked():
            Ui = ShowResultsYS_Dialog(self, parent=self)
            Ui.exec()
        else:
            Ui = ShowResultsYS2D_Dialog(self, parent=self)
            Ui.exec()

        # self.close()

    @Slot()
    def on_Stop_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        try:
            if self.NewThread.isRunning():
                self.NewThread.terminate()
        except AttributeError:
            print()
        ##
        QDialog.close(self)

    # @Slot()
    # def on_YS_textBrowser_textChanged(self):
    #     self.YS_textBrowser.moveCursor(QTextCursor.End)
        # self.YS_textBrowser.ensureCursorVisible()
        # cursor = self.YS_textBrowser.textCursor()
        # pos = len(self.YS_textBrowser.toPlainText())
        # cursor.setPosition(pos)
        # self.YS_textBrowser.setTextCursor(cursor)
        # font = QFont("Monospace")
        #
        # # Set the font size
        # font.setPointSize(9)
        # # Set the font in the QTextBrowser
        # self.YS_textBrowser.setFont(font)
        #
        # # Set the line spacing to be 1 (single spaced)
        # # 创建QTextOption对象
        # text_option = QTextOption()
        # # 设置Tab键的长度为100个像素
        # text_option.setTabArray([100])
        #
        # # 设置QTextBrowser的属性
        # text_browser = QTextBrowser()
        # text_browser.setFontFamily("Courier New")  # 设置等宽字体
        # text_browser.document().setDefaultTextOption(text_option)
    def on_textchanged(self):
        self.ShowResults_pushButton.setEnabled(False)

    def on_changed(self):
        if self.UseExistingMesh_radioButton.isChecked() or self.AutoMesh_radioButton.isChecked():
            self.lineEdit.setEnabled(False)
        elif self.MeshSize_radioButton.isChecked():
            self.lineEdit.setEnabled(True)
        return