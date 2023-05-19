###########################################################################################
#
# MSASECT - Python-based Cross-platforms Section Analysis Software
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
# ===========================================================================
# Import standard libraries
import numpy as np
import codecs
import csv
import os
import copy
import matplotlib.pyplot as plt
# Import internal functions


def StartMessage(tName, tAuthors, tRevisedDate):
    tOutput = "********************************************************************************\n"
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MSASECT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    tOutput += "********************************************************************************\n\n"
    tOutput += "Programme Name: {}\n".format(tName)
    tOutput += "Authors: {}\n".format(tAuthors)
    tOutput += "Last Revised: {}\n".format(tRevisedDate)
    tOutput += "Note: Finite-Element Based Cross-Section (PyFESect) Analysis Software"
    return tOutput


def EndMessage():
    tOutput = "\n"
    tOutput += "********************************************************************************\n"
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    tOutput += "********************************************************************************\n"
    return tOutput


class BPRes:
    @staticmethod
    def AddResult(SP):
        tOutput = '\u03b8,{:.8e}\n'.format(np.rad2deg(SP.Theta))
        tOutput += 'A,{:.8e}\n'.format(SP.Area)
        tOutput += 'Ygc,{:.8e}\n'.format(SP.cy)
        tOutput += 'Zgc,{:.8e}\n'.format(SP.cz)
        tOutput += 'Ysc,{:.8e}\n'.format(SP.cys)
        tOutput += 'Zsc,{:.8e}\n'.format(SP.czs)
        tOutput += 'Vsc,{:.8e}\n'.format(SP.cvs)
        tOutput += 'Wsc,{:.8e}\n'.format(SP.cws)
        tOutput += 'J,{:.8e}\n'.format(SP.J)
        tOutput += 'I\u03c9,{:.8e}\n'.format(SP.Iomg)
        tOutput += 'Iyy,{:.8e}\n'.format(SP.Iyc)
        tOutput += 'Izz,{:.8e}\n'.format(SP.Izc)
        tOutput += 'Iyz,{:.8e}\n'.format(SP.Iyzc)
        tOutput += 'Qy,{:.8e}\n'.format(SP.Qy)
        tOutput += 'Qz,{:.8e}\n'.format(SP.Qz)
        tOutput += '\u03b2y,{:.8e}\n'.format(SP.Betay)
        tOutput += '\u03b2z,{:.8e}\n'.format(SP.Betaz)
        tOutput += '\u03b2\u03c9,{:.8e}\n'.format(SP.Betaomg)
        tOutput += 'ky,{:.8e}\n'.format(SP.ky)
        tOutput += 'kz,{:.8e}\n'.format(SP.kz)
        tOutput += 'Syy,{:.8e}\n'.format(SP.Sy)
        tOutput += 'Szz,{:.8e}\n'.format(SP.Sz)
        tOutput += 'Zyy,{:.8e}\n'.format(SP.Zy)
        tOutput += 'Zzz,{:.8e}\n'.format(SP.Zz)
        tOutput += 'ry,{:.8e}\n'.format(SP.ry)
        tOutput += 'rz,{:.8e}\n'.format(SP.rz)
        tOutput += 'Ivv,{:.8e}\n'.format(SP.Iv)
        tOutput += 'Iww,{:.8e}\n'.format(SP.Iw)
        tOutput += 'Qv,{:.8e}\n'.format(SP.Qv)
        tOutput += 'Qw,{:.8e}\n'.format(SP.Qw)
        tOutput += '\u03b2v,{:.8e}\n'.format(SP.Betav)
        tOutput += '\u03b2w,{:.8e}\n'.format(SP.Betaw)
        tOutput += 'kv,{:.8e}\n'.format(SP.kv)
        tOutput += 'kw,{:.8e}\n'.format(SP.kw)
        tOutput += 'Svv,{:.8e}\n'.format(SP.Sv)
        tOutput += 'Sww,{:.8e}\n'.format(SP.Sw)
        tOutput += 'Zvv,{:.8e}\n'.format(SP.Zv)
        tOutput += 'Zww,{:.8e}\n'.format(SP.Zw)
        tOutput += 'rv,{:.8e}\n'.format(SP.rv)
        tOutput += 'rw,{:.8e}\n'.format(SP.rw)
        return tOutput

    @staticmethod
    def OutBPRes(OutResult, SP):
        ResultFolder = "{}/{}.Json.rst".format(OutResult.Folder, OutResult.FileName)
        fileName = "{}\\{}-Section properties.txt".format(ResultFolder, OutResult.FileName)
        if not os.path.exists(ResultFolder):
            os.makedirs(ResultFolder)
        f = codecs.open(fileName, 'w', 'utf-8')
        tOutput = BPRes.AddResult(SP)
        f.write(tOutput)
        f.close()
        return


class MeshRes:
    @staticmethod
    def IniCSV(fileName,Headings):
        with open(fileName,'w+',newline='') as disRes:
            myWriter=csv.writer(disRes)
            myWriter.writerow(Headings)

    @staticmethod
    def AddCSVRow(fileName, RowRes):
        with open(fileName,'a',newline='') as disRes:
            myWriter=csv.writer(disRes)
            myWriter.writerow(RowRes)

    @staticmethod
    def IniResults(OutResult):
        ResultFolder = "{}{}.rst".format(OutResult.Folder, OutResult.FileName)
        if not os.path.exists(ResultFolder):
            os.makedirs(ResultFolder)
        fileName = "{}\\{}-Meshed-Points List.csv".format(ResultFolder, OutResult.FileName)
        Headings = ["Point ID", "Y", "Z"]
        MeshRes.IniCSV(fileName, Headings)
        # ------------------------------------------------------------------------------------------------------------------
        fileName = "{}\\{}-Meshed-Fiber List.csv".format(ResultFolder, OutResult.FileName)
        Headings = ["Fiber ID", "Group ID", "Point I", "Point J", "Point K", "Area", "cy", "cz"]
        MeshRes.IniCSV(fileName, Headings)
        return

    @staticmethod
    def OutCyCRes(Model):
        MeshRes.IniResults(Model.OutResult)
        ResultFolder = "{}{}.rst".format(Model.OutResult.Folder, Model.OutResult.FileName)
        fileName = "{}\\{}-Meshed-Points List.csv".format(ResultFolder, Model.OutResult.FileName)
        for i in Model.Node.ID:
            RowRes = list(np.zeros(3))
            RowRes[0] = Model.Node.ID[i]
            RowRes[1] = Model.Node.Y[i]
            RowRes[2] = Model.Node.Z[i]
            MeshRes.AddCSVRow(fileName, RowRes)
        fileName = "{}\\{}-Meshed-Fiber List.csv".format(ResultFolder, Model.OutResult.FileName)
        for i in Model.Fiber.ID:
            tID = Model.Fiber.ID[i]
            RowRes = list(np.zeros(8))
            RowRes[0] = Model.Fiber.ID[i]
            RowRes[1] = Model.Fiber.GroupID[tID]
            RowRes[2] = Model.Fiber.PointI[i]
            RowRes[3] = Model.Fiber.PointJ[i]
            RowRes[4] = Model.Fiber.PointK[i]
            RowRes[5] = Model.Fiber.Area[tID]
            RowRes[6] = Model.Fiber.cy[tID]
            RowRes[7] = Model.Fiber.cz[tID]
            MeshRes.AddCSVRow(fileName, RowRes)
        return

    @staticmethod
    def OutGeoFig(Model, FigSize, PointSize, LineWidth):
        ResultFolder = "{}{}.rst".format(Model.OutResult.Folder, Model.OutResult.FileName)
        fileName = "{}\\{}-Geometry Figure.png".format(ResultFolder, Model.OutResult.FileName)
        plt.figure(figsize=FigSize)
        ax = plt.gca()
        ax.set_aspect(1)
        plt.scatter([Model.Point.Z[i] for i in Model.Point.ID], [Model.Point.Y[i] for i in Model.Point.ID], s=PointSize, c='k')
        for i in Model.Outline.ID:
            plt.plot([Model.Point.Z[Model.Outline.Point1[i]], Model.Point.Z[Model.Outline.Point2[i]]],
                     [Model.Point.Y[Model.Outline.Point1[i]], Model.Point.Y[Model.Outline.Point2[i]]],
                     color='k', linestyle='-', linewidth=LineWidth)
        MeshRes.FillColor(Model)
        plt.savefig(fileName)
        plt.close()
        return

    @staticmethod
    def OutMeshFig(Model, FigSize, PointSize, LineWidth):
        ResultFolder = "{}{}.rst".format(Model.OutResult.Folder, Model.OutResult.FileName)
        fileName = "{}\\{}-Mesh Figure.png".format(ResultFolder, Model.OutResult.FileName)
        plt.figure(figsize=FigSize)
        ax = plt.gca()
        ax.set_aspect(1)
        plt.scatter([Model.Point.Z[i] for i in Model.Point.ID], [Model.Point.Y[i] for i in Model.Point.ID], s=PointSize,
                    c='k')
        for i in Model.Outline.ID:
            plt.plot([Model.Point.Z[Model.Outline.Point1[i]], Model.Point.Z[Model.Outline.Point2[i]]],
                     [Model.Point.Y[Model.Outline.Point1[i]], Model.Point.Y[Model.Outline.Point2[i]]],
                     color='k', linestyle='-', linewidth=LineWidth * 2)
        for i in Model.Fiber.ID:
            plt.plot([Model.Node.Z[Model.Fiber.PointI[i]], Model.Node.Z[Model.Fiber.PointJ[i]], Model.Node.Z[Model.Fiber.PointK[i]], Model.Node.Z[Model.Fiber.PointI[i]]],
                     [Model.Node.Y[Model.Fiber.PointI[i]], Model.Node.Y[Model.Fiber.PointJ[i]], Model.Node.Y[Model.Fiber.PointK[i]], Model.Node.Y[Model.Fiber.PointI[i]]],
                     color='k', linestyle='-', linewidth=LineWidth)
        plt.savefig(fileName)
        plt.close()
        return

    @staticmethod
    def GetSequence(Point1, Point2):
        tPoint1 = copy.deepcopy(Point1)
        tPoint2 = copy.deepcopy(Point2)
        Seq = []
        i = 0
        while len(tPoint1) > 0:
            Seq.append([tPoint1[0], tPoint2[0]])
            tPoint1.pop(0)
            tPoint2.pop(0)
            j = 0
            while j < len(Point1):
                if Seq[i][j + 1] in tPoint1:
                    Index = tPoint1.index(Seq[i][j + 1])
                    Seq[i].append(tPoint2[Index])
                elif Seq[i][j + 1] in tPoint2:
                    Index = tPoint2.index(Seq[i][j + 1])
                    Seq[i].append(tPoint1[Index])
                else:
                    break
                tPoint1.pop(Index)
                tPoint2.pop(Index)
                j += 1
            i += 1
        for i in range(len(Seq)):
            Seq[i].pop()
        return Seq

    @staticmethod
    def FillColor(Model):
        Groups = list(Model.Group.ID.keys())
        SolidsP1 = [[] for _ in Groups]
        SolidsP2 = [[] for _ in Groups]
        HolesP1 = [[] for _ in Groups]
        HolePs = [[] for _ in Groups]
        SolidsPs = [[] for _ in Groups]
        HolesP2 = [[] for _ in Groups]
        for i in Model.Outline.ID:
            Index = Groups.index(Model.Outline.GroupID[i])
            if Model.Outline.Type[i] == "S":
                SolidsP1[Index].append(Model.Outline.Point1[i])
                SolidsP2[Index].append(Model.Outline.Point2[i])
            elif Model.Outline.Type[i] == "O":
                HolesP1[Index].append(Model.Outline.Point1[i])
                HolesP2[Index].append(Model.Outline.Point2[i])
        y=list()
        z=list()
        for i in range(len(SolidsP1)):
            SolidsPs[i] = SolidsP1[i]+(SolidsP2[i])
        color=['blue','coral','green','orange','pink','silver','yellow','brown', 'lime', 'skyblue']
        for i in range (len(SolidsPs)):
            SolidsPs[i] = list(set(SolidsPs[i]))
        for i in range(len(HolesP1)):
            HolePs[i] = HolesP1[i] + (HolesP2[i])
            HolePs[i] = list(set(HolePs[i]))
        for a in range (len(SolidsPs)):
            for ii in range (len(SolidsPs[a])):
                y.append(Model.Point.Z[SolidsPs[a][ii]])
                z.append(Model.Point.Y[SolidsPs[a][ii]])
            plt.fill(y,z,color[a])
            y.clear()
            z.clear()
        for a in range(len(HolePs)):
            for ii in range(len(HolePs[a])):
                y.append(Model.Point.Z[HolePs[a][ii]])
                z.append(Model.Point.Y[HolePs[a][ii]])
            plt.fill(y, z, 'white')
            y.clear()
            z.clear()
        return
