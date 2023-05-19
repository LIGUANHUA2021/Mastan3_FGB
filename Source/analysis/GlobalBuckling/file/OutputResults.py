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
# ===========================================================================
# Import standard libraries
import numpy as np
# Import internal functions

def StartMessage(tName, tAuthors, tRevisedDate):
    tOutput = "********************************************************************************\n"
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~Global Buckling Analysis Software~~~~~~~~~~~~~~~~~~~~~~~~\n"
    tOutput += "********************************************************************************\n\n"
    tOutput += "Programme Name: {}\n".format(tName)
    tOutput += "Authors: {}\n".format(tAuthors)
    tOutput += "Last Revised: {}\n".format(tRevisedDate)
    tOutput += "Note: Global Buckling Analysis Software"
    return tOutput

def EndMessage():
    tOutput = "\n"
    tOutput += "********************************************************************************\n"
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    tOutput += "********************************************************************************\n"
    return tOutput


def AddResult():
    tOutput = "\n"
    tOutput += "********************************************************************************\n"
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Global Buckling Results ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    tOutput += "********************************************************************************\n"
    return tOutput

def Output(Lamuda, Pfb, Patb, Pltb):
    tOutput = "\t\t" + '\n'
    tOutput += "* Flexural Buckling" + '\n'
    tOutput += "\t\t" + '\n'
    tOutput += "Slender Ratio" + '\t'+ '\t' + "Compression Load" + '\n'
    for i in range(len(Lamuda)):
        tOutput += str(format(Lamuda[i], "0.4e")) + '\t'+ '\t'+ '\t' + str(format(Pfb[i], "0.4e")) + '\n'
    tOutput += "\t\t" + '\n'
    tOutput += "* Axial-torsional Buckling" + '\n'
    tOutput += "\t\t" + '\n'
    tOutput += "Slender Ratio" + '\t'+ '\t' + "Compression Load" + '\n'
    for i in range(len(Lamuda)):
        tOutput += str(format(Lamuda[i], "0.4e")) +  '\t'+ '\t'+'\t' + str(format(Patb[i], "0.4e")) + '\n'
    tOutput += "\t\t" + '\n'
    tOutput += "* Lateral-torsional Buckling" + '\n'
    tOutput += "\t\t" + '\n'
    if len(Pltb) != 2:
        tOutput += "Slender Ratio" + '\t' + '\t'+ "Bending Load" + '\n'
        for i in range(len(Lamuda)):
            tOutput += str(format(Lamuda[i], "0.4e")) +  '\t'+ '\t'+'\t' + str(format(Pltb[i], "0.4e")) + '\n'
        tOutput += "\t\t" + '\n'
    if len(Pltb) == 2:
        tOutput += "Slender Ratio" + '\t'+ '\t' + "Bending Load (M+)" + '\n'
        for i in range(len(Lamuda)):
            tOutput += str(format(Lamuda[i], "0.4e")) +  '\t'+ '\t'+'\t' + str(format(Pltb[0][i], "0.4e")) + '\n'
        tOutput += "\t\t" + '\n'
        tOutput += "Slender Ratio" + '\t'+ '\t' + "Bending Load (M-)" + '\n'
        for i in range(len(Lamuda)):
            tOutput += str(format(Lamuda[i], "0.4e")) +  '\t'+ '\t'+'\t' + str(format(Pltb[1][i], "0.4e")) + '\n'
        tOutput += "\t\t" + '\n'
    return tOutput


def Output_msa(Lamuda):
    tOutput = "\t\t" + '\n'
    tOutput += "* Calculating Flexural Buckling ..." + '\n'
    tOutput += "\t\t" + '\n'
    for ii in range(len(Lamuda)):
        tOutput += ">>> Flexural Buckling Step = %s, Current λ = %s, Calculation successful" % (
        ii + 1, '{:.2f}'.format(Lamuda[ii])) + '\n'
    tOutput += "\t\t" + '\n'
    tOutput += "* Calculating Axial-torsional Buckling ..." + '\n'
    tOutput += "\t\t" + '\n'
    for ii in range(len(Lamuda)):
        tOutput += ">>> Axial-torsional Buckling Step = %s, Current λ = %s, Calculation successful" % (
        ii + 1, '{:.2f}'.format(Lamuda[ii])) + '\n'
    tOutput += "\t\t" + '\n'
    tOutput += "* Calculating Lateral Torsion Buckling ..." + '\n'
    tOutput += "\t\t" + '\n'
    for ii in range(len(Lamuda)):
        tOutput += ">>> Lateral Torsion Buckling Step = %s, Current λ = %s, Calculation successful" % (
        ii + 1, '{:.2f}'.format(Lamuda[ii])) + '\n'
    return tOutput

def AddResult_msa():
    tOutput = "\n"
    tOutput += "********************************************************************************\n"
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~ Global Buckling Calculating ~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    tOutput += "********************************************************************************\n"
    return tOutput




