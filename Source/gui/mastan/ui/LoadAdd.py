# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_LoadInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel

class LoadAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(LoadAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 限制窗口大小不变
          # 获得id
        self.mw = mw
        self.initDialog()

        # 初始化窗口设置

    def initDialog(self):
        intValidator = QIntValidator(self)
        self.NodeID.setValidator(intValidator)
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


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            LoadList=[]
            NodeIdList = msaModel.Node.ID
            LoadNodeIdList = msaModel.Load.NodeID
            NodeID = int(self.NodeID.text())
            if NodeID not in NodeIdList:
                showMesbox(self, 'Node ID not exist!')
            elif NodeID in LoadNodeIdList:
                showMesbox(self, ' The node ID has been used!')
            else:
                for i in self.LineEditList:
                    LoadList.append(float(i.text()))
                msaModel.Load.Add(NodeID,LoadList)
                self.mw.DelAllBottomItem()
                self.mw.importDataToTree()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
