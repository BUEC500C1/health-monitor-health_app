# health-monitor-health_app
health-monitor-health_app created by GitHub Classroom
This is repository to hold the Health Monitoring Unity Project

The repository contains multiple modules developed independently. 


## Sensors:
Author: Lijunwei

Description: 
  In our proect, we do not use real sensor to test our project. Therefore, simulation file will replace actual sensor as input. 

-- Input
    sensor_pulse.cvs
    sensor_blood_pressure.cvs
    sensor_blood_oxygen.cvs

-- Output
    
## Display:

Author:Jingyi Li

Description: This parts will collect all the information from several parts and show in the screen. When an Alert happened, it will show in the screen with a special notice.

-- Input: setting, data inputs (updated sec by sec)

-- Output: graphs and numbers for blood pressure, heart rate, blood Oxygen levels, and Alert.

## Storage:

Author: Zhenfei Yu

Description: a database which stores data from processor and output to AI prediction module

-- Input: data handled by processor

-- Output: database for use in AI training

## Vitals:

Author: Danny

Description: 

-- Input

-- Output

## Processor:

Author: Steven

Description: 

-- Input

-- Output

## Settings:

Author: Jenny

Description: 

-- Input

-- Output

## Processor:

Author: Dingjun Bian

Description:

-- Input: Recieve the real time data of multiple sensors and process the data.Send the processed data to database for
storage. Check whether it is within normal range, send signal to alert if we detect something abnormal.

-- Output:transfer the processed data to database, send data to  alert

## Alert:

Author: Shiyang Hu

Description: In case of the alert failed which could cause vital result, the alert module should include several alert functions. These functions should be the same which are all received same data from processor separately and then judge these data wether beyond the threshold once the data beyond the threshold the function will generate an alert signal. Once one of these functions have generated signal, the module will output this signal immediately.

-- Input: The data from processor.


-- Output: Alert signal or nothing.
