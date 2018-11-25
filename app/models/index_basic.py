from sqlalchemy import Column, Integer, Numeric, String, Date
from marshmallow import Schema
from . import db


class IndexBasic(db.Model):
    """指数基本信息
    指数基础信息
    """
    __tablename__ = "index_basic"

    id = Column(Integer, primary_key=True)
    ts_code = Column(String(10), index=True)
    name = Column(String(20))
    fullname = Column(String(40))
    market = Column(String(20))
    publisher = Column(String(20))
    index_type = Column(String(20))
    category = Column(String(20))
    base_date = Column(Date)
    base_point = Column(Numeric(12, 4))
    list_date = Column(Date)
    weight_rule = Column(String(10))
    desc = Column(String(200))
    exp_date = Column(Date)


class IndexBasicSchema(Schema):
    class Meta:
        fields = ('id', 'ts_code', 'name')
