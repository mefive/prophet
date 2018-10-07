from sqlalchemy import Column, Integer, Numeric, String, Date
from app.models import db


class DailyBasic(db.Model):
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

