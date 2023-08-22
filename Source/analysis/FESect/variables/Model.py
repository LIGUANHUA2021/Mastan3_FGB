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
# =========================================================================================
# Import standard libraries
# =========================================================================================
from itertools import zip_longest
import numpy as np
from collections import defaultdict
# =========================================================================================
# Import internal functions
from analysis.FESect.element import Tri3


Division = '========================================================================================='


class Material:
    Count = 0
    ID = {}
    E = {}
    nu = {}
    G = {}
    Fy = {}
    Density = {}
    eu = {}
    ##
    Gra = 0
    Gra_ID = {}
    E_ref = {}
    E_begin = {}
    E_end = {}
    Gra_ang = {}
    Gra_law = {}
    Gra_Type  = {}
    GColor = {}
    k = {}

    MaxTenStrn = {}  ## Maximum tension strain
    MaxComStrn = {}  ## Maximum Compressive strain
    MatProperty = {}  ## 1 for simple  properties; 2 for advanced properties
    Type = {}  ## "S" for steel; "C" for concret; "R" for rebar; "UD" for user-defined

    @classmethod
    def Reset(cls):
        Material.Count = 0
        Material.ID = {}
        Material.E = {}
        Material.nu = {}
        Material.G = {}
        Material.Fy = {}
        Material.Density = {}
        Material.eu = {}
        ##
        Material.MaxTenStrn = {}
        Material.MaxComStrn = {}
        Material.MatProperty = {}
        Material.Type = {}
        Material.Gra = 0
        Material.Gra_ID = {}
        Material.E_ref = {}
        Material.E_begin = {}
        Material.E_end = {}
        Material.Gra_ang = {}
        Material.Gra_law = {}
        Material.Gra_Type = {}
        Material.GColor = {}
        Material.k = {}
        return

    def readMat(MatInfo):
        Material.Count = MatInfo.Count
        Material.ID = MatInfo.ID
        Material.E = MatInfo.E
        Material.G = MatInfo.G
        Material.nu = MatInfo.nu
        Material.Fy = MatInfo.Fy
        Material.Density = MatInfo.Density
        Material.eu = MatInfo.eu
        Material.Gra = MatInfo.Gra
        Material.Gra_ID = MatInfo.Gra_ID
        Material.E_ref = MatInfo.E_ref
        Material.E_begin = MatInfo.E_begin
        Material.E_end = MatInfo.E_end
        Material.Gra_ang = MatInfo.Gra_ang
        Material.Gra_law = MatInfo.Gra_law
        Material.Gra_Type = MatInfo.Gra_Type
        Material.GColor = MatInfo.GColor
        Material.k = MatInfo.k

        Material.MaxComStrn = {key: value for key, value in MatInfo.eu.items()}
        Material.MaxTenStrn = {key: -value for key, value in MatInfo.eu.items()}
        Material.Type = {key: "S" for key in MatInfo.ID}
        Material.MatProperty = {key: 1 for key in MatInfo.ID}

        return


class Point:
    Count = 0
    ID = {}
    Y = {}
    Z = {}

    @classmethod
    def Reset(cls):
        Point.Count = 0
        Point.ID = {}
        Point.Y = {}
        Point.Z = {}
        return

    def readPoint(PointInfo):
        Point.Count = PointInfo.Count
        Point.ID = PointInfo.ID
        Point.Y = PointInfo.Yo
        Point.Z = PointInfo.Zo
        return


class Outline:
    Count = 0
    ID = {}
    GroupID = {}
    Type = {}
    Point1 = {}
    Point2 = {}

    @classmethod
    def Reset(cls):
        Outline.Count = 0
        Outline.ID = {}
        Outline.GroupID = {}
        Outline.Type = {}
        Outline.Point1 = {}
        Outline.Point2 = {}
        return


    def readOl(OutlineInfo):
        Outline.Count = OutlineInfo.Count
        Outline.ID = OutlineInfo.ID
        Outline.GroupID = OutlineInfo.GroupID
        Outline.Type = OutlineInfo.Type
        Outline.Point1 = OutlineInfo.PointI
        Outline.Point2 = OutlineInfo.PointJ
        return


class Group:
    Count = 0
    ID = {}
    MaterialID = {}

    @classmethod
    def Reset(cls):
        Group.Count = 0
        Group.ID = {}
        Group.MaterialID = {}
        return


    def readGroup(GroupInfo):
        Group.Count = GroupInfo.Count
        Group.ID = GroupInfo.ID
        Group.MaterialID = GroupInfo.MatID
        return


class Analysis:
    RunAutoMesh = 0
    FiberSize = 0
    Element = ""
    GaussPoints = 0
    BasicProperties = 0
    StressAnalysis = 0
    BucklingAnalysis = 0
    DynamicAnalysis = 0
    HeatTransfer = 0
    YieldSurface = 0
    MomentCurvature = 0
    mat_ref = 1
    E_ref = 0
    nu_ref = 0
    G_ref = 0
    fy_ref = 0

    @classmethod
    def Reset(cls):
        Analysis.FiberSize = 0
        Analysis.Element = ""
        Analysis.GaussPoints = 0
        Analysis.BasicProperties = 0
        Analysis.StressAnalysis = 0
        Analysis.BucklingAnalysis = 0
        Analysis.DynamicAnalysis = 0
        Analysis.HeatTransfer = 0
        Analysis.YieldSurface = 0
        Analysis.MomentCurvature = 0
        Analysis.mat_ref = 1
        Analysis.E_ref = 0
        Analysis.nu_ref = 0
        Analysis.G_ref = 0
        Analysis.fy_ref = 0
        return


    def readAnalysis(AnalysisInfo):
        Analysis.FiberSize = AnalysisInfo["Fiber Size"]
        Analysis.Element = AnalysisInfo["Element"]
        Analysis.GaussPoints = AnalysisInfo["Gauss Points"]
        Analysis.BasicProperties = AnalysisInfo["Basic Properties"]
        Analysis.StressAnalysis = AnalysisInfo["Stress Analysis"]
        Analysis.BucklingAnalysis = AnalysisInfo["Buckling Analysis"]
        Analysis.DynamicAnalysis = AnalysisInfo["Dynamic Analysis"]
        Analysis.HeatTransfer = AnalysisInfo["Heat Transfer"]
        Analysis.YieldSurface = AnalysisInfo["Yield Surface"]
        Analysis.MomentCurvature = AnalysisInfo["Moment Curvature"]
        return


class Node:
    Count = 0
    ID = {}
    Y = {}
    Z = {}
    y = {}
    z = {}
    V = {}
    W = {}
    Node_E = {}
    Omega = {}

    @classmethod
    def Reset(cls):
        Node.Count = 0
        Node.ID = {}
        Node.Y = {}
        Node.Z = {}
        Node.y = {}
        Node.z = {}
        Node.V = {}
        Node.W = {}
        Node.Node_E = {}
        Node.Omega = {}
        return

    def readNode(NodeInfo):
        Node.Count = len(NodeInfo)
        Node.ID = dict(enumerate(np.arange(Node.Count)))
        Node.Y = dict(enumerate(NodeInfo[:, 1]))
        Node.Z = dict(enumerate(NodeInfo[:, 0]))
        return


    def ReadLocal(cy, cz):
        ty = np.zeros(Node.Count)
        tz = np.zeros(Node.Count)

        for i in Node.ID:
            ty[i] = Node.Y[i] - cy
            tz[i] = Node.Z[i] - cz

        Node.y = dict(zip_longest(Node.ID.keys(), ty))
        Node.z = dict(zip_longest(Node.ID.keys(), tz))


    def GetPrinciple(Theta):
        tV = np.zeros(Node.Count)
        tW = np.zeros(Node.Count)

        for i in Node.ID:
            tV[i] = (Node.y[i] * np.cos(Theta) - Node.z[i] * np.sin(Theta))
            tW[i] = (Node.y[i] * np.sin(Theta) + Node.z[i] * np.cos(Theta))

        Node.V = dict(zip_longest(Node.ID.keys(), tV))
        Node.W = dict(zip_longest(Node.ID.keys(), tW))
        return

    @staticmethod
    def ReadOmega(tOmega):
        Node.Omega = dict(zip_longest(Node.ID.keys(), tOmega))
        return

    @staticmethod
    def ReadShearFunction(tPhi, tPsi):
        Node.Phi = dict(zip_longest(Node.ID.keys(), tPhi))
        Node.Psi = dict(zip_longest(Node.ID.keys(), tPsi))
        return

    @staticmethod
    def ReadPrincipleShearFunction(tPhip, tPsip):
        Node.Phip = dict(zip_longest(Node.ID.keys(), tPhip))
        Node.Psip = dict(zip_longest(Node.ID.keys(), tPsip))
        return

    def find_min_max_indexes(lst):
        min_value = min(lst)
        max_value = max(lst)
        min_index = lst.index(min_value)
        max_index = lst.index(max_value)
        return min_index, max_index

    # input angle, E_begin, E_end, law, k
    @staticmethod
    def Calculate_E(y, z, y_begin, z_begin, y_end, z_end, angle, E_begin, E_end, law, k, Type):
        if Type == 0:
            B = np.array([np.cos(angle), np.sin(angle)])
            # A = np.array([y - y_begin, z- z_begin])
            # A_length = np.linalg.norm(A)
            D = (y_end - y_begin) * np.cos(angle) + (z_end - z_begin) * np.sin(angle)
            distance = (y - y_begin) * np.cos(angle) + (z - z_begin) * np.sin(angle)

            if law == 0:
                Node_E = E_begin + (E_end - E_begin) * (distance / D) ** k
            elif law == 1:
                Node_E = E_begin * np.exp((distance / D) * np.log(E_end / E_begin))
            elif law == 2:
                if distance <= D / 2:
                    Node_E = E_begin + (E_end - E_begin) * (distance / D) ** k
                else:
                    Node_E = E_begin + (E_end - E_begin) * (1 - (1-distance / D) ** k)  # k > 1
            elif law == 3:
                Node_E = E_end * (distance / D) ** k + E_begin * (1 - (distance / D) ** k)

        else:
            D = np.sqrt(y_end ** 2 + z_end ** 2) - np.sqrt(y_begin ** 2 + z_begin ** 2)
            distance = np.sqrt(y ** 2 + z ** 2) - np.sqrt(y_begin ** 2 + z_begin ** 2)
            if distance == 0:
                Node_E = E_begin
            elif distance == D:
                Node_E = E_end
            else:
                if law == 0:
                    Node_E = E_begin + (E_end - E_begin) * (distance / D) ** k
                elif law == 1:
                    Node_E = E_begin * np.exp((distance / D) * np.log(E_end / E_begin))
                elif law == 2:
                    if distance <= D / 2:
                        Node_E = E_begin + (E_end - E_begin) * (distance / D) ** k
                    else:
                        Node_E = E_begin + (E_end - E_begin) * (1 - (1 - distance / D) ** k)  # k > 1
        return Node_E

    # Get y_begin, z_begin
    @staticmethod
    def getNodeMaxMin(theta, Type):

        split_dict = defaultdict(list)

        dictionary = Fiber.MaterialID
        # 将键值对的值添加到新字典中对应值的列表中
        for key, value in dictionary.items():
            split_dict[value].append(key)

        result = []

        # 遍历新字典中的每个键值对
        for value_list in split_dict.values():
            # 判断列表的长度
            if len(value_list) > 0:
                # 如果列表长度大于1，说明有多个键对应相同的值，可以进行拆分
                sub_dict = {}
                for key in value_list:
                    sub_dict[key] = dictionary[key]
                result.append(sub_dict)
        Fiber_Mat = sorted(result, key=lambda x: next(iter(x.values())))
        # print(Fiber_Mat)
        values = [[value for value in sub_dict.values()] for sub_dict in Fiber_Mat]
        Grad_Group = [[key for key in sub_dict.keys()] for sub_dict in Fiber_Mat]
        Groups =  [row[0] for row in values]
        Group_maxminCoor = {}

        Grad_Point = []
        for i in range(len(Grad_Group)):
            Point = []
            for j in range(len(Grad_Group[i])):
                Point.append(Fiber.PointI[Grad_Group[i][j]])
                Point.append(Fiber.PointJ[Grad_Group[i][j]])
                Point.append(Fiber.PointK[Grad_Group[i][j]])
            unique_num_Point = list(set(Point))
            Grad_Point.append(unique_num_Point)
        # print(Grad_Point)
        #[]
        y_begin_list, z_begin_list, y_end_list, z_end_list = [], [], [], []
        for i in range(len(Grad_Point)):
            y_begin, z_begin, y_end, z_end = 0, 0, 0, 0
            min_dis = Node.Y[int(Grad_Point[i][0])] * np.cos(theta[i+1]) + Node.Z[int(Grad_Point[i][0])] * np.sin(theta[i+1])
            max_dis = Node.Y[int(Grad_Point[i][0])] * np.cos(theta[i+1]) + Node.Z[int(Grad_Point[i][0])] * np.sin(theta[i+1])
            for j in range(len(Grad_Point[i])):
                if Type[i + 1] == 0:
                    dis = Node.Y[int(Grad_Point[i][j])] * np.cos(theta[i+1]) + Node.Z[int(Grad_Point[i][j])] * np.sin(theta[i+1])
                    if dis <= min_dis:
                        min_dis = dis
                        y_begin, z_begin = Node.Y[int(Grad_Point[i][j])], Node.Z[int(Grad_Point[i][j])]
                    if dis >= max_dis:
                        max_dis = dis
                        y_end, z_end = Node.Y[int(Grad_Point[i][j])], Node.Z[int(Grad_Point[i][j])]
                        # Group_maxminCoor[Groups[i]] = [y_begin, z_begin, y_end, z_end]
                else:
                    DIS = []
                    for i in range(Node.Count):
                        dis = 0
                        dis = np.sqrt(Node.Y[i] ** 2 + Node.Z[i] **2)
                        DIS.append(dis)
                    min_index, max_index = Node.find_min_max_indexes(DIS)
                    y_begin, z_begin = Node.Y[min_index], Node.Z[min_index]
                    y_end, z_end = Node.Y[max_index], Node.Z[max_index]
            y_begin_list.append(y_begin)
            z_begin_list.append(z_begin)
            y_end_list.append(y_end)
            z_end_list.append(z_end)
        return y_begin_list, z_begin_list, y_end_list, z_end_list, Grad_Point

    @staticmethod
    def getNode_E(angle, E_begin, E_end, law, k, Type):
        E = []
        y_begin_list, z_begin_list, y_end_list, z_end_list, Grad_Point = Node.getNodeMaxMin(angle, Type)
        # print(y_begin_list, z_begin_list, y_end_list, z_end_list)
        # print(angle)
        row_indices = []
        for num in range(Node.Count):
            for i, row in enumerate(Grad_Point):
                if num in row:
                    row_indices.append(i)
                    break
        # print(row_indices)
        for i in range(Node.Count):
            Angle = angle[int(row_indices[i]+1)] / 180 * np.pi
            E.append (Node.Calculate_E(Node.Y[i], Node.Z[i], y_begin_list[int(row_indices[i])], z_begin_list[int(row_indices[i])], y_end_list[int(row_indices[i])], z_end_list[int(row_indices[i])], Angle,
                                       E_begin[int(row_indices[i]+1)], E_end[int(row_indices[i]+1)], law[int(row_indices[i]+1)], k[int(row_indices[i]+1)], Type[int(row_indices[i]+1)]))
        # print(E)
        Node.Node_E = dict(enumerate(E))
        # print(Node.Count)
        # print(Node.Y)
        # print(Node.Z)
        # print(Node.Node_E)


class Segment:
    Count = 0
    ID = {}
    NodeI = {}
    NodeJ = {}

    @staticmethod
    def Reset():
        Segment.Count = 0
        Segment.ID = {}
        Segment.NodeI = {}
        Segment.NodeJ = {}

    @staticmethod
    def readSeg(SegInfo):
        Link = np.concatenate((np.array([np.concatenate((SegInfo[:, 0], SegInfo[:, 1], SegInfo[:, 2]))]),
                               np.array([np.concatenate((SegInfo[:, 1], SegInfo[:, 2], SegInfo[:, 0]))])), axis=0)
        Link.sort(axis=0)
        Link = np.unique(Link, axis=1)
        Segment.NodeI = dict(enumerate(Link[0, :]))
        Segment.NodeJ = dict(enumerate(Link[1, :]))
        Segment.Count = np.size(Link, axis=1)
        Segment.ID = dict(enumerate(np.arange(Segment.Count)))
        return


class Fiber:
    Count = 0
    MaterialID = {}
    Material_AVE = {}
    ID = {}
    GroupID = {}
    PointI = {}
    PointJ = {}
    PointK = {}
    Area = {}
    cy = {}
    cz = {}
    Qy = {}
    Qz = {}
    Iy = {}
    Iz = {}
    Iyz = {}
    Qv = {}
    Qw = {}
    Iv = {}
    Iw = {}
    Seq = {}
    ##
    cv = {}
    cw = {}
    ##
    cygo = {}
    czgo = {}
    # Calculate section yield surface
    Idn_limt = 0.0
    MaxComStr = 0.0
    MaxComV = 0.0
    MaxTenStr = 0.0
    MinTenV = 0.0
    NumAxialLoad = 10
    Dn = 0.0  ## sectional neutral axis position
    MaxY = -9999.0  ##
    MinY = 9999.0  ##
    MaxZ = -9999.0  ##
    MinZ = 9999.0  ##
    MaxV = -9999.0  ##
    MinV = 9999.0  ##
    MaxW = -9999.0  ##
    MinW = 9999.0  ##

    @staticmethod
    def Reset():
        Fiber.Count = 0
        Fiber.ID = {}
        Fiber.GroupID = {}
        Fiber.MaterialID = {}
        Fiber.Material_AVE = {}
        Fiber.PointI = {}
        Fiber.PointJ = {}
        Fiber.PointK = {}
        Fiber.Area = {}
        Fiber.cy = {}
        Fiber.cz = {}
        Fiber.Qy = {}
        Fiber.Qz = {}
        Fiber.Iy = {}
        Fiber.Iz = {}
        Fiber.Iyz = {}
        Fiber.Qv = {}
        Fiber.Qw = {}
        Fiber.Iv = {}
        Fiber.Iw = {}
        Fiber.Seq = {}
        ##
        Fiber.cv = {}
        Fiber.cw = {}
        return

    @staticmethod
    def readFiber(FiberInfo, GroupID):
        Fiber.Count = len(FiberInfo)
        Fiber.ID = dict(enumerate(np.arange(Fiber.Count)))
        Fiber.GroupID = GroupID
        Fiber.MaterialID = {key: Group.MaterialID[value] for key, value in GroupID.items()}
        Fiber.PointI = dict(enumerate(FiberInfo[:, 2]))
        Fiber.PointJ = dict(enumerate(FiberInfo[:, 1]))
        Fiber.PointK = dict(enumerate(FiberInfo[:, 0]))
        Fiber.Material_AVE = np.zeros(Fiber.Count)
        tArea = np.zeros(Fiber.Count)
        tSeq = list(range(Fiber.Count))
        tcy = np.zeros(Fiber.Count)
        tcz = np.zeros(Fiber.Count)
        tIy = np.zeros(Fiber.Count)
        tIz = np.zeros(Fiber.Count)
        tIyz = np.zeros(Fiber.Count)
        tQy = np.zeros(Fiber.Count)
        tQz = np.zeros(Fiber.Count)

        Node.getNode_E(Material.Gra_ang, Material.E_begin, Material.E_end,Material.Gra_law, Material.k, Material.Gra_Type)

        for i in range(Fiber.Count):
            (ttArea, ttSeq) = Tri3.GetA([Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                        [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]])
            tArea[i] = ttArea
            tSeq[i] = ttSeq
            tcy[i] = Tri3.GetCy([Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]],
                                tArea[i], tSeq[i])
            tcz[i] = Tri3.GetCz([Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]],
                                tArea[i], tSeq[i])
            tIy[i] = Tri3.GetIy([Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]],
                                tArea[i], tcz[i])
            tIz[i] = Tri3.GetIz([Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]],
                                tArea[i], tcy[i])
            tIyz[i] = Tri3.GetIyz([Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                  [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]],
                                  tArea[i], tcy[i], tcz[i], tSeq[i])
            tQy[i] = tArea[i] * tcz[i]
            tQz[i] = tArea[i] * tcy[i]
            Fiber.Material_AVE[i] = Tri3.getIntegrate_E([Node.Node_E[Fiber.PointI[i]], Node.Node_E[Fiber.PointJ[i]], Node.Node_E[Fiber.PointK[i]]],
                                                  [Node.Y[Fiber.PointI[i]], Node.Y[Fiber.PointJ[i]], Node.Y[Fiber.PointK[i]]],
                                                  [Node.Z[Fiber.PointI[i]], Node.Z[Fiber.PointJ[i]], Node.Z[Fiber.PointK[i]]])


        Fiber.Area = dict(enumerate(tArea))
        Fiber.cy = dict(enumerate(tcy))
        Fiber.cz = dict(enumerate(tcz))
        Fiber.Qy = dict(enumerate(tQy))
        Fiber.Qz = dict(enumerate(tQz))
        Fiber.Iy = dict(enumerate(tIy))
        Fiber.Iz = dict(enumerate(tIz))
        Fiber.Iyz = dict(enumerate(tIyz))
        Fiber.Seq = dict(enumerate(tSeq))
        Fiber.Material_AVE = dict(enumerate(Fiber.Material_AVE))
        # print('Y')
        # print(list(Fiber.cy.values()))
        # print('Z')
        # print(list(Fiber.cz.values()))
        # print('E')
        # print(list(Fiber.Material_AVE.values()))
        return

    @staticmethod
    def GetPrinciple():
        tcv = np.zeros(Fiber.Count)
        tcw = np.zeros(Fiber.Count)
        tQv = np.zeros(Fiber.Count)
        tQw = np.zeros(Fiber.Count)
        tIv = np.zeros(Fiber.Count)
        tIw = np.zeros(Fiber.Count)

        for i in Fiber.ID.keys():
            tcv[i] = Tri3.GetCy([Node.V[Fiber.PointI[i]], Node.V[Fiber.PointJ[i]], Node.V[Fiber.PointK[i]]],
                                [Node.W[Fiber.PointI[i]], Node.W[Fiber.PointJ[i]], Node.W[Fiber.PointK[i]]],
                                Fiber.Area[i], Fiber.Seq[i])
            tcw[i] = Tri3.GetCz([Node.V[Fiber.PointI[i]], Node.V[Fiber.PointJ[i]], Node.V[Fiber.PointK[i]]],
                                [Node.W[Fiber.PointI[i]], Node.W[Fiber.PointJ[i]], Node.W[Fiber.PointK[i]]],
                                Fiber.Area[i], Fiber.Seq[i])
            tIv[i] = Tri3.GetIy([Node.V[Fiber.PointI[i]], Node.V[Fiber.PointJ[i]], Node.V[Fiber.PointK[i]]],
                                [Node.W[Fiber.PointI[i]], Node.W[Fiber.PointJ[i]], Node.W[Fiber.PointK[i]]],
                                Fiber.Area[i], tcw[i])
            tIw[i] = Tri3.GetIz([Node.V[Fiber.PointI[i]], Node.V[Fiber.PointJ[i]], Node.V[Fiber.PointK[i]]],
                                [Node.W[Fiber.PointI[i]], Node.W[Fiber.PointJ[i]], Node.W[Fiber.PointK[i]]],
                                Fiber.Area[i], tcv[i])
            tQv[i] = Fiber.Area[i] * tcw[i]
            tQw[i] = Fiber.Area[i] * tcv[i]

        Fiber.cv = dict(zip_longest(Fiber.ID.keys(), tcv))
        Fiber.cw = dict(zip_longest(Fiber.ID.keys(), tcw))
        Fiber.Qv = dict(zip_longest(Fiber.ID.keys(), tQv))
        Fiber.Qw = dict(zip_longest(Fiber.ID.keys(), tQw))
        Fiber.Iv = dict(zip_longest(Fiber.ID.keys(), tIv))
        Fiber.Iw = dict(zip_longest(Fiber.ID.keys(), tIw))

        return


class Node3D:
    Count = 0
    ID = {}
    X = {}
    Y = {}
    Z = {}
    Omega = {}

    @classmethod
    def Reset(cls):
        Node3D.Count = 0
        Node3D.ID = {}
        Node3D.X = {}
        Node3D.Y = {}
        Node3D.Z = {}
        Node3D.Omega = {}
        return

    def readNode(NodeInfo):
        Node3D.Count = len(NodeInfo)
        Node3D.ID = dict(enumerate(np.arange(Node3D.Count)))
        Node3D.X = dict(enumerate(NodeInfo[:, 0]))
        Node3D.Y = dict(enumerate(NodeInfo[:, 1]))
        Node3D.Z = dict(enumerate(NodeInfo[:, 2]))
        return

class Segment3D:
    Count = 0
    ID = {}
    NodeI = {}
    NodeJ = {}

    @staticmethod
    def Reset():
        Segment3D.Count = 0
        Segment3D.ID = {}
        Segment3D.NodeI = {}
        Segment3D.NodeJ = {}

    @staticmethod
    def readSeg(SegInfo):
        Link = np.concatenate((np.concatenate((SegInfo[:, 0][np.newaxis, :], SegInfo[:, 1][np.newaxis, :])),
                               np.concatenate((SegInfo[:, 0][np.newaxis, :], SegInfo[:, 2][np.newaxis, :])),
                               np.concatenate((SegInfo[:, 0][np.newaxis, :], SegInfo[:, 3][np.newaxis, :])),
                               np.concatenate((SegInfo[:, 1][np.newaxis, :], SegInfo[:, 2][np.newaxis, :])),
                               np.concatenate((SegInfo[:, 1][np.newaxis, :], SegInfo[:, 3][np.newaxis, :])),
                               np.concatenate((SegInfo[:, 2][np.newaxis, :], SegInfo[:, 3][np.newaxis, :]))), axis=1)
        Link.sort(axis=0)
        Link = np.unique(Link, axis=1)
        Segment3D.NodeI = dict(enumerate(Link[0, :]))
        Segment3D.NodeJ = dict(enumerate(Link[1, :]))
        Segment3D.Count = np.size(Link, axis=1)
        Segment3D.ID = dict(enumerate(np.arange(Segment3D.Count)))
        return


class Fiber3D:
    Count = 0
    MaterialID = {}
    ID = {}
    GroupID = {}
    PointI = {}
    PointJ = {}
    PointK = {}
    PointL = {}


    @staticmethod
    def Reset():
        Fiber3D.Count = 0
        Fiber3D.ID = {}
        Fiber3D.GroupID = {}
        Fiber3D.MaterialID = {}
        Fiber3D.PointI = {}
        Fiber3D.PointJ = {}
        Fiber3D.PointK = {}
        Fiber3D.PointL = {}

    @staticmethod
    def readFiber(FiberInfo, GroupID):
        Fiber3D.Count = len(FiberInfo)
        Fiber3D.ID = dict(enumerate(np.arange(Fiber3D.Count)))
        Fiber3D.GroupID = GroupID
        Fiber3D.MaterialID = {key: Group.MaterialID[value] for key, value in GroupID.items()}
        Fiber3D.PointI = dict(enumerate(FiberInfo[:, 3]))
        Fiber3D.PointJ = dict(enumerate(FiberInfo[:, 2]))
        Fiber3D.PointK = dict(enumerate(FiberInfo[:, 1]))
        Fiber3D.PointL = dict(enumerate(FiberInfo[:, 0]))


class OutResult:
    FileName = ""
    Folder = ""
    ModelInfo = ""

    @staticmethod
    def ReadOutResult(FileName, Folder):
        OutResult.FileName = FileName
        OutResult.Folder = Folder
        OutResult.ModelInfo = ""


class TempNode:
    Count = 0
    ID = {}
    Y = {}
    Z = {}

    @staticmethod
    def Reset():
        TempNode.Count = 0
        TempNode.ID = {}
        TempNode.Y = {}
        TempNode.Z = {}
        return

    @staticmethod
    def readTempNode(NodeInfo):
        TempNode.Count = len(NodeInfo)
        TempNode.ID = dict(enumerate(np.arange(Node.Count)))
        TempNode.Y = dict(enumerate(NodeInfo[:, 1]))
        TempNode.Z = dict(enumerate(NodeInfo[:, 0]))
        return


class TempFiber:
    Count = 0
    MaterialID = {}
    ID = {}
    GroupID = {}
    PointI = {}
    PointJ = {}
    PointK = {}

    @staticmethod
    def Reset():
        TempFiber.Count = 0
        TempFiber.ID = {}
        TempFiber.GroupID = {}
        TempFiber.MaterialID = {}
        TempFiber.PointI = {}
        TempFiber.PointJ = {}
        TempFiber.PointK = {}
        return

    @staticmethod
    def readTempFiber(FiberInfo, GroupID):
        TempFiber.Count = len(FiberInfo)
        TempFiber.ID = dict(enumerate(np.arange(Fiber.Count)))
        TempFiber.GroupID = GroupID
        TempFiber.MaterialID = {key: Group.MaterialID[value] for key, value in GroupID.items()}
        TempFiber.PointI = dict(enumerate(FiberInfo[:, 2]))
        TempFiber.PointJ = dict(enumerate(FiberInfo[:, 1]))
        TempFiber.PointK = dict(enumerate(FiberInfo[:, 0]))
        return

class YieldSAnalResults:

    ONx = dict()
    OMy = dict() ## My or Mv
    OMz = dict() ## Mz or Mw
    OAngle = dict()
    ODn = dict()
    StrnContlType = 0
    ##
    ONx_y = dict()  ## Px vs. My or Px vs. Mv
    OMy_x = dict()  ## Px vs. My or Px vs. Mv
    PMy_StrnContlType = 0
    ONx_z = dict()  ## Px vs. Mz or Px vs. Mw
    OMz_x = dict()  ## Px vs. Mz or Px vs. Mw
    PMz_StrnContlType = 0
    ONx_yz = dict()  ## My vs. Mz or Mv vs. Mw
    OMy_z = dict()  ## My vs. Mz or Mv vs. Mw
    OMz_y = dict()  ## My vs. Mz or Mv vs. Mw
    MyMz_StrnContlType = 0
    ## {'P',{'0', val,'1', val},'My',{'0', val,'1', val},'Mz',{'0', val,'1', val}, 'InAngle',{'0', val,'1', val}, 'InAngle',{'0', val,'1', val}}
    @classmethod
    def Reset(cls):
        YieldSAnalResults.ONx = {}
        YieldSAnalResults.OMy = {}
        YieldSAnalResults.OMz = {}
        YieldSAnalResults.OAngle = {}
        YieldSAnalResults.ODn = {}
        YieldSAnalResults.StrnContlType = 0
        ##
    @classmethod
    def ResetONxMy(cls):
        YieldSAnalResults.ONx_y = {}
        YieldSAnalResults.OMy_x = {}
        YieldSAnalResults.PMy_StrnContlType = 0

    @classmethod
    def ResetONxMz(cls):
        YieldSAnalResults.ONx_z = {}
        YieldSAnalResults.OMz_x = {}
        YieldSAnalResults.PMz_StrnContlType = 0

    @classmethod
    def ResetOMyMz(cls):
        YieldSAnalResults.OMy_z = {}
        YieldSAnalResults.OMz_y = {}
        YieldSAnalResults.MyMz_StrnContlType = 0

    @classmethod
    def ResetAllResults(cls):
        YieldSAnalResults.Reset()
        YieldSAnalResults.ResetONxMy()
        YieldSAnalResults.ResetOMyMz()
        YieldSAnalResults.ResetONxMz()

class YieldSurfaceAnalInfo:
    PosNStep = 10  # P/25
    NegNStep = 10  # -P/25
    MStep = 20  # 360/3
    MaxNumIter = 300
    ConvTol = 0.001
    StrainAtValue = 0.001
    BStrainControl = 0  ## 0: default, Strain reaches ultimate strain;
                        ## 1: Strain at the onset of maximum stress;
                        ## 2: Strin at the value of

    SubAnalType = 1     ## 1: Full Yield Surfaces (P-My-Mz); 2: Planar Yield Surfaces (P-My or P-Mv);
                        ## 3: Planar Yield Surfaces (My-Mz or Mv-Mw); 4: Planar Yield Surfaces (P-Mz or P-Mw);

    AxisSlctn = 1       ## 1: User-defined Axis; 2: Principal Axis


    # SectYSPx = {}
    # SectYSMy = {}
    # SectYSMz = {}
    def InitSectYSurf(self):
        # Initialization
        TotalNumData = (self.PosNStep * 2 + 1) * (self.MStep + 1)
        self.SectYSPx = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
        self.SectYSMy = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
        self.SectYSMz = dict(zip_longest(np.arange(TotalNumData), np.zeros(TotalNumData)))
        #
        return

    def ReadYSurfAnalInfo(self, YSAnalInfo):
        print("YSAnalInfo = ", YSAnalInfo)
        print("YSAnalInfo type = ", type(YSAnalInfo))
        # YSAnalInfo = dict(YSAnalInfo)
        # # print("YSAnalInfo = ", YSAnalInfo)
        # # print("YSAnalInfo type = ", type(YSAnalInfo))

        if YSAnalInfo.size != 0:
            YSAnalInfo = dict(zip_longest(YSAnalInfo[:, 0], YSAnalInfo[:, 1]))
            print("YSAnalInfo = ", YSAnalInfo)
            print("YSAnalInfo type = ", type(YSAnalInfo))
            self.PosNStep = int(YSAnalInfo.get('PosNStep', 50))
            self.NegNStep = int(YSAnalInfo.get('NegNStep', 50))
            self.MStep = int(YSAnalInfo.get('MomentStep', 120))
            self.MaxNumIter = int(YSAnalInfo.get('MaxNumIter', 300))
            self.ConvTol = float(YSAnalInfo.get('ConvTol', 0.001))
            self.StrainAtValue = float(YSAnalInfo.get('StrainAtValue', 0.001))
            self.BStrainControl = int(YSAnalInfo.get('BStrainControl', 0))
            self.SubAnalType = int(YSAnalInfo.get('SubAnalType', 1))
            self.AxisSlctn = int(YSAnalInfo.get('AxisSlctn', 1))

    @staticmethod
    def get_info(YSInfo):
        YieldSurfaceAnalInfo.PosNStep = int(YSInfo[0])
        YieldSurfaceAnalInfo.NegNStep = int(YSInfo[1])
        YieldSurfaceAnalInfo.MStep = int(YSInfo[2])
        YieldSurfaceAnalInfo.MaxNumIter = int(YSInfo[3])
        YieldSurfaceAnalInfo.ConvTol = float(YSInfo[4])
        YieldSurfaceAnalInfo.StrainAtValue = float(YSInfo[5])
        YieldSurfaceAnalInfo.BStrainControl = int(YSInfo[6])
        YieldSurfaceAnalInfo.SubAnalType = int(YSInfo[7])
        YieldSurfaceAnalInfo.AxisSlctn = int(YSInfo[8])


def ResetMesh():
    Material.Reset()
    Point.Reset()
    Outline.Reset()
    Group.Reset()
    Analysis.Reset()
    Node.Reset()
    Segment.Reset()
    Fiber.Reset()
    TempNode.Reset()
    TempFiber.Reset()
