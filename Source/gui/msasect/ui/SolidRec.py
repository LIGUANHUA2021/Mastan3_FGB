# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
import numpy as np
from gui.msasect.ui.Ui_SolidRec import Ui_SolidRec_Dialog
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor, QDoubleValidator, QIntValidator, QPixmap, QIcon
import traceback
from gui.msasect.base.Model import msaModel,msaFEModel, Status, GlobalBuckling
from gui.msasect.ui.msgBox import showMesbox
from analysis.CMSect.variables.Model import SectProperty
from analysis.FESect.variables.Result import SectionProperties
from analysis.CMSect.variables.Model import YieldSAnalResults as CMYieldSAnalResults
from analysis.FESect.variables.Model import YieldSAnalResults as FEYieldSAnalResults


class SolidRec_Dialog(QDialog, Ui_SolidRec_Dialog):
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
        Methodsignal = Signal(int)
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/Solid Rec.ico'))
        self.color = '#aaffff'
        self.ColorButton.clicked.connect(self.ShowColorDialog)
        # self.showImage()
        self.mw = mw
        self.initDialog()
        self.Centerline_radioButton.setEnabled(False)
        self.Outline_radioButton.setChecked(True)
        self.method = 1


    def initDialog(self):
        self.label.setPixmap(QPixmap("ui/Template/Solid Rec.jpg"))
        # MatIdDict = msaModel.Mat.ID
        # if not MatIdDict:
        #     AddId = 1
        # else:
        #     maxId = max(MatIdDict.keys(), key=(lambda x:x))
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
        self.G_inputlineEdit.setValidator(doubleValidator)
        self.fy_inputlineEdit.setValidator(doubleValidator)
        self.eu_inputlineEdit.setValidator(doubleValidator)

        self.B_inputlineEdit.setValidator(doubleValidator)
        self.D_inputlineEdit.setValidator(doubleValidator)

        self.B_inputlineEdit.setText(str(800))
        self.D_inputlineEdit.setText(str(500))

    @Slot()
    def on_Centerline_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
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
                    self.fy_inputlineEdit.text()) == 0 or len(self.B_inputlineEdit.text()) == 0 or len(self.D_inputlineEdit.text()) == 0 :
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
                tE = float(self.E_inputlineEdit.text())
                tμ = float(self.G_inputlineEdit.text())
                tfy = float(self.fy_inputlineEdit.text())
                id = int(self.ID_inputlineEdit.text())
                teu = float(self.eu_inputlineEdit.text())
                B = float(self.B_inputlineEdit.text())
                D = float(self.D_inputlineEdit.text())
                if B<0 or D<0 or tE<0 or tμ<0 or tfy<0 or teu<0:
                    showMesbox(self, 'Please input correct data!')
                else:
                    MatIdDict = msaFEModel.Mat.ID
                    if id in MatIdDict:
                        showMesbox(self, 'Material ID has been used!')
                    else:
                        msaFEModel.Mat.Add(tID=id, tE=tE, tnu=tμ, tFy=tfy, tDensity=999999, teu=teu,tType='C', tColor=self.color)
                        self.accept()
                        B = float(self.B_inputlineEdit.text())
                        D = float(self.D_inputlineEdit.text())
                        msaFEModel.Point.Add(tID=1, ty=0, tz=0)
                        msaFEModel.Point.Add(tID=2, ty=0, tz=B)
                        msaFEModel.Point.Add(tID=3, ty=-D, tz=B)
                        msaFEModel.Point.Add(tID=4, ty=-D, tz=0)
                        msaFEModel.Outline.Add(tID=1, tGID=1, tType="S", tLID=1, tPSID=1, tPEID=2)
                        msaFEModel.Outline.Add(tID=2, tGID=1, tType="S", tLID=1, tPSID=2, tPEID=3)
                        msaFEModel.Outline.Add(tID=3, tGID=1, tType="S", tLID=1, tPSID=3, tPEID=4)
                        msaFEModel.Outline.Add(tID=4, tGID=1, tType="S", tLID=1, tPSID=4, tPEID=1)
                        msaFEModel.Loop.Add(tID=1, tOID=[1, 2, 3, 4])
                        msaFEModel.Group.Add(tID=1, tMID=id, tLID=[1])
                        self.mw.ResetTable()
                        self.mw.View.autoRange()
                        self.mw.setWindowTitle(
                            'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections'
                        )
                        msaModel.FileInfo.FileName = ""
                        Status.Reset()
                        self.mw.SectIDInput_lineEdit.setText('SolidRec01')
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


