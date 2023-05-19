# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_MaterialInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel

class MaterialDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,id,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MaterialDialog, self).__init__(parent)
        self.setupUi(self)
        self.getMaterialInfo(id)  # 获得id
        self.id = id
        self.mw = mw
        self.initDialog()

    # 初始化窗口设置
    def initDialog(self):
        self.MatID_Input.setEnabled(False)

        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)

        self.E_Input.setValidator(doubleValidator)
        self.G_Input.setValidator(doubleValidator)

    def getMaterialInfo(self,id):
        self.MatID_Input.setText(str(id))
        self.E_Input.setText(str(msaModel.Mat.E[id]))
        self.G_Input.setText(str(msaModel.Mat.G[id]))
    
    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            E = float(self.E_Input.text())
            G = float(self.G_Input.text())
            msaModel.Mat.Modify(self.id,E,G,100)
            self.mw.ResetTreeAndTable()
            self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
