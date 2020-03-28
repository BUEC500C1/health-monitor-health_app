import csv
import os
def Database(store):
    headers = ["blood_pressure","oxygen","pulse"]
    filepath = './database.csv'
    if (os.path.exists(filepath)):
        with open(filepath,'a+') as f:
            f_csv = csv.DictWriter(f, headers)
            for item in store:
                f_csv.writerow(item)
    else:
        with open(filepath,'a+') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            for item in store:
                f_csv.writerow(item)
    filename = './database'
    return filename



if __name__ == '__main__':
    store = [{'blood_pressure': 70, 'oxygen': 100, 'pulse':80}]
    Database(store)
    store = [{'blood_pressure': 0, 'oxygen': 90, 'pulse':70}]
    Database(store)
    store = [{'blood_pressure': 85, 'oxygen': 0, 'pulse':0}]
    Database(store)
    store = [{'blood_pressure': 140, 'oxygen': 80, 'pulse':50}]
    Database(store)
    store = [{'blood_pressure': 151, 'oxygen': 95, 'pulse':30}]
    Database(store)
    store = [{'blood_pressure': 180, 'oxygen': 60, 'pulse':3}]
    Database(store)
    store = [{'blood_pressure': 86, 'oxygen': 50, 'pulse':20}]
    Database(store)
    store = [{'blood_pressure': 70, 'oxygen': 73, 'pulse':100}]
    Database(store)
    store = [{'blood_pressure': 85, 'oxygen': 86, 'pulse':90}]
    Database(store)
    store = [{'blood_pressure': 74, 'oxygen': 92, 'pulse':6}]
    Database(store)
   