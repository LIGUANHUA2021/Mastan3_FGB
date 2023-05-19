# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_HollowTri import Ui_HollowTri_Dialog
from gui.msasect.ui.HollowTriDb import HollowTriDb_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class HollowTri_Dialog(QDialog, Ui_HollowTri_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Hollow Tri.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method = 0
        # self.showImage()
        self.mw = mw
        if self.mw.Outline_radioButton.isChecked()==True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Tri.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked()==True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Tri_Cl.jpg"))
            self.method = 0
        self.initDialog()

    def initDialog(self):
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x:x))
        AddId =  1
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
        self.B1_lineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.tw_lineEdit.setValidator(doubleValidator)

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Tri_Cl.jpg"))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Tri.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)


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
                    self.fy_inputlineEdit.text()) == 0 or len(self.B_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or len(self.tw_lineEdit.text()) == 0 or  float(self.B_inputlineEdit.text())<=0 or float(self.tw_lineEdit.text())>=float(self.D_inputlineEdit.text())/3 :
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
                tE = float(self.E_inputlineEdit.text())
                tμ = float(self.G_inputlineEdit.text())
                tfy = float(self.fy_inputlineEdit.text())
                id = int(self.ID_inputlineEdit.text())
                teu = float(self.eu_inputlineEdit.text())
                B = float(self.B_inputlineEdit.text())
                B1 = float(self.B1_lineEdit.text())
                D = float(self.D_inputlineEdit.text())
                tw = float(self.tw_lineEdit.text())
                if B<0 or D<0 or tw<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    MatIdDict = msaFEModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method==1:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='C', tColor=self.color)
                            self.accept()
                            if 0<B1<B and B>0:
                                k1=D/B1
                                c1=-tw*(1+k1**2)**0.5
                                k2=-D/(B-B1)
                                c3=D-B1*k2
                                c2=c3-tw*(1+k2**2)**0.5
                                z5=(c2-c1)/(k1-k2)
                                y5=(c1*k2-c2*k1)/(k2-k1)
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=D, tz=-B1)
                                msaFEModel.Point.Add(tID=3, ty=0, tz=-B)
                                msaFEModel.Point.Add(tID=4, ty=tw, tz=-(np.around(((tw-c1)/k1), decimals=3 )))
                                msaFEModel.Point.Add(tID=5, ty=np.around(y5, decimals=3 ), tz=-(np.around(z5, decimals=3 )))
                                msaFEModel.Point.Add(tID=6, ty=tw, tz=-(np.around((tw-c2)/k2,decimals=3 )))
                            elif B1==0 and B>0:
                                k1 = -D / B
                                c1=D
                                c2=c1-tw*(1+k1**2)**0.5
                                k2=k1
                                y5=k2*tw+c2
                                z6=(tw-c2)/k2
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=D, tz=-B1)
                                msaFEModel.Point.Add(tID=3, ty=0, tz=-B)
                                msaFEModel.Point.Add(tID=4, ty=tw, tz=-tw)
                                msaFEModel.Point.Add(tID=5, ty=np.around(y5, decimals=3), tz=-tw)
                                msaFEModel.Point.Add(tID=6, ty=tw, tz=-(np.around(z6, decimals=3)))
                            elif B1==B and B>0:
                                k1 = D / B
                                c1 = 0
                                k2=k1
                                c2=c1-tw*(1+k1**2)**0.5
                                y5 = k2 * (B-tw) + c2
                                z6 = (tw - c2) / k2
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=D, tz=-B1)
                                msaFEModel.Point.Add(tID=3, ty=0, tz=-B)
                                msaFEModel.Point.Add(tID=4, ty=tw, tz=-B+tw)
                                msaFEModel.Point.Add(tID=5, ty=np.around(y5, decimals=3), tz=-(B-tw))
                                msaFEModel.Point.Add(tID=6, ty=tw, tz=-(np.around(z6, decimals=3)))
                            elif B1<0 and B>0:
                                k1 = D / B1
                                c1 = +tw * (1 + k1 ** 2) ** 0.5
                                k2 = -D / (B - B1)
                                c3 = D - B1 * k2
                                c2 = c3 - tw * (1 + k2 ** 2) ** 0.5
                                z5 = (c2 - c1) / (k1 - k2)
                                y5 = (c1 * k2 - c2 * k1) / (k2 - k1)
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=D, tz=-B1)
                                msaFEModel.Point.Add(tID=3, ty=0, tz=-B)
                                msaFEModel.Point.Add(tID=4, ty=tw, tz=-(np.around(((tw - c1) / k1), decimals=3)))
                                msaFEModel.Point.Add(tID=5, ty=np.around(y5, decimals=3), tz=-(np.around(z5, decimals=3)))
                                msaFEModel.Point.Add(tID=6, ty=tw, tz=-(np.around((tw - c2) / k2, decimals=3)))
                            elif B1>B and B>0:
                                k1 = D / B1
                                c1 = -tw * (1 + k1 ** 2) ** 0.5
                                k2 = D / (B1 - B)
                                c3 = D - B1 * k2
                                c2 = c3 + tw * (1 + k2 ** 2) ** 0.5
                                z5 = (c2 - c1) / (k1 - k2)
                                y5 = (c1 * k2 - c2 * k1) / (k2 - k1)
                                msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                                msaFEModel.Point.Add(tID=2, ty=D, tz=-B1)
                                msaFEModel.Point.Add(tID=3, ty=0, tz=-B)
                                msaFEModel.Point.Add(tID=4, ty=tw, tz=-(np.around(((tw - c1) / k1), decimals=3)))
                                msaFEModel.Point.Add(tID=5, ty=np.around(y5, decimals=3), tz=-(np.around(z5, decimals=3)))
                                msaFEModel.Point.Add(tID=6, ty=tw, tz=-(np.around((tw - c2) / k2, decimals=3)))
                            msaFEModel.Outline.Add(tID=1, tGID=1, tType="S", tLID=1, tPSID=1, tPEID=2)
                            msaFEModel.Outline.Add(tID=2, tGID=1, tType="S", tLID=1, tPSID=2, tPEID=3)
                            msaFEModel.Outline.Add(tID=3, tGID=1, tType="S", tLID=1, tPSID=3, tPEID=1)
                            msaFEModel.Outline.Add(tID=4, tGID=1, tType="O", tLID=2, tPSID=4, tPEID=5)
                            msaFEModel.Outline.Add(tID=5, tGID=1, tType="O", tLID=2, tPSID=5, tPEID=6)
                            msaFEModel.Outline.Add(tID=6, tGID=1, tType="O", tLID=2, tPSID=6, tPEID=4)
                            msaFEModel.Loop.Add(tID=1, tOID=[1, 2, 3])
                            msaFEModel.Loop.Add(tID=2, tOID=[4, 5, 6])
                            msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1,2])
                        else:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu, tType='S',
                                             tColor=self.color)
                            self.accept()
                            msaModel.Point.Add(tID=1, ty=0, tz=0, tstress=Stress_input)
                            msaModel.Point.Add(tID=2, ty=0, tz=B, tstress=Stress_input)
                            msaModel.Point.Add(tID=3, ty=D, tz=B-B1, tstress=Stress_input)
                            msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=tw)
                            msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=2, tPEID=3, tSegThick=tw)
                            msaModel.Segment.Add(tID=3, tMaterialID=id, tPSID=3, tPEID=1, tSegThick=tw)
                        self.mw.ResetTable()
                        self.mw.View.autoRange()
                        self.mw.setWindowTitle(
                            'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections'
                        )
                        msaModel.FileInfo.FileName = ""
                        self.mw.SectIDInput_lineEdit.setText('HollowTri01')
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

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowTriDb_Dialog(self)
        Ui.OKsignal.connect(self.get_dialog_signal)
        # print(Model.msaModel.Mat.ID)
        Ui.exec()

    def get_dialog_signal(self, connect):
        if connect != {}:
            if self.method == 0:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.B1_lineEdit.setText(str(connect['B1']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tw_lineEdit.setText(str(connect['tw']))
            else:
                self.B_inputlineEdit.setText(str(connect['B']))
                self.B1_lineEdit.setText(str(connect['B1']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tw_lineEdit.setText(str(connect['tw']))
            self.mw.SectIDInput_lineEdit.setText(str(connect['Type']))
            if connect["unit"] == 0:
                self.E_inputlineEdit.setText(str(29733))
                self.fy_inputlineEdit.setText(str(50))
                self.eu_inputlineEdit.setText(str(0.15))
                self.G_inputlineEdit.setText(str(0.3))
            else:
                self.E_inputlineEdit.setText(str(205000))
                self.fy_inputlineEdit.setText(str(345))
                self.eu_inputlineEdit.setText(str(0.15))
                self.G_inputlineEdit.setText(str(0.3))

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