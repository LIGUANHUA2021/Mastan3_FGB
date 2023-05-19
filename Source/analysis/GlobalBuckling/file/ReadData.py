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
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import json
# =========================================================================================
# Import internal functions
from analysis.GlobalBuckling.variables import Model

def GetFileName(filename=""):
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
    Model.OutResult.FileName = filename
    return filename

def LoadDataToModel(DataIn):
    Model.Information.ReadModelGenlInfo((DataIn["INFORMATION"]))
    Model.Material.readMat((DataIn["REF_MATERIAL"]))
    Model.SecProperties.ReadSec((DataIn["SECPROPERTIES"]))
    Model.Analysis.ReadAnalysis(dict(DataIn["ANALYSIS"], dtype=object))
    return

def ModelFromJSON(FileName=""):
    if FileName == "":
        DataIn = ReadJSON()
    else:
        print(FileName)
        f = open(FileName, 'r')
        Savefileinfo(FileName)
        DataIn = json.loads(f.read())
    LoadDataToModel(DataIn)
    return

def ReadJSON():
    FileName = Getfilename()
    f = open(FileName, 'r')
    return json.loads(f.read())
# Load Data from JSON fomat to Mastan Model

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