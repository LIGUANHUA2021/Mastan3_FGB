# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QDialog
from gui.msasect.ui.Ui_About import Ui_Dialog
from gui.msasect.file import WelcomeInfo
from gui.msasect.base.Setting import Program

class AboutDialog(QDialog, Ui_Dialog):
    """
        Class documentation goes here.
        """

    def __init__(self, Version, parent=None):
        """
                Constructor

                @param parent reference to the parent widget (defaults to None)
                @type QWidget (optional)
                """
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/About.png'))
        plot1 = QPixmap('ui/ico/Msa_Sect2_170.png')
        self.label.setPixmap(plot1)
        self.label.setScaledContents(True)
        self.setFixedSize(self.width(), self.height())
        #self.label_13.setText(QCoreApplication.translate("Dialog", "Bucknell University" + "\n" + Version))
        self.initDialog()

    def initDialog(self):
        self.lineEdit_Version.setText(Program.Version)
        self.lineEdit_lastUpdatedDate.setText(Program.Revised)
        self.lineEdit_Version.setEnabled(False)
        self.lineEdit_lastUpdatedDate.setEnabled(False)