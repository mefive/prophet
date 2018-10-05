from flask import Flask
from flask_injector import FlaskInjector

from flask_sqlalchemy import SQLAlchemy
from config import config
from .models import db
from .config_module.session import SessionModule
from .config_module.services import  ServicesModule


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .api import api

    app.register_blueprint(blueprint=api, url_prefix='/api')

    FlaskInjector(app=app, modules=[SessionModule(db.session), ServicesModule])

    return app
