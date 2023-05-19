###########################################################################################
# MSASolid - Finite element analysis with shell element model (v0.0.1)
#
# Project Leader:
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2023 Siwei Liu, All Right Reserved.
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import timeit, sys, logging, os
# =========================================================================================
# Import internal functions
from analysis.shell.variables import Model
from analysis.shell.util.PrintLog import PrintLog as pl
from analysis.shell.file import ReadData
from analysis.shell.solver import StaticLinear, Eigenbuckling
# =========================================================================================
ProgrameName = " MSASolid - Finite element analysis with shell element model (v0.0.1) "
DeveloperName = " Developed by Mastan Team"
RevisedDate = " Last Revised: May. 03, 2023 "
# =========================================================================================
def Run(argv=''):
    # ----------------------------------------------------------------
    # Initializing
    # ----------------------------------------------------------------
    ReadData.modelfromJSON(FileName=argv)

    Model.initialize()

    pl.Initialize(Model.OutResult.FileName, Model.OutResult.ModelName)
    #logging Logo

    pl.Print(pl.StartMessage(ProgrameName, DeveloperName, RevisedDate))

    pl.Print(pl().PrintModelInfo(Model))

    #if argv =="":
    # Start Timer
    StartTime = timeit.default_timer()
    # ----------------------------------------------------------------
    # Run Analysis
    #Solver(model).run()
    if Model.Analysis.Type == "staticLinear":
          StaticLinear.run()
    elif Model.Analysis.Type == "eigenBuckling":
         Eigenbuckling.run()
    # elif Model.Analysis.Type == "staticNonlinear":
    #     StaticNonlinear.run()
    # elif Model.Analysis.Type == "modalAnalysis":
    #     ModalAnalysis.run()
    # elif Model.Analysis.Type == "dynamicNonlinear":
    #     DynamicNonlinear.run()
    #print(Runtime.getRunTime(StartTime))
    pl.Print(pl.EndMessage())
    pl.Print(pl.GetRunTime(StartTime))
    # ----------------------------------------------------------------
    # Analysis is completed
    # ----------------------------------------------------------------
    return

# =========================================================================================
if __name__ == '__main__':
    # Initialize the analysis model
    try:
        Run()
    except:
        Run()
# =========================================================================================
# END OF PROGRAM
# =========================================================================================
