from flask import Flask, render_template
import datetime
import redis
import os

redis_db_host = os.getenv('REDIS_HOST')
redis_db_port = os.getenv('REDIS_PORT')

r = redis.Redis(host=redis_db_host, port=redis_db_port, decode_responses=True)

app = Flask(__name__)

@app.route('/')
def home():
  jokes = []
  data = r.zrange('topjokes', 0, -1, desc=True)
  p = r.pipeline()
  for key in data:
    p.hgetall(key)

  for h in p.execute():
    jokes.append(h)
  
  last_dt_ms=r.get('lastrefresh')
  last_dt=datetime.datetime.fromtimestamp(int(last_dt_ms)/1000.0)
  
  return render_template('index.html', last_dt=last_dt, jokes=jokes)
