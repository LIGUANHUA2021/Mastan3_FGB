# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_HollowRec import Ui_HollowRec_Dialog
from gui.msasect.ui.HollowRecDb import HollowRecDb_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class HollowRec_Dialog(QDialog, Ui_HollowRec_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Hollow Rec.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method=0
        # self.showImage()
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked() == True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Rec_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked() == True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Rec_Cl.jpg"))
            self.method = 0
        if self.Centerline_radioButton.isChecked()==True:
            self.k_inputlineEdit.hide()
            self.label_2.hide()
        else:
            self.k_inputlineEdit.show()
            self.label_2.show()


    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        MatIdDict = msaModel.Mat.ID
        if not MatIdDict:
            AddId = 1
        else:
            maxId = max(MatIdDict.keys(), key=(lambda x:x))
            AddId = maxId + 1
        self.ID_inputlineEdit.setText(str(int(AddId)))
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

        self.B_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.tf_inputlineEdit.setValidator(doubleValidator)
        self.tw_inputlineEdit.setValidator(doubleValidator)
        self.k_inputlineEdit.setValidator(doubleValidator)

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Rec_Cl.jpg"))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tf_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()
        self.k_inputlineEdit.clear()
        self.k_inputlineEdit.hide()
        self.label_2.hide()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Rec_Ol.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tf_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()
        self.k_inputlineEdit.clear()
        self.k_inputlineEdit.show()
        self.label_2.show()

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowRecDb_Dialog(self)
        # print(Model.msaModel.Mat.ID)
        Ui.OKsignal.connect(self.get_dialog_signal)
        Ui.exec()

    @Slot()
    def on_OK_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        Stress_input = 0
        try:
            if len(self.E_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0 or len(
                    self.fy_inputlineEdit.text()) == 0 or len(self.B_inputlineEdit.text()) == 0  or len(self.D_inputlineEdit.text()) == 0 or len(
                    self.tf_inputlineEdit.text()) == 0 or len(self.tw_inputlineEdit.text()) == 0 :
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
                B = float(self.B_inputlineEdit.text())
                D = float(self.D_inputlineEdit.text())
                tf = float(self.tf_inputlineEdit.text())
                tw = float(self.tw_inputlineEdit.text())
                k=max(tf,tw)
                if len(self.k_inputlineEdit.text())==0 and self.Outline_radioButton.isChecked()==True:
                    showMesbox(self, 'Please input correct data!')
                elif len(self.k_inputlineEdit.text())!=0:
                    k = float(self.k_inputlineEdit.text())
                MatIdDict = msaModel.Mat.ID
                if tf>=0.5*D or tw>0.5*B or k>=0.5*D or k>=0.5*B or k<0 or B<0 or D<0 or tf<0 or tw<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method == 0:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy,  tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            msaModel.Point.Add(tID=1, ty=np.around(D/2-tf/2, decimals=3), tz=np.around(B / 2-tw/2, decimals=3), tstress=Stress_input)
                            msaModel.Point.Add(tID=2, ty=np.around(D/2-tf/2, decimals=3), tz=np.around(-B/2+tw/2, decimals=3), tstress=Stress_input)
                            msaModel.Point.Add(tID=3, ty=np.around(-D/2+tf/2, decimals=3), tz=np.around(B / 2-tw/2, decimals=3), tstress=Stress_input)
                            msaModel.Point.Add(tID=4, ty=np.around(-D/2+tf/2, decimals=3), tz=np.around(-B / 2+tw/2, decimals=3), tstress=Stress_input)
                            msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=tf)
                            msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=2, tPEID=4, tSegThick=tw)
                            msaModel.Segment.Add(tID=3, tMaterialID=id, tPSID=3, tPEID=4, tSegThick=tf)
                            msaModel.Segment.Add(tID=4, tMaterialID=id, tPSID=1, tPEID=3, tSegThick=tw)
                        else:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            r=k
                            r2=k-tw
                            oy1=-r
                            oz1=r
                            oy2=-r
                            oz2=B-r
                            oy3=-D+r
                            oz3=B-r
                            oy4=-D+r
                            oz4=r
                            if k>max(tw,tf):
                                msaFEModel.Point.Add(tID=1, ty=0, tz=np.around(r, decimals=3))
                                msaFEModel.Point.Add(tID=2, ty=0, tz=np.around(B-r, decimals=3))
                                msaFEModel.Point.Add(tID=3, ty=np.around(r * np.cos(1/8*np.pi)+oy2, decimals=3), tz=np.around(r * np.sin(1/8*np.pi)+oz2, decimals=3))
                                msaFEModel.Point.Add(tID=4, ty=np.around(r * np.cos(2/8*np.pi)+oy2, decimals=3), tz=np.around(r * np.sin(2/8*np.pi)+oz2, decimals=3))
                                msaFEModel.Point.Add(tID=5, ty=np.around(r * np.cos(3/8*np.pi)+oy2, decimals=3), tz=np.around(r * np.sin(3/8*np.pi)+oz2, decimals=3))
                                msaFEModel.Point.Add(tID=6, ty=np.around(-r, decimals=3), tz=B)
                                msaFEModel.Point.Add(tID=7, ty=np.around(-D+r, decimals=3), tz=B)
                                msaFEModel.Point.Add(tID=8, ty=np.around(r * np.cos(5/8*np.pi)+oy3, decimals=3), tz=np.around(r * np.sin(5/8*np.pi)+oz3, decimals=3))
                                msaFEModel.Point.Add(tID=9, ty=np.around(r * np.cos(6 / 8 * np.pi) + oy3, decimals=3),tz=np.around(r * np.sin(6 / 8 * np.pi) + oz3, decimals=3))
                                msaFEModel.Point.Add(tID=10, ty=np.around(r * np.cos(7 / 8 * np.pi) + oy3, decimals=3),tz=np.around(r * np.sin(7 / 8 * np.pi) + oz3, decimals=3))
                                msaFEModel.Point.Add(tID=11, ty=-D , tz=np.around(B-r, decimals=3))
                                msaFEModel.Point.Add(tID=12, ty=-D, tz=np.around(r, decimals=3))
                                msaFEModel.Point.Add(tID=13, ty=np.around(r * np.cos(9 / 8 * np.pi) + oy4, decimals=3),tz=np.around(r * np.sin(9 / 8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=14, ty=np.around(r * np.cos(10 / 8 * np.pi) + oy4, decimals=3),tz=np.around(r * np.sin(10 / 8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=15, ty=np.around(r * np.cos(11 / 8 * np.pi) + oy4, decimals=3),tz=np.around(r * np.sin(11 / 8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=16, ty=np.around(-D+r, decimals=3), tz=0)
                                msaFEModel.Point.Add(tID=17, ty=np.around(-r, decimals=3), tz=0)
                                msaFEModel.Point.Add(tID=18, ty=np.around(r * np.cos(13 / 8 * np.pi) + oy1, decimals=3),tz=np.around(r * np.sin(13 / 8 * np.pi) + oz1, decimals=3))
                                msaFEModel.Point.Add(tID=19, ty=np.around(r * np.cos(14 / 8 * np.pi) + oy1, decimals=3),tz=np.around(r * np.sin(14 / 8 * np.pi) + oz1, decimals=3))
                                msaFEModel.Point.Add(tID=20, ty=np.around(r * np.cos(15 / 8 * np.pi) + oy1, decimals=3),tz=np.around(r * np.sin(15 / 8 * np.pi) + oz1, decimals=3))
                                msaFEModel.Point.Add(tID=21, ty=-tw, tz=np.around(r, decimals=3))
                                msaFEModel.Point.Add(tID=22, ty=-tw, tz=np.around(B - r, decimals=3))
                                msaFEModel.Point.Add(tID=23, ty=np.around(r2 * np.cos(1 / 8 * np.pi) + oy2, decimals=3),tz=np.around(r2 * np.sin(1 / 8 * np.pi) + oz2, decimals=3))
                                msaFEModel.Point.Add(tID=24, ty=np.around(r2 * np.cos(2 / 8 * np.pi) + oy2, decimals=3),tz=np.around(r2 * np.sin(2 / 8 * np.pi) + oz2, decimals=3))
                                msaFEModel.Point.Add(tID=25, ty=np.around(r2 * np.cos(3 / 8 * np.pi) + oy2, decimals=3),tz=np.around(r2 * np.sin(3 / 8 * np.pi) + oz2, decimals=3))
                                msaFEModel.Point.Add(tID=26, ty=np.around(-r, decimals=3), tz=B-tw)
                                msaFEModel.Point.Add(tID=27, ty=np.around(-D + r, decimals=3), tz=B-tw)
                                msaFEModel.Point.Add(tID=28, ty=np.around(r2 * np.cos(5 / 8 * np.pi) + oy3, decimals=3),tz=np.around(r2 * np.sin(5 / 8 * np.pi) + oz3, decimals=3))
                                msaFEModel.Point.Add(tID=29, ty=np.around(r2 * np.cos(6 / 8 * np.pi) + oy3, decimals=3),tz=np.around(r2 * np.sin(6 / 8 * np.pi) + oz3, decimals=3))
                                msaFEModel.Point.Add(tID=30, ty=np.around(r2 * np.cos(7 / 8 * np.pi) + oy3, decimals=3),tz=np.around(r2 * np.sin(7 / 8 * np.pi) + oz3, decimals=3))
                                msaFEModel.Point.Add(tID=31, ty=-D+tw, tz=np.around(B - r, decimals=3))
                                msaFEModel.Point.Add(tID=32, ty=-D+tw, tz=np.around(r, decimals=3))
                                msaFEModel.Point.Add(tID=33, ty=np.around(r2 * np.cos(9 / 8 * np.pi) + oy4, decimals=3),tz=np.around(r2 * np.sin(9 / 8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=34, ty=np.around(r2 * np.cos(10 / 8 * np.pi) + oy4, decimals=3),tz=np.around(r2 * np.sin(10 / 8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=35, ty=np.around(r2 * np.cos(11 / 8 * np.pi) + oy4, decimals=3),tz=np.around(r2 * np.sin(11 / 8 * np.pi) + oz4, decimals=3))
                                msaFEModel.Point.Add(tID=36, ty=np.around(-D + r, decimals=3), tz=tw)
                                msaFEModel.Point.Add(tID=37, ty=np.around(-r, decimals=3), tz=tw)
                                msaFEModel.Point.Add(tID=38, ty=np.around(r2 * np.cos(13 / 8 * np.pi) + oy1, decimals=3),tz=np.around(r2 * np.sin(13 / 8 * np.pi) + oz1, decimals=3))
                                msaFEModel.Point.Add(tID=39, ty=np.around(r2 * np.cos(14 / 8 * np.pi) + oy1, decimals=3),tz=np.around(r2 * np.sin(14 / 8 * np.pi) + oz1, decimals=3))
                                msaFEModel.Point.Add(tID=40, ty=np.around(r2 * np.cos(15 / 8 * np.pi) + oy1, decimals=3),tz=np.around(r2 * np.sin(15 / 8 * np.pi) + oz1, decimals=3))
                                for i in range(19):
                                    msaFEModel.Outline.Add(tID=i + 1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                                msaFEModel.Outline.Add(tID=20, tGID=1, tType="S", tLID=1, tPSID=20, tPEID=1)
                                for i in range(19):
                                        msaFEModel.Outline.Add(tID=i + 21, tGID=1, tType="O", tLID=2, tPSID=i + 21, tPEID=i + 22)
                                msaFEModel.Outline.Add(tID=40, tGID=1, tType="O", tLID=2, tPSID=40, tPEID=21)
                                tOID1 = []
                                tOID2 = []
                                for ii in range(20):
                                    tOID1.append(ii + 1)
                                    tOID2.append(ii + 21)
                                msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                                msaFEModel.Loop.Add(tID=2, tOID=tOID2)
                                msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1,2])
                            elif k<=tw or k<=tf:
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=0, tz=B)
                                msaFEModel.Point.Add(tID=3, ty=-D, tz=B)
                                msaFEModel.Point.Add(tID=4, ty=-D, tz=0)
                                msaFEModel.Point.Add(tID=5, ty=-tf, tz=tw)
                                msaFEModel.Point.Add(tID=6, ty=-tf, tz=B-tw)
                                msaFEModel.Point.Add(tID=7, ty=-D+tf, tz=B-tw)
                                msaFEModel.Point.Add(tID=8, ty=-D+tf, tz=tw)
                                msaFEModel.Outline.Add(tID=1, tGID=1, tType="S", tLID=1, tPSID=1, tPEID=2)
                                msaFEModel.Outline.Add(tID=2, tGID=1, tType="S", tLID=1, tPSID=2, tPEID=3)
                                msaFEModel.Outline.Add(tID=3, tGID=1, tType="S", tLID=1, tPSID=3, tPEID=4)
                                msaFEModel.Outline.Add(tID=4, tGID=1, tType="S", tLID=1, tPSID=4, tPEID=1)
                                msaFEModel.Outline.Add(tID=5, tGID=1, tType="O", tLID=2, tPSID=5, tPEID=6)
                                msaFEModel.Outline.Add(tID=6, tGID=1, tType="O", tLID=2, tPSID=6, tPEID=7)
                                msaFEModel.Outline.Add(tID=7, tGID=1, tType="O", tLID=2, tPSID=7, tPEID=8)
                                msaFEModel.Outline.Add(tID=8, tGID=1, tType="O", tLID=2, tPSID=8, tPEID=5)
                                msaFEModel.Loop.Add(tID=1, tOID=[1, 2, 3, 4])
                                msaFEModel.Loop.Add(tID=2, tOID=[5, 6, 7, 8])
                                msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1, 2])
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
                        CMYieldSAnalResults.ResetAllResults()
                        FEYieldSAnalResults.ResetAllResults()
                        GlobalBuckling.Reset()
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
    #     self.imgShow.load("ui\Template\RecShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(435, 350))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     # self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)
    def get_dialog_signal(self, connect):
        if connect!= {}:
            if self.method == 0:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tf_inputlineEdit.setText(str(connect['tf(tw)']))
                self.tw_inputlineEdit.setText(str(connect['tf(tw)']))
                self.k_inputlineEdit.setText(str(connect['k']))
            else:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tf_inputlineEdit.setText(str(connect['tf(tw)']))
                self.tw_inputlineEdit.setText(str(connect['tf(tw)']))
                self.k_inputlineEdit.setText(str(connect['k']))
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

