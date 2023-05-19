# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import QDialog, QApplication

from gui.mastan.ui.Ui_MemInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel

class MemberDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw,id,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MemberDialog, self).__init__(parent)
        self.setupUi(self)
        self.id=id
        self.mw=mw
        self.initDialog()
        self.getMemberInfo(id)

    #初始化窗口设置
    def initDialog(self):
        self.MemID_Input.setEnabled(False)
        #设置validator
        doubleValidator = QIntValidator(self)
        self.Node1ID_Input.setValidator(doubleValidator)
        self.Node2ID_Input.setValidator(doubleValidator)
        self.SectionID_Input.setValidator(doubleValidator)

    def getMemberInfo(self,id):
        self.MemID_Input.setText(str(id))
        self.Node1ID_Input.setText(str(msaModel.Member.NodeI[id]))
        self.Node2ID_Input.setText(str(msaModel.Member.NodeJ[id]))
        self.SectionID_Input.setText(str(msaModel.Member.SectionID[id]))

    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            NodeIdList=msaModel.Node.ID
            SectionIdList=msaModel.Sect.ID
            Node1ID=int(self.Node1ID_Input.text())
            Node2ID=int(self.Node2ID_Input.text())
            SectionID=int(self.SectionID_Input.text())
            if Node1ID not in NodeIdList :
                showMesbox(self,'Node I is not existed!')
            elif Node2ID not in NodeIdList :
                showMesbox(self,'Node J is not existed!')
            elif SectionID not in SectionIdList :
                showMesbox(self,'Section is not existed!')
            else:
                msaModel.Member.Modify(self.id,SectionID,Node1ID,Node2ID)
                self.mw.ResetTreeAndTable()
                self.accept()
        except:
            traceback.print_exc()


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     ui = MemberDialog()
#     ui.show()
#     sys.exit(app.exec())