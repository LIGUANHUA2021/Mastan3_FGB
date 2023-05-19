###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Liang Chen, Wenlong Gao
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# ===========================================================================
# Import standard libraries
#import numpy as np
#import math
import datetime
# Import internal functions
# =========================================================================================

class Welcome:

    LatestTime = '2023/1/18'
    LatestVersion = 'v0.1.3'
    tdate = datetime.datetime.today()
    Thisyear = tdate.year

    def PrintWelcomeInfo(self):
        tOutput = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MSASECT2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n'
        tOutput += '* Welcome to MSASECT2 – Matrix Structural Analysis for Arbitrary Cross-sections' + '\n'
        tOutput += '* Developed by: Siwei Liu and Ronald D. Ziemian.' + '\n'
        tOutput += '* Contributors (surnames in alphabetical order): Liang Chen, Wenlong Gao, Guanhua Li, Weihang Ouyang and Haoyi Zhang' + '\n'
        tOutput += '' + '\n'
        #tOutput += '* For more information, please visit http://www.mastan2.com.' + '\n'
        #tOutput += '' + '\n'
        #tOutput += '* Last Updated: ' +Welcome.LatestTime+ '\n'
        #tOutput += '' + '\n'
        #tOutput += 'Copyright © ' + str(Welcome.Thisyear) + ' Siwei Liu and Ronald D. Ziemian, All Right Reserved.' + '\n'
        tOutput += '* Welcome to MSASECT2, a comprehensive module for generating accurate section properties in frame analysis, hosted on' + '\n'
        tOutput += '  the Mastan platform. Our module is based on the coordinate and finite-element-based methods developed by the Mastan' + '\n'
        tOutput += '  team for analyzing thin-walled and general cross-sections. ' + '\n'
        tOutput += '' + '\n'
        tOutput += '* Before using MSASECT2, please read the disclaimer carefully.'+ '\n'
        #tOutput += '' + '\n'
        # tOutput += '* If you would like to cite MSASECT2 in a paper or presentation, please use the following reference: ' + '\n'
        #tOutput += '* Cite it by "SW Liu and RD Ziemian, "MSASECT2 - Matrix Structural Analysis for Arbitrary Cross-sections", 2023."'+ '\n'
        #tOutput += '' + '\n'
        tOutput += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
        return tOutput

    def PrintYieldSurfaceInfo(self):
        tOutput = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n'
        # tOutput += "~~~~~~~~~~~~~~~ MSASECT2 - Calculate Yield Surface " + Welcome.LatestVersion + " ~~~~~~~~~~~~~ " + '\n'
        # tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n'
        # tOutput += '* Welcome to MSASECT2 – Calculate Yield Surfaces for Arbitrary Cross-sections' + '\n'
        # tOutput += '* Developed by: Siwei Liu ' + '\n'
        # tOutput += '* Contributors (surnames in alphabetical order):' + '\n'
        # tOutput += '* Liang Chen, Wenlong Gao' + '\n'
        # tOutput += '* Last Updated: ' + Welcome.LatestTime + '\n'
        # tOutput += 'Copyright © ' + str(Welcome.Thisyear) + ' Siwei Liu All Right Reserved.' + '\n'
        tOutput += "Please click the 'Run' button to calculate the yield surface!"+ '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n'
        return tOutput