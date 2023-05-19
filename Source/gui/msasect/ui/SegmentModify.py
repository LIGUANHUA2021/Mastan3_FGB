# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import traceback

from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QDialog, QApplication

from gui.mastan.ui.Ui_MemInput import Ui_Dialog
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.base.Model import msaModel
from gui.msasect.ui.Ui_SegmentAdd import Ui_SegmentAdd_Dialog

class SegmentModifyDialog(QDialog, Ui_SegmentAdd_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, mw, id, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(SegmentModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Edit Segment")
        self.id = id
        self.mw = mw
        self.initDialog()
        self.getSegmentInfo(id)

    #初始化窗口设置
    def initDialog(self):
        self.SegIDInput.setEnabled(False)
        self.SegIDInput.setStyleSheet("*{    \n"
                                      "    font: 9pt \"Segoe UI\";\n"
                                      "    color: rgb(128, 128, 128);\n"
                                      "    background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        #设置validator
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        intValidator = QIntValidator()
        self.SegIDInput.setValidator(intValidator)
        self.PointSID_Input.setValidator(intValidator)
        self.PointEID_Input.setValidator(intValidator)
        self.Thk_Input.setValidator(QRegularExpressionValidator("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"))
        #self.Thk_Input.setValidator(doubleValidator)

        self.MatID_Input.setValidator(intValidator)

    def getSegmentInfo(self, id):
        self.SegIDInput.setText(str(id))
        self.PointSID_Input.setText(str(int(msaModel.Segment.PointI[id])))
        self.PointEID_Input.setText(str(int(msaModel.Segment.PointJ[id])))
        self.Thk_Input.setText(str(msaModel.Segment.SegThick[id]))
        self.MatID_Input.setText(str(int(msaModel.Segment.MatID[id])))

    @Slot()
    def on_SegmentAdd_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            PointIDList = msaModel.Point.ID
            MaterialIdList = msaModel.Mat.ID
            SegID = int(self.SegIDInput.text())
            PointSID = int(self.PointSID_Input.text())
            PointEID = int(self.PointEID_Input.text())
            MatID = int(self.MatID_Input.text())
            SegThick = float(self.Thk_Input.text())
            #
            if PointSID == PointEID:
                showMesbox(self, 'The start point is same as end point, please check your modify!')
                return
            #
            if PointSID not in PointIDList:
                showMesbox(self, 'Node I is not existed!')
            elif PointEID not in PointIDList:
                showMesbox(self, 'Node J is not existed!')
            elif MatID not in MaterialIdList:
                showMesbox(self, 'Material is not existed!')
            else:
                if SegThick < 0.0001:
                    showMesbox(self, 'Please check your input, the thickness of segment is toooo small!')
                    return
                msaModel.Segment.Modify(SegID, MatID, PointSID, PointEID, SegThick)
                self.mw.ResetTable()
                self.accept()
        except:
            traceback.print_exc()
    @Slot()
    def on_SegAddCancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     ui = MemberDialog()
#     ui.show()
#     sys.exit(app.exec())