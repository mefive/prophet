from sqlalchemy import Column, Integer, BigInteger, Numeric, String, Date
from app.models import db

class Daily(db.Model):
    __tablename__ = 'daily'

    id = Column(Integer, primary_key=True)
    ts_code = Column(String(10), index=True)
    trade_date = Column(Date)
    open = Column(Numeric(2))
    high = Column(Numeric(2))
    low = Column(Numeric(2))
    close = Column(Numeric(2))
    pre_close = Column(Numeric(2))
    change = Column(Numeric(2))
    pct_change = Column(Numeric(2))
    vol = Column(BigInteger)
    amount = Column(Numeric(2))