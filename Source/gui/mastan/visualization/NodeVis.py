# External library
import numpy as np
# Internal library
from gui.mastan.base.model import msaModel

def visualizenode(mw, WhetherShow):
    nsize = 5
    ncolor = (1, 1, 1, 1)
    nid = msaModel.Node.ID
    ncoordinate = {}
    pos = []
    for ii in nid:
        ncoordinate[ii] = np.array([msaModel.Node.x[ii], msaModel.Node.y[ii], msaModel.Node.z[ii]])
        pos.append(ncoordinate[ii])
    if ((not WhetherShow) or len(pos) == 0):
        pos = np.array([[0, 0, 0]])
        mw.Node.set_data(pos=pos, face_color=ncolor, size=0.001)
        return
    pos = np.array(pos)
    mw.Node.set_data(pos=pos, face_color=ncolor, size=nsize)

