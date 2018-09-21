from . import api
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy


@api.route('/stock')
def index(db: SQLAlchemy):
    print(db)
    return jsonify(dict(code=0, data=[]))
