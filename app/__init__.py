from flask import Flask

from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector, request
from .services.h_data_service import HDataService

db = SQLAlchemy()

from . import models

def configure(binder):
    binder.bind(
        SQLAlchemy,
        to=db,
        scope=request
    )
    binder.bind(
        HDataService,
        to=HDataService(),
        scope=request
    )


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api import api

    app.register_blueprint(blueprint=api, url_prefix='/api')

    db.init_app(app)

    FlaskInjector(app=app, modules=[configure])

    return app
