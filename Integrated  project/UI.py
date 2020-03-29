from UI import thread_with_trace, show_real_sensor_data
from Reading_data import sensor_get
from database import Database
import sys
import time

def store_data(data):
    while True :
        store = [{'blood_pressure': float(data[0]), 'oxygen': float(data[1]), 'pulse': float(data[0])}]
        Database(store)
        time.sleep(0.02)



def main():
    # declear data 
    data=['0','0','0']
    # connect to  sensors 
    t0 =  thread_with_trace(target=sensor_get, args=(data,0.015))
    t0.start()
### data is change everry 0.01s  ----- data = [Blood_pressure, Blood_Oxygen, Pulse ] string type 

### for example ['101', '93', '82']
## =====  put all process at here 


## data store 
    t1 = thread_with_trace (target= store_data, args=(data, ))
    t1.start()

# do alarm processing 






# show Data in UI 
    t2 = thread_with_trace(target = show_real_sensor_data,args= (data,))
    t2.start()

### data finished  here 
    
    t2.join() 

    t1.kill()
    t1.join()

    t0.kill() 
    t0.join()  
    
    print ('killed t1')
    sys.exit(0)

if __name__ == '__main__':
    main()
