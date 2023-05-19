#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Description:
# ===========================================================================
# Import standard libraries
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import json  # JSON Library for handling input and output

# =========================================================================================
# Import internal functions
from analysis.frame.variables import Model

def Getfilename():
    print("The following files are found. Please enter a file name to execute:")
    JSONScript = os.getcwd() + "\\examples\\"
    Model.OutResult.Folder = os.getcwd() + "\\"
    files = [f for f in listdir(JSONScript) if isfile(join(JSONScript, f))]
    print(files)
    FileName = input(">>")
    while not (FileName in files):
        print("File is not found, please enter the file name from the list")
        FileName = input(">>")
    Model.OutResult.ModelName = FileName
    #DbDir = os.getcwd() + '\\examples\\'
    OutFolder = os.path.join(JSONScript, FileName + '.rst')
    if not os.path.exists(OutFolder):
        os.makedirs(OutFolder)
    #Model.OutResult.FileName = JSONScript + FileName
    Model.OutResult.FileName = JSONScript + FileName
    return JSONScript + FileName
def Savefileinfo(FileName):
    JSONScript = os.getcwd() + "\\examples\\"
    Model.OutResult.Folder = os.getcwd() + "\\"
    FileName = FileName.split("\\")
    FileName = FileName[len(FileName) - 1]
    Model.OutResult.ModelName = FileName
    OutFolder = os.path.join(JSONScript, FileName + '.rst')
    if not os.path.exists(OutFolder):
        os.makedirs(OutFolder)
    Model.OutResult.FileName = JSONScript + FileName
# Read data file from JSON format,
def ReadJSON():
    FileName = Getfilename()
    f = open(FileName, 'r')
    return json.loads(f.read())
# Load Data from JSON fomat to Mastan Model
def LoadDataToModel(DataIn):
    Model.Information.ReadModelGenlInfo(np.array(DataIn["INFORMATION"]))
    Model.Node.ReadNode(Model.Node, np.array(DataIn["NODE"]))
    Model.Member.ReadMember(np.array(DataIn["MEMBER"]))
    Model.Material.ReadMat(np.array(DataIn["MATERIAL"]))
    Model.Section.ReadSect(np.array(DataIn["SECTION"]))
    Model.Boundary.ReadBoun(np.array(DataIn["BOUNDARY"]))
    try:
        Model.Coupling.ReadCoupl(DataIn["COUPLING"])
    except:
        pass
    try:
        Model.SpringBoundary.ReadSpringBound(DataIn["SPRINGBOUNDARY"])
    except:
        Model.SpringBoundary.Initialize()
    try:
        Model.SpringModel.ReadSpringModel(DataIn["SPRINGMODEL"])
    except:
        Model.SpringModel.Initialize()
    Model.JointLoad.ReadJNTL(np.array(DataIn["JOINTLOAD"]))
    Model.Analysis.ReadAna(np.array(DataIn["ANALYSIS"]))
    try:
        Model.SoilParameter.ReadSoilParameter(DataIn["SOILPARAMETER"])
    except:
        Model.SoilParameter.Initialize()
    try:
        Model.Buried.ReadBuried(DataIn["PILE"])
    except:
        Model.Buried.Initialize()
    try:
        Model.GroundAcceleration.ReadGroundACC(Model.GroundAcceleration, np.array(DataIn["GROUNDACCELARATION"]))
    except:
        pass
    return
# =========================================================================================
def modelfromJSON(FileName=''):
    if FileName == "":
        DataIn = ReadJSON()
    else:
        print(FileName)
        f = open(FileName, 'r')
        Savefileinfo(FileName)
        DataIn = json.loads(f.read())
    LoadDataToModel(DataIn)
    return
# =====DataIn==============================================================================
# The following functions are called by the Mastan GUI
# =========================================================================================
def ReadJSON_GUI(FileName):
    f = open(FileName, 'r')
    return json.loads(f.read())
