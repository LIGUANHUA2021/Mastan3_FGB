# External library
from PySide6.QtWidgets import QApplication, QSplashScreen, QProgressBar, QLabel
from PySide6.QtGui import QPixmap, QPainter, QFont, QPalette, QColor, QBrush, Qt, QImage, QMovie, QIcon
from PySide6.QtCore import QPointF, Qt, QTimer
import PySide6.QtCore
import time
# Internal library
import gui.msasect.base.Setting as Setting

class SplashScreen():
    def __init__(self, splash_image_path):
        self.splash_pix = QPixmap(splash_image_path)
        self.splash_pix.setDevicePixelRatio(1.5)
        self.splash = QSplashScreen(self.splash_pix, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.splash.setAttribute(Qt.WA_TranslucentBackground, True)

        self.loading_status = QLabel(self.splash)
        self.loading_status.setAlignment(Qt.AlignLeft)
        self.loading_status.setFixedSize(200, 30)
        self.loading_status.move(230, 140)
        self.loading_status.setStyleSheet("color: #ffffff; font-size: 10pt; font-family: Segoe UI;")
        self.loading_status.setText("Initializing ...")
        self.circle = [QPixmap("ui/ico/Circle-{:02d}.png".format(i)) for i in range(1, 25)]
        for i in range(24):
            self.circle[i].scaled(16, 16, Qt.KeepAspectRatio)
            self.circle[i].setDevicePixelRatio(2)
        self.label = QLabel(self.splash)
        self.label.setPixmap(self.circle[0])
        # Set the QLabel geometry as per your needs (x position, y position, width, height)
        self.label.setGeometry(205, 140, 16, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.anim_update)
        self.frame = 0
        QTimer.singleShot(500, lambda: self.loading_status.setText("Loading components ..."))
        QTimer.singleShot(1000, lambda: self.loading_status.setText("Displaying GUI ..."))

    def anim_update(self):
        if self.frame <= 22:
            self.frame += 1
            self.label.setPixmap(self.circle[self.frame])
        else:
            self.frame = 0
            self.label.setPixmap(self.circle[self.frame])

    def show(self):
        self.splash.show()
        self.timer.start(40)

    def close(self):
        self.splash.close()
        self.timer.stop()
