from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import csv


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_add.clicked.connect(lambda: self.add())

    def add(self):
        address = self.input_address.text()
        tenants = self.input_tenant.text()
        if self.option_pet_yes.isChecked():
            pet = 'yes'
        elif self.option_pet_no.isChecked():
            pet = 'no'
        rent = self.combo_rent.currentText()
        output = f'{tenants} live at {address}, Do pets live here, {pet} and their rent is {rent}'
        print(output)