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
import numpy as np
import timeit
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
# =========================================================================================
# Import internal functions
from analysis.FESect.variables import Model
from analysis.FESect.variables.Result import SectionProperties as SP
from analysis.FESect.util import GaussianQuadrature as GQ
from analysis.FESect.util import PrintLog as pl
from analysis.FESect.element import Tri3
from analysis.FESect.file.OutputResults import BPRes
from analysis.FESect.variables.Model import Fiber


def GetPerimeter(ID, OutlineType, Point1, Point2, Y, Z):
    Perimeter = 0
    for i in ID:
        if OutlineType[i] == "S":
            Perimeter += np.sqrt((Y[Point1[i]] - Y[Point2[i]]) ** 2 + (Z[Point1[i]] - Z[Point2[i]]) ** 2)
    return Perimeter


def GetIyIz(ID, FiberA, FiberIy, FiberIz, FiberCy, FiberCz, Y0, Z0, E_ref):
    EIy = 0
    EIz = 0
    for i in ID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        EIy += E * (FiberIy[i] + FiberA[i] * (FiberCz[i] - Z0) ** 2)
        EIz += E * (FiberIz[i] + FiberA[i] * (FiberCy[i] - Y0) ** 2)
    Iy = EIy / E_ref
    Iz = EIz / E_ref
    return Iy, Iz


def GetIyz(ID, FiberA, FiberIyz, FiberCy, FiberCz, Y0, Z0, E_ref):
    EIyz = 0
    for i in ID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        EIyz += E * (FiberIyz[i] + FiberA[i] * (FiberCy[i] - Y0) * (FiberCz[i] - Z0))
    Iyz = EIyz / E_ref
    return Iyz


def SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, AxisV, E_ref):
    EAc = 0
    EAt = 0
    for i in ID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        if VList[PointI[i]] >= AxisV and VList[PointJ[i]] >= AxisV and VList[PointK[i]] >= AxisV:
            EAc += E * FiberArea[i]
        elif VList[PointI[i]] <= AxisV and VList[PointJ[i]] <= AxisV and VList[PointK[i]] <= AxisV:
            EAt += E * FiberArea[i]
        else:
            (tAc, tAt) = Tri3.TruncatedTriangleAreas([VList[PointI[i]], VList[PointJ[i]], VList[PointK[i]]],
                                                     [WList[PointI[i]], WList[PointJ[i]], WList[PointK[i]]],
                                                     FiberArea[i], AxisV)
            EAc += E * tAc
            EAt += E * tAt
    Ac = EAc / E_ref
    At = EAt / E_ref
    return Ac, At


def GetPNA(VList, WList, ID, PointI, PointJ, PointK, FiberArea, SectA, E_ref):
    Vu = max(VList.values())
    Vl = min(VList.values())

    Acu = SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, Vu, E_ref)[0]
    Acl = SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, Vl, E_ref)[0]
    Vn = Vl + (Vu - Vl) / (Acu - Acl) * (SectA / 2 - Acl)

    (Acn, Atn) = SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, Vn, E_ref)

    while abs(Acn - Atn) >= SectA / 10000:
        Vn = Vl + (Vu - Vl) / (Acu - Acl) * (SectA / 2 - Acl)
        (Acn, Atn) = SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, Vn, E_ref)

        if Acn > Atn:
            Vl = Vn
        elif Acn < Atn:
            Vu = Vn
        elif Acn == Atn:
            break

        Acu = SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, Vu, E_ref)[0]
        Acl = SumBilateralAreas(ID, VList, WList, PointI, PointJ, PointK, FiberArea, Vl, E_ref)[0]

    return Vn


def GetZyZz(NodeY, NodeZ, ID, PointI, PointJ, PointK, FiberArea, FiberCy, FiberCz, cyp, czp, E_ref):
    EQyc = 0
    EQyt = 0
    EQzc = 0
    EQzt = 0
    for i in ID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        if NodeZ[PointI[i]] >= czp and NodeZ[PointJ[i]] >= czp and NodeZ[PointK[i]] >= czp:
            EQyc += E * FiberArea[i] * (FiberCz[i] - czp)
        elif NodeZ[PointI[i]] <= czp and NodeZ[PointJ[i]] <= czp and NodeZ[PointK[i]] <= czp:
            EQyt += E * FiberArea[i] * (czp - FiberCz[i])
        else:
            (tQyc, tQyt) = Tri3.TruncatedTriangleStatics([NodeZ[PointI[i]], NodeZ[PointJ[i]], NodeZ[PointK[i]]],
                                                         [NodeY[PointI[i]], NodeY[PointJ[i]], NodeY[PointK[i]]],
                                                         FiberArea[i], czp)
            EQyc += E * tQyc
            EQyt += E * tQyt
        if NodeY[PointI[i]] >= cyp and NodeY[PointJ[i]] >= cyp and NodeY[PointK[i]] >= cyp:
            EQzc += E * FiberArea[i] * (FiberCy[i] - cyp)
        elif NodeY[PointI[i]] <= cyp and NodeY[PointJ[i]] <= cyp and NodeY[PointK[i]] <= cyp:
            EQzt += E * FiberArea[i] * (cyp - FiberCy[i])
        else:
            (tQzc, tQzt) = Tri3.TruncatedTriangleStatics([NodeY[PointI[i]], NodeY[PointJ[i]], NodeY[PointK[i]]],
                                                         [NodeZ[PointI[i]], NodeZ[PointJ[i]], NodeZ[PointK[i]]],
                                                         FiberArea[i], cyp)
            EQzc += E * tQzc
            EQzt += E * tQzt
    Zy = (EQyc + EQyt) / E_ref
    Zz = (EQzc + EQzt) / E_ref
    return Zy, Zz


def FormTotalKP(NodeNum, NodeID, FiberID, Nodey, Nodez, PointI, PointJ, PointK, GPNum):
    KT = np.zeros([NodeNum, NodeNum])
    PT = np.zeros([NodeNum, 1])
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        tI = NodeID[PointI[i]]
        tJ = NodeID[PointJ[i]]
        tK = NodeID[PointK[i]]
        (Ke, Pe) = Tri3.GetKePe([Nodey[PointI[i]], Nodey[PointJ[i]], Nodey[PointK[i]]],
                                [Nodez[PointI[i]], Nodez[PointJ[i]], Nodez[PointK[i]]],
                                GPNum, GPs, Wts)
        KT[tI, tI] += Ke[0, 0]
        KT[tI, tJ] += Ke[0, 1]
        KT[tI, tK] += Ke[0, 2]
        KT[tJ, tI] += Ke[1, 0]
        KT[tJ, tJ] += Ke[1, 1]
        KT[tJ, tK] += Ke[1, 2]
        KT[tK, tI] += Ke[2, 0]
        KT[tK, tJ] += Ke[2, 1]
        KT[tK, tK] += Ke[2, 2]
        PT[tI] += Pe[0]
        PT[tJ] += Pe[1]
        PT[tK] += Pe[2]
    return KT, PT


def GetOmegaWRTCentroid(NodeNum, NodeID, Nodey, Nodez, FiberID, PointI, PointJ, PointK, GPNum):
    (KT, PT) = FormTotalKP(NodeNum, NodeID, FiberID, Nodey, Nodez, PointI, PointJ, PointK, GPNum)
    tKT = KT[1:, 1:]
    tPT = PT[1:]
    CSRKT = csr_matrix(tKT)
    tOmegaInit = np.squeeze(spsolve(CSRKT, tPT))
    OmegaInit = np.hstack((np.zeros(1), tOmegaInit))
    return OmegaInit


def GetAomg(NodeV, NodeW, NodeOmega, PointI, PointJ, PointK, FiberID, GPNum, E_ref):
    EAomg = 0
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        tAomg = Tri3.GetAomg([NodeV[PointI[i]], NodeV[PointJ[i]], NodeV[PointK[i]]],
                             [NodeW[PointI[i]], NodeW[PointJ[i]], NodeW[PointK[i]]],
                             [NodeOmega[PointI[i]], NodeOmega[PointJ[i]], NodeOmega[PointK[i]]],
                             GPNum, GPs, Wts)
        EAomg += E * tAomg
    Aomg = EAomg / E_ref
    return Aomg


def GetAvomgAwomg(NodeV, NodeW, NodeOmega, PointI, PointJ, PointK, FiberID, GPNum, E_ref):
    EAvomg = 0
    EAwomg = 0
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        (tAvomg, tAwomg) = Tri3.GetAvomgAwomg([NodeV[PointI[i]], NodeV[PointJ[i]], NodeV[PointK[i]]],
                                              [NodeW[PointI[i]], NodeW[PointJ[i]], NodeW[PointK[i]]],
                                              [NodeOmega[PointI[i]], NodeOmega[PointJ[i]], NodeOmega[PointK[i]]],
                                              GPNum, GPs, Wts)
        EAvomg += E * tAvomg
        EAwomg += E * tAwomg
    Avomg = EAvomg / E_ref
    Awomg = EAwomg / E_ref
    return Avomg, Awomg


def GetPrincipleShearCentre(NodeV, NodeW, NodeOmega, FiberID, PointI, PointJ, PointK, Iv, Iw, GPNum, E_ref):
    (Avomg, Awomg) = GetAvomgAwomg(NodeV, NodeW, NodeOmega, PointI, PointJ, PointK, FiberID, GPNum, E_ref)
    cvs = Awomg / Iv
    cws = -Avomg / Iw
    return cvs, cws


def StandardizeOmega(NodeV, NodeW, NodeOmega, FiberID, PointI, PointJ, PointK, cvs, cws, A, GPNum, E_ref):
    Aomg = GetAomg(NodeV, NodeW, NodeOmega, PointI, PointJ, PointK, FiberID, GPNum, E_ref)
    OmegaK = Aomg / A
    Omega = np.array(list(NodeOmega.values())) - OmegaK - cvs * np.array(list(NodeW.values())) + cws * np.array(list(NodeV.values()))
    return Omega


def GetJ(NodeY, NodeZ, NodeOmega, FiberID, PointI, PointJ, PointK, cys, czs, GPNum, G_ref):
    GJ = 0
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        G = Model.Material.G[mat_id]
        tJ = Tri3.GetJ([NodeY[PointI[i]], NodeY[PointJ[i]], NodeY[PointK[i]]],
                       [NodeZ[PointI[i]], NodeZ[PointJ[i]], NodeZ[PointK[i]]],
                       [NodeOmega[PointI[i]], NodeOmega[PointJ[i]], NodeOmega[PointK[i]]],
                       cys, czs, GPNum, GPs, Wts)
        GJ += G * tJ
    J = GJ / G_ref
    return J


def GetIomg(NodeY, NodeZ, NodeOmega, FiberID, PointI, PointJ, PointK, GPNum, G_ref):
    GIomg = 0
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        G = Model.Material.G[mat_id]
        tIomg = Tri3.GetIomg([NodeY[PointI[i]], NodeY[PointJ[i]], NodeY[PointK[i]]],
                             [NodeZ[PointI[i]], NodeZ[PointJ[i]], NodeZ[PointK[i]]],
                             [NodeOmega[PointI[i]], NodeOmega[PointJ[i]], NodeOmega[PointK[i]]],
                             GPNum, GPs, Wts)
        GIomg += G * tIomg
    Iomg = GIomg / G_ref
    return Iomg


def GetWagnerCoef(NodeY, NodeZ, NodeOmega, FiberID, PointI, PointJ, PointK, ysc, zsc, Iy, Iz, Iomg, GPNum, E_ref, G_ref):
    tEBetay = 0
    tEBetaz = 0
    tGBetaomg = 0
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        E = Model.Material.E[mat_id]
        G = Model.Material.G[mat_id]
        (ttBetay, ttBetaz, ttBetaomg) = Tri3.GetWagnerCoefIntg([NodeY[PointI[i]], NodeY[PointJ[i]], NodeY[PointK[i]]],
                                                               [NodeZ[PointI[i]], NodeZ[PointJ[i]], NodeZ[PointK[i]]],
                                                               [NodeOmega[PointI[i]], NodeOmega[PointJ[i]], NodeOmega[PointK[i]]],
                                                               GPNum, GPs, Wts)
        tEBetay += E * ttBetay
        tEBetaz += E * ttBetaz
        tGBetaomg += G * ttBetaomg
    tBetay = tEBetay / E_ref
    tBetaz = tEBetaz / E_ref
    tBetaomg = tGBetaomg / G_ref
    Betay = tBetay / Iy - 2 * zsc
    Betaz = tBetaz / Iz - 2 * ysc
    Betaomg = tBetaomg / Iomg
    return Betay, Betaz, Betaomg


def FormShearLoad(Iy, Iz, Iyz, NodeNum, NodeID, FiberID, Nodey, Nodez, PointI, PointJ, PointK, GPNum):
    PTy = np.zeros([NodeNum, 1])
    PTz = np.zeros([NodeNum, 1])
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        nu = Model.Material.nu[mat_id]
        tI = NodeID[PointI[i]]
        tJ = NodeID[PointJ[i]]
        tK = NodeID[PointK[i]]
        (Pey, Pez) = Tri3.GetShearLoad([Nodey[PointI[i]], Nodey[PointJ[i]], Nodey[PointK[i]]],
                                       [Nodez[PointI[i]], Nodez[PointJ[i]], Nodez[PointK[i]]],
                                       Iy, Iz, Iyz, nu, GPNum, GPs, Wts)
        PTy[tI] += Pey[0]
        PTy[tJ] += Pey[1]
        PTy[tK] += Pey[2]
        PTz[tI] += Pez[0]
        PTz[tJ] += Pez[1]
        PTz[tK] += Pez[2]
    return PTy, PTz


def GetShearFunction(NodeNum, NodeID, Nodey, Nodez, FiberID, PointI, PointJ, PointK, Iy, Iz, Iyz, GPNum):
    (KT, _) = FormTotalKP(NodeNum, NodeID, FiberID, Nodey, Nodez, PointI, PointJ, PointK, GPNum)
    (PTy, PTz) = FormShearLoad(Iy, Iz, Iyz, NodeNum, NodeID, FiberID, Nodey, Nodez, PointI, PointJ, PointK, GPNum)
    CSRKT = csr_matrix(KT)
    Phi = np.squeeze(spsolve(CSRKT, PTy))
    Psi = np.squeeze(spsolve(CSRKT, PTz))

    #tKT = KT[1:, 1:]
    #tPTy = PTy[1:]
    #tPTz = PTz[1:]
    #CSRKT = csr_matrix(tKT)
    #tPhi = np.squeeze(spsolve(CSRKT, tPTy))
    #tPsi = np.squeeze(spsolve(CSRKT, tPTz))
    #Phi = np.hstack((np.zeros(1), tPhi))
    #Psi = np.hstack((np.zeros(1), tPsi))
    return Phi, Psi


def GetShearCoefficient(Nodey, Nodez, NodePhi, NodePsi, FiberID, PointI, PointJ, PointK, A, Iy, Iz, Iyz, GPNum):
    ky = 0
    kz = 0
    tky = 0
    tkz = 0
    (GPs, Wts) = GQ.GaussPointsTri(GPNum)
    for i in FiberID:
        mat_id = Model.Fiber.MaterialID[i]
        nu = Model.Material.nu[mat_id]
        (tKappay, tKappaz) = Tri3.GetKappa([Nodey[PointI[i]], Nodey[PointJ[i]], Nodey[PointK[i]]],
                                           [Nodez[PointI[i]], Nodez[PointJ[i]], Nodez[PointK[i]]],
                                           [NodePhi[PointI[i]], NodePhi[PointJ[i]], NodePhi[PointK[i]]],
                                           [NodePsi[PointI[i]], NodePsi[PointJ[i]], NodePsi[PointK[i]]],
                                           Iy, Iz, Iyz, nu, GPNum, GPs, Wts)
        tky += tKappay / (1 + nu) ** 2
        tkz += tKappaz / (1 + nu) ** 2
    Delta = 2 * (Iy * Iz - Iyz ** 2)
    ky += Delta ** 2 / (tky * A)
    kz += Delta ** 2 / (tkz * A)
    return ky, kz


def CalSectProps(RunAutoMesh, E_ref):
    pl.Print(pl.BPLog.CalSectProp(Fiber))
    SP.Perimeter = GetPerimeter(Model.Outline.ID, Model.Outline.Type, Model.Outline.Point1, Model.Outline.Point2,
                                Model.Point.Y, Model.Point.Z)
    if RunAutoMesh == 0:
        SP.Area = sum([Model.Material.E[Model.Fiber.MaterialID[i]] * Model.Fiber.Area[i] for i in Model.Fiber.ID]) / E_ref
        SP.Qy = sum([Model.Material.E[Model.Fiber.MaterialID[i]] * Model.Fiber.Qy[i] for i in Model.Fiber.ID]) / E_ref
        SP.Qz = sum([Model.Material.E[Model.Fiber.MaterialID[i]] * Model.Fiber.Qz[i] for i in Model.Fiber.ID]) / E_ref
        SP.cy = SP.Qz / SP.Area
        SP.cz = SP.Qy / SP.Area
        Model.Node.ReadLocal(SP.cy, SP.cz)
        (SP.Iyc, SP.Izc) = GetIyIz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iy, Model.Fiber.Iz,
                                   Model.Fiber.cy, Model.Fiber.cz, SP.cy, SP.cz, E_ref)
        SP.Iyzc = GetIyz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iyz,
                         Model.Fiber.cy, Model.Fiber.cz, SP.cy, SP.cz, E_ref)
        if SP.Iyc == SP.Izc:
            SP.Theta = 0
        elif SP.Iyc < SP.Izc:
            SP.Theta = np.arctan(2 * SP.Iyzc / (SP.Iyc - SP.Izc)) / 2
        else:
            SP.Theta = (np.arctan(2 * SP.Iyzc / (SP.Iyc - SP.Izc)) + np.pi) / 2
        SP.ExtY = max(Model.Point.Y.values()) - min(Model.Point.Y.values())
        SP.ExtZ = max(Model.Point.Z.values()) - min(Model.Point.Z.values())
    (SP.Iyg, SP.Izg) = GetIyIz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iy, Model.Fiber.Iz,
                               Model.Fiber.cy, Model.Fiber.cz, 0, 0, E_ref)
    SP.Iyzg = GetIyz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iyz, Model.Fiber.cy, Model.Fiber.cz, 0, 0, E_ref)
    SP.ry = np.sqrt(SP.Iyc / SP.Area)
    SP.rz = np.sqrt(SP.Izc / SP.Area)
    #SP.Sy = SP.Iyc / max(abs(min(Model.Node.Z.values()) - SP.cz), abs(max(Model.Node.Z.values()) - SP.cz))
    #SP.Sz = SP.Izc / max(abs(min(Model.Node.Y.values()) - SP.cy), abs(max(Model.Node.Y.values()) - SP.cy))
    SP.cyp = GetPNA(Model.Node.Y, Model.Node.Z, Model.Fiber.ID,
                    Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, Model.Fiber.Area, SP.Area, E_ref)
    SP.czp = GetPNA(Model.Node.Z, Model.Node.Y, Model.Fiber.ID,
                    Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, Model.Fiber.Area, SP.Area, E_ref)
    #(SP.Zy, SP.Zz) = GetZyZz(Model.Node.Y, Model.Node.Z, Model.Fiber.ID,
                             #Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                             #Model.Fiber.Area, Model.Fiber.cy, Model.Fiber.cz, SP.cyp, SP.czp, E_ref)
    if RunAutoMesh == 0:
        Model.Node.GetPrinciple(SP.Theta)
        Model.Fiber.GetPrinciple()
        (SP.Iv, SP.Iw) = GetIyIz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iv, Model.Fiber.Iw,
                                 Model.Fiber.cv, Model.Fiber.cw, 0, 0, E_ref)
    SP.rv = np.sqrt(SP.Iv / SP.Area)
    SP.rw = np.sqrt(SP.Iw / SP.Area)
    #SP.Sv = SP.Iv / max(abs(min(Model.Node.W.values())), abs(max(Model.Node.W.values())))
    #SP.Sw = SP.Iw / max(abs(min(Model.Node.V.values())), abs(max(Model.Node.V.values())))
    SP.cvp = GetPNA(Model.Node.V, Model.Node.W, Model.Fiber.ID,
                    Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, Model.Fiber.Area, SP.Area, E_ref)
    SP.cwp = GetPNA(Model.Node.W, Model.Node.V, Model.Fiber.ID,
                    Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, Model.Fiber.Area, SP.Area, E_ref)
    #(SP.Zv, SP.Zw) = GetZyZz(Model.Node.V, Model.Node.W, Model.Fiber.ID,
                             #Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                             #Model.Fiber.Area, Model.Fiber.cv, Model.Fiber.cw, SP.cvp, SP.cwp, E_ref)
    return


def CalTorsionalProps(RunAutoMesh, GPNum, E_ref, G_ref):
    pl.Print(pl.BPLog.CalTorsionProp(pl.BPLog))
    if RunAutoMesh == 0:
        pl.Print(pl.BPLog.SolWarpingFunc(Model.Node.Count))
        tOmega = GetOmegaWRTCentroid(Model.Node.Count, Model.Node.ID, Model.Node.y, Model.Node.z, Model.Fiber.ID,
                                     Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, GPNum)
        Model.Node.ReadOmega(tOmega)
        (SP.cvs, SP.cws) = GetPrincipleShearCentre(Model.Node.V, Model.Node.W, Model.Node.Omega, Model.Fiber.ID,
                                                   Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                                   SP.Iv, SP.Iw, GPNum, E_ref)
        SP.ysc = (SP.cvs * np.cos(-SP.Theta) - SP.cws * np.sin(-SP.Theta))
        SP.zsc = (SP.cvs * np.sin(-SP.Theta) + SP.cws * np.cos(-SP.Theta))
        SP.cys = SP.cy + SP.ysc
        SP.czs = SP.cz + SP.zsc
        tOmega = StandardizeOmega(Model.Node.V, Model.Node.W, Model.Node.Omega, Model.Fiber.ID,
                                  Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                  SP.cvs, SP.cws, SP.Area, GPNum, E_ref)
        Model.Node.ReadOmega(tOmega)
        SP.J = GetJ(Model.Node.Y, Model.Node.Z, Model.Node.Omega, Model.Fiber.ID,
                    Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, SP.cys, SP.czs, GPNum, G_ref)
    ptm = 0
    for i in Model.Fiber.ID:
        ptm += Model.Fiber.Area[i] * (Model.Fiber.cy[i] ** 2 + Model.Fiber.cz[i] ** 2) ** 0.5
    SP.Zt = ptm
    SP.Iomg = GetIomg(Model.Node.Y, Model.Node.Z, Model.Node.Omega, Model.Fiber.ID,
                      Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, GPNum, G_ref)
    (SP.Betay, SP.Betaz, SP.Betaomg) = GetWagnerCoef(Model.Node.y, Model.Node.z, Model.Node.Omega, Model.Fiber.ID,
                                                     Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                                     SP.ysc, SP.zsc, SP.Iyc, SP.Izc, SP.Iomg, GPNum, E_ref, G_ref)
    (SP.Betav, SP.Betaw, _) = GetWagnerCoef(Model.Node.V, Model.Node.W, Model.Node.Omega, Model.Fiber.ID,
                                                      Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                                      SP.cvs, SP.cws, SP.Iv, SP.Iw, SP.Iomg, GPNum, E_ref, G_ref)
    return


def CalShearProps(GPNum):
    pl.Print(pl.BPLog.CalShearProp(pl.BPLog))
    pl.Print(pl.BPLog.SolShearFunc(Model.Node.Count))
    (tPhi, tPsi) = GetShearFunction(Model.Node.Count, Model.Node.ID, Model.Node.y, Model.Node.z,
                                    Model.Fiber.ID, Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                    SP.Iyc, SP.Izc, SP.Iyzc, GPNum)
    Model.Node.ReadShearFunction(tPhi, tPsi)
    (SP.ky, SP.kz) = GetShearCoefficient(Model.Node.y, Model.Node.z, Model.Node.Phi, Model.Node.Psi,
                                         Model.Fiber.ID, Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                         SP.Area, SP.Iyc, SP.Izc, SP.Iyzc, GPNum)
    pl.Print(pl.BPLog.SolPrinShearFunc(Model.Node.Count))
    (tPhip, tPsip) = GetShearFunction(Model.Node.Count, Model.Node.ID, Model.Node.V, Model.Node.W,
                                      Model.Fiber.ID, Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                      SP.Iv, SP.Iw, 0, GPNum)
    Model.Node.ReadPrincipleShearFunction(tPhip, tPsip)
    (SP.kv, SP.kw) = GetShearCoefficient(Model.Node.V, Model.Node.W, Model.Node.Phip, Model.Node.Psip,
                                         Model.Fiber.ID, Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                         SP.Area, SP.Iv, SP.Iw, 0, GPNum)
    SP.Ayy = SP.Area * SP.ky
    SP.Azz = SP.Area * SP.kz
    SP.Avv = SP.Area * SP.kv
    SP.Aww = SP.Area * SP.kw


def GetAutoMeshJ(GPNum):
    mat_ref = next(iter(Model.Material.ID))
    E_ref = Model.Material.E[mat_ref]
    G_ref = Model.Material.G[mat_ref]
    SP.Area = sum([Model.Material.E[Model.Fiber.MaterialID[i]] * Model.Fiber.Area[i] for i in Model.Fiber.ID]) / E_ref
    SP.Qy = sum([Model.Material.E[Model.Fiber.MaterialID[i]] * Model.Fiber.Qy[i] for i in Model.Fiber.ID]) / E_ref
    SP.Qz = sum([Model.Material.E[Model.Fiber.MaterialID[i]] * Model.Fiber.Qz[i] for i in Model.Fiber.ID]) / E_ref
    SP.cy = SP.Qz / SP.Area
    SP.cz = SP.Qy / SP.Area
    Model.Node.ReadLocal(SP.cy, SP.cz)
    (SP.Iyc, SP.Izc) = GetIyIz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iy, Model.Fiber.Iz,
                               Model.Fiber.cy, Model.Fiber.cz, SP.cy, SP.cz, E_ref)
    SP.Iyzc = GetIyz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iyz,
                     Model.Fiber.cy, Model.Fiber.cz, SP.cy, SP.cz, E_ref)
    if SP.Iyc == SP.Izc:
        SP.Theta = 0
    elif SP.Iyc < SP.Izc:
        SP.Theta = np.arctan(2 * SP.Iyzc / (SP.Iyc - SP.Izc)) / 2
    else:
        SP.Theta = (np.arctan(2 * SP.Iyzc / (SP.Iyc - SP.Izc)) + np.pi) / 2
    Model.Node.GetPrinciple(SP.Theta)
    Model.Fiber.GetPrinciple()
    (SP.Iv, SP.Iw) = GetIyIz(Model.Fiber.ID, Model.Fiber.Area, Model.Fiber.Iv, Model.Fiber.Iw,
                             Model.Fiber.cv, Model.Fiber.cw, 0, 0, E_ref)
    tOmega = GetOmegaWRTCentroid(Model.Node.Count, Model.Node.ID, Model.Node.y, Model.Node.z, Model.Fiber.ID,
                                 Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, GPNum)
    Model.Node.ReadOmega(tOmega)
    (SP.cvs, SP.cws) = GetPrincipleShearCentre(Model.Node.V, Model.Node.W, Model.Node.Omega, Model.Fiber.ID,
                                               Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                                               SP.Iv, SP.Iw, GPNum, E_ref)
    SP.ysc = (SP.cvs * np.cos(-SP.Theta) - SP.cws * np.sin(-SP.Theta))
    SP.zsc = (SP.cvs * np.sin(-SP.Theta) + SP.cws * np.cos(-SP.Theta))
    SP.cys = SP.cy + SP.ysc
    SP.czs = SP.cz + SP.zsc
    tOmega = StandardizeOmega(Model.Node.V, Model.Node.W, Model.Node.Omega, Model.Fiber.ID,
                              Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK,
                              SP.cvs, SP.cws, SP.Area, GPNum, E_ref)
    Model.Node.ReadOmega(tOmega)
    SP.J = GetJ(Model.Node.Y, Model.Node.Z, Model.Node.Omega, Model.Fiber.ID,
                Model.Fiber.PointI, Model.Fiber.PointJ, Model.Fiber.PointK, SP.cys, SP.czs, GPNum, G_ref)
    return


def Run(progress_Signal, mat_ref):
    E_ref = 0
    G_ref = 0
    if mat_ref == "id":
        E_ref = Model.Material.E[Model.Analysis.mat_ref]
        G_ref = Model.Material.G[Model.Analysis.mat_ref]
    elif mat_ref == "value":
        E_ref = Model.Analysis.E_ref
        G_ref = Model.Analysis.G_ref
    if progress_Signal:
        progress_Signal.emit(20)
    CalSectProps(Model.Analysis.RunAutoMesh, E_ref)
    if progress_Signal:
        progress_Signal.emit(40)
    CalTorsionalProps(Model.Analysis.RunAutoMesh, 7, E_ref, G_ref)
    if progress_Signal:
        progress_Signal.emit(60)
    CalShearProps(7)
    if progress_Signal:
        progress_Signal.emit(80)
    pl.Print(pl.BPLog.OutRes(SP))
    BPRes.OutBPRes(Model.OutResult, SP)
    return
