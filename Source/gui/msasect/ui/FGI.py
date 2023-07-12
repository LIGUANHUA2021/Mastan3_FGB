# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_FGI import Ui_FGI_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel, msaFEModel, GlobalBuckling, Status
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class FGI_Dialog(QDialog, Ui_FGI_Dialog):
    """
    Class documentation goes here.
    """
    Methodsignal = Signal(int)
    def __init__(self, mw, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/FG-I.ico'))
        self.color = []
        # self.showImage()
        self.mw = mw
        self.initDialog()
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
        self.method = 1
        self.Law=1
        self.Law_comboBox.currentIndexChanged.connect(self.Law_add)
        self.k_inputlineEdit.show()
        self.label_4.show()

    def Law_add(self):
        if self.Law_comboBox.currentText() == "Power law":
            self.Law= 1
            self.k_inputlineEdit.show()
            self.label_4.show()
            self.label.setPixmap(QPixmap("ui/Template/FG-I_1.jpg"))
        elif self.Law_comboBox.currentText() == "Exponential law":
            self.Law= 2
            self.k_inputlineEdit.hide()
            self.label_4.hide()
            self.label.setPixmap(QPixmap("ui/Template/FG-I_2.jpg"))
        elif self.Law_comboBox.currentText() == "Sigmoid law":
            self.Law= 3
            self.k_inputlineEdit.show()
            self.label_4.show()
            self.label.setPixmap(QPixmap("ui/Template/FG-I_3.jpg"))

    def initDialog(self):
        self.label.setPixmap(QPixmap("ui/Template/FG-I_1.jpg"))
        self.fy_inputlineEdit.setText(str(345))
        self.eu_inputlineEdit.setText(str(0.15))
        self.G_inputlineEdit.setText(str(0.3))
        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)
        intValidator = QIntValidator()
        self.k_inputlineEdit.setValidator(doubleValidator)
        self.Ei_inputlineEdit.setValidator(doubleValidator)
        self.E0_inputlineEdit.setValidator(doubleValidator)
        self.G_inputlineEdit.setValidator(doubleValidator)
        self.fy_inputlineEdit.setValidator(doubleValidator)
        self.eu_inputlineEdit.setValidator(doubleValidator)

        self.B1_inputlineEdit.setValidator(doubleValidator)
        self.B2_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.tf_inputlineEdit.setValidator(doubleValidator)
        self.tw_inputlineEdit.setValidator(doubleValidator)
        self.Num_inputlineEdit.setValidator(intValidator)

        self.B1_inputlineEdit.setText(str(50))
        self.B2_inputlineEdit.setText(str(50))
        self.D_inputlineEdit.setText(str(100))
        self.Num_inputlineEdit.setText(str(int(20)))
        self.Ei_inputlineEdit.setText(str(205000))
        self.E0_inputlineEdit.setText(str(70000))
        self.k_inputlineEdit.setText(str(0.8))
        self.tf_inputlineEdit.setText(str(6))
        self.tw_inputlineEdit.setText(str(4))

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.method = 0

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.method = 1


    @Slot()
    def on_OK_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        Stress_input = 0
        try:
            if len(self.Ei_inputlineEdit.text()) == 0 or len(self.E0_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0 or len(
                    self.fy_inputlineEdit.text()) == 0 or len(self.eu_inputlineEdit.text()) == 0 or len(self.B1_inputlineEdit.text()) == 0 or len(self.B2_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or\
                    len(self.Num_inputlineEdit.text()) == 0 or len(self.tf_inputlineEdit.text()) == 0 or len(self.tw_inputlineEdit.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
                msaModel.ResetAll()
                msaModel.Mat.Reset()
                msaModel.Point.Reset()
                msaModel.Segment.Reset()
                msaFEModel.ResetAll()
                msaFEModel.Mat.Reset()
                msaFEModel.Point.Reset()
                msaFEModel.Outline.Reset()
                msaFEModel.Loop.Reset()
                msaFEModel.Group.Reset()
                Ei = float(self.Ei_inputlineEdit.text())
                E0 = float(self.E0_inputlineEdit.text())
                k = float(self.k_inputlineEdit.text())
                tμ = float(self.G_inputlineEdit.text())
                tfy = float(self.fy_inputlineEdit.text())
                teu = float(self.eu_inputlineEdit.text())
                B1 = float(self.B1_inputlineEdit.text())
                B2 = float(self.B2_inputlineEdit.text())
                D = float(self.D_inputlineEdit.text())
                tf = float(self.tf_inputlineEdit.text())
                tw = float(self.tw_inputlineEdit.text())
                StripNum=int(self.Num_inputlineEdit.text())
                MatIdDict = msaFEModel.Mat.ID
                if Ei<0 or E0<0 or k<0 or tμ<0 or tfy<0 or teu<0 or B1<0 or B2<0 or D<0 or StripNum<3 or D<tf*2 or B1<=tw or B2<=tw :
                    showMesbox(self, 'Please input correct data!')
                else:
                    values = [int(i * (255-30) / StripNum+32) for i in range(StripNum)]
                    colors = ["#%02x%02x%02x" % (int(g), int(g), int(g)) for g in values]
                    if len(MatIdDict)!=0:
                        id = max(MatIdDict)
                    else:
                        id=0
                    va= [float(i+0.5) for i in range(StripNum)]
                    if self.Law== 1:
                        E=[float(round(E0+(Ei-E0)*(n/StripNum)**k, 3)) for n in va]
                    elif self.Law==2:
                        E=[float(round(E0*np.exp((n/StripNum)*np.log(Ei/E0)), 3)) for n in va]
                    elif self.Law==3:
                        if StripNum % 2 == 0:
                            StripNum+=0
                        else:
                            StripNum+=1
                        colors =[]
                        E = []
                        values = [int(i * 250 / (StripNum/2)) for i in range(int(StripNum/2))]
                        E1=[round(E0+(Ei-E0)*(1-(n/StripNum)**k), 3) for n in va]
                        E2=[round(E0+(Ei-E0)*(n/StripNum)**k, 3) for n in va]
                        color1 = ["#%02x%02x%02x" % (int(g), 255, 255) for g in values]
                        color2 = ["#%02x%02x%02x" % (255-int(g), 255, 255) for g in values]
                        for i in range(int(StripNum/2)):
                            E.append(E2[i])
                            colors.append(color2[i])
                        for i in range(int(StripNum/2)):
                            E.append(E1[int(StripNum/2-i-1)])
                            colors.append(color1[i])
                    for i in range(StripNum):
                        msaFEModel.Mat.Add(tID=id+i+1, tE=E[i], tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=colors[i])
                        self.accept()
                    Rva = float(D/StripNum)
                    tf_num=round(tf/Rva)
                    if tf_num<=1:
                        tf_num=1
                        Rva=float(D-2*tf)/(StripNum-2)
                    elif tf_num > 1:
                        Rva_tf=float(tf/tf_num)
                        Rva_tw=float((D-2*tf)/(StripNum-2*tf_num))

                    if tf_num==1:
                        msaFEModel.Point.Add(tID=1, ty=round(0, 3), tz=round(0, 3))
                        msaFEModel.Point.Add(tID=2, ty=round(0, 3), tz=round(B1, 3))
                        msaFEModel.Point.Add(tID=3, ty=round(-tf, 3), tz=round(B1,3))
                        msaFEModel.Point.Add(tID=4, ty=round(-tf, 3), tz=round(0.5*B1+0.5*tw, 3))
                        msaFEModel.Point.Add(tID=5, ty=round(-tf,3), tz=round(0.5*B1-0.5*tw, 3))
                        msaFEModel.Point.Add(tID=6, ty=round(-tf, 3),tz=round(0, 3))
                        for ii in range(StripNum - 2):
                            msaFEModel.Point.Add(tID=7 + ii * 4, ty=round(-tf-Rva*ii, 3),tz=round(0.5 * B1 - 0.5 * tw, 3))
                            msaFEModel.Point.Add(tID=8 + ii * 4, ty=round(-tf-Rva*ii, 3),tz=round(0.5 * B1 + 0.5 * tw, 3))
                            msaFEModel.Point.Add(tID=9 + ii * 4, ty=round(-tf-Rva*(ii+1), 3),tz=round(0.5 * B1 + 0.5 * tw, 3))
                            msaFEModel.Point.Add(tID=10 + ii * 4, ty=round(-tf-Rva*(ii+1), 3),tz=round(0.5 * B1 - 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=4 * StripNum - 1, ty=round(-(StripNum - 2) * Rva-tf, 3),tz=round(0.5 * B1 - 0.5 * B2, 3))
                        msaFEModel.Point.Add(tID=4 * StripNum, ty=round(-(StripNum - 2) * Rva-tf, 3),tz=round(0.5 * B1 - 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=4 * StripNum + 1, ty=round(-(StripNum - 2) * Rva-tf, 3),tz=round(0.5 * B1 + 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=4 * StripNum + 2, ty=round(-(StripNum - 2) * Rva-tf, 3),tz=round(0.5 * B1 + 0.5 * B2, 3))
                        msaFEModel.Point.Add(tID=4 * StripNum + 3, ty=round(-D, 3),tz=round(0.5 * B1 + 0.5 * B2, 3))
                        msaFEModel.Point.Add(tID=4 * StripNum + 4, ty=round(-D, 3),tz=round(0.5 * B1 - 0.5 * B2, 3))
                        for i in range(5):
                            msaFEModel.Outline.Add(tID=1 + i, tGID=1 , tType="S", tLID=1 ,tPSID=i + 1 , tPEID=i + 2 )
                        msaFEModel.Outline.Add(tID=6, tGID=1, tType="S", tLID=1 ,tPSID=6, tPEID=1)
                        for ii in range(StripNum-2):
                            for i in range(3):
                                msaFEModel.Outline.Add(tID=7 + i + ii * 4, tGID=2 + ii, tType="S", tLID=2 + ii,tPSID=i + 7 + ii * 4, tPEID=i + 8 + ii * 4)
                            msaFEModel.Outline.Add(tID=10 + ii * 4, tGID=2 + ii, tType="S", tLID=2 + ii,tPSID=10 + ii * 4, tPEID=7 + ii * 4)
                        for i in range(5):
                            msaFEModel.Outline.Add(tID=4 * StripNum - 1 + i, tGID=StripNum , tType="S", tLID=StripNum ,tPSID=4 * StripNum - 1 + i , tPEID=4 * StripNum + i )
                        msaFEModel.Outline.Add(tID=4 * StripNum + 4, tGID=StripNum, tType="S", tLID=StripNum ,tPSID=4 * StripNum + 4, tPEID=4 * StripNum - 1)
                        tOID = [[1,2,3,4,5,6]]
                        for ii in range(StripNum-2):
                            ID = []
                            for i in range(4):
                                ID.append(int(i + 7 + ii * 4))
                            tOID.append(ID)
                        IDr = []
                        for i in range(6):
                            IDr.append(int(4 * StripNum - 1+i))
                        tOID.append(IDr)
                        for ii in range(len(tOID)):
                            msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                        for i in range(StripNum):
                            msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[i + 1])
                    else:
                        for ii in range(tf_num-1):
                            msaFEModel.Point.Add(tID=1+4*ii, ty=round(-Rva_tf*ii, 3), tz=round(0, 3))
                            msaFEModel.Point.Add(tID=2+4*ii, ty=round(-Rva_tf*ii, 3), tz=round(B1, 3))
                            msaFEModel.Point.Add(tID=3+4*ii, ty=round(-Rva_tf*(ii+1), 3), tz=round(B1, 3))
                            msaFEModel.Point.Add(tID=4+4*ii, ty=round(-Rva_tf*(ii+1), 3), tz=round(0, 3))
                        msaFEModel.Point.Add(tID=5+4*(tf_num-2), ty=round((-(tf_num-1)*Rva_tf), 3), tz=round(0, 3))
                        msaFEModel.Point.Add(tID=6+4*(tf_num-2), ty=round(-(tf_num-1)*Rva_tf, 3), tz=round(B1, 3))
                        msaFEModel.Point.Add(tID=7+4*(tf_num-2), ty=round(-tf, 3), tz=round(B1, 3))
                        msaFEModel.Point.Add(tID=8+4*(tf_num-2), ty=round(-tf, 3), tz=round(0.5 * B1 + 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=9+4*(tf_num-2), ty=round(-tf, 3), tz=round(0.5 * B1 - 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=10+4*(tf_num-2), ty=round(-tf, 3), tz=round(0, 3))
                        for ii in range(StripNum - 2*tf_num):
                            msaFEModel.Point.Add(tID=11+4*(tf_num-2) + ii * 4, ty=round(-tf-Rva_tw*ii, 3),tz=round(0.5 * B1 - 0.5 * tw, 3))
                            msaFEModel.Point.Add(tID=12+4*(tf_num-2) + ii * 4, ty=round(-tf-Rva_tw*ii, 3),tz=round(0.5 * B1 + 0.5 * tw, 3))
                            msaFEModel.Point.Add(tID=13+4*(tf_num-2) + ii * 4, ty=round(-tf-Rva_tw*(ii+1), 3),tz=round(0.5 * B1 + 0.5 * tw, 3))
                            msaFEModel.Point.Add(tID=14+4*(tf_num-2) + ii * 4, ty=round(-tf-Rva_tw*(ii+1), 3),tz=round(0.5 * B1 - 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=3 + 4 * (StripNum-tf_num), ty=round((-tf-(StripNum - 2*tf_num) * Rva_tw), 3),tz=round(0.5 * B1 - 0.5 * B2, 3))
                        msaFEModel.Point.Add(tID=4 + 4 * (StripNum-tf_num), ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw, 3),tz=round(0.5 * B1 - 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=5 + 4 * (StripNum-tf_num), ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw, 3), tz=round(0.5 * B1 + 0.5 * tw, 3))
                        msaFEModel.Point.Add(tID=6 + 4 * (StripNum-tf_num), ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw, 3),tz=round(0.5 * B1 + 0.5 * B2, 3))
                        msaFEModel.Point.Add(tID=7 + 4 * (StripNum-tf_num), ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw-Rva_tf, 3),tz=round(0.5 * B1 + 0.5 * B2, 3))
                        msaFEModel.Point.Add(tID=8 + 4 * (StripNum-tf_num), ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw-Rva_tf, 3), tz=round(0.5 * B1 - 0.5 * B2, 3))
                        for ii in range(tf_num-1):
                            msaFEModel.Point.Add(tID=9 + 4 * (StripNum-tf_num)+4*ii, ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw-Rva_tf*(ii+1), 3), tz=round(0.5 * B1 - 0.5 * B2, 3))
                            msaFEModel.Point.Add(tID=10 + 4 * (StripNum-tf_num)+4*ii, ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw-Rva_tf*(ii+1), 3), tz=round(0.5 * B1 + 0.5 * B2, 3))
                            msaFEModel.Point.Add(tID=11 + 4 * (StripNum-tf_num)+4*ii, ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw-Rva_tf*(ii+2), 3), tz=round(0.5 * B1 + 0.5 * B2, 3))
                            msaFEModel.Point.Add(tID=12 + 4 * (StripNum-tf_num)+4*ii, ty=round(-tf-(StripNum - 2*tf_num) * Rva_tw-Rva_tf*(ii+2), 3), tz=round(0.5 * B1 - 0.5 * B2, 3))
                        for ii in range(tf_num-1):
                            for i in range(3):
                                msaFEModel.Outline.Add(tID=1 + i+4*ii, tGID=1+ii, tType="S", tLID=1+ii ,tPSID=1 + i+4*ii , tPEID=2 + i+4*ii )
                            msaFEModel.Outline.Add(tID=4+4*ii, tGID=1+ii, tType="S", tLID=1+ii ,tPSID=4+4*ii, tPEID=1+4*ii)
                        for i in range(5):
                            msaFEModel.Outline.Add(tID=1 + i + 4 * (tf_num-1), tGID=tf_num, tType="S", tLID=tf_num, tPSID=1 + i + 4 * (tf_num-1), tPEID=2 + i + 4 * (tf_num-1))
                        msaFEModel.Outline.Add(tID=6 + 4 * (tf_num-1), tGID=tf_num, tType="S", tLID=tf_num, tPSID=6 + 4 * (tf_num-1), tPEID=1 + 4 * (tf_num-1))
                        for ii in range(StripNum - 2*tf_num):
                            for i in range(3):
                                msaFEModel.Outline.Add(tID=7+i+4*ii + 4 * (tf_num-1), tGID=tf_num+ii+1, tType="S", tLID=tf_num+ii+1,tPSID=7+i+4*ii + 4 * (tf_num-1), tPEID=8+i+4*ii + 4 * (tf_num-1))
                            msaFEModel.Outline.Add(tID=10+4*ii + 4 * (tf_num-1), tGID=tf_num+ii+1, tType="S", tLID=tf_num+ii+1,tPSID=10+4*ii + 4 * (tf_num-1), tPEID=7+4*ii + 4 * (tf_num-1))
                        for i in range(5):
                            msaFEModel.Outline.Add(tID=3 + i + 4 * (StripNum-tf_num), tGID=StripNum-tf_num+1, tType="S", tLID=StripNum-tf_num+1, tPSID=3 + i + 4 * (StripNum-tf_num), tPEID=4 + i + 4 * (StripNum-tf_num))
                        msaFEModel.Outline.Add(tID=8 + 4 * (StripNum-tf_num), tGID=StripNum-tf_num+1, tType="S", tLID=StripNum-tf_num+1, tPSID=8 + 4 * (StripNum-tf_num), tPEID=3 + 4 * (StripNum-tf_num))
                        for ii in range(tf_num-1):
                            for i in range(3):
                                msaFEModel.Outline.Add(tID=9 + 4 * (StripNum-tf_num)+i+4*ii, tGID=StripNum-tf_num+2+ii, tType="S", tLID=StripNum-tf_num+2+ii ,tPSID=9 + 4 * (StripNum-tf_num)+i+4*ii , tPEID=10 + 4 * (StripNum-tf_num)+i+4*ii )
                            msaFEModel.Outline.Add(tID=12 + 4 * (StripNum-tf_num)+4*ii, tGID=StripNum-tf_num+2+ii, tType="S", tLID=StripNum-tf_num+2+ii ,tPSID=12 + 4 * (StripNum-tf_num)+4*ii, tPEID=9 + 4 * (StripNum-tf_num)+4*ii)

                        tOID = []
                        for ii in range(tf_num-1):
                            ID = []
                            for i in range(4):
                                ID.append(int(i + 1 + ii * 4))
                            tOID.append(ID)
                        ID1=[]
                        for i in range (6):
                            ID1.append(int(i + 5+4*(tf_num-2)))
                        tOID.append(ID1)
                        for ii in range(StripNum - 2*tf_num):
                            IDr = []
                            for i in range(4):
                                IDr.append(int(11+i+4*ii+4*(tf_num-2)))
                            tOID.append(IDr)
                        ID2=[]
                        for i in range (6):
                            ID2.append(int(3 + 4 * (StripNum-tf_num)+i))
                        tOID.append(ID2)
                        for ii in range(tf_num-1):
                            ID3 = []
                            for i in range(4):
                                ID3.append(int(9 + 4 * (StripNum-tf_num)+4*ii+i))
                            tOID.append(ID3)
                        for ii in range(len(tOID)):
                            msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                        for i in range(StripNum):
                            msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[i + 1])
                    # if tf < Rva:
                    #     msaFEModel.Point.Add(tID=1 , ty=np.around(0, decimals=3),tz=np.around(0, decimals=3))
                    #     msaFEModel.Point.Add(tID=2 , ty=np.around(0, decimals=3),tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=3 , ty=np.around(-tf, decimals=3),tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 , ty=np.around(-tf, decimals=3),tz=np.around(0.5*B1+0.5*tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=5, ty=np.around(-Rva, decimals=3),tz=np.around(0.5*B1+0.5*tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=6, ty=np.around(-Rva, decimals=3),tz=np.around(0.5*B1-0.5*tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=7, ty=np.around(-tf, decimals=3),tz=np.around(0.5*B1-0.5*tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=8, ty=np.around(-tf, decimals=3),tz=np.around(0, decimals=3))
                    #     for ii in range(StripNum-2):
                    #         msaFEModel.Point.Add(tID=9 + ii*4, ty=np.around(-Rva*(ii+1), decimals=3),tz=np.around(0.5*B1-0.5*tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=10 + ii*4, ty=np.around(-Rva*(ii+1), decimals=3),tz=np.around(0.5*B1+0.5*tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=11 + ii*4, ty=np.around(-Rva*(ii+2), decimals=3),tz=np.around(0.5*B1+0.5*tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=12 + ii*4, ty=np.around(-Rva*(ii+2), decimals=3),tz=np.around(0.5*B1-0.5*tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 1, ty=np.around(-(StripNum-1) * Rva, decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 2, ty=np.around(-(StripNum-1) * Rva, decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 3, ty=np.around(-D+tf, decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 4, ty=np.around(-D+tf, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 5, ty=np.around(-D, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 6, ty=np.around(-D, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 7, ty=np.around(-D+tf, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4*StripNum + 8, ty=np.around(-D+tf, decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     for i in range(7):
                    #         msaFEModel.Outline.Add(tID=1 + i, tGID=1 , tType="S", tLID=1 ,tPSID=i + 1 , tPEID=i + 2 )
                    #     msaFEModel.Outline.Add(tID=8, tGID=1 , tType="S", tLID=1 ,tPSID=8, tPEID=1 )
                    #     for ii in range(StripNum-2):
                    #         for i in range(3):
                    #             msaFEModel.Outline.Add(tID=9 +i+ ii*4, tGID=2+ii, tType="S", tLID=2+ii, tPSID=i+9+ii*4, tPEID=i+10+ii*4)
                    #         msaFEModel.Outline.Add(tID=12 + ii * 4, tGID=2 + ii, tType="S", tLID=2 + ii,tPSID=12+ ii * 4, tPEID=9+ii*4)
                    #     for i in range(7):
                    #         msaFEModel.Outline.Add(tID=4*StripNum+1+i, tGID=StripNum , tType="S", tLID=StripNum ,tPSID=i +4*StripNum + 1 , tPEID=i + 2+4*StripNum)
                    #     msaFEModel.Outline.Add(tID=4*StripNum+8, tGID=StripNum , tType="S", tLID=StripNum ,tPSID=8+4*StripNum, tPEID=4*StripNum +1 )
                    #     tOID = []
                    #     tOID.append([i+1 for i in range(8)])
                    #     for ii in range(StripNum-2):
                    #         ID = []
                    #         for i in range(4):
                    #             ID.append(int(i + 9 + ii * 4))
                    #         tOID.append(ID)
                    #     tOID.append([i+1+4*StripNum for i in range(8)])
                    #     for ii in range(len(tOID)):
                    #         msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                    #     for i in range(StripNum):
                    #         msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[i + 1])
                    # if tf == Rva:
                    #     msaFEModel.Point.Add(tID=1, ty=np.around(0, decimals=3), tz=np.around(0, decimals=3))
                    #     msaFEModel.Point.Add(tID=2, ty=np.around(0, decimals=3), tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=3, ty=np.around(-tf, decimals=3), tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=4, ty=np.around(-tf, decimals=3),tz=np.around(0, decimals=3))
                    #     for ii in range(StripNum - 2):
                    #         msaFEModel.Point.Add(tID=5 + ii * 4, ty=np.around(-Rva * (ii + 1), decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=6 + ii * 4, ty=np.around(-Rva * (ii + 1), decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=7 + ii * 4, ty=np.around(-Rva * (ii + 2), decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=8 + ii * 4, ty=np.around(-Rva * (ii + 2), decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum -3, ty=np.around(-(StripNum - 1) * Rva, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum -2, ty=np.around(-(StripNum - 1) * Rva, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum -1, ty=np.around(-D , decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum , ty=np.around(-D , decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     for ii in range(StripNum):
                    #         for i in range(3):
                    #             msaFEModel.Outline.Add(tID=1 +i+ ii*4, tGID=1+ii, tType="S", tLID=1+ii, tPSID=i+1+ii*4, tPEID=i+2+ii*4)
                    #         msaFEModel.Outline.Add(tID=4 + ii * 4, tGID=1 + ii, tType="S", tLID=1 + ii,tPSID=4+ ii * 4, tPEID=1+ii*4)
                    #         tOID = []
                    #     for ii in range(StripNum):
                    #         for ii in range(StripNum):
                    #             ID = []
                    #             for i in range(4):
                    #                 ID.append(int(i + 1 + ii * 4))
                    #             tOID.append(ID)
                    #         for ii in range(len(tOID)):
                    #             msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                    #         for i in range(StripNum):
                    #             msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[i + 1])
                    # if tf > Rva:
                    #     msaFEModel.Point.Add(tID=1, ty=np.around(0, decimals=3), tz=np.around(0, decimals=3))
                    #     msaFEModel.Point.Add(tID=2, ty=np.around(0, decimals=3), tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=3, ty=np.around(-Rva, decimals=3), tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=4, ty=np.around(-Rva, decimals=3), tz=np.around(0, decimals=3))
                    #     msaFEModel.Point.Add(tID=5, ty=np.around(-Rva, decimals=3), tz=np.around(0, decimals=3))
                    #     msaFEModel.Point.Add(tID=6, ty=np.around(-Rva, decimals=3), tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=7, ty=np.around(-tf, decimals=3), tz=np.around(B1, decimals=3))
                    #     msaFEModel.Point.Add(tID=8, ty=np.around(-tf, decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=9, ty=np.around(-2*Rva, decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=10, ty=np.around(-2*Rva, decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=11, ty=np.around(-tf, decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=12, ty=np.around(-tf, decimals=3), tz=np.around(0, decimals=3))
                    #     for ii in range(StripNum - 4):
                    #         msaFEModel.Point.Add(tID=13 + ii * 4, ty=np.around(-Rva * (ii + 2), decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=14 + ii * 4, ty=np.around(-Rva * (ii + 2), decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=15 + ii * 4, ty=np.around(-Rva * (ii + 3), decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #         msaFEModel.Point.Add(tID=16 + ii * 4, ty=np.around(-Rva * (ii + 3), decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum - 3, ty=np.around(-(StripNum - 2) * Rva, decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum - 2, ty=np.around(-(StripNum - 2) * Rva, decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum - 1, ty=np.around(-D + tf, decimals=3),tz=np.around(0.5 * B1 + 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum , ty=np.around(-D + tf, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 1, ty=np.around(-D +Rva, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 2, ty=np.around(-D +Rva, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 3, ty=np.around(-D + tf, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 4, ty=np.around(-D + tf, decimals=3),tz=np.around(0.5 * B1 - 0.5 * tw, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 5, ty=np.around(-D +Rva, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 6, ty=np.around(-D +Rva, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 7, ty=np.around(-D, decimals=3),tz=np.around(0.5 * B1 + 0.5 * B2, decimals=3))
                    #     msaFEModel.Point.Add(tID=4 * StripNum + 8, ty=np.around(-D, decimals=3),tz=np.around(0.5 * B1 - 0.5 * B2, decimals=3))
                    #     for i in range(3):
                    #         msaFEModel.Outline.Add(tID=1 + i, tGID=1 , tType="S", tLID=1 ,tPSID=i + 1 , tPEID=i + 2 )
                    #     msaFEModel.Outline.Add(tID=4, tGID=1 , tType="S", tLID=1 ,tPSID=4, tPEID=1 )
                    #     for i in range(7):
                    #         msaFEModel.Outline.Add(tID=5 + i, tGID=2 , tType="S", tLID=2 ,tPSID=i + 5 , tPEID=i + 6 )
                    #     msaFEModel.Outline.Add(tID=12, tGID=2 , tType="S", tLID=2 ,tPSID=12, tPEID=5 )
                    #     for ii in range(StripNum-4):
                    #         for i in range(3):
                    #             msaFEModel.Outline.Add(tID=13 +i+ ii*4, tGID=3+ii, tType="S", tLID=3+ii, tPSID=i+13+ii*4, tPEID=i+14+ii*4)
                    #         msaFEModel.Outline.Add(tID=16 + ii * 4, tGID=3 + ii, tType="S", tLID=3 + ii,tPSID=16+ ii * 4, tPEID=13+ii*4)
                    #     for i in range(7):
                    #         msaFEModel.Outline.Add(tID=4*StripNum-3+i, tGID=StripNum-1 , tType="S", tLID=StripNum-1 ,tPSID=i +4*StripNum -3 , tPEID=i - 2+4*StripNum)
                    #     msaFEModel.Outline.Add(tID=4*StripNum+4, tGID=StripNum-1 , tType="S", tLID=StripNum-1 ,tPSID=4+4*StripNum, tPEID=4*StripNum -3 )
                    #     for i in range(3):
                    #         msaFEModel.Outline.Add(tID=i+5+4*StripNum, tGID=StripNum , tType="S", tLID=StripNum ,tPSID=i+5+4*StripNum , tPEID=i+6+4*StripNum )
                    #     msaFEModel.Outline.Add(tID=8+4*StripNum , tGID=StripNum , tType="S", tLID=StripNum ,tPSID=8+4*StripNum, tPEID=5+4*StripNum )
                    #     tOID = []
                    #     tOID.append([i+1 for i in range(4)])
                    #     tOID.append([i+5 for i in range(8)])
                    #     for ii in range(StripNum-4):
                    #         ID = []
                    #         for i in range(4):
                    #             ID.append(int(i + 13 + ii * 4))
                    #         tOID.append(ID)
                    #     tOID.append([i+4*StripNum-3 for i in range(8)])
                    #     tOID.append([i+4*StripNum+5 for i in range(4)])
                    #     for ii in range(len(tOID)):
                    #         msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                    #     for i in range(StripNum):
                    #         msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[i + 1])
                    self.mw.ResetTable()
                    self.mw.View.autoRange()
                    self.mw.setWindowTitle(
                        'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections'
                    )
                    msaModel.FileInfo.FileName = ""
                    self.mw.SectIDInput_lineEdit.setText('SolidCircle01')
                    self.accept()
                    SectProperty.Reset()
                    SectionProperties.Reset()
                    CMYieldSAnalResults.ResetAllResults()
                    FEYieldSAnalResults.ResetAllResults()
                    GlobalBuckling.Reset()
                    Status.Reset()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # if msaFEModel.Loop!=0:
        #     radioButton = 1
        #     self.Methodsignal.emit(radioButton)
        #     self.Outline_radioButton.setChecked(True)
        # elif msaModel.Segment.Count!=0:
        #     radioButton = 0
        #     self.Methodsignal.emit(radioButton)
        #     self.Centerline_radioButton.setChecked(True)
        QDialog.close(self)

    @Slot()
    def closeEvent(self, event):
        if msaFEModel.Loop.Count != 0 or msaFEModel.Point.Count != 0 or msaFEModel.Mat.Count != 0:
            radioButton = 1
            self.Methodsignal.emit(radioButton)
            # self.Outline_radioButton.setChecked(True)
        elif msaModel.Segment.Count != 0 or msaModel.Point.Count != 0 or msaModel.Mat.Count != 0:
            radioButton = 0
            self.Methodsignal.emit(radioButton)
            # self.Centerline_radioButton.setChecked(True)
        self.close()


    # def ShowColorDialog(self):
    #     # try:
    #
    #         col = QColorDialog.getColor()
    #         # print(QColor.isValid(col))
    #         if QColor.isValid(col) == False:
    #             pass
    #         else:
    #             colname = col.name()
    #             #print("Color name = ", colname)
    #             senderButton = self.sender()
    #             senderButtonName = senderButton.objectName()
    #             senderButton.setText('')
    #             self.color = colname
    #             senderButton.setStyleSheet(f"QPushButton#{senderButtonName}{{background:{colname}}}")
                # self.SoilNailColor[senderButtonName] =colname
        # except Exception as ex:
        #     traceback.print_exc()


    # def showImage(self):
    #
    #     self.graphicsView.scene_img = QGraphicsScene()
    #     self.imgShow = QPixmap()
    #     self.imgShow.load("ui\Template\ElliShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(440,  370))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)