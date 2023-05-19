import json, os
from gui.mastan.base.model import *

'''============================================================
 Import data file
============================================================'''
def ImportDataFile(FileName):
    File = open(FileName)
    ImportData = json.load(File)
    msaModel.ResetAll()
    tFilelName = FileName.split("/")
    msaModel.FileInfo.FileName = tFilelName[len(tFilelName) - 1]
    ReadMat(ImportData["MATERIAL"])
    ReadSect(ImportData["SECTION"])
    ReadNode(ImportData["NODE"])
    ReadMember(ImportData["MEMBER"])
    ReadLoad(ImportData["LOAD"])
    ReadBound(ImportData["BOUND"])
    try:
        ReadSpringModel(ImportData["SPRINGMODEL"])
    except:
        pass
    try:
        ReadSpringBound(ImportData["SPRINGBOUN"])
    except:
        pass
    ReadInfo(ImportData["MODELINFO"])
    ReadIterInfo(ImportData["INTERATION"])
    return
# Read material information
def ReadMat(tMat):
    for key in tMat:
        tID = int(key)
        tE, tG, tFy = float(tMat[key]["E"]), float(tMat[key]["G"]), float(tMat[key]["Fy"])
        msaModel.Mat.Add(tID,tE,tG,tFy)
    return
# Read section information
def ReadSect(tSect):
    for key in tSect:
        tID = int(key)
        tMat = tSect[key]["MAT"]
        tA = tSect[key]["A"]
        tIy, tIz = tSect[key]["Iy"], tSect[key]["Iz"]
        tJ = tSect[key]["J"]
        tIw = tSect[key]["Iw"]
        tyc, tzc = tSect[key]["yc"], tSect[key]["zc"]
        tky, tkz = tSect[key]["ky"], tSect[key]["kz"]
        tbetay, tbetaz, tbetaw = tSect[key]["betay"], tSect[key]["betaz"], tSect[key]["betaw"]
        msaModel.Sect.Add(tID, tMat, tA, tIy, tIz, tJ, tIw, tyc, tzc, tky, tkz, tbetay, tbetaz, tbetaw)
    return
# Read node information
def ReadNode(tNode):
    for key in tNode:
        tID = int(key)
        tx, ty, tz = tNode[key][0],tNode[key][1],tNode[key][2]
        msaModel.Node.Add(tID,tx, ty, tz)
    return
# Read member information
def ReadMember(tMem):
    for key in tMem:
        tID = int(key)
        tSecctID = tMem[key]["Section"]
        tNodeI,tNodeJ = tMem[key]["Node"][0],tMem[key]["Node"][1]
        msaModel.Member.Add(tID,tSecctID,tNodeI,tNodeJ)
    return
# Read load condtions
def ReadLoad(tLoad):
    for key in tLoad:
        tNodeID = int(key)
        tLoadVector = tLoad[key]
        msaModel.Load.Add(tNodeID,tLoadVector)
    return
# Read Boundary conditions
def ReadBound(tBound):
    for key in tBound:
        tNID = int(key)
        tBoundCondition = tBound[key]
        msaModel.Bound.Add(tNID,tBoundCondition)
    return
# Read Spring model
def ReadSpringModel(tSprModel):
    for key in tSprModel:
        tSID = int(key)
        tDis, tF = tSprModel[key]
        msaModel.SpringModel.Add(tSID, tDis, tF)
    return
# Read Spring boundary conditions
def ReadSpringBound(tSprBound):
    for key in tSprBound:
        tNID = int(key)
        tBound = tSprBound[key]
        msaModel.SpringBoundary.Add(tNID, tBound)
    return
# Read model information
def ReadInfo(tMInfo):
    msaModel.Info.ModelName = tMInfo["ModelName"]
    msaModel.Info.Version = tMInfo["Version"]
    msaModel.Info.CreatT = tMInfo["CreatedTime"]
    msaModel.Info.LastSavedT = tMInfo["LastRevised"]
    return
# Read iteration information
def ReadIterInfo(tIterInfo):
    tMaxIter = tIterInfo["MaxIter"]
    tTOL = tIterInfo["TOL"]
    tLoadStep = tIterInfo["LoadStep"]
    tLoadFactor = tIterInfo["LoadFactor"]
    tAnalysisType = tIterInfo["AnalysisType"]
    msaModel.IterationInfo.Modify(tMaxIter, tTOL, tLoadStep, tLoadFactor, tAnalysisType)
    return

'''============================================================
 Import data file
============================================================'''
def SaveDataFile(FileName):
    SavedModel = {"MATERIAL": {}, "SECTION":{}, "NODE":{}, "MEMBER": {}, "LOAD":{}, "BOUND":{}, "MODELINFO":{}, "INTERATION":{}, "MODELINFO":{}}
    SavedModel["MATERIAL"] = SaveMat()
    SavedModel["SECTION"] = SaveSect()
    SavedModel["NODE"] = SaveNode()
    SavedModel["MEMBER"] = SaveMember()
    SavedModel["LOAD"] = SaveLoad()
    SavedModel["BOUND"] = SaveBound()
    SavedModel["SPRINGMODEL"] = SaveSpringModel()
    SavedModel["SPRINGBOUN"] = SaveSpringBound()
    SavedModel["MODELINFO"] = SaveInfo()
    SavedModel["INTERATION"] = SaveIterInfo()
    print("Mastan3 FileName = ", FileName)
    with open(FileName, "w") as fp:
        fp.write(json.dumps(SavedModel, indent=4))
    return

def SaveMat():
    tMat = msaModel.Mat()
    OutputMat = {}
    for ii in range(tMat.Count):
        tID = tMat.ID[ii]
        tSingleMat = {"E": tMat.E[tID], "G": tMat.G[tID],"Fy": tMat.Fy[tID]}
        OutputMat[str(tID)] = tSingleMat
    return OutputMat

def SaveSect():
    tSect = msaModel.Sect()
    OutputSect = {}
    for ii in range(tSect.Count):
        tID = tSect.ID[ii]
        tSingleSect = {"MAT": tSect.MatID[tID], "A": tSect.A[tID], "Iy": tSect.Iy[tID], "Iz": tSect.Iz[tID],
                       "J": tSect.J[tID], "Iw": tSect.Iw[tID], "yc": tSect.yc[tID], "zc": tSect.zc[tID],
                       "ky": tSect.ky[tID], "kz": tSect.kz[tID],
                       "betay": tSect.betay[tID], "betaz": tSect.betaz[tID], "betaw": tSect.betaw[tID]}
        OutputSect[str(tID)] = tSingleSect
    return OutputSect

def SaveNode():
    tNode = msaModel.Node()
    OutputNode = {}
    for ii in range(tNode.Count):
        tID = tNode.ID[ii]
        tSingeNode = [tNode.x[tID], tNode.y[tID], tNode.z[tID]]
        OutputNode[str(tID)] = tSingeNode
    return OutputNode

def SaveMember():
    tMem = msaModel.Member()
    OuputMem = {}
    for ii in range(tMem.Count):
        tID = tMem.ID[ii]
        tSectID = tMem.SectionID[tID]
        tNID = [tMem.NodeI[tID],tMem.NodeJ[tID]]
        tSingleMem = {"Section":tSectID,"Node":tNID}
        OuputMem[str(tID)] = tSingleMem
    return OuputMem

def SaveLoad():
    tLoad = msaModel.Load()
    OutputLoad = {}
    for ii in range(tLoad.Count):
        tNodeID = tLoad.NodeID[ii]
        tLoadVector = tLoad.LoadVector[tNodeID]
        OutputLoad[str(tNodeID)] = tLoadVector
    return OutputLoad

def SaveBound():
    tBound = msaModel.Bound()
    OutputBound = {}
    for ii in range(tBound.Count):
        tNID = tBound.NodeID[ii]
        tSingleBound = tBound.Bound[tNID]
        OutputBound[str(tNID)] = tSingleBound
    return OutputBound

def SaveSpringModel():
    tSprModel = msaModel.SpringModel
    OutputSprModel = {}
    for ii in range(tSprModel.Count):
        tSID = tSprModel.ID[ii]
        tDis, tF = tSprModel.Dis[tSID], tSprModel.F[tSID]
        OutputSprModel[str(tSID)] = [tDis, tF]
    return  OutputSprModel

def SaveSpringBound():
    tSprBound = msaModel.SpringBoundary
    OutputSprBound = {}
    for ii in range(tSprBound.Count):
        tNID = tSprBound.NodeID[ii]
        tBound = tSprBound.Bound[tNID]
        OutputSprBound[str(tNID)] = tBound
    return OutputSprBound

def SaveInfo():
    msaModel.Info.Save()
    tInfo = msaModel.Info()
    Output = {"ModelName": tInfo.ModelName,"Version": tInfo.Version,"CreatedTime":tInfo.CreatT, "LastRevised":tInfo.LastSavedT}
    return Output

def SaveIterInfo():
    tIterInfo = msaModel.IterationInfo()
    Output = {"MaxIter": tIterInfo.MaxIter,"TOL": tIterInfo.TOL,"LoadStep":tIterInfo.LoadStep,"LoadFactor": tIterInfo.LF, "AnalysisType": tIterInfo.AnalysisType}
    # print(os.path.abspath(__file__))
    return Output
'''============================================================
TEST UNIT
============================================================'''
if __name__ == "__main__":
    ImportDataFile("D:\Research File\ResearchProgram\Mastan3\Source\gui\mastan\examples\Sample0.json")
    # print("Successfully import!")
    # print(msaModel.Info.ModelName)
    # print(msaModel.SpringBoundary.NodeID, msaModel.SpringBoundary.Bound)
    # print(msaModel.SpringModel.Dis, msaModel.SpringModel.F)
    # print(os.path.abspath(__file__))
    # print(msaModel.Mat.ID,msaModel.Mat.E)
    # print(msaModel.Sect.ID,msaModel.Sect.A)
    # print(msaModel.Node.ID,msaModel.Node.x)
    SaveDataFile("D:\Research File\ResearchProgram\Mastan3\Source\gui\mastan\examples\Sample2.json")