from . import api
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from ..services.h_data_service import HDataService


@api.route('/stock')
def index(db: SQLAlchemy, service: HDataService):
    service.import_index_h_data()
    return jsonify(dict(code=0, data=[]))
