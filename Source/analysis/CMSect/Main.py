###########################################################################################
#
# PyCMSect - Python-based Cross-platforms Section Analysis Software for Thin-walled Sections
#
# Developed by:
#   Siwei Liu        -   The Hong Kong Polytechnic University
#
# Contributed by:
#   Wenlong Gao, Liang Chen
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
from analysis.CMSect.variables import Model
from analysis.CMSect.file import ReadData, VersionControl
from analysis.CMSect.solver import CalSectionProperties
from analysis.CMSect.solver import CalYieldSurface
from analysis.CMSect.util.PrintLog import PrintLog as pl
# =========================================================================================
ProgrameName = " MSASECT - Python-based Cross-platforms Section Analysis Software (v1.0.0) "
DeveloperName = " Copyright © 2022 Siwei Liu, All Right Reserved."
RevisedDate = " Last Revised: May 5, 2023 "
# =========================================================================================
# =========================================================================================
def Run(analType, argv='', progress_Signal=None, finish_Signal=None):
    # ----------------------------------------------------------------
    # Initializing
    # ----------------------------------------------------------------
    ReadData.modelfromJSON(FileName=argv)
    # Model.initialize()
    pl().Initialize(Model.OutResult.FileName, Model.OutResult.ModelName)
    # plogger = pl(Model.OutResult.FileName, Model.OutResult.ModelName)
    # logging Logo
    # pl().Print(pl().StartMessage(ProgrameName, DeveloperName, RevisedDate))
    pl().Print(pl().PrintModelInfo(Model))
    # if argv =="":
    StartTime = timeit.default_timer()
    # ---------------------------------------------------------------------------------
    ##################################### Main function ###############################
    ###################################################################################
    if analType == 1: ## 1 for Sectional properties
        CalSectionProperties.CalSectProps(Model)
        # ---------------------------------------------------------------------------------
        pl().Print(pl().PrintSectProInfo(Model))
        pl().OutputSectProps(Model, ProgrameName, DeveloperName, RevisedDate)
        pl().Print(pl().ShowRuntime(StartTime))
    elif analType == 2: ## 2 for Sectional Yield Surface
        CalYieldSurface.CalYieldS().Run()
        pl().Print(pl().GetRunTime(StartTime))

    # ----------------------------------------------------------------
    # Analysis is completed
    # ----------------------------------------------------------------
    if progress_Signal:
        progress_Signal.emit(100)
    if progress_Signal:
        finish_Signal.emit()
    return


# =========================================================================================
if __name__ == '__main__':
    # Initialize the analysis model
    try:
        Run(1, sys.argv[1])
    except:
        Run(1, argv='')
# =========================================================================================
# END OF PROGRAM
# =========================================================================================