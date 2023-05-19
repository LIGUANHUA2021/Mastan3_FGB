from PySide6.QtWidgets import QMessageBox

def NewshowMesbox(mw):
    #Newmesbox = QMessageBox()
    # QMessageBox.layout()
    # QMessageBox.
    # reply = QMessageBox.question(mw, 'New', 'Are you sure you want to start over?<br>(unsaved data will be lost)',
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    reply = QMessageBox.question(mw, 'New', 'Are you sure you want to start over?<br>(unsaved data will be lost)',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    if reply == QMessageBox.Yes:
        flag = 1
    else:
        flag = 0
    return flag

    # Newmesbox.exec()

    # mesBox = QMessageBox()
    # mesBox.setWindowTitle('Warning')
    # # mesBox.setWindowIcon(QIcon('GUI/fengzhenxishu.ico'))
    # mesBox.setText(content)
    # mesBox.setIcon(mesBox.Icon.Warning)
    # mesBox.setStandardButtons(QMessageBox.StandardButton.NoButton)
    # mesBox.addButton(mw.tr("Close") ,QMessageBox.ButtonRole.NoRole)
    # mesBox.exec()