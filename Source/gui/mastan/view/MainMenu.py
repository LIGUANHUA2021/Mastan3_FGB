# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
import gui.mastan.view.MainMenuAction as MainMenuAction

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1139, 100)
        Form.setMinimumSize(QtCore.QSize(0, 100))
        Form.setMaximumSize(QtCore.QSize(16777215, 100))
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabProperties = QtWidgets.QTabWidget(Form)
        self.tabProperties.setStyleSheet("")
        self.tabProperties.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabProperties.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabProperties.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tabProperties.setObjectName("tabProperties")
        self.tabHome = QtWidgets.QWidget()
        self.tabHome.setObjectName("tabHome")
        self.toolButton = QtWidgets.QToolButton(self.tabHome)
        self.toolButton.setGeometry(QtCore.QRect(2, 3, 39, 65))
        self.toolButton.setMaximumSize(QtCore.QSize(40, 100))
        self.toolButton.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.toolButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resouces/img/new-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(36, 36))
        self.toolButton.setCheckable(False)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.openButton = QtWidgets.QToolButton(self.tabHome)
        self.openButton.setGeometry(QtCore.QRect(45, 3, 39, 65))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resouces/img/opon-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/Icons/opon-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.openButton.setIcon(icon1)
        self.openButton.setIconSize(QtCore.QSize(36, 36))
        self.openButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.openButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.openButton.setAutoRaise(True)
        self.openButton.setObjectName("openButton")
        # clicked action
        self.openButton.clicked.connect(MainMenuAction.openFileAction)
        #


        self.toolButton_3 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_3.setGeometry(QtCore.QRect(131, 3, 70, 20))
        self.toolButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resouces/img/save-as-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_4.setGeometry(QtCore.QRect(88, 3, 39, 65))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resouces/img/save-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_4.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_5.setGeometry(QtCore.QRect(131, 26, 70, 20))
        self.toolButton_5.setMaximumSize(QtCore.QSize(100, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../resouces/img/export-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_6.setGeometry(QtCore.QRect(131, 48, 70, 20))
        self.toolButton_6.setMaximumSize(QtCore.QSize(100, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../resouces/img/close-file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.line = QtWidgets.QFrame(self.tabHome)
        self.line.setGeometry(QtCore.QRect(206, 5, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.toolButton_7 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_7.setGeometry(QtCore.QRect(211, 3, 60, 65))
        self.toolButton_7.setMaximumSize(QtCore.QSize(60, 100))
        self.toolButton_7.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.toolButton_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.toolButton_7.setAutoFillBackground(False)
        self.toolButton_7.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../resouces/img/Fit-to-Screen.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_7.setCheckable(False)
        self.toolButton_7.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_7.setAutoRaise(True)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_8 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_8.setGeometry(QtCore.QRect(275, 3, 60, 65))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../resouces/img/xyz-axis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_8.setIcon(icon7)
        self.toolButton_8.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_8.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_8.setAutoRaise(True)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_9.setGeometry(QtCore.QRect(339, 48, 110, 20))
        self.toolButton_9.setMaximumSize(QtCore.QSize(120, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../resouces/img/yz-view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_9.setIcon(icon8)
        self.toolButton_9.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_9.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_9.setAutoRaise(True)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_10.setGeometry(QtCore.QRect(339, 26, 110, 20))
        self.toolButton_10.setMaximumSize(QtCore.QSize(120, 16777215))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../resouces/img/xz-view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_10.setIcon(icon9)
        self.toolButton_10.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_10.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_10.setAutoRaise(True)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.tabHome)
        self.toolButton_11.setGeometry(QtCore.QRect(339, 3, 110, 20))
        self.toolButton_11.setMaximumSize(QtCore.QSize(120, 16777215))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../resouces/img/xy-view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_11.setIcon(icon10)
        self.toolButton_11.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_11.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_11.setAutoRaise(True)
        self.toolButton_11.setObjectName("toolButton_11")
        self.line_2 = QtWidgets.QFrame(self.tabHome)
        self.line_2.setGeometry(QtCore.QRect(454, 5, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox.setGeometry(QtCore.QRect(460, 3, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_2.setGeometry(QtCore.QRect(460, 25, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_3.setGeometry(QtCore.QRect(460, 47, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_4.setGeometry(QtCore.QRect(544, 25, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_5.setGeometry(QtCore.QRect(544, 3, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_6.setGeometry(QtCore.QRect(544, 47, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_7.setGeometry(QtCore.QRect(679, 3, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setChecked(False)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_8.setGeometry(QtCore.QRect(679, 47, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tabHome)
        self.checkBox_9.setEnabled(True)
        self.checkBox_9.setGeometry(QtCore.QRect(679, 25, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.line_3 = QtWidgets.QFrame(self.tabHome)
        self.line_3.setGeometry(QtCore.QRect(820, 5, 3, 60))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.statusEdit = QtWidgets.QTextEdit(self.tabHome)
        self.statusEdit.setGeometry(QtCore.QRect(820, 5, 200, 60))
        self.statusEdit.setObjectName("statusEdit")
        self.line_4 = QtWidgets.QFrame(self.tabHome)
        self.line_4.setGeometry(QtCore.QRect(1020, 5, 4, 60))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabProperties.addTab(self.tabHome, "")
        self.tabView_2 = QtWidgets.QWidget()
        self.tabView_2.setObjectName("tabView_2")
        self.tabProperties.addTab(self.tabView_2, "")
        self.tabGeometry = QtWidgets.QWidget()
        self.tabGeometry.setObjectName("tabGeometry")
        self.NodeAddButton = QtWidgets.QToolButton(self.tabGeometry)
        self.NodeAddButton.setGeometry(QtCore.QRect(1, 1, 40, 62))
        self.NodeAddButton.setMaximumSize(QtCore.QSize(40, 100))
        self.NodeAddButton.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.NodeAddButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.NodeAddButton.setAutoFillBackground(False)
        self.NodeAddButton.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../resouces/img/Node.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.NodeAddButton.setIcon(icon11)
        self.NodeAddButton.setIconSize(QtCore.QSize(35, 38))
        self.NodeAddButton.setCheckable(False)
        self.NodeAddButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.NodeAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.NodeAddButton.setAutoRaise(True)
        self.NodeAddButton.setObjectName("NodeAddButton")
        self.MemberAddButton = QtWidgets.QToolButton(self.tabGeometry)
        self.MemberAddButton.setGeometry(QtCore.QRect(50, 1, 50, 62))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MemberAddButton.sizePolicy().hasHeightForWidth())
        self.MemberAddButton.setSizePolicy(sizePolicy)
        self.MemberAddButton.setMinimumSize(QtCore.QSize(0, 0))
        self.MemberAddButton.setMaximumSize(QtCore.QSize(60, 100))
        self.MemberAddButton.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.MemberAddButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.MemberAddButton.setAutoFillBackground(False)
        self.MemberAddButton.setStyleSheet("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../resouces/img/addMember.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.MemberAddButton.setIcon(icon12)
        self.MemberAddButton.setIconSize(QtCore.QSize(39, 39))
        self.MemberAddButton.setCheckable(False)
        self.MemberAddButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.MemberAddButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.MemberAddButton.setAutoRaise(True)
        self.MemberAddButton.setObjectName("MemberAddButton")
        self.tabProperties.addTab(self.tabGeometry, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabProperties.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabProperties.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabProperties.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabProperties.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabProperties)

        self.retranslateUi(Form)
        self.tabProperties.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "New"))
        self.openButton.setText(_translate("Form", "Open"))
        self.toolButton_3.setText(_translate("Form", "Save as"))
        self.toolButton_4.setText(_translate("Form", "Save"))
        self.toolButton_5.setText(_translate("Form", "Export"))
        self.toolButton_6.setText(_translate("Form", "Close"))
        self.toolButton_7.setText(_translate("Form", "Fit Screen"))
        self.toolButton_8.setText(_translate("Form", "3D View"))
        self.toolButton_9.setText(_translate("Form", "Top View: y-z"))
        self.toolButton_10.setText(_translate("Form", "Side View: y-z"))
        self.toolButton_11.setText(_translate("Form", "Front View: x-y "))
        self.checkBox.setText(_translate("Form", "Axis"))
        self.checkBox_2.setText(_translate("Form", "Node I#s"))
        self.checkBox_3.setText(_translate("Form", "Element #s"))
        self.checkBox_4.setText(_translate("Form", "Element Connections"))
        self.checkBox_5.setText(_translate("Form", "Element Local axes"))
        self.checkBox_6.setText(_translate("Form", "Element Forces"))
        self.checkBox_7.setText(_translate("Form", "Nodal Loads"))
        self.checkBox_8.setText(_translate("Form", "Nodal Settlements"))
        self.checkBox_9.setText(_translate("Form", "Nodal Fixities"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tabHome), _translate("Form", "Home"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tabView_2), _translate("Form", "View"))
        self.NodeAddButton.setText(_translate("Form", "Node"))
        self.MemberAddButton.setText(_translate("Form", "Member"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tabGeometry), _translate("Form", "Geometry"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tab_2), _translate("Form", "Properties"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tab), _translate("Form", "Conditions"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tab_3), _translate("Form", "Analysis"))
        self.tabProperties.setTabText(self.tabProperties.indexOf(self.tab_4), _translate("Form", "Results"))
