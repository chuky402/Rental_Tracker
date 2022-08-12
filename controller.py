from PyQt5.QtWidgets import *
from view import Ui_MainWindow
from tinydb import *
import ast


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
        """

        :param address:
        :param tenants:
        :param pet:
        :param rent:
        :param note:
        :param number_id:
        :return:
        """
        db.insert({'ID': number_id, 'address': address, 'Tenants': tenants, 'pet': pet, 'rent': rent, 'notes': note})

    def add(self):
        """

        :return:
        """
        address = self.input_address.text()
        tenants = self.number_tenants.text()
        if self.option_pet_yes.isChecked():
            pet = 'yes'
        elif self.option_pet_no.isChecked():
            pet = 'no'
        rent = self.combo_rent.currentText()
        note = self.tenant_notes.toPlainText()
        number_id = self.id_number.text()
        search = self.id_number.text()
        result = str(db.search(Query().ID == search))
        print(result[1:-1] + 'result')
        db.remove(where('ID') == number_id)

        self.insert(address, tenants, pet, rent, note, number_id)

    def search(self):
        """

        :return:
        """
        search = self.id_number.text()
        result = str(db.search(Query().ID == search))
        print(result[1:-1] + 'result')
        data = result[1:-1]
        print(data)
        res = ast.literal_eval(data)
        print(str(res) + 'res')
        rent = res['rent']
        address = res['address']
        tenants = res['Tenants']
        pet = res['pet']
        notes = res['notes']
        number_id = res['ID']

        self.id_number.setValue(0 if number_id is None else int(number_id))
        self.combo_rent.setCurrentText('$0/Month' if rent is None else rent)
        self.input_address.setText('No Address listed' if address is None else address)
        self.number_tenants.setValue(0 if tenants is None else int(tenants))
        if pet == 'yes':
            self.option_pet_yes.setChecked(True)
        elif pet == 'no':
            self.option_pet_no.setChecked(True)
        else:
            self.option_pet_no.setChecked(False)
        self.tenant_notes.setText('Invalid Tenant ID Number' if notes is None else notes)
