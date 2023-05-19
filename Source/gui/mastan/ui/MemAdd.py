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

class MemberAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MemberAddDialog, self).__init__(parent)
        self.setupUi(self)

        self.mw=mw
        self.initDialog()


    #初始化窗口设置
    def initDialog(self):
        # self.MemID_Input.setEnabled(False)
        MemIdList = msaModel.Member.ID
        if MemIdList == []:
            AddId = 1
        else:
            maxId = max(MemIdList)
            AddId = maxId + 1
        self.MemID_Input.setText(str(AddId))
        #设置validator
        intValidator = QIntValidator(self)
        self.Node1ID_Input.setValidator(intValidator)
        self.Node2ID_Input.setValidator(intValidator)
        self.SectionID_Input.setValidator(intValidator)


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            MemIdList=msaModel.Member.ID
            NodeIdList=msaModel.Node.ID
            SectionIdList=msaModel.Sect.ID

            Node1ID=int(self.Node1ID_Input.text())
            Node2ID=int(self.Node2ID_Input.text())
            SectionID=int(self.SectionID_Input.text())
            id=int(self.MemID_Input.text())

            if id in MemIdList :
                showMesbox(self, 'Member ID has been used!')
            elif Node1ID not in NodeIdList :
                showMesbox(self,'Node1ID not exist!')
            elif Node2ID not in NodeIdList :
                showMesbox(self,'Node2ID not exist!')
            elif SectionID not in SectionIdList :
                showMesbox(self,'SectionID not exist!')
            else:
                msaModel.Member.Add(id,SectionID,Node1ID,Node2ID)
                self.mw.ResetTreeAndTable()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     ui = MemberDialog()
#     ui.show()
#     sys.exit(app.exec())