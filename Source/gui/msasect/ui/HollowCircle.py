# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_HollowCircle import Ui_HollowCircle_Dialog
from gui.msasect.ui.HollowCircleDb import HollowCircleDb_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class HollowCircle_Dialog(QDialog, Ui_HollowCircle_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Hollow Circle.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        # self.showImage()
        self.method=0
        self.mw = mw
        self.initDialog()
        if self.mw.Outline_radioButton.isChecked() == True:
            self.Outline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Circle_Ol.jpg"))
            self.method = 1
        elif self.mw.Centerline_radioButton.isChecked() == True:
            self.Centerline_radioButton.setChecked(True)
            self.label.setPixmap(QPixmap("ui/Template/Hollow Circle_Cl.jpg"))
            self.method = 0

    def initDialog(self):
        # self.MatID_Input.setEnabled(False)
        MatIdDict = msaModel.Mat.ID
        if not MatIdDict:
            AddId = 1
        else:
            maxId = max(MatIdDict.keys(), key=(lambda x:x))
            AddId = maxId + 1
        self.ID_inputlineEdit.setText(str(int(AddId)))
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
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
        self.tw_inputlineEdit.setValidator(doubleValidator)

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Circle_Cl.jpg"))
        self.method = 0
        radioButton = 0
        self.Methodsignal.emit(radioButton)
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label.setPixmap(QPixmap("ui/Template/Hollow Circle_Ol.jpg"))
        self.method = 1
        radioButton = 1
        self.Methodsignal.emit(radioButton)
        self.B_inputlineEdit.clear()
        self.D_inputlineEdit.clear()
        self.tw_inputlineEdit.clear()

    @Slot()
    def on_Import_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Ui = HollowCircleDb_Dialog(self)
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
        theta=0
        num = 50
        try:
            if len(self.E_inputlineEdit.text()) == 0 or len(self.G_inputlineEdit.text()) == 0 or len(
                    self.fy_inputlineEdit.text()) == 0 or len(self.B_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 or len(
                    self.tw_inputlineEdit.text()) == 0 :
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
                D = float(self.D_inputlineEdit.text())
                tw = float(self.tw_inputlineEdit.text())
                if tw>=0.5*B or tw>=0.5*D or B<0 or D<0 or tw<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    MatIdDict = msaModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        if self.method == 0:
                            msaModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy,  tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            for i in range(num):
                                msaModel.Point.Add(tID=(i+1), ty=np.around((D/2-0.5*tw)*np.cos(theta), decimals=3), tz=np.around((B/2-0.5*tw)*np.sin(theta), decimals=3), tstress=Stress_input)
                                theta+=2*np.pi/(num)
                            for i in range(num-1):
                                msaModel.Segment.Add(tID=(i+1), tMaterialID=id, tPSID=(i+1), tPEID=(i+2), tSegThick=tw)
                            msaModel.Segment.Add(tID=(num), tMaterialID=id, tPSID=(num), tPEID=1, tSegThick=tw)
                        else:
                            msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='S', tColor=self.color)
                            self.accept()
                            for i in range(num):
                                msaFEModel.Point.Add(tID=i + 1, ty=np.around(D/2 * np.cos(theta), decimals=3),
                                                     tz=np.around(B/2 * np.sin(theta), decimals=3))
                                theta += 2 * np.pi / (num)
                            for i in range(num):
                                msaFEModel.Point.Add(tID=i + 1 + num, ty=np.around((D/2 - tw) * np.cos(theta), decimals=3),
                                                     tz=np.around((B/2 - tw) * np.sin(theta), decimals=3))
                                theta += 2 * np.pi / (num)
                            for i in range(num - 1):
                                msaFEModel.Outline.Add(tID=i + 1, tGID=1, tType="S", tLID=1, tPSID=i + 1, tPEID=i + 2)
                            msaFEModel.Outline.Add(tID=num, tGID=1, tType="S", tLID=1, tPSID=num, tPEID=1)
                            for i in range(num - 1):
                                msaFEModel.Outline.Add(tID=i + num + 1, tGID=1, tType="O", tLID=2, tPSID=i + 1 + num,
                                                       tPEID=i + 2 + num)
                            msaFEModel.Outline.Add(tID=num * 2, tGID=1, tType="O", tLID=2, tPSID=num * 2, tPEID=1 + num)
                            tOID1 = []
                            tOID2 = []
                            for ii in range(num):
                                tOID1.append(ii + 1)
                            for ii in range(num):
                                tOID2.append(ii + 1 + num)
                            msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                            msaFEModel.Loop.Add(tID=2, tOID=tOID2)
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
    #     self.imgShow.load("ui\Template\ElliShape.png")
    #     self.imgShowItem = QGraphicsPixmapItem()
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow))
    #     self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(440,  370))
    #     self.graphicsView.scene_img.addItem(self.imgShowItem)
    #     self.graphicsView.setScene(self.graphicsView.scene_img)
    #     #self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)), Qt.IgnoreAspectRatio)
    def get_dialog_signal(self, connect):
        if connect!= {}:
            if self.method == 0:
                self.B_inputlineEdit.setText(str(connect['B(D)']))
                self.D_inputlineEdit.setText(str(connect['B(D)']))
                self.tw_inputlineEdit.setText(str(connect['tw']))
            else:
                self.B_inputlineEdit.setText(str(connect['B(D)']))
                self.D_inputlineEdit.setText(str(connect['B(D)']))
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


