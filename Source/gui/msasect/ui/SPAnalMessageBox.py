# -*- coding: utf-8 -*-

"""
Module implementing SPAnalMessageBox_Dialog.
"""
import sys, os
from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QSize, QFileInfo, QTime, Signal, Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QFont, QFontDatabase, QTextOption
from gui.msasect.ui.Ui_SPAnalMessageBox import Ui_SPAnalMessageBox_Dialog
from gui.msasect.base.OutputRedir import ConsoleOutput
from gui.msasect.base.OutputRedir import ConsoleOutput
from gui.msasect.base.MultiThreadSetting import MultiThread
from gui.msasect.base.Model import msaModel, msaFEModel, Status
from analysis.FESect.variables import Model
from analysis.CMSect import Main as CMMain
from analysis.FESect import Main as FEMain
from analysis.FESect.util.MeshGen import FEMesh
from gui.msasect.slotfunc import SlotFuncInMainWindow
from gui.msasect.file import IO


class SPAnalMessageBox_Dialog(QDialog, Ui_SPAnalMessageBox_Dialog):
    """
    Class documentation goes here.
    """
    meshFinish_Signal = Signal()
    SPCalProgress_Signal = Signal(int)
    SPCalFinish_Signal = Signal()
    CSMCalProgress_Signal = Signal(int)
    CSMCalFinish_Signal = Signal()

    def __init__(self, mw, parent=None, CM=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("Section Properties: Analysis in progress...")
        self.mw = mw
        self.cwd = os.getcwd()
        self.parent_window = self.parent()
        self.grandparent_window = self.parent_window.parent
        ##
        self.Stop_pushButton.setEnabled(True)
        self.OK_pushButton.setEnabled(False)
        ##
        # Disable QTextBrowser text selection and focus
        self.YSMessageBox_textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.YSMessageBox_textBrowser.setFocusPolicy(Qt.NoFocus)
        #
        monospace_font = QFont("Courier New", 10)
        self.YSMessageBox_textBrowser.setFont(monospace_font)
        self.YSMessageBox_textBrowser.setFont(QFont('Courier New', 10))

        font_info = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font = font_info.family()
        font_size = font_info.pointSize()
        self.YSMessageBox_textBrowser.setFontPointSize(font_size)
        self.YSMessageBox_textBrowser.setFontFamily(font)
        ##
        self.YSMessageBox_textBrowser.setWordWrapMode(QTextOption.NoWrap)
        ##
        today = datetime.now().strftime("%Y/%m/%d")
        self.StartTimeDay_label.setText(today)
        ##
        current_time = datetime.now().strftime("%H:%M:%S")
        self.StartTimer_label.setText(current_time)
        ##
        self.SaveText_toolButton.setIcon(QIcon('ui/ico/save.ico'))
        self.SaveText_toolButton.setIconSize(QSize(32, 32))
        ##
        sys.stdout = ConsoleOutput(self.YSMessageBox_textBrowser)
        self.meshFinish_Signal.connect(self.mesh_finish)
        self.SPCalFinish_Signal.connect(self.SectPropCalFinish)
        self.CSMCalFinish_Signal.connect(self.CSMCalFinish)
        self.OK_pushButton.setEnabled(False)
        if CM:
            CMMain.Run(1, msaModel.Information.ModelName)
            SlotFuncInMainWindow.UpdateOutputW(self.grandparent_window)
            self.OK_pushButton.setEnabled(True)
            self.Stop_pushButton.setEnabled(False)
            self.setWindowTitle("Section Properties: Analysis complete!")
        else:
            if self.parent_window.AutoMesh_radioButton.isChecked():
                self.YSMessageBox_textBrowser.insertPlainText("Generating Mesh...\n")
                self.NewThread = MultiThread(label="Mesh",
                                             parameter={"meshSize": 0,
                                                        "msaFEModel": msaFEModel,
                                                        "FEMesh": FEMesh(finish_Signal=self.meshFinish_Signal)})
                self.NewThread.start()
            elif self.parent_window.MeshSize_radioButton.isChecked():
                self.YSMessageBox_textBrowser.insertPlainText("Generating Mesh...\n")
                self.NewThread = MultiThread(label="Mesh",
                                             parameter={"meshSize": float(self.parent_window.lineEdit.text()),
                                                        "msaFEModel": msaFEModel,
                                                        "FEMesh": FEMesh(finish_Signal=self.meshFinish_Signal)})
                self.NewThread.start()
            else:
                self.SectPropCal()

    def mesh_finish(self):
        self.grandparent_window.FEMeshFinish()
        self.NewThread.quit()
        self.SectPropCal()

    def SectPropCal(self):
        self.NewThread = MultiThread(label="CalSP", parameter={"msaFEModel": msaFEModel,
                                                               "FEMain": FEMain,
                                                               "progress_Signal": self.SPCalProgress_Signal,
                                                               "finish_Signal": self.SPCalFinish_Signal,
                                                               "mat_ref": self.parent_window.mat_ref})
        self.NewThread.start()

    @Slot()
    def on_Stop_pushButton_clicked(self):
        if self.NewThread:
            self.NewThread.terminate()
            try:
                self.meshFinish_Signal.disconnect(self.SectPropCal)
            except:
                pass
            self.SPCalFinish_Signal.disconnect(self.SectPropCalFinish)
        QDialog.close(self)
        self.grandparent_window.StatusOutput.append("Section properties calculation canceled!")

    @Slot()
    def on_SaveText_toolButton_clicked(self):
        DirFile, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save Section Properties Output Text", self.cwd, "Text Files (*.txt)")
        # print("Current Save DataFilePath=", DirFile)
        if DirFile == "":
            self.YSMessageBox_textBrowser.setFont(QFont("Courier", 10))
            self.YSMessageBox_textBrowser.append(QTime.currentTime().toString() + ": Cancel save output text file!")
            return
        else:
            with open((DirFile + '.txt'), 'w', encoding='utf-8') as f:
                f.write(self.YSMessageBox_textBrowser.toPlainText())
            self.YSMessageBox_textBrowser.append(QTime.currentTime().toString() + (': The log results have been successfully saved.'))

    def SectPropCalFinish(self):
        self.NewThread.quit()
        tAnaFileName = msaFEModel.Information.ModelName  ## absolute FilePath
        ttfileinfo = QFileInfo(tAnaFileName)
        OutFolder = os.path.join(ttfileinfo.path() + os.sep, ttfileinfo.baseName() + '.Json.rst')
        if not os.path.exists(OutFolder):
            os.makedirs(OutFolder)
        IO.FEFile.SaveCompSPDataFile(
            ttfileinfo.path() + os.sep + ttfileinfo.baseName() + '.Json.rst' + os.sep + ttfileinfo.baseName() + "-RCDOnly.Json")
        ##
        self.CompSectModuCal()

    def CompSectModuCal(self):
        self.NewThread = MultiThread(label="CalCompSectModu",
                                     parameter={"mw": self, "AnaFileName": msaFEModel.Information.ModelName,
                                                "Flag": 1,
                                                "progress_Signal": self.CSMCalProgress_Signal,
                                                "finish_Signal": self.CSMCalFinish_Signal})
        self.NewThread.start()

    def CSMCalFinish(self):
        self.NewThread.quit()
        self.setWindowTitle("Section Properties: Analysis complete!")
        self.OK_pushButton.setEnabled(True)
        self.Stop_pushButton.setEnabled(False)
        SlotFuncInMainWindow.UpdateOutputW(self.grandparent_window)
        Status.SP = 1
        self.grandparent_window.OutSPtoMW()
        self.grandparent_window.ResetPanel()
        self.grandparent_window.StatusOutput.append(
            QTime.currentTime().toString() + (": The calculation process has been successfully completed."))
        try:
            self.meshFinish_Signal.disconnect(self.SectPropCal)
            self.SPCalFinish_Signal.disconnect(self.SectPropCalFinish)
            self.CSMCalFinish_Signal.disconnect(self.CSMCalFinish)
        except:
            pass

    @Slot()
    def on_OK_pushButton_clicked(self):
        QDialog.close(self)