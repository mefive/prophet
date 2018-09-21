from . import api
from flask import jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from ..services.h_data_service import HDataService


@api.route('/stock')
def index():
    print(current_app.db)
    return jsonify(dict(code=0, data=[]))
