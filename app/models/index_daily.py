from sqlalchemy import Column, Integer, BigInteger, Numeric, String, Date
from app.models import db


class IndexDaily(db.Model):
    """指数日线行情
    """
    __tablename__ = "index_daily"

    id = Column(Integer, primary_key=True)
    ts_code = Column(String(10), index=True)
    trade_date = Column(Date)
    close = Column(Numeric(12, 4))
    open = Column(Numeric(12, 4))
    high = Column(Numeric(12, 4))
    low = Column(Numeric(12, 4))
    pre_close = Column(Numeric(12, 4))
    change = Column(Numeric(12, 4))
    pct_change = Column(Numeric(12, 4))
    vol = Column(BigInteger)
    amount = Column(Numeric(20, 4))

