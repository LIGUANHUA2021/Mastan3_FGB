# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import re
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_SpringBoundaryInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel

class SpringBoundaryAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(SpringBoundaryAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 限制窗口大小不变
        # 获得id
        self.id = id
        self.mw =mw
        self.comboBoxList = [self.comboBox_Ux,
                             self.comboBox_Uy,
                             self.comboBox_Uz,
                             self.comboBox_Rx,
                             self.comboBox_Ry,
                             self.comboBox_Rz, ]
        self.springIDList = msaModel.SpringModel.ID
        self.initDialog()


        # 初始化窗口设置

    def initDialog(self):
        intValidator = QIntValidator(self)
        self.NodeID.setValidator(intValidator)
        springIDList_str=['free']
        for i in self.springIDList :
            springIDList_str.append('spring '+str(i))
        self.comboBox_Ux.addItems(springIDList_str)
        self.comboBox_Uy.addItems(springIDList_str)
        self.comboBox_Uz.addItems(springIDList_str)
        self.comboBox_Rx.addItems(springIDList_str)
        self.comboBox_Ry.addItems(springIDList_str)
        self.comboBox_Rz.addItems(springIDList_str)


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            id=int(self.NodeID.text())
            NodeIdList = msaModel.Node.ID
            LoadNodeIdList = msaModel.SpringBoundary.NodeID
            NodeID = int(self.NodeID.text())
            if NodeID not in NodeIdList:
                showMesbox(self, 'Node ID not exist!')
            elif NodeID in LoadNodeIdList:
                showMesbox(self, ' The node ID has been used!')
            else:
                f=lambda comboBox: 0 if comboBox.currentText() == 'free' else int(re.findall(r"\d+", comboBox.currentText())[0])
                BoundaryList=[]
                for i in self.comboBoxList:
                    BoundaryList.append(f(i))
                msaModel.SpringBoundary.Add(id,BoundaryList)
                self.mw.ResetTreeAndTable()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()
