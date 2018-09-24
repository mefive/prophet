from sqlalchemy import Column, Integer, String, Date, BigInteger
from . import Base


class HData(Base):
    id = Column(Integer, primary_key=True)
    code = Column(String(10), index=True)
    date = Column(Date)
    open = Column(Integer)
    high = Column(Integer)
    close = Column(Integer)
    volume = Column(BigInteger)
    amount = Column(BigInteger)
