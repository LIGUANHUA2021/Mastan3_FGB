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
# =========================================================================================
# Import standard libraries
#import numpy as np
#import math
import timeit, sys, logging, os, codecs
import numpy as np
# Import internal functions
# =========================================================================================
from analysis.FESect.variables.Model import OutResult


def Print(message):
    print(message)
    LogFile.Output += message
    return


class MainLog:
    @staticmethod
    def StartMessage(tName, tAuthors, tRevisedDate):
        tOutput = "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MSASECT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n"
        tOutput += "\n"
        tOutput += tName + "\n"
        tOutput += tAuthors + "\n"
        tOutput += tRevisedDate + "\n"
        return tOutput

    @staticmethod
    def EndMessage():
        tOutput = "\n"
        tOutput += "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n"
        return tOutput

    @staticmethod
    def GetRuntime(StartTime):
        Time = timeit.default_timer() - StartTime
        tOutput = "********************************************************************************\n"
        tOutput += "Run time = {:.2f} s\n".format(Time)
        tOutput += "********************************************************************************\n"
        return tOutput


class LogFile:
    Output = ""

    @staticmethod
    def OutputLogFile():
        ResultFolder = "{}/{}.Json.rst".format(OutResult.Folder, OutResult.FileName)
        LogFileName = "{}\\{}.Json.log".format(ResultFolder, OutResult.FileName)
        if not os.path.exists(ResultFolder):
            os.makedirs(ResultFolder)
        logging.basicConfig(filename=LogFileName, filemode="w", format="%(message)s", level=logging.INFO)
        logging.info(LogFile.Output)
        return


class ModelLog:
    def Info(Description, Material, Point, Outline, Group, AnalysisType, Element):
        tOutput = "\n"
        tOutput += "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODEL INFORMATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n\n"
        tOutput += "* DESCRIPTION\n"
        tOutput += "\t{}\n\n".format(Description)
        tOutput += "* SUMMARY\n"
        tOutput += "\tNUM. OF POINTS....................................... = {}\n".format(Point.Count)
        tOutput += "\tNUM. OF OUTLINES..................................... = {}\n".format(Outline.Count)
        tOutput += "\tNUM. OF MATERIALS.................................... = {}\n".format(Material.Count)
        tOutput += "\tNUM. OF GROUPS....................................... = {}\n\n".format(Group.Count)
        tOutput += "* ANALYSIS PARAMETERS\n"
        for (i, Type) in enumerate(AnalysisType):
            tOutput += "\tTYPE {}............................................. = {}\n".format(str(i).zfill(3), Type)
        tOutput += "\tELEMENT.............................................. = {}\n\n".format(Element)
        tOutput += "* MATERIAL DEFINITION\n"
        for (Index, i) in enumerate(Material.ID):
            tOutput += "\tID = {}; E = {:.4e}; G = {:.4e}; NU = {:.4e};\n".format(i, Material.E[i], Material.G[i], Material.nu[i])
            tOutput += "\tFY = {:.4e}; DENSITY = {:.4e}; ECU = {:.4e};\n".format(Material.Fy[i], Material.Density[i], Material.Epscu[i])
            tOutput += "\tSTRESS-STRAIN CURVE:\n"
            tOutput += "\t{:<16}{}\n".format("STRAIN.", "STRESS.")
            for P in Material.StressStrain[i]:
                tOutput += "\t{:<16.4e}{:.4e}\n".format(P[0], P[1])
            tOutput += "\n"
        tOutput += "* POINT COORDINATES IN GLOBAL AXIS\n"
        tOutput += "\t{:<8}{:<16}{}\n".format("ID.", "Y-COOR.", "Z-COOR.")
        for i in Point.ID:
            tOutput += "\t{:<8}{:<16.4e}{:.4e}\n".format(i, Point.Y[i], Point.Z[i])
        tOutput += "\n"
        tOutput += "* OUTLINE DEFINITION\n"
        tOutput += "\t{:<8}{:<12}{:<12}{:<12}{}\n".format("ID.", "POINTI.", "POINTJ.", "GROUP.", "TYPE")
        for i in Outline.ID:
            tOutput += "\t{:<8}{:<12}{:<12}{:<12}{}\n".format(i, Outline.Point1[i], Outline.Point2[i],
                                                                      Outline.GroupID[i], Outline.Type[i])
        tOutput += "\n"
        tOutput += "* GROUP DEFINITION\n"
        tOutput += "\t{:<8}{}\n".format("ID.", "MATERIAL.")
        for i in Group.ID:
            tOutput += "\t{:<8}{}\n".format(i, Group.MaterialID[i])
        return tOutput

    @staticmethod
    def BasicInfo(Material, Point, Outline, Group):
        tOutput = "\n"
        tOutput += "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODEL INFORMATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n\n"
        # tOutput += "* DESCRIPTION\n"
        # tOutput += "\t{}\n\n".format(Description)
        tOutput += "* SUMMARY\n"
        tOutput += "\tNUM. OF POINTS....................................... = {}\n".format(Point.Count)
        tOutput += "\tNUM. OF OUTLINES..................................... = {}\n".format(Outline.Count)
        tOutput += "\tNUM. OF MATERIALS.................................... = {}\n".format(Material.Count)
        tOutput += "\tNUM. OF GROUPS....................................... = {}\n\n".format(Group.Count)
        # tOutput += "* ANALYSIS PARAMETERS\n"
        # for (i, Type) in enumerate(AnalysisType):
        #     tOutput += "\tTYPE {}............................................. = {}\n".format(str(i).zfill(3), Type)
        # tOutput += "\tELEMENT.............................................. = {}\n\n".format(Element)
        tOutput += "* MATERIAL DEFINITION\n"
        for (Index, i) in enumerate(Material.ID):
            tOutput += "\tID = {}; E = {:.4e}; G = {:.4e}; NU = {:.4e};\n".format(i, Material.E[i], Material.G[i], Material.nu[i])
            tOutput += "\tFY = {:.4e}; DENSITY = {:.4e}; ECU = {:.4e};\n".format(Material.Fy[i], Material.Density[i], Material.eu[i])
            # tOutput += "\tSTRESS-STRAIN CURVE:\n"
            # tOutput += "\t{:<16}{}\n".format("STRAIN.", "STRESS.")
            # for P in Material.StressStrain[i]:
            #     tOutput += "\t{:<16.4e}{:.4e}\n".format(P[0], P[1])
            # tOutput += "\n"
        tOutput += "* POINT COORDINATES IN GLOBAL AXIS\n"
        tOutput += "\t{:<8}{:<16}{}\n".format("ID.", "Y-COOR.", "Z-COOR.")
        for i in Point.ID:
            tOutput += "\t{:<8}{:<16.4e}{:.4e}\n".format(i, Point.Y[i], Point.Z[i])
        tOutput += "\n"
        tOutput += "* OUTLINE DEFINITION\n"
        tOutput += "\t{:<8}{:<12}{:<12}{:<12}{}\n".format("ID.", "POINTI.", "POINTJ.", "GROUP.", "TYPE")
        for i in Outline.ID:
            tOutput += "\t{:<8}{:<12}{:<12}{:<12}{}\n".format(i, Outline.Point1[i], Outline.Point2[i],
                                                                      Outline.GroupID[i], Outline.Type[i])
        tOutput += "\n"
        tOutput += "* GROUP DEFINITION\n"
        tOutput += "\t{:<8}{}\n".format("ID.", "MATERIAL.")
        for i in Group.ID:
            tOutput += "\t{:<8}{}\n".format(i, Group.MaterialID[i])
        return tOutput


class MeshLog:
    def Info(GroupID, MeshSize, RunAutoMesh):
        tOutput = "\n"
        tOutput += "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MESH INFORMATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n\n"
        tOutput += "* SUMMARY\n"
        j = 0
        for i in GroupID:
            tOutput += "\tMESH SIZE FOR GROUP {}.............................. = {}\n".format(str(i).zfill(3), MeshSize[j])
            j += 1
        if RunAutoMesh == 1:
            tOutput += "\tAUTOMESH............................................. = Y\n\n"
        else:
            tOutput += "\tAUTOMESH............................................. = N\n\n"
        return tOutput

    def StartMesh(RunAutoMesh):
        if RunAutoMesh == 1:
            tOutput = "* AUTO MESH GENERATION\n"
            tOutput += "\tSTEP.\tNUM. OF NODES.\tNUM. OF ELEMENTS.\tDIFF. RATIO.\n"
        else:
            tOutput = "* MESH GENERATION\n"
            tOutput += "\tSTEP.\tNUM. OF NODES.\tNUM. OF ELEMENTS.\n"
        return tOutput

    def AutoMeshInfo(Step, NodeNum, EleNum, Diff):
        tOutput = "\t{:<8}{:<16}{:<20}{:.4e}\n".format(Step, NodeNum, EleNum, Diff)
        return tOutput

    def MeshInfo(NodeNum, EleNum):
        tOutput = "\t{:<8}{:<16}{}\n".format(1, NodeNum, EleNum)
        return tOutput


class BPLog:
    @staticmethod
    def CalSectProp(Fiber):
        tOutput = "\n"
        tOutput += "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SOLUTION START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n\n"
        tOutput += 'Calculating Section Properties...' + '\n'
        tOutput += "\tNUM. OF Fibers.... = {}\n".format(Fiber.Count)
        return tOutput

    def CalTorsionProp(self):
        tOutput = 'Calculating Torsion Properties...' + '\n'
        return tOutput

    def SolWarpingFunc(Dim):
        tOutput = 'Solving Warping Functions {0:n} × {0:n}...'.format(Dim) + '\n'
        return tOutput

    def CalShearProp(self):
        tOutput = 'Calculating Shear Properties...' + '\n'
        return tOutput

    def SolShearFunc(Dim):
        tOutput = 'Solving Shear Functions {0:n} × {0:n}...'.format(Dim) + '\n'
        return tOutput

    def SolPrinShearFunc(Dim):
        tOutput = 'Solving Principle Shear Functions {0:n} × {0:n}...'.format(Dim) + '\n'
        return tOutput

    @staticmethod
    def OutRes(SP):
        tOutput = "\n"
        tOutput += "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BASIC PROPERTIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        tOutput += "********************************************************************************\n\n"
        tOutput += "* GENERAL\n"
        tOutput += "\tCross-Section Area, A......................................... = {:.8e}\n".format(SP.Area)
        tOutput += "\tCentroid, Y................................................... = {:.8e}\n".format(SP.cy)
        tOutput += "\tCentroid, Z................................................... = {:.8e}\n".format(SP.cz)
        tOutput += "\tPlastic Centroid, Yp.......................................... = {:.8e}\n".format(SP.cyp)
        tOutput += "\tPlastic Centroid, Zp.......................................... = {:.8e}\n".format(SP.czp)
        tOutput += "\tShear Centre WRT Centroid, Ys................................. = {:.8e}\n".format(SP.ysc)
        tOutput += "\tShear Centre WRT Centroid, Zs................................. = {:.8e}\n".format(SP.zsc)
        tOutput += "\tTorsional Constant, J......................................... = {:.8e}\n".format(SP.J)
        tOutput += "\tWarping Constant, Iomg........................................ = {:.8e}\n".format(SP.Iomg)
        tOutput += "\tPrinciple bending angle (rad)................................. = {:.8e}\n".format(SP.Theta)
        tOutput += "\tPrinciple bending angle (deg)................................. = {:.8e}\n\n".format(np.rad2deg(SP.Theta))
        tOutput += "* SECTION PROPERTIES ABOUT USER-DEFINED AXIS\n"
        tOutput += "\tMoment of Inertia, Iy......................................... = {:.8e}\n".format(SP.Iyc)
        tOutput += "\tMoment of Inertia, Iz......................................... = {:.8e}\n".format(SP.Izc)
        tOutput += "\tProduct of Inertia, Iyz....................................... = {:.8e}\n".format(SP.Iyzc)
        tOutput += "\tElastic Section Modulus, Sy................................... = {:.8e}\n".format(SP.Sy)
        tOutput += "\tElastic Section Modulus, Sz................................... = {:.8e}\n".format(SP.Sz)
        tOutput += "\tPlastic Section Modulus, Zy................................... = {:.8e}\n".format(SP.Zy)
        tOutput += "\tPlastic Section Modulus, Zz................................... = {:.8e}\n".format(SP.Zz)
        tOutput += "\tPlastic Tortional Modulus, Zt................................. = {:.8e}\n".format(SP.Zt)
        tOutput += "\tRadius of Gyration, ry........................................ = {:.8e}\n".format(SP.ry)
        tOutput += "\tRadius of Gyration, rz........................................ = {:.8e}\n".format(SP.rz)
        tOutput += "\tWagner Coefficient, Betay..................................... = {:.8e}\n".format(SP.Betay)
        tOutput += "\tWagner Coefficient, Betaz..................................... = {:.8e}\n".format(SP.Betaz)
        tOutput += "\tWagner Coefficient, Betaomg................................... = {:.8e}\n".format(SP.Betaomg)
        tOutput += "\tShear Coefficient, ky......................................... = {:.8e}\n".format(SP.ky)
        tOutput += "\tShear Coefficient, kz......................................... = {:.8e}\n\n".format(SP.kz)
        tOutput += "* SECTION PROPERTIES ABOUT PRINCIPAL AXIS\n"
        tOutput += "\tPrinciple moment of inertia, Iv............................... = {:.8e}\n".format(SP.Iv)
        tOutput += "\tPrinciple moment of inertia, Iw............................... = {:.8e}\n".format(SP.Iw)
        tOutput += "\tPrinciple elastic section modulus, Sv......................... = {:.8e}\n".format(SP.Sv)
        tOutput += "\tPrinciple elastic section modulus, Sw......................... = {:.8e}\n".format(SP.Sw)
        tOutput += "\tPrinciple plastic section modulus, Zv......................... = {:.8e}\n".format(SP.Zv)
        tOutput += "\tPrinciple plastic section modulus, Zw......................... = {:.8e}\n".format(SP.Zw)
        tOutput += "\tRadius of gyration, rv........................................ = {:.8e}\n".format(SP.rv)
        tOutput += "\tRadius of gyration, rw........................................ = {:.8e}\n".format(SP.rw)
        tOutput += "\tWagner Coefficient, Betav..................................... = {:.8e}\n".format(SP.Betav)
        tOutput += "\tWagner Coefficient, Betaw..................................... = {:.8e}\n".format(SP.Betaw)
        tOutput += "\tWagner Coefficient, Betaomg................................... = {:.8e}\n".format(SP.Betaomg)
        tOutput += "\tShear Coefficient, kv......................................... = {:.8e}\n".format(SP.kv)
        tOutput += "\tShear Coefficient, kw......................................... = {:.8e}\n".format(SP.kw)
        return tOutput