from .. import main
from flask import jsonify


@main.route('/stock')
def index():
    return jsonify(dict(code=0, data=[]))
