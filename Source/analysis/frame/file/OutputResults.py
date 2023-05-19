#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Description:
# ===========================================================================
# Import standard libraries
import numpy as np
import csv
import os

# Import internal functions
from analysis.frame.variables import Result
from analysis.frame.variables import Model

# ===========================================================================

def IniCSV(fileName,Headings):
    with open(fileName,'w+',newline='') as disRes:
        myWriter=csv.writer(disRes)
        myWriter.writerow(Headings)

def AddCSVRow(fileName, RowRes):
    with open(fileName,'a',newline='') as disRes:
        myWriter=csv.writer(disRes)
        myWriter.writerow(RowRes)

def IniResults():
    ResultFolder = Model.OutResult.FileName + '.rst'
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Dis.csv'
    Headings = ["LF", "ID", "UX", "UY", "UZ", "RX", "RY", "RZ", "B"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName +  '-Bound.csv'
    Headings = ["LF", "ID", "FX", "FY", "FZ", "MX", "MY", "MZ", "MB"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName +  '-Mem.csv'
    Headings = ["LF","ID","FX1","FY1","FZ1","MX1","MY1","MZ1","MB1","FX2","FY2","FZ2","MX2","MY2","MZ2","MB2"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName +  '-MemDisinGaussPoint.csv'
    Headings = ["LF","ID","GaussPoint","GaussPointCoeff","UX","UY","UZ","ThetaX"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName +  '-MemForceinGaussPoint.csv'
    Headings = ["LF","ID","GaussPoint","GaussPointCoeff","Px","FY","FZ","MX","MY","MZ","MB"]
    IniCSV(fileName, Headings)
    # ------------------------------------------------------------------------------------------------------------------
    if (Model.Analysis.Type == 'dynamicNonlinear' or Model.Analysis.Type == 'dynamicLoinear'):
        fileName = ResultFolder + os.sep + Model.OutResult.ModelName +  '-Vel.csv'
        Headings = ["Time", "ID", "VelUX", "VelUY", "VelUZ", "VelRX", "VelRY", "VelRZ", "VelB"]
        IniCSV(fileName, Headings)
        # --------------------------------------------------------------------------------------------------------------
        fileName = ResultFolder + os.sep + Model.OutResult.ModelName +  '-Acc.csv'
        Headings = ["Time", "ID", "AccUX", "AccUY", "AccUZ", "AccRX", "AccRY", "AccRZ", "AccB"]
        IniCSV(fileName, Headings)
    return

def OutCyCRes(result):
    ResultFolder = Model.OutResult.FileName + '.rst'
    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Dis.csv'
    #csvfile = file(folder+fileName,'wb')
    if Model.Analysis.SolnTech =="Dis":
        RowRes = list(np.zeros(9))
        RowRes[0] = result.CyCRes.LF
        tID = Model.Node.ID[Model.Analysis.CtlNode]
        RowRes[1] = Model.Analysis.CtlNode
        RowRes[2] = result.CyCRes.CurU[tID * 7]
        RowRes[3] = result.CyCRes.CurU[tID * 7 + 1]
        RowRes[4] = result.CyCRes.CurU[tID * 7 + 2]
        RowRes[5] = result.CyCRes.CurU[tID * 7 + 3]
        RowRes[6] = result.CyCRes.CurU[tID * 7 + 4]
        RowRes[7] = result.CyCRes.CurU[tID * 7 + 5]
        RowRes[8] = result.CyCRes.CurU[tID * 7 + 6]
    else:
        for ii in Model.Node.ID:
            tvID = Model.Node.ID[ii]
            RowRes = list(np.zeros(9))
            RowRes[0] = result.CyCRes.LF
            RowRes[1] = ii
            RowRes[2] = result.CyCRes.CurU[tvID * 7]
            RowRes[3] = result.CyCRes.CurU[tvID * 7 + 1]
            RowRes[4] = result.CyCRes.CurU[tvID * 7 + 2]
            RowRes[5] = result.CyCRes.CurU[tvID * 7 + 3]
            RowRes[6] = result.CyCRes.CurU[tvID * 7 + 4]
            RowRes[7] = result.CyCRes.CurU[tvID * 7 + 5]
            RowRes[8] = result.CyCRes.CurU[tvID * 7 + 6]
            AddCSVRow(fileName, RowRes)

    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Bound.csv'
    for ii in Model.Boundary.NodeID:
        tvBoundID = Model.Boundary.NodeID[ii]
        RowRes = list(np.zeros(9))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        RowRes[2] = result.CyCRes.Rect[tvBoundID, 0]
        RowRes[3] = result.CyCRes.Rect[tvBoundID, 1]
        RowRes[4] = result.CyCRes.Rect[tvBoundID, 2]
        RowRes[5] = result.CyCRes.Rect[tvBoundID, 3]
        RowRes[6] = result.CyCRes.Rect[tvBoundID, 4]
        RowRes[7] = result.CyCRes.Rect[tvBoundID, 5]
        RowRes[8] = result.CyCRes.Rect[tvBoundID, 6]
        AddCSVRow(fileName, RowRes)

    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Mem.csv'
    for ii in Model.Member.ID:
        if len(Model.Member.ID) >= 2:
            tvMID = Model.Member.ID[ii]
            RowRes = list(np.zeros(16))
            RowRes[0] = result.CyCRes.LF
            RowRes[1] = ii
            RowRes[2] = result.CyCRes.MemF[tvMID, 0]
            RowRes[3] = result.CyCRes.MemF[tvMID, 1]
            RowRes[4] = result.CyCRes.MemF[tvMID, 2]
            RowRes[5] = result.CyCRes.MemF[tvMID, 3]
            RowRes[6] = result.CyCRes.MemF[tvMID, 4]
            RowRes[7] = result.CyCRes.MemF[tvMID, 5]
            RowRes[8] = result.CyCRes.MemF[tvMID, 6]
            RowRes[9] = result.CyCRes.MemF[tvMID, 7]
            RowRes[10] = result.CyCRes.MemF[tvMID, 8]
            RowRes[11] = result.CyCRes.MemF[tvMID, 9]
            RowRes[12] = result.CyCRes.MemF[tvMID, 10]
            RowRes[13] = result.CyCRes.MemF[tvMID, 11]
            RowRes[14] = result.CyCRes.MemF[tvMID, 12]
            RowRes[15] = result.CyCRes.MemF[tvMID, 13]
        else:
            #tvMID = Model.Member.ID[ii]
            RowRes = list(np.zeros(16))
            RowRes[0] = result.CyCRes.LF
            RowRes[1] = ii
            RowRes[2] = result.CyCRes.MemF[0]
            RowRes[3] = result.CyCRes.MemF[1]
            RowRes[4] = result.CyCRes.MemF[2]
            RowRes[5] = result.CyCRes.MemF[3]
            RowRes[6] = result.CyCRes.MemF[4]
            RowRes[7] = result.CyCRes.MemF[5]
            RowRes[8] = result.CyCRes.MemF[6]
            RowRes[9] = result.CyCRes.MemF[7]
            RowRes[10] = result.CyCRes.MemF[8]
            RowRes[11] = result.CyCRes.MemF[9]
            RowRes[12] = result.CyCRes.MemF[10]
            RowRes[13] = result.CyCRes.MemF[11]
            RowRes[14] = result.CyCRes.MemF[12]
            RowRes[15] = result.CyCRes.MemF[13]
        AddCSVRow(fileName, RowRes)

    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-MemDisinGaussPoint.csv'
    # tID = Model.Node.ID[Model.Analysis.CtlNode]
    GaussPointCoefficients = [0.025446, 0.129234, 0.297077, 0.500000, 0.702923, 0.870766, 0.974554]
    GaussPointNum = 7
    for ii in Model.Member.ID:
        RowRes =list(np.zeros(8))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        tI = Model.Node.ID[Model.Member.I[ii]]
        tJ = Model.Node.ID[Model.Member.J[ii]]
        L = Model.Member.L0[ii]
        ##
        for jj in range(GaussPointNum):
            tGPC = GaussPointCoefficients[jj]
            RowRes[2] = jj
            RowRes[3] = tGPC
            u1 = result.CyCRes.CurU[tI * 7]
            u2 = result.CyCRes.CurU[tJ * 7]
            v1 = result.CyCRes.CurU[tI * 7 + 1]
            v2 = result.CyCRes.CurU[tJ * 7 + 1]
            w1 = result.CyCRes.CurU[tI * 7 + 2]
            w2 = result.CyCRes.CurU[tJ * 7 + 2]
            Rx1 = result.CyCRes.CurU[tI * 7 + 3]
            Rx2 = result.CyCRes.CurU[tJ * 7 + 3]
            Ry1 = result.CyCRes.CurU[tI * 7 + 4]
            Ry2 = result.CyCRes.CurU[tJ * 7 + 4]
            Rz1 = result.CyCRes.CurU[tI * 7 + 5]
            Rz2 = result.CyCRes.CurU[tJ * 7 + 5]
            Rb1 = result.CyCRes.CurU[tI * 7 + 6]
            Rb2 = result.CyCRes.CurU[tJ * 7 + 6]
            #%%#
            RowRes[4] = (1-tGPC) * u1 + tGPC * u2
            RowRes[5] = v2*(3.0*tGPC**2-2.0*tGPC**3)+v1*(1-3.0*tGPC**2+2.0*tGPC**3)+\
                        Rz1*(tGPC*L-2*tGPC/L+tGPC**2*tGPC*L) - Rz2*(tGPC/L-tGPC**2*tGPC*L)
            RowRes[6] = w2*(3.0*tGPC**2-2.0*tGPC**3)+w1*(1-3.0*tGPC**2+2.0*tGPC**3)-\
                        Ry1*(tGPC*L-2*tGPC/L+tGPC**2*tGPC*L) + Ry2*(tGPC/L-tGPC**2*tGPC*L)
            RowRes[7] = Rb1*(tGPC*L-2*tGPC/L+tGPC**2*tGPC*L) + Rb2*(tGPC/L-tGPC**2*tGPC*L)+\
                        Rx1*(1-3.0*tGPC**2+2.0*tGPC**3) + Rx2*(3.0*tGPC**2-2.0*tGPC**3)
            AddCSVRow(fileName, RowRes)

    fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-MemForceinGaussPoint.csv'
    for ii in Model.Member.ID:
        tvMID = Model.Member.ID[ii]
        RowRes = list(np.zeros(11))
        RowRes[0] = result.CyCRes.LF
        RowRes[1] = ii
        # tI = Model.Node.ID[Model.Member.I[ii]]
        # tJ = Model.Node.ID[Model.Member.J[ii]]
        L = Model.Member.L0[ii]
        for jj in range(GaussPointNum):
            ##
            tGPC = GaussPointCoefficients[jj]
            RowRes[2] = jj
            RowRes[3] = tGPC
            if len(Model.Member.ID) >= 2:
                Fx1 = result.CyCRes.MemF[tvMID, 0]
                Fx2 = result.CyCRes.MemF[tvMID, 7]
                Fy1 = result.CyCRes.MemF[tvMID, 1]
                Fy2 = result.CyCRes.MemF[tvMID, 8]
                Fz1 = result.CyCRes.MemF[tvMID, 2]
                Fz2 = result.CyCRes.MemF[tvMID, 9]
                Mx1 = result.CyCRes.MemF[tvMID, 3]
                Mx2 = result.CyCRes.MemF[tvMID, 10]
                My1 = result.CyCRes.MemF[tvMID, 4]
                My2 = result.CyCRes.MemF[tvMID, 11]
                Mz1 = result.CyCRes.MemF[tvMID, 5]
                Mz2 = result.CyCRes.MemF[tvMID, 12]
                Mb1 = result.CyCRes.MemF[tvMID, 6]
                Mb2 = result.CyCRes.MemF[tvMID, 13]
            else:
                Fx1 = result.CyCRes.MemF[0]
                Fx2 = result.CyCRes.MemF[7]
                Fy1 = result.CyCRes.MemF[1]
                Fy2 = result.CyCRes.MemF[8]
                Fz1 = result.CyCRes.MemF[2]
                Fz2 = result.CyCRes.MemF[9]
                Mx1 = result.CyCRes.MemF[3]
                Mx2 = result.CyCRes.MemF[10]
                My1 = result.CyCRes.MemF[4]
                My2 = result.CyCRes.MemF[11]
                Mz1 = result.CyCRes.MemF[5]
                Mz2 = result.CyCRes.MemF[12]
                Mb1 = result.CyCRes.MemF[6]
                Mb2 = result.CyCRes.MemF[13]

            RowRes[4] = (1-tGPC) * Fx1 + tGPC * Fx2
            RowRes[5] = Fy2*(3.0*tGPC**2-2.0*tGPC**3)+Fy1*(1-3.0*tGPC**2+2.0*tGPC**3)+\
                        Mz1*(tGPC*L-2*tGPC/L+tGPC**2*tGPC*L) - Mz2*(tGPC/L-tGPC**2*tGPC*L)
            RowRes[6] = Fz2*(3.0*tGPC**2-2.0*tGPC**3)+Fz1*(1-3.0*tGPC**2+2.0*tGPC**3)-\
                        My1*(tGPC*L-2*tGPC/L+tGPC**2*tGPC*L) + My2*(tGPC/L-tGPC**2*tGPC*L)
            RowRes[7] = Mb1*(tGPC*L-2*tGPC/L+tGPC**2*tGPC*L) + Mb2*(tGPC/L-tGPC**2*tGPC*L)+\
                        Mx1*(1-3.0*tGPC**2+2.0*tGPC**3) + Mx2*(3.0*tGPC**2-2.0*tGPC**3)
            AddCSVRow(fileName, RowRes)


    if Model.Analysis.Type == "dynamicNonlinear":
        fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Vel.csv'
        for ii in Model.Node.ID:
            tvID = Model.Node.ID[ii]
            RowRes = list(np.zeros(9))
            RowRes[0] = result.CyCRes.Time
            RowRes[1] = ii
            RowRes[2] = result.CyCRes.VEL[tvID * 7]
            RowRes[3] = result.CyCRes.VEL[tvID * 7 + 1]
            RowRes[4] = result.CyCRes.VEL[tvID * 7 + 2]
            RowRes[5] = result.CyCRes.VEL[tvID * 7 + 3]
            RowRes[6] = result.CyCRes.VEL[tvID * 7 + 4]
            RowRes[7] = result.CyCRes.VEL[tvID * 7 + 5]
            RowRes[8] = result.CyCRes.VEL[tvID * 7 + 6]
            AddCSVRow(fileName, RowRes)

        fileName = ResultFolder + os.sep + Model.OutResult.ModelName + '-Acc.csv'
        for ii in Model.Node.ID:
            tvID = Model.Node.ID[ii]
            RowRes = list(np.zeros(9))
            RowRes[0] = result.CyCRes.Time
            RowRes[1] = ii
            RowRes[2] = result.CyCRes.ACC[tvID * 7]
            RowRes[3] = result.CyCRes.ACC[tvID * 7 + 1]
            RowRes[4] = result.CyCRes.ACC[tvID * 7 + 2]
            RowRes[5] = result.CyCRes.ACC[tvID * 7 + 3]
            RowRes[6] = result.CyCRes.ACC[tvID * 7 + 4]
            RowRes[7] = result.CyCRes.ACC[tvID * 7 + 5]
            RowRes[8] = result.CyCRes.ACC[tvID * 7 + 6]
            AddCSVRow(fileName, RowRes)