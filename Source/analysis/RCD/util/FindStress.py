#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
# ===========================================================================
from analysis.RCD.variables import Model

def FindStress(CurStrn, CurMatID):
    # CurStrn: current strain
    # CurStress: current stress
    # CurMatID: current material ID

    # Initializing
    CurStress = 0
    ActMatID = CurMatID
    ##
    MatIn = Model.Material
    ##
    # Find stress for different material types
    if MatIn.MatType[ActMatID] == 1 or MatIn.MatType[ActMatID] == 3:  # For steel and rebar
        CurStress = FindSteelStress(CurStrn, ActMatID)

    elif MatIn.MatType[ActMatID] == 2:  # For concrete
        CurStress = FindConcreteStress(CurStrn, ActMatID)

    return CurStress

def FindSteelStress(CurStrn, CurMatID):
    # Initializing
    CurStress = 0
    ##
    MatIn = Model.Material
    s1, n1, s2, n2 = 0, 0, 0, 0

    # Check if compression or tension
    if CurStrn >= 0:  # Compression
        # Simple material property
        if MatIn.MatProperty[CurMatID] == 1:
            CurStress = CurStrn * MatIn.E[CurMatID]
            if CurStress > MatIn.Fc[CurMatID]:
                CurStress = MatIn.Fc[CurMatID]
        # Advanced material property
        else:
            pass
            # if abs(CurStrn) >= abs(MatIn.MaxComStn[CurMatID]):
            #     CurStress = MatIn[CurMatID].CurStress[MatIn[CurMatID].CurNum]
            # else:
            #     for JJ in range(MatIn[CurMatID].CurZero, MatIn[CurMatID].CurNum + 1):
            #         if MatIn[CurMatID].CurStrain[JJ] > abs(CurStrn):
            #             if JJ == MatIn[CurMatID].CurZero:
            #                 # s1 = 0
            #                 # n1 = 0
            #                 pass
            #             else:
            #                 s1 = MatIn[CurMatID].CurStress[JJ - 1]
            #                 n1 = MatIn[CurMatID].CurStrain[JJ - 1]
            #
            #                 s2 = MatIn[CurMatID].CurStress[JJ]
            #                 n2 = MatIn[CurMatID].CurStrain[JJ]
            #
            #                 CurStress = s1 + (CurStrn - n1) * (s2 - s1) / (n2 - n1)
            #             break
    else:  # Tension
        # Simple material property
        if MatIn.MatProperty[CurMatID] == 1:
            CurStress = CurStrn * MatIn.E[CurMatID]
            if abs(CurStress) > abs(MatIn.Ft[CurMatID]):
                CurStress = MatIn.Ft[CurMatID]
        # Advanced material property
        else:
            pass
            # if abs(CurStrn) >= abs(MatIn.MaxTenStn[CurMatID]):
            #     CurStress = MatIn[CurMatID].CurStress[1]
            # else:
            #     for JJ in range(MatIn[CurMatID].CurZero, 0, -1):
            #         if abs(MatIn[CurMatID].CurStrain[JJ]) > abs(CurStrn):
            #             if JJ == MatIn[CurMatID].CurZero:
            #                 # s1 = 0
            #                 # n1 = 0
            #                 pass
            #             else:
            #                 s1 = MatIn[CurMatID].CurStress[JJ + 1]
            #                 n1 = MatIn[CurMatID].CurStrain[JJ + 1]
            #
            #                 s2 = MatIn[CurMatID].CurStress[JJ]
            #                 n2 = MatIn[CurMatID].CurStrain[JJ]
            #
            #                 CurStress = s1 + (CurStrn - n1) * (s2 - s1) / (n2 - n1)
            #             break

    return CurStress

def FindConcreteStress(CurStrn, ActMatID):
    # Initializing
    CurStress = 0

    return CurStress