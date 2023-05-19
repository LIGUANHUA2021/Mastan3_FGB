from PySide6.QtCore import QObject, Signal

class QtSignal(QObject):
    meshProgress_Signal = Signal(int)
    meshFinish_Signal = Signal()
    meshIter_Signal = Signal(int)
    meshText_Signal = Signal(str)
    SPCalProgress_Signal = Signal(int)
    SPCalFinish_Signal = Signal()

    def __init__(self):
        super().__init__()