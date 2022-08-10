from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import csv


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def add(self):
        name = self.name_input.text()

