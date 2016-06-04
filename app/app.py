import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

# Setup config
app.config.from_object('config.default')
# Environment-specific config
env = os.environ.get('FLASK_ENV') or 'development'
app.config.from_object('config.' + env)
app.config['ENV'] = env

redis = Redis(host='redis', port=6379)


@app.route('/')
def hello_world():
  redis.incr('hits')
  return 'Hello World! This page has been viewed %s times. Currently running in %s' \
       % (redis.get('hits'), app.config['ENV'])

if __name__ == '__main__':
    app.run(host="0.0.0.0")
