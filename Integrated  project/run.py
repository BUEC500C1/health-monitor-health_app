from UI import thread_with_trace, show_real_sensor_data
from Reading_data import sensor_get
import sys

def main():
    # declear data 
    data=['0','0','0']
    # connect to  sensors 
    t1 =  thread_with_trace(target=sensor_get, args=(data,0.01))
    t1.start()
### data is change everry 0.01s  ----- data = [Blood_pressure, Blood_Oxygen, Pulse ] string type 

### for example ['101', '93', '82']
## =====  put all process at here 

# show Data in UI 
    t2 = thread_with_trace(target = show_real_sensor_data,args= (data,))
    t2.start()

# do alarm processing 



### data finished  here 
    
    t2.join() 
    t1.kill() 
    t1.join()  
    print ('killed t1')
    sys.exit(0)

if __name__ == '__main__':
    main()
