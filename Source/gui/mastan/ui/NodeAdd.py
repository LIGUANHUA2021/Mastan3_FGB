# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog, QApplication

from gui.mastan.ui.Ui_NodeInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel



class NodeAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(NodeAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height()) #限制窗口大小不变
        self.mw=mw
        self.initDialog()

    #初始化窗口设置
    def initDialog(self):
        try:
            # self.ID_Input.setEnabled(False)
            NodeIdList=msaModel.Node.ID
            if NodeIdList == []:
                AddId = 1
            else:
                maxId = max(NodeIdList)
                AddId = maxId + 1
            self.ID_Input.setText(str(AddId))
            #设置validator
            doubleValidator = QDoubleValidator(bottom=-999,top=999)

            self.y_coordinate.setValidator(doubleValidator)
            self.x_coordinate.setValidator(doubleValidator)
            self.z_coordinate.setValidator(doubleValidator)
        except:
            traceback.print_exc()



    @Slot()
    def on_AcceptButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            x_coordinate=float(self.x_coordinate.text())
            y_coordinate=float(self.y_coordinate.text())
            z_coordinate=float(self.z_coordinate.text())
            id=int(self.ID_Input.text())
            NodeIdList = msaModel.Node.ID
            if id in NodeIdList:
                showMesbox(self, 'Node ID has been used!')
            else:
                msaModel.Node.Add(tID=id,tx=x_coordinate,ty=y_coordinate,tz=z_coordinate)
                self.mw.ResetTreeAndTable()
                self.accept()

        except:
            showMesbox(self,'Please enter correct data!')
            traceback.print_exc()
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     ui = NodeDialog()
#     ui.show()
#     sys.exit(app.exec())