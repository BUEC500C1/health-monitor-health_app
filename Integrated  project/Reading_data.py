import threading
import csv
import time
import sys 
import trace 

class thread_with_trace(threading.Thread): 
  def __init__(self, *args, **keywords): 
    threading.Thread.__init__(self, *args, **keywords) 
    self.killed = False
  
  def start(self): 
    self.__run_backup = self.run 
    self.run = self.__run       
    threading.Thread.start(self) 
  
  def __run(self): 
    sys.settrace(self.globaltrace) 
    self.__run_backup() 
    self.run = self.__run_backup 
  
  def globaltrace(self, frame, event, arg): 
    if event == 'call': 
      return self.localtrace 
    else: 
      return None
  
  def localtrace(self, frame, event, arg): 
    if self.killed: 
      if event == 'line': 
        raise SystemExit() 
    return self.localtrace 
  
  def kill(self): 
    self.killed = True

def read_file(file_name):
    Blood_Pressure_mmHg =[]
    Blood_Oxygen_mmHg = []
    Pulse_BPM =[]
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader: 
            if row:
                if row[0] == 'Blood_Pressure_mmHg':
                    Blood_Pressure_mmHg = row

                elif row[0] == 'Blood_Oxygen_mmHg':
                    Blood_Oxygen_mmHg = row

                elif row[0] == 'Pulse_BPM':
                    Pulse_BPM = row

    return Blood_Pressure_mmHg, Blood_Oxygen_mmHg, Pulse_BPM

def sensor_get(data, time_interval):
    Blood_pressure, Blood_Oxygen, Pulse = read_file('example_data.csv')
    for i in range(1,len(Blood_pressure)):
        data[0] = Blood_pressure[i]
        data[1] = Blood_Oxygen[i]
        data[2] = Pulse[i] 
        time.sleep(time_interval)

def print_value(data):
        print(data)
        
if __name__ == '__main__':
    data =[1,2,3]
    t1 = thread_with_trace(target=sensor_get, args=(data, 0.5))
    t1.start()
    for i in range(20) :
        t2 = thread_with_trace(target=print_value, args=(data,))
        t2.start()
        time.sleep(0.5)
    t1.kill() 
    t1.join()
    t2.kill() 
    t2.join()
