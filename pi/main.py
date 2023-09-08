import time
import datetime

from sensorTemperatureAcquisition import getTemperatureValue
from sensorMoistureAcquisition import getMoistureValue
from sensorLightSensor import getUVsensorValue, getALsensorValue

from actuatorMotorControl import TurnOnMotor

from requestsWebService import post_sensor_data, get_motor_action

# Configure the Flask Server URL
URL = 'https://desktop-garden-6550e8a69600.herokuapp.com'

# Get the current timestamp
MEASUREMENT_TIME_INTERVAL = 10
startTimeStamp = time.time()
currentTimeString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    elapsedTime = time.time() - startTimeStamp
    
    if elapsedTime >= MEASUREMENT_TIME_INTERVAL:
        print(currentTimeString)
        startTimeStamp = time.time()
        startTimeString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            t = getTemperatureValue()
            m1 = getMoistureValue(sensorIndex = 1)
            m2 = getMoistureValue(sensorIndex = 2)
            m3 = getMoistureValue(sensorIndex = 3)
            uvs = getUVsensorValue()
            als = getALsensorValue()
            
            # Publish to the Server
            post_sensor_data(URL, currentTimeString, t["result"], m1["result"], m2["result"], m3["result"], uvs["result"], als["result"])
            
            motor_data = get_motor_action(URL)
            print(motor_data)
            if motor_data["action"]:
                TurnOnMotor(index = motor_data["id"], upTime = motor_data["upTime"])
        except Exception:
            print("Error in main code")
            
        currentTimeString = startTimeString
    
    else:
        #print(elapsedTime)
        time.sleep(2)
