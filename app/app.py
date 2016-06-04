import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.default')
env = os.environ.get('FLASK_ENV') or 'development'
app.config.from_object('config.' + env)
app.config['ENV'] = env
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


@app.route('/')
def hello_world():
  return 'Hello World! This page has been viewed times. Currently running in %s' \
       % app.config['ENV']

if __name__ == '__main__':
    app.run(host="0.0.0.0")
