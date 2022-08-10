from PyQt5.QtWidgets import *
from view import Ui_MainWindow


class Controller(QMainWindow, Ui_MainWindow):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
