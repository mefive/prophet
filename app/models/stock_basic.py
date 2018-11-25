from sqlalchemy import Column, Integer, String, Date
from . import db
from marshmallow import Schema


class StockBasic(db.Model):
    """股票列表

    基础信息数据，包括股票代码、名称、上市日期、退市日期等
    """
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
    class Meta:
        fields = ('id', 'ts_code', 'symbol', 'name', 'list_date')
