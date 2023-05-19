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
# ===========================================================================
# Import standard libraries
import numpy as np
#import math
import timeit, sys, logging, os, codecs
# Import internal functions
# =========================================================================================


class UTF8LoggingFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encoding = 'utf-8'

    def format(self, record):
        # Encode the log message using the specified encoding
        record.msg = record.msg.encode(self.encoding, 'replace').decode(self.encoding)
        return super().format(record)


class PrintLog:
    #StartTime = 0.0
    #
    # Logger_SP = None
    # Logger_YS = None


    def Initialize(self, FileName, ModelName):
        # print("Check FileName", FileName)
        # print("Check ModelName111", ModelName)
        #
        # if os.path.exists(FileName + '.rst' + "/" + ModelName + ".log"):
        #     os.remove(FileName + '.rst' + "/" + ModelName + ".log")
        #

        # set up logging
        # self.Logger_SP = logging.getLogger('Logger_SP')
        # self.Logger_YS = logging.getLogger('Logger_YS')
        # self.Logger_SP.setLevel(logging.INFO)
        # self.Logger_YS.setLevel(logging.INFO)
        # fh1 = logging.FileHandler(FileName + '.rst' + "/" + ModelName + ".log")
        # fh2 = logging.FileHandler(FileName + '.rst' + "/" + ModelName + "-YS" + ".log")
        # self.Logger_SP.addHandler(fh1)
        # self.Logger_YS.addHandler(fh2)
        # formatter1 = logging.Formatter("%(message)s")
        # formatter2 = logging.Formatter("%(message)s")
        # fh1.setFormatter(formatter1)
        # fh2.setFormatter(formatter2)
        ##
        # logging.basicConfig(
        #     level=logging.INFO,  # set log level to INFO
        #     format='%(message)s',  # set output format
        #     handlers=[
        #         logging.FileHandler(os.path.join('logs', 'example.log'), mode='a', encoding='utf-8'),  # set log file name and path, and append permission
        #         logging.StreamHandler()  # specify output to console
        #     ]
        # )
        # logger = logging.getLogger(__name__)
        # if analType == 1:  ## 1 for Sectional properties
        # Logfile = FileName + '.rst' + "/" + ModelName + ".log"
        Logfile = FileName + '.rst' + os.sep + ModelName + ".log"
        # logging.basicConfig(filename=Logfile,filemode="w",format="[%(asctime)s]:\t%(message)s",datefmt="%H:%M:%S",level=logging.INFO)
        # print("Check filename222", Logfile)

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(UTF8LoggingFormatter('%(levelname)s: %(message)s'))
        logging.getLogger().addHandler(handler)

        logging.basicConfig(filename=Logfile, encoding='utf-8', filemode="w", format="%(message)s", level=logging.INFO)
        # elif analType == 2:  ## 2 for Sectional Yield Surface
        #     Logfile = FileName + '.rst' + "/" + ModelName + "-YS" + ".log"
        #     # logging.basicConfig(filename=Logfile,filemode="w",format="[%(asctime)s]:\t%(message)s",datefmt="%H:%M:%S",level=logging.INFO)
        #     print("Check filename222", Logfile)
        #     logging.basicConfig(filename=Logfile, filemode="w", format="%(message)s", level=logging.INFO)
        self.StartTime = timeit.default_timer()
        return
    #
    def StartMessage(self, tName, tAuthors, tRevisedDate):
        # tOutput = "   " + '\n'
        tOutput = "********************************************************************************" + '\r\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MSASECT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        tOutput += "   " + '\r\n'
        tOutput += "Programe Name: " + tName + '\r\n'
        tOutput += "Authors: " + tAuthors + '\r\n'
        tOutput += "Last Revised: " + tRevisedDate + '\r\n'
        tOutput += "Note: PyCMSect - Cross Section Properties Calculation Program Based on CM Method"
        return tOutput


    def SectProps(self, Model):
        tOutput = '\u03b8,{:.8e}\n'.format(np.rad2deg(Model.SectProperty.phi))
        tOutput += 'A,{:.8e}\n'.format(Model.SectProperty.Area)
        tOutput += 'Ygc,{:.8e}\n'.format(Model.SectProperty.ygc)
        tOutput += 'Zgc,{:.8e}\n'.format(Model.SectProperty.zgc)
        tOutput += 'Ysc,{:.8e}\n'.format(Model.SectProperty.ysc)
        tOutput += 'Zsc,{:.8e}\n'.format(Model.SectProperty.zsc)
        tOutput += 'Vsc,{:.8e}\n'.format(Model.SectProperty.vsc)
        tOutput += 'Wsc,{:.8e}\n'.format(Model.SectProperty.wsc)
        tOutput += 'J,{:.8e}\n'.format(Model.SectProperty.J)
        tOutput += 'I\u03c9,{:.8e}\n'.format(Model.SectProperty.Cw)
        tOutput += 'Iyy,{:.8e}\n'.format(Model.SectProperty.Iyy)
        tOutput += 'Izz,{:.8e}\n'.format(Model.SectProperty.Izz)
        tOutput += 'Iyz,{:.8e}\n'.format(Model.SectProperty.Iyz)
        tOutput += 'Qy,{:.8e}\n'.format(Model.SectProperty.Qv)
        tOutput += 'Qz,{:.8e}\n'.format(Model.SectProperty.Qw)
        tOutput += '\u03b2y,{:.8e}\n'.format(Model.SectProperty.Betay)
        tOutput += '\u03b2z,{:.8e}\n'.format(Model.SectProperty.Betaz)
        tOutput += '\u03b2\u03c9,{:.8e}\n'.format(Model.SectProperty.Betaω)
        tOutput += 'Zyy,{:.8e}\n'.format(Model.SectProperty.Zyy)
        tOutput += 'Zzz,{:.8e}\n'.format(Model.SectProperty.Zzz)
        tOutput += 'ry,{:.8e}\n'.format(Model.SectProperty.ry)
        tOutput += 'rz,{:.8e}\n'.format(Model.SectProperty.rz)
        tOutput += 'Ivv,{:.8e}\n'.format(Model.SectProperty.Ivv)
        tOutput += 'Iww,{:.8e}\n'.format(Model.SectProperty.Iww)
        tOutput += 'Qv,{:.8e}\n'.format(Model.SectProperty.Qv)
        tOutput += 'Qw,{:.8e}\n'.format(Model.SectProperty.Qw)
        tOutput += '\u03b2v,{:.8e}\n'.format(Model.SectProperty.Betav)
        tOutput += '\u03b2w,{:.8e}\n'.format(Model.SectProperty.Betaw)
        tOutput += 'Zvv,{:.8e}\n'.format(Model.SectProperty.Zvv)
        tOutput += 'Zww,{:.8e}\n'.format(Model.SectProperty.Zww)
        tOutput += 'rv,{:.8e}\n'.format(Model.SectProperty.rv)
        tOutput += 'rw,{:.8e}\n'.format(Model.SectProperty.rw)
        return tOutput

    #
    def OutputSectProps(self, Model, tName, tAuthors, tRevisedDate):
        ResultFolder = Model.OutResult.FileName + '.rst'
        fileName = ResultFolder + '\\' + Model.OutResult.ModelName + '-Section properties.txt'
        f = codecs.open(fileName, 'w', 'utf-8')
        tOutput = self.SectProps(Model)
        f.write(tOutput)
        f.close()
        return


    # def OutputYieldSurfaceInfo(self,Model,tName, tAuthors, tRevisedDate):
    #     ResultFolder = Model.OutResult.FileName + '.rst'
    #     fileName = ResultFolder + '\\' + Model.OutResult.ModelName + '-Section properties.txt'
    #     f = codecs.open(fileName, 'w', 'utf-8')
    #     tOutput = '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ' + '\n'
    #     tOutput += '&&&&&&&&&&&&&&&&&&&&&&&&&& Cross-Sectional' + ' Properties &&&&&&&&&&&&&&&&&&&&&&&&&& ' + '\n'
    #     # f.write(title)
    #     # f.close()
    #     # f = codecs.open(fileName, 'w', 'utf-8')
    #     tOutput += self.StartMessage(tName, tAuthors, tRevisedDate) + '\n'
    #     f.write(tOutput)
    #     f.close()
    #     return

    # def OutputSectYSAnalInfo(self, Model, tName, tAuthors, tRevisedDate):



    def PrintModelInfo(self, Model):
        tOutput = "\t\t" + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODEL INFORMATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        tOutput += "* DESCRIPTION" + '\r\n'
        tOutput += "\t" + Model.Information.Description + '\r\n'
        tOutput += "* SUMMARY" + '\r\n'
        tOutput += "\t" + "NUM. OF POINTS........................................ = " + str(Model.Point.Count) + '\r\n'
        tOutput += "\t" + "NUM. OF SEGMENTS...................................... = " + str(Model.Segment.Count) + '\r\n'

        tOutput += "\t\t" + '\r\n'
        tOutput += "* POINT'S COORDINATES IN GLOBAL AXIS   " + '\r\n'
        # tOutput += "\t" + "ID." + "\t\t\t" + "Y-COOR." + "\t\t\t" + "Z-COOR." + '\r\n'
        tOutput += "\t{:<14}{:<24}{:<24}\r\n".format("ID.", "Y-COOR.", "Z-COOR.")
        for jj in Model.Point.ID:
            tOutput += "\t{:<14}{:<24}{:<24}\r\n".format(int(jj), format(Model.Point.Yo[jj], "0.4e"), format(Model.Point.Zo[jj], "0.4e"))
            # tOutput += "\t" + str(int(jj)) + "\t\t" + str(format(Model.Point.Yo[jj], "0.4e")) \
            #         + "\t\t" + str(format(Model.Point.Zo[jj], "0.4e")) + '\r\n'

        tOutput += "\t\t" + '\n'
        tOutput += "* SEGMENT CONNECTIVITY" + '\r\n'
        # tOutput += "\t" + "ID." + "\t\t" + "POINT I" + "\t\t" + "POINT J" + "\t\t" + "THICKNESS" + '\r\n'
        tOutput += "\t{:<14}{:<18}{:<18}{:<18}\r\n".format("ID.", "POINT I", "POINT J", "THICKNESS")
        for ii in Model.Segment.ID:
            # tOutput += "\t" + str(int(ii)) + "\t\t" + str(int(Model.Segment.PointI[ii])) + "\t\t\t" \
            #            + str(int(Model.Segment.PointJ[ii])) + "\t\t\t" + str(Model.Segment.SegThick[ii]) + '\r\n'
            tOutput += "\t{:<14}{:<18}{:<18}{:<18}\r\n".format(int(ii), int(Model.Segment.PointI[ii]), int(Model.Segment.PointJ[ii]),
                                                              Model.Segment.SegThick[ii])

        return tOutput

    def PrintSectProInfo(self, Model):
        ## Print Section Properties
        #tOutput = "\t\t" + '\n'
        tOutput = "********************************************************************************" + '\r\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SECTION PROPERTIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        tOutput += '*** PROPERTIES ***'.ljust(50) + '*** VALUES ***'.rjust(30) + '\r\n'
        # tOutput += "Cross-Section Area, A " + " .................................................... = "\
        #           + str(format(Model.SectProperty.Area, "0.4e")) + '\n'
        #tOutput += 'Cross-Section Area, A'.ljust(50, '.') + '{:.8e}'.format(Model.SectProperty.Area).rjust(30, '.') + '\n'
        tOutput += 'Cross-Section Area, A'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Area)).rjust(30,'.') + '\r\n'
        tOutput += 'Centroid, Ygc'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.ygc)).rjust(30,'.') + '\r\n'
        tOutput += 'Centroid, Zgc'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.zgc)).rjust(30,'.') + '\r\n'
        tOutput += 'Static Moment, Qy'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Qv)).rjust(30,'.') + '\r\n'
        tOutput += 'Static Moment, Qz'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Qw)).rjust(30,'.') + '\r\n'
        tOutput += 'Static Moment, Qv'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Qv)).rjust(30,'.') + '\r\n'
        tOutput += 'Static Moment, Qw'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Qw)).rjust(30,'.') + '\r\n'
        tOutput += 'Moment of Inertia, Iyy'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Iyy)).rjust(30,'.') + '\r\n'
        tOutput += 'Moment of Inertia, Izz'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Izz)).rjust(30,'.') + '\r\n'
        tOutput += 'Moment of Inertia, Iyz'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Iyz)).rjust(30,'.') + '\r\n'
        tOutput += 'Moment of Inertia, Ivv'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Ivv)).rjust(30,'.') + '\r\n'
        tOutput += 'Moment of Inertia, Iww'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Iww)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Centre, Ysc'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.ysc)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Centre, Zsc'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.zsc)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Centre, Vsc'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.vsc)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Centre, Wsc'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.wsc)).rjust(30,'.') + '\r\n'
        tOutput += 'Torsion Constant, J'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.J)).rjust(30,'.') + '\r\n'
        tOutput += 'Warping Constant, Iomg'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Cw)).rjust(30,'.') + '\r\n'
        tOutput += 'Wagner Coefficient, Betay'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Betay)).rjust(30,'.') + '\r\n'
        tOutput += 'Wagner Coefficient, Betaz'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Betaz)).rjust(30,'.') + '\r\n'
        tOutput += 'Wagner Coefficient, Betav'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Betav)).rjust(30,'.') + '\r\n'
        tOutput += 'Wagner Coefficient, Betaw'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Betaw)).rjust(30,'.') + '\r\n'
        tOutput += 'Wagner Coefficient, Betaomg'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Betaω)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Area, Ayy'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Ayy)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Area, Azz'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Azz)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Area, Avv'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Avv)).rjust(30,'.') + '\r\n'
        tOutput += 'Shear Area, Aww'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Aww)).rjust(30,'.') + '\r\n'
        tOutput += 'Plastic Section Module, Zyy'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Zyy)).rjust(30,'.') + '\r\n'
        tOutput += 'Plastic Section Module, Zzz'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Zzz)).rjust(30,'.') + '\r\n'
        tOutput += 'Plastic Section Module, Zvv'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Zvv)).rjust(30,'.') + '\r\n'
        tOutput += 'Plastic Section Module, Zww'.ljust(50,'.') + str('= '+'{:.8e}'.format(Model.SectProperty.Zww)).rjust(30,'.') + '\r\n'
        return tOutput

    # @classmethod
    def Print(self, message):
        print(message)
        logging.info(message)

    def ShowRuntime(self, StartTime):
        tOutPut1 = self.GetRunTime(StartTime)
        tOutPut2 = self.EndMessage()
        tOutPut = tOutPut1 + tOutPut2
        return tOutPut

    def GetRunTime(self, StartTime):
        Time = timeit.default_timer() - StartTime
        Time = format(Time, "0.2f")
        tOutput = "********************************************************************************" + '\r\n'
        tOutput += "Run time = " + str(Time) + " s" + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        return tOutput

    def EndMessage(self):
        tOutput = "   " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        tOutput += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + '\r\n'
        tOutput += "********************************************************************************" + '\r\n'
        return tOutput
