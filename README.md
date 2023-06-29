# AI Controlled Desktop Garden

## Introduction
This is a fun project that makes uses AI to monitor and control the Desktop Plant Garden.

Plants in the Desktop Garden is continously monitored on its environmental conditions like Moisture, UV light, Temperature, Ambient Light. The Desktop Garden also contains the controls for wattering the plant and controlled UV ray exposure. Now a AI is introduced into this system that uses the data sensed by these sensors from the garden and decides when and how much to water the plant and when to expose to the UV rays based on the plant health.

## System design
TBD

### Hardware design
TBD

## Technology Used
1. Front End: Grafana (for viewing the timeseries sensor data)
2. Backend: Python 3.11, Quart framework for service, hosted in Heroku
3. Hardware Controller: Raspberry Pi (at node) and relays
4. Sensors: Moisture Sensor, Temperature Sensor, UV sensor
5. Actuators: UV light, DC Motor
