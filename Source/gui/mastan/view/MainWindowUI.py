# External library
import traceback
import vispy.scene
import vispy.app
from PySide6.QtGui import QIcon, QAction, QCursor, QColor
from vispy.scene import visuals
from enum import Enum
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
import sys
from PySide6.QtCore import QTimer, QThread,Qt
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QMenu, QMessageBox, QTableWidgetItem, \
    QItemDelegate, QAbstractItemView, QHeaderView, QStyleFactory
# Internal library
from gui.mastan.slotfunc import SlotFuncInMainWindow,OutputWidgetDisplay
from gui.mastan.base import model
from gui.mastan.ui.BoundaryAdd import BoundaryAddDialog
from gui.mastan.ui.LoadAdd import LoadAddDialog
from gui.mastan.ui.MaterialAdd import MaterialAddDialog
from gui.mastan.ui.MaterialInput import MaterialDialog
from gui.mastan.ui.MemAdd import MemberAddDialog
from gui.mastan.ui.NodeInput import NodeDialog
from gui.mastan.ui.NodeAdd import NodeAddDialog
from gui.mastan.ui.MemInput import MemberDialog
from gui.mastan.ui.BoundaryInput import BoundaryDialog
from gui.mastan.ui.LoadInput import LoadDialog
from gui.mastan.ui.SectionAdd import SectionAddDialog
from gui.mastan.ui.SectionInput import SectionDialog
from gui.mastan.ui.SpingModelAdd import SpringModelAddDialog
from gui.mastan.ui.SpingModelInput import SpringModelDialog
from gui.mastan.ui.SpringBoundaryAdd import SpringBoundaryAddDialog
from gui.mastan.ui.SpringBoundaryInput import SpringBoundaryDialog
from gui.mastan.ui.RunShow import RunShowDialog


class TreeItemType(Enum):
    itemTopItem=11
    itemMaterialItem=21
    itemSectionItem=22
    itemNodeItem=23
    itemMemberItem=24
    itemBoundaryItem=25
    itemJointLoadItem=26
    itemSpringItem=27
    itemSpringModelItem=271
    itemSpringBoundaryItem=272
    itemBottomItem=31

class TreeColNum(Enum):
    idItem=0
    detailItem=1

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
        # self.setStyleSheet("color: rgb(255, 255, 255);\n"
        #     "background-color: rgb(128, 128, 128);")
        self.tabWidget.setStyleSheet("""
            color: rgb(255, 255, 255);
            background-color: rgb(128, 128, 128);
            font-family: Segoe UI;
            font-size: 9pt;
            """)
        self.tabWidget.setStyleSheet("""
            QTabBar::tab:selected{
            background:rgb(128, 128, 128);
            color:white;}
        """)
        self.tabTree.setStyleSheet("background:rgb(128, 128, 128);")
        self.tabNode.setStyleSheet("background:rgb(128, 128, 128);")
        self.tabMember.setStyleSheet("background:rgb(128, 128, 128);")
        self.NodeAddButton.setStyleSheet("background:rgb(255, 255, 255);")
        self.NodeModifyButton.setStyleSheet("background:rgb(255, 255, 255);")
        self.NodeDeleteButton.setStyleSheet("background:rgb(255, 255, 255);")
        self.MemberAddButton.setStyleSheet("background:rgb(255, 255, 255);")
        self.MemberModifyButton.setStyleSheet("background:rgb(255, 255, 255);")
        self.MemberDeleteButton.setStyleSheet("background:rgb(255, 255, 255);")
        self.OutputW.setStyleSheet("background-color:rgb(43, 43, 43);")
        self.nodeTable.setStyleSheet("background-color:white;")
        self.memberTable.setStyleSheet("background-color:white;")

    def CreateWidget(self):
        self.centralwidget = QtWidgets.QWidget()
        self.MainMenu = QtUiTools.QUiLoader().load("ui/MainMenu.ui")
        #self.InputW = QtWidgets.QTextEdit(self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        # self.tabWidget.setStyleSheet("""
        #     background-color: rgb(128, 128, 128);
        #     font-family: Segoe UI;
        #     font-size: 9pt;
        #     color: rgb(255, 255, 255);}
        #     """)
        self.tabTree = QtWidgets.QWidget()
        self.tabTree.setObjectName("Model")
        self.tabNode = QtWidgets.QWidget()
        self.tabNode.setObjectName("Node")
        self.tabMember = QtWidgets.QWidget()
        self.tabMember.setObjectName("Member")

        self.tabWidget.addTab(self.tabTree,'')
        self.tabWidget.addTab(self.tabNode,'')
        self.tabWidget.addTab(self.tabMember,'')

        self.InputW = QtWidgets.QTreeWidget(self.tabTree)

        self.InputW.setGeometry(QtCore.QRect(12, 12, 460, 450))
        self.InputW.setColumnCount(1)
        self.InputW.setStyle(QStyleFactory.create('windows'))
        # self.InputW.setHeaderLabel('Item')
        self.InputW.header().hide()
        self.TreeLayout = QtWidgets.QVBoxLayout(self.tabTree)
        self.TreeLayout.addWidget(self.InputW)

        self.nodeTable = QtWidgets.QTableWidget(self.tabNode)
        self.nodeTable.setGeometry(QtCore.QRect(12, 12, 460, 400))
        self.nodeTable.setObjectName("nodeTable")
        self.nodeTable.setColumnCount(4)
        # self.nodeTable.horizontalHeader().setDefaultSectionSize(115)
        self.nodeTable.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.nodeTable.setItemDelegateForColumn(1,EmptyDelegate(self))
        self.nodeTable.setItemDelegateForColumn(2,EmptyDelegate(self))
        self.nodeTable.setItemDelegateForColumn(3,EmptyDelegate(self))
        self.nodeTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.nodeTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.nodeTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.nodeTable.setBackgroundRole()
        item = QtWidgets.QTableWidgetItem('Node')
        self.nodeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('X')
        self.nodeTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('Y')
        self.nodeTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem('Z')
        self.nodeTable.setHorizontalHeaderItem(3, item)

        self.NodeLayout = QtWidgets.QVBoxLayout(self.tabNode)
        self.NodeLayout.addWidget(self.nodeTable)
        self.NodeButtonLayout = QtWidgets.QHBoxLayout(self.tabNode)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.NodeButtonLayout.addItem(spacerItem)

        self.NodeAddButton = QtWidgets.QPushButton()
        self.NodeAddButton.setObjectName("Add")
        self.NodeAddButton.setText("Add")
        self.NodeAddButton.clicked.connect(lambda: self.AddItem(1))
        self.NodeModifyButton = QtWidgets.QPushButton()
        self.NodeModifyButton.setObjectName("Modify")
        self.NodeModifyButton.setText("Modify")
        self.NodeModifyButton.clicked.connect(lambda: self.ModifyItem(1))
        self.NodeDeleteButton = QtWidgets.QPushButton()
        self.NodeDeleteButton.setObjectName("Delete")
        self.NodeDeleteButton.setText("Delete")
        self.NodeDeleteButton.clicked.connect(lambda: self.DelItem(1))

        self.NodeButtonLayout.addWidget(self.NodeAddButton)
        self.NodeButtonLayout.addWidget(self.NodeModifyButton)
        self.NodeButtonLayout.addWidget(self.NodeDeleteButton)
        self.NodeLayout.addLayout(self.NodeButtonLayout)
        self.NodeLayout.setStretch(0, 1)
        self.NodeLayout.setStretch(20, 1)


        self.memberTable = QtWidgets.QTableWidget(self.tabMember)
        self.memberTable.setGeometry(QtCore.QRect(12, 12, 460, 400))
        self.memberTable.setObjectName("memberTable")
        self.memberTable.setColumnCount(4)
        # self.memberTable.horizontalHeader().setDefaultSectionSize(115)
        self.memberTable.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.memberTable.setItemDelegateForColumn(1,EmptyDelegate(self))
        self.memberTable.setItemDelegateForColumn(2,EmptyDelegate(self))
        self.memberTable.setItemDelegateForColumn(3,EmptyDelegate(self))
        self.memberTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.memberTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.memberTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem('Member')
        self.memberTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('Node I')
        self.memberTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem('Node J')
        self.memberTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem('Section')
        self.memberTable.setHorizontalHeaderItem(3, item)

        self.MemberLayout = QtWidgets.QVBoxLayout(self.tabMember)
        self.MemberLayout.addWidget(self.memberTable)
        self.MemberButtonLayout = QtWidgets.QHBoxLayout(self.tabMember)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.MemberButtonLayout.addItem(spacerItem)

        self.MemberAddButton = QtWidgets.QPushButton()
        self.MemberAddButton.setObjectName("Add")
        self.MemberAddButton.setText("Add")
        self.MemberAddButton.clicked.connect(lambda :self.AddItem(2))
        self.MemberModifyButton = QtWidgets.QPushButton()
        self.MemberModifyButton.setObjectName("Modify")
        self.MemberModifyButton.setText("Modify")
        self.MemberModifyButton.clicked.connect(lambda :self.ModifyItem(2))
        self.MemberDeleteButton = QtWidgets.QPushButton()
        self.MemberDeleteButton.setObjectName("Delete")
        self.MemberDeleteButton.setText("Delete")
        self.MemberDeleteButton.clicked.connect(lambda :self.DelItem(2))
        # 设置member table的layout
        self.MemberButtonLayout.addWidget(self.MemberAddButton)
        self.MemberButtonLayout.addWidget(self.MemberModifyButton)
        self.MemberButtonLayout.addWidget(self.MemberDeleteButton)
        self.MemberLayout.addLayout(self.MemberButtonLayout)
        self.MemberLayout.setStretch(0, 1)
        self.MemberLayout.setStretch(20, 1)


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
        self.initTree()

    def initTree(self):
        self.InputW.setContextMenuPolicy(Qt.CustomContextMenu)
        self.InputW.customContextMenuRequested.connect(self.treeWidgetItem_fun)

        self.itemFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate)

        topItem=QTreeWidgetItem(self.InputW,TreeItemType.itemTopItem.value)

        topItem.setFlags(self.itemFlags)
        topItem.setData(0,Qt.UserRole,'')
        topItem.setText(0,'Structural Model')
        # topItem.setCheckState(0,Qt.CheckState.Unchecked)
        self.InputW.addTopLevelItem(topItem)

        middleItemNameDict = {TreeItemType.itemMaterialItem.value: "Material",
                              TreeItemType.itemSectionItem.value: "Section",
                              TreeItemType.itemNodeItem.value: "Node",
                              TreeItemType.itemMemberItem.value: "Member",
                              TreeItemType.itemBoundaryItem.value: "Boundary",
                              TreeItemType.itemJointLoadItem.value: "Joint Load",
                              TreeItemType.itemSpringItem.value: "Spring",
                              }

        middleItemTypeList=[TreeItemType.itemMaterialItem.value,
                            TreeItemType.itemSectionItem.value,
                            TreeItemType.itemNodeItem.value,
                            TreeItemType.itemMemberItem.value,
                            TreeItemType.itemBoundaryItem.value,
                            TreeItemType.itemJointLoadItem.value,
                            TreeItemType.itemSpringItem.value,]

        for i in range(7):
            if i == 2 or i == 3:
                pass
            else:
                middleItem=QTreeWidgetItem(topItem,middleItemTypeList[i])
                middleItem.setText(0,middleItemNameDict[middleItemTypeList[i]])
                middleItem.setFlags(self.itemFlags)
                middleItem.setData(0,Qt.UserRole,'')
                # middleItem.setCheckState(0,Qt.CheckState.Unchecked)
                topItem.addChild(middleItem)
                topItem.setExpanded(True)
                if i == 6:
                    springModelItem=QTreeWidgetItem(middleItem,TreeItemType.itemSpringModelItem.value)
                    springModelItem.setText(0,'Spring Model')
                    springModelItem.setFlags(self.itemFlags)
                    springModelItem.setData(0, Qt.UserRole, '')
                    springBoundaryItem=QTreeWidgetItem(middleItem,TreeItemType.itemSpringBoundaryItem.value)
                    springBoundaryItem.setText(0,'Spring Boundary')
                    springBoundaryItem.setFlags(self.itemFlags)
                    springBoundaryItem.setData(0, Qt.UserRole, '')
                    middleItem.addChild(springModelItem)
                    middleItem.addChild(springBoundaryItem)
                    middleItem.setExpanded(True)

    def treeWidgetItem_fun(self, pos):
        item = self.InputW.currentItem()
        item1 = self.InputW.itemAt(pos)
        if item.type() == TreeItemType.itemBottomItem.value :
            if item != None and item1 != None:
                popMenu = QMenu()
                ModifyAction=QAction(u'Modify', self)
                DelAction=QAction(u'Delete', self)
                popMenu.addAction(ModifyAction)
                popMenu.addAction(DelAction)
                ModifyAction.triggered.connect(lambda: self.ModifyItem(0))
                DelAction.triggered.connect(lambda: self.DelItem(0))
                # popMenu.triggered[QAction].connect(lambda: self.processtrigger(a="I am the changed Label",q=QAction(u'aaa', self)))
                popMenu.exec_(QCursor.pos())
        elif item.type() == TreeItemType.itemTopItem.value :
                return
        elif item.type() == TreeItemType.itemSpringItem.value :
                return
        else:
            if item != None and item1 != None:
                popMenu = QMenu()
                AddAction = QAction(u'Add', self)
                popMenu.addAction(AddAction)
                AddAction.triggered.connect(lambda: self.AddItem(0))
                # popMenu.triggered[QAction].connect(lambda: self.processtrigger(a="I am the changed Label",q=QAction(u'aaa', self)))
                popMenu.exec_(QCursor.pos())

    def setBottomItem(self,middleItem,count,name,idList):
            for j in range(count):
                bottomItem = QTreeWidgetItem(TreeItemType.itemBottomItem.value)
                if middleItem.type()==272:
                    BoundaryList=model.msaModel.SpringBoundary.Bound[idList[j]]
                    BoundaryTranslate={0:'0'}
                    for jj in model.msaModel.SpringModel.ID:
                        BoundaryTranslate[jj]='S'+str(jj)
                    name=''
                    for k in range(6):
                        temp=BoundaryTranslate[BoundaryList[k]]+' ,'
                        name+=temp
                    name=name[:-1]
                    bottomItem.setText(0, f'[Node {idList[j]}]' + ' ' + name)
                elif middleItem.type() == 25:
                    BoundaryList=model.msaModel.Bound.Bound[idList[j]]
                    name=''
                    for k in range(6):
                        temp=str(BoundaryList[k])+' ,'
                        name+=temp
                    name=name[:-1]
                    bottomItem.setText(0, f'[Node {idList[j]}]' + ' ' + name)
                elif middleItem.type() == 26:
                    LoadList=model.msaModel.Load.LoadVector[idList[j]]
                    name=''
                    for k in range(6):
                        temp=str(LoadList[k])+' ,'
                        name+=temp
                    name=name[:-1]
                    bottomItem.setText(0, f'[Node {idList[j]}]' + ' ' + name)
                else:
                    bottomItem.setText(0, f'[{j + 1}]' + ' ' + name + ' ' + str(idList[j]))
                bottomItem.setFlags(self.itemFlags)
                bottomItem.setData(0, Qt.UserRole, idList[j])
                # bottomItem_Section.setCheckState(0,Qt.CheckState.Unchecked)
                middleItem.addChild(bottomItem)
                middleItem.setExpanded(True)

    def importDataToTree(self):
        try:
            topItem = self.InputW.topLevelItem(0)
            for i in range(topItem.childCount()):
                middleItem=topItem.child(i)
                for j in range(middleItem.childCount()):
                    bottomItem=middleItem.child(j)

            for i in range(topItem.childCount()):
                middleItem=topItem.child(i)
                if middleItem.type() == 21 :
                    self.setBottomItem(middleItem=middleItem,count=model.msaModel.Mat.Count,name="Material",idList=model.msaModel.Mat.ID)
                elif middleItem.type() == 22 :
                    self.setBottomItem(middleItem=middleItem, count=model.msaModel.Sect.Count, name="Section",idList=model.msaModel.Sect.ID)
                # elif middleItem.type() == 23 :
                #     self.setBottomItem(middleItem=middleItem, count=model.msaModel.Node.Count, name="Node",idList=model.msaModel.Node.ID)
                # elif middleItem.type() == 24 :
                #     self.setBottomItem(middleItem=middleItem, count=model.msaModel.Member.Count, name="Member",idList=model.msaModel.Member.ID)
                elif middleItem.type() == 25 :
                    self.setBottomItem(middleItem=middleItem, count=model.msaModel.Bound.Count, name="Node",idList=model.msaModel.Bound.NodeID)
                elif middleItem.type() == 26 :
                    self.setBottomItem(middleItem=middleItem, count=model.msaModel.Load.Count, name="Node",idList=model.msaModel.Load.NodeID)
                elif middleItem.type() == 27 :
                    springModelItem=middleItem.child(0)
                    self.setBottomItem(middleItem=springModelItem, count=model.msaModel.SpringModel.Count, name="Spring Model",idList=model.msaModel.SpringModel.ID)
                    springBoundaryItem=middleItem.child(1)
                    self.setBottomItem(middleItem=springBoundaryItem, count=model.msaModel.SpringBoundary.Count, name="Spring Boundary",idList=model.msaModel.SpringBoundary.NodeID)

        except:
            traceback.print_exc()

    def importDataToNodeTable(self):
        try:
            self.nodeTable.verticalHeader().hide()

            self.nodeTable.setColumnWidth(0,100)
            nodeIDList=model.msaModel.Node.ID
            self.nodeTable.setRowCount(0)
            self.nodeTable.setRowCount(model.msaModel.Node.Count)
            for i in range(model.msaModel.Node.Count):
                for j in range(4):
                    Item = QTableWidgetItem('')
                    Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.nodeTable.setItem(i, j, Item)
                    if j == 0:
                        Item.setText(str(model.msaModel.Node.ID[i]))
                    elif j == 1:
                        Item.setText(str(model.msaModel.Node.x[nodeIDList[i]]))
                    elif j == 2:
                        Item.setText(str(model.msaModel.Node.y[nodeIDList[i]]))
                    elif j == 3:
                        Item.setText(str(model.msaModel.Node.z[nodeIDList[i]]))
            # self.nodeTable.resizeColumnsToContents()
            # self.nodeTable.resizeRowsToContents()
            self.nodeTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except:
            traceback.print_exc()

    def importDataToMemberTable(self):
        try:
            self.memberTable.verticalHeader().hide()
            self.memberTable.setColumnWidth(0,100)
            memberIDList=model.msaModel.Member.ID
            self.memberTable.setRowCount(0)
            self.memberTable.setRowCount(model.msaModel.Member.Count)
            for i in range(model.msaModel.Member.Count):
                for j in range(4):
                    Item = QTableWidgetItem('')
                    Item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.memberTable.setItem(i, j, Item)
                    if j == 0:
                        Item.setText(str(model.msaModel.Member.ID[i]))
                    elif j == 1:
                        Item.setText(str(model.msaModel.Member.NodeI[memberIDList[i]]))
                    elif j == 2:
                        Item.setText(str(model.msaModel.Member.NodeJ[memberIDList[i]]))
                    elif j == 3:
                        Item.setText(str(model.msaModel.Member.SectionID[memberIDList[i]]))

            # self.memberTable.resizeColumnsToContents()
            # self.memberTable.resizeRowsToContents()
            self.memberTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
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
            currentRow = self.nodeTable.currentRow()
            id = int(self.nodeTable.item(currentRow, 0).text())
            ConcreteDetailUi = NodeDialog(self, id)
            # ConcreteDetailUi.SendMaterialsSignal.connect(self.get_Materials_data)
            ConcreteDetailUi.exec()
        elif tabIndex == 2:
            currentRow = self.memberTable.currentRow()
            id = int(self.memberTable.item(currentRow, 0).text())
            ConcreteDetailUi = MemberDialog(self, id)
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
                        model.msaModel.Mat.Remove(id)
                    elif parentItem.type()==22:
                        model.msaModel.Sect.Remove(id)
                    # elif parentItem.type()==23:
                    #     model.msaModel.Node.Remove(id)
                    # elif parentItem.type()==24:
                    #     model.msaModel.Member.Remove(id)
                    elif parentItem.type()==25:
                        model.msaModel.Bound.Remove(id)
                    elif parentItem.type()==26:
                        model.msaModel.Load.Remove(id)
                    elif parentItem.type() == 272:
                        model.msaModel.SpringBoundary.Remove(id)
                    elif parentItem.type() == 271:
                        model.msaModel.SpringModel.Remove(id)
                    # elif parentItem.type()==27:
                    #     model.msaModel.Member.Remove(id)
                    parentItem.removeChild(item)
                    self.ResetTreeAndTable()
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
                        model.msaModel.Node.Remove(id)
                        self.ResetTreeAndTable()
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
                            model.msaModel.Member.Remove(id)
                            self.ResetTreeAndTable()
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
                self.ResetTreeAndTable()
            elif tabIndex == 1:
                currentRow = self.nodeTable.currentRow()
                # id = int(self.nodeTable.item(currentRow, 0).text())
                Ui = NodeAddDialog(self)
                Ui.exec()
                self.ResetTreeAndTable()
            elif tabIndex == 2:
                currentRow = self.memberTable.currentRow()
                # id = int(self.memberTable.item(currentRow, 0).text())
                Ui = MemberAddDialog(self)
                Ui.exec()
                self.ResetTreeAndTable()
        except:
            traceback.print_exc()

    def DelAllBottomItem(self):
        try:
            topItem = self.InputW.topLevelItem(0)
            for i in range(topItem.childCount()):
                    middleItem=topItem.child(i)
                    itemList = []
                    if middleItem.type()==27:
                        for j in range(middleItem.childCount()):
                            springMiddleItem=middleItem.child(j)
                            for k in range(springMiddleItem.childCount()):
                                bottomItem = springMiddleItem.child(k)
                                itemList.append(bottomItem)
                            for k in itemList:
                                springMiddleItem.removeChild(k)
                    else:
                        for j in range(middleItem.childCount()):
                            bottomItem = middleItem.child(j)
                            itemList.append(bottomItem)
                        for k in itemList:
                            middleItem.removeChild(k)
        except:
            traceback.print_exc()

    def ResetTreeAndTable(self):
        self.DelAllBottomItem()
        self.importDataToTree()
        self.memberTable.setRowCount(0)
        self.importDataToMemberTable()
        self.nodeTable.setRowCount(0)
        self.importDataToNodeTable()

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
        self.setWindowTitle(_translate("MainWindow", "Mastan3 - Python-based Frame Analysis Software"))
        # self.RunButton.setText(_translate("MainWindow", "Run"))
        # self.PlotButton.setText(_translate("MainWindow", "Plot"))
        # self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuGeometry.setTitle(_translate("MainWindow", "Geometry"))
        self.menuProperties.setTitle(_translate("MainWindow", "Properties"))
        self.menuConditions.setTitle(_translate("MainWindow", "Conditions"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuResults.setTitle(_translate("MainWindow", "Results"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTree), _translate("MainWindow", "Model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNode), _translate("MainWindow", "Node"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMember), _translate("MainWindow", "Member"))

    def VisualizeModel(self):
        SlotFuncInMainWindow.VisualizeModel(self)

    def NewFile(self):
        SlotFuncInMainWindow.NewFile(self)
        self.ResetTreeAndTable()
        # self.importDataToTree()
        # self.importDataToNodeTable()
        # self.importDataToMemberTable()
    def OpenFile(self):
        SlotFuncInMainWindow.OpenFile(self)
        self.ResetTreeAndTable()
        self.VisualizeModel()
        # self.importDataToTree()
        # self.importDataToNodeTable()
        # self.importDataToMemberTable()
    def SaveFile(self):
        SlotFuncInMainWindow.SaveFile(self)
    def SaveAsFile(self):
        SlotFuncInMainWindow.SaveAsFile(self)
    def Run(self):
        Ui = RunShowDialog(self)
        Ui.exec()
        SlotFuncInMainWindow.UpdateOutputW(self)
        # SlotFuncInMainWindow.Run(self)
