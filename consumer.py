import os
import json 
from kafka import KafkaConsumer
from kafka import TopicPartition
from dotenv import load_dotenv

load_dotenv()
BOOTSTRAP_SERVERS=os.getenv("KAFKA_BOOTSTRAP_SERVERS")
# TOPIC_NAME="MSKTutorialTopic"
# SASL_USERNAME=os.getenv("KAFKA_SASL_USERNAME")
# SASL_PASSWORD=os.getenv("KAFKA_SASL_PASSWORD")

print(BOOTSTRAP_SERVERS)

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'test',
        bootstrap_servers=BOOTSTRAP_SERVERS

    )
    for message in consumer:
        print(message.value)