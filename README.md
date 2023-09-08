# AI-Controlled Desktop Garden [Work in Progress]

## Introduction
This is a fun project that makes uses AI to monitor and control the Desktop Plant Garden.

Plants in the Desktop Garden are continuously monitored on its environmental conditions like Moisture, UV light, Temperature, and Ambient Light. The Desktop Garden also contains the controls for watering the plant and controlled UV ray exposure. Now an AI is introduced into this system that uses the data sensed by these sensors from the garden and decides when and how much to water the plant and when to expose it to the UV rays based on the plant's health.

## System design
![image](https://github.com/navinsubramani/ai-controlled-dektop-garden/assets/17029551/e8282de4-01c3-4401-9224-d49dd4b5a4b9)

### Hardware Components at Edge
1. 1 x Raspberry Pi 3B+
2. ![1 x 4 Channel 5V Relay Module](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
3. ![4 x Mini Water Pump](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
4. ![1 x 4M Vinyl Tubing (Material: PVC)](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
5. ![4 x Capacitive Soil Moisture Sensor (TL555C)](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TMVNTDK/ref=sr_1_11?hvadid=190480806186&hvdev=c&hvlocphy=9001880&hvnetw=g&hvqmt=e&hvrand=9455202391857626053&hvtargid=kwd-317572890378&hydadcr=24600_9648833&keywords=raspberry+pi+soil+moisture+sensor&qid=1686106761&sr=8-11)
6. ![1 x UV & Ambient Light Sensor (LTR390)](https://www.amazon.com/gp/product/B09FDGTKLX/ref=ppx_yo_dt_b_asin_title_o09_s01?ie=UTF8&psc=1)
7. ![1 x DS18B20 Temperature Sensor](https://www.amazon.com/Hilitchi-DS18B20-Waterproof-Temperature-Sensors/dp/B018KFX5X0?th=1)
8. ![1 x MCP221A ADC to convert moisture sensor analog to digital values](https://www.adafruit.com/product/4471)
9. ![1 x DOMMIA Grow Light](https://www.amazon.com/dp/B07TRKXX9D?ref=ppx_yo2ov_dt_b_product_details&th=1)
10. ![1 x myTouchSmart Indoor Digital Timer Switch](https://www.homedepot.com/p/myTouchSmart-Indoor-Digital-24-Hour-Fashion-Timer-with-Cloth-Cover-2-Settings-1-Polarized-Outlet-66985/324058579)
11. Prototype PCBs, Male-Male, Male-Female Wires, Solder Kit as required

## Technology Used
1. Front End: Grafana (for viewing the time-series sensor data)
3. Backend: Python 3.11, Quart framework for service, hosted in Heroku
4. Hardware Controller: Raspberry Pi 3 B+ and Relay Module
5. Sensors: Moisture Sensor, Temperature Sensor, UV sensor
6. Actuators: UV light, DC Motor
