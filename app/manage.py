import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

app.config.from_object('config.default')
env = os.environ.get('FLASK_ENV') or 'development'
app.config.from_object('config.' + env)
app.config['ENV'] = env

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()