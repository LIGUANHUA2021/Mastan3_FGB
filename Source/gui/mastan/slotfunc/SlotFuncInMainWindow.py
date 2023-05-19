# This file contains all the slot functions called in the Mastan3 Main Window (MW)
# External library
import os, json, sys
from PySide6 import QtWidgets
from PySide6.QtGui import QFont
# Internal library
from gui.mastan.visualization import NodeVis, MemVis, TextVis, LoadVis
from analysis.frame.variables import Model
from analysis.frame.file import ReadData
from analysis.frame import Main
from gui.mastan.file import io
from gui.mastan.base.model import msaModel
class FileInfo:
    FileName = ""
def NewFile(mw):
    FileName, FileType = QtWidgets.QFileDialog.getSaveFileName(mw, "New File", "/")
    FileInfo.FileName = FileName
    msaModel.ResetAll()
    FileName = FileName.split("/")
    msaModel.FileInfo.FileName = FileName[len(FileName) - 1]
def OpenFile(mw):
    FileName, FileType = QtWidgets.QFileDialog.getOpenFileName(mw, "Open File", "/",
                                                               "All Files (*);;Text Files (*.txt)")
    FileInfo.FileName = FileName
    io.ImportDataFile(FileName)
def SaveFile(mw):
    SaveAsFile(mw)
    if FileInfo.FileName == "":
        SaveAsFile(mw)
        return
    print(FileInfo.FileName)
    io.SaveDataFile(FileInfo.FileName)
def SaveAsFile(mw):
    FileName, Filetype = QtWidgets.QFileDialog.getSaveFileName(mw, "Save File", "/")
    io.SaveDataFile(FileName)
    FileInfo.FileName = FileName
    tFilelName = FileName.split("/")
    msaModel.FileInfo.FileName = tFilelName[len(tFilelName) - 1]
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
def Run(mw):
    t = r"""\ """ # To add "\" in strings (t[0] = "\")
    FileName = FileInfo.FileName.split("/")
    FileName = FileName[len(FileName) - 1]
    if FileName == '':
        try:
            SaveAsFile(mw)
        except:
            return
    FileName = os.path.dirname(os.path.dirname(os.path.abspath('.'))) + r'\analysis\frame\examples' + t[0] + FileName
    # print(FileName)
    f = open(FileName,'w')
    # f.write(mw.InputW.toPlainText())
    f.close()
    Model.OutResult.FileName = FileName
    Main.Run(argv=FileName)
    os.remove(FileName)
# Update the text information in OutputW every half second
def UpdateOutputW(mw):
    t = r"""\ """  # To add "\" in strings (t[0] = "\")
    FileName = msaModel.FileInfo.FileName
    LogFileName = sys.path[1] + "\\Source\\gui\\mastan\\examples\\" + FileName + ".rst\\" + FileName + ".log"
    # print(LogFileName)
    try:
        f = open(LogFileName, 'r')
        textInfo = f.read()
        mw.OutputW.setFont(QFont("Courier New", 12))
        mw.OutputW.setText(textInfo)
        # print("OUTPUT LOG FILE")
    except:
        pass