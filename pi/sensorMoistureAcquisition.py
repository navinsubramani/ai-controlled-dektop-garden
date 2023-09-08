import os
os.environ['BLINKA_MCP2221'] = "1"
import time

def getMoistureValue(sensorIndex = 1):
    try:
        moisture = -1
        
        import board
        import analogio
        import glob
        
        if sensorIndex == 1:
            ADC1 = analogio.AnalogIn(board.G1)
            time.sleep(0.2)
            moisture = ADC1.value
        elif sensorIndex == 2:
            ADC2 = analogio.AnalogIn(board.G2)
            time.sleep(0.2)
            moisture = ADC2.value
        elif sensorIndex == 3:
            ADC3 = analogio.AnalogIn(board.G3)
            time.sleep(0.2)
            moisture = ADC3.value
        else:
            pass
        return { "success": (moisture > -1), "result": moisture }
    
    except Exception:
        print(Exception)
        return { "success": False, "result": -1 }