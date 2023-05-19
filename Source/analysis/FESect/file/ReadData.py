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
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# ===========================================================================
# Import standard libraries
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import json
# =========================================================================================
# Import internal functions
from analysis.FESect.variables import Model
from analysis.FESect.util import PrintLog as pl


def GetFileName():
    print("The following files are found. Please enter a file name to execute:")
    JSONScript = os.getcwd() + "\\examples\\"
    Model.OutResult.Folder = JSONScript
    Files = [f for f in listdir(JSONScript) if isfile(join(JSONScript, f))]
    print(Files)
    FileName = input(">>")
    while not (FileName in Files):
        print("File is not found, please enter the file name from the list")
        print(Files)
        FileName = input(">>")
    Model.OutResult.FileName = FileName
    return JSONScript + FileName


# Read data file from JSON format,
def ReadJSON():
    FileName = GetFileName()
    f = open(FileName, 'r')
    return json.loads(f.read())


# Load Data from JSON fomat to Mastan Model
def LoadDataToModel(DataIn):
    Model.Material.ReadMaterial(np.array(DataIn["MATERIAL"], dtype=object))
    Model.Point.ReadPoint(np.array(DataIn["POINT"]))
    Model.Outline.ReadOutline(np.array(DataIn["OUTLINE"]))
    Model.Group.ReadGroup(np.array(DataIn["GROUP"]))
    Model.Analysis.ReadAnalysis(dict(DataIn["ANALYSIS"]))
    Model.YieldSurfaceAnalInfo.ReadYSurfAnalInfo(np.array(DataIn["YIELDSANALINFO"]))
    Model.OutResult.ModelInfo = (dict(DataIn["INFORMATION"]))
    return


# =========================================================================================
def ModelFromJSON(FileName=""):
    if FileName == "":
        DataIn = ReadJSON()
    else:
        f = open(FileName, 'r')
        DataIn = json.loads(f.read())
    LoadDataToModel(DataIn)
    AnalysisType = []
    if Model.Analysis.BasicProperties == 1:
        AnalysisType.append("BasicProperties")
    if Model.Analysis.StressAnalysis == 1:
        AnalysisType.append("StressAnalysis")
    if Model.Analysis.BucklingAnalysis == 1:
        AnalysisType.append("BucklingAnalysis")
    if Model.Analysis.DynamicAnalysis == 1:
        AnalysisType.append("DynamicAnalysis")
    if Model.Analysis.HeatTransfer == 1:
        AnalysisType.append("HeatTransfer")
    if Model.Analysis.YieldSurface == 1:
        AnalysisType.append("YieldSurface")
    if Model.Analysis.MomentCurvature == 1:
        AnalysisType.append("MomentCurvature")
    pl.Print(pl.ModelLog.Info(Model.OutResult.ModelInfo["Description"], Model.Material, Model.Point, Model.Outline, Model.Group, AnalysisType, Model.Analysis.Element))
    return