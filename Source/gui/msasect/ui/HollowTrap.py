# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from gui.msasect.ui.Ui_HollowTrap import Ui_HollowTrap_Dialog
from gui.msasect.ui.HollowTrapDb import HollowTrapDb_Dialog
from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QPixmap, QDoubleValidator, QIntValidator, QIcon
import traceback
import numpy as np
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class HollowTrap_Dialog(QDialog, Ui_HollowTrap_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Hollow Trap.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        self.method=0
        # self.showImage()
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked() == True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Trap_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked() == True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Trap_Cl.jpg"))
            self.method = 0


    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x:x))
        AddId =  1
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

        self.B1_inputlineEdit.setValidator(doubleValidator)
        self.B1_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)
        self.tf1_inputlineEdit.setValidator(doubleValidator)
        self.tf2_inputlineEdit.setValidator(doubleValidator)
        self.tw_inputlineEdit.setValidator(doubleValidator)

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Trap_Cl.jpg"))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.B1_inputlineEdit.clear()
        self.B2_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tf1_inputlineEdit.clear()
        self.tf2_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Trap_Ol.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.B1_inputlineEdit.clear()
        self.B2_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tf1_inputlineEdit.clear()
        self.tf2_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowTrapDb_Dialog (self)
        # print(Model.msaModel.Mat.ID)
        Ui.OKsignal.connect(self.get_dialog_signal)
        Ui.exec()

    @Slot()
    def on_OK_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Stress_input = 0
        try:
            if len(self.E_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0 or len(
                    self.fy_inputlineEdit.text()) == 0 or len(self.B1_inputlineEdit.text()) == 0 or len(self.B2_inputlineEdit.text()) == 0 or len(
                self.tf1_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or len(
                self.tf2_inputlineEdit.text()) == 0 or len(self.tw_inputlineEdit.text()) == 0:
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
                tf1 = float(self.tf1_inputlineEdit.text())
                tf2 = float(self.tf2_inputlineEdit.text())
                tw = float(self.tw_inputlineEdit.text())
                MatIdDict = msaModel.Mat.ID
                if (tf1+tf2)>=D or tw>=0.5*B1 or tw>=0.5*B2 or B1<0 or B2<0 or D<0 or tf1<0 or tf2<0 or tw<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method == 0:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy,  tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            msaModel.Point.Add(tID=1, ty=0, tz=B1/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=2, ty=0, tz=-B1/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=3, ty=-D, tz=-B2/2, tstress=Stress_input)
                            msaModel.Point.Add(tID=4, ty=-D, tz=B2/2, tstress=Stress_input)
                            msaModel.Segment.Add(tID=1, tMaterialID=id, tPSID=1, tPEID=2, tSegThick=tf1)
                            msaModel.Segment.Add(tID=2, tMaterialID=id, tPSID=2, tPEID=3, tSegThick=tw)
                            msaModel.Segment.Add(tID=3, tMaterialID=id, tPSID=3, tPEID=4, tSegThick=tf2)
                            msaModel.Segment.Add(tID=4, tMaterialID=id, tPSID=4, tPEID=1, tSegThick=tw)
                        else:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            B1 = float(self.B1_inputlineEdit.text())
                            B2 = float(self.B2_inputlineEdit.text())
                            D = float(self.D_inputlineEdit.text())
                            tf1 = float(self.tf1_inputlineEdit.text())
                            tf2 = float(self.tf2_inputlineEdit.text())
                            tw = float(self.tw_inputlineEdit.text())
                            msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                            msaFEModel.Point.Add(tID=2, ty=0, tz=B1)
                            msaFEModel.Point.Add(tID=3, ty=-D, tz=0.5*B1+0.5*B2)
                            msaFEModel.Point.Add(tID=4, ty=-D, tz=0.5*B1-0.5*B2)
                            if B1 < B2:
                                k=D/(0.5*(B2-B1))
                                b=-1*tw*(1+k**2)**(0.5)
                                msaFEModel.Point.Add(tID=5, tz=np.around((-tf1-b)/k, decimals=3), ty=-tf1)
                                msaFEModel.Point.Add(tID=6, tz=np.around((B1-(-tf1-b)/k), decimals=3), ty=-tf1)
                                msaFEModel.Point.Add(tID=7, tz=np.around((B1-(-D+tf2-b)/k), decimals=3), ty=-D+tf2)
                                msaFEModel.Point.Add(tID=8, tz=np.around((-D+tf2-b)/k, decimals=3), ty=-D+tf2)
                            elif B1>B2:
                                k = -D / (0.5 * (B1 - B2))
                                b = tw * (1 + k ** 2) ** (0.5)
                                msaFEModel.Point.Add(tID=5, tz=np.around((-tf1 - b) / k, decimals=3), ty=-tf1)
                                msaFEModel.Point.Add(tID=6, tz=np.around((B1 - (-tf1 - b) / k), decimals=3), ty=-tf1)
                                msaFEModel.Point.Add(tID=7, tz=np.around(B1-(-D + tf2 - b) / k, decimals=3),ty=-D + tf2)
                                msaFEModel.Point.Add(tID=8, tz=np.around((-D + tf2 - b) / k, decimals=3), ty=-D + tf2)
                            elif B1==B2:
                                msaFEModel.Point.Add(tID=5, ty=-tf1, tz=tw)
                                msaFEModel.Point.Add(tID=6, ty=-tf1, tz=B1 - tw)
                                msaFEModel.Point.Add(tID=7, ty=-D + tf2, tz=B2 - tw)
                                msaFEModel.Point.Add(tID=8, ty=-D + tf2, tz=tw)
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
    #     self.imgShow.load("ui\Template\TrapShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(435,  430))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)
    def get_dialog_signal(self, connect):
        if connect!= {}:
            if self.method == 0:
                self.B1_inputlineEdit.setText(str(connect['B1']))
                self.B2_inputlineEdit.setText(str(connect['B2']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tf1_inputlineEdit.setText(str(connect['tf1']))
                self.tf2_inputlineEdit.setText(str(connect['tf2']))
                self.tw_inputlineEdit.setText(str(connect['tw']))
            else:
                self.B1_inputlineEdit.setText(str(connect['B1']))
                self.B2_inputlineEdit.setText(str(connect['B2']))
                self.D_inputlineEdit.setText(str(connect['D']))
                self.tf1_inputlineEdit.setText(str(connect['tf1']))
                self.tf2_inputlineEdit.setText(str(connect['tf2']))
                self.tw_inputlineEdit.setText(str(connect['tw']))
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
