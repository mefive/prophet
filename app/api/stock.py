from . import api
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy, SessionBase
from ..services import StockBasicService


@api.route('/stock')
def index(service: StockBasicService):
    service.import_stock_basic()
    return jsonify(dict(code=0, data=[]))
