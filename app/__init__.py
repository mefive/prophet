from flask import Flask, current_app
from injector import Injector, Key

from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .services.h_data_service import HDataService


def configure(binder):
    binder.bind(Key('db'), db)


def init_db():
    injector = Injector(configure)
    h_data_service = injector.get(HDataService)
    current_app.h_data_service = h_data_service


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api import api

    app.register_blueprint(blueprint=api, url_prefix='/api')

    db.init_app(app)

    with app.app_context():
        init_db()

    # FlaskInjector(app=app, modules=[configure])

    return app
