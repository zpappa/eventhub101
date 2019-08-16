import random
import json
from datetime import datetime
from service import EventHubService

producer = EventHubService()

for i in range(0, 1000):
    sample_sensor_reading = {
        "sensor_id": random.randrange(1, 5),
        "temperature": random.randrange(0, 100, 1),
        "timestamp": str(datetime.utcnow())
    }
    print(sample_sensor_reading)
    producer.send(json.dumps(sample_sensor_reading))

producer.stop()
