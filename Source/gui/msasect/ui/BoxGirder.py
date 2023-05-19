# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_BoxGirder import Ui_BoxGirder_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel, msaFEModel, GlobalBuckling, Status
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults

class BoxGirder_Dialog(QDialog, Ui_BoxGirder_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Box Girder.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        # self.showImage()
        self.mw = mw
        self.initDialog()
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
        self.method = 1

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x:x))
        self.label.setPixmap(QPixmap("ui/Template/Box Girder.jpg"))
        AddId = 1
        self.ID_inputlineEdit.setText(str(int(AddId)))
        self.E_inputlineEdit.setText(str(34500))
        self.fy_inputlineEdit.setText(str(42.5))
        self.eu_inputlineEdit.setText(str(0.0033))
        self.G_inputlineEdit.setText(str(0.2))
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
        self.D1_lineEdit.setValidator(doubleValidator)
        self.D2_lineEdit.setValidator(doubleValidator)
        self.D3_lineEdit.setValidator(doubleValidator)
        self.D4_lineEdit.setValidator(doubleValidator)
        self.tf_lineEdit.setValidator(doubleValidator)
        self.tw1_lineEdit.setValidator(doubleValidator)
        self.tw2_lineEdit.setValidator(doubleValidator)
        self.tw3_lineEdit.setValidator(doubleValidator)

        self.B1_inputlineEdit.setText(str(6000))
        self.B2_inputlineEdit.setText(str(4000))
        self.D1_lineEdit.setText(str(100))
        self.D2_lineEdit.setText(str(1500))
        self.D3_lineEdit.setText(str(1250))
        self.D4_lineEdit.setText(str(200))
        self.tf_lineEdit.setText(str(150))
        self.tw1_lineEdit.setText(str(200))
        self.tw2_lineEdit.setText(str(200))
        self.tw3_lineEdit.setText(str(200))

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Box Girder.jpg"))
        self.method = 0

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Box Girder.jpg"))
        self.method = 1


    @Slot()
    def on_OK_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        Stress_input = 0
        theta=0
        num = 50
        try:
            if len(self.E_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0 or len(
                    self.fy_inputlineEdit.text()) == 0 or len(self.B1_inputlineEdit.text()) == 0 or len(self.B2_inputlineEdit.text()) == 0 or \
                    len(self.D1_lineEdit.text()) == 0 or len(self.D2_lineEdit.text()) == 0 or len(self.D3_lineEdit.text()) == 0 or \
                    len(self.D4_lineEdit.text()) == 0 or len(self.tf_lineEdit.text()) == 0 or len(self.tw1_lineEdit.text()) == 0 or len(self.tw2_lineEdit.text()) == 0 or \
                    (float(self.D3_lineEdit.text())+float(self.D4_lineEdit.text()))>=(float(self.D1_lineEdit.text())+float(self.D2_lineEdit.text())+float(self.tf_lineEdit.text())) or \
                    (float(self.tw1_lineEdit.text())+float(self.tw2_lineEdit.text())+float(self.tw3_lineEdit.text()))>=(float(self.B2_inputlineEdit.text())) or \
                    float(self.B2_inputlineEdit.text())>float(self.B1_inputlineEdit.text()):
                showMesbox(self, 'Please input correct data!')
            else:
                msaFEModel.ResetAll()
                msaFEModel.Mat.Reset()
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
                D1 = float(self.D1_lineEdit.text())
                D2 = float(self.D2_lineEdit.text())
                D3 = float(self.D3_lineEdit.text())
                D4 = float(self.D4_lineEdit.text())
                tf = float(self.tf_lineEdit.text())
                tw1 = float(self.tw1_lineEdit.text())
                tw2 = float(self.tw2_lineEdit.text())
                tw3 = float(self.tw3_lineEdit.text())
                if B1 < 0 or B2 < 0 or D1 < 0 or D2 < 0 or D3 < 0 or D4 < 0 or tf<0 or tw1<0 or tw2<0 or tw3<0 or tE < 0 or tμ < 0 or tfy < 0 or teu < 0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    MatIdDict = msaFEModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='C', tColor=self.color)
                        self.accept()
                        msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                        msaFEModel.Point.Add(tID=2, ty=0, tz=B1)
                        msaFEModel.Point.Add(tID=3, ty=-tf, tz=B1)
                        msaFEModel.Point.Add(tID=4, ty=-tf-D1, tz=0.5*(B1+B2))
                        msaFEModel.Point.Add(tID=5, ty=-tf-D1-D2, tz=0.5*(B1+B2))
                        msaFEModel.Point.Add(tID=6, ty=-tf - D1-D2, tz=0.5 * (B1 - B2))
                        msaFEModel.Point.Add(tID=7, ty=-tf-D1, tz=0.5*(B1-B2))
                        msaFEModel.Point.Add(tID=8, ty=-tf, tz=0)
                        msaFEModel.Point.Add(tID=9, ty=-tf-D1-D2+D4+D3, tz=0.5*(B1-B2)+tw1)
                        msaFEModel.Point.Add(tID=10, ty=-tf - D1 - D2 + D4+D3, tz=0.5 * (B1 - tw2))
                        msaFEModel.Point.Add(tID=11, ty=-tf - D1 - D2 + D4 , tz=0.5 * (B1 - tw2))
                        msaFEModel.Point.Add(tID=12, ty=-tf - D1 - D2 + D4 , tz=0.5*(B1-B2)+tw1)
                        msaFEModel.Point.Add(tID=13, ty=-tf - D1 - D2 + D4+D3, tz=0.5 * (B1 + tw2))
                        msaFEModel.Point.Add(tID=14, ty=-tf - D1 - D2 + D4 + D3, tz=0.5*(B1+B2)-tw3)
                        msaFEModel.Point.Add(tID=15, ty=-tf - D1 - D2 + D4 , tz=0.5 * (B1 + B2) - tw3)
                        msaFEModel.Point.Add(tID=16, ty=-tf - D1 - D2 + D4 , tz=0.5 * (B1 + tw2))
                        for i in range(7):
                            msaFEModel.Outline.Add(tID=1+i, tGID=1, tType="S", tLID=1, tPSID=i+1, tPEID=i+2)
                        msaFEModel.Outline.Add(tID=8, tGID=1, tType="S", tLID=1, tPSID=8, tPEID=1)
                        msaFEModel.Outline.Add(tID=9, tGID=1, tType="O", tLID=2, tPSID=9, tPEID=10)
                        msaFEModel.Outline.Add(tID=10, tGID=1, tType="O", tLID=2, tPSID=10, tPEID=11)
                        msaFEModel.Outline.Add(tID=11, tGID=1, tType="O", tLID=2, tPSID=11, tPEID=12)
                        msaFEModel.Outline.Add(tID=12, tGID=1, tType="O", tLID=2, tPSID=12, tPEID=9)
                        msaFEModel.Outline.Add(tID=13, tGID=1, tType="O", tLID=3, tPSID=13, tPEID=14)
                        msaFEModel.Outline.Add(tID=14, tGID=1, tType="O", tLID=3, tPSID=14, tPEID=15)
                        msaFEModel.Outline.Add(tID=15, tGID=1, tType="O", tLID=3, tPSID=15, tPEID=16)
                        msaFEModel.Outline.Add(tID=16, tGID=1, tType="O", tLID=3, tPSID=16, tPEID=13)
                        msaFEModel.Loop.Add(tID=1, tOID=[1, 2, 3,4,5,6,7,8])
                        msaFEModel.Loop.Add(tID=2, tOID=[9,10,11,12])
                        msaFEModel.Loop.Add(tID=3, tOID=[13, 14, 15, 16])
                        msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1, 2,3])
                    self.mw.ResetTable()
                    self.mw.View.autoRange()
                    self.mw.setWindowTitle(
                        'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections'
                    )
                    msaModel.FileInfo.FileName = ""
                    self.mw.SectIDInput_lineEdit.setText('BoxGirder01')
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
    #     self.imgShow.load("ui\Template\ElliShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(440,  370))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)