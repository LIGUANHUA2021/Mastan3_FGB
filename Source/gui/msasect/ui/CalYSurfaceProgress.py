# -*- coding: utf-8 -*-

"""
Module implementing CalYSProgress.
"""

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from .Ui_CalYSurfaceProgress import Ui_CalYSProgress


class CalYSProgress(QWidget, Ui_CalYSProgress):
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
        self.setWindowIcon(QIcon("ui/ico/YieldSurface.ico"))
        self.initDialog()

    def initDialog(self):
        self.CalYS_progressBar.setValue(0)
        self.setWindowModality(Qt.WindowModal)

    @Slot()
    def on_OK_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QWidget.close(self)

    def Complete(self):
        self.CalYS_progressBar.setValue(100)
        self.Info_textLabel.setText("Calculate yield surface completely!")