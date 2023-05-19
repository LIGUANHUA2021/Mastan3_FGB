# External library
import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, Qt
from PySide6.QtCore import QTimer
# Internal library
import Configuration
from gui.msasect.ui.MainWindow import MainWindow
from gui.msasect.ui.Splashscreen import SplashScreen
# ================================================================


class MSASECT2APP(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('ui/ico/MSASect2.ico'))

        # Create and configure the splash screen
        # self.splash = SplashScreen('ui/Template/SplashScreen.png')
        # self.splash.show()

        # Set up the QTimer
        QTimer().singleShot(0, self.launch_main_window)  # Wait for 3 seconds
        #
        Configuration.basedir = os.path.dirname(__file__)

    def launch_main_window(self):
        # Close the splash screen and open the main window
        # self.splash.close()
        self.main = MainWindow()
        self.main.show()


if __name__ == '__main__':
    app = MSASECT2APP(sys.argv)
    sys.exit(app.exec())
