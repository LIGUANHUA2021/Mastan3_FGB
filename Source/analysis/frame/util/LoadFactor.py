import numpy as np

#Get current load factor
def GetLF(tFg,tRg):
    Index=np.nonzero(tFg)
    return np.mean([tRg[Index[i]]/tFg[Index[i]] for i in range(len(Index))])