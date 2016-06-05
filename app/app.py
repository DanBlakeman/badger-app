import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.default')
app.config.from_object('config.' + app.config['ENV'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


@app.route('/')
def hello_world():
    return 'Hello World! This page is live. Currently running in %s' \
       % app.config['ENV']

if __name__ == '__main__':
    app.run(host="0.0.0.0")
