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


class SectionDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,mw,id, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(SectionDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 限制窗口大小不变
          # 获得id
        self.id = id
        self.mw = mw
        self.initDialog()
        self.getSectionInfo(id)

        # 初始化窗口设置

    def initDialog(self):
        self.SecID.setEnabled(False)

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


    def getSectionInfo(self, id):
        self.SecID.setText(str(id))
        self.MatID.setText(str(msaModel.Sect.MatID[id]))
        self.A.setText(str(msaModel.Sect.A[id]))
        self.Iz.setText(str(msaModel.Sect.Iz[id]))
        self.Iy.setText(str(msaModel.Sect.Iy[id]))
        self.J.setText(str(msaModel.Sect.J[id]))
        self.Iw.setText(str(msaModel.Sect.Iw[id]))
        self.yc.setText(str(msaModel.Sect.yc[id]))
        self.zc.setText(str(msaModel.Sect.zc[id]))
        self.ky.setText(str(msaModel.Sect.ky[id]))
        self.kz.setText(str(msaModel.Sect.kz[id]))
        self.betay.setText(str(msaModel.Sect.betay[id]))
        self.betaz.setText(str(msaModel.Sect.betaz[id]))
        self.betaw.setText(str(msaModel.Sect.betaw[id]))


    @Slot()
    def on_OKButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
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

            IdList = msaModel.Mat.ID
            if MatID not in IdList:
                showMesbox(self, 'Material ID not exist!')
            else:
                msaModel.Sect.Modify(tID=self.id,tMatID=MatID,tA=A,tIy=Iy,tIz=Iz,tJ=J,tIw=Iw,tyc=yc,tzc=zc,tky=ky,tkz=kz,tbetay=betay,tbetaz=betaz,tbetaw=betaw)
                self.mw.ResetTreeAndTable()
                self.accept()

        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

