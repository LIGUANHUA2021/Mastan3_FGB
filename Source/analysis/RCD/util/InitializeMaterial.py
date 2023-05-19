#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math
from itertools import zip_longest  # For establishing dictionary
# ===========================================================================
from analysis.RCD.variables import Model

def InitializeSteel(tMatID, tAnalF=1):
    # Initialize variables
    tempout = ""
    tempout2 = ""
    PeakComStress = 0.0
    PeakStrain = 0.0
    ##
    MatIn = Model.Material
    ##
    # Simplified properties
    if MatIn.MatProperty[tMatID] == 1:
        # Whether it can take the tension and compression
        if MatIn.MatSymmetry[tMatID] == 0:  # Symmetry
            temStress = max(abs(MatIn.Fc[tMatID]), abs(MatIn.Ft[tMatID]))
            MatIn.Ft[tMatID] = -1 * temStress
            MatIn.Fc[tMatID] = temStress

            temStrain = max(abs(MatIn.Kc[tMatID]), abs(MatIn.Kt[tMatID]))
            MatIn.Kt[tMatID] = -1 * temStrain
            MatIn.Kc[tMatID] = temStrain
            tempout2 = "Symmetry"

        elif MatIn.MatSymmetry[tMatID] == 1:  # Tension only
            temStress = max(abs(MatIn.Fc[tMatID]), abs(MatIn.Ft[tMatID]))
            MatIn.Ft[tMatID] = -1 * temStress
            MatIn.Fc[tMatID] = 0
            tempout2 = "Tension Only"

            MatIn.Kt[tMatID] = -1 * abs(MatIn.Kt[tMatID])
            MatIn.Kc[tMatID] = abs(MatIn.Kc[tMatID])
        elif MatIn.MatSymmetry[tMatID] == 2:  # Compression only
            temStress = max(abs(MatIn.Fc[tMatID]), abs(MatIn.Ft[tMatID]))
            MatIn.Ft[tMatID] = 0
            MatIn.Fc[tMatID] = temStress
            tempout2 = "Compression Only"

            MatIn.Kt[tMatID] = -1 * abs(MatIn.Kt[tMatID])
            MatIn.Kc[tMatID] = abs(MatIn.Kc[tMatID])

        tempout = 'Simplified Model'
        if tAnalF == 1:
            print(f"    {'Stress vs. strain type  =':<28}{tempout} ({tempout2})")

        # Calculate design strength
        # MatIn[tMatID]['pt'] = MatIn[tMatID]['Ft'] / gamma_ss
        # MatIn[tMatID]['pc'] = MatIn[tMatID]['Fc'] / gamma_ss

        # If analysis is SLS, modify the controlling strain
        # if RunType == 1:  # SLS
        #     if MatIn[mID]['kc'] > 0:
        #         MatIn[mID]['kc'] = MatIn[mID]['pc'] / MatIn[mID]['E']
        #     if MatIn[mID]['kt'] < 0:
        #         MatIn[mID]['kt'] = MatIn[mID]['pt'] / MatIn[mID]['E']
        #
        # print(
        #     f"    {'Design Strength [pc] = ':<28}{MatIn[mID]['pc']:10.5f}; {'Com. Strain [kc]    = ':<25}{MatIn[mID]['kc']:10.5f}")
        # print(
        #     f"    {'Design Strength [pt] = ':<28}{MatIn[mID]['pt']:10.5f}; {'Ten. Strain [kt]    = ':<25}{MatIn[mID]['kt']:10.5f}")

    # Advanced properties
    else:
        tempout = 'Advanced Model'
        print(f'    Stress vs. strain type = {tempout}')

        # Print stress vs. strain value
        MatIn.pc[tMatID] = -999
        MatIn.pt[tMatID] = 999
        MatCurvIN = np.array(MatIn.MatCurveInfo[tMatID]["MATCURVE"])

        # Loop over all material stress vs. strain curve data points
        for ii in np.arange(len(MatCurvIN)):
            CurStrain = MatCurvIN[ii, 1]
            CurStress = MatCurvIN[ii, 2]
            #MatIn[mID].CurStress[II] /= gamma_ss  # Factored stress
            if CurStress > MatIn.pc[tMatID]:
                MatIn.pc[tMatID] = CurStress
                MatIn.Kc[tMatID] = CurStrain

            if CurStress < MatIn.pt[tMatID]:
                MatIn.pt[tMatID] = CurStress
                MatIn.Kt[tMatID] = CurStrain

            print(f'    Point {ii:3} ; Design Strain = {CurStrain:10.5f}; Design Stress = {CurStress:10.5f}')
        # # If analysis is ULS
        # if RunType == 0:  # ULS
        #     MatIn.Kt[tMatID] = MatIn[tMatID].CurStrain[0]
        #     MatIn.Kc[tMatID] = MatIn[tMatID].CurStrain[MatIn[tMatID].CurNum]
        #
        # print(f'    Peak Com. Stress[pc]= {MatIn.pc[tMatID]:10.5f}; Com. Strain [kc]    = {MatIn.Kc[tMatID]:10.5f}')
        # print(f'    Peak Ten. Stress[pt]= {MatIn.pt[tMatID]:10.5f}; Ten. Strain [kt]    = {MatIn.Kt[tMatID]:10.5f}')

    return

def InitializeRebar(tMatID):
    tempout = ''
    tempout2 = ''
    II = 0
    JJ = 0
    temStress = 0.0
    temStrain = 0.0
    PeakComStress = 0.0
    PeakStrain = 0.0
    ##
    MatIn = Model.Material
    ##
    # Simplified properties
    if MatIn.MatProperty[tMatID] == 1:

        # Write Young's modulus and shear modulus to the console
        print(f"    Young's modulus [E]  = {MatIn.E[tMatID]:10.5f}; Shear Modulus [G]   = {MatIn.G[tMatID]:10.5f}")

        # Check whether the material can take tension and compression
        if MatIn.MatSymmetry[tMatID] == 0:  # Symmetry
            temStress = max(abs(MatIn.Fc[tMatID]), abs(MatIn.Ft[tMatID]))
            MatIn.Ft[tMatID] = -1 * temStress
            MatIn.Fc[tMatID] = temStress

            temStrain = max(abs(MatIn.Kc[tMatID]), abs(MatIn.Kt[tMatID]))
            MatIn.Kt[tMatID] = -1 * temStrain
            MatIn.Kc[tMatID] = temStrain
            tempout2 = "Symmetry"

        if MatIn.MatSymmetry[tMatID] == 1:  # 1 for tension only
            temStress = max(abs(MatIn.Fc[tMatID]), abs(MatIn.Ft[tMatID]))
            MatIn.Ft[tMatID] = -1 * temStress
            MatIn.Fc[tMatID] = 0
            tempout2 = "Tension Only"

            # temStrain=Max(Abs(MatIn(mID)%Kc),Abs(MatIn(mID)%Kt))
            MatIn.Kt[tMatID] = -1 * abs(MatIn.Kt[tMatID])
            MatIn.Kc[tMatID] = abs(MatIn.Kc[tMatID])

        if MatIn.MatSymmetry[tMatID] == 2:  # 2 for compression only
            temStress = max(abs(MatIn.Fc[tMatID]), abs(MatIn.Ft[tMatID]))
            MatIn.Ft[tMatID] = 0
            MatIn.Fc[tMatID] = temStress
            tempout2 = "Compression Only"

            # temStrain=Max(Abs(MatIn(mID)%Kc),Abs(MatIn(mID)%Kt))
            MatIn.Kt[tMatID] = -1 * abs(MatIn.Kt[tMatID])
            MatIn.Kc[tMatID] = abs(MatIn.Kc[tMatID])

        tempout = 'Simplified Model'
        print(f"    Stree vs. strain type  = {tempout} ({tempout2})")

        # Calculate design strength
        # MatIn.pt[tMatID] = MatIn.Ft[tMatID] / gamma_sb
        # MatIn.pc[tMatID] = MatIn.Fc[tMatID] / gamma_sb

        # If analysis is SLS, modify the controlling strain
        # if MatIn.RunType[tMatID] == 1:  # SLS
        #     if MatIn.kc[tMatID] > 0:
        #         MatIn.kc[tMatID] = MatIn.pc[tMatID] / MatIn.E[tMatID]
        #     if MatIn.kt[tMatID] < 0:
        #         MatIn.kt[tMatID] = MatIn.pt[tMatID] / MatIn.E[tMatID]
        #
        # print(f"    Design Strength [pc] = {MatIn.pc[tMatID]:.5f}; Com. Strain [kc] = {MatIn.kc[tMatID]:.5f}")
        # print(f"    Design Strength [pt] = {MatIn.pt[tMatID]:.5f}; Ten. Strain [kt] = {MatIn.kt[tMatID]:.5f}")

        # Advanced properties
    else:
        tempout = 'Advanced Model'
        print(f"    Stress vs. strain type  = {tempout}")

        # Print stress vs. strain value
        MatIn.pc[tMatID] = -999
        MatIn.pt[tMatID] = 999
        MatCurvIN = np.array(MatIn.MatCurveInfo[tMatID]["MATCURVE"])

        # Loop over all material stress vs. strain curve data points
        for ii in np.arange(len(MatCurvIN)):
            CurStrain = MatCurvIN[ii, 1]
            CurStress = MatCurvIN[ii, 2]
            # MatIn[tMatID].CurStress[II] /= gamma_sb  # Factored stress
            if CurStress > MatIn.pc[tMatID]:
                MatIn.pc[tMatID] = CurStress
                MatIn.Kc[tMatID] = CurStrain

            if CurStress < MatIn.pt[tMatID]:
                MatIn.pt[tMatID] = CurStress
                MatIn.Kt[tMatID] = CurStrain

            print(f"    Point {ii:3d} ; Design Strain = {CurStrain:10.5f}; "
                  f"Design Stress = {CurStress:10.5f}")

        # If analysis is ULS
        # if RunType == 0:  # ULS
        #     MatIn[tMatID].kt = MatIn[tMatID].CurStrain[1]
        #     MatIn[tMatID].kc = MatIn[tMatID].CurStrain[MatIn[tMatID].CurNum]
        #
        # print(f"    Peak Com. Stress [pc] = {MatIn[tMatID].pc:.5f}; Com. Strain [kc] = {MatIn[tMatID].kc:.5f}")
        # print(f"    Peak Ten. Stress [pt] = {MatIn[tMatID].pt:.5f}; Ten. Strain [kt] = {MatIn[tMatID].kt:.5f}")

    return


def InitializeConcrete(tMatID):
    ##
    tempout = ''
    ##
    MatIn = Model.Material
    ##
    if MatIn.MatProperty[tMatID] == 1:
        #
        # GetConcreteDesignProperties(tMatID)
        #
        print(f'{"Youngs modulus [E]": <20}= {MatIn.E[tMatID]:10.5f}; {"Shear Modulus [G]": <23}= {MatIn.G[tMatID]:10.5f}')
        print(f'{"Cube Strength [fcu]": <20}= {MatIn[tMatID].Fc:10.5f}; {"Design strength [fc]": <23}= {MatIn[tMatID].pc:10.5f}')
        print(f'{"Ini. Yield Strn[kci]": <20}= {MatIn[tMatID].iniKc:10.5f}; {"Max. Frac. Strn.[kc]": <23}= {MatIn[tMatID].Kc:10.5f}')

        # if RunType == 0:  # ULS
        #     tempout = 'Equivalent Stress Block Model'
        #
        # elif RunType == 1:  # SLS
        #     tempout = 'Simple Linear Model'
        #     MatIn[tMatID].Kc = MatIn[tMatID].iniKc
        # print(f'    {"Stress vs. strain type": <20}= {tempout: <42}')

    else:
        tempout = 'Advanced Model'
        print(f'    {"Stress vs. strain type": <20}= {tempout: <42}')

        MatIn.pc[tMatID] = -999.0
        MatCurvIN = np.array(MatIn.MatCurveInfo[tMatID]["MATCURVE"])

        # Loop over all material stress vs. strain curve data points
        for ii in np.arange(len(MatCurvIN)):
            # MatIn[tMatID].CurStress[II] = MatIn[tMatID].CurStress[II] / gamma_cu  # Factored stress
            CurStrain = MatCurvIN[ii, 1]
            CurStress = MatCurvIN[ii, 2]
            if CurStress > MatIn.pc[tMatID]:
                MatIn.pc[tMatID] = CurStress
                MatIn.iniKc[tMatID] = CurStrain

        MatIn.Kc[tMatID] = np.Max(MatCurvIN[:, 1])  # Find the max. compressive strain
        print(f'{"Peak Stress   [fc ]": <20}= {MatIn.pc[tMatID]:10.5f}; {"Fracture Stress[fcu]": <23}= {MatCurvIN[0, 1]:10.5f}')
        print(f'{"Ini. Yield Strn[kci]": <20}= {MatIn.iniKc[tMatID]:10.5f}; {"Max. Frac. Strn.[kc]": <23}= {MatIn.Kc[tMatID]:10.5f}')

        # Print stress vs. strain value
        for ii in np.arange(len(MatCurvIN)):
            print(f'{"Point": <6} {ii:3} ; {"Design Strain": <19}= {MatCurvIN[ii, 1]:10.5f}; {"Design Stress": <19}= {MatCurvIN[ii, 2]:10.5f}')
        return

def InitializeMat(tAnalF=1):
    ##
    NumMat = Model.Material.Count
    MatIn = Model.Material
    if tAnalF == 1:
        print('INITIALIZING MATERIAL PROPERTIES ...')

    for ii in MatIn.ID:
        # Output Name, ID, Type
        if MatIn.MatType[ii] == 1:
            tempout = 'Steel'
        elif MatIn.MatType[ii] == 2:
            tempout = 'Concrete'
        elif MatIn.MatType[ii] == 3:
            tempout = 'Rebar'
        if tAnalF == 1:
            print('    Mat. ID = {:5d} ; Type = {:10s} ; Name = {:20s}'.format(MatIn.ID[ii], tempout, MatIn.Name[ii]))

        if MatIn.MatType[ii] == 1:
            InitializeSteel(ii, tAnalF)
        # elif MatIn.MatType[ii] == 2:
        #     initialze_concrete(ii)
        # elif MatIn.MatType[ii] == 3:
        #     initialze_rebar(ii)

