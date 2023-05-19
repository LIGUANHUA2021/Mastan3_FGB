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
import timeit
# =========================================================================================
# Import internal functions
from PySide6.QtCore import QObject, Signal
from analysis.FESect.file import ReadData
from analysis.FESect.util import PrintLog as pl
from analysis.FESect.variables.Model import OutResult
from analysis.FESect.variables import Model
from analysis.FESect.solver import BasicProperties, CalYieldSurface, BucklingAnalysis, DynamicAnalysis, HeatTransfer, MomentCurvature, StressAnalysis, YieldSurface
# =========================================================================================
ProgrameName = " PyFESect - Python-based Cross-platforms Section Analysis Software (v1.0.0) "
DeveloperName = " Copyright © 2022 Siwei Liu, All Right Reserved."
RevisedDate = " Last Revised: July 5, 2022 "
# =========================================================================================

def Run(analType, progress_Signal=None, finish_Signal=None, mat_ref=None):
    # ----------------------------------------------------------------
    # Initializing
    # ----------------------------------------------------------------
    StartTime = timeit.default_timer()
    # pl.Print(pl.MainLog.StartMessage(ProgrameName, DeveloperName, RevisedDate))
    #ReadData.ModelFromJSON(FileName=argv)
    if analType == 1:  ## 1 for Sectional properties
        BasicProperties.Run(progress_Signal, mat_ref)
        # pl.Print(pl.MainLog.EndMessage())
        # pl.Print(pl.MainLog.GetRuntime(StartTime))
    elif analType == 2:  ##
        # pl.Print(pl.MainLog.StartMessage(ProgrameName, DeveloperName, RevisedDate))
        pl.Print(pl.ModelLog.BasicInfo(Model.Material, Model.Point, Model.Outline, Model.Group))
        CalYieldSurface.CalYieldS().Run()
        pl.Print(pl.MainLog.EndMessage())
        pl.Print(pl.MainLog.GetRuntime(StartTime))
    # ----------------------------------------------------------------
    # Analysis is completed
    # ----------------------------------------------------------------
    pl.LogFile.OutputLogFile()
    if progress_Signal:
        progress_Signal.emit(100)
    if finish_Signal:
        finish_Signal.emit()
    return
# =========================================================================================
# END OF PROGRAM
# =========================================================================================
