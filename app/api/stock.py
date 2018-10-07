from . import api
from flask import jsonify

from ..services.stock_basic_service import StockBasicService
from ..services.daily_service import DailyService
from ..services.daily_basic_service import DailyBasicService
from ..models.stock_basic import stockBasicSchema


@api.route('/import/stockBasic')
def import_stock_basic(service: StockBasicService):
    service.import_stock_basic()
    return jsonify(dict(code=0, data=[]))


@api.route('/import/daily')
def import_daily(service: DailyService):
    service.import_all_stock_daily()
    return jsonify(dict(code=0, data=[stockBasicSchema.dump(s).data for s in stocks]))

@api.route('/import/dailyBasic')
def import_daily_basic(service: DailyBasicService):
    service.import_all_daily_basic()
    return jsonify(dict(code=0))


