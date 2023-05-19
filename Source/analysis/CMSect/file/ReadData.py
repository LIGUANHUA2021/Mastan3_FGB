#############################################################################

# Project Leaders :
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

# ===========================================================================
# Import internal functions
from analysis.CMSect.variables import Model
# ===========================================================================

def Getfilename():
    print("The following files are found. Please enter a file name to execute:")
    #JSONScript = os.getcwd() + "\\examples\\" # No GUI
    JSONScript = os.getcwd() # With GUI
    Model.OutResult.Folder = os.getcwd() + os.sep
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
    Model.OutResult.FileName = JSONScript + os.sep + FileName
    return JSONScript + os.sep + FileName

def Savefileinfo(FileName):
    #JSONScript = os.getcwd() + "\\examples\\" # No GUI
    JSONScript = os.getcwd() # With GUI
    # print("Check savefileinfo:",JSONScript)
    # print("Check savefileinfo99999:", FileName)
    #Model.OutResult.Folder = os.getcwd() + "\\"
    tDirFileName = FileName.split("/")[-1]
    ModelName = os.path.basename(tDirFileName)
    #print("type FileName.split("/")",type(FileName.split("/")))
    # print("FileName.split("")", FileName.split("/"))
    # print("Check 2:", ModelName)
    Model.OutResult.ModelName = ModelName
    tOutFolder ="/".join(FileName.split("/")[0:len(FileName.split("/"))-1])
    OutFolder = os.path.join(tOutFolder, ModelName + '.rst')
    Model.OutResult.Folder = OutFolder
    if not os.path.exists(OutFolder):
        os.makedirs(OutFolder)
    Model.OutResult.FileName = tOutFolder + os.sep + ModelName
    # print("Check savefileinfo22222:", Model.OutResult.FileName)
# Read data file from JSON format,
def ReadJSON():
    FileName = Getfilename()
    f = open(FileName, 'r')
    Output = json.loads(f.read())
    f.close()
    return Output
# Load Data from JSON fomat to Mastan Model
def LoadDataToModel(DataIn):
    Model.Information.ReadModelGenlInfo(np.array(DataIn["INFORMATION"]))
    Model.Point.ReadPoint(Model.Point, np.array(DataIn["POINT"]))
    Model.Segment.ReadSegment(np.array(DataIn["SEGMENT"]))
    Model.Material.ReadMaterial(np.array(DataIn["MATERIAL"]))
    Model.Fiber.ReadFiber(np.array(DataIn["FIBER"]))
    Model.YieldSurfaceAnalInfo.ReadYSurfAnalInfo(np.array(DataIn["YieldSAnalInfo"]))
    Model.OutResult.ModelInfo = (np.array(DataIn["INFORMATION"]))
    return
# =========================================================================================
def modelfromJSON(FileName=''):
    if FileName == "":
        DataIn = ReadJSON()
        # print(DataIn)
        LoadDataToModel(DataIn)
    else:
        try:
            # print(FileName)
            LoadDataToModel(FileName)
        except:
            f = open(FileName, 'r')
            Savefileinfo(FileName)
            DataIn = json.loads(f.read())
            f.close()
            LoadDataToModel(DataIn)
    return
# =====DataIn==============================================================================
