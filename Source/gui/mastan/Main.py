# External library
import sys
from PySide6.QtWidgets import QApplication
# Internal library
from gui.mastan.view.MainWindowUI import MainWindow

# ================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Mastan3")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())