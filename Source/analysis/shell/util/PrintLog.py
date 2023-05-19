###########################################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
###########################################################################################
# Description:
# ===========================================================================
# Import standard libraries
#import numpy as np
#import math
import timeit, sys, logging, os
# Import internal functions
# =========================================================================================

class PrintLog:
    #StartTime = 0.0

    def Initialize(FileName, ModelName):
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

    def EndMessage():
        tOutput = "   " + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
        tOutput += "********************************************************************************" + '\n'
        return tOutput

    def GetRunTime(StartTime):
        Time = timeit.default_timer() - StartTime
        Time = format(Time, "0.2f")
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
        tOutput += "\t" + "NUM. OF NODES........................................ = " + str(Model.Node.Count) + '\n'
        tOutput += "\t" + "NUM. OF ElementS...................................... = " + str(Model.Element.Count) + '\n'
        tOutput += "\t" + "NUM. OF MATERIALS.................................... = " + str(Model.Material.Count) + '\n'
        tOutput += "\t" + "NUM. OF SECTIONS..................................... = " + str(Model.Section.Count) + '\n'
        tOutput += "\t" + "NUM. OF BOUNDARY..................................... = " + str(Model.Boundary.Count) + '\n'
        tOutput += "\t" + "NUM. OF JOINTLOAD.................................... = " + str(Model.JointLoad.Count) + '\n'
        tOutput += "\t\t" + '\n'
        tOutput += "* ANALYSIS PARAMETERS" + '\n'
        tOutput += "\t" + "TYPE ................................................ = " + Model.Analysis.Type + '\n'
        if Model.Analysis.Type == "staticLinear":
            tOutput += "\t" + "TARGET LOAD FACTOR................................... = " + str(Model.Analysis.TargetLF) + '\n'
        elif Model.Analysis.Type == "staticNonlinear":
            tOutput += "\t" + "TARGET LOAD FACTOR................................... = " + str(Model.Analysis.TargetLF) + '\n'
            tOutput += "\t" + "LOAD STEP............................................ = " + str(Model.Analysis.LoadStep) + '\n'
            tOutput += "\t" + "MAX. ITERATION....................................... = " + str(Model.Analysis.MaxIter) + '\n'
            tOutput += "\t" + "CONVERGENCE.......................................... = " + str(Model.Analysis.TOL) + '\n'
            tOutput += "\t" + "SOLUTION TECHNIQUE................................... = " + str(Model.Analysis.SolnTech) + '\n'
        elif (Model.Analysis.Type == "eigenBuckling" or Model.Analysis.Type == "modalAnalysis"):
            tOutput += "\t" + "MODES NUMBER......................................... = " + str(Model.Analysis.ModesNum) + '\n'
        elif Model.Analysis.Type == "dynamicNonlinear":
            tOutput += "\t" + "TARGET LOAD FACTOR................................... = " + str(Model.Analysis.TargetLF) + '\n'
            tOutput += "\t" + "LOAD STEP............................................ = " + str(Model.Analysis.LoadStep) + '\n'
            tOutput += "\t" + "MAX. ITERATION....................................... = " + str(Model.Analysis.MaxIter) + '\n'
            tOutput += "\t" + "CONVERGENCE.......................................... = " + str(Model.Analysis.TOL) + '\n'
            tOutput += "\t" + "MASS TYPE............................................ = " + str(Model.Analysis.MassType) + '\n'
            tOutput += "\t" + "ADDITIONAL MASS DIRECTION............................ = " + str(Model.Analysis.AddMassDir) + '\n'
            tOutput += "\t" + "NEWMARK GAMMA........................................ = " + str(Model.Analysis.NewmarkGamma) + '\n'
            tOutput += "\t" + "NEWMARK BETA......................................... = " + str(Model.Analysis.NewmarkBeta) + '\n'
            tOutput += "\t" + "TOTAL TIME STEPS..................................... = " + str(Model.Analysis.TotalTimeSteps) + '\n'
            tOutput += "\t" + "TIME INCREMENT (SEC.)................................ = " + str(Model.Analysis.Timeincr) + '\n'
            tOutput += "\t" + "DAMPING RATIO........................................ = " + str(Model.Analysis.DampingRatio) + '\n'
            tOutput += "\t" + "FIRST FREQUENCY...................................... = " + str(Model.Analysis.FirstFreq) + '\n'
            tOutput += "\t" + "SECOND FREQUENCY..................................... = " + str(Model.Analysis.SecondFreq) + '\n'
            tOutput += "\t" + "GRAVITATIONAL ACCELERATION........................... = " + str(Model.Analysis.GraAcc) + '\n'
        else:
            tOutput += "Please check Analysis type !! "

        tOutput += "\t\t" + '\n'
        tOutput += "* MATERIAL DEFINITION" + '\n'
        for ii in Model.Material.ID:
            tOutput += "\t" + "ID = " + str(int(ii)).zfill(3) + "; " + "E = " + str(format(Model.Material.E[ii], "0.4e")) + "; "\
                    + "G = " + str(format(Model.Material.G[ii], "0.4e")) + "; " + "Nu = " + str(format(Model.Material.Nu[ii], "0.4e")) + "; " \
                       + "FY = " + str(format(Model.Material.Fy[ii], "0.4e")) + "; "\
                    + "DENSITY = " + str(format(Model.Material.Dens[ii], "0.4e")) + "; " + '\n'

        tOutput += "\t\t" + '\n'
        tOutput += "* SECTION DEFINITION" + '\n'
        for ii in Model.Section.ID:
            if Model.Section.ElementType[ii] == 2:
                tOutput += "\t" + "ID = " + str(int(ii)).zfill(3) + "; " + "ELEMENT TYPE = " + "Warping Beam-Column Element" + "; " +'\n'

            tOutput += "\t" + "MAT. ID = " + str(int(Model.Section.MatID[ii])).zfill(3) + "; " + "t = " + str(format(Model.Section.t[ii], "0.4e")) + "; "\
                     + '\n'

        tOutput += "\t\t" + '\n'
        tOutput += "* NODAL COORDINATES IN GLOBAL AXIS   " + '\n'
        tOutput += "\t" + "ID." + "\t\t" + "X-COOR." + "\t\t\t" + "Y-COOR." + "\t\t\t" + "Z-COOR." + '\n'
        for jj in Model.Node.ID:
            tOutput += "\t" + str(int(jj)) + "\t\t" + str(format(Model.Node.X[jj], "0.4e")) \
                    + "\t\t" + str(format(Model.Node.Y[jj], "0.4e")) + "\t\t" + str(format(Model.Node.Z[jj], "0.4e")) + '\n'

        tOutput += "\t\t" + '\n'
        tOutput += "* Element CONNECTIVITY" + '\n'
        tOutput += "\t" + "ID." + "\t\t" + "SECT." + "\t\t" + "NODE I" + "\t\t" + "NODE J" + "\t\t" + "NODE K" + '\n'
        for ii in Model.Element.ID:
            tOutput += "\t" + str(int(ii)) + "\t\t" + str(int(Model.Element.SectID[ii])) + "\t\t\t" \
                       + str(int(Model.Element.I[ii])) + "\t\t\t" + str(int(Model.Element.J[ii])) + "\t\t\t" \
                       + str(format(Model.Element.K[ii])) + '\n'

        tOutput += "\t\t" + '\n'
        tOutput += "* BOUNDARY" + '\n'
        tOutput += "\t" + "ID." + "\t\t" + "UX" + "\t\t" + "UY" + "\t\t" + "UZ" + "\t\t" + "RX" + "\t\t" + "RY" \
                + "\t\t" + "RZ" + '\n'
        for ii in Model.Boundary.NodeID:
            tOutput += "\t" + str(int(ii)) + "\t\t" + str(int(Model.Boundary.UX[ii])) + "\t\t" + str(int(Model.Boundary.UY[ii])) \
                    + "\t\t" + str(int(Model.Boundary.UZ[ii])) + "\t\t" + str(int(Model.Boundary.RX[ii])) \
                    + "\t\t" + str(int(Model.Boundary.RY[ii])) + "\t\t" + str(int(Model.Boundary.RZ[ii])) + '\n'

        tOutput += "\t\t" + '\n'
        tOutput += "* JOINTLOAD" + '\n'
        tOutput += "\t" + "ID." + "\t\t" + "FX" + "\t\t\t" + "FY" + "\t\t\t" + "FZ" + "\t\t\t" + "MX" + "\t\t\t" + "MY" \
                   + "\t\t\t" + "MZ" + '\n'
        for ii in Model.JointLoad.NodeID:
            tOutput += "\t" + str(int(ii)) + "\t" + str(format(Model.JointLoad.FX[ii], "0.3e")) + "\t" + str(format(Model.JointLoad.FY[ii], "0.3e")) \
                       + "\t" + str(format(Model.JointLoad.FZ[ii], "0.3e")) + "\t" + str(format(Model.JointLoad.MX[ii], "0.3e")) \
                       + "\t" + str(format(Model.JointLoad.MY[ii], "0.3e")) + "\t" + str(format(Model.JointLoad.MZ[ii], "0.3e")) + '\n'

        tOutput += "\t\t" + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SOLUTION START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n'
        tOutput += "********************************************************************************" + '\n'
        return tOutput