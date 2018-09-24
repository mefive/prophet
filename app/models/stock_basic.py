from sqlalchemy import Column, Integer, String, Date, BigInteger, Unicode
from . import Base

class StockBasic(Base):
    __tablename__ = 'stock_basic'

    id = Column(Integer, primary_key=True)
    code = Column(String(20), index=True)
    name = Column(Unicode(50))
    industry = Column(String(100))
    area = Column(String(100))
    pe = Column(String(50))
    outstanding = Column(BigInteger)
    totals = Column(BigInteger)
    total_assets = Column(BigInteger)
    liquid_assets = Column(BigInteger)
    fixed_assets = Column(BigInteger)
    esp = Column(Integer)
    bvps = Column(Integer)
    pb = Column(Integer)
    time_to_market = Column(Date)
    undp = Column(Integer)
    perundp = Column(Integer)
    rev = Column(Integer)
    profit = Column(Integer)
    npr = Column(Integer)
