from matplotlib import pyplot as plt
import numpy as np
import codecs
import copy
import os


def ReadBulge(NodeY, NodeZ, Bulge, MinSeg, SegResolu):
    i = 0
    while i < len(NodeY):
        if Bulge[i] != 0:
            n = max(MinSeg, int(np.ceil(SegResolu * abs(Bulge[i]))))
            AngRange = 4 * np.arctan(Bulge[i])
            K = (1 / Bulge[i] - Bulge[i]) / 2
            Ys = NodeY[i]
            Zs = NodeZ[i]
            if i + 1 >= len(NodeY):
                Ye = NodeY[0]
                Ze = NodeZ[0]
            else:
                Ye = NodeY[i + 1]
                Ze = NodeZ[i + 1]
            CY = (Ys + Ye + (Ze - Zs) * K) / 2
            CZ = (Zs + Ze - (Ye - Ys) * K) / 2
            R = np.sqrt((Ye - CY) ** 2 + (Ze - CZ) ** 2)
            for j in range(1, n):
                Y = CY + (Ys - CY) * np.cos(AngRange * j / n) + (Zs - CZ) * np.sin(AngRange * j / n)
                Z = CZ + (Zs - CZ) * np.cos(AngRange * j / n) - (Ys - CY) * np.sin(AngRange * j / n)
                NodeY.insert(i + j, Y)
                NodeZ.insert(i + j, Z)
                Bulge.insert(i + j, 0)
            i += n - 1
        else:
            i += 1
    return NodeY, NodeZ


def ReadPolyline(Text, i):
    NodeY = []
    NodeZ = []
    Type = ""
    NodeCount = 0
    TotalNodes = 0
    while i < len(Text):
        if Text[i] == "90":
            i += 1
            TotalNodes = int(Text[i])
            i += 1
        if Text[i] == "43":
            i += 1
            if Text[i] == "1.0":
                Type = "O"
            elif Text[i] == "0.0":
                Type = "S"
            break
        i += 1
    Bulge = [0] * TotalNodes
    while NodeCount < TotalNodes:
        if Text[i] == "10":
            i += 1
            NodeZ.append(float(Text[i]))
            i += 1
            if Text[i] == "20":
                i += 1
                NodeY.append(float(Text[i]))
                i += 1
                if Text[i] == "42":
                    i += 1
                    Bulge[NodeCount] = float(Text[i])
                    i += 1
            NodeCount += 1
        else:
            i += 1
    return NodeY, NodeZ, Bulge, Type, i


def OutputFile(FileName, DXF):
    f = codecs.open(FileName, 'w', 'utf-8')
    tOutput = StartMessage()
    f.write(tOutput)
    tOutput = WritePoint(DXF)
    f.write(tOutput)
    tOutput = WriteOutline(DXF)
    f.write(tOutput)
    tOutput = EndMessage()
    f.write(tOutput)
    f.close()
    return


def StartMessage():
    tOutput = "{\n"
    tOutput += "  \"INFORMATION\":[\n"
    tOutput += "    [ \"Version\", \"1.0.0\"],\n"
    tOutput += "    [ \"Date\", \"20220501\"],\n"
    tOutput += "    [ \"Description\", \"This example is provided for FESect testing\"]\n"
    tOutput += "  ],\n"
    tOutput += "  \"MATERIAL\": [\n"
    tOutput += "    [ 1, 200000, 76923, 0.3, 350, 7900, 0.2, [ [0, 1], [0, 1] ] ]\n"
    tOutput += "  ],\n"
    return tOutput


def WritePoint(DXF):
    tOutput = "  \"POINT\": [\n"
    for i in range(len(DXF)):
        for j in range(len(DXF[i][0])):
            if DXF[i][5][j] == 0:
                if i < len(DXF) - 1 or j < len(DXF[i][0]) - 1:
                    tOutput += "    [ {}, {}, {} ],\n".format(DXF[i][0][j], DXF[i][1][j], DXF[i][2][j])
                else:
                    tOutput += "    [ {}, {}, {} ]\n".format(DXF[i][0][j], DXF[i][1][j], DXF[i][2][j])
    tOutput += "  ],\n"
    return tOutput


def EndMessage():
    tOutput = "  \"GROUP\": [\n"
    tOutput += "    [ 1, 1 ]\n"
    tOutput += "  ],\n"
    tOutput += "  \"LOADCASE\": [\n"
    tOutput += "    [ 1, 0, 0, 0, 0, 0, 0, 0 ]\n"
    tOutput += "  ],\n"
    tOutput += "  \"ANALYSIS\": [\n"
    tOutput += "    [ \"Fiber Size\", 0 ],\n"
    tOutput += "    [ \"Element\", \"Tri3\" ],\n"
    tOutput += "    [ \"Gauss Points\", 7 ],\n"
    tOutput += "    [ \"Basic Properties\", 1 ],\n"
    tOutput += "    [ \"Stress Analysis\", 0 ],\n"
    tOutput += "    [ \"Buckling Analysis\", 0 ],\n"
    tOutput += "    [ \"Dynamic Analysis\", 0 ],\n"
    tOutput += "    [ \"Heat Transfer\", 0 ],\n"
    tOutput += "    [ \"Yield Surface\", 0 ],\n"
    tOutput += "    [ \"Moment Curvature\", 0 ]\n"
    tOutput += "  ]\n"
    tOutput += "}"
    return tOutput


def WriteOutline(DXF):
    tOutput = "  \"OUTLINE\": [\n"
    k = 1
    for i in range(len(DXF)):
        for j in range(len(DXF[i][0])):
            if j < len(DXF[i][0]) - 1:
                tOutput += "    [ {}, {}, \"{}\", {}, {} ],\n".format(k, DXF[i][3], DXF[i][4], DXF[i][0][j], DXF[i][0][j + 1])
            elif i < len(DXF) - 1:
                tOutput += "    [ {}, {}, \"{}\", {}, {} ],\n".format(k, DXF[i][3], DXF[i][4], DXF[i][0][j], DXF[i][0][0])
            else:
                tOutput += "    [ {}, {}, \"{}\", {}, {} ]\n".format(k, DXF[i][3], DXF[i][4], DXF[i][0][j], DXF[i][0][0])
            k += 1
    tOutput += "  ],\n"
    return tOutput


def PlotPolyLine(i, DXF, YLB, YUB, ZLB, ZUB):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    Range = list(range(len(DXF)))
    Range.pop(i)
    for j in Range:
        tNodeY = copy.deepcopy(DXF[j][1])
        tNodeZ = copy.deepcopy(DXF[j][2])
        tNodeY.append(tNodeY[0])
        tNodeZ.append(tNodeZ[0])
        ax.set_xlim(ZLB, ZUB)
        ax.set_ylim(YLB, YUB)
        ax.set_aspect('equal',adjustable='box')
        ax.plot(tNodeZ, tNodeY, color='lightgray', linewidth=1)
    tNodeY = copy.deepcopy(DXF[i][1])
    tNodeZ = copy.deepcopy(DXF[i][2])
    tNodeY.append(tNodeY[0])
    tNodeZ.append(tNodeZ[0])
    ax.set_xlim(ZLB, ZUB)
    ax.set_ylim(YLB, YUB)
    ax.set_aspect('equal', adjustable='box')
    ax.plot(tNodeZ, tNodeY, color='k', linewidth=1)
    plt.show(block=False)
    plt.pause(999)
    print("Apply GroupID:")
    GroupID = input(">>")
    DXF[i][3] = GroupID
    plt.close()
    return


def Deduplicate(DXF):
    for i in range(len(DXF)):
        DXF[i].append([0] * len(DXF[i][0]))
    for i in range(len(DXF)):
        for j in range(len(DXF[i][0])):
            if DXF[i][5][j] == 0:
                if j < len(DXF[i][0]) - 1:
                    for jj in range(j + 1, len(DXF[i][0])):
                        if DXF[i][1][jj] == DXF[i][1][j] and DXF[i][2][jj] == DXF[i][2][j]:
                            DXF[i][0][jj] = DXF[i][0][j]
                            DXF[i][5][jj] = 1
                if i < len(DXF) - 1:
                    for ii in range(i + 1, len(DXF)):
                        for jj in range(len(DXF[ii][0])):
                            if DXF[ii][1][jj] == DXF[i][1][j] and DXF[ii][2][jj] == DXF[i][2][j]:
                                DXF[ii][0][jj] = DXF[i][0][j]
                                DXF[ii][5][jj] = 1


def ReadDXF(MinSeg, SegResolu):
    print("Input File Path:")
    Input = input(">>")
    Folder = os.path.dirname(Input)
    DXFName = os.path.basename(Input).split(".")[0]
    FileName = "{}\\{}".format(Folder, DXFName)
    File = open(Input)
    Text = []
    DXF = []
    while True:
        Line = File.readline()
        if not Line:
            break
        Text.append(Line.strip())
    i = 0
    while i < len(Text):
        if Text[i] == "AcDbPolyline":
            [NodeY, NodeZ, Bulge, Type, EndRow] = ReadPolyline(Text, i)
            DXF.append([NodeY, NodeZ, Bulge, Type])
            i = EndRow
        else:
            i += 1
    j = 1
    for i in range(len(DXF)):
        [NodeY, NodeZ] = ReadBulge(DXF[i][0], DXF[i][1], DXF[i][2], MinSeg, SegResolu)
        DXF[i].insert(0, list(range(j, j + len(NodeY))))
        DXF[i][1] = NodeY
        DXF[i][2] = NodeZ
        j += len(NodeY)
    YMax = YMin = DXF[0][1][0]
    ZMax = ZMin = DXF[0][2][0]
    for i in range(len(DXF)):
        YMax = max(YMax, max(DXF[i][1]))
        YMin = min(YMin, min(DXF[i][1]))
        ZMax = max(ZMax, max(DXF[i][2]))
        ZMin = min(ZMin, min(DXF[i][2]))
    YMargin = (YMax - YMin) / 10
    ZMargin = (ZMax - ZMin) / 10
    YLB = YMin - YMargin
    YUB = YMax + YMargin
    ZLB = ZMin - ZMargin
    ZUB = ZMax + ZMargin
    for i in range(len(DXF)):
        PlotPolyLine(i, DXF, YLB, YUB, ZLB, ZUB)
    Deduplicate(DXF)
    OutputFile(FileName, DXF)


ReadDXF(2, 3)