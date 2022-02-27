import os
import json 
from kafka import KafkaConsumer
# from dotenv import load_dotenv

# load_dotenv()
# BOOTSTRAP_SERVERS=os.getenv("KAFKA_BOOTSTRAP_SERVERS")
# TOPIC_NAME="MSKTutorialTopic"
# SASL_USERNAME=os.getenv("KAFKA_SASL_USERNAME")
# SASL_PASSWORD=os.getenv("KAFKA_SASL_PASSWORD")

BOOTSTRAP_SERVERS="b-3-public.iot-project.dztnn7.c3.kafka.ap-southeast-1.amazonaws.com:9196,b-1-public.iot-project.dztnn7.c3.kafka.ap-southeast-1.amazonaws.com:9196,b-2-public.iot-project.dztnn7.c3.kafka.ap-southeast-1.amazonaws.com:9196".split(",")
TOPIC_NAME="MSKTutorialTopic"
SASL_USERNAME="iotproject"
SASL_PASSWORD="iotproject"

if __name__ == '__main__':
    # Kafka Consumer 
    # consumer = KafkaConsumer(
    #     'messages',
    #     bootstrap_servers='localhost:9092',
    #     auto_offset_reset='earliest'
    # )
    consumer = KafkaConsumer(security_protocol="SASL_SSL",  sasl_mechanism="SCRAM-SHA-512", sasl_plain_username=SASL_USERNAME, sasl_plain_password=SASL_PASSWORD, bootstrap_servers=BOOTSTRAP_SERVERS)
    consumer.subscribe(TOPIC_NAME)
    for message in consumer:
        print(json.loads(message.value))