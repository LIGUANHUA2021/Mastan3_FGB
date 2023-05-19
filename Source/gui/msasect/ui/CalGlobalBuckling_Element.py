import numpy as np
from analysis.frame.file import ReadData
from analysis.frame.variables import Model as FrameModel
from analysis.frame.solver import Eigenbuckling
from gui.msasect.base import Model as msaModel
import timeit

class MultiThread:

    class Parameters:
        E = 0
        mu = 0
        Fy = 0
        Area = 0
        MomentofInertia_v = 0
        MomentofInertia_w = 0
        TorsionConstant = 0
        WarpingConstant = 0
        ShearCentre_v = 0
        ShearCentre_w = 0
        ky = 0
        kz = 0
        WagnerCoefficient_v = 0
        WagnerCoefficient_w = 0
        WagnerCoefficient_ww = 0
        L = []
        Px = 0
        Mx = 0
        My = 0
        Mz = 0
        Nodes_number = 0
        Lamuda = []

    @classmethod
    def Reset(cls):
        MultiThread.Parameters.E = 0
        MultiThread.Parameters.mu = 0
        MultiThread.Parameters.Fy = 0
        MultiThread.Parameters.Area = 0
        MultiThread.Parameters.MomentofInertia_v = 0
        MultiThread.Parameters.MomentofInertia_w = 0
        MultiThread.Parameters.TorsionConstant = 0
        MultiThread.Parameters.WarpingConstant = 0
        MultiThread.Parameters.ShearCentre_v = 0
        MultiThread.Parameters.ShearCentre_w = 0
        MultiThread.Parameters.ky = 0
        MultiThread.Parameters.kz = 0
        MultiThread.Parameters.WagnerCoefficient_v = 0
        MultiThread.Parameters.WagnerCoefficient_w = 0
        MultiThread.Parameters.WagnerCoefficient_ww = 0
        MultiThread.Parameters.L = []
        MultiThread.Parameters.Px = 0
        MultiThread.Parameters.Mx = 0
        MultiThread.Parameters.My = 0
        MultiThread.Parameters.Mz = 0
        MultiThread.Parameters.Nodes_number = 0
        MultiThread.Parameters.Lamuda = []

    @staticmethod
    def CalGlobalBuckling(E, mu, Fy, Area, MomentofInertia_v, MomentofInertia_w,
                          TorsionConstant, WarpingConstant, ShearCentre_v, ShearCentre_w,
                          ky, kz, WagnerCoefficient_v, WagnerCoefficient_w, WagnerCoefficient_ww,
                          L, Px, Mx, My, Mz, Nodes_number, Lamuda,progress_Signal=None, finish_Signal=None):
        StartTime = timeit.default_timer()
        if ky == 0:
            ky = 0.01
        if kz == 0:
            kz = 0.01
        Buckling_data = {}
        Buckling_data["INFORMATION"] = [
            [ "Version", "3.0.0"],
            [ "Date", "20230412"],
            [ "Description", "This example is provided for testing Eigen buckling analysis in MASTAN3.0.0"]
          ]
        Buckling_data["MATERIAL"] = [
            [ 1, float(E), float(E/(2*(1+mu))), float(Fy) , 0 ]
          ]
        Buckling_data["SECTION"] = [
            [1, 1, 2, float(Area), float(MomentofInertia_v), float(MomentofInertia_w), float(TorsionConstant),
             float(WarpingConstant), float(ShearCentre_v), float(ShearCentre_w), ky, kz, float(WagnerCoefficient_v),
             float(WagnerCoefficient_w), float(WagnerCoefficient_ww)]
        ]
        Buckling_data["RELEASE"] = []
        Buckling_data["BOUNDARY"] = [
            [1, 0, 1, 1, 0, 0, 0],
            [Nodes_number, 1, 1, 1, 1, 0, 0]
        ]
        Buckling_data["JOINTLOAD"] = [
            [1, float(Px), 0, 0, float(Mx), float(My), float(Mz), 0, 0],
            [Nodes_number, 0, 0, 0, 0, -float(My), -float(Mz), 0, 0]
        ]
        Buckling_data["ANALYSIS"] = [
            ["Type", "eigenBuckling"],
            ["Modes Number", 1]
        ]
        Factors1 = []
        Factors2 = []
        Factors3 = []
        print(">>> Global Buckling Analysis considering twisting effects is running ...")
        for ii in range(len(L)):
            Load_factor = []
            print(">>> Global Buckling Step = %s, Current λ = %s, Convergence = Ture, Calculation Successful"  % (ii + 1, '{:.2f}'.format(Lamuda[ii])))
            x_L= np.linspace(0, L[ii], Nodes_number)
            Buckling_data["NODE"] = []
            Buckling_data["MEMBER"] = []
            for m in range(len(x_L)):
                Buckling_data["NODE"].append([m + 1, x_L[m], 0, 0])
            for n in range(len(x_L) - 1):
                Buckling_data["MEMBER"].append([1 + n, 1, 1 + n, 2 + n, 0])
            # print(Buckling_data)
            ReadData.LoadDataToModel(Buckling_data)
            FrameModel.initialize()
            Load_factor = Eigenbuckling.run()
            Factors1.append(Load_factor[0])
        Buckling_data["SECTION"] = [
            [1, 1, 2, float(Area), float(MomentofInertia_v), float(MomentofInertia_w), float(TorsionConstant),
             float(WarpingConstant), 0, 0, ky, kz, 0, 0, 0]]
        print(" ")
        print(">>> Global Buckling Analysis ignoring twisting effects is running ...")
        for ii in range(len(L)):
            Load_factor2 = []
            print(">>> Global Buckling Step = %s, Current λ = %s, Convergence = Ture, Calculation Successful"  % (ii + 1, '{:.2f}'.format(Lamuda[ii])))
            x_L= np.linspace(0, L[ii], Nodes_number)
            Buckling_data["NODE"] = []
            Buckling_data["MEMBER"] = []
            for m in range(len(x_L)):
                Buckling_data["NODE"].append([m + 1, x_L[m], 0, 0])
            for n in range(len(x_L) - 1):
                Buckling_data["MEMBER"].append([1 + n, 1, 1 + n, 2 + n, 0])
            # print(Buckling_data)
            ReadData.LoadDataToModel(Buckling_data)
            FrameModel.initialize()
            Load_factor2 = Eigenbuckling.run()
            Factors2.append(Load_factor2[0])
        Buckling_data = {}
        Buckling_data['Lamuda'] = Lamuda
        Buckling_data['Factors1'] = Factors1
        Buckling_data['Factors2'] = Factors2
        # Buckling_data['Factors3'] = Factors3
        Buckling_data['method'] = 'Line_element'
        msaModel.GlobalBuckling.Buckling_data = Buckling_data
        Time = timeit.default_timer() - StartTime
        Time = format(Time, "0.5f")
        tOutput = "" + '\n'
        tOutput += "Global buckling analysis using line element is finished!" + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "Run time = " + str(Time) + " s" + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "" + '\n'
        tOutput += "********************************************************************************" + '\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\n'
        tOutput += "********************************************************************************" + '\n'

        print(tOutput)
        if progress_Signal:
            progress_Signal.emit(100)
        if progress_Signal:
            finish_Signal.emit()
        return