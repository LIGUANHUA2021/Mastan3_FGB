#############################################################################
# RCD - Python-based Cross-platforms Complex cross-section analysis and design Software

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
#############################################################################
# Function purpose:
# ===========================================================================
# Description:
# ===========================================================================
# Import standard libraries
#import numpy as np
#import math
import timeit, sys, logging, os, codecs
# Import internal functions
# =========================================================================================
class PLog:
    def Initialize(self):
        return
    def printLogo(self):
        tOutput ="____________________________________________________________________________"+ '\r\n'
        # tOutput +=""+ '\r\n'
        # tOutput +="  RRRRRRRRRRRRRRRRR              CCCCCCCCCCCCC   DDDDDDDDDDDDD        "+ '\r\n'
        # tOutput +="  R::::::::::::::::R          CCC::::::::::::C   D::::::::::::DDD     "+ '\r\n'
        # tOutput +="  R::::::RRRRRR:::::R       CC:::::::::::::::C   D:::::::::::::::DD   "+ '\r\n'
        # tOutput +="  RR:::::R     R:::::R     C:::::CCCCCCCC::::C   DDD:::::DDDDD:::::D  "+ '\r\n'
        # tOutput +="    R::::R     R:::::R   C:::::C                   D:::::D     D:::::D"+ '\r\n'
        # tOutput +="    R::::RRRRRR:::::R    C:::::C                   D:::::D     D:::::D"+ '\r\n'
        # tOutput +="    R:::::::::::::RR     C:::::C                   D:::::D     D:::::D"+ '\r\n'
        # tOutput +="    R::::RRRRRR:::::R    C:::::C                   D:::::D     D:::::D"+ '\r\n'
        # tOutput +="    R::::R     R:::::R   C:::::C                   D:::::D     D:::::D"+ '\r\n'
        # tOutput +="    R::::R     R:::::R   C:::::C                   D:::::D     D:::::D"+ '\r\n'
        # tOutput +="    R::::R     R:::::R    C:::::C       CCCCCC     D:::::D    D:::::D "+ '\r\n'
        # tOutput +="  RR:::::R     R:::::R     C:::::CCCCCCCC::::C   DDD:::::DDDDD:::::D  "+ '\r\n'
        # tOutput +="  R::::::R     R:::::R      CC:::::::::::::::C   D:::::::::::::::DD  "+ '\r\n'
        # tOutput +="  R::::::R     R:::::R        CCC::::::::::::C   D::::::::::::DDD     "+ '\r\n'
        # tOutput +="  RRRRRRRR     RRRRRRR           CCCCCCCCCCCCC   DDDDDDDDDDDDD        "+ '\r\n'
        # tOutput +=""+ '\r\n'
        tOutput +="____________________________________________________________________________"+ '\r\n'
        return print(tOutput)

    def StartMessage(self, tName, tAuthors, tRevisedDate):
        # tOutput = "   " + '\n'
        tOutput = "****************************************************************************" + '\r\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PyRCD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\r\n'
        tOutput += "****************************************************************************" + '\r\n'
        tOutput += "   " + '\r\n'
        tOutput += "Programe Name: " + tName + '\r\n'
        tOutput += "Authors: " + tAuthors + '\r\n'
        tOutput += "Last Revised: " + tRevisedDate + '\r\n'
        tOutput += "Note: PyRCD - Python-based Complex Cross Section Yield Surface Analysis Software"
        return print(tOutput)

    def GetRunTime(self, StartTime):
        Time = timeit.default_timer() - StartTime
        Time = format(Time, "0.2f")
        tOutput = "********************************************************************************" + '\r\n'
        tOutput += "Run time = " + str(Time) + " s" + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        return print(tOutput)

    def EndMessage(self):
        tOutput = "   " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        return print(tOutput)