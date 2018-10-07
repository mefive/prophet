from sqlalchemy import Column, Integer, BigInteger, Numeric, String, Date
from app.models import db
from marshmallow import Schema, fields


class StockBasic(db.Model):
    __tablename__ = 'stock_basic'

    id = Column(Integer, primary_key=True)
    ts_code = Column(String(10), index=True)
    symbol = Column(String(10))
    name = Column(String(10))
    fullname = Column(String(20))
    enname = Column(String(20))
    exchange_id = Column(String(10))
    curr_type = Column(String(10))
    list_status = Column(String(2))
    list_date = Column(Date)
    delist_date = Column(Date)
    is_hs = Column(String(2))


class StockBasicSchema(Schema):
    id = fields.Integer()
    ts_code = fields.Str()
    symbol = fields.Str()
    name = fields.Str()
    list_date = fields.Date()


stockBasicSchema = StockBasicSchema()
