import numpy as np
from gui.msasect.base.Model import msaModel


def GetNode():
    msaModel.Node.Reset()
    for i in msaModel.Segment.ID:
        t = msaModel.Segment.SegThick[i]
        tMax = max(msaModel.Segment.SegThick.values())
        if t > tMax / 1000:
            Zo1 = msaModel.Point.Zo[msaModel.Segment.PointI[i]]
            Yo1 = msaModel.Point.Yo[msaModel.Segment.PointI[i]]
            Zo2 = msaModel.Point.Zo[msaModel.Segment.PointJ[i]]
            Yo2 = msaModel.Point.Yo[msaModel.Segment.PointJ[i]]
            L = np.sqrt((Zo2 - Zo1) ** 2 + (Yo2 - Yo1) ** 2)
            if t < tMax:
                FiberNumT = 4
            else:
                FiberNumT = 5
            FiberNumL = max(int(L / (t / FiberNumT)), 1)
            for j in range(FiberNumL + 1):
                tZ = Zo1 + (Zo2 - Zo1) * j / FiberNumL
                tY = Yo1 + (Yo2 - Yo1) * j / FiberNumL
                for k in range(FiberNumT + 1):
                    msaModel.Node.Add(msaModel.Node.Count + 1, tY - (t / 2 - t / FiberNumT * k) / L * (Zo2 - Zo1),
                                                               tZ + (t / 2 - t / FiberNumT * k) / L * (Yo2 - Yo1))
            msaModel.Segment.FiberNumT[i] = FiberNumT
            msaModel.Segment.FiberNumL[i] = FiberNumL
            msaModel.Segment.NodeNum[i] = (FiberNumT + 1) * (FiberNumL + 1)
        else:
            msaModel.Segment.FiberNumT[i] = 0
            msaModel.Segment.FiberNumL[i] = 0
            msaModel.Segment.NodeNum[i] = 0


def GetFiber():
    msaModel.Fiber.Reset()
    NodeStart = 1
    for i in msaModel.Segment.ID:
        for j in range(msaModel.Segment.FiberNumL[i]):
            for k in range(msaModel.Segment.FiberNumT[i]):
                msaModel.Fiber.Add(msaModel.Fiber.Count + 1,
                                   NodeStart + j * (msaModel.Segment.FiberNumT[i] + 1) + k,
                                   NodeStart + j * (msaModel.Segment.FiberNumT[i] + 1) + k + 1,
                                   NodeStart + (j + 1) * (msaModel.Segment.FiberNumT[i] + 1) + k + 1,
                                   NodeStart + (j + 1) * (msaModel.Segment.FiberNumT[i] + 1) + k,
                                   msaModel.Segment.MatID[i])
        # print(msaModel.Segment.FiberNumT[i])
        NodeStart += msaModel.Segment.NodeNum[i]
    for i in msaModel.Fiber.ID:
        msaModel.Fiber.Yc[i] = (msaModel.Node.Yo[msaModel.Fiber.NodeI[i]] + msaModel.Node.Yo[msaModel.Fiber.NodeK[i]]) / 2
        msaModel.Fiber.Zc[i] = (msaModel.Node.Zo[msaModel.Fiber.NodeI[i]] + msaModel.Node.Zo[msaModel.Fiber.NodeK[i]]) / 2
        Y = [msaModel.Node.Yo[msaModel.Fiber.NodeI[i]], msaModel.Node.Yo[msaModel.Fiber.NodeJ[i]],
             msaModel.Node.Yo[msaModel.Fiber.NodeK[i]], msaModel.Node.Yo[msaModel.Fiber.NodeL[i]],
             msaModel.Node.Yo[msaModel.Fiber.NodeI[i]]]
        Z = [msaModel.Node.Zo[msaModel.Fiber.NodeI[i]], msaModel.Node.Zo[msaModel.Fiber.NodeJ[i]],
             msaModel.Node.Zo[msaModel.Fiber.NodeK[i]], msaModel.Node.Zo[msaModel.Fiber.NodeL[i]],
             msaModel.Node.Zo[msaModel.Fiber.NodeI[i]]]
        for j in range(4):
            msaModel.Fiber.FArea[i] += (Y[j + 1] * Z[j] - Y[j] * Z[j + 1]) / 2
        msaModel.Fiber.FArea[i] = abs(msaModel.Fiber.FArea[i])

def GetNodeFSM():
    msaModel.Node3D.Reset()
    L_min = min(np.sqrt(
        (msaModel.Point.Zo[msaModel.Segment.PointJ[i]] - msaModel.Point.Zo[msaModel.Segment.PointI[i]]) ** 2 + (
                    msaModel.Point.Yo[msaModel.Segment.PointJ[i]] - msaModel.Point.Yo[msaModel.Segment.PointI[i]]) ** 2)
                for i in msaModel.Segment.ID)
    for i in msaModel.Segment.ID:
        t = msaModel.Segment.SegThick[i]
        tMax = max(msaModel.Segment.SegThick.values())
        if t <= tMax / 1000:
            t *= 1000
        Zo1 = msaModel.Point.Zo[msaModel.Segment.PointI[i]]
        Yo1 = msaModel.Point.Yo[msaModel.Segment.PointI[i]]
        Zo2 = msaModel.Point.Zo[msaModel.Segment.PointJ[i]]
        Yo2 = msaModel.Point.Yo[msaModel.Segment.PointJ[i]]
        L = np.sqrt((Zo2 - Zo1) ** 2 + (Yo2 - Yo1) ** 2)
        FiberNumL3D = int(L // L_min)
        for j in range(FiberNumL3D + 1):
            tZ = Zo1 + (Zo2 - Zo1) * j / FiberNumL3D
            tY = Yo1 + (Yo2 - Yo1) * j / FiberNumL3D
            for k in range(2):
                msaModel.Node3D.Add(msaModel.Node3D.Count + 1, tY - (t / 2 - t * k) / L * (Zo2 - Zo1),
                                                           tZ + (t / 2 - t * k) / L * (Yo2 - Yo1))
        msaModel.Segment.FiberNumL3D[i] = FiberNumL3D
        msaModel.Segment.NodeNum3D[i] = 2 * (FiberNumL3D + 1)


def GetFiberFSM():
    msaModel.Fiber3D.Reset()
    NodeStart = 1
    for i in msaModel.Segment.ID:
        for j in range(msaModel.Segment.FiberNumL3D[i]):
            msaModel.Fiber3D.Add(msaModel.Fiber3D.Count + 1,
                               NodeStart + j * 2,
                               NodeStart + j * 2 + 1,
                               NodeStart + (j + 1) * 2 + 1,
                               NodeStart + (j + 1) * 2,
                               msaModel.Segment.MatID[i])
        NodeStart += msaModel.Segment.NodeNum3D[i]
    for i in msaModel.Fiber3D.ID:
        msaModel.Fiber3D.Yc[i] = (msaModel.Node3D.Yo[msaModel.Fiber3D.NodeI[i]] + msaModel.Node3D.Yo[msaModel.Fiber3D.NodeK[i]]) / 2
        msaModel.Fiber3D.Zc[i] = (msaModel.Node3D.Zo[msaModel.Fiber3D.NodeI[i]] + msaModel.Node3D.Zo[msaModel.Fiber3D.NodeK[i]]) / 2
        Y = [msaModel.Node3D.Yo[msaModel.Fiber3D.NodeI[i]], msaModel.Node3D.Yo[msaModel.Fiber3D.NodeJ[i]],
             msaModel.Node3D.Yo[msaModel.Fiber3D.NodeK[i]], msaModel.Node3D.Yo[msaModel.Fiber3D.NodeL[i]],
             msaModel.Node3D.Yo[msaModel.Fiber3D.NodeI[i]]]
        Z = [msaModel.Node3D.Zo[msaModel.Fiber3D.NodeI[i]], msaModel.Node3D.Zo[msaModel.Fiber3D.NodeJ[i]],
             msaModel.Node3D.Zo[msaModel.Fiber3D.NodeK[i]], msaModel.Node3D.Zo[msaModel.Fiber3D.NodeL[i]],
             msaModel.Node3D.Zo[msaModel.Fiber3D.NodeI[i]]]
        for j in range(4):
            msaModel.Fiber3D.FArea[i] += (Y[j + 1] * Z[j] - Y[j] * Z[j + 1]) / 2
        msaModel.Fiber3D.FArea[i] = abs(msaModel.Fiber3D.FArea[i])


def MeshGenCM():
    GetNode()
    GetFiber()
    return


def MeshGenCM_FSM():
    GetNodeFSM()
    GetFiberFSM()
    return