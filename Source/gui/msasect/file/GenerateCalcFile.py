import json
from gui.msasect.base.Model import msaModel, msaFEModel

class CMSect:
    def GenerateCalcFile(FileName):
        CalcModel = {}
        CalcModel["INFORMATION"] = CMSect.GetINFORMATION()
        CalcModel["MATERIAL"] = CMSect.GetMATERIAL()
        CalcModel["POINT"] = CMSect.GetPOINT()
        CalcModel["SEGMENT"] = CMSect.GetSEGMENT()
        # CalcModel["ANALYSIS"] = GetANALYSIS()
        with open(FileName, "w") as fp:
            fp.write(json.dumps(CalcModel, indent=4))
        return CalcModel

    @classmethod
    def GetINFORMATION(cls):
        INFORMATION = []
        Info = msaModel.Information
        INFORMATION.append(["Version", Info.Version])
        INFORMATION.append(["Date", Info.LastSavedT])
        INFORMATION.append(["Description", Info.Description])
        return INFORMATION

    @classmethod
    def GetMATERIAL(cls):
        MATERIAL = []
        Mat = msaModel.Mat
        for ii in Mat.ID:
            MATERIAL.append([ii, Mat.E[ii], Mat.G[ii], Mat.nu[ii], Mat.Fy[ii], Mat.eu[ii], Mat.Density[ii]])
            print("Material properties = ",[ii, Mat.E[ii], Mat.G[ii], Mat.nu[ii], Mat.Fy[ii], Mat.eu[ii], Mat.Density[ii]])
        return MATERIAL

    @classmethod
    def GetPOINT(cls):
        POINT = []
        Point = msaModel.Point
        for ii in Point.ID:
            POINT.append([ii, Point.Yo[ii], Point.Zo[ii]])
        return POINT

    @classmethod
    def GetSEGMENT(cls):
        SEGMENT = []
        Segment = msaModel.Segment
        for ii in Segment.ID:
            tbeta = 0
            SEGMENT.append([ii, Segment.MatID[ii], Segment.PointI[ii], Segment.PointJ[ii], Segment.SegThick[ii]])
        return SEGMENT


class FESect:
    def GenerateCalcFile(FileName):
        CalcModel = {}
        CalcModel["INFORMATION"] = FESect.GetINFORMATION()
        CalcModel["MATERIAL"] = FESect.GetMATERIAL()
        CalcModel["POINT"] = FESect.GetPOINT()
        CalcModel["OUTLINE"] = FESect.GetSEGMENT()
        CalcModel["GROUP"] = FESect.GetGROUP()
        # CalcModel["ANALYSIS"] = GetANALYSIS()
        with open(FileName, "w") as fp:
            fp.write(json.dumps(CalcModel, indent=4))
        return CalcModel

    @classmethod
    def GetINFORMATION(cls):
        INFORMATION = []
        Info = msaModel.Information
        INFORMATION.append(["Version", Info.Version])
        INFORMATION.append(["Date", Info.LastSavedT])
        INFORMATION.append(["Description", Info.Description])
        return INFORMATION

    @classmethod
    def GetMATERIAL(cls):
        MATERIAL = []
        Mat = msaModel.Mat
        for ii in Mat.ID:
            MATERIAL.append([ii, Mat.E[ii], Mat.G[ii], Mat.nu[ii], Mat.Fy[ii], Mat.eu[ii], Mat.Density[ii]])
            print("Material properties = ",
                  [ii, Mat.E[ii], Mat.G[ii], Mat.nu[ii], Mat.Fy[ii], Mat.eu[ii], Mat.Density[ii]])
        return MATERIAL

    @classmethod
    def GetPOINT(cls):
        POINT = []
        Point = msaModel.Point
        for ii in Point.ID:
            POINT.append([ii, Point.Yo[ii], Point.Zo[ii]])
        return POINT

    @classmethod
    def GetSEGMENT(cls):
        SEGMENT = []
        Segment = msaModel.Segment
        for ii in Segment.ID:
            tbeta = 0
            SEGMENT.append([ii, Segment.MatID[ii], Segment.PointI[ii], Segment.PointJ[ii], Segment.SegThick[ii]])
        return SEGMENT

    @classmethod
    def GetGROUP(cls):
        GROUP = []
        Segment = msaModel.Segment
        for ii in Segment.ID:
            tbeta = 0
            GROUP.append([ii, Segment.MatID[ii], Segment.PointI[ii], Segment.PointJ[ii], Segment.SegThick[ii]])
        return GROUP