# -*- coding: utf-8 -*-

"""
Module implementing StressAnalysisAnalDialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from gui.msasect.ui.Ui_AnalStressAnalysis import Ui_StressAnal_Dialog


class StressAnalysisAnalDialog(QDialog, Ui_StressAnal_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/StressAnalysis.png'))
        self.ShowResults_pushButton.setDisabled(True)
        ##
        ## Under Developing
        self.Run_pushButton.setEnabled(False)
        self.ShowResults_pushButton.setEnabled(False)

    @Slot()
    def on_Run_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

    @Slot()
    def on_ShowResults_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
