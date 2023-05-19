###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
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
from analysis.RCD.variables import Model
from analysis.RCD.file import ReadData
from analysis.RCD.solver import RunAnalysis
from analysis.RCD.util.PrintLog import PLog
# =========================================================================================
ProgrameName = " PyRCD - Python-based Complex Cross Section Yield Surface Analysis Software (v0.0.9) "
DeveloperName = " Copyright © 2023 Siwei Liu, All Right Reserved."
RevisedDate = " Last Revised: March 26, 2023 "
# =========================================================================================
# =========================================================================================
# @jit(nopython=True)

def Run(analFlag, argv="", progress_Signal=None, finish_Signal=None):
    # ----------------------------------------------------------------
    # Initializing
    # ----------------------------------------------------------------
    ReadData.modelfromJSON(FileName=argv, tAnalFlag=analFlag)
    # Model.initialize()
    # pl().Initialize(Model.OutResult.FileName, Model.OutResult.ModelName)
    # # plogger = pl(Model.OutResult.FileName, Model.OutResult.ModelName)
    # # logging Logo
    # # pl().Print(pl().StartMessage(ProgrameName, DeveloperName, RevisedDate))
    # pl().Print(pl().PrintModelInfo(Model))
    # # if argv =="":
    StartTime = timeit.default_timer()
    # # ---------------------------------------------------------------------------------
    # ##################################### Main function ###############################
    # ###################################################################################
    # if analType == 1: ## 1 for Sectional properties
    #     CalSectionProperties.CalSectProps(Model)
    #     # ---------------------------------------------------------------------------------
    #     pl().Print(pl().PrintSectProInfo(Model))
    #     pl().OutputSectProps(Model, ProgrameName, DeveloperName, RevisedDate)
    #     pl().Print(pl().ShowRuntime(StartTime))
    # elif analType == 2: ## 2 for Sectional Yield Surface
    #     CalYieldSurface.CalYieldS().Run()
    #     pl().Print(pl().GetRunTime(StartTime))
    if analFlag == 999:
        RunAnalysis.RunAnal(tAnalF=999)
    else:
        PLog().printLogo()
        PLog().StartMessage(ProgrameName, DeveloperName, RevisedDate)
        ##
        RunAnalysis.RunAnal()
        ##
    PLog().EndMessage()
    PLog().GetRunTime(StartTime)
    # ----------------------------------------------------------------
    # Analysis is completed
    # ----------------------------------------------------------------
    if progress_Signal:
        progress_Signal.emit(100)
    if finish_Signal:
        finish_Signal.emit()
    return


# =========================================================================================
if __name__ == '__main__':
    # Initialize the analysis model
    # print("sys.argv=", sys.argv[0])
    try:
        Run(1, sys.argv[1])
    except:
        Run(1)
# =========================================================================================
# END OF PROGRAM
# =========================================================================================