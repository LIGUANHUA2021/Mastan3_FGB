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
# Copyright © 2023 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import timeit, sys, logging, os
from analysis.GlobalBuckling.variables.Model import Material, SecProperties,Analysis

class PrintLog:
    #StartTime = 0.0

    def Initialize(self, FileName, ModelName):
        if os.path.exists(FileName + '.rst' + "/" + ModelName + ".log"):
            os.remove(FileName + '.rst' + "/" + ModelName + ".log")

        Logfile = FileName + '.rst' + "/" + ModelName + ".log"
        #logging.basicConfig(filename=Logfile,filemode="w",format="[%(asctime)s]:\t%(message)s",datefmt="%H:%M:%S",level=logging.INFO)
        logging.basicConfig(filename=Logfile, filemode="w", format="%(message)s", level=logging.INFO)

        #self.StartTime = timeit.default_timer()
        return

    def Print(message):
        print(message)
        logging.info(message)
        return

    def ShowRuntime(self, StartTime):
        tOutPut1 = self.getRunTime(StartTime)
        tOutPut2 = self.EndMessage()
        tOutPut = tOutPut1 + tOutPut2
        return tOutPut

    def StartMessage(tName, tAuthors, tRevisedDate):
        # tOutput = "   " + '\n'
        tOutput = "********************************************************************************" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MASTAN3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "   " + '\n'
        tOutput += "Programe Name: " + tName + '\n'
        tOutput += "Authors: " + tAuthors + '\n'
        tOutput += "Last Revised: " + tRevisedDate + '\n'
        tOutput += "Note: MASTAN3 - Python-based Cross-platforms Frame Analysis Software"
        return tOutput

    def EndMessage(self):
        tOutput = "   " + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
        tOutput += "********************************************************************************" + '\n'
        return tOutput

    @staticmethod
    def getRunTime(StartTime):
        Time = timeit.default_timer() - StartTime
        Time = format(Time, "0.5f")
        tOutput = "********************************************************************************" + '\n'
        tOutput += "Run time = " + str(Time) + " s" + '\n'
        tOutput += "********************************************************************************" + '\n'
        return tOutput

    def PrintModelInfo(self, Model):
        tOutput = "\t\t" + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODEL INFORMATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "* DESCRIPTION" + '\n'
        tOutput += "\t" + Model.Information.Description + '\n'
        tOutput += "* SUMMARY" + '\n'
        tOutput += "\t" + "E OF MATERIAL........................................ = " + str(Model.Material.E) + '\n'
        tOutput += "\t" + "mu OF MATERIAL....................................... = " + str(Model.Material.mu) + '\n'
        tOutput += "\t" + "Fy OF MATERIAL....................................... = " + str(Model.Material.Fy) + '\n'
        tOutput += "\t" + "eu OF MATERIAL....................................... = " + str(Model.Material.eu) + '\n'
        tOutput += "\t\t" + '\n'
        tOutput += "* SECTION PROPERTIES" + '\n'
        tOutput += "\t" + "Area................................................. = " + str(Model.SecProperties.Area) + '\n'
        tOutput += "\t" + "Moment of Inertia of v............................... = " + str(Model.SecProperties.MomentofInertia_v) + '\n'
        tOutput += "\t" + "Moment of Inertia of w............................... = " + str(Model.SecProperties.MomentofInertia_w) + '\n'
        tOutput += "\t" + "Torsion Constant..................................... = " + str(Model.SecProperties.TorsionConstant) + '\n'
        tOutput += "\t" + "Warping Constant..................................... = " + str(Model.SecProperties.WarpingConstant) + '\n'
        tOutput += "\t" + "Shear Centre of v.................................... = " + str(Model.SecProperties.ShearCentre_v) + '\n'
        tOutput += "\t" + "Shear Centre of w.................................... = " + str(Model.SecProperties.ShearCentre_w) + '\n'
        tOutput += "\t" + "Wagner Coefficient of v.............................. = " + str(Model.SecProperties.WagnerCoefficient_v) + '\n'
        tOutput += "\t" + "Wagner Coefficient of w.............................. = " + str(Model.SecProperties.WagnerCoefficient_w) + '\n'
        tOutput += "* ANALYSIS PARAMETERS" + '\n'
        tOutput += "\t" + "Flexural Buckling_Axis............................... = " + str(Model.Analysis.FlexuralBuckling_Axis) + '\n'
        tOutput += "\t" + "Lateraltorsional_Buckling_Axis....................... = " + str(Model.Analysis.Lateraltorsional_Buckling_Axis) + '\n'
        tOutput += "\t" + "Minimun Slender Ratio................................ = " + str(Model.Analysis.SlenderRatio_min) + '\n'
        tOutput += "\t" + "Maximun Slender Ratio................................ = " + str(Model.Analysis.SlenderRatio_max) + '\n'
        tOutput += "\t" + "Steps of Slender Ratio............................... = " + str(Model.Analysis.SlenderRatio_steps) + '\n'
        if  Analysis.TwistingEffects == 1:
            tOutput += "\t" + "Twisting Effects..................................... = " + str("ON") + '\n'
        elif Analysis.TwistingEffects == 0:
            tOutput += "\t" + "Twisting Effects..................................... = " + str("OFF") + '\n'
        return tOutput


