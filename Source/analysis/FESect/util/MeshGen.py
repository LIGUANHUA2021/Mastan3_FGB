import numpy as np
from scipy.spatial import cKDTree
import gmsh
import analysis.FESect.variables.Model as FEModel
from analysis.FESect.solver.BasicProperties import GetAutoMeshJ
from analysis.FESect.variables.Result import SectionProperties as SP
from copy import copy


class FEMesh:
    def __init__(self, progress_Signal=None, finish_Signal=None, iter_Signal=None, text_Signal=None):
        self.progress_Signal = progress_Signal
        self.finish_Signal = finish_Signal
        self.iter_Signal = iter_Signal
        self.text_Signal = text_Signal

    def MeshGenFE(self, model, meshSize=0, temp=False):
        gmsh.initialize()
        if temp:
            meshSize = max(max(model.Point.Yo.values()) - min(model.Point.Yo.values()),
                           max(model.Point.Zo.values()) - min(model.Point.Zo.values()))
            (nodeCoords, eleNodes, eleGID) = self.GmshGen(model, meshSize / 10)
            self.readGmshRes(model, nodeCoords, eleNodes, eleGID, temp)
            gmsh.finalize()
        else:
            if meshSize:
                (nodeCoords, eleNodes, eleGID) = self.GmshGen(model, meshSize)
                self.readGmshRes(model, nodeCoords, eleNodes, eleGID, temp)
            else:
                if self.iter_Signal:
                    self.iter_Signal.emit(0)
                SP.ExtY = max(model.Point.Yo.values()) - min(model.Point.Yo.values())
                SP.ExtZ = max(model.Point.Zo.values()) - min(model.Point.Zo.values())
                meshSize = min(SP.ExtY, SP.ExtZ) / 10
                (nodeCoords, eleNodes, eleGID) = self.GmshGen(model, meshSize)
                self.readGmshRes(model, nodeCoords, eleNodes, eleGID, temp)
                if self.text_Signal:
                    self.text_Signal.emit("Perparing convergence criteria...")
                if self.progress_Signal:
                    self.progress_Signal.emit(90)
                GetAutoMeshJ(7)
                JIter = [SP.J * 2, SP.J]
                nodeNum = [FEModel.Node.Count]
                eleNum = [FEModel.Fiber.Count]
                if self.progress_Signal:
                    self.progress_Signal.emit(100)
                i = 1
                while abs(JIter[-2] - JIter[-1]) >= abs(JIter[-1]) / 100 and len(JIter) <= 100:
                    meshSize /= 1.25
                    if self.iter_Signal:
                        self.iter_Signal.emit(i)
                    (nodeCoords, eleNodes, eleGID) = self.GmshGen(model, meshSize)
                    self.readGmshRes(model, nodeCoords, eleNodes, eleGID, temp)
                    nodeNum.append(FEModel.Node.Count)
                    eleNum.append(FEModel.Fiber.Count)
                    if self.text_Signal:
                        self.text_Signal.emit("Checking error...")
                    if self.progress_Signal:
                        self.progress_Signal.emit(90)
                    while nodeNum[-1] < 1.2 * nodeNum[-2] or eleNum[-1] < 1.2 * eleNum[-2]:
                        nodeNum.pop()
                        eleNum.pop()
                        meshSize /= 1.25
                        (nodeCoords, eleNodes, eleGID) = self.GmshGen(model, meshSize)
                        self.readGmshRes(model, nodeCoords, eleNodes, eleGID, temp)
                        nodeNum.append(FEModel.Node.Count)
                        eleNum.append(FEModel.Fiber.Count)
                    GetAutoMeshJ(7)
                    JIter.append(SP.J)
                    if self.progress_Signal:
                        self.progress_Signal.emit(100)
                    i += 1
        if self.finish_Signal:
            self.finish_Signal.emit()
        if self.progress_Signal:
            self.progress_Signal.emit(100)

    def GmshGen(self, model, meshSize):
        Geo = gmsh.model.geo
        PBValue = 0
        if self.progress_Signal:
            self.progress_Signal.emit(PBValue)
        if meshSize:
            PBMultip = 2
        else:
            PBMultip = 1

        if self.text_Signal:
            self.text_Signal.emit("Importing point data...")
        for i in model.Point.ID:
            Geo.addPoint(model.Point.Zo[i], model.Point.Yo[i], 0, meshSize, int(i))
        if self.progress_Signal:
            PBValue += PBMultip * 5
            self.progress_Signal.emit(PBValue)

        if self.text_Signal:
            self.text_Signal.emit("Importing outline data...")
        for i in model.Outline.ID:
            Geo.addLine(int(model.Outline.PointI[i]), int(model.Outline.PointJ[i]), int(i))
        if self.progress_Signal:
            PBValue += PBMultip * 5
            self.progress_Signal.emit(PBValue)

        if self.text_Signal:
            self.text_Signal.emit("Importing loop data...")
        for i in model.Loop.ID:
            OID = copy(model.Loop.OutlineID[i])
            for j in range(len(OID)):
                if not j:
                    if model.Outline.PointI[OID[j]] == model.Outline.PointI[OID[j + 1]] \
                            or model.Outline.PointI[OID[j]] == model.Outline.PointJ[OID[j + 1]]:
                        OID[j] = -int(OID[j])
                    else:
                        OID[j] = int(OID[j])
                elif model.Outline.PointJ[abs(OID[j])] == model.Outline.PointI[abs(OID[j - 1])] \
                        or model.Outline.PointJ[abs(OID[j])] == model.Outline.PointJ[abs(OID[j - 1])]:
                    OID[j] = -int(OID[j])
                else:
                    OID[j] = int(OID[j])
            Geo.addCurveLoop(OID, int(i))
        if self.progress_Signal:
            PBValue += PBMultip * 5
            self.progress_Signal.emit(PBValue)

        if self.text_Signal:
            self.text_Signal.emit("Importing group data...")
        for i in model.Group.ID:
            Geo.addPlaneSurface(model.Group.LoopID[i], int(i))
        Geo.synchronize()
        if self.progress_Signal:
            PBValue += PBMultip * 5
            self.progress_Signal.emit(PBValue)

        if self.text_Signal:
            self.text_Signal.emit("Generating mesh...")
        gmsh.model.mesh.generate(2)
        eleGID = {}
        nodeCoords = gmsh.model.mesh.getNodes(-1, -1)[1].reshape((-1, 3))[:, :2].astype(float)
        eleNodes = gmsh.model.mesh.getElements(2, -1)[2][0].reshape((-1, 3)).astype(int) - 1
        IDDiv = int(gmsh.model.mesh.getElements(1, -1)[1][0][-1] + 1)
        for i in model.Group.ID:
            FID = gmsh.model.mesh.getElements(2, i)[1][0].astype(int) - IDDiv
            for j in FID:
                eleGID[j] = i
        gmsh.model.remove()
        if self.progress_Signal:
            PBValue += PBMultip * 10
            self.progress_Signal.emit(PBValue)
        return nodeCoords, eleNodes, eleGID

    def get_rept_rows(self, node_array):
        rept_nodes = cKDTree(node_array)
        rept_rows = dict(rept_nodes.query_pairs(r=0.00001))
        return rept_rows

    def merge_rept_nodes(self, node_coords, ele_node_ID):
        rept_nodes = self.get_rept_rows(node_coords)
        if rept_nodes:
            node_coords = np.delete(node_coords, np.asarray([i for i in rept_nodes]), axis=0)
            for i in range(len(ele_node_ID)):
                for j in range(3):
                    node_ID = ele_node_ID[i, j]
                    if node_ID in rept_nodes:
                        ele_node_ID[i, j] = rept_nodes[node_ID]
            for i in range(len(ele_node_ID)):
                for j in range(3):
                    ele_node_ID[i, j] -= sum(ele_node_ID[i, j] > ID for ID in rept_nodes)
        return node_coords

    def readGmshRes(self, model, nodeCoords, eleNodes, eleGID, temp):
        if self.text_Signal:
            self.text_Signal.emit("Merging nodes...")
        if self.progress_Signal:
            self.progress_Signal.emit(75)
        nodeCoords = self.merge_rept_nodes(nodeCoords, eleNodes)
        if temp:
            FEModel.Group.readGroup(model.Group)
            FEModel.TempNode.readTempNode(nodeCoords)
            FEModel.TempFiber.readTempFiber(eleNodes, eleGID)
        else:
            FEModel.Material.readMat(model.Mat)
            FEModel.Point.readPoint(model.Point)
            FEModel.Outline.readOl(model.Outline)
            FEModel.Group.readGroup(model.Group)
            FEModel.Node.readNode(nodeCoords)
            FEModel.Segment.readSeg(eleNodes)
            FEModel.Fiber.readFiber(eleNodes, eleGID)
