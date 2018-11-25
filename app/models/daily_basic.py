from sqlalchemy import Column, Integer, Numeric, String, Date
from . import db
from marshmallow import Schema

class DailyBasic(db.Model):
    """每日指标

    获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。
    """
    __tablename__ = 'daily_basic'

    id = Column(Integer, primary_key=True)
    ts_code = Column(String(10), index=True)
    trade_date = Column(Date)
    close = Column(Numeric(6, 2))
    turnover_rate = Column(Numeric(8, 4))
    volume_ratio = Column(Numeric(6, 2))
    pe = Column(Numeric(8, 4))
    pe_ttm = Column(Numeric(8, 4))
    pb = Column(Numeric(8, 4))
    ps = Column(Numeric(8, 4))
    ps_ttm = Column(Numeric(8, 4))
    total_share = Column(Numeric(12, 4))
    float_share = Column(Numeric(12, 4))
    free_share = Column(Numeric(12, 4))
    total_mv = Column(Numeric(12, 4))
    circ_mv = Column(Numeric(12, 4))


class DailyBasicSchema(Schema):
    class Meta:
        fields = ('id', 'ts_code', 'trade_date', 'close', 'turnover_rate', 'volume_ratio',
                  'pe', 'pe_ttm', 'pb', 'ps', 'ps_ttm', 'total_share', 'float_share',
                  'free_share', 'total_mv', 'circ_mv')
