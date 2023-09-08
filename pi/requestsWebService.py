import requests
import json

# Endpoint URL of the Flask server

timeout_seconds = 10

def post_sensor_data(URL, timestamp, t, m1, m2, m3, uvs, als):
    # Prepare the data to be sent in the POST request
    data = {
        'timestamp': timestamp,
        'sensor_temperature': t,
        'sensor_moisture_1': m1,
        'sensor_moisture_2': m2,
        'sensor_moisture_3': m3,
        'sensor_uvs': uvs,
        'sensor_als': als,
    }
    
    print(data)
    
    try:
        # Send the POST request to the Flask server
        response = requests.post(URL + '/log_sensor_data', data=data, timeout=timeout_seconds)

        # Check the response status
        if response.status_code == 200:
            #print('Data published successfully.')
            pass
        else:
            print('Failed to publish data.')
            
    except Exception:
        print(Exception)


def get_motor_action(URL):
    # Prepare the data to be sent in the POST request
    
    try:
        # Send the POST request to the Flask server
        response = requests.post(URL + '/get_motor_status', timeout=timeout_seconds)

        # Check the response status
        if response.status_code == 200:
            #print('Data recieved successfully.')
            data = response.json()["data"]
            return { "action": bool(data["action"]), "id": int(data["id"]), "upTime": int(data["upTime"]) }
        else:
            print('Failed to recieve data.')
            return { "action": False, "id": -1, "upTime": -1 }
            
    except Exception:
        print(Exception)



if __name__ == '__main__':
    #post_sensor_data('http://10.0.0.132:5000', '2023-06-24 20:43:21', 1, 2, 3, 4, 5, 6)
    pass