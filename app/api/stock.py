from . import api
from flask import jsonify

from ..services.stock_basic_service import StockBasicService
from ..services.daily_service import DailyService
from ..models.stock_basic import stockBasicSchema


@api.route('/import/stockBasic')
def index(service: StockBasicService):
    service.import_stock_basic()
    return jsonify(dict(code=0, data=[]))


@api.route('/import/daily')
def get_all(service: DailyService):
    stocks = service.import_all_stock_daily()

    return jsonify(dict(code=0, data=[stockBasicSchema.dump(s).data for s in stocks]))
