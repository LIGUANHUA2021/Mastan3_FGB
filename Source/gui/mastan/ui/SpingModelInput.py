# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_SpingModelInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel


class SpringModelDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw,id,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(SpringModelDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 限制窗口大小不变
        # 获得id
        self.id = id
        self.mw = mw
        self.initDialog()
        self.getInfo(id)

        # 初始化窗口设置
    def initDialog(self):
        self.ID_Input.setEnabled(False)

    def getInfo(self, id):
        self.ID_Input.setText(str(id))
        for i in range(len(msaModel.SpringModel.Dis[id])):
            self.plainTextEdit.appendPlainText(str(msaModel.SpringModel.F[id][i])+' '+str(msaModel.SpringModel.Dis[id][i]))


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            tempText=self.plainTextEdit.toPlainText()
            tempList=tempText.split('\n')
            Dis_List=[]
            F_List=[]
            for i in range(len(tempList)):
                tempList2=tempList[i].split(' ')
                Dis_List.append(float(tempList2[0]))
                F_List.append(float(tempList2[1]))
            msaModel.SpringModel.Modify(self.id,Dis_List,F_List)
            self.mw.ResetTreeAndTable()
            self.accept()
            # print('-------------------------')
            # print(tempList)
            # print(Dis_List)
            # print(F_List)
            # print('-------------------------')
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()



