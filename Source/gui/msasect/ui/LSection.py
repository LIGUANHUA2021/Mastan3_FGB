# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults
from gui.msasect.ui.Ui_LSection import Ui_LSection_Dialog
from gui.msasect.ui.LSectionDb import LSectionDb_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor,  QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
import numpy as np

class LSection_Dialog(QDialog, Ui_LSection_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/L-Section.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method=0
        # self.showImage()
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked() == True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/L-Section_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked() == True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/L-Section_Cl.jpg"))
            self.method = 0
        if self.Centerline_radioButton.isChecked() == True:
            self.k_inputlineEdit.hide()
            self.label_2.hide()
        else:
            self.k_inputlineEdit.show()
            self.label_2.show()

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x:x))
        #     AddId = maxId + 1
        AddId = 1
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
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
        self.t1_inputlineEdit.setValidator(doubleValidator)
        self.t2_inputlineEdit.setValidator(doubleValidator)
        self.k_inputlineEdit.setValidator(doubleValidator)

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/L-Section_Cl.jpg"))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.k_inputlineEdit.hide()
        self.label_2.hide()
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.t1_inputlineEdit.clear()
        self.t2_inputlineEdit.clear()
        self.k_inputlineEdit.clear()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/L-Section_Ol.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.k_inputlineEdit.show()
        self.label_2.show()
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.t1_inputlineEdit.clear()
        self.t2_inputlineEdit.clear()
        self.k_inputlineEdit.clear()

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = LSectionDb_Dialog(self)
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
                    self.fy_inputlineEdit.text()) == 0 or len(self.B_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or len(
                    self.t1_inputlineEdit.text()) == 0 or len(self.t2_inputlineEdit.text()) == 0:
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
                t1 = float(self.t1_inputlineEdit.text())
                t2 = float(self.t2_inputlineEdit.text())
                k = max(t1,t2)
                if len(self.k_inputlineEdit.text()) != 0 :
                    k = float(self.k_inputlineEdit.text())
                if t1>=B or t2>=D or k<t1 or k<t2 or k>=0.8*(B-t1) or k>=0.8*(D-t2) or B<0 or D<0 or t1<0 or t2<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    MatIdDict = msaModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method == 0:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy,  tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            msaModel.Point.Add(tID=1, ty=0, tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=2, ty=np.around(-D+0.5*t2, decimals=3), tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=3, ty=np.around(-D+0.5*t2, decimals=3), tz=-(np.around(B-0.5*t1, decimals=3)), tstress=Stress_input)
                            msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=t1)
                            msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=2, tPEID=3, tSegThick=t2)
                        else:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            if k>t2:
                                k = float(self.k_inputlineEdit.text())
                                oy1=-0.6*t1
                                oz1=0
                                oy2=-D+k
                                oz2=t1+k-t2
                                oy3=-D
                                oz3=B-0.6*t2
                                r=k-t2
                                msaFEModel.Point.Add(tID=1, ty=0,tz=0)
                                msaFEModel.Point.Add(tID=2, ty=np.around(0.6*t1 * np.cos(1 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(t1 * np.sin(1 / 12 * np.pi) + oz1, decimals=3)))
                                msaFEModel.Point.Add(tID=3, ty=np.around(0.6*t1 * np.cos(2 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(t1 * np.sin(2 / 12 * np.pi) + oz1, decimals=3)))
                                msaFEModel.Point.Add(tID=4, ty=np.around(0.6*t1 * np.cos(3 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(t1 * np.sin(3 / 12 * np.pi) + oz1, decimals=3)))
                                msaFEModel.Point.Add(tID=5, ty=np.around(0.6*t1 * np.cos(4 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(t1 * np.sin(4 / 12 * np.pi) + oz1, decimals=3)))
                                msaFEModel.Point.Add(tID=6, ty=np.around(0.6*t1 * np.cos(5 / 12 * np.pi) + oy1, decimals=3),tz=-(np.around(t1 * np.sin(5 / 12 * np.pi) + oz1, decimals=3)))
                                msaFEModel.Point.Add(tID=7, ty=np.around(-0.6*t1, decimals=3), tz=-t1)
                                msaFEModel.Point.Add(tID=8, ty=-D + k, tz=-t1)
                                msaFEModel.Point.Add(tID=9, ty=np.around(r * np.cos(11 / 8 * np.pi) + oy2, decimals=3),tz=-(np.around(r * np.sin(11 / 8 * np.pi) + oz2, decimals=3)))
                                msaFEModel.Point.Add(tID=10, ty=np.around(r * np.cos(10 / 8 * np.pi) + oy2, decimals=3),tz=-(np.around(r * np.sin(10 / 8 * np.pi) + oz2, decimals=3)))
                                msaFEModel.Point.Add(tID=11, ty=np.around(r * np.cos(9 / 8 * np.pi) + oy2, decimals=3),tz=-(np.around(r * np.sin(9 / 8 * np.pi) + oz2, decimals=3)))
                                msaFEModel.Point.Add(tID=12, ty=-D+t2, tz=np.around(-(t1+r), decimals=3))
                                msaFEModel.Point.Add(tID=13, ty=-D+t2, tz=np.around(-(B-0.6*t2), decimals=3))
                                msaFEModel.Point.Add(tID=14, ty=np.around(t2 * np.cos(1 / 12 * np.pi) + oy3, decimals=3),tz=-(np.around(0.6*t2 * np.sin(1 / 12 * np.pi) + oz3, decimals=3)))
                                msaFEModel.Point.Add(tID=15, ty=np.around(t2 * np.cos(2 / 12 * np.pi) + oy3, decimals=3),tz=-(np.around(0.6*t2 * np.sin(2 / 12 * np.pi) + oz3, decimals=3)))
                                msaFEModel.Point.Add(tID=16, ty=np.around(t2 * np.cos(3 / 12 * np.pi) + oy3, decimals=3),tz=-(np.around(0.6*t2 * np.sin(3 / 12 * np.pi) + oz3, decimals=3)))
                                msaFEModel.Point.Add(tID=17, ty=np.around(t2 * np.cos(4 / 12 * np.pi) + oy3, decimals=3),tz=-(np.around(0.6*t2 * np.sin(4 / 12 * np.pi) + oz3, decimals=3)))
                                msaFEModel.Point.Add(tID=18, ty=np.around(t2 * np.cos(5 / 12 * np.pi) + oy3, decimals=3),tz=-(np.around(0.6*t2 * np.sin(5 / 12 * np.pi) + oz3, decimals=3)))
                                msaFEModel.Point.Add(tID=19, ty=-D, tz=-B)
                                msaFEModel.Point.Add(tID=20, ty=-D, tz=0)
                                for i in range(19):
                                    msaFEModel.Outline.Add(tID=i+1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                                msaFEModel.Outline.Add(tID=20, tGID=1, tType="S", tLID=1, tPSID=20, tPEID=1)
                                tOID1 = []
                                for ii in range(20):
                                    tOID1.append(ii + 1)
                                msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                                msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1])
                            elif k == t2:
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=0, tz=-t1)
                                msaFEModel.Point.Add(tID=3, ty=-D+t2, tz=-t1)
                                msaFEModel.Point.Add(tID=4, ty=-D + t2, tz=-B)
                                msaFEModel.Point.Add(tID=5, ty=-D, tz=-B)
                                msaFEModel.Point.Add(tID=6, ty=-D, tz=0)
                                for i in range(5):
                                    msaFEModel.Outline.Add(tID=i+1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                                msaFEModel.Outline.Add(tID=6, tGID=1, tType="S", tLID=1, tPSID=6, tPEID=1)
                                tOID1 = []
                                for ii in range(6):
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
    #     self.imgShow.load("ui\Template\LShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(435, 520))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     # self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)
    def get_dialog_signal(self, connect):
        if connect!= {}:
            if self.method == 0:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.t1_inputlineEdit.setText(str(connect['t1(2)']))
                self.t2_inputlineEdit.setText(str(connect['t1(2)']))
                self.k_inputlineEdit.setText(str(connect['k']))
            else:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.t1_inputlineEdit.setText(str(connect['t1(2)']))
                self.t2_inputlineEdit.setText(str(connect['t1(2)']))
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
