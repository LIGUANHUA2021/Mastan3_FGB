###########################################################################################
#
# MSASolid - Finite element analysis with solid element model (v0.0.1)
#
# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Function purpose:
# =========================================================================================
# Import standard libraries
#import numpy as np
#import math
import timeit, sys, logging, os, codecs
import numpy as np
# Import internal functions
# =========================================================================================
from analysis.solid.variables.Model import OutResult


def Print(message):
    print(message)
    LogFile.Output += message
    return


class MainLog:
    @staticmethod
    def StartMessage(tName, tAuthors, tRevisedDate):
        tOutput = "********************************************************************************\n"
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PyFESect ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
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
    ##
    @staticmethod
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
