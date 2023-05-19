import io
from PySide6.QtWidgets import QTextBrowser
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import QEvent, QCoreApplication


class CallableEvent(QEvent):
    def __init__(self, callback):
        super().__init__(QEvent.Type(QEvent.registerEventType()))
        self.callback = callback

    def execute(self):
        self.callback()


class ConsoleOutput(io.StringIO):
    def __init__(self, text_browser: QTextBrowser):
        super().__init__()
        self.text_browser = text_browser

    def write(self, text):
        # Insert plain text and move the cursor to the end using custom QEvent in the GUI thread
        QCoreApplication.postEvent(self.text_browser, CallableEvent(lambda: self.text_browser.insertPlainText(text)))
        QCoreApplication.postEvent(self.text_browser,
                                   CallableEvent(lambda: self.text_browser.moveCursor(QTextCursor.End)))
