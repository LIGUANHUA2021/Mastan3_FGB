# External library
import numpy as np
import math
# Internal library
from gui.mastan.base.model import msaModel
def VisualizeJointLoad(mw, WhetherShow):
    VisualizeJointLoadF(mw, WhetherShow)
    VisualizeJointLoadM(mw, WhetherShow)

# Visualize the force in the joinload
def VisualizeJointLoadF(mw, WhetherShow):
    ratio = 0.2
    nodesize = 0.1
    arrowsize = 0.2 * ratio
    pos = []
    if not WhetherShow:
        mw.JointLoadF.set_data(pos=np.array([[[0,0,0],[0.00001,0,0]]]))
        return
    for ii in msaModel.Load.NodeID:
        tNx, tNy, tNz = msaModel.Node.x[ii], msaModel.Node.y[ii], msaModel.Node.z[ii]
        if msaModel.Load.LoadVector[ii][0] != 0:
            tFX = msaModel.Load.LoadVector[ii][0]
            deflection = nodesize * np.sign(tFX) * ratio
            tpos_line = [[tNx - deflection, tNy, tNz], [tNx - tFX * ratio - deflection, tNy, tNz]]
            pos.append(tpos_line)
            tpos_arrow1 = [[tNx - deflection, tNy, tNz], [tNx - deflection - arrowsize * np.sign(tFX), tNy - arrowsize, tNz]]
            tpos_arrow2 = [[tNx - deflection, tNy, tNz], [tNx - deflection - arrowsize * np.sign(tFX), tNy + arrowsize, tNz]]
            pos.append(tpos_arrow1)
            pos.append(tpos_arrow2)
        if msaModel.Load.LoadVector[ii][1] != 0:
            tFY = msaModel.Load.LoadVector[ii][1]
            deflection = nodesize * np.sign(tFY) * ratio
            tpos_line = [[tNx, tNy - deflection, tNz], [tNx, tNy - tFY * ratio - deflection, tNz]]
            pos.append(tpos_line)
            tpos_arrow1 = [[tNx, tNy - deflection, tNz],
                           [tNx, tNy - deflection - arrowsize * np.sign(tFY), tNz - arrowsize]]
            tpos_arrow2 = [[tNx, tNy - deflection, tNz],
                           [tNx, tNy - deflection - arrowsize * np.sign(tFY), tNz + arrowsize]]
            pos.append(tpos_arrow1)
            pos.append(tpos_arrow2)
        if msaModel.Load.LoadVector[ii][2] != 0:
            tFZ = msaModel.Load.LoadVector[ii][2]
            deflection = nodesize * np.sign(tFZ) * ratio
            tpos_line = [[tNx, tNy, tNz - deflection], [tNx, tNy, tNz - tFZ * ratio - deflection]]
            pos.append(tpos_line)
            tpos_arrow1 = [[tNx, tNy, tNz - deflection],
                           [tNx - arrowsize, tNy, tNz - deflection - arrowsize * np.sign(tFZ)]]
            tpos_arrow2 = [[tNx, tNy, tNz - deflection],
                           [tNx + arrowsize, tNy, tNz - deflection - arrowsize * np.sign(tFZ)]]
            pos.append(tpos_arrow1)
            pos.append(tpos_arrow2)
    if len(pos) == 0:
        pos = [[0,0,0],[0.000001,0,0]] # Entities.pos in VISPY cannot be empty.
    pos = np.array(pos)
    mw.JointLoadF.set_data(pos=pos)

def VisualizeJointLoadM(mw, WhetherShow):
    archsize = 0.5
    arrowsize = 0.1
    pos = []
    if not WhetherShow:
        mw.JointLoadM.set_data(pos=np.array([[[0,0,0],[0.00001,0,0]]]))
        return
    for ii in msaModel.Load.NodeID:
        tNx, tNy, tNz = msaModel.Node.x[ii], msaModel.Node.y[ii], msaModel.Node.z[ii]
        if msaModel.Load.LoadVector[ii][3] != 0:
            tMX = msaModel.Load.LoadVector[ii][3]
            tpos = generateMXLine(tMX, tNx, tNy, tNz, archsize, arrowsize)
            for jj in tpos:
                pos.append(jj)
        if msaModel.Load.LoadVector[ii][4] != 0:
            tMY = msaModel.Load.LoadVector[ii][4]
            tpos = generateMYLine(tMY, tNx, tNy, tNz, archsize, arrowsize)
            for jj in tpos:
                pos.append(jj)
        if msaModel.Load.LoadVector[ii][5] != 0:
            tMZ = msaModel.Load.LoadVector[ii][5]
            tpos = generateMZLine(tMZ, tNx, tNy, tNz, archsize, arrowsize)
            for jj in tpos:
                pos.append(jj)
    if len(pos) == 0:
        pos = [[0, 0, 0], [0.000001, 0, 0]] # Entities.pos in VISPY cannot be empty.
    pos = np.array(pos)
    mw.JointLoadM.set_data(pos=pos)


# Generate the arch line used in the moment visualization
# MX
def generateMXLine(M, x, y, z, R, arrowsize):
    angle = [-60, -30, 30, 90, 150, 210, 240]
    pos = []
    pos_y, pos_z = [], []
    pi = math.pi
    # the position of the arch
    for ii in range(len(angle)):
        angle[ii] = angle[ii] * pi / 180
    for ii in range(len(angle)):
        tpos_y = y + math.cos(angle[ii]) * R
        tpos_z = z + math.sin(angle[ii]) * R
        pos_y.append(tpos_y)
        pos_z.append(tpos_z)
    for ii in range(len(pos_y) - 1):
        tpos = [[x, pos_y[ii], pos_z[ii]], [x, pos_y[ii + 1], pos_z[ii + 1]]]
        pos.append(tpos)
    # the position of the arrow
    if M >= 0:
        end_pos = pos[len(pos) - 1][1]
        tpos1 = [end_pos, [end_pos[0], end_pos[1], end_pos[2] + arrowsize]]
        tpos2 = [end_pos, [end_pos[0], end_pos[1] - arrowsize * math.cos(30 / 180 * pi),
                           end_pos[2] + arrowsize * math.sin(30 / 180 * pi)]]
    else:
        end_pos = pos[0][0]
        tpos1 = [end_pos, [end_pos[0], end_pos[1], end_pos[2] + arrowsize]]
        tpos2 = [end_pos, [end_pos[0], end_pos[1] + arrowsize * math.cos(30 / 180 * pi),
                           end_pos[2] + arrowsize * math.sin(30 / 180 * pi)]]
    pos.append(tpos1)
    pos.append(tpos2)
    return pos


# MY
def generateMYLine(M, x, y, z, R, arrowsize):
    angle = [-60, -30, 30, 90, 150, 210, 240]
    pos = []
    pos_x, pos_z = [], []
    # the position of line
    pi = math.pi
    for ii in range(len(angle)):
        angle[ii] = angle[ii] * pi / 180
    for ii in range(len(angle)):
        tpos_x = x + math.cos(angle[ii]) * R
        tpos_z = z + math.sin(angle[ii]) * R
        pos_x.append(tpos_x)
        pos_z.append(tpos_z)
    for ii in range(len(pos_x) - 1):
        tpos = [[pos_x[ii], y, pos_z[ii]], [pos_x[ii + 1], y, pos_z[ii + 1]]]
        pos.append(tpos)
    # the position of the arrow
    if M >= 0:
        end_pos = pos[0][0]
        tpos1 = [end_pos, [end_pos[0], end_pos[1], end_pos[2] + arrowsize]]
        tpos2 = [end_pos, [end_pos[0] + arrowsize * math.cos(30 / 180 * pi), end_pos[1],
                           end_pos[2] + arrowsize * math.sin(30 / 180 * pi)]]
    else:
        end_pos = pos[len(pos)][1]
        tpos1 = [end_pos, [end_pos[0], end_pos[1], end_pos[2] + arrowsize]]
        tpos2 = [end_pos, [end_pos[0] - arrowsize * math.cos(30 / 180 * pi), end_pos[1],
                           end_pos[2] + arrowsize * math.sin(30 / 180 * pi)]]
    pos.append(tpos1)
    pos.append(tpos2)
    return pos

# MZ
def generateMZLine(M, x, y, z, R, arrowsize):
    angle = [-60, -30, 30, 90, 150, 210, 240]
    pos = []
    pos_x, pos_y = [], []
    pi = math.pi
    for ii in range(len(angle)):
        angle[ii] = angle[ii] * pi / 180
    for ii in range(len(angle)):
        tpos_x = x + math.cos(angle[ii]) * R
        tpos_y = y + math.sin(angle[ii]) * R
        pos_x.append(tpos_x)
        pos_y.append(tpos_y)
    for ii in range(len(pos_y) - 1):
        tpos = [[pos_x[ii], pos_y[ii], z], [pos_x[ii + 1], pos_y[ii + 1], z]]
        pos.append(tpos)
    # the position of the arrow
    if M >= 0:
        end_pos = pos[len(pos) - 1][1]
        tpos1 = [end_pos, [end_pos[0], end_pos[1] + arrowsize, end_pos[2]]]
        tpos2 = [end_pos, [end_pos[0] - arrowsize * math.cos(30 / 180 * pi),
                           end_pos[1] + arrowsize * math.sin(30 / 180 * pi), end_pos[2]]]
    else:
        end_pos = pos[0][0]
        tpos1 = [end_pos, [end_pos[0], end_pos[1] + arrowsize, end_pos[2]]]
        tpos2 = [end_pos, [end_pos[0] + arrowsize * math.cos(30 / 180 * pi),
                           end_pos[1] + arrowsize * math.sin(30 / 180 * pi), end_pos[2]]]
    pos.append(tpos1)
    pos.append(tpos2)
    return pos
