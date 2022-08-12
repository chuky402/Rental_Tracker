from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from view import Ui_MainWindow
from tinydb import *

db = TinyDB('tenants.json')


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

    def insert(self, address, tenants, pet, rent, note, number_id):
        db.insert({'ID': number_id, 'address': address, 'Tenants': tenants, 'pet': pet, 'rent': rent, 'notes': note})

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
        if db.contains('ID' == number_id):
            db.update_multiple([
                ({'address': address}, where('ID') == number_id),
                ({'Tenants': tenants}, where('ID') == number_id),
                ({'pet': pet}, where('ID') == number_id),
                ({'rent': rent}, where('ID') == number_id),
                ({'notes': note}, where('ID') == number_id)
                ])
        else:
            self.insert(address, tenants, pet, rent, note, number_id)

    def search(self):
        user = Query()
        search = self.id_number.text()
        result = db.search('ID' == search)
        print(result)

        self.id_number.setValue(int(number_id))
        self.combo_rent.setCurrentText(rent)
        self.input_address.setText(address)
        self.number_tenants.setValue(int(tenants))
        if pet == 'yes':
            self.option_pet_yes.setChecked(True)
        elif pet == 'no':
            self.option_pet_no.setChecked(True)
        self.tenant_notes.setText(notes)
