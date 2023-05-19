# External library
import numpy as np
# Internal library
from gui.mastan.base.model import msaModel

def visualizemember(mw, WhetherShow):
    pos = []
    Member = msaModel.Member
    Node = msaModel.Node
    for ii in Member.ID:
        tNI = Member.NodeI[ii]; tNJ = Member.NodeJ[ii]
        tNI_pos = [Node.x[tNI], Node.y[tNI], Node.z[tNI]]
        tNJ_pos = [Node.x[tNJ], Node.y[tNJ], Node.z[tNJ]]
        tline_pos = [tNI_pos,tNJ_pos]
        pos.append(tline_pos)
    pos = np.array(pos)
    if ((not WhetherShow) or len(pos) == 0):
        mw.Mem.set_data(pos=np.array([[[0,0,0],[0.001,0,0]]]))
        return
    mw.Mem.set_data(pos=pos)