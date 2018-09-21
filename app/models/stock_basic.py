from flask_sqlalchemy import SQLAlchemy

Column = SQLAlchemy.Column


class StockBasic(SQLAlchemy.Model):
    __tablename__ = 'stock_basic'

    id = Column(Column.Integer, primary_key=True)
    code = Column(Column.String(20), index=True)
    name = Column(Column.Unicode(50))
    industry = Column(Column.String(100))
    area = Column(Column.String(100))
    pe = Column(Column.String(50))
    outstanding = Column(Column.BigInteger)
    totals = Column(Column.BigInteger)
    total_assets = Column(Column.BigInteger)
    liquid_assets = Column(Column.BigInteger)
    fixed_assets = Column(Column.BigInteger)
    esp = Column(Column.Integer)
    bvps = Column(Column.Integer)
    pb = Column(Column.Integer)
    time_to_market = Column(Column.Date)
    undp = Column(Column.Integer)
    perundp = Column(Column.Integer)
    rev = Column(Column.Integer)
    profit = Column(Column.Integer)
    npr = Column(Column.Integer)
