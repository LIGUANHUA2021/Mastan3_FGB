import json, os
import numpy as np
from itertools import zip_longest  # For establishing dictionary
from PySide6.QtCore import QTime, QFileInfo

from gui.msasect.base.Model import msaModel, msaFEModel
from gui.msasect.ui.msgBox import showMesbox
##
from analysis.FESect.variables import Model as FEModel
##============================================================
## Import data file
##============================================================


class CMFile:
    def __init__(self, mw, parent=None):
        super().__init__(parent)
        self.mw = mw

    def ImportDataFile(mw, FileName):
        with open(FileName, 'r') as File:
            ImportData = json.load(File)
        msaModel.ResetAll()
        fileinfo = QFileInfo(FileName)
        tfilename = fileinfo.baseName()
        # DirFileName = fileinfo.absolutePath() + "/" + tfilename
        # # print("absoluteFilePath =", fileinfo.absoluteFilePath())
        # print("absolutePath =", fileinfo.absolutePath())
        # print("absolutePath =", DirFileName)

        msaModel.Information.ModelName = FileName  ## absolute FilePath
        msaModel.FileInfo.FileName = tfilename  ## the model file name
        CMFile.ReadMaterial(mw, np.array(ImportData["MATERIAL"]))
        CMFile.ReadPoint(mw, np.array(ImportData["POINT"]))
        CMFile.ReadSegment(mw, np.array(ImportData["SEGMENT"]))
        # print(msaModel.Segment.ID)
        # print(msaModel.Segment.SegThick)
        CMFile.ReadInfo(np.array(ImportData["INFORMATION"]))
        CMFile.ReadYSAnalInfo(mw, np.array(ImportData["YieldSAnalInfo"]))
        CMFile.ReadFiber(mw, np.array(ImportData["FIBER"]))
        # ReadSect(ImportData["SECTION"])
        # ReadLoad(ImportData["LOAD"])
        # ReadBound(ImportData["BOUND"])
        # ReadInfo(ImportData["MODELINFO"])
        # ReadIterInfo(ImportData["INTERATION"])
        return

    # def ReadMat(tMat):
    #     for key in tMat:
    #         tID = int(tMat[key]["E"])
    #         tE, tG, tFy = float(tMat[key]["E"]), float(tMat[key]["G"]), float(tMat[key]["Fy"])
    #         msaModel.Mat.Add(tID,tE,tG,tFy)
    #     return

    def ReadMaterial(mw, MaterialInfo):
        # print("MaterialInfo type = ",type(MaterialInfo))
        # print("MaterialInfo data = ", MaterialInfo)
        # print("MaterialInfo size = ", MaterialInfo.size)
        msaModel.Mat.Count = len(MaterialInfo)
        tID = np.fromiter(MaterialInfo[:, 0], float).astype('int').tolist()
        msaModel.Mat.ID = dict(zip_longest(tID, np.arange(msaModel.Mat.Count).tolist()))
        msaModel.Mat.E = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 1], float).tolist()))
        msaModel.Mat.G = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 2], float).tolist()))
        msaModel.Mat.nu = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 3], float).tolist()))
        msaModel.Mat.Fy = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 4], float).tolist()))
        msaModel.Mat.eu = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 5], float).tolist()))
        msaModel.Mat.Density = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 6], float).tolist()))
        if MaterialInfo.shape[1] >= 8:
            msaModel.Mat.Type = dict(zip_longest(tID, MaterialInfo[:, 7]))
    # def ReadPoint(tPoint):
    #     for key in tPoint:
    #         tID = int(key)
    #         tx, ty, tz = tPoint[key][0],tPoint[key][1],tPoint[key][2]
    #         msaModel.Point.Add(tID, tx, ty, tz)
    #     return

    def ReadPoint(mw, PointInfo):
        msaModel.Point.Count = len(PointInfo)
        tID = np.fromiter(PointInfo[:, 0], int).tolist()
        msaModel.Point.ID = dict(zip_longest(tID, np.arange(msaModel.Point.Count).tolist()))
        msaModel.Point.Yo = dict(zip_longest(tID, PointInfo[:, 1].tolist()))
        msaModel.Point.Zo = dict(zip_longest(tID, PointInfo[:, 2].tolist()))
        # print(PointInfo[:, 2])
        # print("type PointInfo[:, 2]= ",type(PointInfo[:, 2]))
        # print("size PointInfo[:, 2]= ", PointInfo.size)
        # print("Shape PointInfo[:, 2]= ", PointInfo.shape[1])
        if 4 < PointInfo.shape[1] <= 8:
            msaModel.Point.xDof = dict(zip_longest(tID, PointInfo[:, 3].tolist()))
            msaModel.Point.yDof = dict(zip_longest(tID, PointInfo[:, 4].tolist()))
            msaModel.Point.zDof = dict(zip_longest(tID, PointInfo[:, 5].tolist()))
            msaModel.Point.qDof = dict(zip_longest(tID, PointInfo[:, 6].tolist()))
            msaModel.Point.stress = dict(zip_longest(tID, PointInfo[:, 7].tolist()))
        else:
            msaModel.Point.xDof = dict(zip_longest(tID, [1]*len(PointInfo)))
            msaModel.Point.yDof = dict(zip_longest(tID, [1]*len(PointInfo)))
            msaModel.Point.zDof = dict(zip_longest(tID, [1]*len(PointInfo)))
            msaModel.Point.qDof = dict(zip_longest(tID, [1]*len(PointInfo)))
            msaModel.Point.stress = dict(zip_longest(tID, [0.0]*len(PointInfo)))

    # def ReadSegment(tSeg):
    #     for key in tSeg:
    #         tID = int(key)
    #         tMatID = tSeg[key]["Material"]
    #         tPointI, tPointJ = tSeg[key]["Point"][0], tSeg[key]["Point"][1]
    #         msaModel.Member.Add(tID, tMatID, tPointI, tPointJ)
    #     return

    def ReadSegment(mw, SegmInfo):
        msaModel.Segment.Count = len(SegmInfo)
        tID = np.fromiter(SegmInfo[:, 0], int).tolist()
        msaModel.Segment.ID = dict(zip_longest(tID, np.arange(msaModel.Segment.Count).tolist()))
        msaModel.Segment.MatID = dict(zip_longest(tID, np.fromiter(SegmInfo[:, 1], int).tolist()))
        msaModel.Segment.PointI = dict(zip_longest(tID, np.fromiter(SegmInfo[:, 2], int).tolist()))
        msaModel.Segment.PointJ = dict(zip_longest(tID, np.fromiter(SegmInfo[:, 3], int).tolist()))
        msaModel.Segment.SegThick = dict(zip_longest(tID, SegmInfo[:, 4].tolist()))
        msaModel.Segment.FiberNumL = dict(zip_longest(tID, [0] * msaModel.Segment.Count))
        msaModel.Segment.FiberNumT = dict(zip_longest(tID, [0] * msaModel.Segment.Count))
        msaModel.Segment.NodeNum = dict(zip_longest(tID, [0] * msaModel.Segment.Count))
        # print("Input datafile", msaModel.Segment.ID)

    def ReadInfo(tMInfo):
        tMInfoDict = dict(tMInfo)
        #msaModel.Information.ModelName = msaModel.FileInfo.FileName
        msaModel.Information.Version = tMInfoDict["Version"]
        msaModel.Information.CreatT = tMInfoDict["Date"]
        msaModel.Information.Description = tMInfoDict["Description"]
        return

    @classmethod
    def ReadYSAnalInfo(self, mw, tYSAnalInfo):
        # print("type tYSAnalInfo = ", type(tYSAnalInfo))
        # print("tYSAnalInfo = ", tYSAnalInfo)
        # print("tYSAnalInfo.size = ", tYSAnalInfo.size)
        tYSAnalInfo = dict(tYSAnalInfo)
        # print("tYSAnalInfo = ", tYSAnalInfo)
        msaModel.YieldSurfaceAnalInfo.PosNStep = tYSAnalInfo["PosNStep"]
        # print("msaModel.YieldSurfaceAnalInfo.PosNStep =", msaModel.YieldSurfaceAnalInfo.PosNStep)
        msaModel.YieldSurfaceAnalInfo.NegNStep = tYSAnalInfo["NegNStep"]
        msaModel.YieldSurfaceAnalInfo.MStep = tYSAnalInfo["MomentStep"]
        msaModel.YieldSurfaceAnalInfo.MaxNumIter = tYSAnalInfo["MaxNumIter"]
        msaModel.YieldSurfaceAnalInfo.ConvTol = tYSAnalInfo["ConvTol"]
        msaModel.YieldSurfaceAnalInfo.StrainAtValue = tYSAnalInfo["StrainAtValue"]
        msaModel.YieldSurfaceAnalInfo.SubAnalType = tYSAnalInfo["SubAnalType"]
        msaModel.YieldSurfaceAnalInfo.AxisSlctn = tYSAnalInfo["AxisSlctn"]

    @classmethod
    def ReadFiber(self, mw, tFiberInfo):
        if tFiberInfo.size == 0:
            #mw.StatusOutput.append(QTime.currentTime().toString() + (": There is no 'Fiber' data in input file!"))
            return
        msaModel.Fiber.Count = len(tFiberInfo)
        tID = np.fromiter(tFiberInfo[:, 0], int).tolist()
        msaModel.Fiber.ID = dict(zip_longest(tID, np.arange(msaModel.Fiber.Count).tolist()))
        msaModel.Fiber.Yc = dict(zip_longest(tID, tFiberInfo[:, 1].tolist()))
        msaModel.Fiber.Zc = dict(zip_longest(tID, tFiberInfo[:, 2].tolist()))
        msaModel.Fiber.FArea = dict(zip_longest(tID, tFiberInfo[:, 3].tolist()))
        msaModel.Fiber.FMatID = dict(zip_longest(tID, tFiberInfo[:, 4].tolist()))
        msaModel.Fiber.NodeI = dict(zip_longest(tID, [0] * msaModel.Fiber.Count))
        msaModel.Fiber.NodeJ = dict(zip_longest(tID, [0] * msaModel.Fiber.Count))
        msaModel.Fiber.NodeK = dict(zip_longest(tID, [0] * msaModel.Fiber.Count))
        msaModel.Fiber.NodeL = dict(zip_longest(tID, [0] * msaModel.Fiber.Count))
        # print("msaModel.Fiber.ID = ", msaModel.Fiber.ID)


    def SaveDataFile(FileName, tFlag):
        SavedModel = {"INFORMATION":{},"MATERIAL": {}, "POINT":{}, "SEGMENT": {}, "YieldSAnalInfo":[], "FIBER":[]}
        SavedModel["MATERIAL"] = CMFile.SaveMat()
        SavedModel["POINT"] = CMFile.SavePoint()
        # print("Save file Checkkkkkk", msaModel.Segment.ID)
        SavedModel["SEGMENT"] = CMFile.SaveSegment()
        SavedModel["INFORMATION"] = CMFile.SaveInfo()
        if tFlag == 2:
            SavedModel["YieldSAnalInfo"] = CMFile.SaveYieldSAnalInfo()
            SavedModel["FIBER"] = CMFile.SaveFiber()
        # SavedModel["INTERATION"] = SaveIterInfo()
        # print("Check ModelName000000 =", msaModel.Information.ModelName)
        # print("Original Filename9999999 =", FileName)
        with open(FileName, 'w') as fp:
            fp.write(json.dumps(SavedModel, indent=4))
            fp.flush()
        return

    def SaveMCurvaDataFile(FileName):
        ##
        SavedModel = {"GENERAL":{}, "MATERIAL": {}, "COMPONENT":{}, "ANALYSIS": {}}
        SavedModel["GENERAL"] = CMFile.SaveMCGeneInfo()
        SavedModel["MATERIAL"] = CMFile.SaveMCMat()
        SavedModel["COMPONENT"] = CMFile.SaveMCComp()
        SavedModel["ANALYSIS"] = CMFile.SaveMCAnal()
        ##
        with open(FileName, 'w') as fp:
            fp.write(json.dumps(SavedModel, indent=4))
            fp.flush()
        return

    @classmethod
    def SaveMCGeneInfo(cls):
        msaModel.Information.Save()
        tInfo = msaModel.Information
        tnameInfo = msaModel.FileInfo
        Output = [["Version", tInfo.Version], ["Unit", "N,mm"], ["ModelFileName", tnameInfo.FileName],
                  ["SectionName", "Section 1"],
                  ["SectionType", 1]]  ## 1 For steel

        return Output

    @classmethod
    def SaveMCMat(cls):
        tMat = msaModel.Mat
        OutputMat = []
        for ii in tMat.ID:
            iMat = [ii, "S275", 1, 1, 0, tMat.E[ii], tMat.nu[ii], tMat.G[ii], tMat.Fy[ii], tMat.eu[ii], tMat.Fy[ii], tMat.eu[ii], {"MATCURVE":[[]]}]
            OutputMat.append(iMat)
        return OutputMat

    @classmethod
    def SaveMCComp(cls):
        OutputComp = []
        OutputFiber = []
        tMat = msaModel.Mat
        ##
        tFiber = msaModel.Fiber
        for ii in tMat.ID:
            if tMat.Type[ii] == "S":
                tComType = 1
            ##
            if tFiber.ID:
                for jj in tFiber.ID:
                    if tFiber.FMatID[jj]==ii:
                        iFiber = [jj, tFiber.Yc[jj], tFiber.Zc[jj], tFiber.FArea[jj]]
                        OutputFiber.append(iFiber)
            ##
            iComp = [ii, "Default Name", tComType, ii, {"Fibers": OutputFiber}]
            OutputComp.append(iComp)
        return OutputComp

    @classmethod
    def SaveMCAnal(cls):
        OutPutMCAnal = []
        tMCurvaAnalInfo = msaModel.MomentCurvaAnalInfo
        if tMCurvaAnalInfo.SubAnalType == 1:
            tAnaName = "My Curvature"
        else:
            tAnaName = "Mz Curvature"
        OutPutMCAnal = [["AnaName", tAnaName], ["AnaIterTimes", tMCurvaAnalInfo.MaxNumIter], ["AnaConver", tMCurvaAnalInfo.ConvTol],
                        ["AnaType", tAnaName], ["RunType", 0], ["CurveType", 0], ["AxisSlctn", tMCurvaAnalInfo.AxisSlctn], ["AxialStep", 20],
                        ["MomentStep", tMCurvaAnalInfo.MomentStep],["StrainControlType", 0],["AnalysisAxialLoad", tMCurvaAnalInfo.Anap], ["AnalAxialLoadType", tMCurvaAnalInfo.AxialLoadType]]

        return OutPutMCAnal

    @classmethod
    def SaveMat(cls):
        tMat = msaModel.Mat
        OutputMat = []
        # print("Material test", tMat)
        # print("Material test", tMat.ID)
        for ii in tMat.ID:
            # print("Mat ID", tMat.ID)
            # print("Type ii", type(ii))
            # print("int ii = ", ii)
            iMat = [ii, tMat.E[ii], tMat.G[ii], tMat.nu[ii], tMat.Fy[ii], tMat.eu[ii], tMat.Density[ii], tMat.Type[ii]]
            OutputMat.append(iMat)
        return OutputMat

    @classmethod
    def SavePoint(cls):
        tPoint = msaModel.Point
        # print(tPoint)
        # print(tPoint.ID)
        # print(type(tPoint))
        OutputPoint = []
        for ii in tPoint.ID:
            # iPoint = [ii, tPoint.Yo[ii], tPoint.Zo[ii], tPoint.xDof[ii], tPoint.yDof[ii], tPoint.zDof[ii], tPoint.qDof[ii], tPoint.stress[ii]]
            iPoint = [ii, tPoint.Yo[ii], tPoint.Zo[ii], tPoint.stress[ii]]
            OutputPoint.append(iPoint)
        return OutputPoint

    @classmethod
    def SaveSegment(cls):
        tSeg = msaModel.Segment
        OutputSeg = []
        # print("Segment ID = ", tSeg.ID)
        # print("Segment Thickness = ", tSeg.SegThick)
        for ii in tSeg.ID:
            iseg = [ii, tSeg.MatID[ii], tSeg.PointI[ii], tSeg.PointJ[ii], tSeg.SegThick[ii]]
            # print(iseg)
            OutputSeg.append(iseg)
        #OutputSeg = np.array(OutputSeg)
        # print(OutputSeg)
        return OutputSeg

    @classmethod
    def SaveInfo(cls):
        msaModel.Information.Save()
        tInfo = msaModel.Information
        tnameInfo = msaModel.FileInfo
        Output = [["ModelFileName", tnameInfo.FileName], ["Version", tInfo.Version], ["Date", tInfo.CreatT], ["LastRevised", tInfo.LastSavedT],
                  ["Description", tInfo.Description]]
        # Output = np.array(list(tInfo.items()))
        #     #           ["Description", tInfo.Description])
        # Output = np.array(["ModelName", tInfo.ModelName], ["Version", tInfo.Version], ["Date", tInfo.CreatT], ["LastRevised", tInfo.LastSavedT],\
        #           ["Description", tInfo.Description])
        return Output

    @classmethod
    def SaveYieldSAnalInfo(cls):
        tYSAnalInfo = msaModel.YieldSurfaceAnalInfo
        Output = []
        if tYSAnalInfo.PosNStep:
            Output = [["PosNStep", tYSAnalInfo.PosNStep], ["NegNStep", tYSAnalInfo.NegNStep], ["MomentStep", tYSAnalInfo.MStep],
                      ["MaxNumIter", tYSAnalInfo.MaxNumIter], ["ConvTol", tYSAnalInfo.ConvTol], ["StrainAtValue", tYSAnalInfo.StrainAtValue],
                      ["BStrainControl", tYSAnalInfo.BStrainControl], ["SubAnalType", tYSAnalInfo.SubAnalType], ["AxisSlctn", tYSAnalInfo.AxisSlctn]]
        return Output

    @classmethod
    def SaveFiber(cls):
        tFiber = msaModel.Fiber
        OutPutFiber = []
        if tFiber.ID:
            for ii in tFiber.ID:
                iFiber = [ii, tFiber.Yc[ii], tFiber.Zc[ii], tFiber.FArea[ii], tFiber.FMatID[ii]]
                OutPutFiber.append(iFiber)
        return OutPutFiber


class FEFile:
    def ImportDataFile(mw, FileName):
        with open(FileName, 'r') as File:
            ImportData = json.load(File)
        msaFEModel.ResetAll()

        fileinfo = QFileInfo(FileName)
        tfilename = fileinfo.baseName()
        msaFEModel.Information.ModelName = FileName  # absolute file path
        msaFEModel.FileInfo.FileName = tfilename  # the model file name

        FEFile.ReadMaterial(np.array(ImportData["MATERIAL"]))
        FEFile.ReadPoint(np.array(ImportData["POINT"]))
        FEFile.ReadOutline(np.array(ImportData["OUTLINE"]))
        FEFile.ReadLoop(np.array(ImportData["LOOP"], dtype=object))
        FEFile.ReadGroup(np.array(ImportData["GROUP"], dtype=object))
        FEFile.ReadInfo(np.array(ImportData["INFORMATION"]))
        return

    def ReadMaterial(MaterialInfo):
        msaFEModel.Mat.Count = len(MaterialInfo)
        tID = np.fromiter(MaterialInfo[:, 0], float).astype('int').tolist()
        msaFEModel.Mat.ID = dict(zip_longest(tID, np.arange(msaFEModel.Mat.Count).tolist()))
        msaFEModel.Mat.E = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 1], float).tolist()))
        msaFEModel.Mat.G = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 2], float).tolist()))
        msaFEModel.Mat.nu = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 3], float).tolist()))
        msaFEModel.Mat.Fy = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 4], float).tolist()))
        msaFEModel.Mat.eu = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 5], float).tolist()))
        msaFEModel.Mat.Density = dict(zip_longest(tID, np.fromiter(MaterialInfo[:, 6], float).tolist()))
        if MaterialInfo.shape[1] >= 8:
            msaFEModel.Mat.Type = dict(zip_longest(tID, MaterialInfo[:, 7]))

    def ReadPoint(PointInfo):
        msaFEModel.Point.Count = len(PointInfo)
        tID = np.fromiter(PointInfo[:, 0], int).tolist()
        msaFEModel.Point.ID = dict(zip_longest(tID, np.arange(msaFEModel.Point.Count).tolist()))
        msaFEModel.Point.Yo = dict(zip_longest(tID, PointInfo[:, 1].tolist()))
        msaFEModel.Point.Zo = dict(zip_longest(tID, PointInfo[:, 2].tolist()))

    def ReadOutline(OutlineInfo):
        msaFEModel.Outline.Count = len(OutlineInfo)
        tID = np.fromiter(OutlineInfo[:, 0], float).astype('int')
        msaFEModel.Outline.ID = dict(zip_longest(tID, np.arange(msaFEModel.Outline.Count).tolist()))
        msaFEModel.Outline.GroupID = dict(zip_longest(tID, np.fromiter(OutlineInfo[:, 1], int).tolist()))
        msaFEModel.Outline.LoopID = dict(zip_longest(tID, np.fromiter(OutlineInfo[:, 2], int).tolist()))
        msaFEModel.Outline.Type = dict(zip_longest(tID, OutlineInfo[:, 3]))
        msaFEModel.Outline.PointI = dict(zip_longest(tID, np.fromiter(OutlineInfo[:, 4], int).tolist()))
        msaFEModel.Outline.PointJ = dict(zip_longest(tID, np.fromiter(OutlineInfo[:, 5], int).tolist()))

    def ReadLoop(LoopInfo):
        msaFEModel.Loop.Count = len(LoopInfo)
        tID = np.fromiter(LoopInfo[:, 0], int)
        msaFEModel.Loop.ID = dict(zip_longest(tID, np.arange(msaFEModel.Loop.Count).tolist()))
        msaFEModel.Loop.OutlineID = dict(zip_longest(tID, LoopInfo[:, 1]))
        for i in msaFEModel.Loop.ID:
            msaFEModel.GetLoopPointID(i)

    def ReadGroup(GroupInfo):
        msaFEModel.Group.Count = len(GroupInfo)
        tID = np.fromiter(GroupInfo[:, 0], int)
        msaFEModel.Group.ID = dict(zip_longest(tID, np.arange(msaFEModel.Group.Count).tolist()))
        msaFEModel.Group.MatID = dict(zip_longest(tID, np.fromiter(GroupInfo[:, 1], int).tolist()))
        msaFEModel.Group.LoopID = dict(zip_longest(tID, GroupInfo[:, 2]))

    def ReadInfo(tMInfo):
        tMInfoDict= dict(tMInfo)
        msaFEModel.Information.Version = tMInfoDict["Version"]
        msaFEModel.Information.CreatT = tMInfoDict["Date"]
        msaFEModel.Information.Description = tMInfoDict["Description"]
        return

    def SaveDataFile(FileName, tFlag=1):
        SavedModel = {"INFORMATION":{},"MATERIAL": {}, "POINT":{}, "OUTLINE": {}, "LOOP": {}, "GROUP": {}, "YIELDSANALINFO": {}}
        SavedModel["MATERIAL"] = FEFile.SaveMat()
        SavedModel["POINT"] = FEFile.SavePoint()
        SavedModel["OUTLINE"] = FEFile.SaveOutline()
        SavedModel["LOOP"] = FEFile.SaveLoop()
        SavedModel["GROUP"] = FEFile.SaveGroup()
        SavedModel["INFORMATION"] = FEFile.SaveInfo()
        if tFlag == 2:
            SavedModel["YIELDSANALINFO"] = FEFile.SaveYieldSAnalInfo()
        with open(FileName, 'w') as fp:
            fp.write(json.dumps(SavedModel, indent=4))
            fp.flush()
        return

    @classmethod
    def SaveMat(cls):
        tMat = msaFEModel.Mat
        OutputMat = []
        for ii in tMat.ID:
            iMat = [ii, tMat.E[ii], tMat.G[ii], tMat.nu[ii], tMat.Fy[ii], tMat.eu[ii], tMat.Density[ii], tMat.Type[ii]]
            OutputMat.append(iMat)
        return OutputMat

    @classmethod
    def SavePoint(cls):
        tPoint = msaFEModel.Point
        OutputPoint = []
        for ii in tPoint.ID:
            iPoint = [int(ii), tPoint.Yo[ii], tPoint.Zo[ii]]
            OutputPoint.append(iPoint)
        return OutputPoint

    @classmethod
    def SaveOutline(cls):
        tLine = msaFEModel.Outline
        OutputLine = []
        for ii in tLine.ID:
            iLine = [int(ii), int(tLine.GroupID[ii]), int(tLine.LoopID[ii]), tLine.Type[ii], int(tLine.PointI[ii]), int(tLine.PointJ[ii])]
            OutputLine.append(iLine)
        return OutputLine

    @classmethod
    def SaveLoop(cls):
        tLoop = msaFEModel.Loop
        OutputLoop = []
        for ii in tLoop.ID:
            iLoop = [int(ii), [int(_) for _ in tLoop.OutlineID[ii]]]
            OutputLoop.append(iLoop)
        return OutputLoop

    @classmethod
    def SaveGroup(cls):
        tGroup = msaFEModel.Group
        OutputGroup = []
        for ii in tGroup.ID:
            iGroup = [int(ii), int(tGroup.MatID[ii]), [int(_) for _ in tGroup.LoopID[ii]]]
            OutputGroup.append(iGroup)
        return OutputGroup

    @classmethod
    def SaveInfo(cls):
        msaFEModel.Information.Save()
        tInfo = msaFEModel.Information
        Output = [["ModelName", tInfo.ModelName], ["Version", tInfo.Version],["Date", tInfo.CreatT],["LastRevised", tInfo.LastSavedT],
                  ["Description", tInfo.Description]]
        return Output

    @classmethod
    def SaveYieldSAnalInfo(cls):
        tYSAnalInfo = msaFEModel.YieldSurfaceAnalInfo
        Output = []
        if tYSAnalInfo.PosNStep:
            Output = [["PosNStep", tYSAnalInfo.PosNStep], ["NegNStep", tYSAnalInfo.NegNStep],
                      ["MomentStep", tYSAnalInfo.MStep],
                      ["MaxNumIter", tYSAnalInfo.MaxNumIter], ["ConvTol", tYSAnalInfo.ConvTol],
                      ["StrainAtValue", tYSAnalInfo.StrainAtValue],
                      ["BStrainControl", tYSAnalInfo.BStrainControl], ["SubAnalType", tYSAnalInfo.SubAnalType],
                      ["AxisSlctn", tYSAnalInfo.AxisSlctn]]
        return Output

    def SaveMCurvaDataFile(FileName):
        ##
        SavedModel = {"GENERAL":{}, "MATERIAL": {}, "COMPONENT":{}, "ANALYSIS": {}}
        SavedModel["GENERAL"] = FEFile.SaveMCGeneInfo()
        SavedModel["MATERIAL"] = FEFile.SaveMCMat()
        SavedModel["COMPONENT"] = FEFile.SaveMCComp()
        SavedModel["ANALYSIS"] = FEFile.SaveMCAnal()
        ##
        with open(FileName, 'w') as fp:
            fp.write(json.dumps(SavedModel, indent=4))
            fp.flush()
        return

    def SaveCompSPDataFile(FileName):
        ##
        SavedModel = {"GENERAL":{}, "MATERIAL": {}, "COMPONENT":{}, "ANALYSIS": {}}
        SavedModel["GENERAL"] = FEFile.SaveMCGeneInfo()
        SavedModel["MATERIAL"] = FEFile.SaveMCMat()
        SavedModel["COMPONENT"] = FEFile.SaveMCComp()
        SavedModel["ANALYSIS"] = FEFile.SaveSPAnal()
        ##
        with open(FileName, 'w') as fp:
            fp.write(json.dumps(SavedModel, indent=4))
            fp.flush()
        return

    @classmethod
    def SaveMCGeneInfo(cls):
        msaFEModel.Information.Save()
        tInfo = msaFEModel.Information
        tnameInfo = msaFEModel.FileInfo
        Output = [["Version", tInfo.Version], ["Unit", "N,mm"], ["ModelFileName", tnameInfo.FileName],
                  ["SectionName", "Section 1"],
                  ["SectionType", 1]]  ## 1 For steel

        return Output

    @classmethod
    def SaveMCMat(cls):
        tMat = msaFEModel.Mat
        OutputMat = []
        for ii in tMat.ID:
            iMat = [ii, "S275", 1, 1, 0, tMat.E[ii], tMat.nu[ii], tMat.G[ii], tMat.Fy[ii], tMat.eu[ii], tMat.Fy[ii], tMat.eu[ii], {"MATCURVE":[[]]}]
            OutputMat.append(iMat)
        return OutputMat

    @classmethod
    def SaveMCComp(cls):
        OutputComp = []
        OutputFiber = []
        tMat = msaFEModel.Mat
        ##
        tFiber = FEModel.Fiber
        for ii in tMat.ID:
            if tMat.Type[ii] == "S":
                tComType = 1
            ##
            if tFiber.ID:
                for jj in tFiber.ID:
                    if tFiber.MaterialID[jj]==ii:
                        iFiber = [jj, tFiber.cy[jj], tFiber.cz[jj], tFiber.Area[jj]]
                        OutputFiber.append(iFiber)
            ##
            iComp = [ii, "Default", 1, ii, {"Fibers": OutputFiber}]
            OutputComp.append(iComp)
        return OutputComp

    @classmethod
    def SaveMCAnal(cls):
        OutPutMCAnal = []
        tMCurvaAnalInfo = msaFEModel.MomentCurvaAnalInfo
        if tMCurvaAnalInfo.SubAnalType == 1:
            tAnaName = "My Curvature"
        else:
            tAnaName = "Mz Curvature"
        OutPutMCAnal = [["AnaName", tAnaName], ["AnaIterTimes", tMCurvaAnalInfo.MaxNumIter], ["AnaConver", tMCurvaAnalInfo.ConvTol],
                        ["AnaType", tAnaName], ["RunType", 0], ["CurveType", 0], ["AxisSlctn", tMCurvaAnalInfo.AxisSlctn], ["AxialStep", 20],
                        ["MomentStep", tMCurvaAnalInfo.MomentStep], ["StrainControlType", 0], ["AnalysisAxialLoad", tMCurvaAnalInfo.Anap], ["AnalAxialLoadType", tMCurvaAnalInfo.AxialLoadType]]


        return OutPutMCAnal

    @classmethod
    def SaveSPAnal(cls):
        OutPutSPAnal = []
        tSPAnalInfo = msaFEModel.SectPAnalInfo
        # if tMCurvaAnalInfo.SubAnalType == 1:
        #     tAnaName = "My Curvature"
        # else:
        #     tAnaName = "Mz Curvature"
        OutPutSPAnal = [["AnaName", "SP"], ["AnaIterTimes", 300],
                        ["AnaConver", 0.01],
                        ["AnaType", "SP"], ["RunType", 0], ["CurveType", 0],
                        ["AxisSlctn", 1], ["AxialStep", 20],
                        ["MomentStep", 100], ["StrainControlType", tSPAnalInfo.StrnConT], ["StrainatValue", tSPAnalInfo.StrnatVal],
                        ["AnalysisAxialLoad", 0.0],
                        ["AnalAxialLoadType", 1],
                        ["RefMatID", tSPAnalInfo.RefMatID], ["User-Defined_E", tSPAnalInfo.UDE], ["User-Defined_PR", tSPAnalInfo.UDPR],
                        ["User-Defined_fy", tSPAnalInfo.UDfy], ["User-Defined_eu", tSPAnalInfo.UDeu]]
        ##
        return OutPutSPAnal