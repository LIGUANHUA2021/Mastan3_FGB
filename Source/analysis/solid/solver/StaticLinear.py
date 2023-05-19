#############################################################################
# MSASolid - Finite element analysis with solid element model (v0.0.1)

# Project Leaders :
#   R.D. Ziemian    -   Bucknell University, the United States
#   S.W. Liu        -   The Hong Kong Polytechnic University, Hong Kong, China
#
# Copyright © 2022 Siwei Liu, All Right Reserved.
#
#############################################################################
# Function purpose:
# ===========================================================================
# Import standard libraries
import numpy as np
import math
import logging
from scipy import linalg as LA
from scipy.sparse import coo_matrix  # Most efficient storage format for sparse matrix

# Import internal functions
from analysis.solid.variables import Model, Results
from analysis.solid.file import OutputResults
from analysis.solid.element import FourNodeTetrahedron
from analysis.solid.util import Assembly
from analysis.solid.util import FormMtxg
from analysis.solid.util import PrintLog as pl

def run():
    pl.Print("Start 1st-order elastic analysis ...")
    # Preparation
    AppliedF = Model.Analysis.TargetLF * Model.Node.Fg
    OutputResults.IniResults()
    # initialize KG
    KL0 = coo_matrix((Model.Node.Count * 3, Model.Node.Count * 3), dtype=np.float64).todense()
    tMtrType = "linear"
    U0 = np.zeros(Model.Node.Count * 3)
    KL = FormMtxg.FormKg(Model.Material, Model.Node, Model.Element, FourNodeTetrahedron, KL0, tMtrType, U0)
    # ---------------------------------------------------------------------------
    # Apply boundary condition
    KLb = Assembly.ApplyBdyCond(Model.Boundary, Model.Node, KL)
    # ---------------------------------------------------------------------------
    # Newton-Raphson method
    U = np.linalg.solve(KLb, AppliedF)
    # ---------------------------------------------------------------------------
    # Post-processing
    Rg = Results.CyCRes.GetResF_g(Model.Node, U, KL)
    # Get Node Reactions
    Results.CyCRes.GetNodeReactForce(Model.Boundary, Model.Node, Rg)
    # Get Element Stress
    Results.CyCRes.GetElementStress(Model.Material, Model.Node, Model.Element, FourNodeTetrahedron, U)
    # Get Element Principal Stress
    Results.CyCRes.GetElementPStress(Model.Element, FourNodeTetrahedron)
    # ---------------------------------------------------------------------------
    # Record Results
    Results.CyCRes.LF = Model.Analysis.TargetLF
    Results.CyCRes.CurU = U
    # ---------------------------------------------------------------------------
    # Output Results
    OutputResults.OutCyCRes(Results)
    # ---------------------------------------------------------------------------
    return