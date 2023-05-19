#############################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries

import numpy as np
import math

class NonsymWarpingBeam:


    # Member Deflection
    # def GetEleDu(self):
    #
    #     return Du, Dv, Dw, Dtha
    # # Member Force
    # def GetEleF(self):
    #     return Du, Dv, Dw, Dtha

    # Internal functions
    #Get Linear Stiffness Matrix, 14x14
    def GetEleKL(L,E,G,Sect,tSID):
        A=Sect.A[tSID]; Iy=Sect.Iy[tSID]; Iz=Sect.Iz[tSID]; J=Sect.J[tSID]; Cw=Sect.Cw[tSID]
        ky = Sect.ky[tSID];kz = Sect.kz[tSID]
        if ky > 1e2:
            ky = float("inf")
        if kz > 1e2:
            kz = float("inf")
        ## shear
        etayy = (E * Iz) / (ky * A * G)
        etazz = (E * Iy) / (kz * A * G)
        prezz = (12.0*E*Iz)/(L**3+12.0*etayy*L)
        preyy = (12.0 * E * Iy) / (L**3 + 12.0 * etazz * L)
        tMtx=np.zeros((14,14))
        #Non-diagonal
        tMtx[0,7]=-1.0*E*A/L
        tMtx[1,5] = prezz*L/2.0 # tMtx[1,5]=6.0*E*Iz/L**2
        tMtx[1,8] = -prezz # tMtx[1,8]=-1.0*12.0*E*Iz/L**3
        tMtx[1,12] = prezz*L/2.0 # tMtx[1,12]=6.0*E*Iz/L**2
        tMtx[2,4] = -1.0*preyy*L/2.0 # tMtx[2,4]=-1.0*6.0*E*Iy/L**2
        tMtx[2,9] = -1.0*preyy # tMtx[2,9]=-1.0*12.0*E*Iy/L**3
        tMtx[2,11] = -1.0*preyy*L/2.0 # tMtx[2,11]=-1.0*6.0*E*Iy/L**2
        tMtx[3,6]=(60.0*E*Cw*L+G*J*L**3)/(10.0*L**3)
        tMtx[3,10]=-1.0*(120.0*E*Cw+12.0*G*J*L**2)/(10.0*L**3)
        tMtx[3,13]=(60.0*E*Cw*L+G*J*L**3)/(10.0*L**3)
        tMtx[4,9] = 1.0*preyy*L/2.0 # tMtx[4,9]=6.0*E*Iy/L**2
        tMtx[4,11] = preyy*(L**2/6.0-etazz)# tMtx[4,11]=2.0*E*Iy/L
        tMtx[5,8]= -prezz*L/2.0 # tMtx[5,8]=-1.0*6.0*E*Iz/L**2
        tMtx[5,12] = prezz*(L**2/6.0-etayy) # tMtx[5,12]=2.0*E*Iz/L
        tMtx[6,10]=-1.0*(180.0*E*Cw+3.0*G*J*L**2)/(30.0*L**2)
        tMtx[6,13]=(60.0*E*Cw*L-G*J*L**3)/(30.0*L**2)
        tMtx[8,12] = -1.0*prezz*L/2.0 # tMtx[8,12]=-1.0*6.0*E*Iz/L**2
        tMtx[9,11]= preyy*L/2.0# tMtx[9,11]=6.0*E*Iy/L**2
        tMtx[10,13]=-1.0*(60.0*E*Cw*L+G*J*L**3)/(10.0*L**3)
        tMtx+=tMtx.transpose()
        #Diagonal
        tMtx[0,0]= E*A/L
        tMtx[1,1]= prezz # tMtx[1,1]=12.0*E*Iz/L**3
        tMtx[2,2] = preyy # tMtx[2,2]=12.0*E*Iy/L**3
        tMtx[3,3]=(120.0*E*Cw+12.0*G*J*L**2)/(10.0*L**3)
        tMtx[4,4] = preyy*(L**2/3.0+etazz) # tMtx[4,4]=4.0*E*Iy/L
        tMtx[5,5] = prezz*(L**2/3.0+etayy) # tMtx[5,5]=4.0*E*Iz/L
        tMtx[6,6] = (120.0*E*Cw*L+4.0*G*J*L**3)/(30.0*L**2); tMtx[7,7]=E*A/L
        tMtx[8,8] = prezz# tMtx[8,8]=12.0*E*Iz/L**3
        tMtx[9,9] = preyy# tMtx[9,9]=12.0*E*Iy/L**3
        tMtx[10,10]=-1.0*(-1.0*120.0*E*Cw-12.0*G*J*L**2)/(10.0*L**3)
        tMtx[11,11]= preyy*(L**2/3.0+etazz)# tMtx[11,11]=4.0*E*Iy/L
        tMtx[12, 12] = prezz*(L**2/3.0+etayy) # tMtx[12,12]=4.0*E*Iz/L
        tMtx[13,13]=(120.0*E*Cw*L+4.0*G*J*L**3)/(30.0*L**2)
        return tMtx

    #=========================================================================================
    #Get Geometric Stiffness Matrix, 14x14
    def GetEleKG(L,P,My1,My2,Mz1,Mz2,Mx2,Mb,Sect,tSID):
        #Section informations
        A=Sect.A[tSID]; Iy=Sect.Iy[tSID]; Iz=Sect.Iz[tSID]; J=Sect.J[tSID]; Cw=Sect.Cw[tSID]
        yc=Sect.yc[tSID]; zc=Sect.zc[tSID]
        betay=Sect.betay[tSID]; betaz=Sect.betaz[tSID]; betaw=Sect.betaw[tSID]
        #Initialization
        Ip=Iy+Iz; tMtx=np.zeros((14,14))
        #Non-diagonal
        tMtx[0,7]=-1.0*P/L
        tMtx[1,3]=(11.0*My1-My2)/(10.0*L); tMtx[1,4]=Mx2/L; tMtx[1,5]=P/10.0
        tMtx[1,8]=-6.0*P/(5.0*L); tMtx[1,10]=-1.0*(My1-11.0*My2)/(10.0*L)
        tMtx[1,11]=-1.0*Mx2/L; tMtx[1,12]=P/10.0
        tMtx[1,6]=My1/10.0; tMtx[1,13]=-1.0*My2/10.0
        tMtx[2,3]=(11.0*Mz1-Mz2)/(10.0*L); tMtx[2,4]=-1.0*P/10.0; tMtx[2,5]=Mx2/L
        tMtx[2,9]=-6.0*P/(5.0*L); tMtx[2,10]=-1.0*(Mz1-11.0*Mz2)/(10.0*L)
        tMtx[2,11]=-1.0*P/10.0; tMtx[2,12]=-1.0*Mx2/L; tMtx[2,6]=Mz1/10.0
        tMtx[2,13]=-1.0*Mz2/10.0
        tMtx[3,8]=-1.0*(11.0*My1-My2)/(10.0*L)
        tMtx[3,9]=-1.0*(11.0*Mz1-Mz2)/(10.0*L); tMtx[3,10]=-1.0*6.0*P*Ip/(5.0*A)
        tMtx[3,11]=-1.0*(2.0*Mz1+Mz2)/10.0; tMtx[3,12]=(2.0*My1+My2)/10.0
        tMtx[3,6]=P*Ip/(10.0*A); tMtx[3,13]=P*Ip/(10.0*A)
        tMtx[4,8]=-1.0*Mx2/L; tMtx[4,9]=P/10.0
        tMtx[4,10]=-1.0*(Mz1+2.0*Mz2)/10.0; tMtx[4,11]=-1.0*P*L/30.0
        tMtx[4,12]=Mx2/2.0; tMtx[4,6]=-1.0*(3.0*Mz1-Mz2)*L/30.0
        tMtx[4,13]=Mz1*L/30.0; tMtx[5,8]=-1.0*P/10.0; tMtx[5,9]=-1.0*Mx2/L
        tMtx[5,10]=(My1+2.0*My2)/10.0; tMtx[5,11]=-1.0*Mx2/2.0
        tMtx[5,12]=-1.0*P*L/30.0; tMtx[5,6]=(3.0*My1-My2)*L/30.0
        tMtx[5,13]=-1.0*My1*L/30.0; tMtx[8,10]=(My1-11.0*My2)/(10.0*L)
        tMtx[8,11]=Mx2/L; tMtx[8,12]=-1.0*P/10.0; tMtx[8,6]=-1.0*My1/10.0
        tMtx[8,13]=My2/10.0; tMtx[9,10]=(Mz1-11.0*Mz2)/(10.0*L); tMtx[9,11]=P/10.0
        tMtx[9,12]=Mx2/L; tMtx[9,6]=-1.0*Mz1/10.0
        tMtx[9,13]=Mz2/10.0;
        tMtx[10,12]=-1.0*(My1-2.0*My2)/5.0; tMtx[10,6]=-1.0*P*Ip/(10.0*A)
        tMtx[10,13]=-1.0*P*Ip/(10.0*A); tMtx[11,6]=-1.0*Mz2*L/30.0
        tMtx[11,13]=-1.0*(Mz1-3.0*Mz2)*L/30.0; tMtx[12,6]=My2*L/30.0
        tMtx[12,13]=(My1-3.0*My2)*L/30.0; tMtx[6,13]=-P*Ip*L/(30.0*A)
        #Old factors
        tMtx[3,4]=-1.0*(2.0*Mz1-Mz2)/5.0
        tMtx[3,5]=(2.0*My1-My2)/5.0
        tMtx[10,11]=(Mz1-2.0*Mz2)/5.0
        #---------------------------------------------------------------
        #For asymmetric sections
        tMtx[1,3]+=(-6*P*zc)/(5.*L)
        tMtx[1,6]+=-(P*zc)/10.
        tMtx[1,10]+=(6*P*zc)/(5.*L)
        tMtx[1,13]+=-(P*zc)/10.
        tMtx[2,3]+=(6*P*yc)/(5.*L)
        tMtx[2,6]+=(P*yc)/10.
        tMtx[2,10]+=(-6*P*yc)/(5.*L)
        tMtx[2,13]+=(P*yc)/10.
        tMtx[3,4]+=-(P*yc)/10.
        tMtx[3,5]+=-(P*zc)/10.
        tMtx[3,6]+=(betaw*L*Mb+betay*L*My2-betaz*L*Mz2)/(10.*L)
        tMtx[3,8]+=(6*P*zc)/(5.*L)
        tMtx[3,9]+=(-6*P*yc)/(5.*L)
        tMtx[3,10]+=(-12*betaw*Mb+6*betay*My1-6*betay*My2-6*betaz*Mz1+6*betaz*Mz2)/(10.*L)
        tMtx[3,11]+=-(P*yc)/10.
        tMtx[3,12]+=-(P*zc)/10.
        tMtx[3,13]+=(betaw*L*Mb-betay*L*My1+betaz*L*Mz1)/(10.*L)
        tMtx[4,6]+=(-2*L*P*yc)/15.
        tMtx[4,10]+=(P*yc)/10.
        tMtx[4,13]+=(L*P*yc)/30.
        tMtx[5,6]+=(-2*L*P*zc)/15.
        tMtx[5,10]+=(P*zc)/10.
        tMtx[5,13]+=(L*P*zc)/30.
        tMtx[6,8]+=(P*zc)/10.
        tMtx[6,9]+=-(P*yc)/10.
        tMtx[6,10]+=(-6*betaw*Mb-6*betay*My2+6*betaz*Mz2)/60.
        tMtx[6,11]+=(L*P*yc)/30.
        tMtx[6,12]+=(L*P*zc)/30.
        tMtx[6,13]+=(-2*betaw*L*Mb+betay*L*My1-betay*L*My2-betaz*L*Mz1+betaz*L*Mz2)/60.
        tMtx[8,10]+=(-6*P*zc)/(5.*L)
        tMtx[8,13]+=(P*zc)/10.
        tMtx[9,10]+=(6*P*yc)/(5.*L)
        tMtx[9,13]+=-(P*yc)/10.
        tMtx[10,11]+=(P*yc)/10.
        tMtx[10,12]+=(P*zc)/10.
        tMtx[10,13]+=(-(betaw*L*Mb)+betay*L*My1-betaz*L*Mz1)/(10.*L)
        tMtx[11,13]+=(-2*L*P*yc)/15.
        tMtx[12,13]+=(-2*L*P*zc)/15.
        #---------------------------------------------------------------
        tMtx[1,0]+=(Mz1+Mz2)/L**2.
        tMtx[2,0]+=(-My1-My2)/L**2
        tMtx[8,0]+=-(Mz1+Mz2)/L**2
        tMtx[9,0]+=(My1+My2)/L**2
        tMtx[7,1]+=-(Mz1+Mz2)/L**2
        tMtx[7,2]+=(My1+My2)/L**2
        tMtx[7,8]+=-((-Mz1-Mz2)/L**2)
        tMtx[7,9]+=-((My1+My2)/L**2)
        #---------------------------------------------------------------
        tMtx+=tMtx.transpose()
        #Diagonal
        tMtx[0,0]=P/L; tMtx[1,1]=6.0*P/(5.0*L); tMtx[2,2]=6.0*P/(5.0*L)
        tMtx[3,3]=6.0*P*Ip/(5.0*A*L); tMtx[4,4]=2.0*P*L/15.0
        tMtx[5,5]=2.0*P*L/15.0; tMtx[7,7]=P/L
        tMtx[8,8]=6.0*P/(5.0*L); tMtx[9,9]=6.0*P/(5.0*L)
        tMtx[10,10]=6.0*P*Ip/(5.0*A*L); tMtx[11,11]=2.0*P*L/15.0
        tMtx[12,12]=2.0*P*L/15.0; tMtx[6,6]=2.0*P*Ip/(15.0*A)
        tMtx[13,13]=2.0*P*Ip/(15.0*A)
        #---------------------------------------------------------------
        #For asymmetric sections
        tMtx[3,3]+=(12*betaw*Mb-6*betay*My1+6*betay*My2+6*betaz*Mz1-6*betaz*Mz2-10*Mz1*yc-10*Mz2*yc+10*My1*zc+10*My2*zc)/(10.*L)
        tMtx[6,6]+=(8*betaw*L*Mb-6*betay*L*My1+2*betay*L*My2+6*betaz*L*Mz1-2*betaz*L*Mz2)/60.
        tMtx[10,10]+=(12*betaw*Mb-6*betay*My1+6*betay*My2+6*betaz*Mz1-6*betaz*Mz2+10*Mz1*yc+10*Mz2*yc-10*My1*zc-10*My2*zc)/(10.*L)
        tMtx[13,13]+=(8*betaw*L*Mb-2*betay*L*My1+6*betay*L*My2+2*betaz*L*Mz1-6*betaz*L*Mz2)/60.
        return tMtx

    #=========================================================================================
    #Get rigid body Matrix, 14x14
    def GetEleKI(L, P, My1, My2, Mz1, Mz2, Mx2, Mb, Sect, tSID):
        tMtx = np.zeros((14, 14))
        tMtx[3, 4] = -0.5 * Mz1
        tMtx[3, 5] = 0.5 * My1
        tMtx[10, 11] = -0.5 * Mz2
        tMtx[10, 12] = 0.5 * My2
        tMtx += tMtx.transpose()
        return tMtx

    #=========================================================================================
    #Get Mass Matrix, 14x14 -  including lumped and Consistent
    def GetEleMM(Mat, Sect, Member, MassType, tIDX):
        tMtx = np.zeros((14, 14))
        tSectID = Member.SectID[tIDX]
        MatID = Sect.MatID[Member.SectID[tIDX]]
        mL = Member.L[Member.ID[tIDX]]
        ML = Mat.Dens[MatID] * Sect.A[tSectID] * mL  # / (2*GrAcc)
        if MassType == "Consistent":
            MC = ML / 420
            # Consistent Mass for Uniform Sections
            tMtx[4, 2] = -MC * 22 * mL
            tMtx[5, 1] = MC * 22 * mL
            tMtx[6, 0] = ML / 6
            tMtx[7, 1] = MC * 54
            tMtx[7, 5] = MC * 13 * mL
            tMtx[8, 2] = MC * 54
            tMtx[8, 4] = -MC * 13 * mL
            tMtx[10, 2] = MC * 13 * mL
            tMtx[10, 4] = -MC * 3 * mL ** 2
            tMtx[10, 8] = MC * 22 * mL
            tMtx[11, 1] = -MC * 13 * mL
            tMtx[11, 5] = -MC * 3 * mL ** 2
            tMtx[11, 7] = -MC * 22 * mL
            tMtx += tMtx.transpose()
            tMtx[0, 0] = MC * 140
            tMtx[1, 1] = MC * 156
            tMtx[2, 2] = MC * 156
            tMtx[4, 4] = MC * 4 * mL ** 2
            tMtx[5, 5] = MC * 4 * mL ** 2
            tMtx[6, 6] = MC * 140
            tMtx[7, 7] = MC * 156
            tMtx[8, 8] = MC * 156
            tMtx[10, 10] = MC * 4 * mL ** 2
            tMtx[11, 11] = MC * 4 * mL ** 2
        else:  # lumped mass
            tMtx[0, 0] = ML/2.0
            tMtx[1, 1] = ML/2.0
            tMtx[2, 2] = ML/2.0
            tMtx[6, 6] = ML/2.0
            tMtx[7, 7] = ML/2.0
            tMtx[8, 8] = ML/2.0
        # ......Mb1......Mb2
        tMtx[:,[7,12]] = tMtx[:,[6,11]]
        tMtx[:,6] = 0
        return tMtx

