import time
import sys
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2 import QtWidgets, QtGui

from typing import Callable
import src.labs.lab3.sorts as sort
from src.labs.lab3.Ui_window import Ui_MainWindow

SortFunc = Callable[[list[sort.TNum]], list[sort.TNum]]


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnSave.triggered.connect(self.save)
        self.btnLoad.triggered.connect(self.load)
        self.btnBubble.triggered.connect(self.bubble)
        self.btnSelection.triggered.connect(self.selection)
        self.btnQuick.triggered.connect(self.quick)

    def save(self) -> None:
        path = QFileDialog().getSaveFileName()[0]
        if path:
            open(path).write(self.tbOutput.toPlainText())

    def load(self) -> None:
        path = QFileDialog().getOpenFileName()[0]
        if path:
            self.tbInput.setPlainText(open(path).read())

    def sorting(self, func: SortFunc) -> None:
        nums = self.parse_list(self.tbInput.toPlainText())
        start = time.time()
        nums = func(nums)
        stop = time.time()
        self.statusbar.showMessage(f"{stop - start} секунд")
        self.tbOutput.setPlainText(self.list_str(nums))

    def bubble(self) -> None:
        self.sorting(sort.bubble)

    def selection(self) -> None:
        self.sorting(sort.selection)

    def quick(self) -> None:
        self.sorting(sort.quick)

    def parse_list(self, text: str) -> list[float]:
        return [float(w.strip()) for w in text.split(',')]

    def list_str(self, nums: list[float]) -> str:
        return ",".join([str(x) for x in nums])


def run() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
