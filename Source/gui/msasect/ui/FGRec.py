# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_FGRec import Ui_FGRec_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel, msaFEModel, GlobalBuckling, Status
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults

class FGRec_Dialog(QDialog, Ui_FGRec_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/FG-Rec.ico'))
        self.color =[]
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
            self.label.setPixmap(QPixmap("ui/Template/FG-Rec_1.jpg"))
        elif self.Law_comboBox.currentText() == "Exponential law":
            self.Law= 2
            self.k_inputlineEdit.hide()
            self.label_4.hide()
            self.label.setPixmap(QPixmap("ui/Template/FG-Rec_2.jpg"))
        elif self.Law_comboBox.currentText() == "Sigmoid law":
            self.Law= 3
            self.k_inputlineEdit.show()
            self.label_4.show()
            self.label.setPixmap(QPixmap("ui/Template/FG-Rec_3.jpg"))

    def initDialog(self):
        self.label.setPixmap(QPixmap("ui/Template/FG-Rec_1.jpg"))
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

        self.B_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.Num_inputlineEdit.setValidator(intValidator)

        self.B_inputlineEdit.setText(str(300))
        self.D_inputlineEdit.setText(str(500))
        self.Num_inputlineEdit.setText(str(int(20)))
        self.Ei_inputlineEdit.setText(str(205000))
        self.E0_inputlineEdit.setText(str(70000))
        self.k_inputlineEdit.setText(str(3))

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
                    self.fy_inputlineEdit.text()) == 0 or len(self.eu_inputlineEdit.text()) == 0 or len(self.B_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or len(self.Num_inputlineEdit.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
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
                B = float(self.B_inputlineEdit.text())
                D = float(self.D_inputlineEdit.text())
                StripNum=int(self.Num_inputlineEdit.text())
                MatIdDict = msaFEModel.Mat.ID
                if Ei<0 or E0<0 or k<0 or tμ<0 or tfy<0 or teu<0 or B<0 or D<0 or StripNum<3:
                    showMesbox(self, 'Please input correct data!')
                else:
                    values = [int(i * 255 / StripNum) for i in range(StripNum)]
                    colors = ["#%02x%02x%02x" % (int(g), 255, 255) for g in values]
                    colors.reverse()
                    if len(MatIdDict)!=0:
                        id = max(MatIdDict)
                    else:
                        id=0
                    va= [float(i+0.5) for i in range(StripNum)]
                    if self.Law== 1:
                        E=[round(E0+(Ei-E0)*(n/StripNum)**k, 3) for n in va]
                    elif self.Law==2:
                        E=[round(E0*np.exp((n/StripNum)*np.log(Ei/E0)), 3) for n in va]
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
                            E.append(E1[int(StripNum/2-1-i)])
                            colors.append(color1[i])
                    for i in range(StripNum):
                        msaFEModel.Mat.Add(tID=id+i+1, tE=E[i], tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=colors[i])
                        self.accept()
                    Rva = float(D/StripNum)
                    for ii in range(StripNum):
                        msaFEModel.Point.Add(tID=1 + ii*4, ty=round(Rva*ii, 4),tz=round(0, 4))
                        msaFEModel.Point.Add(tID=2 + ii*4, ty=round(Rva*ii, 4),tz=round(B, 4))
                        msaFEModel.Point.Add(tID=3 + ii*4, ty=round(Rva*(ii+1), 4),tz=round(B, 4))
                        msaFEModel.Point.Add(tID=4 + ii*4, ty=round(Rva*(ii+1), 4),tz=round(0, 4))
                        for i in range(3):
                            msaFEModel.Outline.Add(tID=1 +i+ ii*4, tGID=1+ii, tType="S", tLID=1+ii, tPSID=i+1+ii*4, tPEID=i+2+ii*4)
                        msaFEModel.Outline.Add(tID=4 + ii * 4, tGID=1 + ii, tType="S", tLID=1 + ii,tPSID=4+ ii * 4, tPEID=1+ii*4)
                    tOID=[]
                    for ii in range(StripNum):
                        ID=[]
                        for i in range(4):
                            ID.append(int(i+1+ii*4))
                        tOID.append(ID)
                    for ii in range(len(tOID)):
                        msaFEModel.Loop.Add(tID=1+ii, tOID=tOID[ii])
                    for i in range(StripNum):
                        msaFEModel.Group.Add(tID=1+i, tMID=id+1+i, tLID=[i+1])
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