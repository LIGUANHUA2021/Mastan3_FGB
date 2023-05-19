###########################################################################################
# MASTAN3 - Python-based Cross-platforms Frame Analysis Software
#
# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
###########################################################################################
# Description:
# =========================================================================================
# Import standard libraries
import timeit, sys, logging, os
# =========================================================================================
# Import internal functions
from analysis.frame.variables import Model
#from analysis.frame.util import Message, Runtime, Logger
from analysis.frame.util.PrintLog import PrintLog as pl
from analysis.frame.file import ReadData
from analysis.frame.solver import StaticLinear, StaticNonlinear, Eigenbuckling, ModalAnalysis ,DynamicNonlinear
# =========================================================================================
ProgrameName = " Mastan3 - Frame Analysis Module(v1.0.0) "
DeveloperName = " Developed by Mastan Team"
RevisedDate = " Last Revised: Apr. 01, 2022 "
# =========================================================================================
def Run(argv=''):
    # ----------------------------------------------------------------
    # Initializing
    # ----------------------------------------------------------------
    ReadData.modelfromJSON(FileName=argv)
    Model.initialize()
    pl().Initialize(Model.OutResult.FileName, Model.OutResult.ModelName)
    # logging Logo
    pl.Print(pl.StartMessage(ProgrameName, DeveloperName, RevisedDate))
    pl.Print(pl().PrintModelInfo(Model))
    #if argv =="":
    # Start Timer
    StartTime = timeit.default_timer()
    # ----------------------------------------------------------------
    # Run Analysis
    # Solver(model).run()
    if Model.Analysis.Type == "staticLinear":
        StaticLinear.run()
    elif Model.Analysis.Type == "staticNonlinear":
        StaticNonlinear.run()
    elif Model.Analysis.Type == "eigenBuckling":
        Eigenbuckling.run()
    elif Model.Analysis.Type == "modalAnalysis":
        ModalAnalysis.run()
    elif Model.Analysis.Type == "dynamicNonlinear":
        DynamicNonlinear.run()

    #print(Runtime.getRunTime(StartTime))
    # pl.Print(Message.EndMessage())
    pl.Print(pl().ShowRuntime(StartTime))
    # ----------------------------------------------------------------
    # Analysis is completed
    # ----------------------------------------------------------------
    return


# =========================================================================================
if __name__ == '__main__':
    # Initialize the analysis model
    try:
        Run(sys.argv[1])
    except:
        Run()
# =========================================================================================
# END OF PROGRAM
# =========================================================================================