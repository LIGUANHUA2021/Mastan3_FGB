import datetime

class msaModel:
    # Model information
    class FileInfo:
        FileName = ""
    class Info():
        ModelName = 'test'
        Version = ''
        CreatT = ''
        LastSavedT = ''
        # Creat File
        def Create(tModelName:str):
            msaModel.Info.ModelName = tModelName
            msaModel.Info.Version = "Mastan3"
            CurrentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msaModel.CreatT = CurrentT
            msaModel.LastSavedT = CurrentT
        # Save model
        def Save():
            CurrentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msaModel.LastSavedT = CurrentT
        # Reset
        def Reset():
            msaModel.Info.ModelName = ''
            msaModel.Info.Version = ''
            msaModel.CreatT = ''
            msaModel.LastSavedT = ''
    # Material Properties
    class Mat:
        Count = 0
        ID = []
        E = {}
        G = {}
        Fy = {}
        #Add Material
        def Add(tID:int, tE:float, tG:float, tFy:float):
            msaModel.Mat.Count += 1
            msaModel.Mat.ID.append(tID)
            msaModel.Mat.E[tID] = tE
            msaModel.Mat.G[tID] = tG
            msaModel.Mat.Fy[tID] = tFy
        #Remove Material -
        def Remove(tID:int):
            if msaModel.CheckID(tID,msaModel.Mat.ID) == 0:
                print('Warning! Please input the correct material ID.')
                return
            if msaModel.Sect.Count > 0:
                if msaModel.Mat.Count == 1:
                    print('Warning! Please define at least one material property for sections.')
                    return
                else:
                    msaModel.Mat.ID.remove(tID)
                    msaModel.Mat.Count -= 1
                    defaultID = msaModel.Mat.ID[0]
                    del msaModel.Mat.E[tID]
                    del msaModel.Mat.G[tID]
                    del msaModel.Mat.Fy[tID]
                    # Revise the section property accordingly
                    tSectionID_list = [k for k, v in msaModel.Sect.MatID.items() if v == tID]
                    for ii in tSectionID_list:
                        msaModel.Sect.MatID[ii] = defaultID
                    return
            msaModel.Mat.ID.remove(tID)
            msaModel.Mat.Count -= 1
            del msaModel.Mat.E[tID]
            del msaModel.Mat.G[tID]
            del msaModel.Mat.Fy[tID]
        #Modify Material
        def Modify(tID:int, tE:float, tG:float, tFy:float):
            if msaModel.CheckID(tID,msaModel.Mat.ID) == 0:
                print('Warning! Please input the correct material ID.')
                return
            msaModel.Mat.E[tID] = tE
            msaModel.Mat.G[tID] = tG
            msaModel.Mat.Fy[tID] = tFy
        #Reset Material
        def Reset():
            msaModel.Mat.Count = 0
            msaModel.Mat.E.clear()
            msaModel.Mat.G.clear()
            msaModel.Mat.Fy.clear()
            msaModel.Mat.ID.clear()
    # Section Properties
    class Sect:
        Count = 0
        ID = []
        MatID = {}
        A = {}
        Iy, Iz = {},{}
        J = {}
        Iw = {}
        yc, zc = {}, {}
        ky, kz = {}, {}
        betay, betaz, betaw = {},{},{}
        # Add Section
        def Add(tID:int, tMatID:int, tA:float, tIy:float, tIz:float, tJ:float, tIw:float, tyc:float, tzc:float, tky:float, tkz:float, tbetay:float, tbetaz:float, tbetaw:float):
            if msaModel.CheckID(tMatID,msaModel.Mat.ID) == 0:
                print('Please input the exists material ID.')
                return
            msaModel.Sect.Count += 1
            msaModel.Sect.ID.append(tID)
            msaModel.Sect.MatID[tID] = tMatID
            msaModel.Sect.A[tID] = tA
            msaModel.Sect.Iy[tID], msaModel.Sect.Iz[tID] = tIy, tIz
            msaModel.Sect.J[tID] = tJ
            msaModel.Sect.Iw[tID] = tIw
            msaModel.Sect.yc[tID], msaModel.Sect.zc[tID] = tyc, tzc
            msaModel.Sect.ky[tID], msaModel.Sect.kz[tID] = tky, tkz
            msaModel.Sect.betay[tID], msaModel.Sect.betaz[tID], msaModel.Sect.betaw[tID] = tbetay, tbetaz, tbetaw
        # Remove Section
        def Remove(tID):
            if msaModel.CheckID(tID,msaModel.Sect.ID) == 0:
                print('Warning! Please input the correct section ID.')
                return
            if msaModel.Node.Count > 0:
                if msaModel.Sect.Count == 1:
                    print('Warning! Please define at least one section property for nodes.')
                    return
                else:
                    msaModel.Sect.ID.remove(tID)
                    msaModel.Sect.Count -= 1
                    defaultID = msaModel.Sect.ID[0]
                    del msaModel.Sect.MatID[tID]
                    del msaModel.Sect.A[tID]
                    del msaModel.Sect.Iy[tID]
                    del msaModel.Sect.Iz[tID]
                    del msaModel.Sect.J[tID]
                    del msaModel.Sect.Iw[tID]
                    del msaModel.Sect.yc[tID]
                    del msaModel.Sect.zc[tID]
                    del msaModel.Sect.ky[tID]
                    del msaModel.Sect.kz[tID]
                    del msaModel.Sect.betay[tID]
                    del msaModel.Sect.betaz[tID]
                    del msaModel.Sect.betaw[tID]
                    # Revise the node property accordingly
                    tNodeID_list = [k for k, v in msaModel.Node.SectID.items() if v == tID]
                    for ii in tNodeID_list:
                        msaModel.Node.SectID[ii] = defaultID
                    return
            msaModel.Sect.Count -= 1
            del msaModel.Sect.MatID[tID]
            del msaModel.Sect.A[tID]
            del msaModel.Sect.Iy[tID]; del msaModel.Sect.Iz[tID]
            del msaModel.Sect.J[tID]
            del msaModel.Sect.Iw[tID]
            del msaModel.Sect.yc[tID]; del msaModel.Sect.zc[tID]
            del msaModel.Sect.ky[tID]; del msaModel.Sect.kz[tID]
            del msaModel.Sect.betay[tID]; del msaModel.Sect.betaz[tID]; del msaModel.Sect.betaw[tID]
            msaModel.Sect.ID.remove(tID)
            # please revise the node property accodingly
        # Modify Section property
        def Modify(tID:int, tMatID:int, tA:float, tIy:float, tIz:float, tJ:float, tIw:float, tyc:float, tzc:float, tky:float, tkz:float, tbetay:float, tbetaz:float, tbetaw:float):
            if msaModel.CheckID(tID,msaModel.Sect.ID) == 0:
                print('Warning! Please input the correct section ID.')
                return
            msaModel.Sect.MatID[tID] = tMatID
            msaModel.Sect.A[tID] = tA
            msaModel.Sect.Iy[tID], msaModel.Sect.Iz[tID] = tIy, tIz
            msaModel.Sect.J[tID] = tJ
            msaModel.Sect.Iw[tID] = tIw
            msaModel.Sect.yc[tID], msaModel.Sect.zc[tID] = tyc, tzc
            msaModel.Sect.ky[tID], msaModel.Sect.kz[tID] = tky, tkz
            msaModel.Sect.betay[tID], msaModel.Sect.betaz[tID], msaModel.Sect.betaw[tID] = tbetay, tbetaz, tbetaw
        # Resect Section property
        def Reset():
            msaModel.Sect.Count = 0
            msaModel.Sect.ID = []
            msaModel.Sect.MatID = {}
            msaModel.Sect.A = {}
            msaModel.Sect.Iy, msaModel.Sect.Iz = {}, {}
            msaModel.Sect.J = {}
            msaModel.Sect.Iw = {}
            msaModel.Sect.yc, msaModel.Sect.zc = {}, {}
            msaModel.Sect.betay, msaModel.Sect.betaz, msaModel.Sect.betaw = {}, {}, {}
    # Node Properties
    class Node:
        Count = 0
        ID = []
        x,y,z = {},{},{} # Coordinate of the node
        # Add Node
        def Add(tID:int, tx:float, ty:float, tz:float):
            if msaModel.CheckID(tID,msaModel.Node.ID) == 1:
                print('Please input the correct node ID.')
                return
            msaModel.Node.Count += 1
            msaModel.Node.ID.append(tID)
            msaModel.Node.x[tID] = tx
            msaModel.Node.y[tID] = ty
            msaModel.Node.z[tID] = tz
        # Remove Node
        def Remove(tID):
            if msaModel.CheckID(tID,msaModel.Node.ID) == 0:
                print('Warning! Please input the correct node ID.')
                return
            msaModel.Node.Count -= 1
            del msaModel.Node.x[tID]
            del msaModel.Node.y[tID]
            del msaModel.Node.z[tID]
            msaModel.Node.ID.remove(tID)
            tRemoved_MemberID = []
            for ii in range(msaModel.Member.Count):
                tMID = msaModel.Member.ID[ii]
                if (tID == msaModel.Member.NodeI[tMID] or tID == msaModel.Member.NodeJ[tMID]):
                    tRemoved_MemberID.append(tMID)
            for ii in tRemoved_MemberID:
                msaModel.Member.Remove(ii)
            if msaModel.CheckID(tID,msaModel.Load.NodeID) == 1:
                msaModel.Load.Remove(tID)
        # Modify Node property
        def Modify(tID:int, tx:float, ty:float, tz:float):
            if msaModel.CheckID(tID,msaModel.Node.ID) == 0:
                print('Warning! Please input the correct node ID.')
                return
            msaModel.Node.x[tID] = tx
            msaModel.Node.y[tID] = ty
            msaModel.Node.z[tID] = tz
        # Reset
        def Reset():
            msaModel.Node.Count = 0
            msaModel.Node.ID = []
            msaModel.Node.x = {}
            msaModel.Node.y = {}
            msaModel.Node.z = {}
    # Member property
    class Member:
        Count = 0
        ID = []
        SectionID = {}
        NodeI = {}
        NodeJ = {}
        # Add member
        def Add(tID:int, tSectionID: int, tN1ID:int, tN2ID:int): # N1ID and N2ID: the indices of two member's end nodes
            if (msaModel.CheckID(tN1ID,msaModel.Node.ID) == 0 or msaModel.CheckID(tN2ID,msaModel.Node.ID) == 0):
                print('Please input the exists node ID.')
                return
            if msaModel.CheckID(tSectionID,msaModel.Sect.ID) == 0:
                print("Please input the exists node ID")
                return
            msaModel.Member.Count += 1
            msaModel.Member.ID.append(tID)
            msaModel.Member.SectionID[tID] = tSectionID
            msaModel.Member.NodeI[tID] = tN1ID
            msaModel.Member.NodeJ[tID] = tN2ID
        # Remove member
        def Remove(tID:int):
            if msaModel.CheckID(tID,msaModel.Member.ID) == 0:
                print('Warning! Please input the correct member ID.')
                return
            msaModel.Member.Count -= 1
            del msaModel.Member.SectionID[tID]
            del msaModel.Member.NodeI[tID]
            del msaModel.Member.NodeJ[tID]
            msaModel.Member.ID.remove(tID)
        # Modify member property
        def Modify(tID:int, tSectionID:int, tN1ID:int, tN2ID:int):
            if msaModel.CheckID(tID,msaModel.Member.ID) == 0:
                print('Warning! Please input the correct member ID.')
                return
            msaModel.Member.SectionID[tID] = tSectionID
            msaModel.Member.NodeI[tID] = tN1ID
            msaModel.Member.NodeJ[tID] = tN2ID
        # Reset
        def Reset():
            msaModel.Member.Count = 0
            msaModel.Member.ID = []
            msaModel.Member.SectionID = {}
            msaModel.Member.NodeI = {}
            msaModel.Member.NodeJ = {}
    # if tID is an element in tIDList, return 1; else, return 0
    class SpringModel():
        Count = 0
        ID = []
        Dis = {} # The key here is the spring ID and the corresponding value is a list
        F = {} # The key here is the spring ID and the corresponding value is a list
        # Add spring
        def Add(tID: int, tDis: list, tF: list):
            if (len(tDis) != len(tF)):
                print('Please the correct d vs F for creating srping!')
                return
            msaModel.SpringModel.Count += 1
            msaModel.SpringModel.ID.append(tID)
            msaModel.SpringModel.Dis[tID] = tDis
            msaModel.SpringModel.F[tID] = tF
        # Remove spring
        def Remove(tID: int):
            msaModel.SpringModel.Count -= 1
            msaModel.SpringModel.ID.remove(tID)
            del msaModel.SpringModel.Dis[tID]
            del msaModel.SpringModel.F[tID]
        # Modify spring
        def Modify(tID: int, tDis: list, tF: list):
            if msaModel.CheckID(tID,msaModel.SpringModel.ID) == 0:
                print('Warning! Please input the correct member ID.')
                return
            msaModel.SpringModel.Dis[tID] = tDis
            msaModel.SpringModel.F[tID] = tF
        # Reset
        def Reset():
            msaModel.SpringModel.Count = 0
            msaModel.SpringModel.ID = []
            msaModel.SpringModel.Dis = {}
            msaModel.SpringModel.F = {}
    class SpringBoundary():
        Count = 0
        NodeID = []
        Bound = {}
        def Add(tNodeID: int, tBound: list):
            if msaModel.CheckID(tNodeID,msaModel.Node.ID) == 0:
                print('Please input the exists node ID.')
                return
            if msaModel.CheckID(tNodeID,msaModel.SpringBoundary.NodeID) == 1:
                for ii in range(len(msaModel.Load.LoadVector[tNodeID])):
                    msaModel.SpringBoundary.Modify(tNodeID, tBound)
                return
            msaModel.SpringBoundary.Count += 1
            msaModel.SpringBoundary.NodeID.append(tNodeID)
            msaModel.SpringBoundary.Bound[tNodeID] = tBound
        def Remove(tNodeID: int):
            if msaModel.CheckID(tNodeID, msaModel.SpringBoundary.NodeID) == 0:
                print('Please input the exists nodal spring boundary condition.')
                return
            msaModel.SpringBoundary.Count -= 1
            msaModel.SpringBoundary.NodeID.remove(tNodeID)
            del msaModel.SpringBoundary.Bound[tNodeID]
        def Modify(tNodeID: int, tBound: list):
            if msaModel.CheckID(tNodeID, msaModel.SpringBoundary.NodeID) == 0:
                print('Please input the exists nodal spring boundary condition.')
                return
            msaModel.SpringBoundary.Bound[tNodeID] = tBound
        def Reset():
            msaModel.SpringBoundary.Count = 0
            msaModel.SpringBoundary.NodeID = []
            msaModel.SpringBoundary.Bound = {}
    # Load Conditions
    class Load():
        Count = 0
        NodeID = []
        LoadVector = {}
        def Add(tNodeID: int, tLoadVector: list):
            if msaModel.CheckID(tNodeID,msaModel.Node.ID) == 0:
                print('Please input the exists node ID.')
                return
            if msaModel.CheckID(tNodeID,msaModel.Load.NodeID) == 1:
                for ii in range(len(msaModel.Load.LoadVector[tNodeID])):
                    msaModel.Load.Modify(tNodeID, tLoadVector)
                return
            msaModel.Load.Count += 1
            msaModel.Load.NodeID.append(tNodeID)
            msaModel.Load.LoadVector[tNodeID] = tLoadVector
        def Remove(tNodeID: int):
            if msaModel.CheckID(tNodeID, msaModel.Load.NodeID) == 0:
                print('Please input the exists nodal load.')
                return
            msaModel.Load.Count -= 1
            msaModel.Load.NodeID.remove(tNodeID)
            del msaModel.Load.LoadVector[tNodeID]
        def Modify(tNodeID: int, tLoadVector:list):
            if msaModel.CheckID(tNodeID, msaModel.Load.NodeID) == 0:
                print('Please input the exists nodal load.')
                return
            msaModel.Load.LoadVector[tNodeID] = tLoadVector
        def Reset():
            msaModel.Load.Count = 0
            msaModel.Load.NodeID = []
            msaModel.Load.LoadVector = {}
    # Boundary Conditions
    class Bound():
        Count = 0
        NodeID = []
        Bound = {} # The  boundary conditions are given here in detail
        # Add
        def Add(tNodeID: int, tBound: list):
            if msaModel.CheckID(tNodeID,msaModel.Node.ID) == 0:
                print('Please input the correct Node ID')
                return
            if msaModel.CheckID(tNodeID,msaModel.Bound.NodeID) == 1:
                msaModel.Bound.Modify(tNodeID,tBound)
            msaModel.Bound.Count += 1
            msaModel.Bound.NodeID.append(tNodeID)
            msaModel.Bound.Bound[tNodeID] = tBound
        def Remove(tNodeID:int):
            if msaModel.CheckID(tNodeID,msaModel.Bound.NodeID) == 0:
                print('Please input the correct boundary condition ID')
                return
            msaModel.Bound.Count -= 1
            msaModel.Bound.NodeID.remove(tNodeID)
            del msaModel.Bound.Bound[tNodeID]
        # Modify
        def Modify(tNodeID: int, tBound: list):
            if msaModel.CheckID(tNodeID,msaModel.Bound.NodeID) == 0:
                print('Please input the correct node ID')
                return
            msaModel.Bound.Bound[tNodeID] = tBound
        # Reset
        def Reset():
            msaModel.Bound.Count  = 0
            msaModel.Bound.NodeID = []
            msaModel.Bound.Bound = {}
    # Iteration Information
    class IterationInfo():
        MaxIter = 100
        TOL = 0.001
        LoadStep = 100
        LF = 1
        AnalysisType = "staticLinear"
        def Modify(tMaxIter:int,tTOL:float,tLoadStep:int,tLF:float,tAnalysisType:str):
            msaModel.IterationInfo.MaxIter = tMaxIter
            msaModel.IterationInfo.TOL = tTOL
            msaModel.IterationInfo.LoadStep = tLoadStep
            msaModel.IterationInfo.LF = tLF
            msaModel.IterationInfo.AnalysisType = tAnalysisType
        def Reset():
            msaModel.IterationInfo.MaxIter = 100
            msaModel.IterationInfo.TOL = 0.001
            msaModel.IterationInfo.LoadStep = 100
            msaModel.IterationInfo.LF = 1.0
            msaModel.IterationInfo.AnalysisType = "staticLinear"
            # Check whether a given ID is in the searched list
    def CheckID(tID,tIDList):
        if tID in tIDList:
            return 1
        else:
            return 0
    # Reset All
    def ResetAll():
        msaModel.Info.Reset()
        msaModel.Mat.Reset()
        msaModel.Sect.Reset()
        msaModel.Node.Reset()
        msaModel.Member.Reset()
        msaModel.Load.Reset()
        msaModel.Bound.Reset()
        msaModel.SpringModel.Reset()
        msaModel.SpringBoundary.Reset()
        msaModel.IterationInfo.Reset()

    # Member Properties
# Analysis Information
class AnaInfo:
    Type = "staticLinear"
    LF = 1.0
    LoadStep = 10
    MaxIter = 100
    Convergence = 0.001
    SolutionTech = "NL"
    def Modify(Type="staticLinear", LF=1.0, LoadStep=10, MaxIter=100, Convergence=0.001, SolutionTech="NL"):
        AnaInfo.Type = Type
        AnaInfo.LF = LF
        AnaInfo.LoadStep = LoadStep
        AnaInfo.MaxIter = MaxIter
        AnaInfo.Convergence = Convergence
        AnaInfo.SolutionTech = SolutionTech
# Recorded information in one time step
class AnaResOTS(object): # Analysis Result In One Time Step (OTS)
    def __init__(self):
        self.LoadFactor = []
        self.Dis = {}
        self.Force = {}
        self.Bound = {}
    # Record the analysis information in one load step
    def Add(self,tLF:float,tDis:list,tForce:list,tBound:list):
        self.LoadFactor.append(tLF)
        self.Dis[tLF] = tDis
        self.Force[tLF] = tForce
        self.Bound[tLF] = tBound
    # Modify the analysis results of the given load step
    def Modify(self,tLF:float,tDis:list,tForce:list,tBound:list):
        self.Dis[tLF] = tDis
        self.Force[tLF] = tForce
        self.Bound[tLF] = tBound
#==============================================================
#TEST UNIT
#==============================================================
# msaModel.Mat.Add(1,1,10,100)
# msaModel.Mat.Add(2,2,20,200)
# print(msaModel.Mat.ID,msaModel.Mat.E,msaModel.Mat.Fy,msaModel.Mat.G)
# msaModel.Sect.Add(1,1,1,1,1,1,1,1,1,1,1,1)
# msaModel.Sect.Add(2,2,2,2,2,2,2,2,2,2,2,2)
# print(msaModel.Sect.ID,msaModel.Sect.MatID)
# msaModel.Mat.Remove(2)
# print(msaModel.Sect.ID,msaModel.Sect.MatID)
# msaModel.Mat.Remove(1)
# print(msaModel.Sect.ID,msaModel.Sect.MatID)
# msaModel.Node.Add(1, 1,0.1,0.1,0.1)
# msaModel.Node.Add(2, 1,0.2,0.2,0.2)
# msaModel.Node.Add(3, 1,0.3,0.3,0.3)
# msaModel.Member.Add(1,1,2)
# msaModel.Member.Add(2,2,3)
# msaModel.Node.Remove(2)
# print(msaModel.Member.ID)
# print(msaModel.Member.ID,msaModel.Member.NodeID)
# msaModel.Node.Remove(1)
# print(msaModel.Member.ID,msaModel.Member.NodeID)
