# -*- coding: utf-8 -*-

"""
Module implementing MomentCurvatureAnalDialog.
"""
import os, traceback, sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, QTime, QFileInfo, QRegularExpression, QLocale
from PySide6.QtWidgets import QDialog
from gui.msasect.file import IO
from PySide6.QtGui import QDoubleValidator, QIntValidator, QFont, QTextOption, QIcon, QRegularExpressionValidator
from gui.msasect.ui.ShowResultsMCurv import ShowResultsMCurv_Dialog
from gui.msasect.ui.Ui_AnalMomentCurvature import Ui_MomentCurAnal_Dialog
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.base.OutputRedir import ConsoleOutput
from gui.msasect.ui.MCAnalMessageBox import MCAnalMessageBox_Dialog
from gui.msasect.base.Model import Status

from analysis.CMSect.util.MeshGen import MeshGenCM
from analysis.FESect.variables import Model as FEModel
from analysis.RCD.variables.Model import AnalysisInfo
from analysis.RCD.variables.Model import MomentCurvatureResults as MomCurvaResults
from analysis.RCD import Main as RCDMain


class MomentCurvatureAnalDialog(QDialog, Ui_MomentCurAnal_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("ui/ico/MomentCurvature.png"))
        self.cwd = os.getcwd()
        self.parent_window = self.parent()
        self.grandparent_window = self.parent_window.parent()
        ##
        self.setFixedSize(self.width(), self.height())
        ##
        self.InputtedPx_lineEdit.textChanged.connect(self.on_textchanged)
        self.InputtedPPy_lineEdit.textChanged.connect(self.on_textchanged)
        self.MomStep_lineEdit.textChanged.connect(self.on_textchanged)
        self.MaxNumIntera_lineEdit.textChanged.connect(self.on_textchanged)
        self.Tol_lineEdit.textChanged.connect(self.on_textchanged)
        ##
        self.InputtedPPy_lineEdit.setPlaceholderText('(-100, 100)')
        self.ShowResults_pushButton.setDisabled(True)
        # Set a QRegularExpressionValidator for the QLineEdit
        # regex = QRegularExpression('^([0-9]{0,2}(\\.\\d{0,2})?|100(\\.0{0,2})?)%?$')
        # validator = QRegularExpressionValidator(regex, self.InputtedPPy_lineEdit)
        # validator = QDoubleValidator(-1, 1, 2, self)  #
        validator = QDoubleValidator(-100.0, 100.0, 2, self)
        validator.setLocale(QLocale(QLocale.English))
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.InputtedPPy_lineEdit.setValidator(validator)
        ##
        self.AbsoluteValue_radioButton.toggled.connect(self.AbsoluteValueradio_changed)
        self.PercentageofMaxP_radioButton.toggled.connect(self.PCTofMaxPradio_changed)
        #
        self.MyCur_radioButton.toggled.connect(self.ShowResultsSetting)
        self.MzCur_radioButton.toggled.connect(self.ShowResultsSetting)
        self.AbsoluteValue_radioButton.toggled.connect(self.ShowResultsSetting)
        self.PercentageofMaxP_radioButton.toggled.connect(self.ShowResultsSetting)
        ##
        self.InputtedPPy_lineEdit.setDisabled(True)
        ##
        # self.ShowResults_pushButton.setEnabled(False)
        ##
        self.initDialog()

    def initDialog(self):
        ##
        doubleValidator = QDoubleValidator(bottom=-999999, top=999999)
        self.InputtedPx_lineEdit.setValidator(doubleValidator)
        doubleValidator2 = QDoubleValidator(bottom=-100, top=100)
        self.InputtedPPy_lineEdit.setValidator(doubleValidator2)
        ##
        if Status.MC:
            if self.AbsoluteValue_radioButton.isChecked() and len(MomCurvaResults.OMz_y) > 0 and len(MomCurvaResults.Oan_y) > 0 and len(MomCurvaResults.Idn_y) > 0:
                self.ShowResults_pushButton.setDisabled(False)
            else:
                self.ShowResults_pushButton.setDisabled(True)
        else:
            self.ShowResults_pushButton.setDisabled(True)
        ##
        ##
        return

    def ShowResultsSetting(self):
        if Status.MC:
            tLType = AnalysisInfo.AxialLoadType
            if self.MyCur_radioButton.isChecked() and self.AbsoluteValue_radioButton.isChecked():
                if len(MomCurvaResults.OMz_y) > 0 and len(MomCurvaResults.Oan_y) > 0 and len(MomCurvaResults.Idn_y) > 0 and tLType==0:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            if self.MyCur_radioButton.isChecked() and self.PercentageofMaxP_radioButton.isChecked():
                if len(MomCurvaResults.OMz_y) > 0 and len(MomCurvaResults.Oan_y) > 0 and len(MomCurvaResults.Idn_y) > 0 and tLType==1:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            ##
            if self.MzCur_radioButton.isChecked() and self.AbsoluteValue_radioButton.isChecked():
                if len(MomCurvaResults.OMz_z) > 0 and len(MomCurvaResults.Oan_z) > 0 and len(MomCurvaResults.Idn_z) > 0 and tLType==0:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
            if self.MzCur_radioButton.isChecked() and self.PercentageofMaxP_radioButton.isChecked():
                if len(MomCurvaResults.OMz_z) > 0 and len(MomCurvaResults.Oan_z) > 0 and len(MomCurvaResults.Idn_z) > 0 and tLType==1:
                    self.ShowResults_pushButton.setDisabled(False)
                else:
                    self.ShowResults_pushButton.setDisabled(True)
        else:
            self.ShowResults_pushButton.setDisabled(True)
        ##
        return

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

    @Slot()
    def on_Run_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            if self.parent_window.Centerline_radioButton.isChecked():
                if (not msaModel.Point.ID and not msaModel.Segment.ID) and (
                        not msaFEModel.Point.ID and not msaFEModel.Outline.ID):
                    showMesbox(self,
                               "Cannot perform action until a model has been created.\nPlease create a model first and try again.")
                    return
                ##
                if len(self.InputtedPx_lineEdit.text()) == 0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    tInputtedPx = float(self.InputtedPx_lineEdit.text())
                    tInputtedPPy = float(self.InputtedPPy_lineEdit.text())
                    # print("InputtedPx = ", tInputtedPx)
                    if abs(tInputtedPPy) >= 100.0:
                        showMesbox(self,
                                   "Kindly provide a numerical value, ranging from -100 to 100, \nwithin the 'Percentage of Axial Capacity' input field.")
                        return
                    tInpPx = 0.0
                    tLType = 0
                    if self.AbsoluteValue_radioButton.isChecked():
                        tInpPx = tInputtedPx
                        tLType = 0
                    elif self.PercentageofMaxP_radioButton.isChecked():
                        tInpPx = tInputtedPPy
                        tLType = 1
                    ##
                    tMomentStep = int(self.MomStep_lineEdit.text())
                    tMaxNumIter = int(self.MaxNumIntera_lineEdit.text())
                    tConvTol = float(self.Tol_lineEdit.text())
                    msaModel.MomentCurvaAnalInfo.AddInfo(tAnap=tInpPx, tLoadType=tLType, tMomentStep=tMomentStep,
                                                         tMaxNumIter=tMaxNumIter, tConvTol=tConvTol)
                    ##
                    if self.PrinAxis_radioButton.isChecked():
                        msaModel.MomentCurvaAnalInfo.AxisSlctn = 1
                    else:
                        msaModel.MomentCurvaAnalInfo.AxisSlctn = 2
                    ##
                    if self.MyCur_radioButton.isChecked():
                        msaModel.MomentCurvaAnalInfo.SubAnalType = 1
                    elif self.MzCur_radioButton.isChecked():
                        msaModel.MomentCurvaAnalInfo.SubAnalType = 2
                    ##
                    if not msaModel.Fiber.ID:
                        MeshGenCM()
                        Status.Meshed = 1
                    ##
                    if msaModel.FileInfo.FileName == "":
                        DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", self.cwd,
                                                                                      "Json Files (*.Json)")
                        if DirFileName == "":
                            self.parent_window.StatusOutput.setFont(QFont("Courier", 9))
                            self.parent_window.StatusOutput.append(
                                QTime.currentTime().toString() + ": Cancel save file!")
                            self.parent_window.View.autoRange()
                            return
                        else:
                            fileinfo = QFileInfo(DirFileName)
                            tfilename = fileinfo.baseName()
                            msaModel.Information.ModelName = DirFileName  ## absolute FilePath
                            msaModel.FileInfo.FileName = tfilename
                            IO.CMFile.SaveDataFile(DirFileName, 2)
                            ##
                            OutFolder = os.path.join(fileinfo.path() + os.sep, tfilename + '.Json.rst')
                            if not os.path.exists(OutFolder):
                                os.makedirs(OutFolder)
                            #
                            IO.CMFile.SaveMCurvaDataFile(fileinfo.path() + os.sep + tfilename + '.Json.rst' + os.sep + tfilename + "-RCDOnly.Json")
                            # print("SaveMCurvaDataFile path = ", fileinfo.path() + os.sep + tfilename)
                            self.parent_window.setWindowTitle(
                                'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections-' + tfilename)
                            ##
                    ##
                    tAnaFileName = msaModel.Information.ModelName  ## absolute FilePath
                    ttfileinfo = QFileInfo(tAnaFileName)
                    ##
                    OutFolder = os.path.join(ttfileinfo.path() + os.sep,  ttfileinfo.baseName() + '.Json.rst')
                    if not os.path.exists(OutFolder):
                        os.makedirs(OutFolder)
                    #
                    IO.CMFile.SaveMCurvaDataFile(ttfileinfo.path() + os.sep + ttfileinfo.baseName() + '.Json.rst' + os.sep + ttfileinfo.baseName() + "-RCDOnly.Json")
                    Status.NewFile = 0
                    Status.Saved = 1
                    # RCDMain.Run(1, ttfileinfo.path() + os.sep + ttfileinfo.baseName() + '.rst' + os.sep + ttfileinfo.baseName() + "-RCDOnly.Json")
                    QDialog.close(self)
                    Ui = MCAnalMessageBox_Dialog(self, parent=self)
                    Ui.exec()

            elif self.parent_window.Outline_radioButton.isChecked():
                if (not msaFEModel.Point.ID and not msaFEModel.Outline.ID):
                    showMesbox(self, "There is no data in present model, please create a model firstly!")
                    return
                #
                if len(self.InputtedPx_lineEdit.text()) == 0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    tInputtedPx = float(self.InputtedPx_lineEdit.text())
                    tInputtedPPy = float(self.InputtedPPy_lineEdit.text())
                    # print("InputtedPx = ", tInputtedPx)
                    if abs(tInputtedPPy) >= 100.0:
                        showMesbox(self,
                                   "Kindly provide a numerical value, ranging from -100 to 100, \nwithin the 'Percentage of Axial Capacity' input field.")
                        return
                    tInpPx = 0.0
                    tLType = 0
                    if self.AbsoluteValue_radioButton.isChecked():
                        tInpPx = tInputtedPx
                        tLType = 0
                    elif self.PercentageofMaxP_radioButton.isChecked():
                        tInpPx = tInputtedPPy
                        tLType = 1
                    ##
                    tMomentStep = int(self.MomStep_lineEdit.text())
                    tMaxNumIter = int(self.MaxNumIntera_lineEdit.text())
                    tConvTol = float(self.Tol_lineEdit.text())
                    msaFEModel.MomentCurvaAnalInfo.AddInfo(tAnap=tInpPx, tLoadType=tLType, tMomentStep=tMomentStep,
                                                         tMaxNumIter=tMaxNumIter, tConvTol=tConvTol)
                    ##
                    if self.PrinAxis_radioButton.isChecked():
                        msaFEModel.MomentCurvaAnalInfo.AxisSlctn = 1
                    else:
                        msaFEModel.MomentCurvaAnalInfo.AxisSlctn = 2
                    ##
                    if self.MyCur_radioButton.isChecked():
                        msaFEModel.MomentCurvaAnalInfo.SubAnalType = 1
                    elif self.MzCur_radioButton.isChecked():
                        msaFEModel.MomentCurvaAnalInfo.SubAnalType = 2
                    ##
                    if not FEModel.Fiber.ID:
                        showMesbox(self, 'Please click the mesh tool button to generate fiber firstly!')
                        return
                    ##
                    if msaFEModel.FileInfo.FileName == "" or msaFEModel.Information.ModelName == "":

                        DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", self.cwd,
                                                                                      "Json Files (*.Json)")
                        if DirFileName == "":
                            self.parent_window.StatusOutput.setFont(QFont("Courier", 9))
                            self.parent_window.StatusOutput.append(QTime.currentTime().toString() + ": Cancel save file!")
                            self.parent_window.View.autoRange()
                            return
                        else:
                            fileinfo = QFileInfo(DirFileName)
                            tfilename = fileinfo.baseName()
                            msaFEModel.Information.ModelName = DirFileName  ## absolute FilePath
                            msaFEModel.FileInfo.FileName = tfilename
                            IO.FEFile.SaveDataFile(DirFileName, 2)
                            ##
                            OutFolder = os.path.join(fileinfo.path() + os.sep, tfilename + '.Json.rst')
                            if not os.path.exists(OutFolder):
                                os.makedirs(OutFolder)
                            #
                            IO.FEFile.SaveMCurvaDataFile(fileinfo.path() + os.sep + tfilename + '.Json.rst' + os.sep + tfilename + "-RCDOnly.Json")
                            ##
                            self.parent_window.setWindowTitle(
                                'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections-' + tfilename)
                            FEModel.OutResult.ReadOutResult(msaFEModel.FileInfo.FileName,
                                                            os.path.dirname(msaFEModel.Information.ModelName))
                    ##
                    tAnaFileName = msaFEModel.Information.ModelName  ## absolute FilePath
                    ttfileinfo = QFileInfo(tAnaFileName)
                    ##
                    OutFolder = os.path.join(ttfileinfo.path() + os.sep,  ttfileinfo.baseName() + '.Json.rst')
                    if not os.path.exists(OutFolder):
                        os.makedirs(OutFolder)
                    #
                    IO.FEFile.SaveMCurvaDataFile(ttfileinfo.path() + os.sep + ttfileinfo.baseName() + '.Json.rst' + os.sep + ttfileinfo.baseName() + "-RCDOnly.Json")
                    Status.NewFile = 0
                    Status.Saved = 1
                    # RCDMain.Run(1, ttfileinfo.path() + os.sep + ttfileinfo.baseName() + "-RCDOnly.Json")
                    QDialog.close(self)
                    Ui = MCAnalMessageBox_Dialog(self, parent=self)
                    Ui.exec()
            ##
            sys.stdout = ConsoleOutput(self.parent_window.StatusOutput)



        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

        # Ui = ShowMomentCurvature_Dialog(self)
        # Ui.exec()
        # Ui = ShowResultsMCurv_Dialog(parent=self)
        # Ui.exec()

    @Slot()
    def on_GeoAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError

    def AbsoluteValueradio_changed(self):
        self.InputtedPPy_lineEdit.setDisabled(True)
        self.InputtedPx_lineEdit.setDisabled(False)
        self.InputtedPPy_lineEdit.setText('10')
        return

    def PCTofMaxPradio_changed(self):
        self.InputtedPx_lineEdit.setDisabled(True)
        self.InputtedPPy_lineEdit.setDisabled(False)
        self.InputtedPx_lineEdit.setText('0.0')
        return

    @Slot()
    def on_ShowResults_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)
        Ui = ShowResultsMCurv_Dialog(parent=self)
        Ui.exec()

    def on_textchanged(self):
        self.ShowResults_pushButton.setEnabled(False)