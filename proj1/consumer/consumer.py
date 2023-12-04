import os
import json 
from kafka import KafkaConsumer
from pymongo import MongoClient
from db_service import MongoDBService

kafka_bs_servers = os.getenv('KAFKA_BS')
db_url = os.getenv('DB_CONN')
db_name = os.getenv('DB_NAME')

def main():

  consumer = KafkaConsumer(
    'jokes',
    bootstrap_servers=kafka_bs_servers,
    max_poll_records = 100,
    value_deserializer=lambda m: json.loads(m.decode('ascii')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='jokes-consumer'
  )

  for message in consumer:
    db_service.insert_document(message.value)

if __name__ == "__main__":
  db_service = MongoDBService(db_url, db_name)
  main()