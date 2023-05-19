# -*- coding: utf-8 -*-

"""
Module implementing MCAnalMessageBox_Dialog.
"""
import sys, os
from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QSize, Signal, QFileInfo, QTime, Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QFont, QFontDatabase, QTextOption
from .Ui_GBAnalMessageBox import Ui_GBAnalMessageBox_Dialog
from gui.msasect.ui.ShowResultsMCurv import ShowResultsMCurv_Dialog
from gui.msasect.base.MultiThreadSetting import MultiThread
from gui.msasect.base.OutputRedir import ConsoleOutput
from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.base import Model as GBModel
from gui.msasect.base.Model import Status
from gui.msasect.ui.ShowResultsBuckling import GlobalBucklingPlot_Dialog
from gui.msasect.ui.ShowResultsBuckling_Element import GlobalBuckling_Element_Plot_Dialog

class GBAnalMessageBox_Dialog(QDialog, Ui_GBAnalMessageBox_Dialog):
    """
    Class documentation goes here.
    """
    GBCalProgress_Signal = Signal(int)
    GBCalFinish_Signal = Signal()

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
        self.Stop_pushButton.setEnabled(True)
        self.Stop_pushButton.setStyleSheet("background-color: red")
        self.OK_pushButton.setEnabled(False)
        #
        # Disable QTextBrowser text selection and focus
        self.MCMessageBox_textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.MCMessageBox_textBrowser.setFocusPolicy(Qt.NoFocus)
        #
        self.ExportFileFormat_comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
                                                     "background-color: rgb(255, 255, 255)\n")
        self.SaveText_toolButton.setStyleSheet("background-color: rgb(128, 128, 128)\n")
        ##
        monospace_font = QFont("Courier New", 10)
        self.MCMessageBox_textBrowser.setFont(monospace_font)
        self.MCMessageBox_textBrowser.setFont(QFont('Courier New', 10))

        font_info = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font = font_info.family()
        font_size = font_info.pointSize()
        self.MCMessageBox_textBrowser.setFontPointSize(font_size)
        self.MCMessageBox_textBrowser.setFontFamily(font)
        ##
        self.MCMessageBox_textBrowser.setWordWrapMode(QTextOption.NoWrap)
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
        sys.stdout = ConsoleOutput(self.MCMessageBox_textBrowser)
        self.GBCalFinish_Signal.connect(self.GBCalFinish)
        ##
        if self.parent_window.AnalyticalExpression_radioButton.isChecked():
            self.NewThread = MultiThread(label="CalGB",
                                         parameter={"mw": self, "AnaFileName": msaModel.Information.ModelName,
                                                    "Flag": 1,
                                                    "progress_Signal": self.GBCalProgress_Signal,
                                                    "finish_Signal": self.GBCalFinish_Signal})
        elif self.parent_window.LineElement_radioButton.isChecked():
            self.NewThread = MultiThread(label="CalGB",parameter={"mw": self, "AnaFileName": msaModel.Information.ModelName,
                                                    "Flag": 2,
                                                    "progress_Signal": self.GBCalProgress_Signal,
                                                    "finish_Signal": self.GBCalFinish_Signal})
        ##
        self.NewThread.start()


    @Slot()
    def on_Stop_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ##raise NotImplementedError
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
        Buckling_data = GBModel.GlobalBuckling.Buckling_data
        QDialog.close(self)
        if Buckling_data['method'] == 'Analytical':
            Ui = GlobalBucklingPlot_Dialog(self)
            Ui.exec()
        elif Buckling_data['method'] == 'Line_element':
            Ui = GlobalBuckling_Element_Plot_Dialog(self)
            Ui.exec()

    def GBCalFinish(self):
        self.Stop_pushButton.setEnabled(False)
        self.Stop_pushButton.setStyleSheet("color: rgb(153, 153, 153);\n"
                                           "background-color: rgb(255, 255, 255)\n")
        self.OK_pushButton.setEnabled(True)
        self.OK_pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255)\n")
        self.SaveText_toolButton.setStyleSheet("background-color: rgb(128, 128, 128)\n")
        self.ExportFileFormat_comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(255, 255, 255)\n")

        self.setWindowTitle("The analysis is complete. Please click the 'OK' button to review the results.")
        Status.MC = 1
        return

    @Slot()
    def on_SaveText_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ##raise NotImplementedError
        DirFile, Filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save Moment Curvature Output Text", self.cwd,
                                                                  "Text Files (*.txt)")
        # print("Current Save DataFilePath=", DirFile)
        if DirFile == "":
            self.MCMessageBox_textBrowser.setFont(QFont("Courier", 10))
            self.MCMessageBox_textBrowser.append(QTime.currentTime().toString() + ": Cancel save output text file!")
            return
        else:
            fileinfo = QFileInfo(DirFile)
            tfilename = fileinfo.baseName()
            # tfilesuff = fileinfo.suffix()
            # print("File basename=", tfilename)
            # print("Filename suffix=", tfilesuff)
            # with open((str(tfilename) + '-Result output.txt'), 'w', encoding='utf-8') as f:
            with open((DirFile + '.txt'), 'w', encoding='utf-8') as f:
                f.write(self.MCMessageBox_textBrowser.toPlainText())
            self.MCMessageBox_textBrowser.append(
                QTime.currentTime().toString() + (': The log file have been successfully saved.'))

