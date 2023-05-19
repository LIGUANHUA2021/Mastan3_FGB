#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import json  # JSON Library for handling input and output

# =========================================================================================
# Import internal functions
from analysis.solid.variables import Model

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
    print("Read Data Save Modelname = ", Model.OutResult.ModelName)
    #DbDir = os.getcwd() + '\\examples\\'
    OutFolder = os.path.join(JSONScript, FileName + '.rst')
    if not os.path.exists(OutFolder):
        os.makedirs(OutFolder)
    #Model.OutResult.FileName = JSONScript + FileName
    Model.OutResult.FileName = JSONScript + FileName
    print("Read Data Save Filename = ", Model.OutResult.FileName)
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
    Model.Node.ReadNode(np.array(DataIn["NODE"]))
    Model.Element.ReadElement(np.array(DataIn["ELEMENT"]))
    Model.Material.ReadMat(np.array(DataIn["MATERIAL"]))
    Model.Boundary.ReadBoun(np.array(DataIn["BOUNDARY"]))
    Model.PointLoad.ReadPNTL(np.array(DataIn["POINTLOAD"]))
    Model.Analysis.ReadAnal(np.array(DataIn["ANALYSIS"]))
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
