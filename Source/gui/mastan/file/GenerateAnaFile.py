import json
from gui.mastan.base.model import msaModel

def GenerateAnaFile(FileName):
    AnaModel = {}
    AnaModel["INFORMATION"] = GetINFORMATION()
    AnaModel["MATERIAL"] = GetMATERIAL()
    AnaModel["NODE"] = GetNODE()
    AnaModel["SECTION"] = GetSECTION()
    AnaModel["MEMBER"] = GetMEMBER()
    AnaModel["BOUNDARY"] = GetBOUNDARY()
    AnaModel["JOINTLOAD"] = GetJOINTLOAD()
    AnaModel["ANALYSIS"] = GetANALYSIS()
    with open(FileName, "w") as fp:
        fp.write(json.dumps(AnaModel, indent=4))
    return

def GetINFORMATION():
    INFORMATION = []
    Info = msaModel.Info
    INFORMATION.append(["Version", Info.Version])
    INFORMATION.append(["Date", Info.LastSavedT])
    INFORMATION.append(["Description", "Analysis Model"])
    return INFORMATION

def GetMATERIAL():
    MATERIAL = []
    Mat = msaModel.Mat
    for ii in Mat.ID:
        MATERIAL.append([ii, Mat.E[ii], Mat.G[ii], 0, 0])
    return MATERIAL

def GetSECTION():
    SECTION = []
    Sect = msaModel.Sect
    for ii in Sect.ID:
        tElemType = 2
        SECTION.append(
            [ii, Sect.MatID[ii], tElemType, Sect.A[ii], Sect.Iy[ii], Sect.Iz[ii], Sect.J[ii], Sect.Iw[ii], Sect.yc[ii],
             Sect.zc[ii], Sect.ky[ii], Sect.kz[ii], Sect.betay[ii], Sect.betaz[ii], Sect.betaw[ii]])
    return SECTION

def GetNODE():
    NODE = []
    Node = msaModel.Node
    for ii in Node.ID:
        NODE.append([ii, Node.x[ii], Node.y[ii], Node.z[ii]])
    return NODE

def GetMEMBER():
    MEMBER = []
    Member = msaModel.Member
    for ii in Member.ID:
        tbeta = 0
        MEMBER.append([ii, Member.SectionID[ii], Member.NodeI[ii], Member.NodeJ[ii], tbeta])
    return MEMBER

def GetBOUNDARY():
    BOUNDARY = []
    Bound = msaModel.Bound
    for ii in Bound.NodeID:
        BOUNDARY.append([ii] + Bound.Bound[ii])
    return BOUNDARY

def GetJOINTLOAD():
    JOINTLOAD = []
    Load = msaModel.Load
    for ii in Load.NodeID:
        tExtraF = [0, 0]
        JOINTLOAD.append([ii] + Load.LoadVector[ii] + tExtraF)
    return JOINTLOAD

def GetANALYSIS():
    IterationInfo = msaModel.IterationInfo
    ANALYSIS = [
        ["Type", "staticNonlinear"],
        ["Target Load Factor", 90],
        ["Load Step", 500],
        ["Max. Iteration", 199],
        ["Convergence", 0.001],
        ["Solution Technique", "NL"]
    ]
    ANALYSIS[0][1] = IterationInfo.AnalysisType
    ANALYSIS[1][1] = IterationInfo.LF
    ANALYSIS[2][1] = IterationInfo.LoadStep
    ANALYSIS[3][1] = IterationInfo.MaxIter
    ANALYSIS[4][1] = IterationInfo.TOL
    return ANALYSIS
