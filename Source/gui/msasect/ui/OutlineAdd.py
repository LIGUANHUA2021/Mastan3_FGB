# -*- coding: utf-8 -*-

"""
Module implementing OutlineAdd_Dialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator, QIntValidator
from gui.msasect.ui.Ui_OutlineAdd import Ui_OutlineAdd_Dialog
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.base.Model import msaFEModel
import traceback

class OutlineAdd_Dialog(QDialog, Ui_OutlineAdd_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self,mw,parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        self.method = 0
        super().__init__(parent)
        self.setupUi(self)
        self.mw = mw
        self.initDialog()
        self.Solid_radioButton.setChecked(True)

    def initDialog(self):
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        intValidator = QIntValidator()
        self.GroupID_lineEdit.setValidator(intValidator)
        self.LoopID_lineEdit.setValidator(intValidator)
        self.MatID_lineEdit.setValidator(intValidator)
        self.Points_lineEdit.text()
        LoopIdDictol = msaFEModel.Loop.ID
        if not LoopIdDictol:
            AddId = 1
        else:
            maxId = max(LoopIdDictol.keys(), key=(lambda x: x))
            AddId = maxId + 1
        print(AddId)
        self.LoopID_lineEdit.setText(str(int(AddId)))

    @Slot()
    def on_Solid_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.method = 0

    @Slot()
    def on_Opening_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.method = 1

    @Slot()
    def on_OutlineAdd_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        try:
            if len(self.GroupID_lineEdit.text()) == 0 or len(self.LoopID_lineEdit.text()) == 0 or len(
                    self.MatID_lineEdit.text()) == 0 or len(self.Points_lineEdit.text()) == 0:
                showMesbox(self, 'Please input correct data!')
            else:
                GroupID = int(self.GroupID_lineEdit.text())
                LoopID = int(self.LoopID_lineEdit.text())
                MatID = int(self.MatID_lineEdit.text())
                if not self.method:
                    Type = "S"
                else:
                    Type = "O"
                Points = str(self.Points_lineEdit.text())
                Points =list(Points.split(","))
                Points=list(map(int, Points))
                MatIdDict = msaFEModel.Mat.ID
                LoopIDDict = msaFEModel.Loop.ID
                PointsDict=msaFEModel.Point.ID
                outlineID=len(msaFEModel.Outline.ID)
                set_Points = set(Points)
                if not MatID in MatIdDict:
                    showMesbox(self, 'Material ID does not exist!')
                elif LoopID in LoopIDDict:
                    showMesbox(self, 'Loop ID has been used!')
                    for i in range(len(Points)):
                        if not Points[i] in PointsDict:
                            showMesbox(self, 'Point ID %s does not exist!' % (Points[i]))
                elif len(Points) < 3:
                    showMesbox(self, 'Please input correct points!')
                elif len(set_Points)!=len(Points):
                    showMesbox(self, 'Point ID is repeated in the outline!')
                else:
                    Lenpoints=len(Points)
                    for i in range(Lenpoints-1):
                        msaFEModel.Outline.Add(tID=i + outlineID + 1, tGID=GroupID, tType=Type, tLID=LoopID,
                                               tPSID=Points[i], tPEID=Points[i + 1])
                    msaFEModel.Outline.Add(tID=Lenpoints + outlineID, tGID=GroupID, tType=Type, tLID=LoopID,
                                           tPSID=Points[Lenpoints - 1], tPEID=Points[0])
                    outline = []
                    for i in range(Lenpoints):
                        outline.append(int(i+outlineID+1))
                    msaFEModel.Loop.Add(tID=LoopID, tOID=outline)
                    if GroupID not in msaFEModel.Group.ID:
                        msaFEModel.Group.Add(tID=GroupID, tMID=MatID, tLID=[LoopID])
                    else:
                        msaFEModel.Group.LoopID[GroupID].append(LoopID)
            self.mw.ResetTable()
            self.mw.View.autoRange()
            self.mw.setWindowTitle(
                'MASTAN2 - Matrix Structural Analysis for Arbitrary Cross-sections - '
            )
            msaFEModel.FileInfo.FileName = ""
            self.accept()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

    @Slot()
    def on_OutlineAddCancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)
