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

class MaterialAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MaterialAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.mw = mw
        self.initDialog()

    # 初始化窗口设置
    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        IdList = msaModel.Mat.ID
        if IdList == []:
            AddId = 1
        else:
            maxId = max(IdList)
            AddId = maxId + 1
        self.MatID_Input.setText(str(AddId))
        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)

        self.E_Input.setValidator(doubleValidator)
        self.G_Input.setValidator(doubleValidator)

    
    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            E = float(self.E_Input.text())
            G = float(self.G_Input.text())
            id = int(self.MatID_Input.text())
            MatIdList = msaModel.Mat.ID
            if id in MatIdList:
                showMesbox(self, 'Material ID has been used!')
            else:
                msaModel.Mat.Add(id,E,G,100)
                self.mw.ResetTreeAndTable()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
