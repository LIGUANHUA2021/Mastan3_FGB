from PySide6.QtCore import QThread, QFileInfo
import os
##
from gui.msasect.base.Model import msaModel
##
from analysis.CMSect import Main
from analysis.FESect import Main as FEMain
from analysis.FESect.variables import Model as FEModel
from analysis.RCD import Main as RCDMain
from analysis.GlobalBuckling import Main as GBMain
from gui.msasect.ui.CalGlobalBuckling_Element import MultiThread as GBCal

class MultiThread(QThread):
    """
    QThread class
    """

    # MeshProgressUpdate_Signal = Signal(int)
    def __init__(self, label=None, parameter=None):
        QThread.__init__(self)
        self.label = label
        self.parameter = parameter

    def MeshGenFE_Thread(self):
        FEMesh_Instance = self.parameter["FEMesh"]
        FEMesh_Instance.MeshGenFE(self.parameter["msaFEModel"], self.parameter["meshSize"])

    def SectPropCal_Thread(self):
        FEModel.OutResult.ReadOutResult(self.parameter["msaFEModel"].FileInfo.FileName,
                                        os.path.dirname(self.parameter["msaFEModel"].Information.ModelName))
        FEMain = self.parameter["FEMain"]
        FEMain.Run(1, self.parameter["progress_Signal"], self.parameter["finish_Signal"], self.parameter["mat_ref"])

    def CalYSurface_Thread(self):
        tAnaFileName = self.parameter["AnaFileName"] #msaModel.Information.ModelName
        mw = self.parameter["mw"]
        tFlag = self.parameter["Flag"]
        # ##
        # mw.Run_pushButton.setStyleSheet("background-color: red")
        # mw.Run_pushButton.setText("Stop")
        #
        if tFlag == 1:
            Main.Run(2, tAnaFileName, self.parameter["progress_Signal"], self.parameter["finish_Signal"])
        elif tFlag == 2:
            FEMain.Run(2, self.parameter["progress_Signal"], self.parameter["finish_Signal"])
        #mw.Stop_pushButton.setStyleSheet("background-color: white")
        # mw.Notes_label.setStyleSheet('color: yellow;')
        # mw.Notes_label.setText("The analysis has been completed. Please click on the 'Show Results' button.")
        #mw.Cancel_pushButton.setEnabled(True)
        #mw.ShowResults_pushButton.setEnabled(True)
        #mw.Cancel_pushButton.setText("Cancel")
        #mw.Cancel_pushButton.setStyleSheet("QPushButton::hover{background-color:rgb(144, 200, 246)}\n"
                                        #"QPushButton{    \n"
                                        #"    font: 9pt \"Segoe UI\";\n"
                                        #"    color: rgb(0, 0, 0);\n"
                                        #"    background: rgb(255, 255, 255);\n""}")
        mw.NewThread.quit()
        #mw.YS_textBrowser.append("The analysis has been completed. Please click on the 'Show Results' button.")
        # mw.Stop_pushButton.setStyleSheet("background-color: red")
        # mw.OK_pushButton.setEnabled(True)

    def CalMomCurvature_Thread(self):
        tAnaFileName = self.parameter["AnaFileName"] #msaModel.Information.ModelName
        mw = self.parameter["mw"]
        tempAnaFileName = QFileInfo(tAnaFileName)
        RCDMain.Run(1, tempAnaFileName.path() + os.sep + tempAnaFileName.baseName() + '.Json.rst' + os.sep + tempAnaFileName.baseName() + "-RCDOnly.Json", self.parameter["progress_Signal"], self.parameter["finish_Signal"])
        mw.NewThread.quit()

    def CalGlobalBuckling_Thread(self):
        tAnaFileName = self.parameter["AnaFileName"]  # msaModel.Information.ModelName
        mw = self.parameter["mw"]
        tFlag = self.parameter["Flag"]
        if tFlag == 1:
            GBMain.Run(1, tAnaFileName, self.parameter["progress_Signal"], self.parameter["finish_Signal"])
        elif tFlag == 2:
            GBCal.CalGlobalBuckling(GBCal.Parameters.E, GBCal.Parameters.mu, GBCal.Parameters.Fy, GBCal.Parameters.Area, GBCal.Parameters.MomentofInertia_v,
                                    GBCal.Parameters.MomentofInertia_w, GBCal.Parameters.TorsionConstant, GBCal.Parameters.WarpingConstant,
                                    GBCal.Parameters.ShearCentre_v, GBCal.Parameters.ShearCentre_w, GBCal.Parameters.ky, GBCal.Parameters.kz, GBCal.Parameters.WagnerCoefficient_v,
                                    GBCal.Parameters.WagnerCoefficient_w, GBCal.Parameters.WagnerCoefficient_ww, GBCal.Parameters.L, GBCal.Parameters.Px, GBCal.Parameters.Mx,
                                    GBCal.Parameters.My, GBCal.Parameters.Mz, GBCal.Parameters.Nodes_number, GBCal.Parameters.Lamuda,
                                    self.parameter["progress_Signal"], self.parameter["finish_Signal"])
        mw.NewThread.quit()

    def CalCompSectModu_Thread(self):
        tAnaFileName = self.parameter["AnaFileName"] #msaModel.Information.ModelName
        mw = self.parameter["mw"]
        tempAnaFileName = QFileInfo(tAnaFileName)
        RCDMain.Run(999, tempAnaFileName.path() + os.sep + tempAnaFileName.baseName() + '.Json.rst' + os.sep + tempAnaFileName.baseName() + "-RCDOnly.Json", self.parameter["progress_Signal"], self.parameter["finish_Signal"])
        mw.NewThread.quit()

    def run(self):
        if self.label == "Mesh":
            self.MeshGenFE_Thread()
        elif self.label == "CalSP":
            self.SectPropCal_Thread()
        elif self.label == "CalYS":
            self.CalYSurface_Thread()
        elif self.label == "CalMC":
            self.CalMomCurvature_Thread()
        elif self.label == "CalGB":
            self.CalGlobalBuckling_Thread()
        elif self.label == "CalCompSectModu":
            self.CalCompSectModu_Thread()
