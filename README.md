# health-monitor-health_app
health-monitor-health_app created by GitHub Classroom
This is repository to hold the Health Monitoring Unity Project

The repository contains multiple modules developed independently. 

## Sensors:
Author: Lijunwei

Description: 

-- Input

-- Output

## Display:

Author: Lijunwei

Description: 

-- Input: setting, data inputs (updated sec by sec)

-- Outpu: graphs + numbers for blood pressure, heart rate, oxygen concentration in pyqt gUI


## Storage:

Author: Zhenfei Yu

Description: a database which accepts data from processor and output to AI prediction module

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

Description: Recieve the real time data of multiple sensors and process the data.Send the processed data to database for

storage. Check whether it is within normal range, send signal to alert if we detect something abnormal.


-- Input:data of pulse ,blood pressure and blood oxygen.

-- Output:transfer the processed data to database, send data to  alert
