# AI-Controlled Desktop Garden [Work in Progress]

## Introduction
This is a fun project that makes uses AI to monitor and control the Desktop Plant Garden.

Plants in the Desktop Garden are continuously monitored on its environmental conditions like Moisture, UV light, Temperature, and Ambient Light. The Desktop Garden also contains the controls for watering the plant and controlled UV ray exposure. Now an AI is introduced into this system that uses the data sensed by these sensors from the garden and decides when and how much to water the plant and when to expose it to the UV rays based on the plant's health.

## System design
![image](https://github.com/navinsubramani/ai-controlled-dektop-garden/assets/17029551/e8282de4-01c3-4401-9224-d49dd4b5a4b9)

### Hardware design
TBD

## Technology Used
1. Front End: Grafana (for viewing the timeseries sensor data)
2. Backend: Python 3.11, Quart framework for service, hosted in Heroku
3. Hardware Controller: Raspberry Pi (at node) and relays
4. Sensors: Moisture Sensor, Temperature Sensor, UV sensor
5. Actuators: UV light, DC Motor
