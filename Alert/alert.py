from flask import Flask
from flask_restful import Resource, Apireqparse, abort

import functions as f
import csv
app = Flask(__name__)
api = Api(app)

oxy_standard = 60
systolic_standard = 140
dia_standard = 90
pul_standard = 80
database_temp = {}

def csv2dict(in_file,key,value):
    with open('database.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            database_temp[row[key]] = row[value]
    return database_temp


def abort_if_not_exist(index):
    if index not in database_temp:
        abort(404, message="Alert: index {} doesn't exist".format(index))

class User(Resource):
    def get(self, index):
        abort_if_not_exist(index)
        alert = f.Alert()
        oxygen = alert.get_oxygen()
        bp = alert.get_bp()
        pulse = alert.get_pulse()
        return {"oxygen": oxygen, "blood pressure": bp, "pulse": pulse}


class Alert():
    def __init__(self):
        pass

    def get_oxygen(self):
        oxy = database_temp.get('oxygen') #get data from database
        if oxy < oxy_standard: 
                print("Alert: Abnormal oxygen level !")
        return oxy

    def get_bp(self):
        bp = database_temp.get('blood pressure') 
        if bp > systolic_standard or bp < 80: 
            print("Alert: Abnormal oxygen level !")
        return bp

    def get_pulse(self):
        pulse = database_temp.get('pulse') 
        if pulse > pul_standard:
            print("Alert: Abnormal oxygen level !")
        return pulse

api.add_resource(Alert, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)