import os
basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get('FLASK_ENV') or 'development'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] + '_' + ENV

