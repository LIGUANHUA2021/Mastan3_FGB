# External library
import traceback
import vispy.scene
import vispy.app
from PySide6.QtGui import QIcon, QAction, QCursor
from vispy.scene import visuals
from enum import Enum
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
import sys
from PySide6.QtCore import QTimer, QThread,Qt
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QMenu, QMessageBox, QTableWidgetItem, \
    QItemDelegate, QAbstractItemView, QHeaderView, QStyleFactory


# Internal library
from gui.msasect.slotfunc import SlotFuncInMainWindow
from gui.msasect.base import Model
from gui.msasect.ui.PointAdd import PointAddDialog
from gui.msasect.ui.PointModify import PointModifyDialog
from gui.msasect.ui.MaterialAdd import MatAddDialog
from gui.msasect.ui.MaterialModify import MatModifyDialog
from gui.msasect.ui.SegmentAdd import SegmentAddDialog

class EmptyDelegate(QItemDelegate):
    def __init__(self,parent=None):
        super(EmptyDelegate, self).__init__(parent)
    def createEditor(self,QWidget,QStyleOptionViewItem,QModelIndex):
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 700)
        self.CreateWidget()
        self.InitVispyEntity()
        self.SetLayout()
        self.SetMenubar()
        self.ConnectSignal()
        self.RetranslateUI()
        # self.getLogThread = getLogThread(self)
        # self.setWindowIcon(QIcon('ui/ico/document.ico'))

    def CreateWidget(self):
        self.centralwidget = QtWidgets.QWidget()
        self.MainMenu = QtUiTools.QUiLoader().load("ui/MainMenu.ui")
        #self.InP = QtWidgets.QTextEdit(self.centralwidget)
        #self.tMatGroupBoxWidget = QtWidgets.QGroupBox(self.centralwidget)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabMaterial = QtWidgets.QWidget()
        self.tabMaterial.setObjectName("Material")
        self.tabPoint = QtWidgets.QWidget()
        self.tabPoint.setObjectName("Point")
        self.tabSegment = QtWidgets.QWidget()
        self.tabSegment.setObjectName("Segment")

        self.tabWidget.addTab(self.tabMaterial,'')
        self.tabWidget.addTab(self.tabPoint,'')
        self.tabWidget.addTab(self.tabSegment,'')

        self.materialTable = QtWidgets.QTableWidget(self.tabMaterial)
        self.materialTable.setGeometry(QtCore.QRect(12, 12, 460, 400))
        self.materialTable.setObjectName("materialTable")
        self.materialTable.setColumnCount(4)
        self.materialTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.materialTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.materialTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem('Mat. ID ')
        self.materialTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('E')
        self.materialTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('G')
        self.materialTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem('fy')
        self.materialTable.setHorizontalHeaderItem(3, item)

        self.MaterialLayout = QtWidgets.QVBoxLayout(self.tabMaterial)
        self.MaterialLayout.addWidget(self.materialTable)
        self.MatButtonLayout = QtWidgets.QHBoxLayout(self.tabMaterial)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.MatButtonLayout.addItem(spacerItem)

        self.MatAddButton = QtWidgets.QPushButton()
        self.MatAddButton.setObjectName("Add")
        self.MatAddButton.setText("Add")
        self.MatAddButton.clicked.connect(lambda: self.AddItem(1))
        self.MatModifyButton = QtWidgets.QPushButton()
        self.MatModifyButton.setObjectName("Modify")
        self.MatModifyButton.setText("Modify")
        self.MatModifyButton.clicked.connect(lambda: self.ModifyItem(1))
        self.MatDeleteButton = QtWidgets.QPushButton()
        self.MatDeleteButton.setObjectName("Delete")
        self.MatDeleteButton.setText("Delete")
        self.MatDeleteButton.clicked.connect(lambda: self.DelItem(1))

        self.MatButtonLayout.addWidget(self.MatAddButton)
        self.MatButtonLayout.addWidget(self.MatModifyButton)
        self.MatButtonLayout.addWidget(self.MatDeleteButton)
        self.MaterialLayout.addLayout(self.MatButtonLayout)
        self.MaterialLayout.setStretch(0, 1)
        self.MaterialLayout.setStretch(20, 1)



        self.pointTable = QtWidgets.QTableWidget(self.tabPoint)
        self.pointTable.setGeometry(QtCore.QRect(12, 12, 460, 400))
        self.pointTable.setObjectName("pointTable")
        self.pointTable.setColumnCount(3)
        # self.nodeTable.horizontalHeader().setDefaultSectionSize(115)
        # self.nodeTable.setItemDelegateForColumn(0,EmptyDelegate(self))
        # self.nodeTable.setItemDelegateForColumn(1,EmptyDelegate(self))
        # self.nodeTable.setItemDelegateForColumn(2,EmptyDelegate(self))
        # self.nodeTable.setItemDelegateForColumn(3,EmptyDelegate(self))
        self.pointTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pointTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pointTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem('Point')
        self.pointTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('Y')
        self.pointTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('Z')
        self.pointTable.setHorizontalHeaderItem(2, item)
        #item = QtWidgets.QTableWidgetItem('Z')
        #self.pointTable.setHorizontalHeaderItem(3, item)

        self.PointLayout = QtWidgets.QVBoxLayout(self.tabPoint)
        self.PointLayout.addWidget(self.pointTable)
        self.PointButtonLayout = QtWidgets.QHBoxLayout(self.tabPoint)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.PointButtonLayout.addItem(spacerItem)

        self.PointAddButton = QtWidgets.QPushButton()
        self.PointAddButton.setObjectName("Add")
        self.PointAddButton.setText("Add")
        self.PointAddButton.clicked.connect(lambda: self.AddItem(2))
        self.PointModifyButton = QtWidgets.QPushButton()
        self.PointModifyButton.setObjectName("Modify")
        self.PointModifyButton.setText("Modify")
        self.PointModifyButton.clicked.connect(lambda: self.ModifyItem(2))
        self.PointDeleteButton = QtWidgets.QPushButton()
        self.PointDeleteButton.setObjectName("Delete")
        self.PointDeleteButton.setText("Delete")
        self.PointDeleteButton.clicked.connect(lambda: self.DelItem(2))

        self.PointButtonLayout.addWidget(self.PointAddButton)
        self.PointButtonLayout.addWidget(self.PointModifyButton)
        self.PointButtonLayout.addWidget(self.PointDeleteButton)
        self.PointLayout.addLayout(self.PointButtonLayout)
        self.PointLayout.setStretch(0, 1)
        self.PointLayout.setStretch(20, 1)


        self.segmentTable = QtWidgets.QTableWidget(self.tabSegment)
        self.segmentTable.setGeometry(QtCore.QRect(12, 12, 460, 400))
        self.segmentTable.setObjectName("segmentTable")
        self.segmentTable.setColumnCount(5)
        # self.memberTable.horizontalHeader().setDefaultSectionSize(115)
        self.segmentTable.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.segmentTable.setItemDelegateForColumn(1,EmptyDelegate(self))
        self.segmentTable.setItemDelegateForColumn(2,EmptyDelegate(self))
        self.segmentTable.setItemDelegateForColumn(3,EmptyDelegate(self))
        self.segmentTable.setItemDelegateForColumn(4,EmptyDelegate(self))
        self.segmentTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.segmentTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.segmentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem('Seg. ID')
        self.segmentTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('P. I')
        self.segmentTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('P. J')
        self.segmentTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem('Thick.')
        self.segmentTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem('Mat. ID')
        self.segmentTable.setHorizontalHeaderItem(4, item)

        self.SegmentLayout = QtWidgets.QVBoxLayout(self.tabSegment)
        self.SegmentLayout.addWidget(self.segmentTable)
        self.SegmentButtonLayout = QtWidgets.QHBoxLayout(self.tabSegment)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.SegmentButtonLayout.addItem(spacerItem)

        self.SegmentAddButton = QtWidgets.QPushButton()
        self.SegmentAddButton.setObjectName("Add")
        self.SegmentAddButton.setText("Add")
        self.SegmentAddButton.clicked.connect(lambda :self.AddItem(3))
        self.SegmentModifyButton = QtWidgets.QPushButton()
        self.SegmentModifyButton.setObjectName("Modify")
        self.SegmentModifyButton.setText("Modify")
        self.SegmentModifyButton.clicked.connect(lambda :self.ModifyItem(3))
        self.SegmentDeleteButton = QtWidgets.QPushButton()
        self.SegmentDeleteButton.setObjectName("Delete")
        self.SegmentDeleteButton.setText("Delete")
        self.SegmentDeleteButton.clicked.connect(lambda :self.DelItem(3))
        # 设置member table的layout
        self.SegmentButtonLayout.addWidget(self.SegmentAddButton)
        self.SegmentButtonLayout.addWidget(self.SegmentModifyButton)
        self.SegmentButtonLayout.addWidget(self.SegmentDeleteButton)
        self.SegmentLayout.addLayout(self.SegmentButtonLayout)
        self.SegmentLayout.setStretch(0, 1)
        self.SegmentLayout.setStretch(20, 1)


        # self.TreeView = QtWidgets.QTreeWidget(self.centralwidget)
        self.OutputW = QtWidgets.QTextBrowser(self.centralwidget)

        self.MainMenu.New.setIcon(QIcon('ui/ico/new.ico'))
        self.MainMenu.Open.setIcon(QIcon('ui/ico/folder.ico'))
        self.MainMenu.Save.setIcon(QIcon('ui/ico/save.ico'))
        self.MainMenu.Plot.setIcon(QIcon('ui/ico/plot.ico'))
        self.MainMenu.Run.setIcon(QIcon('ui/ico/run.ico'))


        self.canvas = vispy.scene.SceneCanvas(keys='interactive', show=False, autoswap=True)
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'arcball'
        self.VispyW = self.canvas.native
        # self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        # self.PlotButton = QtWidgets.QPushButton(self.centralwidget)
        # self.ClearButton = QtWidgets.QPushButton(self.centralwidget)

        self.Timer = QTimer() # This timer is created for automatically update the text information in Output Widget (OutputW)
    # Initialize the entity used in VISPY. User should not revised the name of all the vispy entities
    # Please do not create new entities somewhere else!!!
    #     self.initTree()


    # def treeWidgetItem_fun(self, pos):
    #     item = self.InputW.currentItem()
    #     item1 = self.InputW.itemAt(pos)
    #     if item.type() == TreeItemType.itemBottomItem.value :
    #         if item != None and item1 != None:
    #             popMenu = QMenu()
    #             ModifyAction=QAction(u'Modify', self)
    #             DelAction=QAction(u'Delete', self)
    #             popMenu.addAction(ModifyAction)
    #             popMenu.addAction(DelAction)
    #             ModifyAction.triggered.connect(lambda: self.ModifyItem(0))
    #             DelAction.triggered.connect(lambda: self.DelItem(0))
    #             # popMenu.triggered[QAction].connect(lambda: self.processtrigger(a="I am the changed Label",q=QAction(u'aaa', self)))
    #             popMenu.exec_(QCursor.pos())
    #     elif item.type() == TreeItemType.itemTopItem.value :
    #             return
    #     elif item.type() == TreeItemType.itemSpringItem.value :
    #             return
    #     else:
    #         if item != None and item1 != None:
    #             popMenu = QMenu()
    #             AddAction = QAction(u'Add', self)
    #             popMenu.addAction(AddAction)
    #             AddAction.triggered.connect(lambda: self.AddItem(0))
    #             # popMenu.triggered[QAction].connect(lambda: self.processtrigger(a="I am the changed Label",q=QAction(u'aaa', self)))
    #             popMenu.exec_(QCursor.pos())
    #
    # def setBottomItem(self,middleItem,count,name,idList):
    #         for j in range(count):
    #             bottomItem = QTreeWidgetItem(TreeItemType.itemBottomItem.value)
    #             if middleItem.type()==272:
    #                 BoundaryList=Model.msaModel.SpringBoundary.Bound[idList[j]]
    #                 BoundaryTranslate={0:'0'}
    #                 for jj in Model.msaModel.SpringModel.ID:
    #                     BoundaryTranslate[jj]='S'+str(jj)
    #                 name=''
    #                 for k in range(6):
    #                     temp=BoundaryTranslate[BoundaryList[k]]+' ,'
    #                     name+=temp
    #                 name=name[:-1]
    #                 bottomItem.setText(0, f'[Node {idList[j]}]' + ' ' + name)
    #             elif middleItem.type() == 25:
    #                 BoundaryList=Model.msaModel.Bound.Bound[idList[j]]
    #                 name=''
    #                 for k in range(6):
    #                     temp=str(BoundaryList[k])+' ,'
    #                     name+=temp
    #                 name=name[:-1]
    #                 bottomItem.setText(0, f'[Node {idList[j]}]' + ' ' + name)
    #             elif middleItem.type() == 26:
    #                 LoadList=Model.msaModel.Load.LoadVector[idList[j]]
    #                 name=''
    #                 for k in range(6):
    #                     temp=str(LoadList[k])+' ,'
    #                     name+=temp
    #                 name=name[:-1]
    #                 bottomItem.setText(0, f'[Node {idList[j]}]' + ' ' + name)
    #             else:
    #                 bottomItem.setText(0, f'[{j + 1}]' + ' ' + name + ' ' + str(idList[j]))
    #             bottomItem.setFlags(self.itemFlags)
    #             bottomItem.setData(0, Qt.UserRole, idList[j])
    #             # bottomItem_Section.setCheckState(0,Qt.CheckState.Unchecked)
    #             middleItem.addChild(bottomItem)
    #             middleItem.setExpanded(True)

    def importDataToMatTable(self):
        try:
            self.materialTable.verticalHeader().hide()

            self.materialTable.setColumnWidth(0,100)
            matIDList=Model.msaModel.Mat.ID
            self.materialTable.setRowCount(0)
            self.materialTable.setRowCount(Model.msaModel.Mat.Count)
            for i in range(Model.msaModel.Mat.Count):
                for j in range(4):
                    Item = QTableWidgetItem('')
                    Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.materialTable.setItem(i, j, Item)
                    if j == 0:
                        Item.setText(str(Model.msaModel.Mat.ID[i]))
                    elif j == 1:
                        Item.setText(str(Model.msaModel.Mat.E[matIDList[i]]))
                    elif j == 2:
                        Item.setText(str(Model.msaModel.Mat.G[matIDList[i]]))
                    elif j == 3:
                        Item.setText(str(Model.msaModel.Mat.Fy[matIDList[i]]))
            # self.nodeTable.resizeColumnsToContents()
            # self.nodeTable.resizeRowsToContents()
            self.materialTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except:
            traceback.print_exc()


    def importDataToPointTable(self):
        try:
            self.pointTable.verticalHeader().hide()

            self.pointTable.setColumnWidth(0,100)
            pointIDList=Model.msaModel.Point.ID
            self.pointTable.setRowCount(0)
            self.pointTable.setRowCount(Model.msaModel.Point.Count)
            for i in range(Model.msaModel.Point.Count):
                for j in range(3):
                    Item = QTableWidgetItem('')
                    Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.pointTable.setItem(i, j, Item)
                    if j == 0:
                        Item.setText(str(Model.msaModel.Point.ID[i]))
                    elif j == 1:
                        Item.setText(str(Model.msaModel.Point.y[pointIDList[i]]))
                    elif j == 2:
                        Item.setText(str(Model.msaModel.Point.z[pointIDList[i]]))
            # self.nodeTable.resizeColumnsToContents()
            # self.nodeTable.resizeRowsToContents()
            self.pointTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except:
            traceback.print_exc()

    def importDataToSegmentTable(self):
        try:
            self.segmentTable.verticalHeader().hide()
            self.segmentTable.setColumnWidth(0,100)
            segmentIDList=Model.msaModel.Segment.ID
            self.segmentTable.setRowCount(0)
            self.segmentTable.setRowCount(Model.msaModel.Segment.Count)
            for i in range(Model.msaModel.Segment.Count):
                for j in range(5):
                    Item = QTableWidgetItem('')
                    Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.segmentTable.setItem(i, j, Item)
                    if j == 0:
                        Item.setText(str(Model.msaModel.Segment.ID[i]))
                    elif j == 1:
                        Item.setText(str(Model.msaModel.Segment.PointI[segmentIDList[i]]))
                    elif j == 2:
                        Item.setText(str(Model.msaModel.Segment.PointJ[segmentIDList[i]]))
                    elif j == 3:
                        Item.setText(str(Model.msaModel.Segment.SegThick[segmentIDList[i]]))
                    elif j == 4:
                        Item.setText(str(Model.msaModel.Segment.MaterialID[segmentIDList[i]]))

            # self.memberTable.resizeColumnsToContents()
            # self.memberTable.resizeRowsToContents()
            self.segmentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except:
            traceback.print_exc()

    def ModifyItem(self,tabIndex):
        if tabIndex == 0:
            item = self.InputW.currentItem()
            parentItem=item.parent()
            ScrollBarValue=self.InputW.verticalScrollBar().value()
            if parentItem.type() == 21:
                id=item.data(0,Qt.UserRole)
                ConcreteDetailUi = MaterialDialog(self,id)
                # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                ConcreteDetailUi.exec()
            elif parentItem.type() == 22:
                id=item.data(0,Qt.UserRole)
                ConcreteDetailUi = SectionDialog(self,id)
                # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                ConcreteDetailUi.exec()
            # elif parentItem.type() == 23:
            #     id=item.data(0,Qt.UserRole)
            #     ConcreteDetailUi = NodeDialog(self,id)
            #     # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
            #     ConcreteDetailUi.exec()
            # elif parentItem.type() == 24:
            #     id=item.data(0,Qt.UserRole)
            #     ConcreteDetailUi = MemberDialog(self,id)
            #     # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
            #     ConcreteDetailUi.exec()
            elif parentItem.type() == 25:
                id = item.data(0, Qt.UserRole)
                ConcreteDetailUi = BoundaryDialog(self,id)
                # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                ConcreteDetailUi.exec()
            elif parentItem.type() == 26:
                id = item.data(0, Qt.UserRole)
                ConcreteDetailUi = LoadDialog(self,id)
                # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                ConcreteDetailUi.exec()
            elif parentItem.type() == 272:
                id = item.data(0, Qt.UserRole)
                ConcreteDetailUi = SpringBoundaryDialog(self,id)
                # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                ConcreteDetailUi.exec()
            elif parentItem.type() == 271:
                id = item.data(0, Qt.UserRole)
                ConcreteDetailUi = SpringModelDialog(self,id)
                # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                ConcreteDetailUi.exec()
            self.InputW.verticalScrollBar().setValue(ScrollBarValue)
        elif tabIndex == 1:
            currentRow = self.materialTable.currentRow()
            id = int(self.materialTable.item(currentRow, 0).text())
            ConcreteDetailUi = MatModifyDialog(self, id)
            # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
            ConcreteDetailUi.exec()

        elif tabIndex == 2:
            currentRow = self.pointTable.currentRow()
            id = int(self.pointTable.item(currentRow, 0).text())
            ConcreteDetailUi = PointModifyDialog(self, id)
            # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
            ConcreteDetailUi.exec()
        elif tabIndex == 3:
            currentRow = self.segmentTable.currentRow()
            id = int(self.segmentTable.item(currentRow, 0).text())
            ConcreteDetailUi = SegmentAddDialog(self, id)
            # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
            ConcreteDetailUi.exec()

    def DelItem(self,tabIndex):
        try:
            if tabIndex == 0:
                mesBox = QMessageBox()
                mesBox.setWindowTitle('Reminder')
                mesBox.setText(
                    'Are you sure you want to delete?')
                mesBox.setIcon(mesBox.Icon.Warning)
                mesBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
                buttonNo = mesBox.button(QMessageBox.StandardButton.No)
                mesBox.exec()
                if mesBox.clickedButton() == buttonYes:
                    item = self.InputW.currentItem()
                    id=item.data(0,Qt.UserRole)
                    parentItem=item.parent()
                    if parentItem.type()==21:
                        Model.msaModel.Mat.Remove(id)
                    elif parentItem.type()==22:
                        Model.msaModel.Sect.Remove(id)
                    # elif parentItem.type()==23:
                    #     Model.msaModel.Node.Remove(id)
                    # elif parentItem.type()==24:
                    #     Model.msaModel.Member.Remove(id)
                    elif parentItem.type()==25:
                        Model.msaModel.Bound.Remove(id)
                    elif parentItem.type()==26:
                        Model.msaModel.Load.Remove(id)
                    elif parentItem.type() == 272:
                        Model.msaModel.SpringBoundary.Remove(id)
                    elif parentItem.type() == 271:
                        Model.msaModel.SpringModel.Remove(id)
                    # elif parentItem.type()==27:
                    #     Model.msaModel.Member.Remove(id)
                    parentItem.removeChild(item)
                    self.ResetTable()
            elif tabIndex == 1:
                currentRow = self.nodeTable.currentRow()
                if currentRow != -1:
                    mesBox = QMessageBox()
                    mesBox.setWindowTitle('Reminder')
                    mesBox.setText(
                        'Are you sure you want to delete?')
                    mesBox.setIcon(mesBox.Icon.Warning)
                    mesBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
                    buttonNo = mesBox.button(QMessageBox.StandardButton.No)
                    mesBox.exec()
                    if mesBox.clickedButton() == buttonYes:
                        id = int(self.nodeTable.item(currentRow, 0).text())
                        Model.msaModel.Node.Remove(id)
                        self.ResetTable()
            elif tabIndex == 2:
                currentRow = self.memberTable.currentRow()
                if currentRow != -1:
                    mesBox = QMessageBox()
                    mesBox.setWindowTitle('Reminder')
                    mesBox.setText(
                        'Are you sure you want to delete?')
                    mesBox.setIcon(mesBox.Icon.Warning)
                    mesBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    buttonYes = mesBox.button(QMessageBox.StandardButton.Yes)
                    buttonNo = mesBox.button(QMessageBox.StandardButton.No)
                    mesBox.exec()
                    if mesBox.clickedButton() == buttonYes:
                        currentRow = self.memberTable.currentRow()
                        if currentRow != -1:
                            id = int(self.memberTable.item(currentRow, 0).text())
                            Model.msaModel.Member.Remove(id)
                            self.ResetTable()
            else:
                pass

        except:
            traceback.print_exc()

    def AddItem(self,tabIndex):
        try:
            if tabIndex == 0:
                item = self.InputW.currentItem()
                if item.type() == 21:
                    Ui = MaterialAddDialog(self)
                    Ui.exec()
                elif item.type() == 22:
                    Ui = SectionAddDialog(self)
                    Ui.exec()
                # elif item.type() == 23:
                #     Ui = NodeAddDialog(self)
                #     Ui.exec()
                # elif item.type() == 24:
                #     Ui = MemberAddDialog(self)
                #     Ui.exec()
                elif item.type() == 25:
                    Ui = BoundaryAddDialog(self)
                    Ui.exec()
                elif item.type() == 26:
                    Ui = LoadAddDialog(self)
                    Ui.exec()
                elif item.type() == 272:
                    Ui = SpringBoundaryAddDialog(self)
                    Ui.exec()
                elif item.type() == 271:
                    Ui = SpringModelAddDialog(self)
                    Ui.exec()
                # elif item.type() == 272:
                #     Ui = SpringBoundaryDialog(self)
                #     Ui.exec()
                # elif parentItem.type() == 25:
                #     id = item.data(0, Qt.UserRole)
                #     ConcreteDetailUi = BoundaryDialog(self, id)
                #     # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                #     ConcreteDetailUi.exec()
                # elif parentItem.type() == 26:
                #     id = item.data(0, Qt.UserRole)
                #     ConcreteDetailUi = LoadDialog(self, id)
                #     # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
                #     ConcreteDetailUi.exec()
                # self.InputW.verticalScrollBar().setValue(ScrollBarValue)
                self.ResetTable()
            elif tabIndex == 1:
                currentRow = self.materialTable.currentRow()
                # id = int(self.pointTable.item(currentRow, 0).text())
                Ui = MatAddDialog(self)
                Ui.exec()
                self.ResetTable()
            elif tabIndex == 2:
                currentRow = self.pointTable.currentRow()
                # id = int(self.pointTable.item(currentRow, 0).text())
                Ui = PointAddDialog(self)
                Ui.exec()
                self.ResetTable()
            elif tabIndex == 3:
                currentRow = self.segmentTable.currentRow()
                # id = int(self.memberTable.item(currentRow, 0).text())
                Ui = SegmentAddDialog(self)
                Ui.exec()
                self.ResetTable()
        except:
            traceback.print_exc()

    # def DelAllBottomItem(self):
    #     try:
    #         topItem = self.InputW.topLevelItem(0)
    #         for i in range(topItem.childCount()):
    #                 middleItem=topItem.child(i)
    #                 itemList = []
    #                 if middleItem.type()==27:
    #                     for j in range(middleItem.childCount()):
    #                         springMiddleItem=middleItem.child(j)
    #                         for k in range(springMiddleItem.childCount()):
    #                             bottomItem = springMiddleItem.child(k)
    #                             itemList.append(bottomItem)
    #                         for k in itemList:
    #                             springMiddleItem.removeChild(k)
    #                 else:
    #                     for j in range(middleItem.childCount()):
    #                         bottomItem = middleItem.child(j)
    #                         itemList.append(bottomItem)
    #                     for k in itemList:
    #                         middleItem.removeChild(k)
    #     except:
    #         traceback.print_exc()

    def ResetTable(self):
        #self.DelAllBottomItem()
        self.segmentTable.setRowCount(0)
        self.importDataToSegmentTable()
        self.pointTable.setRowCount(0)
        self.importDataToPointTable()
        self.materialTable.setRowCount(0)
        self.importDataToMatTable()

    def InitVispyEntity(self):
        visuals.XYZAxis(parent=self.view.scene)
        self.Node = visuals.Markers(parent=self.view.scene, size=10)
        self.Mem = vispy.scene.Line(parent=self.view.scene, method="gl", antialias=False, connect='segments')
        self.NodeText = vispy.scene.Text(face="Arial", parent=self.view.scene, color='green', method="cpu",
                                         font_size=20)
        self.MemText = vispy.scene.Text(face="Arial", parent=self.view.scene, color='green', method="cpu",
                                        font_size=20)
        self.JointLoadF = vispy.scene.Line(parent=self.view.scene, method="gl", antialias=False, color='red', connect='segments')
        self.JointLoadM = vispy.scene.Line(parent=self.view.scene, method="gl", antialias=False, color='red', connect='segments')

    def SetLayout(self):
        self.VLayoutMain = QtWidgets.QVBoxLayout(self.centralwidget)
        self.HLayoutMain = QtWidgets.QHBoxLayout()
        self.VLayoutLeft = QtWidgets.QVBoxLayout()
        self.VLayoutLeft.addWidget(self.tabWidget)
        # self.ButtonLayout = QtWidgets.QHBoxLayout()
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
        #                                    QtWidgets.QSizePolicy.Policy.Minimum)
        # self.ButtonLayout.addItem(spacerItem)
        # self.ButtonLayout.addWidget(self.RunButton)
        # self.ButtonLayout.addWidget(self.PlotButton)
        # self.ButtonLayout.addWidget(self.ClearButton)
        # self.VLayoutLeft.addLayout(self.ButtonLayout)
        self.VLayoutLeft.setStretch(0, 1)
        self.VLayoutLeft.setStretch(20, 1)

        self.VLayoutRight = QtWidgets.QVBoxLayout()
        self.VLayoutRight.addWidget(self.VispyW)
        self.VLayoutRight.addWidget(self.OutputW)
        self.VLayoutRight.setStretch(0, 1)
        self.VLayoutRight.setStretch(18, 1)

        self.HLayoutMain.addLayout(self.VLayoutLeft)
        self.HLayoutMain.addLayout(self.VLayoutRight)
        self.HLayoutMain.setStretch(0, 1)
        self.HLayoutMain.setStretch(1, 4.5)

        self.VLayoutMain.addWidget(self.MainMenu)
        self.VLayoutMain.addLayout(self.HLayoutMain)
        self.setCentralWidget(self.centralwidget)

    def SetMenubar(self):
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 30))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuGeometry = QtWidgets.QMenu(self.menubar)
        self.menuProperties = QtWidgets.QMenu(self.menubar)
        self.menuConditions = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction()
        self.actionOpen = QtGui.QAction()
        self.actionSave = QtGui.QAction()
        self.actionSaveAs = QtGui.QAction()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuGeometry.menuAction())
        self.menubar.addAction(self.menuProperties.menuAction())
        self.menubar.addAction(self.menuConditions.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())

    def ConnectSignal(self):
        # self.RunButton.clicked.connect(self.Run)
        self.MainMenu.Run.clicked.connect(self.Run)
        self.MainMenu.Plot.clicked.connect(self.VisualizeModel)
        # self.PlotButton.clicked.connect(self.VisualizeModel)
        self.actionNew.triggered.connect(self.NewFile)
        self.MainMenu.New.clicked.connect(self.NewFile)
        self.actionOpen.triggered.connect(self.OpenFile)
        self.MainMenu.Open.clicked.connect(self.OpenFile)
        self.actionSave.triggered.connect(self.SaveFile)
        self.MainMenu.Save.clicked.connect(self.SaveFile)
        self.actionSaveAs.triggered.connect(self.SaveAsFile)
        # Update the text information in OutputW every half second

    def RetranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Msasect - Python-based Cross-section Analysis Software"))
        # self.RunButton.setText(_translate("MainWindow", "Run"))
        # self.PlotButton.setText(_translate("MainWindow", "Plot"))
        # self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        #self.menuGeometry.setTitle(_translate("MainWindow", "Geometry"))
        #self.menuProperties.setTitle(_translate("MainWindow", "Properties"))
        #self.menuConditions.setTitle(_translate("MainWindow", "Conditions"))
        #self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        #self.menuResults.setTitle(_translate("MainWindow", "Results"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMaterial), _translate("MainWindow", "Material"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPoint), _translate("MainWindow", "Point"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSegment), _translate("MainWindow", "Segment"))

    def VisualizeModel(self):
        SlotFuncInMainWindow.VisualizeModel(self)
    #
    def NewFile(self):
        SlotFuncInMainWindow.NewFile(self)
        self.ResetTable()
        # self.importDataToTree()
        # self.importDataToPointTable()
        # self.importDataToSegmentTable()
    def OpenFile(self):
        SlotFuncInMainWindow.OpenFile(self)
        self.ResetTable()
        self.VisualizeModel()
        # self.importDataToTree()
        # self.importDataToPointTable()
        # self.importDataToSegmentTable()
    def SaveFile(self):
        SlotFuncInMainWindow.SaveFile(self)
    def SaveAsFile(self):
        SlotFuncInMainWindow.SaveAsFile(self)
    # def Run(self):
    #     Ui = RunShowDialog(self)
    #     Ui.exec()
    #     SlotFuncInMainWindow.UpdateOutputW(self, 1)
        # SlotFuncInMainWindow.Run(self)