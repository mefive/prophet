from . import api
from flask import jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from ..services.h_data_service import HDataService


@api.route('/stock')
def index():
    current_app.h_data_service.import_index_h_data()
    return jsonify(dict(code=0, data=[]))
