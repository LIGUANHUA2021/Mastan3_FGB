from PySide6.QtWidgets import QMessageBox


def showMesbox(mw, content: str):
    mesBox = QMessageBox()
    mesBox.setWindowTitle('Information')
    # mesBox.setWindowIcon(QIcon('GUI/fengzhenxishu.ico'))
    mesBox.setText(content)
    mesBox.setIcon(mesBox.Icon.Warning)
    mesBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
    mesBox.addButton(mw.tr("Close"), QMessageBox.ButtonRole.NoRole)
    mesBox.exec()