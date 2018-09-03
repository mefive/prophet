from flask import Flask

from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

from . import models


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api import api

    app.register_blueprint(blueprint=api, url_prefix='/api')

    migrate = Migrate(app, db)

    return app
