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

def StartMessage(tName, tAuthors, tRevisedDate):
    #tOutput = "   " + '\n'
    tOutput =  "****************************************************************************************" + '\n'
    tOutput += "Programe Name: " + tName + '\n'
    tOutput += "Authors: " + tAuthors + '\n'
    tOutput += "Last Revised: " + tRevisedDate + '\n'
    #tOutput += "Note: MASTAN3 - Python-based Cross-platforms Frame Analysis Software" + '\n'
    tOutput += "****************************************************************************************"+ '\n'
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
    tOutput += "****************************************************************************************" + '\n'
    return tOutput

def EndMessage():
    tOutput = "   " + '\n'
    tOutput += "****************************************************************************************" + '\n'
    tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
    tOutput += "****************************************************************************************" + '\n'
    return tOutput
# print(getLogo("Mastan3", "v0.1", "SW Liu"))
