from . import api
from flask import jsonify, request

from ..services.stock_basic_service import StockBasicService
from ..services.daily_service import DailyService
from ..services.daily_basic_service import DailyBasicService
from ..models.stock_basic import StockBasicSchema
from ..models.daily_basic import DailyBasicSchema


# @api.route('/import/stockBasic')
# def import_stock_basic(service: StockBasicService):
#     service.import_stock_basic()
#     return jsonify(dict(code=0))
#
#
# @api.route('/import/daily')
# def import_daily(service: DailyService):
#     service.import_all_stock_daily()
#     return jsonify(dict(code=0))
#
#
# @api.route('/import/dailyBasic')
# def import_daily_basic(service: DailyBasicService):
#     service.import_all_daily_basic()
#     return jsonify(dict(code=0))


@api.route('/stockBasic/list')
def get_stock_basic_list(service: StockBasicService):
    start = int(request.args.get('start'))
    limit = int(request.args.get('limit'))

    stocks, total = service.get_page(start, limit)

    stock_basic_schema = StockBasicSchema()

    return jsonify({
        'code': 0,
        'data': {
            'data': [stock_basic_schema.dump(s).data for s in stocks],
            'total': total,
        },
    })


@api.route('/dailyBasic/list')
def get_daily_basic_list(service: DailyBasicService):
    start = int(request.args.get('start'))
    limit = int(request.args.get('limit'))

    records, total = service.get_page(start, limit)

    daily_basic_schema = DailyBasicSchema()

    return jsonify({
        'code': '0',
        'data': {
            'data': [daily_basic_schema.dump(record).data for record in records],
            'total': total,
        }
    })
