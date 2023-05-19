###########################################################################################
#
# PyFESect - Python-based Cross-platforms Section Analysis Software
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Liang Chen, Haoyi Zhang, Guanhua Li
#
# Copyright © 2023 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
# =========================================================================================
from itertools import zip_longest
import numpy as np
# =========================================================================================
# Import internal functions
from analysis.FESect.element import Tri3

def initialize():
    Information.Reset()
    Material.Reset()
    SecProperties.Reset()
    Analysis.Reset()
    OutResult.Reset()
    return

class Information:
    Version = " "
    EDate = " "
    Description = " "

    # def __init__(self):
    #     self.Version = " "
    #     self.EDate = " "
    #     self.Description = " "


    def ReadModelGenlInfo(ModelGenlInfo):
        ModelGenlInfo = dict(ModelGenlInfo)
        Information.Version = str(ModelGenlInfo["Version"])
        Information.EDate = str(ModelGenlInfo["Date"])
        Information.Description = str(ModelGenlInfo["Description"])
        return

    @classmethod
    def Reset(cls):
        Information.Version = " "
        Information.EDate = " "
        Information.Description = " "
        ##
        return


class Material:
    ID = 0
    E = 0
    mu = 0
    Fy = 0
    eu = 0
    ##

    @classmethod
    def Reset(cls):
        Material.ID = 0
        Material.E = 0
        Material.mu = 0
        Material.Fy = 0
        Material.eu = 0
        ##
        return

    def readMat(MatInfo):
        Material.ID = int(MatInfo[0][0])
        Material.E = float(MatInfo[0][1])
        Material.mu = float(MatInfo[0][2])
        Material.Fy = float(MatInfo[0][3])
        Material.eu = float(MatInfo[0][4])
        return


class SecProperties:
    Area = 0
    MomentofInertia_v = 0
    MomentofInertia_w = 0
    TorsionConstant = 0
    WarpingConstant = 0
    ShearCentre_v = 0
    ShearCentre_w = 0
    WagnerCoefficient_v = 0
    WagnerCoefficient_w = 0

    @classmethod
    def Reset(cls):
        SecProperties.Area = 0
        SecProperties.MomentofInertia_v = 0
        SecProperties.MomentofInertia_w = 0
        SecProperties.TorsionConstant = 0
        SecProperties.WarpingConstant = 0
        SecProperties.ShearCentre_v = 0
        SecProperties.ShearCentre_w = 0
        SecProperties.WagnerCoefficient_v = 0
        SecProperties.WagnerCoefficient_w = 0
        return

    def ReadSec(AnalysisInfo):
        AnalysisInfo = dict(AnalysisInfo)
        SecProperties.Area = float(AnalysisInfo["Cross-Sectional Area"])
        SecProperties.MomentofInertia_v = float(AnalysisInfo["Moment of Inertia of y"])
        SecProperties.MomentofInertia_w = float(AnalysisInfo["Moment of Inertia of z"])
        SecProperties.TorsionConstant = float(AnalysisInfo["Torsion Constant"])
        SecProperties.WarpingConstant = float(AnalysisInfo["Warping Constant"])
        SecProperties.ShearCentre_v = float(AnalysisInfo["Shear Centre of y"])
        SecProperties.ShearCentre_w = float(AnalysisInfo["Shear Centre of z"])
        SecProperties.WagnerCoefficient_w = float(AnalysisInfo["Wagner Coefficient of y"])
        SecProperties.WagnerCoefficient_v = float(AnalysisInfo["Wagner Coefficient of z"])
        return

class Analysis:
    FlexuralBuckling = 0
    FlexuralBuckling_Axis = ""
    Axialtorsional_Buckling = 0
    Lateraltorsional_Buckling = 0
    Lateraltorsional_Buckling_Axis = ""
    TwistingEffects = 0
    SlenderRatio_min = 0
    SlenderRatio_max = 0
    SlenderRatio_steps = 0

    @classmethod
    def Reset(cls):
        Analysis.FlexuralBuckling = 0
        Analysis.FlexuralBuckling_Axis = ""
        Analysis.Axialtorsional_Buckling = 0
        Analysis.Lateraltorsional_Buckling = 0
        Analysis.Lateraltorsional_Buckling_Axis = ""
        Analysis.TwistingEffects = 0
        Analysis.SlenderRatio_min = 0
        Analysis.SlenderRatio_max = 0
        Analysis.SlenderRatio_steps = 0
        return


    def ReadAnalysis(AnalysisInfo):
        AnalysisInfo = dict(AnalysisInfo)
        Analysis.FlexuralBuckling = int(AnalysisInfo["Flexural Buckling"])
        Analysis.FlexuralBuckling_Axis = str(AnalysisInfo["Flexural Buckling_Axis"])
        Analysis.Axialtorsional_Buckling = int(AnalysisInfo["Axial-torsional Buckling"])
        Analysis.Lateraltorsional_Buckling = int(AnalysisInfo["Lateral-torsional Buckling"])
        Analysis.Lateraltorsional_Buckling_Axis = str(AnalysisInfo["Lateral-torsional Buckling_Axis"])
        Analysis.TwistingEffects = int(AnalysisInfo["Twisting Effects"])
        Analysis.SlenderRatio_min = float(AnalysisInfo["SlenderRatio_min"])
        Analysis.SlenderRatio_max = float(AnalysisInfo["SlenderRatio_max"])
        Analysis.SlenderRatio_steps = float(AnalysisInfo["SlenderRatio_steps"])
        return

class OutResult:
    FileName = ""
    Folder = ""
    ModelInfo = ""
    Flexural_Buckling = []
    Axial_torsionalBuckling = []
    Lateral_torsionalBuckling = []


    @staticmethod
    def ReadOutResult(FileName, Folder):
        OutResult.FileName = FileName
        OutResult.Folder = Folder
        OutResult.ModelInfo = ""

    @classmethod
    def Reset(cls):
        OutResult.FileName = ""
        OutResult.Folder = ""
        OutResult.ModelInfo = ""
        OutResult.Flexural_Buckling = []
        OutResult.Axial_torsionalBuckling = []
        OutResult.Lateral_torsionalBuckling = []




