# -*- coding: utf-8 -*-

"""
Module implementing dialog.
"""
import traceback

from PySide6.QtCore import Slot,Qt
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_BoundaryInput import Ui_dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel


class BoundaryDialog(QDialog, Ui_dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw, NodeId,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(BoundaryDialog, self).__init__(parent)
        self.setupUi(self)
        self.Id=NodeId
        self.mw=mw
        self.initDialog()
        self.getBoundaryInfo(NodeId)

    #初始化窗口设置
    def initDialog(self):
        self.NodeID.setEnabled(False)
        self.CheckBoxList=[self.Ux,
                    self.Uy,
                    self.Uz,
                    self.Rx,
                    self.Ry,
                    self.Rz,
                      ]


    def getBoundaryInfo(self,id):
        try:
            self.NodeID.setText(str(id))
            BoundaryList=msaModel.Bound.Bound[id]

            for i in range(len(self.CheckBoxList)):
                CheckBox=self.CheckBoxList[i]
                if BoundaryList[i] == 1:
                    CheckBox.setCheckState(Qt.CheckState.Checked)
        except:
            traceback.print_exc()



    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            BoundaryList=[]
            for i in self.CheckBoxList:
                if i.isChecked():
                    BoundaryList.append(1)
                else:
                    BoundaryList.append(0)
            msaModel.Bound.Modify(self.Id,BoundaryList)
            self.mw.ResetTreeAndTable()
            self.accept()
        except:
            traceback.print_exc()