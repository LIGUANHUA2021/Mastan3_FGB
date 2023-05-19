# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_LoadInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel

class LoadDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,id, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(LoadDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 限制窗口大小不变
          # 获得id
        self.id = id
        self.mw = mw
        self.initDialog()
        self.getLoadInfo(id)

        # 初始化窗口设置

    def initDialog(self):
        self.NodeID.setEnabled(False)

        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)

        self.Fx.setValidator(doubleValidator)
        self.Fy.setValidator(doubleValidator)
        self.Fz.setValidator(doubleValidator)
        self.Mx.setValidator(doubleValidator)
        self.My.setValidator(doubleValidator)
        self.Mz.setValidator(doubleValidator)

        self.LineEditList=[self.Fx,
                    self.Fy,
                    self.Fz,
                    self.Mx,
                    self.My,
                    self.Mz,
                      ]

    def getLoadInfo(self, id):
        self.NodeID.setText(str(id))
        LoadList=msaModel.Load.LoadVector[self.id]
        for i in range(len(self.LineEditList)):
            LineEdit = self.LineEditList[i]
            LineEdit.setText(str(float(LoadList[i])))

    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            LoadList=[]
            for i in self.LineEditList:
                LoadList.append(float(i.text()))
            msaModel.Load.Modify(self.id,LoadList)
            self.mw.ResetTreeAndTable()
            self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
