from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from config import config
from app.models import db

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(config['development'])

    with app.app_context():
        db.init_app(app)

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    manager.run()
