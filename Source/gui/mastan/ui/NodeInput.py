# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog, QApplication

from gui.mastan.ui.Ui_NodeInput import Ui_Dialog
from gui.mastan.base.model import msaModel


class NodeDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw,id,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(NodeDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height()) #限制窗口大小不变
        self.getNodeInfo(id) #获得id
        self.id=id
        self.mw=mw
        self.initDialog()

    #初始化窗口设置
    def initDialog(self):
        self.ID_Input.setEnabled(False)

        #设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)
        self.y_coordinate.setValidator(doubleValidator)
        self.x_coordinate.setValidator(doubleValidator)
        self.z_coordinate.setValidator(doubleValidator)

    def getNodeInfo(self,id):
        self.ID_Input.setText(str(id))
        self.y_coordinate.setText(str(msaModel.Node.y[id]))
        self.x_coordinate.setText(str(msaModel.Node.x[id]))
        self.z_coordinate.setText(str(msaModel.Node.z[id]))

    @Slot()
    def on_AcceptButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        x_coordinate=float(self.x_coordinate.text())
        y_coordinate=float(self.y_coordinate.text())
        z_coordinate=float(self.z_coordinate.text())
        msaModel.Node.Modify(tID=self.id,tx=x_coordinate,ty=y_coordinate,tz=z_coordinate)
        # self.mw.InputW.clear()
        # self.mw.initTree()
        # self.mw.importDataToTree()
        self.mw.ResetTreeAndTable()
        self.accept()

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     ui = NodeDialog()
#     ui.show()
#     sys.exit(app.exec())