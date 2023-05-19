# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
from gui.msasect.ui.Ui_ZSection import Ui_ZSection_Dialog
from gui.msasect.ui.ZSectionDb import ZSectionDb_Dialog
import numpy as np
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


import traceback
class ZSection_Dialog(QDialog, Ui_ZSection_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Z-Section.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method=0
        # self.showImage()
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked() == True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Z-Section_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked() == True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Z-Section_Cl.jpg"))
            self.method = 0

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x: x))
        #     AddId = maxId + 1
        AddId = 1
        self.ID_inputlineEdit.setText(str(int(AddId)))
        self.ID_inputlineEdit.setText(str(int(AddId)))
        self.E_inputlineEdit.setText(str(205000))
        self.fy_inputlineEdit.setText(str(345))
        self.eu_inputlineEdit.setText(str(0.15))
        self.G_inputlineEdit.setText(str(0.3))
        # 设置validator
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
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

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Z-Section_Cl.jpg"))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.B1_inputlineEdit.clear()
        self.B2_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.t1_inputlineEdit.clear()
        self.t2_inputlineEdit.clear()
        self.t3_inputlineEdit.clear()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Z-Section_Ol.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.B1_inputlineEdit.clear()
        self.B2_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.t1_inputlineEdit.clear()
        self.t2_inputlineEdit.clear()
        self.t3_inputlineEdit.clear()

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = ZSectionDb_Dialog(self)
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
                    self.fy_inputlineEdit.text()) == 0 or len(self.B1_inputlineEdit.text()) == 0 or len(
                    self.B2_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or len(
                    self.t1_inputlineEdit.text()) == 0 or len(self.t2_inputlineEdit.text()) == 0 or len(
                    self.t3_inputlineEdit.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
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
                # print("teu = ", teu)
                MatIdDict = msaModel.Mat.ID
                if B1<0 or B2< 0 or D<0 or t1< 0 or t2<0 or t3<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
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
                    if B2<=t2 or B1<=t2 or D<=(t1+t2) :
                        showMesbox(self, 'Please input correct data!')
                    else:
                        MatIdDict = msaModel.Mat.ID
                        if id in MatIdDict:
                            showMesbox(self, 'Material ID has been used!')
                        else:
                            if self.method == 0:
                                msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=self.color)
                                self.accept()
                                msaModel.Point.Add(tID=1, ty=0, tz=0, tstress=Stress_input)
                                msaModel.Point.Add(tID=2, ty=0, tz=np.around(B1-0.5*t2, decimals=3), tstress=Stress_input)
                                msaModel.Point.Add(tID=3, ty=np.around(-(D-0.5*t1)+0.5*t3, decimals=3), tz=np.around(-B2+0.5*t2 , decimals=3), tstress=Stress_input)
                                msaModel.Point.Add(tID=4, ty=np.around(-(D-0.5*t1)+0.5*t3, decimals=3), tz=0, tstress=Stress_input)
                                msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=t1)
                                msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=1, tPEID=4, tSegThick=t2)
                                msaModel.Segment.Add(tID=3, tMaterialID=id, tPSID=3, tPEID=4, tSegThick=t3)
                            else:
                                msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S',
                                                   tColor=self.color)
                                self.accept()
                                B1 = float(self.B1_inputlineEdit.text())
                                B2 = float(self.B2_inputlineEdit.text())
                                D = float(self.D_inputlineEdit.text())
                                t1 = float(self.t1_inputlineEdit.text())
                                t2 = float(self.t2_inputlineEdit.text())
                                t3 = float(self.t3_inputlineEdit.text())
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=0, tz=-B1)
                                msaFEModel.Point.Add(tID=3, ty=-D+t3, tz=-B1)
                                msaFEModel.Point.Add(tID=4, ty=-D+t3, tz=np.around(-(B1+B2-t2), decimals=3))
                                msaFEModel.Point.Add(tID=5, ty=-D, tz=np.around(-(B1+B2-t2),decimals=3))
                                msaFEModel.Point.Add(tID=6, ty=-D, tz=np.around(-(B1 - t2),decimals=3))
                                msaFEModel.Point.Add(tID=7, ty=-t1, tz=np.around(-(B1 - t2),decimals=3))
                                msaFEModel.Point.Add(tID=8, ty=-t1, tz=0)
                                for i in range(7):
                                    msaFEModel.Outline.Add(tID=i + 1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                                msaFEModel.Outline.Add(tID=8, tGID=1, tType="S", tLID=1, tPSID=8, tPEID=1)
                                msaFEModel.Loop.Add(tID=1, tOID=[1, 2, 3, 4, 5, 6, 7, 8])
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

    colname = '#ffffff'

    @Slot()
    def on_ColorButton_clicked(self):

        """
        Slot documentation goes here.
        """
        #self.ColorButton.setStyleSheet(f"QPushButton#ColorButton{'{{'}background:{colname}{'}}'}")
        # TODO: not implemented yet
        #raise NotImplementedError


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
    #     self.imgShow.load("ui\Template\ZShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(445,  540))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)

    def get_dialog_signal(self, connect):
        if connect!= {}:
            if self.method == 0:
                self.B1_inputlineEdit.setText(str(connect['B1(2)']))
                self.B2_inputlineEdit.setText(str(connect['B1(2)']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.t1_inputlineEdit.setText(str(connect['tf']))
                self.t2_inputlineEdit.setText(str(connect['tw']))
                self.t3_inputlineEdit.setText(str(connect['tf']))
            else:
                self.B1_inputlineEdit.setText(str(connect['B1(2)']))
                self.B2_inputlineEdit.setText(str(connect['B1(2)']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.t1_inputlineEdit.setText(str(connect['tf']))
                self.t2_inputlineEdit.setText(str(connect['tw']))
                self.t3_inputlineEdit.setText(str(connect['tf']))
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


