###########################################################################################
#
# PyFESect - Python-based Cross-platforms Section Analysis Software
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Liang Chen, Haoyi Zhang, Guanhua Li
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import numpy as np
# =========================================================================================
# Import internal functions
from analysis.GlobalBuckling.variables.Model import Material, SecProperties,Analysis

# =========================================================================================

def CalFlexuralBuckling ():
    # =========================================================================================
    # Read input data
    # =========================================================================================
    # Read material properties
    E = Material.E
    mu = Material.mu
    Fy = Material.Fy
    eu = Material.eu
    # Read section properties
    A = SecProperties.Area
    Iv = SecProperties.MomentofInertia_v
    Iw = SecProperties.MomentofInertia_w
    I_major = max(Iw, Iv)
    I_minor = min(Iw, Iv)
    # =========================================================================================
    # Calculate flexural buckling
    # =========================================================================================
    Lamuda_min = Analysis.SlenderRatio_min
    Lamuda_max = Analysis.SlenderRatio_max
    Lamuda_steps = Analysis.SlenderRatio_steps
    if Analysis.FlexuralBuckling_Axis == "Minor":
        r = np.sqrt(I_minor / A)
    elif Analysis.FlexuralBuckling_Axis == "Major":
        r = np.sqrt(I_minor / A)
    Lamuda = np.array(list(np.arange(Lamuda_min, (Lamuda_max + (Lamuda_max - Lamuda_min) / Lamuda_steps), (Lamuda_max - Lamuda_min) / Lamuda_steps)))
    L = Lamuda * r
    Pfb = []
    if Analysis.FlexuralBuckling_Axis == "Minor":
        for i in range(len(L)):
            Pfb.append(np.pi ** 2 * E * I_minor / (L [i]) ** 2)
    elif Analysis.FlexuralBuckling_Axis == "Major":
        for i in range(len(L)):
            Pfb.append(np.pi ** 2 * E * I_major / (L [i]) ** 2)
    return Lamuda, Pfb

def CalAxialtorsionalBuckling ():
    # =========================================================================================
    # Read input data
    # =========================================================================================
    # Read material properties
    E = Material.E
    mu = Material.mu
    Fy = Material.Fy
    eu = Material.eu
    G = E / (2 * (1 + mu))
    # Read section properties
    A = SecProperties.Area
    Iv = SecProperties.MomentofInertia_v
    Iw = SecProperties.MomentofInertia_w
    I_major = max(Iw, Iv)
    I_minor = min(Iw, Iv)
    Iww = SecProperties.WarpingConstant
    J = SecProperties.TorsionConstant
    vs = SecProperties.ShearCentre_v
    ws = SecProperties.ShearCentre_w
    TwistEffects = Analysis.TwistingEffects
    # =========================================================================================
    # Calculate axial-torsional buckling
    # =========================================================================================
    Lamuda_min = Analysis.SlenderRatio_min
    Lamuda_max = Analysis.SlenderRatio_max
    Lamuda_steps = Analysis.SlenderRatio_steps
    if Analysis.FlexuralBuckling_Axis == "Minor":
        r = np.sqrt(I_minor / A)
    elif Analysis.FlexuralBuckling_Axis == "Major":
        r = np.sqrt(I_minor / A)
    Lamuda = np.array(list(np.arange(Lamuda_min, (Lamuda_max + (Lamuda_max - Lamuda_min) / Lamuda_steps), (Lamuda_max - Lamuda_min) / Lamuda_steps)))
    L = Lamuda * r
    Patb = []
    if TwistEffects == 0:
        for i in range(len(L)):
            Patb.append((G * J + np.pi**2 * E * Iww / L[i]**2) / ((Iv + Iw) / A))
    elif TwistEffects == 1:
        for i in range(len(L)):
            Patb.append((G * J + np.pi**2 * E * Iww / L[i]**2) / (vs**2 + ws**2 + (Iv + Iw) / A ))
    return Lamuda, Patb

def CalLateraltorsionalBuckling ():
    # =========================================================================================
    # Read input data
    # =========================================================================================
    # Read material properties
    E = Material.E
    mu = Material.mu
    Fy = Material.Fy
    eu = Material.eu
    G = E / (2 * (1 + mu))
    # Read section properties
    A = SecProperties.Area
    Iv = SecProperties.MomentofInertia_v
    Iw = SecProperties.MomentofInertia_w
    I_major = max(Iw, Iv)
    I_minor = min(Iw, Iv)
    Iww = SecProperties.WarpingConstant
    J = SecProperties.TorsionConstant
    Beta_v= SecProperties.WagnerCoefficient_v
    Beta_w= SecProperties.WagnerCoefficient_w
    # =========================================================================================
    # Calculate lateral-torsional buckling
    # =========================================================================================
    Lamuda_min = Analysis.SlenderRatio_min
    Lamuda_max = Analysis.SlenderRatio_max
    Lamuda_steps = Analysis.SlenderRatio_steps
    TwistEffects = Analysis.TwistingEffects
    if Analysis.FlexuralBuckling_Axis == "Minor":
        r = np.sqrt(I_minor / A)
    elif Analysis.FlexuralBuckling_Axis == "Major":
        r = np.sqrt(I_minor / A)
    Lamuda = np.array(list(np.arange(Lamuda_min, (Lamuda_max + (Lamuda_max - Lamuda_min) / Lamuda_steps), (Lamuda_max - Lamuda_min) / Lamuda_steps)))
    L = Lamuda * r
    Pltb = []
    if TwistEffects == 0:
        Beta = 0
        if Analysis.Lateraltorsional_Buckling_Axis == "Major":
            for i in range(len(L)):
                Pltb.append(np.pi**2 * E * I_minor / L[i]**2 * (Beta / 2 + np.sqrt((Beta / 2)**2 + Iww / I_minor + G * J * L[i]**2 / (E * I_minor * np.pi**2))))
        elif Analysis.Lateraltorsional_Buckling_Axis == "Minor":
            for i in range(len(L)):
                Pltb.append(np.pi**2 * E * I_major / L[i]**2 * (Beta / 2 + np.sqrt((Beta / 2)**2 + Iww / I_major + G * J * L[i]**2 / (E * I_major * np.pi**2))))
    elif TwistEffects == 1:
        Pltb1 = []
        Pltb2 = []
        if Analysis.Lateraltorsional_Buckling_Axis == "Major":
            if I_minor == Iv:
                Beta = Beta_w
            else:
                Beta = Beta_v
            for i in range(len(L)):
                Pltb1.append(np.pi**2 * E * I_minor / L[i]**2 * (Beta / 2 + np.sqrt((Beta / 2)**2 + Iww / I_minor + G * J * L[i]**2 / (E * I_minor * np.pi**2))))
            for ii in range(len(L)):
                Pltb2.append(np.pi**2 * E * I_minor / L[ii]**2 * (- Beta / 2 + np.sqrt((Beta / 2)**2 + Iww / I_minor + G * J * L[ii]**2 / (E * I_minor * np.pi**2))))
            Pltb.append(Pltb1)
            Pltb.append(Pltb2)
        elif Analysis.Lateraltorsional_Buckling_Axis == "Minor":
            if I_major == Iv:
                Beta = Beta_w
            else:
                Beta = Beta_v
            for i in range(len(L)):
                Pltb1.append(np.pi**2 * E * I_major / L[i]**2 * (Beta / 2 + np.sqrt((Beta / 2)**2 + Iww / I_major + G * J * L[i]**2 / (E * I_major * np.pi**2))))
            for ii in range(len(L)):
                Pltb2.append(np.pi**2 * E * I_major / L[ii]**2 * (- Beta / 2 + np.sqrt((Beta / 2)**2 + Iww / I_major + G * J * L[ii]**2 / (E * I_major * np.pi**2))))
            Pltb.append(Pltb1)
            Pltb.append(Pltb2)
    return Lamuda, Pltb