import os
import time 
import json 
import random 
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer
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
# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=serializer,
#     compression_type='gzip'
# )

producer = KafkaProducer(value_serializer=serializer, security_protocol="SASL_SSL",  sasl_mechanism="SCRAM-SHA-512", sasl_plain_username=SASL_USERNAME, sasl_plain_password=SASL_PASSWORD, bootstrap_servers=BOOTSTRAP_SERVERS)



if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        test = producer.send(TOPIC_NAME, dummy_message)
        print(test)
        time.sleep(10)