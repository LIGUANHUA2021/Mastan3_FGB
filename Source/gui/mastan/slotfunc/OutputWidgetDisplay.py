# This module contains the function we needed to display the information in OutputWidget
from PySide6.QtCore import QEventLoop, QTimer
from PySide6 import QtCore, QtGui, QtWidgets
import sys, json

class EmittingStr(QtCore.QObject):
        textWritten = QtCore.Signal(str)
        def write(self, text):
            self.textWritten.emit(str(text))
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()
def displayOWinf(OutputW):
    sys.stdout = EmittingStr()
    OutputW.OutputW.connect(sys.stdout, QtCore.SIGNAL("textWritten(QString)"))
    sys.stderr = EmittingStr()
    OutputW.OutputW.connect(sys.stderr, QtCore.SIGNAL("textWritten(QString)"))