# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QBrush, QColor, QPixmap, QIcon
from gui.msasect.ui.Ui_MaterialDb import Ui_MaterialDb_Dialog
from gui.msasect.ui.msgBox import showMesbox


class library_Path:
    Path = r"base/library/"


class MaterialDb_Dialog(QDialog, Ui_MaterialDb_Dialog):
    """
    Class documentation goes here.
    """
    OKsignal = Signal(dict)

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.initlize()
        self.Material_tableWidget.clicked.connect(self.load_DimensionsTable)
        self.ComboBox.currentIndexChanged.connect(self.refresh_DimensionsTable)

    @Slot()
    def on_OK_button_clicked(self):
        Num_row = self.Properties_tableWidget.rowCount()
        Sect_Dimensions = {}
        tMatType = ""
        for ii in range(Num_row):
            type = self.Properties_tableWidget.item(ii, 0).text().strip('=')
            value = self.Properties_tableWidget.item(ii, 1).text()
            Sect_Dimensions[type] = float(value)
        Mattype=self.ComboBox.currentIndex()
        if Mattype <=4:
            tMatType = "S"
        elif Mattype == 5 or Mattype ==6 or Mattype ==7:
            tMatType = "C"
        #elif Mattype == 8 or Mattype ==9 or Mattype ==10 or Mattype ==11 or Mattype ==12 or Mattype ==13:
            #tMatType = "R"
        elif Mattype == 8:
            tMatType = "A"
        Sect_Dimensions["tMatType"] = tMatType
        self.OKsignal.emit(Sect_Dimensions)
        QDialog.close(self)

    @Slot()
    def on_Cancel_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QDialog.close(self)
    # @Slot()
    # def on_Import_pushButton_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     # raise NotImplementedError

    def initlize(self):
        MatType = self.ComboBox.currentText()
        FileName = library_Path.Path + MatType + ".dat"
        Section_list = self.read_Database(FileName)
        self.load_PropertiesTable(Section_list)

    def refresh_DimensionsTable(self):
        MatType = self.ComboBox.currentText()
        FileName = library_Path.Path + MatType + ".dat"
        Section_list = self.read_Database(FileName)
        self.load_PropertiesTable(Section_list)

    def load_PropertiesTable(self, Properties_list):
        self.Material_tableWidget.setRowCount(0)
        self.Material_tableWidget.clearContents()
        self.Material_tableWidget.setRowCount(len(Properties_list))
        self.Material_tableWidget.setColumnCount(1)
        self.Material_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for ii in range(len(Properties_list)):
            tsect = Properties_list[ii]["Material"]
            tItem = QTableWidgetItem(tsect)
            # tItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tItem.setForeground(QBrush(QColor(0, 0, 0)))
            self.Material_tableWidget.setItem(ii, 0, tItem)
        self.Material_tableWidget.selectRow(0)
        self.load_DimensionsTable(self.Material_tableWidget.model().index(0, 0))

    def load_DimensionsTable(self, index):
        table_row = index.row()
        MatType = self.ComboBox.currentText()
        FileName = library_Path.Path + MatType + ".dat"
        Section_list = self.read_Database(FileName)
        Section = Section_list[table_row]
        self.Properties_tableWidget.setRowCount(0)
        self.Properties_tableWidget.clearContents()
        self.Properties_tableWidget.setRowCount(len(Section) - 1)
        self.Properties_tableWidget.setColumnCount(2)
        self.Properties_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Counter = 0
        for ii in Section:
            if ii == "Material":
                continue
            Name = ii + "="
            Data = str(Section[ii])
            NameItem = QTableWidgetItem(Name)
            DataItem = QTableWidgetItem(Data)
            #NameItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            NameItem.setForeground(QBrush(QColor(0, 0, 0)))
            #DataItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            DataItem.setForeground(QBrush(QColor(0, 0, 0)))
            self.Properties_tableWidget.setItem(Counter, 0, NameItem)
            self.Properties_tableWidget.setItem(Counter, 1, DataItem)
            Counter += 1


    def read_Database(self, Filename):
        result = []
        dic = {}
        dic1 = []
        with open(Filename, 'r') as f:
            for line in f:
                if list(line.strip('\n').split('	')) != ['']:
                    if len(list(line.strip('\n').split('	'))) == 1:
                        result.append(list(line.strip('\n').split(', ')))
                    else:
                        result.append(list(line.strip('\n').split('	')))
                else:
                    break
        for i in result[1][0]:
            if i in "% ":
                result[1][0]=result[1][0].replace(i,"")
        # print(result)
        for i in range(len(result)):
            if i > 1:
                for ii in range(len(result[i])):
                    dic[result[1][ii]] = result[i][ii]
                dic1.append(dic)
                dic = {}
        return dic1

