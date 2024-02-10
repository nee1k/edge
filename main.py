import datetime
import os
import random
import time
import json  # Import json for easy data serialization


def generate_cpu_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wattage = round(random.uniform(1.0, 10.0), 6)  # power in Watts
    pid = str(random.randint(100000, 999999))  # PID
    process = random.choice(["python", "java", "c++", "go", "ruby"])  # process name
    return {"timestamp": timestamp, "watt": wattage, "pid": pid, "process": process}


if __name__ == '__main__':
    generated_files = []

    # for i in range(1, 6):
    start_time = datetime.datetime.now()
    cpu_data = []
    while True:
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        if elapsed_time.total_seconds() > 5:
            break

        data = generate_cpu_data()
        cpu_data.append(data)
        time.sleep(0.5)

    file_name = f'logs/cpu.json'
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as file:
        json.dump(cpu_data, file, indent=4)
    generated_files.append(file_name)
