# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import QDialog

from gui.mastan.ui.Ui_SectionInput import Ui_Dialog
from gui.mastan.ui.msgBox import showMesbox
from gui.mastan.base.model import msaModel


class SectionAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(SectionAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 限制窗口大小不变
          # 获得id
        self.mw = mw
        self.initDialog()

        # 初始化窗口设置

    def initDialog(self):
        # self.SecID.setEnabled(False)
        IdList = msaModel.Sect.ID
        if IdList == []:
            AddId = 1
        else:
            maxId = max(IdList)
            AddId = maxId + 1
        self.SecID.setText(str(AddId))
        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)
        intValidator = QIntValidator(self)
        self.MatID.setValidator(intValidator)
        self.A.setValidator(doubleValidator)
        self.Iy.setValidator(doubleValidator)
        self.Iz.setValidator(doubleValidator)
        self.J.setValidator(doubleValidator)
        self.Iw.setValidator(doubleValidator)
        self.yc.setValidator(doubleValidator)
        self.zc.setValidator(doubleValidator)
        self.ky.setValidator(doubleValidator)
        self.kz.setValidator(doubleValidator)
        self.betay.setValidator(doubleValidator)
        self.betaz.setValidator(doubleValidator)
        self.betaw.setValidator(doubleValidator)



    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            id=int(self.SecID.text())
            MatID=int(self.MatID.text())
            A=float(self.A.text())
            Iy=float(self.Iy.text())
            Iz=float(self.Iz.text())
            J=float(self.J.text())
            Iw=float(self.Iw.text())
            yc=float(self.yc.text())
            zc=float(self.zc.text())
            ky=float(self.ky.text())
            kz=float(self.kz.text())
            betay=float(self.betay.text())
            betaz=float(self.betaz.text())
            betaw=float(self.betaw.text())

            SectIdList = msaModel.Sect.ID
            MatIdList = msaModel.Mat.ID
            if id in SectIdList:
                showMesbox(self, 'Section ID has been used!')
            elif MatID not in MatIdList:
                showMesbox(self, 'Material ID not exist!')
            else:
                msaModel.Sect.Add(tID=id,tMatID=MatID,tA=A,tIy=Iy,tIz=Iz,tJ=J,tIw=Iw,tyc=yc,tzc=zc,tky=ky,tkz=kz,tbetay=betay,tbetaz=betaz,tbetaw=betaw)
                self.mw.ResetTreeAndTable()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

