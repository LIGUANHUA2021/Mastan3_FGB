# -*- coding: utf-8 -*-

"""
Module implementing OutlineModify_Dialog.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator, QIntValidator
from gui.msasect.ui.Ui_OutlineModify import Ui_OutlineModify_Dialog
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.base.Model import msaFEModel
from gui.msasect.ui.Ui_OutlineModifyL import Ui_OutlineModify_Dialog
import traceback

class OutlineModify_Dialog(QDialog, Ui_OutlineModify_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, mw, idG,idL, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(OutlineModify_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Edit Outline")
        self.id = idG
        self.idL=idL
        self.mw = mw
        self.method = 0
        self.initDialog()
        currentRow = self.mw.SegmenttableWidget.currentRow()
        SO = str(self.mw.SegmenttableWidget.item(currentRow, 3).text())
        if SO=='Solid':
            self.Opening_radioButton.setEnabled(False)
            self.Solid_radioButton.setChecked(True)
            self.method = 0
        elif SO=='Opening':
            self.Solid_radioButton.setEnabled(False)
            self.Opening_radioButton.setChecked(True)
            self.method = 1
        self.getOutlineInfo(idG,idL)

    def initDialog(self):
        self.GroupID_lineEdit.setEnabled(False)
        self.LoopID_lineEdit.setEnabled(False)
        self.MatID_lineEdit.setEnabled(False)
        self.GroupID_lineEdit.setStyleSheet("*{    \n"
                                      "    font: 9pt \"Segoe UI\";\n"
                                      "    color: rgb(128, 128, 128);\n"
                                      "    background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        self.LoopID_lineEdit.setStyleSheet("*{    \n"
                                      "    font: 9pt \"Segoe UI\";\n"
                                      "    color: rgb(128, 128, 128);\n"
                                      "    background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        self.MatID_lineEdit.setStyleSheet("*{    \n"
                                      "    font: 9pt \"Segoe UI\";\n"
                                      "    color: rgb(128, 128, 128);\n"
                                      "    background: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "")
        #设置validator
        doubleValidator = QDoubleValidator(bottom=-999, top=999)
        intValidator = QIntValidator()
        self.Points_lineEdit.text()


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
            if len(self.MatID_lineEdit.text()) == 0 or len(self.Points_lineEdit.text()) == 0  :
                showMesbox(self, 'Please input correct data!')
            else:
                pre_LoopID=self.idL
                pre_OUT = msaFEModel.Loop.OutlineID[pre_LoopID]
                PointsDict=msaFEModel.Point.ID
                GroupID = int(self.GroupID_lineEdit.text())
                LoopID = int(self.LoopID_lineEdit.text())
                MatID = int(self.MatID_lineEdit.text())
                Points = str(self.Points_lineEdit.text())
                Points = list(Points.split(","))
                Points = list(map(int, Points))
                set_Points = set(Points)
                for i in range(len(Points)):
                    if not Points[i] in PointsDict:
                        showMesbox(self, 'Point ID %s does not exist!' % (Points[i]))
                if len(Points)<3:
                    showMesbox(self, 'Please input correct points!')
                elif len(set_Points)!=len(Points):
                    showMesbox(self, 'Point ID is repeated in the outline!')
                else:
                    if not self.method:
                        Type='S'
                    else:
                        Type='O'
                    Lenpoints=len(Points)
                    for i in range (len(pre_OUT)):
                        msaFEModel.Outline.Remove(int(pre_OUT[i]))#Delet all the outlines in current loop
                    outlineID = len(msaFEModel.Outline.ID)
                    for i in range(Lenpoints - 1):
                        msaFEModel.Outline.Add(tID=i + outlineID + 1, tGID=GroupID, tType=Type, tLID=LoopID,
                                               tPSID=Points[i], tPEID=Points[i + 1])
                    msaFEModel.Outline.Add(tID=Lenpoints + outlineID, tGID=GroupID, tType=Type, tLID=LoopID,
                                           tPSID=Points[Lenpoints - 1], tPEID=Points[0]) #Add new outlines
                    outlineID_current=[]
                    for i in range(Lenpoints):
                        outlineID_current.append(i + outlineID + 1)
                    msaFEModel.Loop.OutlineID[LoopID] = outlineID_current#Modify outlineIDs in current loop
                    msaFEModel.Loop.PointID[LoopID]=Points
            self.mw.ResetTable()
            self.mw.View.autoRange()
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
        #raise NotImplementedError
        QDialog.close(self)

    def getOutlineInfo(self, idG,idL):
        self.GroupID_lineEdit.setText(str(idG))
        self.LoopID_lineEdit.setText(str(idL))
        self.MatID_lineEdit.setText(str(int(msaFEModel.Group.MatID[idG])))
        Loop = []
        Point = msaFEModel.Loop.PointID[idL]
        Loop.append(Point[0])
        for ii in range(len(Point) - 1):
            Loop.append(Point[len(Point) - 1 - ii])
        Outlines=[]
        Points=''
        for i in range(len(Loop)):
            Outlines.append(Loop[i])
        Points += str(Outlines[0])
        for i in range(int(len(Outlines)-1)):
            Points+=','
            Points+=str(Outlines[i+1])
        self.Points_lineEdit.setText(str(Points))