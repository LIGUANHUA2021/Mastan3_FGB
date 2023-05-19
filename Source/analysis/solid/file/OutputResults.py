#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import csv
import os

# Import internal functions
from analysis.solid.variables import Model

def IniCSV(fileName,Headings):
    with open(fileName, 'w+', newline='') as disRes:
        myWriter = csv.writer(disRes)
        myWriter.writerow(Headings)

def AddCSVRow(fileName, RowRes):
    with open(fileName, 'a', newline='') as disRes:
        myWriter = csv.writer(disRes)
        myWriter.writerow(RowRes)

def IniResults():
    ResultFolder = Model.OutResult.FileName + '.rst'
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Dis.csv'
    Headings = ["LF", "ID", "UX", "UY", "UZ"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Bound.csv'
    Headings = ["LF", "ID", "FX", "FY", "FZ"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-ElementStress.csv'
    Headings = ["LF", "ID", "S11", "S22", "S33", "S12", "S23", "S13"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-ElementPStress.csv'
    Headings = ["LF", "ID", "S11", "S22", "S33"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    return

def IniResults_Eigen():
    ResultFolder = Model.OutResult.FileName + '.rst'
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-EigenBuckling.csv'
    Headings = ["Mode NO.", "Load Factor"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    return

def OutCyCRes_Eigen(result):
    ResultFolder = Model.OutResult.FileName + '.rst'
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-EigenBuckling.csv'
    EigenBuckling_rst = result.CyCRes.EigenBuckling
    RowRes = list(np.zeros(2))
    for ii in EigenBuckling_rst:
        RowRes[0] = ii
        RowRes[1] = EigenBuckling_rst[ii]
        AddCSVRow(fileName, RowRes)
    return


def OutCyCRes(result):
    ResultFolder = Model.OutResult.FileName + '.rst'
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Dis.csv'
    for ii in Model.Node.ID:
        tvID = Model.Node.ID[ii]
        RowRes = list(np.zeros(5))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        RowRes[2] = result.CyCRes.CurU[tvID * 3]
        RowRes[3] = result.CyCRes.CurU[tvID * 3 + 1]
        RowRes[4] = result.CyCRes.CurU[tvID * 3 + 2]
        AddCSVRow(fileName, RowRes)
    ##
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Bound.csv'
    for ii in Model.Boundary.NodeID:
        tvBoundID = Model.Boundary.NodeID[ii]
        RowRes = list(np.zeros(5))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        RowRes[2] = result.CyCRes.Rect[tvBoundID, 0]
        RowRes[3] = result.CyCRes.Rect[tvBoundID, 1]
        RowRes[4] = result.CyCRes.Rect[tvBoundID, 2]
        AddCSVRow(fileName, RowRes)
    ##
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-ElementStress.csv'
    for ii in Model.Element.ID:
        tEleStrs = result.CyCRes.EleStrs[ii]
        tEleStrs_list = list(tEleStrs)
        # tvID = Model.Element.ID[ii]
        RowRes = list(np.zeros(8))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        RowRes[2] = tEleStrs_list[0]
        RowRes[3] = tEleStrs_list[1]
        RowRes[4] = tEleStrs_list[2]
        RowRes[5] = tEleStrs_list[3]
        RowRes[6] = tEleStrs_list[4]
        RowRes[7] = tEleStrs_list[5]
        AddCSVRow(fileName, RowRes)
    ##
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-ElementPStress.csv'
    for ii in Model.Element.ID:
        tElePStrs = result.CyCRes.ElePStrs[ii]
        tElePStrs_list = list(tElePStrs)
        RowRes = list(np.zeros(5))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        RowRes[2] = tElePStrs_list[0]
        RowRes[3] = tElePStrs_list[1]
        RowRes[4] = tElePStrs_list[2]
        AddCSVRow(fileName, RowRes)
    return