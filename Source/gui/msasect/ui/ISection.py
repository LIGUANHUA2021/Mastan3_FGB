# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import os
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_ISection import Ui_ISection_Dialog
from gui.msasect.ui.ISectionDb import ISectionDb_Dialog
from PySide6.QtWidgets import QColorDialog
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults

from PySide6.QtGui import QColor,  QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel, msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox

from gui.msasect.Configuration import basedir

class ISection_Dialog(QDialog, Ui_ISection_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/I-Section.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method=0
        # self.showImage()
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked() == True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap(os.path.join(basedir,"ui","Template","I-Section_Ol.jpg")))
            print(os.path.join(basedir,"ui","Template","I-Section_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked() == True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/I-Section_Cl.jpg"))
            self.method = 0
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        # if self.method == 0:
        #     self.k_inputlineEdit.setEnabled(False)
        #     self.k1_inputlineEdit.setEnabled(False)
        # else:
        #     self.k_inputlineEdit.setEnabled(True)
        #     self.k1_inputlineEdit.setEnabled(True)
        #     self.k_inputlineEdit.setValidator(doubleValidator)
        #     self.k1_inputlineEdit.setValidator(doubleValidator)

        if self.Centerline_radioButton.isChecked()==True:
            self.k_inputlineEdit.hide()
            self.k1_inputlineEdit.hide()
            self.label_3.hide()
            self.label_4.hide()
        else:
            self.k_inputlineEdit.show()
            self.k1_inputlineEdit.show()
            self.label_3.show()
            self.label_4.show()

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x:x))
        #     AddId = maxId + 1
        AddId = 1
        self.ID_inputlineEdit.setText(str(int(AddId)))
        self.E_inputlineEdit.setText(str(205000))
        self.fy_inputlineEdit.setText(str(345))
        self.eu_inputlineEdit.setText(str(0.15))
        self.G_inputlineEdit.setText(str(0.3))
        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999,top=999)
        intValidator = QIntValidator()
        self.ID_inputlineEdit.setValidator(intValidator)
        self.E_inputlineEdit.setValidator(doubleValidator)
        self.G_inputlineEdit.setValidator(doubleValidator)
        self.fy_inputlineEdit.setValidator(doubleValidator)
        self.eu_inputlineEdit.setValidator(doubleValidator)
        self.B1_inputlineEdit.setValidator(doubleValidator)
        self.B2_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.t1_inputlineEdit.setValidator(doubleValidator)
        self.t2_inputlineEdit.setValidator(doubleValidator)
        self.t3_inputlineEdit.setValidator(doubleValidator)
        self.k_inputlineEdit.setValidator(doubleValidator)
        self.k1_inputlineEdit.setValidator(doubleValidator)

    @Slot()
    def on_OK_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Stress_input = 0
        theta = 0
        try:
            if len(self.E_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0 or len(
                    self.fy_inputlineEdit.text()) == 0 or len(self.B1_inputlineEdit.text()) == 0 or len(self.B2_inputlineEdit.text()) == 0 or len(
                self.D_inputlineEdit.text()) == 0 or len(
                self.t1_inputlineEdit.text()) == 0 or  len(self.t2_inputlineEdit.text()) == 0 or  len(self.t3_inputlineEdit.text()) == 0 :
                showMesbox(self, 'Please input correct data!')
            else:
                msaModel.ResetAll()
                msaFEModel.ResetAll()
                msaModel.Mat.Reset()
                msaModel.Point.Reset()
                msaModel.Segment.Reset()
                msaFEModel.Point.Reset()
                msaFEModel.Outline.Reset()
                msaFEModel.Loop.Reset()
                msaFEModel.Group.Reset()
                tE = float(self.E_inputlineEdit.text())
                tμ = float(self.G_inputlineEdit.text())
                tfy = float(self.fy_inputlineEdit.text())
                id = int(self.ID_inputlineEdit.text())
                teu = float(self.eu_inputlineEdit.text())
                B1 = float(self.B1_inputlineEdit.text())
                B2 = float(self.B2_inputlineEdit.text())
                D = float(self.D_inputlineEdit.text())
                t1 = float(self.t1_inputlineEdit.text())
                t2 = float(self.t2_inputlineEdit.text())
                t3 = float(self.t3_inputlineEdit.text())
                k=max(t1,t2)
                k1=0.5*t3
                if len(self.k_inputlineEdit.text()) != 0 and  len(self.k1_inputlineEdit.text()) != 0 :
                    k = float(self.k_inputlineEdit.text())
                    k1 = float(self.k1_inputlineEdit.text())
                if D<=(t1+t2) or B1<=t3 or B2<=t3 or k>=0.5*D or k1>=0.5*B1 or k1>=0.5*B2 or B1<0 or B2<0 or t1<0 or t2<0 or t3<0 or D<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    MatIdDict = msaModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method == 0:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy,  tDensity=999999, teu=teu, tType="S", tColor=self.color)
                            self.accept()
                            msaModel.Point.Add(tID=1, ty=0, tz=-B1/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=2, ty=0, tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=3, ty=0, tz=B1/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=4, ty=-t1/2, tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=5, ty=np.around(-(D-t2-0.5*t1), decimals=5), tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=6, ty=np.around(-(D-0.5*t2-0.5*t1), decimals=5), tz=-B2 / 2, tstress=Stress_input)
                            msaModel.Point.Add(tID=7, ty=np.around(-(D-0.5*t2-0.5*t1), decimals=5), tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=8, ty=np.around(-(D-0.5*t2-0.5*t1), decimals=5), tz=B2 / 2, tstress=Stress_input)
                            msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=t1)
                            msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=2, tPEID=3, tSegThick=t1)
                            msaModel.Segment.Add(tID=3, tMaterialID=id, tPSID=2, tPEID=4, tSegThick=np.around(t3/1000, decimals=5))
                            msaModel.Segment.Add(tID=4, tMaterialID=id, tPSID=4, tPEID=5, tSegThick=t3)
                            msaModel.Segment.Add(tID=5, tMaterialID=id, tPSID=5, tPEID=7, tSegThick=np.around(t3/1000, decimals=5))
                            msaModel.Segment.Add(tID=6, tMaterialID=id, tPSID=6, tPEID=7, tSegThick=t2)
                            msaModel.Segment.Add(tID=7, tMaterialID=id, tPSID=7, tPEID=8, tSegThick=t2)
                        else:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu, tType="S", tColor=self.color)
                            self.accept()
                            if k>t1 and k>t2 and k1>0.5*t3:
                                A=k1-0.5*t3
                                B=k-t2
                                oy1=-k
                                oz1=0.5*B1+k1
                                oy2=-D+k
                                oz2=0.5*(B1+t3)+A
                                oy3 =-D+k
                                oz3 =0.5*(B1-t3)-A
                                oy4 =-k
                                oz4 =0.5*(B1-t3)-A
                                B1 = float(self.B1_inputlineEdit.text())
                                B2 = float(self.B2_inputlineEdit.text())
                                D = float(self.D_inputlineEdit.text())
                                t1 = float(self.t1_inputlineEdit.text())
                                t2 = float(self.t2_inputlineEdit.text())
                                t3 = float(self.t3_inputlineEdit.text())
                                msaFEModel.Point.Add(tID=1, ty=0,tz=0)
                                msaFEModel.Point.Add(tID=2, ty=0, tz=B1 )
                                msaFEModel.Point.Add(tID=3, ty=-t1, tz=B1 )
                                msaFEModel.Point.Add(tID=4, ty=-t1, tz=np.around((0.5*B1+0.5*t3+A), decimals=3))
                                msaFEModel.Point.Add(tID=5, ty=np.around(B * np.cos(15/8*np.pi)+oy1, decimals=3), tz=np.around(A * np.sin(15/8*np.pi)+oz1, decimals=3))
                                msaFEModel.Point.Add(tID=6, ty=np.around(B * np.cos(14/8*np.pi)+oy1, decimals=3), tz=np.around(A * np.sin(14/8*np.pi)+oz1, decimals=3))
                                msaFEModel.Point.Add(tID=7, ty=np.around(B * np.cos(13/8 * np.pi) + oy1, decimals=3),tz=np.around(A * np.sin(13/8 * np.pi) + oz1, decimals=3))
                                msaFEModel.Point.Add(tID=8, ty=-k, tz=np.around(0.5 * B1 + 0.5 * t3, decimals=3) )
                                msaFEModel.Point.Add(tID=9, ty=-D+k, tz=np.around(0.5 * B1 + 0.5 * t3, decimals=3) )
                                msaFEModel.Point.Add(tID=10, ty=np.around(B * np.cos(11/8*np.pi)+oy2, decimals=3), tz=np.around(A * np.sin(11/8*np.pi)+oz2, decimals=3))
                                msaFEModel.Point.Add(tID=11, ty=np.around(B * np.cos(10/8 * np.pi) + oy2, decimals=3),tz=np.around(A * np.sin(10/8 * np.pi) + oz2, decimals=3))
                                msaFEModel.Point.Add(tID=12, ty=np.around(B * np.cos(9/8 * np.pi) + oy2, decimals=3),tz=np.around(A * np.sin(9/8 * np.pi) + oz2, decimals=3))
                                msaFEModel.Point.Add(tID=13, ty=-D+t2, tz=np.around((0.5*B1+0.5*t3+A), decimals=3))
                                msaFEModel.Point.Add(tID=14, ty=-D+t2, tz=np.around(0.5*(B1+B2), decimals=3))
                                msaFEModel.Point.Add(tID=15, ty=-D, tz=np.around(.5*(B1+B2), decimals=3))
                                msaFEModel.Point.Add(tID=16, ty=-D, tz=np.around((0.5*(B1-B2)), decimals=3))
                                msaFEModel.Point.Add(tID=17, ty=-D+t2, tz=np.around((0.5*(B1-B2)), decimals=3))
                                msaFEModel.Point.Add(tID=18, ty=-D+t2, tz=np.around((0.5*B1-k1), decimals=3))
                                msaFEModel.Point.Add(tID=19, ty=np.around(B * np.cos(7/8*np.pi)+oy3, decimals=3), tz=np.around(A * np.sin(7/8*np.pi)+oz3, decimals=3))
                                msaFEModel.Point.Add(tID=20, ty=np.around(B * np.cos(6/8*np.pi)+oy3, decimals=3), tz=np.around(A * np.sin(6/8*np.pi)+oz3, decimals=3))
                                msaFEModel.Point.Add(tID=21, ty=np.around(B * np.cos(5/8*np.pi)+oy3, decimals=3), tz=np.around(A * np.sin(5/8*np.pi)+oz3, decimals=3))
                                msaFEModel.Point.Add(tID=22, ty=-D + k, tz=np.around(0.5 * (B1 - t3), decimals=3))
                                msaFEModel.Point.Add(tID=23, ty=-k, tz=np.around(0.5 * (B1 - t3), decimals=3))
                                msaFEModel.Point.Add(tID=24, ty=np.around(B * np.cos(3/8 * np.pi) + oy4, decimals=3),tz=np.around(A * np.sin(3/8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=25, ty=np.around(B * np.cos(2/8 * np.pi) + oy4, decimals=3),tz=np.around(A * np.sin(2/8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=26, ty=np.around(B * np.cos(1/8 * np.pi) + oy4, decimals=3),tz=np.around(A * np.sin(1/8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=27, ty=-t1, tz=np.around((0.5 * B1 - k1),decimals=3))
                                msaFEModel.Point.Add(tID=28, ty=-t1, tz=0)
                                for i in range(27):
                                    msaFEModel.Outline.Add(tID=i + 1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                                msaFEModel.Outline.Add(tID=28, tGID=1, tType="S", tLID=1, tPSID=28, tPEID=1)
                                tOID1 = []
                                for ii in range(28):
                                    tOID1.append(ii + 1)
                                msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                                msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1])
                            else:
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=0, tz=B1)
                                msaFEModel.Point.Add(tID=3, ty=-t1, tz=B1)
                                msaFEModel.Point.Add(tID=4, ty=-t1, tz=0.5*B1+0.5*t3)
                                msaFEModel.Point.Add(tID=5, ty=-D+t2, tz=0.5 * B1 + 0.5 * t3)
                                msaFEModel.Point.Add(tID=6, ty=-D+t2, tz=0.5 * B1 + 0.5 * B2)
                                msaFEModel.Point.Add(tID=7, ty=-D, tz=0.5 * B1 + 0.5 * B2)
                                msaFEModel.Point.Add(tID=8, ty=-D, tz=0.5 * B1 - 0.5 * B2)
                                msaFEModel.Point.Add(tID=9, ty=-D+t2, tz=0.5 * B1 - 0.5 * B2)
                                msaFEModel.Point.Add(tID=10, ty=-D+t2, tz=0.5 * B1 - 0.5 * t3)
                                msaFEModel.Point.Add(tID=11, ty=-t1, tz=0.5 * B1 - 0.5 * t3)
                                msaFEModel.Point.Add(tID=12, ty=-t1, tz=0)
                                for i in range(11):
                                    msaFEModel.Outline.Add(tID=i + 1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                                msaFEModel.Outline.Add(tID=12, tGID=1, tType="S", tLID=1, tPSID=12, tPEID=1)
                                tOID1 = []
                                for ii in range(12):
                                    tOID1.append(ii + 1)
                                msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                                msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1])
                        self.mw.ResetTable()
                        self.mw.View.autoRange()
                        self.mw.setWindowTitle(
                            'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections'
                        )
                        msaModel.FileInfo.FileName = ""
                        Status.Reset()
                        self.accept()
                        SectProperty.Reset()
                        SectionProperties.Reset()
                        ##
                        CMYieldSAnalResults.ResetAllResults()
                        FEYieldSAnalResults.ResetAllResults()
                        GlobalBuckling.Reset()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()


    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap(os.path.join(basedir,"ui","Template","I-Section_Cl.jpg")))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.k_inputlineEdit.hide()
        self.k1_inputlineEdit.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.B1_inputlineEdit.clear()
        self.B2_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.t1_inputlineEdit.clear()
        self.t2_inputlineEdit.clear()
        self.t3_inputlineEdit.clear()
        self.k_inputlineEdit.clear()
        self.k1_inputlineEdit.clear()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/I-Section_Ol.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.k_inputlineEdit.show()
        self.k1_inputlineEdit.show()
        self.label_3.show()
        self.label_4.show()
        self.B1_inputlineEdit.clear()
        self.B2_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.t1_inputlineEdit.clear()
        self.t2_inputlineEdit.clear()
        self.t3_inputlineEdit.clear()
        self.k_inputlineEdit.clear()
        self.k1_inputlineEdit.clear()

    # @Slot()
    # def on_Import_pushButton_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     # raise NotImplementedError

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = ISectionDb_Dialog(self)
        Ui.OKsignal.connect(self.get_dialog_signal)
        # print(Model.msaModel.Mat.ID)
        Ui.exec()

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
        self.mw.SectIDInput_lineEdit.setText(str('Section01'))
        self.close()

    def ShowColorDialog(self):
        # try:

            col = QColorDialog.getColor()
            # print(QColor.isValid(col))
            if QColor.isValid(col) == False:
                pass
            else:
                colname = col.name()
                #print("Color name = ", colname)
                senderButton = self.sender()
                senderButtonName = senderButton.objectName()
                senderButton.setText('')
                self.color = colname
                senderButton.setStyleSheet(f"QPushButton#{senderButtonName}{{background:{colname}}}")
                # self.SoilNailColor[senderButtonName] =colname
        # except Exception as ex:
        #     traceback.print_exc()

    # def showImage(self):
    #
    #     self.graphicsView.scene_img = QGraphicsScene()
    #     self.imgShow = QPixmap()
    #     self.imgShow.load("ui\Template\IShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(435,  545))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)
    def get_dialog_signal(self, connect):
        if connect != {}:
            if self.method == 0:
                self.B1_inputlineEdit.setText(str(connect['B1(2)']))
                self.B2_inputlineEdit.setText(str(connect['B1(2)']))
                self.D_inputlineEdit.setText(str(float(np.around(float(connect['D']), decimals=3))))
                self.t1_inputlineEdit.setText(str(connect['t1(2)']))
                self.t2_inputlineEdit.setText(str(connect['t1(2)']))
                self.t3_inputlineEdit.setText(str(connect['t3']))
                self.k_inputlineEdit.setText(str(connect['k']))
                self.k1_inputlineEdit.setText(str(connect['k1']))
            else:
                self.B1_inputlineEdit.setText(str(connect['B1(2)']))
                self.B2_inputlineEdit.setText(str(connect['B1(2)']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.t1_inputlineEdit.setText(str(connect['t1(2)']))
                self.t2_inputlineEdit.setText(str(connect['t1(2)']))
                self.t3_inputlineEdit.setText(str(connect['t3']))
                self.k_inputlineEdit.setText(str(connect['k']))
                self.k1_inputlineEdit.setText(str(connect['k1']))
            self.mw.SectIDInput_lineEdit.setText(str(connect['Type']))
            if connect["unit"]==0:
                self.E_inputlineEdit.setText(str(29733))
                self.fy_inputlineEdit.setText(str(50))
                self.eu_inputlineEdit.setText(str(0.15))
                self.G_inputlineEdit.setText(str(0.3))
            else:
                self.E_inputlineEdit.setText(str(205000))
                self.fy_inputlineEdit.setText(str(345))
                self.eu_inputlineEdit.setText(str(0.15))
                self.G_inputlineEdit.setText(str(0.3))



