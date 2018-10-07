from sqlalchemy import Column, Integer, Numeric, String, Date
from app.models import db

class Daily(db.Model):
    __tablename__ = 'daily'

    id = Column(Integer, primary_key=True)
    ts_code = Column(String(10), index=True)
    trade_date = Column(Date)
    open = Column(Numeric(6, 2))
    high = Column(Numeric(6, 2))
    low = Column(Numeric(6, 2))
    close = Column(Numeric(6, 2))
    pre_close = Column(Numeric(6, 2))
    change = Column(Numeric(6, 2))
    pct_change = Column(Numeric(6, 4))
    vol = Column(Numeric(15, 3))
    amount = Column(Numeric(15, 3))