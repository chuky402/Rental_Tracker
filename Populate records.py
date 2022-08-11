import csv

with open('records.csv', 'a', newline='') as file:
    header = ['id_number', 'rent', 'address', 'tenants', 'pet', 'notes']
    writer = csv.DictWriter(file, fieldnames=header)
    for i in range(25):
        writer.writerow({'id_number': i+1, 'rent': "$0/Month", 'address': "", 'tenants': 0, 'pet': "no", 'notes': ""})