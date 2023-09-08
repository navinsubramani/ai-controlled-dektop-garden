# Import Libraries
import os
import glob
import time
import RPi.GPIO as GPIO

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MOTOR_GPIB_LIST = [17, 17, 27, 17]

# Turn OFF all motors to while starting
for index in MOTOR_GPIB_LIST:
    Motor_GPIB = index
    GPIO.setup(Motor_GPIB,GPIO.OUT)
    GPIO.output(Motor_GPIB,GPIO.LOW)

def TurnOnMotor(index = 1, upTime = 10):
    Motor_GPIB = MOTOR_GPIB_LIST[index]
    GPIO.setup(Motor_GPIB,GPIO.OUT)
    GPIO.output(Motor_GPIB,GPIO.HIGH)
    time.sleep(upTime)
    GPIO.output(Motor_GPIB,GPIO.LOW)


if __name__ == '__main__':
    TurnOnMotor(1, 5)