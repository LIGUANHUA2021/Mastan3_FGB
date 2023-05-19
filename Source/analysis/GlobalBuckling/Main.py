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
import timeit
# =========================================================================================
# Import internal functions
from analysis.GlobalBuckling.variables import Model
from analysis.GlobalBuckling.solver.GlobalBucklingCal import CalFlexuralBuckling, CalAxialtorsionalBuckling, CalLateraltorsionalBuckling
from analysis.GlobalBuckling.variables.Model import Material, SecProperties, Analysis
from analysis.GlobalBuckling.util.Printlog import PrintLog as pl
from analysis.GlobalBuckling.file import ReadData
from analysis.GlobalBuckling.file import OutputResults
import sys
# =========================================================================================
ProgrameName = " PyFESect - Python-based Cross-platforms Section Analysis Software (v1.0.0) "
DeveloperName = " Copyright © 2023 Siwei Liu, All Right Reserved."
RevisedDate = " Last Revised: March 31, 2023 "
# =========================================================================================

def Run(analType, argv='',progress_Signal=None, finish_Signal=None):
    # ----------------------------------------------------------------
    # Initializing
    # ----------------------------------------------------------------
    # Model.initialize()
    # ReadData.ModelFromJSON(FileName=argv)
    # pl().Initialize(Model.OutResult.FileName, Model.OutResult.ModelName)
    StartTime = timeit.default_timer()
    pl.Print(pl.StartMessage(ProgrameName, DeveloperName, RevisedDate))
    pl.Print(pl().PrintModelInfo(Model))
    Lamuda1, Pfb = CalFlexuralBuckling()
    Lamuda2, Patb = CalAxialtorsionalBuckling()
    Lamuda3, Pltb = CalLateraltorsionalBuckling()
    pl.Print(OutputResults.AddResult_msa())
    # pl.Print(OutputResults.Output(Lamuda1, Pfb, Patb, Pltb))
    pl.Print(OutputResults.Output_msa(Lamuda1))
    pl.Print(pl.getRunTime(StartTime))
    pl.Print(OutputResults.EndMessage())
    # ----------------------------------------------------------------
    # Analysis is completed
    # ----------------------------------------------------------------
    if progress_Signal:
        progress_Signal.emit(100)
    if progress_Signal:
        finish_Signal.emit()
    return
# =========================================================================================
# END OF PROGRAM
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
