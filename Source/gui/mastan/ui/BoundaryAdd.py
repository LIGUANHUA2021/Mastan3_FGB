# -*- coding: utf-8 -*-

"""
Module implementing dialog.
"""
import traceback

from PySide6.QtCore import Slot,Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_BoundaryInput import Ui_dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel


class BoundaryAddDialog(QDialog, Ui_dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(BoundaryAddDialog, self).__init__(parent)
        self.setupUi(self)

        self.mw=mw
        self.initDialog()


    #初始化窗口设置
    def initDialog(self):
        intValidator = QIntValidator(self)
        self.NodeID.setValidator(intValidator)
        self.CheckBoxList=[self.Ux,
                    self.Uy,
                    self.Uz,
                    self.Rx,
                    self.Ry,
                    self.Rz,
                      ]


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            BoundaryList=[]
            NodeIdList = msaModel.Node.ID
            LoadNodeIdList = msaModel.Bound.NodeID
            NodeID = int(self.NodeID.text())
            if NodeID not in NodeIdList:
                showMesbox(self, 'Node ID not exist!')
            elif NodeID in LoadNodeIdList:
                showMesbox(self, ' The node ID has been used!')
            else:
                for i in self.CheckBoxList:
                    if i.isChecked():
                        BoundaryList.append(1)
                    else:
                        BoundaryList.append(0)
                msaModel.Bound.Add(NodeID,BoundaryList)
                self.mw.DelAllBottomItem()
                self.mw.importDataToTree()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()