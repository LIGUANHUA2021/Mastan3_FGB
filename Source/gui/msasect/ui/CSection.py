# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback
from gui.msasect.base.Model import msaModel, msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
from gui.msasect.ui.Ui_CSection import Ui_CSection_Dialog
from gui.msasect.ui.CSectionDb import CSectionDb_Dialog
import numpy as np
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class CSection_Dialog(QDialog, Ui_CSection_Dialog):
    """
    Class documentation goes here.
    """
    Methodsignal = Signal(int)
    def __init__(self,mw, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/C-Section.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method=0
        # self.showImage()
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked()==True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/C-Section_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked()==True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/C-Section_Cl.jpg"))
            self.method = 0

        if self.Centerline_radioButton.isChecked()==True:
            self.k_inputlineEdit.hide()
            self.theta_inputlineEdit.hide()
            self.k1_lineEdit.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.k1_label.hide()
        else:
            self.k_inputlineEdit.show()
            self.theta_inputlineEdit.show()
            self.k1_lineEdit.show()
            self.label_2.show()
            self.label_3.show()
            self.k1_label.show()

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
        self.fy_inputlineEdit.setValidator(doubleValidator)
        self.eu_inputlineEdit.setValidator(doubleValidator)
        self.G_inputlineEdit.setValidator(doubleValidator)
        self.B_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.tf_inputlineEdit.setValidator(doubleValidator)
        self.tw_inputlineEdit.setValidator(doubleValidator)
        self.k_inputlineEdit.setValidator(doubleValidator)
        self.theta_inputlineEdit.setValidator(doubleValidator)

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/C-Section_Cl.jpg"))
        self.method=0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.k_inputlineEdit.hide()
        self.k1_lineEdit.hide()
        self.theta_inputlineEdit.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.k1_label.hide()
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tf_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()
        self.k_inputlineEdit.clear()
        self.k1_lineEdit.clear()
        self.theta_inputlineEdit.clear()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/C-Section_Ol.jpg"))
        self.method=1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.k_inputlineEdit.show()
        self.k1_lineEdit.show()
        self.theta_inputlineEdit.show()
        self.label_2.show()
        self.label_3.show()
        self.k1_label.show()
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tf_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()
        self.k_inputlineEdit.clear()
        self.k1_lineEdit.clear()
        self.theta_inputlineEdit.clear()

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = CSectionDb_Dialog(self)
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
            if len(self.E_inputlineEdit.text()) == 0 or len(
                        self.fy_inputlineEdit.text()) == 0 or len(self.eu_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0  or len(self.D_inputlineEdit.text()) == 0 or len(
                        self.tf_inputlineEdit.text()) == 0 or len(self.tw_inputlineEdit.text()) == 0 :
                    showMesbox(self, 'Please input correct data0!')
            else:
                msaModel.ResetAll()
                msaFEModel.ResetAll()
                msaModel.Mat.Reset()
                msaModel.Point.Reset()
                msaModel.Segment.Reset()
                msaFEModel.Mat.Reset()
                msaFEModel.Point.Reset()
                msaFEModel.Outline.Reset()
                msaFEModel.Loop.Reset()
                msaFEModel.Group.Reset()
                tE = float(self.E_inputlineEdit.text())
                tfy = float(self.fy_inputlineEdit.text())
                id = int(self.ID_inputlineEdit.text())
                teu = float(self.eu_inputlineEdit.text())
                tμ = float(self.G_inputlineEdit.text())
                B = float(self.B_inputlineEdit.text())
                D = float(self.D_inputlineEdit.text())
                tf = float(self.tf_inputlineEdit.text())
                tw = float(self.tw_inputlineEdit.text())
                k = tf
                theta = 0
                k1 = 0
                if len(self.k_inputlineEdit.text())==0 and self.Outline_radioButton.isChecked():
                    showMesbox(self, 'Please input correct data1!')
                elif len(self.k1_lineEdit.text())==0 and self.Outline_radioButton.isChecked():
                    showMesbox(self, 'Please input correct data2!')
                elif len(self.theta_inputlineEdit.text())==0 and self.Outline_radioButton.isChecked():
                    showMesbox(self, 'Please input correct data3!')
                elif len(self.k_inputlineEdit.text())!=0 and len(self.theta_inputlineEdit.text())!=0 and len(self.k1_lineEdit.text())!=0:
                    k = float(self.k_inputlineEdit.text())
                    theta = float(self.theta_inputlineEdit.text())
                    k1 = float(self.k1_lineEdit.text())
                if tf >= (0.5 * D - theta * (0.5 * B - tw)) or tw >= 0.5 * B \
                        or k < (tf + theta * (0.5 * B - tw)) or theta < 0 or theta >= 1 \
                        or B < 0 or D < 0 or tf < 0 or tw < 0 or tE < 0 or k >= B-k1-tw or k1 >= B/2 or k1 < 0 or tμ < 0 or tfy < 0 or teu < 0:
                    showMesbox(self, 'Please input correct data4!')
                else:
                    MatIdDict = msaModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method == 0:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ,tFy=tfy,  tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            msaModel.Point.Add(tID=1, ty=-tf/2, tz=-B, tstress=Stress_input)
                            msaModel.Point.Add(tID=2, ty=-tf/2, tz=-tw/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=3, ty=-D+tf/2, tz=-tw/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=4, ty=-D+tf/2, tz=-B, tstress=Stress_input)
                            msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=tf)
                            msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=2, tPEID=3, tSegThick=tw)
                            msaModel.Segment.Add(tID=3, tMaterialID=id, tPSID=3, tPEID=4, tSegThick=tf)
                        else:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            r1=tf-(0.5*B-k1)*theta
                            r2=(k-tf-0.5*B*theta+theta*tw)/(1-1.5*theta)
                            r3=k1
                            r4=1.5*r2
                            oy1=0
                            oz1=B-r3
                            oy2=-k
                            oz2=tw+r4
                            oy3=-D+k
                            oz3=tw+r4
                            oy4=-D
                            oz4=B-r3
                            msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                            msaFEModel.Point.Add(tID=2, ty=0, tz=-B)
                            msaFEModel.Point.Add(tID=3, ty=np.around(r1 * np.cos(7 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(r3 * np.sin(7 / 12 * np.pi) + oz1, decimals=3)))
                            msaFEModel.Point.Add(tID=4, ty=np.around(r1 * np.cos(8 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(r3 * np.sin(8 / 12 * np.pi) + oz1, decimals=3)))
                            msaFEModel.Point.Add(tID=5, ty=np.around(r1 * np.cos(9 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(r3 * np.sin(9 / 12 * np.pi) + oz1, decimals=3)))
                            msaFEModel.Point.Add(tID=6, ty=np.around(r1 * np.cos(10 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(r3 * np.sin(10 / 12 * np.pi) + oz1, decimals=3)))
                            msaFEModel.Point.Add(tID=7, ty=np.around(r1 * np.cos(11 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(r3 * np.sin(11 / 12 * np.pi) + oz1, decimals=3)))
                            msaFEModel.Point.Add(tID=8, ty=np.around(-r1, decimals=3), tz=-(np.around(B-r3, decimals=3)))
                            msaFEModel.Point.Add(tID=9, ty=np.around(-k+r2, decimals=3), tz=-(np.around(tw+r4, decimals=3)))
                            msaFEModel.Point.Add(tID=10, ty=np.around(r2 * np.cos(15 / 8 * np.pi) + oy2, decimals=3),tz=-(np.around(r4 * np.sin(15 / 8 * np.pi) + oz2, decimals=3)))
                            msaFEModel.Point.Add(tID=11, ty=np.around(r2 * np.cos(14 / 8 * np.pi) + oy2, decimals=3),tz=-(np.around(r4 * np.sin(14 / 8 * np.pi) + oz2, decimals=3)))
                            msaFEModel.Point.Add(tID=12, ty=np.around(r2 * np.cos(13 / 8 * np.pi) + oy2, decimals=3),tz=-(np.around(r4 * np.sin(13 / 8 * np.pi) + oz2, decimals=3)))
                            msaFEModel.Point.Add(tID=13, ty=np.around(-k, decimals=3), tz=-(np.around(tw, decimals=3)))
                            msaFEModel.Point.Add(tID=14, ty=np.around(-D+k, decimals=3), tz=-(np.around(tw, decimals=3)))
                            msaFEModel.Point.Add(tID=15, ty=np.around(r2 * np.cos(11 / 8 * np.pi) + oy3, decimals=3),tz=-(np.around(r4 * np.sin(11 / 8 * np.pi) + oz3, decimals=3)))
                            msaFEModel.Point.Add(tID=16, ty=np.around(r2 * np.cos(10 / 8 * np.pi) + oy3, decimals=3),tz=-(np.around(r4 * np.sin(10 / 8 * np.pi) + oz3, decimals=3)))
                            msaFEModel.Point.Add(tID=17, ty=np.around(r2 * np.cos(9 / 8 * np.pi) + oy3, decimals=3),tz=-(np.around(r4 * np.sin(9 / 8 * np.pi) + oz3, decimals=3)))
                            msaFEModel.Point.Add(tID=18, ty=np.around(-D+(k-r2), decimals=3), tz=-(np.around(tw+r4, decimals=3)))
                            msaFEModel.Point.Add(tID=19, ty=np.around(-D + r1, decimals=3), tz=-(np.around(B - r3, decimals=3)))
                            msaFEModel.Point.Add(tID=20, ty=np.around(r1 * np.cos(1 / 12 * np.pi) + oy4, decimals=3),tz=-(np.around(r3 * np.sin(1 / 12 * np.pi) + oz4, decimals=3)))
                            msaFEModel.Point.Add(tID=21, ty=np.around(r1 * np.cos(2 / 12 * np.pi) + oy4, decimals=3),tz=-(np.around(r3 * np.sin(2 / 12 * np.pi) + oz4, decimals=3)))
                            msaFEModel.Point.Add(tID=22, ty=np.around(r1 * np.cos(3 / 12 * np.pi) + oy4, decimals=3),tz=-(np.around(r3 * np.sin(3 / 12 * np.pi) + oz4, decimals=3)))
                            msaFEModel.Point.Add(tID=23, ty=np.around(r1 * np.cos(4 / 12 * np.pi) + oy4, decimals=3),tz=-(np.around(r3 * np.sin(4 / 12 * np.pi) + oz4, decimals=3)))
                            msaFEModel.Point.Add(tID=24, ty=np.around(r1 * np.cos(5 / 12 * np.pi) + oy4, decimals=3),tz=-(np.around(r3 * np.sin(5 / 12 * np.pi) + oz4, decimals=3)))
                            msaFEModel.Point.Add(tID=25, ty=np.around(-D, decimals=3), tz=-B)
                            msaFEModel.Point.Add(tID=26, ty=np.around(-D, decimals=3), tz=0)
                            for i in range(25):
                                msaFEModel.Outline.Add(tID=i + 1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                            msaFEModel.Outline.Add(tID=26, tGID=1, tType="S", tLID=1, tPSID=26, tPEID=1)
                            tOID1 = []
                            for ii in range(26):
                                tOID1.append(ii + 1)
                            msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                            msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1])
                        self.mw.ResetTable()
                        self.mw.View.autoRange()
                        self.mw.setWindowTitle(
                        'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections'
                        )
                        msaModel.FileInfo.FileName=""
                        Status.Reset()
                        self.accept()
                        SectProperty.Reset()
                        SectionProperties.Reset()
                        CMYieldSAnalResults.ResetAllResults()
                        FEYieldSAnalResults.ResetAllResults()
                        GlobalBuckling.Reset()
        except:
            showMesbox(self, 'Please enter correct data5!')
            traceback.print_exc()

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QDialog.close(self)

    @Slot()
    def closeEvent(self, event):
        if msaFEModel.Loop.Count != 0 or msaFEModel.Point.Count!=0 or msaFEModel.Mat.Count!=0:
            radioButton = 1
            self.Methodsignal.emit(radioButton)
            #self.Outline_radioButton.setChecked(True)
        elif msaModel.Segment.Count != 0 or msaModel.Point.Count!=0 or msaModel.Mat.Count!=0:
            radioButton = 0
            self.Methodsignal.emit(radioButton)
            #self.Centerline_radioButton.setChecked(True)
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
                self.color=colname
                senderButton.setStyleSheet(f"QPushButton#{senderButtonName}{{background:{colname}}}")
                # self.SoilNailColor[senderButtonName] =colname
        # except Exception as ex:
        #     traceback.print_exc()
    # def showImage(self):
    #
    #     self.graphicsView.scene_img = QGraphicsScene()
    #     self.imgShow = QPixmap()
    #     self.imgShow.load("ui\Template\CShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(435,  545))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)
    def get_dialog_signal(self, connect):
        if connect!= {}:
            if self.method == 0:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tf_inputlineEdit.setText(str(connect['tf']))
                self.tw_inputlineEdit.setText(str(connect['tw']))
                self.k_inputlineEdit.setText(str(connect['k']))
                self.theta_inputlineEdit.setText(str(connect['ks']))
                self.k1_lineEdit.setText(str(connect['k1']))
            else:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tf_inputlineEdit.setText(str(connect['tf']))
                self.tw_inputlineEdit.setText(str(connect['tw']))
                self.k_inputlineEdit.setText(str(connect['k']))
                self.theta_inputlineEdit.setText(str(connect['ks']))
                self.k1_lineEdit.setText(str(connect['k1']))
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


