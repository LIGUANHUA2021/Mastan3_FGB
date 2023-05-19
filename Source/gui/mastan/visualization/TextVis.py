# External library
import numpy as np

# Internal library
from gui.mastan.base.model import msaModel

def visualizenodetext(mw, WhetherShow):
    text = []
    pos = []
    if not WhetherShow:
        mw.NodeText.text = [" "]
        mw.NodeText.pos = np.array([[0,0,0]])
        return
    l = 0
    for ii in msaModel.Node.ID:
        text.append(str(int(ii)))
        tNpos = [msaModel.Node.x[ii] + l, msaModel.Node.y[ii] + l, msaModel.Node.z[ii] + l]
        pos.append(tNpos)
    pos = np.array(pos)
    mw.NodeText.text = text
    mw.NodeText.pos = pos

def visualizememtext(mw, WhetherShow):
    text = []
    pos = []
    if not WhetherShow:
        mw.MemText.text = [" "]
        mw.MemText.pos = np.array([[0,0,0]])
        return
    for ii in msaModel.Member.ID:
        text.append(str(int(ii)))
        tNI = msaModel.Member.NodeI[ii]; tNJ = msaModel.Member.NodeJ[ii]
        tNI_pos = np.array([msaModel.Node.x[tNI], msaModel.Node.y[tNI], msaModel.Node.z[tNI]])
        tNJ_pos = np.array([msaModel.Node.x[tNJ], msaModel.Node.y[tNJ], msaModel.Node.z[tNJ]])
        tpos = 0.5 * tNI_pos + 0.5 * tNJ_pos
        pos.append(tpos)
    pos = np.array(pos)
    mw.MemText.text = text
    mw.MemText.pos = pos
