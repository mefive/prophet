from . import api
from flask import jsonify


@api.route('/stock')
def index():
    return jsonify(dict(code=0, data=[]))
