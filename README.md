# AI-Controlled Desktop Garden [Work in Progress]

## Introduction
This is a fun project that makes uses AI to monitor and control the Desktop Plant Garden.

Plants in the Desktop Garden are continuously monitored on its environmental conditions like Moisture, UV light, Temperature, and Ambient Light. The Desktop Garden also contains the controls for watering the plant and controlled UV ray exposure. Now an AI is introduced into this system that uses the data sensed by these sensors from the garden and decides when and how much to water the plant and when to expose it to the UV rays based on the plant's health.

This [Blog in Boring Engineer]() contains a demo video of the existing system.

## System design
![image](https://github.com/navinsubramani/ai-controlled-dektop-garden/assets/17029551/e8282de4-01c3-4401-9224-d49dd4b5a4b9)

### Hardware Components at Edge
1. 1 x Raspberry Pi 3B+
2. [1 x 4 Channel 5V Relay Module](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
3. [4 x Mini Water Pump](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
4. [1 x 4M Vinyl Tubing (Material: PVC)](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
5. [4 x Capacitive Soil Moisture Sensor (TL555C)](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
6. [1 x UV & Ambient Light Sensor (LTR390)](https://www.amazon.com/gp/product/B09FDGTKLX/ref=ppx_yo_dt_b_asin_title_o09_s01?ie=UTF8&psc=1)
7. [1 x DS18B20 Temperature Sensor](https://www.amazon.com/Hilitchi-DS18B20-Waterproof-Temperature-Sensors/dp/B018KFX5X0?th=1)
8. [1 x MCP221A ADC to convert moisture sensor analog to digital values](https://www.adafruit.com/product/4471)
9. [1 x DOMMIA Grow Light](https://www.amazon.com/dp/B07TRKXX9D?ref=ppx_yo2ov_dt_b_product_details&th=1)
10. [1 x myTouchSmart Indoor Digital Timer Switch](https://www.homedepot.com/p/myTouchSmart-Indoor-Digital-24-Hour-Fashion-Timer-with-Cloth-Cover-2-Settings-1-Polarized-Outlet-66985/324058579)
11. Prototype PCBs, Male-Male, Male-Female Wires, Solder Kit as required

### Hardware Connections at Edge
![image](https://github.com/navinsubramani/ai-controlled-dektop-garden/assets/17029551/f2340923-2657-41bb-8fe8-96c6e20f3967)

1. The Sensor with digital output is connected to Raspberry Pi directly through I2C or One Wire pins.
2. The analog sensor (Moisture) is converted into digital using ADC using MCP221A and then connected to the USB interface of Pi.
3. The Water supply is controlled using the mini motor pump which is then turned ON/OFF using the Relay & Pi DIO pins
4. UV Light is turned ON and OFF during a certain time period in a day using a Timer Switch
5. PI runs a Python program (shared in this repo) to acquire the data from the sensor and control the relay.

### Streaming the Plant Health data to Cloud
1. Raspberry Pi runs a Python program that continuously reads the sensor values every 1 minute and then publishes the data to the service running on Heroku through REST endpoints.
2. Similar to the Edge code in Raspberry Pi that publishes the data, the server Python code (web service using Quart) that receives the health data is also added to this repo.
3. The Web service in Heroku saves the data to file once it receives the information.

### Viewing the live data in the Dashboard
1. The Web service on Heroku also services an endpoint using which clients can receive the health trend.
2. Graphana server for dashboarding can be installed in any machine (cloud/client) and a dashboard can be built to view different sensor trends across time.

## Technology Used
1. Front End: Grafana (for viewing the time-series sensor data)
3. Backend: Python 3.11, Quart framework for service, hosted in Heroku
4. Hardware Controller: Raspberry Pi 3 B+ and Relay Module
5. Sensors: Moisture Sensor, Temperature Sensor, UV sensor
6. Actuators: UV light, DC Motor

## To Do
1. Integrate the AI support using OpenAI APIs in the server

## Reference
1. Connect the temperature sensor to the Pi and program it
  a. [Raspberry Pi DS18B20 Sensor](https://www.youtube.com/watch?v=X48OoO8r2Vo)
  b. [Raspberry-Pi-Sensors/ds18b20_single.py at master · israel-dryer/Raspberry-Pi-Sensors · GitHub](https://github.com/israel-dryer/Raspberry-Pi-Sensors/blob/master/ds18b20_single.py)
2. LED connection
  a. [Connect an LED to the Raspberry Pi | Coding projects for kids and teens](https://projects.raspberrypi.org/en/projects/rpi-connect-led)
  b. [Turning on an LED with your Raspberry Pi's GPIO Pins | The Pi Hut](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)
3. Moisture Sensor
   a. [ADC | CircuitPython Libraries on any Computer with MCP2221 | Adafruit Learning System](https://github.com/navinsubramani/ai-controlled-dektop-garden/assets/17029551/87036970-900e-4c37-ba58-b1189c26ec93)
   b. Run Thonny from the command line so it can read the environment variable and load the libraries. [Link](https://superuser.com/questions/664169/what-is-the-difference-between-etc-environment-and-etc-profile)
 4. UV Sensor: LTR390
    a. [Digital LTR390-UV Ultraviolet Sensor (C), Direct UV Index Value Output, I2C Bus | UV Sensor (C) (waveshare.com)](https://github.com/navinsubramani/ai-controlled-dektop-garden/assets/17029551/fe2feb36-b147-4067-9040-d9cf242ad8b9)
    b. [UV Sensor (C)](https://www.waveshare.com/wiki/UV_Sensor_(C))
5. Grafana
   a. [Grafana CLI | Documentation](https://grafana.com/docs/grafana/latest/cli/#:~:text=To%20invoke%20Grafana%20CLI%2C%20add,full%20path%20to%20the%20CLI.)
6. Other Links
   a. [Package updater fails](https://forums.raspberrypi.com/viewtopic.php?t=318242)
   b. [Post Install Checks | Circuit Python Libraries](https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221/post-install-checks)
   c. [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
