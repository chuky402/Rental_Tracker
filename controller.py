from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from view import Ui_MainWindow
import csv


class Controller(QMainWindow, Ui_MainWindow):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_add.clicked.connect(lambda: self.add())
        self.button_search.clicked.connect(lambda: self.search())

    def add(self):
        address = self.input_address.text()
        tenants = self.number_tenants.text()
        if self.option_pet_yes.isChecked():
            pet = 'yes'
        elif self.option_pet_no.isChecked():
            pet = 'no'
        rent = self.combo_rent.currentText()
        note = self.tenant_notes.toPlainText()
        number_id = self.id_number.text()

        with open('records.csv', 'a', newline='') as file:
            val = self.id_number.text()
            for row in file:
                if row[0] == val:
                    pass
                else:
                    header = ['id_number', 'rent', 'address', 'tenants', 'pet', 'notes']
                    writer = csv.DictWriter(file, fieldnames=header)
                    writer.writerow(
                        {'id_number': number_id, 'rent': rent, 'address': address, 'tenants': tenants, 'pet': pet,
                         'notes': note})
                    file.close()

    def search(self):
        val = self.id_number.text()
        with open('records.csv', 'r') as file2:
            reader = csv.reader(file2)
            for row in reader:
                if row[0] == val:
                    number_id = row[0]
                    rent = row[1]
                    address = row[2]
                    tenants = row[3]
                    pet = row[4]
                    notes = row[5]


        self.id_number.setValue(int(number_id))
        self.combo_rent.setCurrentText(rent)
        self.input_address.setText(address)
        self.number_tenants.setValue(int(tenants))
        if pet == 'yes':
            self.option_pet_yes.setChecked(True)
        elif pet == 'no':
            self.option_pet_no.setChecked(True)
        self.tenant_notes.setText(notes)
        file2.close()
