# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QBrush, QColor, QPixmap, QIcon
from gui.msasect.ui.Ui_ISectionDb import Ui_ISectionDb_Dialog

class library_Path:
    Path = r"base/library/"
    SectType = r"AISC-I"


class ISectionDb_Dialog(QDialog, Ui_ISectionDb_Dialog):
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
        self.setWindowIcon(QIcon('ui/ico/TemplateIcon/I-Section.ico'))
        self.initlize()
        self.Section_tableWidget.clicked.connect(self.load_DimensionsTable)
        self.ComboBox.currentIndexChanged.connect(self.refresh_DimensionsTable)

    @Slot()
    def on_OK_button_clicked(self):
        Num_column = 2
        Num_row = self.Dimensions_tableWidget.rowCount()
        Sect_Dimensions = {}
        for ii in range(Num_row):
            type = self.Dimensions_tableWidget.item(ii, 0).text().strip('=')
            value = self.Dimensions_tableWidget.item(ii, 1).text()
            Sect_Dimensions[type] = float(value)
        if self.ComboBox.currentText() == "AISC(in)":
            unit=0
        else:
            unit = 1
        Sect_Dimensions["unit"] = unit
        Section_row = self.Section_tableWidget.currentRow()
        Sect_Dimensions["Type"] = self.Section_tableWidget.item(Section_row, 0).text()
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
        self.label.setPixmap(QPixmap("ui/Template/I-Section_Db.jpg"))
        Database = self.ComboBox.currentText()
        # print(Database)
        if Database == "AISC(in)":
            # print("currentText:", Database)
            FileName = library_Path.Path + library_Path.SectType + ".dat"
        else:
            FileName = library_Path.Path + library_Path.SectType + "_SI" + ".dat"
        Section_list = self.read_Database(FileName)
        self.load_SectionTable(Section_list)

    def refresh_DimensionsTable(self):
        Database = self.ComboBox.currentText()
        if Database == "AISC(in)":
            FileName = library_Path.Path + library_Path.SectType + ".dat"
        else:
            FileName = library_Path.Path + library_Path.SectType + "_SI" + ".dat"
        Section_list = self.read_Database(FileName)
        self.load_SectionTable(Section_list)

    def load_SectionTable(self, Section_list):
        self.Section_tableWidget.setRowCount(0)
        self.Section_tableWidget.clearContents()
        self.Section_tableWidget.setRowCount(len(Section_list))
        self.Section_tableWidget.setColumnCount(1)
        self.Section_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for ii in range(len(Section_list)):
            tsect = Section_list[ii]["Shape"]
            tItem = QTableWidgetItem(tsect)
            # tItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tItem.setForeground(QBrush(QColor(0, 0, 0)))
            self.Section_tableWidget.setItem(ii, 0, tItem)
        self.Section_tableWidget.selectRow(0)
        self.load_DimensionsTable(self.Section_tableWidget.model().index(0, 0))

    def load_DimensionsTable(self, index):
        table_row = index.row()
        Database = self.ComboBox.currentText()
        if Database == "AISC(in)":
            FileName = library_Path.Path + library_Path.SectType + ".dat"
        else:
            FileName = library_Path.Path + library_Path.SectType + "_SI" + ".dat"
        Section_list = self.read_Database(FileName)
        Section = Section_list[table_row]
        self.Dimensions_tableWidget.setRowCount(0)
        self.Dimensions_tableWidget.clearContents()
        self.Dimensions_tableWidget.setRowCount(len(Section) - 2)
        self.Dimensions_tableWidget.setColumnCount(2)
        self.Dimensions_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Counter = 0
        for ii in Section:
            if ii == "Shape":
                continue
            Name = ii + "="
            Data = str(Section[ii])
            NameItem = QTableWidgetItem(Name)
            DataItem = QTableWidgetItem(Data)
            #NameItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            NameItem.setForeground(QBrush(QColor(0, 0, 0)))
            #DataItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            DataItem.setForeground(QBrush(QColor(0, 0, 0)))
            self.Dimensions_tableWidget.setItem(Counter, 0, NameItem)
            self.Dimensions_tableWidget.setItem(Counter, 1, DataItem)
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

