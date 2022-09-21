import sys
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2 import QtWidgets, QtGui

import src.labs.lab3.sorts as sort
from src.labs.lab3.Ui_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnSave.triggered.connect(self.save)
        self.btnLoad.triggered.connect(self.load)
        self.btnBubble.triggered.connect(self.bubble)
        self.btnSelection.triggered.connect(self.selection)
        self.btnSelection.triggered.connect(self.quick)

    def save(self) -> None:
        pass

    def load(self) -> None:
        path = QFileDialog().getOpenFileName()[0]
        if not path:
            return
        msgBox = QMessageBox()
        msgBox.setText(f"файл {path}")
        msgBox.exec()
        file = open(path).read()
        self.tbInput.setPlainText(file)

    def bubble(self) -> None:
        pass

    def selection(self) -> None:
        pass

    def quick(self) -> None:
        pass


def run() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
