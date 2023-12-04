import os
import json
import requests
import time
from kafka import KafkaProducer
import random

kafka_bs_servers = os.getenv('KAFKA_BS')
url_str = os.getenv('MOCK_API')

def serializer(message):
  return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
  bootstrap_servers=['kafka:9092'],
  value_serializer=serializer
)

response = requests.get(url_str)
json_data = json.loads(response.content)
json_data['dt'] = round(time.time() * 1000)
json_data['rating'] = random.randint(100, 1000) / 100

producer.send('jokes', json_data)
producer.flush()
