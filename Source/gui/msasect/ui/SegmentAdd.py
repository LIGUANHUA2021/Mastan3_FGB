# -*- coding: utf-8 -*-

"""
Module implementing SegmentAdd_Dialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator, QRegularExpressionValidator
from PySide6.QtGui import QIntValidator
import traceback

from gui.msasect.base.Model import msaModel
from gui.msasect.ui.Ui_SegmentAdd import Ui_SegmentAdd_Dialog
from gui.msasect.ui.msgBox import showMesbox

class SegmentAddDialog(QDialog, Ui_SegmentAdd_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, mw, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height()) ### Fix the size of window
        self.mw = mw
        self.initDialog()
    def initDialog(self):
        try:
            # self.PointIDInput.setEnabled(False)
            SegmentIDDict=msaModel.Segment.ID
            if not SegmentIDDict:
                AddId = 1
            else:
                maxId = max(SegmentIDDict.keys(), key=(lambda x:x))
                AddId = maxId + 1
            self.SegIDInput.setText(str(int(AddId)))
            ###设置validator
            doubleValidator = QDoubleValidator(bottom=-999, top=999)
            intValidator = QIntValidator()
            self.SegIDInput.setValidator(intValidator)
            self.PointSID_Input.setValidator(intValidator)
            self.PointEID_Input.setValidator(intValidator)
            #self.Thk_Input.setValidator(doubleValidator)
            self.Thk_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
            self.MatID_Input.setValidator(intValidator)
        except:
            traceback.print_exc()

    @Slot()
    def on_SegmentAdd_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            if len(self.PointSID_Input.text()) == 0 or len(self.PointEID_Input.text()) == 0 or len(
                    self.Thk_Input.text()) == 0 \
                    or len(self.MatID_Input.text()) == 0:
                showMesbox(self, 'Please input correct data!')
                return

            PointSID_Input = int(self.PointSID_Input.text())
            PointEID_Input = int(self.PointEID_Input.text())
            if PointSID_Input == PointEID_Input:
                showMesbox(self, 'The start point is same as end point, please check your input!')
                return

            # if (PointSID_Input in msaModel.Segment.PointI and PointEID_Input in msaModel.Segment.PointJ):
            #     showMesbox(self, 'This segment has been created already, please check your input!')
            #     return
            #
            MatID_Input = int(self.MatID_Input.text())
            #
            if (not msaModel.Point.ID or not msaModel.Mat.ID):
                showMesbox(self, "Please input the Point or Material information firstly")
                return
            if (msaModel.CheckID(PointSID_Input, msaModel.Point.ID) == 0 or msaModel.CheckID(PointEID_Input, msaModel.Point.ID) == 0):
                showMesbox(self, 'Please input the exists point ID.')
                return
            if msaModel.CheckID(MatID_Input, msaModel.Mat.ID) == 0:
                showMesbox(self, "Please input the exists Material ID")
                return
            #
            Thk_Input = float(self.Thk_Input.text())
            id = int(self.SegIDInput.text())
            #
            if Thk_Input < 0.0001:
                showMesbox(self, "Please check your input, the thickness of segment is toooo small!")
                return
            #
            SegmentIDDict = msaModel.Segment.ID
            if id in SegmentIDDict:
                showMesbox(self, 'Segment ID has been used!')
            else:
                msaModel.Segment.Add(tID=id, tMaterialID=MatID_Input, tPSID=PointSID_Input, tPEID=PointEID_Input,
                                     tSegThick=Thk_Input)
                self.mw.ResetTable()
                self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

    @Slot()
    def on_SegAddCancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)
