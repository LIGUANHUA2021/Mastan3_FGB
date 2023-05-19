# -*- coding: utf-8 -*-

"""
Module implementing GlobalBucklingAnal_Dialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from gui.msasect.ui.Ui_AnalGlobalBuckling import Ui_GlobalBucklingAnal_Dialog


class GlobalBucklingAnal_Dialog(QDialog, Ui_GlobalBucklingAnal_Dialog):
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

    @Slot()
    def on_Run_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
