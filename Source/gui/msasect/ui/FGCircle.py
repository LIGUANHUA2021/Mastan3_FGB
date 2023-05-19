# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_FGCircle import Ui_FGCircle_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel, msaFEModel, GlobalBuckling, Status
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class FGCircle_Dialog(QDialog, Ui_FGCircle_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/FG-Circle.ico'))
        self.color = []
        # self.showImage()
        self.mw = mw
        self.initDialog()
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
        self.method = 1
        self.Law = 1
        self.Law_comboBox.currentIndexChanged.connect(self.Law_add)
        self.k_inputlineEdit.show()
        self.label_4.show()

    def Law_add(self):
        if self.Law_comboBox.currentText() == "Power law":
            self.Law = 1
            self.k_inputlineEdit.show()
            self.label_4.show()
            self.label.setPixmap(QPixmap("ui/Template/FG-Circle_1.jpg"))
        elif self.Law_comboBox.currentText() == "Exponential law":
            self.Law = 2
            self.k_inputlineEdit.hide()
            self.label_4.hide()
            self.label.setPixmap(QPixmap("ui/Template/FG-Circle_2.jpg"))
        elif self.Law_comboBox.currentText() == "Sigmoid law":
            self.Law = 3
            self.k_inputlineEdit.show()
            self.label_4.show()
            self.label.setPixmap(QPixmap("ui/Template/FG-Circle_3.jpg"))

    def initDialog(self):
        self.label.setPixmap(QPixmap("ui/Template/FG-Circle_1.jpg"))
        self.fy_inputlineEdit.setText(str(345))
        self.eu_inputlineEdit.setText(str(0.15))
        self.G_inputlineEdit.setText(str(0.3))
        # Set validator
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        intValidator = QIntValidator()
        self.k_inputlineEdit.setValidator(doubleValidator)
        self.Ei_inputlineEdit.setValidator(doubleValidator)
        self.E0_inputlineEdit.setValidator(doubleValidator)
        self.G_inputlineEdit.setValidator(doubleValidator)
        self.fy_inputlineEdit.setValidator(doubleValidator)
        self.eu_inputlineEdit.setValidator(doubleValidator)

        self.Ri_inputlineEdit.setValidator(doubleValidator)
        self.R0_inputlineEdit.setValidator(doubleValidator)
        self.Num_inputlineEdit.setValidator(intValidator)

        self.Ri_inputlineEdit.setText(str(400))
        self.R0_inputlineEdit.setText(str(800))
        self.Num_inputlineEdit.setText(str(int(10)))
        self.Ei_inputlineEdit.setText(str(205000))
        self.E0_inputlineEdit.setText(str(70000))
        self.k_inputlineEdit.setText(str(0.8))

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.method = 0

    @Slot()
    def on_Outline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.method = 1

    @Slot()
    def on_OK_button_clicked(self):
        """
        Slot documentation goes here.
        """
        Stress_input = 0
        num = 50
        try:
            if len(self.Ei_inputlineEdit.text()) == 0 or len(self.E0_inputlineEdit.text()) == 0 or\
               len(self.G_inputlineEdit.text()) == 0 or len(self.fy_inputlineEdit.text()) == 0 or\
               len(self.eu_inputlineEdit.text()) == 0 or len(self.Ri_inputlineEdit.text()) == 0 or\
               len(self.R0_inputlineEdit.text()) == 0 or len(self.Num_inputlineEdit.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
                msaModel.ResetAll()
                msaModel.Mat.Reset()
                msaModel.Point.Reset()
                msaModel.Segment.Reset()
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
                Ri = float(self.Ri_inputlineEdit.text())
                R0 = float(self.R0_inputlineEdit.text())
                StripNum = int(self.Num_inputlineEdit.text())
                MatIdDict = msaFEModel.Mat.ID
                if Ei < 0 or E0 < 0 or k < 0 or tμ < 0 or tfy < 0 or teu < 0 or Ri >= R0 or Ri < 0 or R0 < 0 or StripNum < 2:
                    showMesbox(self, 'Please input correct data!')
                else:
                    values = [int(i * 255 / StripNum) for i in range(StripNum)]
                    colors = ["#%02x%02x%02x" % (int(g), 255, 255) for g in values]
                    if len(MatIdDict) != 0:
                        id = max(MatIdDict)
                    else:
                        id = 0
                    va = [float(i + 0.5) for i in range(StripNum)]
                    if self.Law == 1:
                        E = [round(Ei + (E0 - Ei) * (n / StripNum) ** k, 3) for n in va]
                    elif self.Law == 2:
                        E = [round(Ei * np.exp(np.log(E0 / Ei) * (n / StripNum)), 3) for n in va]
                    elif self.Law == 3:
                        if StripNum % 2 == 0:
                            StripNum += 0
                        else:
                            StripNum += 1
                        colors = []
                        E = []
                        values = [int(i * 250 / (StripNum / 2)) for i in range(int(StripNum / 2))]
                        E1 = [round(Ei + (E0 - Ei) * (n / StripNum) ** k, 3) for n in va]
                        E2 = [round(E0 + (Ei - E0) * (1 - n / StripNum) ** k, 3) for n in va]
                        color1 = ["#%02x%02x%02x" % (int(g), 255, 255) for g in values]
                        color2 = ["#%02x%02x%02x" % (255 - int(g), 255, 255) for g in values]
                        for i in range(int(StripNum / 2)):
                            E.append(E1[i])
                            colors.append(color1[i])
                        for i in range(int(StripNum / 2)):
                            E.append(E2[int(StripNum / 2 - i)])
                            colors.append(color2[i])
                    for i in range(StripNum):
                        msaFEModel.Mat.Add(tID=id + i + 1, tE=E[i], tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,
                                           tType='S', tColor=colors[i])
                    self.accept()
                    if Ri != 0:
                        Rva = [float(i / (StripNum) * (R0 - Ri) + Ri) for i in range(StripNum + 1)]
                        for ii in range(len(Rva) - 1):
                            theta = 0
                            for i in range(num):
                                msaFEModel.Point.Add(tID=i + 1 + 2 * ii * num,
                                                     ty=np.around(Rva[ii] * np.cos(theta), decimals=3),
                                                     tz=np.around(Rva[ii] * np.sin(theta), decimals=3))
                                theta += 2 * np.pi / (num)
                            theta = 0
                            for i in range(num):
                                msaFEModel.Point.Add(tID=i + 1 + (1 + 2 * ii) * num,
                                                     ty=np.around(Rva[ii + 1] * np.cos(theta), decimals=3),
                                                     tz=np.around(Rva[ii + 1] * np.sin(theta), decimals=3))
                                theta += 2 * np.pi / (num)
                            for i in range(num - 1):
                                msaFEModel.Outline.Add(tID=i + 1 + (2 * ii) * num, tGID=1 + ii, tType="S",
                                                       tLID=1 + 2 * ii, tPSID=i + 1 + (2 * ii) * num,
                                                       tPEID=i + 2 + (2 * ii) * num)
                            msaFEModel.Outline.Add(tID=num + (2 * ii) * num, tGID=1 + ii, tType="S", tLID=1 + 2 * ii,
                                                   tPSID=num + (2 * ii) * num, tPEID=1 + (2 * ii) * num)
                            for i in range(num - 1):
                                msaFEModel.Outline.Add(tID=i + 1 + (1 + 2 * ii) * num, tGID=1 + ii, tType="O",
                                                       tLID=2 + 2 * ii, tPSID=i + 1 + (1 + 2 * ii) * num,
                                                       tPEID=i + 2 + (1 + 2 * ii) * num)
                            msaFEModel.Outline.Add(tID=num + (1 + 2 * ii) * num, tGID=1 + ii, tType="O",
                                                   tLID=2 + 2 * ii, tPSID=num + (1 + 2 * ii) * num,
                                                   tPEID=1 + + (1 + 2 * ii) * num)
                            tOID = []
                        for ii in range(2 * len(Rva) - 2):
                            ID = []
                            for i in range(num):
                                ID.append(int(i + 1 + ii * num))
                            tOID.append(ID)
                        for ii in range(len(tOID)):
                            msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                        for i in range(int(len(tOID) / 2)):
                            msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[2 * i + 1, 2 * i + 2])
                        # tOID1 = []
                        # for ii in range(num):
                        #     tOID1.append(ii + 1)
                        # msaFEModel.Loop.Add(tID=1, tOID=tOID1)
                        # msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1])
                    elif Ri == 0:
                        Rva = [float(i / (StripNum) * (R0 - Ri) + Ri) for i in range(StripNum + 1)]
                        Rva.reverse()
                        for ii in range(len(Rva) - 2):
                            theta = 0
                            for i in range(num):
                                msaFEModel.Point.Add(tID=i + 1 + 2 * ii * num,
                                                     ty=np.around(Rva[ii] * np.cos(theta), decimals=3),
                                                     tz=np.around(Rva[ii] * np.sin(theta), decimals=3))
                                theta += 2 * np.pi / (num)
                            theta = 0
                            for i in range(num):
                                msaFEModel.Point.Add(tID=i + 1 + (1 + 2 * ii) * num,
                                                     ty=np.around(Rva[ii + 1] * np.cos(theta), decimals=3),
                                                     tz=np.around(Rva[ii + 1] * np.sin(theta), decimals=3))
                                theta += 2 * np.pi / (num)
                            for i in range(num - 1):
                                msaFEModel.Outline.Add(tID=i + 1 + (2 * ii) * num, tGID=1 + ii, tType="S",
                                                       tLID=1 + 2 * ii, tPSID=i + 1 + (2 * ii) * num,
                                                       tPEID=i + 2 + (2 * ii) * num)
                            msaFEModel.Outline.Add(tID=num + (2 * ii) * num, tGID=1 + ii, tType="S", tLID=1 + 2 * ii,
                                                   tPSID=num + (2 * ii) * num, tPEID=1 + (2 * ii) * num)
                            for i in range(num - 1):
                                msaFEModel.Outline.Add(tID=i + 1 + (1 + 2 * ii) * num, tGID=1 + ii, tType="S",
                                                       tLID=2 + 2 * ii, tPSID=i + 1 + (1 + 2 * ii) * num,
                                                       tPEID=i + 2 + (1 + 2 * ii) * num)
                            msaFEModel.Outline.Add(tID=num + (1 + 2 * ii) * num, tGID=1 + ii, tType="S",
                                                   tLID=2 + 2 * ii, tPSID=num + (1 + 2 * ii) * num,
                                                   tPEID=1 + + (1 + 2 * ii) * num)
                        theta = 0
                        for i in range(num):
                            msaFEModel.Point.Add(tID=i + 1 + 2 * (len(Rva) - 2) * num,
                                                 ty=np.around(Rva[(len(Rva) - 2)] * np.cos(theta), decimals=3),
                                                 tz=np.around(Rva[(len(Rva) - 2)] * np.sin(theta), decimals=3))
                            theta += 2 * np.pi / (num)
                        for i in range(num - 1):
                            msaFEModel.Outline.Add(tID=i + 1 + (2 * (len(Rva) - 2)) * num, tGID=1 + (len(Rva) - 2),
                                                   tType="S", tLID=1 + 2 * (len(Rva) - 2),
                                                   tPSID=i + 1 + (2 * (len(Rva) - 2)) * num,
                                                   tPEID=i + 2 + (2 * (len(Rva) - 2)) * num)
                        msaFEModel.Outline.Add(tID=num + (2 * (len(Rva) - 2)) * num, tGID=1 + (len(Rva) - 2), tType="S",
                                               tLID=1 + 2 * (len(Rva) - 2), tPSID=num + (2 * (len(Rva) - 2)) * num,
                                               tPEID=1 + (2 * (len(Rva) - 2)) * num)
                        tOID = []
                        for ii in range(2 * len(Rva) - 3):
                            ID = []
                            for i in range(num):
                                ID.append(int(i + 1 + ii * num))
                            tOID.append(ID)
                        for ii in range(len(tOID)):
                            msaFEModel.Loop.Add(tID=1 + ii, tOID=tOID[ii])
                        for i in range(StripNum - 1):
                            msaFEModel.Group.Add(tID=1 + i, tMID=id + 1 + i, tLID=[2 * i + 1, 2 * i + 2])
                        msaFEModel.Group.Add(tID=StripNum, tMID=StripNum + id, tLID=[2 * StripNum - 1])
                    a = msaFEModel
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
