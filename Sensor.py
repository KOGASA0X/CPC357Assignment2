from google.cloud import pubsub_v1
import json
from datetime import datetime

# set up the project id and topic id
project_id = "cpc357assignment2"
topic_id = "testtopic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# message data
data = {
    "sensor_id": "parking_01",
    "timestamp": datetime.utcnow().isoformat() + "Z",  # ISO 8601 format
    "state": 1  # 1 for occupied, 0 for available
}

# transform data to json format
message = json.dumps(data).encode("utf-8")

# publish message
future = publisher.publish(topic_path, data=message)
print(f"Published message ID: {future.result()}")
