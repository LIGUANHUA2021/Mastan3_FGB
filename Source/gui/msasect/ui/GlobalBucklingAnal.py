# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot,Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon,QPixmap
import numpy as np
from gui.msasect.ui.Ui_AnalGlobalBuckling import Ui_GlobalBucklingAnal_Dialog
from analysis.FESect.variables.Result import SectionProperties as FESp
from analysis.FESect.variables.Model import Material as FEMat
from analysis.CMSect.variables.Model import SectProperty as CMSp
from analysis.CMSect.variables.Model import Material as CMMat
from analysis.FESect.variables.Model import Analysis as FEAnalysis
from analysis.GlobalBuckling.variables import Model as GlobalBucklingmodel
from analysis.GlobalBuckling.solver import GlobalBucklingCal as GlobalBucklingCal
from gui.msasect.base import Model as msaModel
import traceback
from gui.msasect.ui.ShowResultsBuckling import GlobalBucklingPlot_Dialog
from gui.msasect.ui.ShowResultsBuckling_Element import GlobalBuckling_Element_Plot_Dialog
from gui.msasect.ui.msgBox import showMesbox
from gui.msasect.ui.CalGlobalBuckling_Element import MultiThread
from gui.msasect.ui.GBAnalMessageBox import GBAnalMessageBox_Dialog

class GlobalBucklingAnal_Dialog(QDialog, Ui_GlobalBucklingAnal_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/GlobalBuckling.png'))
        # self.Picture_label.setPixmap(QPixmap("ui/Template/Buckling_line1.png"))
        self.mw = mw
        self.Nodes_number = 11
        self.Calculate_method = 0
        self.Axial_method = 0
        self.MaterialCapacity = 2
        self.Bending_method = 0
        self.sleder_min = 0
        self.sleder_max = 0
        self.sleder_steps = 0
        self.initDialog()
        self.MinSlenderRatio_lineEdit.textChanged.connect(self.on_changed)
        self.MaxSlenderRatio_lineEdit.textChanged.connect(self.on_changed)
        self.SlenderRatioSteps_lineEdit.textChanged.connect(self.on_changed)
        self.ElementNumber_lineEdit.textChanged.connect(self.on_changed)
        self.BendingMajor_radioButton.toggled.connect(self.on_changed)
        self.BendingMinor_radioButton.toggled.connect(self.on_changed)
        self.AnalyticalExpression_radioButton.toggled.connect(self.on_changed)
        self.LineElement_radioButton.toggled.connect(self.on_changed)
        self.GeoAxis_radioButton.toggled.connect(self.on_changed)
        self.PrinAxis_radioButton.toggled.connect(self.on_changed)
        self.Px_lineEdit.textChanged.connect(self.on_changed)
        # self.Mx_lineEdit.textChanged.connect(self.on_changed)
        self.My_lineEdit.textChanged.connect(self.on_changed)
        self.Mz_lineEdit.textChanged.connect(self.on_changed)
        self.Elastic_radioButton.toggled.connect(self.on_changed)
        self.Plastic_radioButton.toggled.connect(self.on_changed)
        self.Ignore_radioButton.toggled.connect(self.on_changed)
        self.My_label.setText('Moment (My) :')
        self.Mz_label.setText('Moment (Mz) :')

    def initDialog (self):
        if msaModel.GlobalBuckling.Buckling_data:
            self.ShowResults_pushButton.setEnabled(True)
            self.ShowResults_pushButton.setStyleSheet("*{    \n"
                                             "    font: 9pt \"Segoe UI\";\n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "    background: rgb(255, 255, 255);\n"
                                             "}\n"
                                             "")
        else:
            self.ShowResults_pushButton.setEnabled(False)
            self.ShowResults_pushButton.setStyleSheet("*{    \n"
                                            "    font: 9pt \"Segoe UI\";\n"
                                            "    color: rgb(128, 128, 128);\n"
                                            "    background: rgb(240, 240, 240);\n"
                                            "}\n"
                                            "")
        self.AnalyticalExpression_radioButton.setChecked(True)
        self.PrinAxis_radioButton.setChecked(True)
        self.BendingMajor_radioButton.setChecked(True)
        self.MinSlenderRatio_lineEdit.setText(str(20))
        self.MaxSlenderRatio_lineEdit.setText(str(200))
        self.SlenderRatioSteps_lineEdit.setText(str(50))
        self.ElementNumber_lineEdit.setText(str(20))
        self.Px_lineEdit.setText(str(1))
        # self.Mx_lineEdit.setText(str(0))
        self.My_lineEdit.setText(str(0))
        self.Mz_lineEdit.setText(str(0))
        self.Ignore_radioButton.setChecked(True)
        self.Px_lineEdit.setEnabled(False)
        # self.Mx_lineEdit.setEnabled(False)
        self.My_lineEdit.setEnabled(False)
        self.Mz_lineEdit.setEnabled(False)
        self.ElementNumber_lineEdit.setEnabled(False)
        self.MaterialCapacity = 2
        self.Px_label.setStyleSheet("*{    \n"
                                        "    color: rgb(80, 80, 80);\n"
                                        "}\n"
                                        "")
        self.Px_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                        "    background: rgb(160, 160, 160);\n"
                                        "}\n"
                                        "")
        # self.Mx_label.setStyleSheet("*{    \n"
        #                             "    color: rgb(80, 80, 80);\n"
        #                             "}\n"
        #                             "")
        # self.Mx_lineEdit.setStyleSheet("*{    \n"
        #                                "    color: rgb(0, 0, 0);\n"
        #                                "    background: rgb(160, 160, 160);\n"
        #                                "}\n"
        #                                "")
        self.My_label.setStyleSheet("*{    \n"
                                    "    color: rgb(80, 80, 80);\n"
                                    "}\n"
                                    "")
        self.My_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(160, 160, 160);\n"
                                       "}\n"
                                       "")
        self.Mz_label.setStyleSheet("*{    \n"
                                    "    color: rgb(80, 80, 80);\n"
                                    "}\n"
                                    "")
        self.Mz_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(160, 160, 160);\n"
                                       "}\n"
                                       "")
        self.ElementNumber_label.setStyleSheet("*{    \n"
                                    "    color: rgb(80, 80, 80);\n"
                                    "}\n"
                                    "")
        self.ElementNumber_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(160, 160, 160);\n"
                                       "}\n"
                                       "")
        self.label.setStyleSheet("*{    \n"
                                               "    color: rgb(80, 80, 80);\n"
                                               "}\n"
                                               "")

    @Slot()
    def on_AnalyticalExpression_radioButton_clicked(self):
        self.Calculate_method = 0
        self.BendingMajor_radioButton.setEnabled(True)
        self.BendingMinor_radioButton.setEnabled(True)
        self.Px_lineEdit.setEnabled(False)
        self.My_lineEdit.setEnabled(False)
        self.Mz_lineEdit.setEnabled(False)
        self.ElementNumber_lineEdit.setEnabled(False)
        self.Px_label.setStyleSheet("*{    \n"
                                    "    color: rgb(80, 80, 80);\n"
                                    "}\n"
                                    "")
        self.Px_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(160, 160, 160);\n"
                                       "}\n"
                                       "")
        # self.Mx_label.setStyleSheet("*{    \n"
        #                             "    color: rgb(80, 80, 80);\n"
        #                             "}\n"
        #                             "")
        # self.Mx_lineEdit.setStyleSheet("*{    \n"
        #                                "    color: rgb(0, 0, 0);\n"
        #                                "    background: rgb(160, 160, 160);\n"
        #                                "}\n"
        #                                "")
        self.My_label.setStyleSheet("*{    \n"
                                    "    color: rgb(80, 80, 80);\n"
                                    "}\n"
                                    "")
        self.My_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(160, 160, 160);\n"
                                       "}\n"
                                       "")
        self.Mz_label.setStyleSheet("*{    \n"
                                    "    color: rgb(80, 80, 80);\n"
                                    "}\n"
                                    "")
        self.Mz_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(160, 160, 160);\n"
                                       "}\n"
                                       "")
        self.ElementNumber_label.setStyleSheet("*{    \n"
                                               "    color: rgb(80, 80, 80);\n"
                                               "}\n"
                                               "")
        self.ElementNumber_lineEdit.setStyleSheet("*{    \n"
                                                  "    color: rgb(0, 0, 0);\n"
                                                  "    background: rgb(160, 160, 160);\n"
                                                  "}\n"
                                                  "")
        self.label.setStyleSheet("*{    \n"
                                               "    color: rgb(80, 80, 80);\n"
                                               "}\n"
                                               "")

    @Slot()
    def on_LineElement_radioButton_clicked(self):
        self.Calculate_method = 1
        self.BendingMajor_radioButton.setEnabled(False)
        self.BendingMinor_radioButton.setEnabled(False)
        self.Px_lineEdit.setEnabled(True)
        self.My_lineEdit.setEnabled(True)
        self.Mz_lineEdit.setEnabled(True)
        self.ElementNumber_lineEdit.setEnabled(True)
        self.Px_label.setStyleSheet("*{    \n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "")
        self.Px_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "")
        # self.Mx_label.setStyleSheet("*{    \n"
        #                             "    color: rgb(255, 255, 255);\n"
        #                             "}\n"
        #                             "")
        # self.Mx_lineEdit.setStyleSheet("*{    \n"
        #                                "    color: rgb(0, 0, 0);\n"
        #                                "    background: rgb(255, 255, 255);\n"
        #                                "}\n"
        #                                "")
        self.My_label.setStyleSheet("*{    \n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "")
        self.My_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "")
        self.Mz_label.setStyleSheet("*{    \n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "")
        self.Mz_lineEdit.setStyleSheet("*{    \n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "")
        self.ElementNumber_label.setStyleSheet("*{    \n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "")
        self.ElementNumber_lineEdit.setStyleSheet("*{    \n"
                                                  "    color: rgb(0, 0, 0);\n"
                                                  "    background: rgb(255, 255, 255);\n"
                                                  "}\n"
                                                  "")
        self.label.setStyleSheet("*{    \n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "")

    @Slot()
    def on_PrinAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Axial_method = 0
        self.My_label.setText('Moment (Mv) :')
        self.Mz_label.setText('Moment (Mw) :')
        # self.Picture_label.setPixmap(QPixmap("ui/Template/Buckling_line_vw1.png"))

    @Slot()
    def on_GeoAxis_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Axial_method = 1
        self.My_label.setText('Moment (My) :')
        self.Mz_label.setText('Moment (Mz) :')
        # self.Picture_label.setPixmap(QPixmap("ui/Template/Buckling_line1.png"))

    @Slot()
    def on_BendingMajor_radioButton_clicked(self):
        """
                Slot documentation goes here.
                """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Bending_method = 0

    @Slot()
    def on_BendingMinor_radioButton_clicked(self):
        """
                Slot documentation goes here.
                """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Bending_method = 1

    @Slot()
    def on_Elastic_radioButton_clicked(self):
        """
                Slot documentation goes here.
                """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.MaterialCapacity = 0

    @Slot()
    def on_Plastic_radioButton_clicked(self):
        """
                Slot documentation goes here.
                """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.MaterialCapacity = 1

    @Slot()
    def on_Ignore_radioButton_clicked(self):
        """
                Slot documentation goes here.
                """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.MaterialCapacity = 2

    @Slot()
    def on_Run_pushButton_clicked(self):
        try:
            if not CMSp.Ivv and not FESp.Zv:
                showMesbox(self, 'Please create a model and calculate section properties first!')
                return
            # =========================================================================================
            # Calculate global buckling using analytical expressions
            # =========================================================================================
            if self.AnalyticalExpression_radioButton.isChecked():
                GlobalBucklingmodel.Material.Reset()
                GlobalBucklingmodel.SecProperties.Reset()
                GlobalBucklingmodel.Analysis.Reset()
                msaModel.GlobalBuckling.Reset()
                if float(self.MinSlenderRatio_lineEdit.text())>=float(self.MaxSlenderRatio_lineEdit.text()) or float(
                        self.MinSlenderRatio_lineEdit.text())<=0 or float(self.MaxSlenderRatio_lineEdit.text())<=0 or float(self.SlenderRatioSteps_lineEdit.text())<=0 or len(
                    self.MinSlenderRatio_lineEdit.text())==0 or len(self.MaxSlenderRatio_lineEdit.text())==0 or len(self.SlenderRatioSteps_lineEdit.text())==0 :
                    showMesbox(self, 'Please check the input of slender ratio!')
                    return
                GlobalBucklingmodel.Analysis.SlenderRatio_min = float(self.MinSlenderRatio_lineEdit.text())
                GlobalBucklingmodel.Analysis.SlenderRatio_max = float(self.MaxSlenderRatio_lineEdit.text())
                GlobalBucklingmodel.Analysis.SlenderRatio_steps = int(self.SlenderRatioSteps_lineEdit.text()) - 1
                Lamuda_method1 = []
                Lamuda_method2 = []
                Lamuda_method3 = []
                Lamuda_method4 = []
                Pfb1 = []
                Pfb2 = []
                Pfb3 = []
                Pfb4 = []
                Pfb5 = []
                Buckling_data = {}
                GlobalBucklingmodel.Analysis.TwistingEffects = 1
                if self.mw.Centerline_radioButton.isChecked() == True:
                    GlobalBucklingmodel.Material.E = float(list(CMMat.E.values())[0])
                    GlobalBucklingmodel.Material.mu = float(list(CMMat.nu.values())[0])
                    GlobalBucklingmodel.Material.Fy = float(list(CMMat.Fy.values())[0])
                    if self.Axial_method == 1:
                        GlobalBucklingmodel.SecProperties.Area = CMSp.Area
                        GlobalBucklingmodel.SecProperties.MomentofInertia_v = CMSp.Iyy
                        GlobalBucklingmodel.SecProperties.MomentofInertia_w = CMSp.Izz
                        GlobalBucklingmodel.SecProperties.TorsionConstant = CMSp.J
                        GlobalBucklingmodel.SecProperties.WarpingConstant = CMSp.Cw
                        GlobalBucklingmodel.SecProperties.ShearCentre_v = CMSp.ysc
                        GlobalBucklingmodel.SecProperties.ShearCentre_w = CMSp.zsc
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_v = CMSp.Betay
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_w = CMSp.Betaz
                        Svv = CMSp.Syy
                        Sww = CMSp.Szz
                        Zvv = CMSp.Zyy
                        Zww = CMSp.Zzz
                    elif self.Axial_method == 0:
                        GlobalBucklingmodel.SecProperties.Area = CMSp.Area
                        GlobalBucklingmodel.SecProperties.MomentofInertia_v = CMSp.Ivv
                        GlobalBucklingmodel.SecProperties.MomentofInertia_w = CMSp.Iww
                        GlobalBucklingmodel.SecProperties.TorsionConstant = CMSp.J
                        GlobalBucklingmodel.SecProperties.WarpingConstant = CMSp.Cw
                        GlobalBucklingmodel.SecProperties.ShearCentre_v = CMSp.vsc
                        GlobalBucklingmodel.SecProperties.ShearCentre_w = CMSp.wsc
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_v = CMSp.Betav
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_w = CMSp.Betaw
                        Svv = CMSp.Svv
                        Sww = CMSp.Sww
                        Zvv = CMSp.Zvv
                        Zww = CMSp.Zww
                    GlobalBucklingmodel.Analysis.FlexuralBuckling_Axis = "Major"
                    Lamuda_method1, Pfb1 = GlobalBucklingCal.CalFlexuralBuckling()
                    GlobalBucklingmodel.Analysis.FlexuralBuckling_Axis = "Minor"
                    Lamuda_method2, Pfb2 = GlobalBucklingCal.CalFlexuralBuckling()
                    GlobalBucklingmodel.Analysis.TwistingEffects = 1
                    Lamuda_method3, Pfb31 = GlobalBucklingCal.CalAxialtorsionalBuckling()
                    Pfb3.append(Pfb31)  # consider twisting effects
                    GlobalBucklingmodel.Analysis.TwistingEffects = 0
                    Lamuda_method3, Pfb32 = GlobalBucklingCal.CalAxialtorsionalBuckling()
                    Pfb3.append(Pfb32)  # ignore twisting effects
                    GlobalBucklingmodel.Analysis.TwistingEffects = 1
                    # lateral torsional buckling consider Twisting Effects
                    if self.Bending_method == 0:
                        GlobalBucklingmodel.Analysis.Lateraltorsional_Buckling_Axis = "Major"
                        msaModel.GlobalBuckling.Lateraltorsional_Buckling_Axis = "Major"
                        Lamuda_method4, Pfb4 = GlobalBucklingCal.CalLateraltorsionalBuckling()
                    elif self.Bending_method == 1:
                        GlobalBucklingmodel.Analysis.Lateraltorsional_Buckling_Axis = "Minor"
                        msaModel.GlobalBuckling.Lateraltorsional_Buckling_Axis = "Minor"
                        Lamuda_method4, Pfb4 = GlobalBucklingCal.CalLateraltorsionalBuckling()
                    GlobalBucklingmodel.Analysis.TwistingEffects = 0
                    Lamuda_method5, Pfb5 = GlobalBucklingCal.CalLateraltorsionalBuckling()
                    #print(GlobalBucklingmodel.Analysis.Lateraltorsional_Buckling_Axis)
                elif self.mw.Outline_radioButton.isChecked() == True:
                    ref_Mat = FEAnalysis.mat_ref
                    GlobalBucklingmodel.Material.E = FEMat.E[ref_Mat]
                    GlobalBucklingmodel.Material.mu = FEMat.nu[ref_Mat]
                    GlobalBucklingmodel.Material.eu = FEMat.eu[ref_Mat]
                    GlobalBucklingmodel.Material.Fy = FEMat.Fy[ref_Mat]
                    if self.Axial_method == 0:
                        GlobalBucklingmodel.SecProperties.Area = FESp.Area
                        GlobalBucklingmodel.SecProperties.MomentofInertia_v = FESp.Iv
                        GlobalBucklingmodel.SecProperties.MomentofInertia_w = FESp.Iw
                        GlobalBucklingmodel.SecProperties.TorsionConstant = FESp.J
                        GlobalBucklingmodel.SecProperties.WarpingConstant = FESp.Iomg
                        GlobalBucklingmodel.SecProperties.ShearCentre_v = FESp.cvs
                        GlobalBucklingmodel.SecProperties.ShearCentre_w = FESp.cws
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_v = FESp.Betav
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_w = FESp.Betaw
                        Svv = FESp.Sv
                        Sww = FESp.Sw
                        Zvv = FESp.Zv
                        Zww = FESp.Zw
                    elif self.Axial_method == 1:
                        GlobalBucklingmodel.SecProperties.Area = FESp.Area
                        GlobalBucklingmodel.SecProperties.MomentofInertia_v = FESp.Iyc
                        GlobalBucklingmodel.SecProperties.MomentofInertia_w = FESp.Izc
                        GlobalBucklingmodel.SecProperties.TorsionConstant = FESp.J
                        GlobalBucklingmodel.SecProperties.WarpingConstant = FESp.Iomg
                        GlobalBucklingmodel.SecProperties.ShearCentre_v = FESp.cys
                        GlobalBucklingmodel.SecProperties.ShearCentre_w = FESp.czs
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_v = FESp.Betay
                        GlobalBucklingmodel.SecProperties.WagnerCoefficient_w = FESp.Betaz
                        Svv = FESp.Sy
                        Sww = FESp.Sz
                        Zvv = FESp.Zy
                        Zww = FESp.Zz
                    GlobalBucklingmodel.Analysis.FlexuralBuckling_Axis = "Major"
                    Lamuda_method1, Pfb1 = GlobalBucklingCal.CalFlexuralBuckling()
                    GlobalBucklingmodel.Analysis.FlexuralBuckling_Axis = "Minor"
                    Lamuda_method2, Pfb2 = GlobalBucklingCal.CalFlexuralBuckling()
                    GlobalBucklingmodel.Analysis.TwistingEffects = 1
                    Lamuda_method3, Pfb31 = GlobalBucklingCal.CalAxialtorsionalBuckling()
                    Pfb3.append(Pfb31) #consider twisting effects
                    GlobalBucklingmodel.Analysis.TwistingEffects = 0
                    Lamuda_method3, Pfb32 = GlobalBucklingCal.CalAxialtorsionalBuckling()
                    Pfb3.append(Pfb32) #ignore twisting effects
                    GlobalBucklingmodel.Analysis.TwistingEffects = 1
                    # lateral torsional buckling consider Twisting Effects
                    if self.Bending_method == 0:
                        GlobalBucklingmodel.Analysis.Lateraltorsional_Buckling_Axis = "Major"
                        msaModel.GlobalBuckling.Lateraltorsional_Buckling_Axis = "Major"
                        Lamuda_method4, Pfb4 = GlobalBucklingCal.CalLateraltorsionalBuckling()
                    elif self.Bending_method == 1:
                        GlobalBucklingmodel.Analysis.Lateraltorsional_Buckling_Axis = "Minor"
                        msaModel.GlobalBuckling.Lateraltorsional_Buckling_Axis = "Minor"
                        Lamuda_method4, Pfb4 = GlobalBucklingCal.CalLateraltorsionalBuckling()
                    # lateral torsional buckling ignore Twisting Effects
                    GlobalBucklingmodel.Analysis.TwistingEffects = 0
                    Lamuda_method5, Pfb5 = GlobalBucklingCal.CalLateraltorsionalBuckling()
                Buckling_data['Lamuda_method1'] = Lamuda_method1
                Buckling_data['Lamuda_method2'] = Lamuda_method2
                Buckling_data['Lamuda_method3'] = Lamuda_method3
                Buckling_data['Lamuda_method4'] = Lamuda_method4
                Buckling_data['Pfb1'] = Pfb1 # Flexural Buckling about major axis
                Buckling_data['Pfb2'] = Pfb2 # Flexural Buckling about minor axis
                Buckling_data['Pfb3'] = Pfb3 # Axial torsional Buckling consider and ignore twisting effects
                Buckling_data['Pfb4'] = Pfb4 # lateral torsional buckling consider Twisting Effects
                Buckling_data['Pfb5'] = Pfb5 # lateral torsional buckling ignore Twisting Effects
                E = GlobalBucklingmodel.Material.E
                A = GlobalBucklingmodel.SecProperties.Area
                Fy = GlobalBucklingmodel.Material.Fy
                Buckling_data['Elastic compression'] = [A * Fy] * len(Lamuda_method4)
                if self.mw.Centerline_radioButton.isChecked() == True:
                    S_max = max(Svv, Sww)
                    S_min = min(Svv, Sww)
                    Z_max = max(Zvv, Zww)
                    Z_min = min(Zvv, Zww)
                    if self.Bending_method == 0:
                        Buckling_data['Elastic bending'] = [S_max * Fy] * len(Lamuda_method4)
                        Buckling_data['Plastic bending'] = [Z_max * Fy] * len(Lamuda_method4)
                    elif self.Bending_method == 1:
                        Buckling_data['Elastic bending'] = [S_min * Fy] * len(Lamuda_method4)
                        Buckling_data['Plastic bending'] = [Z_min * Fy] * len(Lamuda_method4)
                elif self.mw.Outline_radioButton.isChecked() == True:
                    S_max = max(Svv, Sww)
                    S_min = min(Svv, Sww)
                    Z_max = max(Zvv, Zww)
                    Z_min = min(Zvv, Zww)
                    if self.Bending_method == 0:
                        Buckling_data['Elastic bending'] = [S_max * Fy] * len(Lamuda_method4)
                        Buckling_data['Plastic bending'] = [Z_max * Fy] * len(Lamuda_method4)
                    elif self.Bending_method == 1:
                        Buckling_data['Elastic bending'] = [S_min * Fy] * len(Lamuda_method4)
                        Buckling_data['Plastic bending'] = [Z_min * Fy] * len(Lamuda_method4)
                if self.MaterialCapacity == 0:
                    Buckling_data['Material'] = 'Elastic'
                elif self.MaterialCapacity == 1:
                    Buckling_data['Material'] = 'Plastic'
                elif self.MaterialCapacity == 2:
                    Buckling_data['Material'] = 'Ignore'
                Buckling_data['method'] = 'Analytical'
                msaModel.GlobalBuckling.Buckling_data = Buckling_data
                msaModel.GlobalBuckling.Lamuda_max = float(self.MaxSlenderRatio_lineEdit.text())
                msaModel.GlobalBuckling.Lamuda_min = float(self.MinSlenderRatio_lineEdit.text())
            # =========================================================================================
            # Calculate global buckling using line element
            # =========================================================================================
            elif self.LineElement_radioButton.isChecked():
                msaModel.GlobalBuckling.Reset()
                MultiThread.Reset()
                if float(self.MinSlenderRatio_lineEdit.text()) >= float(self.MaxSlenderRatio_lineEdit.text()) or float(
                        self.MinSlenderRatio_lineEdit.text()) <= 0 or float(
                    self.MaxSlenderRatio_lineEdit.text()) <= 0 or float(self.SlenderRatioSteps_lineEdit.text()) <= 0 or float(
                    self.ElementNumber_lineEdit.text())<=0 or len(self.MinSlenderRatio_lineEdit.text())==0 or len(self.MaxSlenderRatio_lineEdit.text())==0 or len(self.SlenderRatioSteps_lineEdit.text())==0 or len(
                    self.ElementNumber_lineEdit.text())==0:
                    showMesbox(self, 'Please check the input of slender ratio!')
                    return
                if len(self.Px_lineEdit.text()) == 0  or len(self.My_lineEdit.text()) == 0 or len(self.My_lineEdit.text()) == 0 :
                    showMesbox(self, 'Some inputs are empty,\nPlease check the input of load!')
                    return
                if float(self.Px_lineEdit.text()) == 0 and float(self.My_lineEdit.text()) == 0 and float(self.Mz_lineEdit.text()) == 0:
                    showMesbox(self, 'All loads are zero,\nPlease check the input of load!')
                    return
                if float(self.Px_lineEdit.text()) < 0 and float(self.My_lineEdit.text()) == 0 and float(self.Mz_lineEdit.text()) == 0:
                    showMesbox(self, 'No Buckling under pure tension,\nPlease check the input of load!')
                    return
                SlenderRatio_min = float(self.MinSlenderRatio_lineEdit.text())
                SlenderRatio_max = float(self.MaxSlenderRatio_lineEdit.text())
                SlenderRatio_steps = int(self.SlenderRatioSteps_lineEdit.text()) - 1
                MultiThread.Parameters.Nodes_number = int(self.ElementNumber_lineEdit.text()) + 1
                MultiThread.Parameters.Px = float(self.Px_lineEdit.text())
                # MultiThread.Parameters.Mx = float(self.Mx_lineEdit.text())
                MultiThread.Parameters.My = float(self.My_lineEdit.text())
                MultiThread.Parameters.Mz = float(self.Mz_lineEdit.text())
                if self.mw.Centerline_radioButton.isChecked() == True:
                    MultiThread.Parameters.E = float(list(CMMat.E.values())[0])
                    MultiThread.Parameters.mu = float(list(CMMat.nu.values())[0])
                    MultiThread.Parameters.Fy = float(list(CMMat.Fy.values())[0])
                    if self.Axial_method == 1:
                        MultiThread.Parameters.Area = CMSp.Area
                        MultiThread.Parameters.MomentofInertia_v = CMSp.Iyy
                        MultiThread.Parameters.MomentofInertia_w = CMSp.Izz
                        MultiThread.Parameters.TorsionConstant = CMSp.J
                        MultiThread.Parameters.WarpingConstant = CMSp.Cw
                        MultiThread.Parameters.ShearCentre_v = CMSp.ysc
                        MultiThread.Parameters.ShearCentre_w = CMSp.zsc
                        MultiThread.Parameters.ky = CMSp.ky
                        MultiThread.Parameters.kz = CMSp.kz
                        MultiThread.Parameters.WagnerCoefficient_v = CMSp.Betay
                        MultiThread.Parameters.WagnerCoefficient_w = CMSp.Betaz
                        MultiThread.Parameters.WagnerCoefficient_ww = CMSp.Betaω
                        MultiThread.Parameters.Svv = CMSp.Syy
                        MultiThread.Parameters.Sww = CMSp.Szz
                        MultiThread.Parameters.Zvv = CMSp.Zyy
                        MultiThread.Parameters.Zww = CMSp.Zzz
                    elif self.Axial_method == 0:
                        MultiThread.Parameters.Area = CMSp.Area
                        MultiThread.Parameters.MomentofInertia_v = CMSp.Ivv
                        MultiThread.Parameters.MomentofInertia_w = CMSp.Iww
                        MultiThread.Parameters.TorsionConstant = CMSp.J
                        MultiThread.Parameters.WarpingConstant = CMSp.Cw
                        MultiThread.Parameters.ShearCentre_v = CMSp.vsc
                        MultiThread.Parameters.ShearCentre_w = CMSp.wsc
                        MultiThread.Parameters.ky = CMSp.kv
                        MultiThread.Parameters.kz = CMSp.kw
                        MultiThread.Parameters.WagnerCoefficient_v = CMSp.Betav
                        MultiThread.Parameters.WagnerCoefficient_w = CMSp.Betaw
                        MultiThread.Parameters.WagnerCoefficient_ww = CMSp.Betaω
                        MultiThread.Parameters.Svv = CMSp.Svv
                        MultiThread.Parameters.Sww = CMSp.Sww
                        MultiThread.Parameters.Zvv = CMSp.Zvv
                        MultiThread.Parameters.Zww = CMSp.Zww
                elif self.mw.Outline_radioButton.isChecked() == True:
                    ref_Mat = FEAnalysis.mat_ref
                    # print(FEMat.E[ref_Mat])
                    MultiThread.Parameters.E = FEMat.E[ref_Mat]
                    MultiThread.Parameters.mu = FEMat.nu[ref_Mat]
                    MultiThread.Parameters.eu = FEMat.eu[ref_Mat]
                    MultiThread.Parameters.Fy = FEMat.Fy[ref_Mat]
                    if self.Axial_method == 0:
                        MultiThread.Parameters.Area = FESp.Area
                        MultiThread.Parameters.MomentofInertia_v = FESp.Iv
                        MultiThread.Parameters.MomentofInertia_w = FESp.Iw
                        MultiThread.Parameters.TorsionConstant = FESp.J
                        MultiThread.Parameters.WarpingConstant = FESp.Iomg
                        MultiThread.Parameters.ShearCentre_v = FESp.cvs
                        MultiThread.Parameters.ShearCentre_w = FESp.cws
                        MultiThread.Parameters.ky = FESp.kv
                        MultiThread.Parameters.kz = FESp.kw
                        MultiThread.Parameters.WagnerCoefficient_v = FESp.Betav
                        MultiThread.Parameters.WagnerCoefficient_w = FESp.Betaw
                        MultiThread.Parameters.WagnerCoefficient_ww = FESp.Betaomg
                        MultiThread.Parameters.Svv = FESp.Sv
                        MultiThread.Parameters.Sww = FESp.Sw
                        MultiThread.Parameters.Zvv = FESp.Zv
                        MultiThread.Parameters.Zww = FESp.Zw
                    elif self.Axial_method == 1:
                        MultiThread.Parameters.Area = FESp.Area
                        MultiThread.Parameters.MomentofInertia_v = FESp.Iyc
                        MultiThread.Parameters.MomentofInertia_w = FESp.Izc
                        MultiThread.Parameters.TorsionConstant = FESp.J
                        MultiThread.Parameters.WarpingConstant = FESp.Iomg
                        MultiThread.Parameters.ShearCentre_v = FESp.cys
                        MultiThread.Parameters.ShearCentre_w = FESp.czs
                        MultiThread.Parameters.ky = FESp.ky
                        MultiThread.Parameters.kz = FESp.kz
                        MultiThread.Parameters.WagnerCoefficient_v = FESp.Betay
                        MultiThread.Parameters.WagnerCoefficient_w = FESp.Betaz
                        MultiThread.Parameters.WagnerCoefficient_ww = FESp.Betaomg
                        MultiThread.Parameters.Svv = FESp.Sy
                        MultiThread.Parameters.Sww = FESp.Sz
                        MultiThread.Parameters.Zvv = FESp.Zy
                        MultiThread.Parameters.Zww = FESp.Zz
                I_major = max(MultiThread.Parameters.MomentofInertia_v, MultiThread.Parameters.MomentofInertia_w)
                I_minor = min(MultiThread.Parameters.MomentofInertia_v, MultiThread.Parameters.MomentofInertia_w)
                if self.Bending_method == 0:
                    r = np.sqrt(I_minor / MultiThread.Parameters.Area)
                elif self.Bending_method == 1:
                    r = np.sqrt(I_minor / MultiThread.Parameters.Area)
                MultiThread.Parameters.Lamuda = np.array(list(
                    np.arange(SlenderRatio_min, (SlenderRatio_max + (SlenderRatio_max - SlenderRatio_min) / SlenderRatio_steps),
                              (SlenderRatio_max - SlenderRatio_min) / SlenderRatio_steps)))
                Lamuda = MultiThread.Parameters.Lamuda
                MultiThread.Parameters.L = Lamuda * r
                # if MultiThread.Parameters.ky == 0:
                #     MultiThread.Parameters.ky = 0.1
                # if MultiThread.Parameters.kz == 0:
                #     MultiThread.Parameters.kz = 0.1
                # Buckling_data = {}
                # Buckling_data["INFORMATION"] = [
                #     [ "Version", "3.0.0"],
                #     [ "Date", "20230412"],
                #     [ "Description", "This example is provided for testing Eigen buckling analysis in MASTAN3.0.0"]
                #   ]
                # Buckling_data["MATERIAL"] = [
                #     [ 1, float(E), float(E/(2*(1+mu))), float(Fy) , 0 ]
                #   ]
                # Buckling_data["SECTION"] = [
                #     [1, 1, 2, float(Area), float(MomentofInertia_v), float(MomentofInertia_w), float(TorsionConstant), float(WarpingConstant), float(ShearCentre_v), float(ShearCentre_w), ky, kz, float(WagnerCoefficient_v), float(WagnerCoefficient_w), float(WagnerCoefficient_ww)]
                # ]
                # Buckling_data["RELEASE"] = []
                # Buckling_data["BOUNDARY"] = [
                #     [1, 1, 1, 1, 1, 0, 0],
                #     [self.Nodes_number, 0, 1, 1, 0, 0, 0]
                # ]
                # Buckling_data["JOINTLOAD"] = [
                #     [self.Nodes_number, float(-Px), 0, 0, 0, float(My), float(Mz), 0, 0]
                # ]
                # Buckling_data["ANALYSIS"] = [
                #     ["Type", "eigenBuckling"],
                #     ["Modes Number", 5]
                # ]
                # Factors1 = []
                # Factors2 = []
                # Factors3 = []
                # for ii in range(len(L)):
                #     Load_factor = []
                #     x_L= np.linspace(0, L[ii], self.Nodes_number)
                #     Buckling_data["NODE"] = []
                #     Buckling_data["MEMBER"] = []
                #     for m in range(len(x_L)):
                #         Buckling_data["NODE"].append([m + 1, x_L[m], 0, 0])
                #     for n in range(len(x_L) - 1):
                #         Buckling_data["MEMBER"].append([1 + n, 1, 1 + n, 2 + n, 0])
                #     ReadData.LoadDataToModel(Buckling_data)
                #     FrameModel.initialize()
                #     Load_factor = Eigenbuckling.run()
                #     Factors1.append(Load_factor[0])
                    # Factors2.append(Load_factor[1])
                    # Factors3.append(Load_factor[2])
                # Buckling_data['Lamuda'] = Lamuda
                # Buckling_data['Factors1'] = Factors1
                # Buckling_data['Factors2'] = Factors2
                # Buckling_data['Factors3'] = Factors3
                # Buckling_data['method'] = 'Line_element'
                #print(Buckling_data['Factors1'])
                Buckling_data = {}
                if self.MaterialCapacity == 0:
                    Buckling_data['Material'] = 'Elastic'
                elif self.MaterialCapacity == 1:
                    Buckling_data['Material'] = 'Plastic'
                elif self.MaterialCapacity == 2:
                    Buckling_data['Material'] = 'Ignore'
                if self.mw.Centerline_radioButton.isChecked() == True:
                    Buckling_data['Elastic Factor'] = [MultiThread.Parameters.Fy / (
                                MultiThread.Parameters.My / MultiThread.Parameters.Svv + MultiThread.Parameters.Mz / MultiThread.Parameters.Sww + MultiThread.Parameters.Px / MultiThread.Parameters.Area)] * len(
                        MultiThread.Parameters.Lamuda)
                    Buckling_data['Plastic Factor'] = [MultiThread.Parameters.Fy / (
                                MultiThread.Parameters.My / MultiThread.Parameters.Zvv + MultiThread.Parameters.Mz / MultiThread.Parameters.Zww + MultiThread.Parameters.Px / MultiThread.Parameters.Area)] * len(
                        MultiThread.Parameters.Lamuda)
                elif self.mw.Outline_radioButton.isChecked() == True:
                    Buckling_data['Elastic Factor'] = [MultiThread.Parameters.Fy / (MultiThread.Parameters.My / MultiThread.Parameters.Svv + MultiThread.Parameters.Mz / MultiThread.Parameters.Sww + MultiThread.Parameters.Px / MultiThread.Parameters.Area)] * len(MultiThread.Parameters.Lamuda)
                    Buckling_data['Plastic Factor'] = [MultiThread.Parameters.Fy / (MultiThread.Parameters.My / MultiThread.Parameters.Zvv + MultiThread.Parameters.Mz / MultiThread.Parameters.Zww + MultiThread.Parameters.Px / MultiThread.Parameters.Area)] * len(MultiThread.Parameters.Lamuda)
                msaModel.GlobalBuckling.Buckling_data1 = Buckling_data
                self.ShowResults_pushButton.setEnabled(True)
            # self.ShowResults_pushButton.setEnabled(True)
            # self.ShowResults_pushButton.setStyleSheet("*{    \n"
            #                                           "    font: 9pt \"Segoe UI\";\n"
            #                                           "    color: rgb(0, 0, 0);\n"
            #                                           "    background: rgb(255, 255, 255);\n"
            #                                           "}\n"
            #                                           "")
            # self.Run_pushButton.setEnabled(False)
            # self.Run_pushButton.setStyleSheet("*{    \n"
            #                                           "    font: 9pt \"Segoe UI\";\n"
            #                                           "    color: rgb(128, 128, 128);\n"
            #                                           "    background: rgb(240, 240, 240);\n"
            #                                           "}\n"
            #                                           "")
            print('\nThe calculation process has been successfully completed!')
            # showMesbox(self, 'The calculation process has been successfully completed, please click the "Show Results" button to view the results!')
            # if Buckling_data['method'] == 'Analytical':
            #     Ui = GlobalBucklingPlot_Dialog(self)
            #     Ui.exec()
            # elif Buckling_data['method'] == 'Line_element':
            #     Ui = GlobalBuckling_Element_Plot_Dialog(self)
            #     Ui.exec()
            self.ShowResults_pushButton.setEnabled(True)
            self.ShowResults_pushButton.setStyleSheet("*{    \n"
                                                      "    font: 9pt \"Segoe UI\";\n"
                                                      "    color: rgb(0, 0, 0);\n"
                                                      "    background: rgb(255, 255, 255);\n"
                                                      "}\n"
                                                      "")
            QDialog.close(self)
            Ui = GBAnalMessageBox_Dialog(self, parent=self)
            Ui.exec()
        except:
            showMesbox(self, 'Please enter correct data!')
            traceback.print_exc()

    @Slot()
    def on_ShowResults_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        Buckling_data = msaModel.GlobalBuckling.Buckling_data
        if Buckling_data:
            if Buckling_data['method'] == 'Analytical':
                Ui = GlobalBucklingPlot_Dialog(self)
                Ui.exec()
            elif Buckling_data['method'] == 'Line_element':
                Ui = GlobalBuckling_Element_Plot_Dialog(self)
                Ui.exec()

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)

    def on_changed(self):
        msaModel.GlobalBuckling.Reset()
        self.ShowResults_pushButton.setEnabled(False)
        self.ShowResults_pushButton.setStyleSheet("*{    \n"
                                                  "    font: 9pt \"Segoe UI\";\n"
                                                  "    color: rgb(128, 128, 128);\n"
                                                  "    background: rgb(240, 240, 240);\n"
                                                  "}\n"
                                                  "")