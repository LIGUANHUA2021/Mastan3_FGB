# -*- coding: utf-8 -*-

"""
Module implementing YSAnalMessageBox_Dialog.
"""
import sys, os
from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QSize, QFileInfo, QTime, Signal, Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QFont, QFontDatabase, QTextOption
from .Ui_YSAnalMessageBox import Ui_YSAnalMessageBox_Dialog
from gui.msasect.ui.ShowResultsYieldS import ShowResultsYS_Dialog
from gui.msasect.ui.ShowResultsYieldS2D import ShowResultsYS2D_Dialog
from gui.msasect.base.OutputRedir import ConsoleOutput
from gui.msasect.base.MultiThreadSetting import MultiThread
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.base.Model import Status
from analysis.FESect.util.MeshGen import FEMesh
from analysis.CMSect.util.MeshGen import MeshGenCM


class YSAnalMessageBox_Dialog(QDialog, Ui_YSAnalMessageBox_Dialog):
    """
    Class documentation goes here.
    """
    YSCalProgress_Signal = Signal(int)
    YSCalFinish_Signal = Signal()
    meshFinish_Signal = Signal()

    def __init__(self, mw, parent):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent=parent)
        self.setupUi(self)
        self.mw = mw
        self.cwd = os.getcwd()
        self.parent_window = self.parent()
        self.grandparent_window = self.parent_window.parent()
        ##
        self.setFixedSize(630, 550)
        ##
        self.Stop_pushButton.setEnabled(True)
        self.Stop_pushButton.setStyleSheet("background-color: red")
        self.OK_pushButton.setEnabled(False)
        ##
        # self.YSMessageBox_textBrowser.setReadOnly(True)
        # self.YSMessageBox_textBrowser.setFocusPolicy(Qt.NoFocus)
        # Disable QTextBrowser text selection and focus
        self.YSMessageBox_textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.YSMessageBox_textBrowser.setFocusPolicy(Qt.NoFocus)
        # self.ExportMessage_label.setStyleSheet("color: rgb(0, 0, 0);\n"
        #                                        "background-color: rgb(255, 255, 255)\n")
        # self.ExportMessage_label.setStyleSheet("QLabel { padding-top: 0px; padding-bottom: 1px; }")
        ##
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
        self.YSCalFinish_Signal.connect(self.YieldSurfCalFinish)

        if self.grandparent_window.Centerline_radioButton.isChecked():
            if not Status.Meshed:
                MeshGenCM()
                Status.Meshed = 1
                self.grandparent_window.ResetPanel()
                self.grandparent_window.ResetPlot()
            self.YieldSurfCal()
        elif self.grandparent_window.Outline_radioButton.isChecked():
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
                self.YieldSurfCal()

    def mesh_finish(self):
        self.grandparent_window.FEMeshFinish()
        self.NewThread.quit()
        self.YieldSurfCal()

    def YieldSurfCal(self):
        if self.grandparent_window.Centerline_radioButton.isChecked():
            self.NewThread = MultiThread(label="CalYS",
                                         parameter={"mw": self, "AnaFileName": msaModel.Information.ModelName,
                                                    "Flag": 1,
                                                    "progress_Signal": self.YSCalProgress_Signal,
                                                    "finish_Signal": self.YSCalFinish_Signal})
        else:
            self.NewThread = MultiThread(label="CalYS",
                                         parameter={"mw": self, "AnaFileName": msaFEModel.Information.ModelName,
                                                    "Flag": 2,
                                                    "progress_Signal": self.YSCalProgress_Signal,
                                                    "finish_Signal": self.YSCalFinish_Signal})
        ##
        self.NewThread.start()

    def YieldSurfCalFinish(self):
        ##
        self.NewThread.quit()
        self.Stop_pushButton.setEnabled(False)
        self.Stop_pushButton.setStyleSheet("color: rgb(153, 153, 153);\n"
                                           "background-color: rgb(255, 255, 255)\n")
        # self.Stop_pushButton.setStyleSheet("QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
        #                                 "QPushButton{    \n"
        #                                 "    font: 9pt \"Segoe UI\";\n"
        #                                 "    color: rgb(0, 0, 0);\n"
        #                                 "    background: rgb(255, 255, 255);\n""}")

        self.OK_pushButton.setEnabled(True)
        self.setWindowTitle("The analysis is complete. Please click the 'OK' button to review the results.")
        Status.YS = 1
        return


    @Slot()
    def on_YSMessageBox_textBrowser_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    @Slot()
    def on_Stop_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # self.parent_window
        try:
            if self.NewThread.isRunning():
                self.NewThread.terminate()
            else:
                self.NewThread.quit()
        except AttributeError:
            print()
        # try:
        #     if self.parent_window.NewThread.isRunning():
        #         self.parent_window.NewThread.terminate()
        #     else:
        #         self.parent_window.NewThread.quit()
        # except AttributeError:
        #     print()
        ##
        QDialog.close(self)


    @Slot()
    def on_OK_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)
        if self.parent_window.FYSPMyMz_radioButton.isChecked():
            Ui = ShowResultsYS_Dialog(self, parent=self.mw)
            Ui.exec()
        else:
            Ui = ShowResultsYS2D_Dialog(self, parent=self.mw)
            Ui.exec()

    @Slot()
    def on_SaveText_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        DirFile, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save Yield Surface Output Text", self.cwd, "Text Files (*.txt)")
        # print("Current Save DataFilePath=", DirFile)
        if DirFile == "":
            self.YSMessageBox_textBrowser.setFont(QFont("Courier", 10))
            self.YSMessageBox_textBrowser.append(QTime.currentTime().toString() + ": Cancel save output text file!")
            return
        else:
            fileinfo = QFileInfo(DirFile)
            tfilename = fileinfo.baseName()
            # tfilesuff = fileinfo.suffix()
            # print("File basename=", tfilename)
            # print("Filename suffix=", tfilesuff)
            # with open((str(tfilename) + '-Result output.txt'), 'w', encoding='utf-8') as f:
            with open((DirFile + '.txt'), 'w', encoding='utf-8') as f:
                f.write(self.YSMessageBox_textBrowser.toPlainText())
            self.YSMessageBox_textBrowser.append(QTime.currentTime().toString() + (': The log file have been successfully saved.'))
