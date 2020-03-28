import random
from datetime import datetime
import csv

health_data = {}

def increase(x,Seed):
    random.seed(Seed)
    return x+random.randrange(0,20)
def decrease(x, Seed):
    random.seed(Seed)
    return x+random.randrange(0,20)


def data_gene(key,floor, ciel, health_data):
    health_data[key] = []
    for i in range(100):
        random.seed(-i)
        parameter = random.randrange(floor, ciel)
        # randomly choose increase or decrease 
        random.seed(i)
        if random.randrange(0, 100)> 50:        
            for i in range (10):
                health_data[key].append(str(round(increase(parameter, i*100),2)))
        else:
            for i in range (10):
                health_data[key].append(str(round(decrease(parameter, i*100),2)))
     

def output_file(health_data):
    # file name: 
    file_name = 'example_data.csv'

    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in health_data: 
            row = [i]+ health_data[i] 
            csvwriter.writerow(row)

def main():
    #  generate blood pressure data. low to high range is 70-90 
    #  time interval 0.01s ----  total time 10s
    #  1000 datas
        data_gene("Blood_Pressure_mmHg", 70, 190, health_data)

    # generate Blood Oxygen data
        data_gene("Blood_Oxygen_mmHg", 75, 100, health_data)

    # generate Pulse data
        data_gene("Pulse_BPM", 60, 100, health_data)

    # output file
        output_file(health_data)


if __name__ =='__main__':
    main()
