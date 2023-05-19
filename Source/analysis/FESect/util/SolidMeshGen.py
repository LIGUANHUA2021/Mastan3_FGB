import numpy as np
from scipy.spatial import cKDTree
import gmsh
import analysis.FESect.variables.Model as FEModel
from analysis.FESect.solver.BasicProperties import GetAutoMeshJ
from analysis.FESect.variables.Result import SectionProperties as SP
from copy import copy


class FEMesh:
    def __init__(self, finish_Signal=None):
        self.finish_Signal = finish_Signal

    def MeshGenFE(self, model, length, mesh_size):
        gmsh.initialize()
        (nodeCoords, eleNodes, eleGID) = self.GmshGen(model, length, mesh_size)
        gmsh.finalize()
        self.readGmshRes(model, nodeCoords, eleNodes, eleGID)

    def GmshGen(self, model, length, mesh_size):
        vol = {}
        Geo = gmsh.model.geo
        for i in model.Point.ID:
            Geo.addPoint(0, model.Point.Yo[i], model.Point.Zo[i], mesh_size, int(i))
        for i in model.Outline.ID:
            Geo.addLine(int(model.Outline.PointI[i]), int(model.Outline.PointJ[i]), int(i))
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
        for i in model.Group.ID:
            Geo.addPlaneSurface(model.Group.LoopID[i], int(i))
            vol[int(i)] = Geo.extrude([(2, int(i))], length, 0, 0, [length // mesh_size])
        Geo.synchronize()

        gmsh.model.mesh.generate(3)
        eleGID = {}
        nodeCoords = gmsh.model.mesh.getNodes()[1].reshape((-1, 3)).astype(float)
        eleNodes = gmsh.model.mesh.getElements(3)[2][0].reshape((-1, 4)).astype(int) - 1
        IDDiv = int(max((max(i[0]) for i in gmsh.model.mesh.getElements(2) if type(i) == list)) + 1)
        for i in model.Group.ID:
            FID = gmsh.model.mesh.getElements(3, vol[i][1][1])[1][0].astype(int) - IDDiv
            eleGID.update({j: i for j in FID})
        gmsh.model.remove()
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
                for j in range(4):
                    node_ID = ele_node_ID[i, j]
                    if node_ID in rept_nodes:
                        ele_node_ID[i, j] = rept_nodes[node_ID]
            for i in range(len(ele_node_ID)):
                for j in range(4):
                    ele_node_ID[i, j] -= sum(ele_node_ID[i, j] > ID for ID in rept_nodes)
        return node_coords

    def readGmshRes(self, model, nodeCoords, eleNodes, eleGID):
        nodeCoords = self.merge_rept_nodes(nodeCoords, eleNodes)
        FEModel.Material.readMat(model.Mat)
        FEModel.Point.readPoint(model.Point)
        FEModel.Outline.readOl(model.Outline)
        FEModel.Group.readGroup(model.Group)
        FEModel.Node3D.readNode(nodeCoords)
        FEModel.Segment3D.readSeg(eleNodes)
        FEModel.Fiber3D.readFiber(eleNodes, eleGID)
