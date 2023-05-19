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

# Import internal functions
from analysis.frame.util import Assembly,Transformation

def FormKg(Material,Section,Node,Member,EleMtxL,EleMtxK,teleType,tKg,AnalysisType):
    for ii in Member.ID:
        tMID = Member.ID[ii]
        mL = Member.L[tMID]
        mFx1 = Member.Fx1[tMID]
        mFx2 = Member.Fx2[tMID]
        mFy1 = Member.Fy1[tMID]
        mFy2 = Member.Fy2[tMID]
        mFz1 = Member.Fz1[tMID]
        mFz2 = Member.Fz2[tMID]
        mMx1 = Member.Mx1[tMID]
        mMx2 = Member.Mx2[tMID]
        mMy1 = Member.My1[tMID]
        mMy2 = Member.My2[tMID]
        mMz1 = Member.Mz1[tMID]
        mMz2 = Member.Mz2[tMID]
        mMb1 = Member.Mb1[tMID]
        mMb2 = Member.Mb2[tMID]
        mP = (mFx2 - mFx1) / 2.0
        mMb = (mMb1 + mMb2) / 2.0
        # --------------------------------------------------------------------------
        # Recall section properties
        tSectID = Member.SectID[ii]
        mA = Section.A[tSectID]
        mJ = Section.J[tSectID]
        # --------------------------------------------------------------------------
        # Recall material properties
        tMatID = Section.MatID[tSectID]
        mE = Material.E[tMatID]
        mG = Material.G[tMatID]
        # --------------------------------------------------------------------------
        # Recall the Transformation Matrix
        eleMtxL = EleMtxL[tMID * 3:tMID * 3 + 3, 0:3]
        # --------------------------------------------------------------------------
        # Form Element Stiffness Matrix
        EleKL = teleType.NonsymWarpingBeam.GetEleKL(mL, mE, mG, Section, tSectID)  # 14x14
        EleKI = teleType.NonsymWarpingBeam.GetEleKI(mL, mP, mMy1, mMy2, mMz1, mMz2, mMx2, mMb, Section, tSectID)
        EleKG = teleType.NonsymWarpingBeam.GetEleKG(mL, mP, mMy1, mMy2, mMz1, mMz2, mMx2, mMb, Section, tSectID)  # 14x14
        # --------------------------------------------------------------------------
        if (AnalysisType == "staticLinear" or AnalysisType == "modalAnalysis"):
            EleK = EleKL  # +EleKI #14x14 for static linear analysis
        elif AnalysisType == "staticNonlinear":
            EleK = EleKL + EleKG  # +EleKI #14x14 for static linear analysis
        elif AnalysisType == "eigenBuckling":
            EleK = EleKL + EleKG  # first: Only K_Linear; second: K_Linear + K_Geo
        elif AnalysisType == "dynamicNonlinear":
            EleK = EleKL + EleKG
        #   ......
        # --------------------------------------------------------------------------
        # Relations defined at the geometric centroid
        if AnalysisType == "eigenBuckling":
            pass
        else:
            MtxTf = Transformation.GetMtxTf(Section.yc[tSectID], Section.zc[tSectID])
            EleK = np.dot(MtxTf, EleK)
            EleK = np.dot(EleK, MtxTf.transpose())

        EleMtxK[tMID * 14:tMID * 14 + 14, 0:14] = EleK  # Save Element Stiffness Matrix - Local
        # --------------------------------------------------------------------------
        # Transform the Element Matrix from local to global systems
        EleK = Assembly.MemEleMtxToGlo(eleMtxL, EleK)
        # Assmble element stiffness matrix to global stiffness matrix
        tI=Node.ID[Member.I[ii]]
        tJ=Node.ID[Member.J[ii]]
        Kg = Assembly.AssmbelEleMtxToGlo(tI, tJ, EleK, tKg)

    return Kg, EleMtxK

def FormKgs(Material, Section, Node, Member, teleType,SoilParameter,Buried,EleMtxL0,tKgs):
    for ii in Member.ID:
        tMID = Member.ID[ii]
        if ii in Buried.MemID:
            tEleks = teleType.SoilBoundaryElement.GetEleK(ii, Material, Section, Node, Member, SoilParameter, Buried)
        else:
            tEleks = np.zeros([14, 14])
        # Transform the Element Matrix from local to global systems
        eleMtxL0 = EleMtxL0[tMID * 3:tMID * 3 + 3, 0:3]
        EleKs = Assembly.MemEleMtxToGlo(eleMtxL0, tEleks)
        # Assmble element stiffness matrix to global stiffness matrix
        tI=Node.ID[Member.I[ii]]
        tJ=Node.ID[Member.J[ii]]
        Kgs = Assembly.AssmbelEleMtxToGlo(tI, tJ, EleKs, tKgs)
    return Kgs

def FormMg(Material,Section,Node,Member,EleMtxL,tmassType,teleType,tMg):
    for ii in Member.ID:
        tMID = Member.ID[ii]
        mL = Member.L[tMID]
        tSectID = Member.SectID[ii]
        eleMtxL = EleMtxL[tMID * 3:tMID * 3 + 3, 0:3]
        EleMtxMM = teleType.NonsymWarpingBeam.GetEleMM(Material,Section,Member,tmassType,ii)
        # --------------------------------------------------------------------------
        # Relations defined at the geometric centroid
        MtxTf = Transformation.GetMtxTf(Section.yc[tSectID], Section.zc[tSectID])
        EleMtxMM = np.dot(MtxTf, EleMtxMM)
        EleMtxMM = np.dot(EleMtxMM, MtxTf.transpose())
        #eleMtxMM[tMID * 14:tMID * 14 + 14, 0:14] = EleMtxMM  # Save Element Mass Matrix - Local
        # --------------------------------------------------------------------------
        # Transform the Element Matrix from local to global systems
        eELEMtxMM = Assembly.MemEleMtxToGlo(eleMtxL, EleMtxMM)
        # Assmble element stiffness matrix to global stiffness matrix
        # for testing
        tI=Node.ID[Member.I[ii]]
        tJ=Node.ID[Member.J[ii]]
        Mg = Assembly.AssmbelEleMtxToGlo(tI, tJ, eELEMtxMM, tMg)

    return Mg

def FormAddMg(addMDir,GrAcc,Node,JointLoad,tAddMg):
    for ii in JointLoad.NodeID:
        if addMDir == 'none':
            tAddMg = tAddMg
        elif addMDir =='X-':
            dof_x = 0 + 7 * (Node.ID[ii])
            massval = JointLoad.FX[ii]/GrAcc
            if massval < 0:
                tAddMg[dof_x-1:dof_x+1+1,dof_x-1:dof_x+1+1]=-1*massval*np.eye(3)
        elif addMDir == 'Y-':
            dof_y = 1 + 7 * (Node.ID[ii])
            massval = JointLoad.FY[ii] / GrAcc
            if massval < 0:
                tAddMg[dof_y-1:dof_y+1+1,dof_y-1:dof_y+1+1]=-1*massval*np.eye(3)
                tttAddMg0=np.array(tAddMg)
        elif addMDir == 'Z-':
            dof_z = 2 + 7 * (Node.ID[ii])
            massval = JointLoad.FZ[ii] / GrAcc
            if massval < 0:
                tAddMg[dof_z-1:dof_z+1+1,dof_z-1:dof_z+1+1]=-1*massval*np.eye(3)
    return tAddMg
