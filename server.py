import csv
import os
from datetime import datetime
import json as JSON

import quart
import quart_cors
from quart import request, Quart, session

app = quart_cors.cors(quart.Quart(__name__), allow_origin=[])
app.secret_key = 'your-secret-key'

SENSOR_DATA_FILE_NAME = "sensor_data.csv"
SENSOR_DATA_DIRECTORY = 'sensor_data_logs'
SENSOR_DATA_FILE_BUFFER_SIZE = int(os.getenv('SENSOR_DATA_FILE_BUFFER_SIZE')) or 100
SENSOR_DATA_CHECK_BUFFER_DATE = ""

DEFAULT_MOTOR_STATE = {
    "action": False,
    "id": -1,
    "upTime": 10,
}

def maintain_sensor_data_buffer():
    # find the current date and SENSOR_DATA_CHECK_BUFFER_DATE, if they are different, then we need to check the buffer
    # update SENSOR_DATA_CHECK_BUFFER_DATE to the current date
    # check if the CSV file exists and it row count is greater than SENSOR_DATA_FILE_BUFFER_SIZE
    # if it is, then we need to remove the row count - SENSOR_DATA_FILE_BUFFER_SIZE rows from the CSV file
    # if it is not, then we do nothing
    global SENSOR_DATA_CHECK_BUFFER_DATE
    current_date = datetime.now().strftime("%Y-%m-%d")
    if current_date != SENSOR_DATA_CHECK_BUFFER_DATE:
        SENSOR_DATA_CHECK_BUFFER_DATE = current_date
        filename = os.path.join(SENSOR_DATA_DIRECTORY, SENSOR_DATA_FILE_NAME)
        file_exists = os.path.isfile(filename)
        print("Checked for buffer size...")
        if file_exists:
            # read the CSV file including the first row
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                # get the row count
                existing_data = [row for row in reader]
                row_count = len(existing_data)
            # if the row count is greater than SENSOR_DATA_FILE_BUFFER_SIZE
            if row_count > SENSOR_DATA_FILE_BUFFER_SIZE:
                # remove the row count - SENSOR_DATA_FILE_BUFFER_SIZE rows from the CSV file
                new_data = existing_data[(row_count - SENSOR_DATA_FILE_BUFFER_SIZE):]
                # print(row_count, SENSOR_DATA_FILE_BUFFER_SIZE, existing_data, new_data, sep='\n')
                # write the new data to the CSV file
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(new_data)
                    print("Updated the buffer...")

def write_motor_data(motor_state):
    # Create directory for CSV files (if it doesn't exist)
    os.makedirs(SENSOR_DATA_DIRECTORY, exist_ok=True)

    # Generate CSV filename based on date
    filename = os.path.join(SENSOR_DATA_DIRECTORY, "motor_data.txt")

    # Check if the file already exists
    # file_exists = os.path.isfile(filename)

    # Overrite Write to the text file
    with open(filename, 'w', newline='') as txtfile:
        txtfile.write(JSON.dumps(motor_state))


def read_motor_data():
    # Create directory for CSV files (if it doesn't exist)
    os.makedirs(SENSOR_DATA_DIRECTORY, exist_ok=True)

    # Generate CSV filename based on date
    filename = os.path.join(SENSOR_DATA_DIRECTORY, "motor_data.txt")

    # Check if the file already exists
    file_exists = os.path.isfile(filename)
    if file_exists:
        # Read data from CSV file and not using pandas
        with open(filename, 'r') as txtfile:
            data = JSON.loads(txtfile.read())
        return data
    else:
        return DEFAULT_MOTOR_STATE


write_motor_data(DEFAULT_MOTOR_STATE)

@app.route('/log_sensor_data', methods=['POST'])
async def log_sensor_data():
    data = await request.form
    timestamp_string = data.get('timestamp')
    sensor_temperature = data.get('sensor_temperature')
    sensor_moisture_1 = data.get('sensor_moisture_1')
    sensor_moisture_2 = data.get('sensor_moisture_2')
    sensor_moisture_3 = data.get('sensor_moisture_3')
    sensor_uvs = data.get('sensor_uvs')
    sensor_als = data.get('sensor_als')

    # Create directory for CSV files (if it doesn't exist)
    os.makedirs(SENSOR_DATA_DIRECTORY, exist_ok=True)

    # Generate CSV filename based on date
    filename = os.path.join(SENSOR_DATA_DIRECTORY, SENSOR_DATA_FILE_NAME)

    # Check if the file already exists
    # file_exists = os.path.isfile(filename)

    # Write or append data to the CSV file
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write data row
        writer.writerow([
            timestamp_string,
            sensor_temperature,
            sensor_moisture_1,
            sensor_moisture_2,
            sensor_moisture_3,
            sensor_uvs,
            sensor_als])

    maintain_sensor_data_buffer()
    return quart.Response(response="Data logged successfully", status=200, content_type="application/json")


@app.route('/get_sensor_data', methods=['POST'])
async def get_sensor_data():
    # Get date from query string
    data = await request.form
    # date_string = data.get('date')
    sensor_request = data.get('sensor_request')

    # Generate CSV filename based on date
    filename = os.path.join(SENSOR_DATA_DIRECTORY, SENSOR_DATA_FILE_NAME)

    # Check if the file exists
    file_exists = os.path.isfile(filename)

    if file_exists:
        # Read data from CSV file and not using pandas
        column_names = ["timestamp", "sensor_temperature", "sensor_moisture_1", "sensor_moisture_2", "sensor_moisture_3", "sensor_uvs", "sensor_als"]
        sensor_index = column_names.index(sensor_request)
        print(sensor_request, sensor_index)

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            
            data = [[row[0], row[sensor_index]] for row in reader]

        return {
            'success': True,
            'data': data
        }
    else:
        return {
            'success': False,
            'message': 'No data found for the specified date.'
        }


@app.route('/get_motor_status', methods=['POST'])
async def get_motor_status():
    
    temp_MOTOR_STATE = read_motor_data()
    write_motor_data(DEFAULT_MOTOR_STATE)

    return {
        'success': True,
        'data': temp_MOTOR_STATE
    }

@app.route('/set_motor_status', methods=['POST'])
async def set_motor_status():

    data = await request.form
    action = data.get('action')
    id = data.get('id')
    upTime = data.get('upTime')

    write_motor_data({
        "action": action,
        "id": id,
        "upTime": upTime,
    })

    return {
        'success': True,
    }


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
