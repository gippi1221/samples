import os
import json 
from pymongo import MongoClient
import redis
import time

mongo_db_url = os.getenv('DB_CONN')
mongo_db_name = os.getenv('DB_NAME')
mongo_db_collection = 'jokes'

redis_db_host = os.getenv('REDIS_HOST')
redis_db_port = os.getenv('REDIS_PORT')

client = MongoClient(mongo_db_url)
db = client[mongo_db_name]
collection = db[mongo_db_collection]

r = redis.Redis(host=redis_db_host, port=redis_db_port, decode_responses=True)

def get_hash_name(id):
  return f'joke#{id}'

def get_sset_name():
  return 'topjokes'

pipeline = [
  {
    "$sort": {
      "rating": -1
    }
  },
  {
    "$limit": 10
  },
  {
    "$project": {
      "_id": 0,
      "dt": 0
    }
  }
]

result = list(collection.aggregate(pipeline))

with r.pipeline() as pipe:
  pipe.multi()

  for key in r.scan_iter(get_hash_name('*')):
    r.delete(key)
  
  for obj in result:
    id = obj.pop("id")
    pipe.hset(get_hash_name(id), mapping=obj, )
    pipe.zadd(get_sset_name(), {get_hash_name(id): obj['rating']})
  
  pipe.zremrangebyrank(get_sset_name(), 0, -11)
  
  pipe.set('lastrefresh', round(time.time() * 1000))
  
  pipe.execute()
