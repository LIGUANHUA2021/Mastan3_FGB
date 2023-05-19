#############################################################################
# MSAShell - Finite element analysis with shell element model (v0.0.1)

# Project Leaders :
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2023 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix
# Import internal functions
from analysis.shell.variables import Model, Results
from analysis.shell.file import OutputResults
from analysis.shell.element import NLThinTriShell
from analysis.shell.util import Assembly
from analysis.shell.util import FormMtxg
from analysis.shell.util.PrintLog import PrintLog as pl

def run():
    pl.Print("Start 1st-order elastic analysis ...")
    # Preparation
    AppliedF = Model.Analysis.TargetLF * Model.Node.Fg
    OutputResults.IniResults()
    # initialize KG
    KL0 = coo_matrix((Model.Node.Count * 6, Model.Node.Count * 6), dtype=np.float64).todense()
    tMtrType = "linear"
    U0 = np.zeros(Model.Node.Count * 6)
    KL = FormMtxg.FormKg(Model.Material, Model.Section, Model.Node, Model.Element, NLThinTriShell, KL0, tMtrType, U0)
    # ---------------------------------------------------------------------------
    # Apply boundary condition
    KLb = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, KL)
    # ---------------------------------------------------------------------------
    # Newton-Raphson method
    U = np.linalg.solve(KLb, AppliedF.transpose())
    # ---------------------------------------------------------------------------
    # Post-processing
    Rg = Results.CyCRes.GetResF_g(Model.Node, U, KL)
    # Get Node Reactions
    Results.CyCRes.GetNodeReactForce(Model.Boundary, Model.Node, Rg)
    # Get Element Stress and Element Principal Stress
    Results.CyCRes.GetElementStress(Model.Material, Model.Section, Model.Node, Model.Element, U)
    # ---------------------------------------------------------------------------
    # Record Results
    Results.CyCRes.LF = Model.Analysis.TargetLF
    Results.CyCRes.CurU = U
    # ---------------------------------------------------------------------------
    # Output Results
    OutputResults.OutCyCRes(Results)
    # ---------------------------------------------------------------------------
    return