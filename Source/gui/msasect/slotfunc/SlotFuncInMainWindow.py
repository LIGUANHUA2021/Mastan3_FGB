# This file contains all the slot functions called in the Mastan3 Main Window (MW)
# External library
import os, json, sys
from PySide6 import QtWidgets
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import QTime, Qt, QFileInfo
# Internal library
from gui.mastan.visualization import NodeVis, MemVis, TextVis, LoadVis
from analysis.frame.variables import Model
from analysis.frame.file import ReadData
from analysis.frame import Main
from gui.msasect.file import IO
from gui.msasect.base.Model import msaModel, msaFEModel, Status
from gui.msasect.file import WelcomeInfo
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.NewmsgBox import NewshowMesbox
from PySide6.QtWidgets import QMessageBox
import traceback, logging
##



def NewFile(mw):
    #FileName, FileType = QtWidgets.QFileDialog.getSaveFileName(mw, "New File", "/")
    #FileInfo.FileName = FileName
    # flag = NewshowMesbox(mw)
    # reply = QMessageBox.question(mw,
    #                              'New',
    #                              'Are you sure you want to start over?<br>(unsaved data will be lost)',
    #                              QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    mesBox = QMessageBox()
    mesBox.setWindowTitle('New')
    mesBox.setText('Are you sure you want to start over?<br>(unsaved data will be lost)')
    mesBox.setWindowIcon(QIcon(r'ui/ico/Msa_Sect2.png'))
    mesBox.setIcon(mesBox.Icon.Question)
    mesBox.setStandardButtons(
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    mesBox.setStyleSheet("QPushButton:hover{background-color: rgb(144, 200, 246);}\n"
                         "QMessageBox {background: White;}\n"
                         "QPushButton {background: White;border:1px solid;width:69px;height:22px}\n"
                         "QPushButton:pressed{padding-left:3px;padding-top:3px;}")
    buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
    buttonNo = mesBox.button(QMessageBox.StandardButton.No)
    #buttonCancel = mesBox.button(QMessageBox.StandardButton.Cancel)
    mesBox.exec()
    if mesBox.clickedButton() == buttonYes:
        msaModel.ResetAll()
        msaFEModel.ResetAll()
        mw.StatusOutput.clear()
        tWelcomeInfo = WelcomeInfo.Welcome.PrintWelcomeInfo(mw)
        mw.StatusOutput.setText(tWelcomeInfo)
        mw.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections')
        mw.SectIDInput_lineEdit.setText("Section 01")
        mw.SectNameInput_lineEdit.setText("MsaSect Section")
        logging.shutdown()
        Status.Meshed = 0
        Status.SP = 0
        Status.YS = 0
        Status.MC = 0
        Status.NewFile = 1
        Status.Saved = 0
        mw.ResetPanel()
        mw.ResetPlot()
        mw.ResetTable()
    elif mesBox.clickedButton() == buttonNo:
        mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel New file!")
        mw.View.autoRange()
        Status.NewFile = 0
        return


def OpenFile(mw):
    DirFileName, FileType = QtWidgets.QFileDialog.getOpenFileName(mw, "Open File", mw.cwd,
                                                               "JSON Files (*.json)")
    # print(mw.cwd)
    #
    if DirFileName == "":
        mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel open file!")
        mw.View.autoRange()
        return
    else:
        msaModel.ResetAll()
        msaFEModel.ResetAll()
        mw.StatusOutput.clear()
        tWelcomeInfo = WelcomeInfo.Welcome.PrintWelcomeInfo(mw)
        mw.StatusOutput.setText(tWelcomeInfo)
        #
        fileinfo = QFileInfo(DirFileName)
        tfilename = fileinfo.baseName()
        # tDirFileName = DirFileName.split("/")[-1]
        # ModelName = os.path.basename(tDirFileName)
        # msaModel.FileInfo.FileName = DirFileName
        # print("Openfile, Modelname=", DirFileName)
        Model.OutResult.ModelName = DirFileName ## absolute FilePath
        #
        mw.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + tfilename)
        mw.SectNameInput_lineEdit.setText(tfilename)
        # mw.StatusOutput.append(QTime.currentTime().toString() + (": Open " + ModelName + " successfully!"))
        ## Import Json data file to model
        if mw.Centerline_radioButton.isChecked():
            try:
                open_CM(mw, DirFileName, tfilename)
            except KeyError:
                try:
                    msaModel.ResetAll()
                    mw.Outline_radioButton.setChecked(True)
                    open_FE(mw, DirFileName, tfilename)
                except:
                    msaFEModel.ResetAll()
                    mw.StatusOutput.clear()
                    showMesbox(mw, "Please select correct Data File to Open!")
                    mw.StatusOutput.append(QTime.currentTime().toString() + (": Open " + tfilename + " Failed!"))
                return

        elif mw.Outline_radioButton.isChecked():
            try:
                open_FE(mw, DirFileName, tfilename)
            except KeyError:
                try:
                    msaFEModel.ResetAll()
                    mw.Centerline_radioButton.setChecked(True)
                    open_CM(mw, DirFileName, tfilename)
                except:
                    msaModel.ResetAll()
                    mw.StatusOutput.clear()
                    showMesbox(mw, "Please select correct Data File to Open!")
                    mw.StatusOutput.append(QTime.currentTime().toString() + (": Open " + tfilename + " Failed!"))
                return


def open_CM(mw, DirFileName, tfilename):
    IO.CMFile.ImportDataFile(mw, DirFileName)
    if (msaModel.Mat.ID and msaModel.Point.ID and msaModel.Segment.ID):
        for i in msaModel.Mat.ID:
            msaModel.Mat.Color[i] = "#aaffff"
        mw.StatusOutput.append(QTime.currentTime().toString() + (": Open " + tfilename + " successfully!"))
        Status.NewFile = 0
        Status.YS = 0
        Status.MC = 0
        Status.Saved = 1
    else:
        mw.StatusOutput.append(QTime.currentTime().toString() + (": Please check your input file carefully!"))


def open_FE(mw, DirFileName, tfilename):
    IO.FEFile.ImportDataFile(mw, DirFileName)
    if (msaFEModel.Mat.ID and msaFEModel.Point.ID and msaFEModel.Outline.ID
            and msaFEModel.Loop.ID and msaFEModel.Group.ID):
        for i in msaFEModel.Mat.ID:
            msaFEModel.Mat.Color[i] = "#aaffff"
        mw.StatusOutput.append(QTime.currentTime().toString() + (": Open " + tfilename + " successfully!"))
        Status.NewFile = 0
        Status.YS = 0
        Status.MC = 0
        Status.Saved = 1
    else:
        mw.StatusOutput.append(QTime.currentTime().toString() + (": Please check your input file carefully!"))


def SaveFile(mw, tFlag):
    if (not msaModel.Point.ID and mw.Centerline_radioButton.isChecked()) or \
       (not msaFEModel.Point.ID and mw.Outline_radioButton.isChecked()):
        showMesbox(mw, "There is no data in present model, please create a model firstly!")
        return
    if Status.NewFile or (not Status.NewFile and  # New file or no absolute path stored
                          ((mw.Centerline_radioButton.isChecked() and not msaModel.Information.ModelName)
                           or (mw.Outline_radioButton.isChecked() and not msaFEModel.Information.ModelName))):
        DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(mw, "Save File", mw.cwd, "Json Files (*.Json)")
        if not DirFileName:  # No absolute path input
            mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel save file!")
            mw.View.autoRange()
            return
        else:
            tfilename = QFileInfo(DirFileName).baseName()
            if mw.Centerline_radioButton.isChecked():
                msaModel.Information.ModelName = DirFileName  # absolute FilePath
                msaModel.FileInfo.FileName = tfilename  # the model file name
            elif mw.Outline_radioButton.isChecked():
                msaFEModel.Information.ModelName = DirFileName  # absolute FilePath
                msaFEModel.FileInfo.FileName = tfilename  # the model file name
    if mw.Centerline_radioButton.isChecked():
        if not msaModel.Segment.ID:
            showMesbox(mw, "Requied data missing, please check your model!")
            return
        msaModel.FileInfo.FileName = QFileInfo(msaModel.Information.ModelName).baseName()
        try:
            IO.CMFile.SaveDataFile(msaModel.Information.ModelName, tFlag)
            mw.SectNameInput_lineEdit.setText(msaModel.FileInfo.FileName)
            mw.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + msaModel.FileInfo.FileName)
            mw.StatusOutput.append(QTime.currentTime().toString() + (": Save file successfully!"))
            Status.NewFile = 0
            Status.Saved = 1
        except:
            showMesbox(mw, "Incorrect model information!")
            Status.Saved = 0
    elif mw.Outline_radioButton.isChecked():
        if not msaFEModel.Outline.ID or not msaFEModel.Loop.ID or not msaFEModel.Group.ID:
            showMesbox(mw, "Requied data missing, please check your model!")
            return
        msaFEModel.FileInfo.FileName = QFileInfo(msaFEModel.Information.ModelName).baseName()
        try:
            IO.FEFile.SaveDataFile(msaFEModel.Information.ModelName)
            mw.SectNameInput_lineEdit.setText(msaFEModel.FileInfo.FileName)
            mw.setWindowTitle('MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + msaFEModel.FileInfo.FileName)
            mw.StatusOutput.append(QTime.currentTime().toString() + (": Save file successfully!"))
            Status.NewFile = 0
            Status.Saved = 1
        except:
            showMesbox(mw, "Incorrect model information!")
            Status.Saved = 0


def SaveAsFile(mw, tFlag):
    if (not msaModel.Point.ID and mw.Centerline_radioButton.isChecked()) or \
            (not msaFEModel.Point.ID and mw.Outline_radioButton.isChecked()):
        showMesbox(mw, "There is no data in present model, please create a model firstly!")
        return
    DirFileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(mw, "Save File", mw.cwd, "Json Files (*.Json)")
    if not DirFileName:  # No absolute path input
        mw.StatusOutput.append(QTime.currentTime().toString() + ": Cancel save file!")
        mw.View.autoRange()
        return
    else:
        tfilename = QFileInfo(DirFileName).baseName()
        if mw.Centerline_radioButton.isChecked():
            msaModel.Information.ModelName = DirFileName  # absolute FilePath
            msaModel.FileInfo.FileName = tfilename  # the model file name
        elif mw.Outline_radioButton.isChecked():
            msaFEModel.Information.ModelName = DirFileName  # absolute FilePath
            msaFEModel.FileInfo.FileName = tfilename  # the model file name
    if mw.Centerline_radioButton.isChecked():
        if not msaModel.Segment.ID:
            showMesbox(mw, "Requied data missing, please check your model!")
            return
        msaModel.FileInfo.FileName = QFileInfo(msaModel.Information.ModelName).baseName()
        try:
            IO.CMFile.SaveDataFile(msaModel.Information.ModelName, tFlag)
            mw.SectNameInput_lineEdit.setText(msaModel.FileInfo.FileName)
            mw.setWindowTitle(
                'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + msaModel.FileInfo.FileName)
            mw.StatusOutput.append(QTime.currentTime().toString() + (": Save file successfully!"))
            Status.NewFile = 0
            Status.Saved = 1
        except:
            showMesbox(mw, "Incorrect model information!")
            Status.Saved = 0
    elif mw.Outline_radioButton.isChecked():
        if not msaFEModel.Outline.ID or not msaFEModel.Loop.ID or not msaFEModel.Group.ID:
            showMesbox(mw, "Requied data missing, please check your model!")
            return
        msaFEModel.FileInfo.FileName = QFileInfo(msaFEModel.Information.ModelName).baseName()
        try:
            IO.FEFile.SaveDataFile(msaFEModel.Information.ModelName)
            mw.SectNameInput_lineEdit.setText(msaFEModel.FileInfo.FileName)
            mw.setWindowTitle(
                'MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections - ' + msaFEModel.FileInfo.FileName)
            mw.StatusOutput.append(QTime.currentTime().toString() + (": Save file successfully!"))
            Status.NewFile = 0
            Status.Saved = 1
        except:
            showMesbox(mw, "Incorrect model information!")
            Status.Saved = 0


# Visualize the model in VISPY widget
def VisualizeModel(mw):
    try:
        NodeVis.visualizenode(mw, mw.MainMenu.ShowNode.isChecked())
    except:
        pass
    try:
        MemVis.visualizemember(mw, mw.MainMenu.ShowMember.isChecked())
    except:
        pass
    try:
        TextVis.visualizenodetext(mw, mw.MainMenu.ShowID.isChecked())
    except:
        pass
    try:
        TextVis.visualizememtext(mw, mw.MainMenu.ShowID.isChecked())
    except:
        pass
    try:
        LoadVis.VisualizeJointLoad(mw, mw.MainMenu.ShowJointLoad.isChecked())
    except:
        pass


def UpdateOutputW(mw):
    if mw.Centerline_radioButton.isChecked():
        MFileName = msaModel.FileInfo.FileName
        DirFileName = msaModel.Information.ModelName
    elif mw.Outline_radioButton.isChecked():
        MFileName = msaFEModel.FileInfo.FileName
        DirFileName = msaFEModel.Information.ModelName
    LogFileName = DirFileName + ".rst/" + MFileName + ".Json" + ".log"
    try:
        with open(LogFileName, 'r') as file:
            textInfo = file.read()
            mw.StatusOutput.append(textInfo)
    except:
        pass