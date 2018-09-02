from .. import db

class StockBasic(db.Model):
    __tablename__ = 'stock_basic'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=True)
    name = db.Column(db.Unicode(50))
    industry = db.Column(db.String(100))
    area = db.Column(db.String(100))
    pe = db.Column(db.String(50))
    outstanding = db.Column(db.BigInteger)
    totals = db.Column(db.BigInteger)
    total_assets = db.Column(db.BigInteger)
    liquid_assets = db.Column(db.BigInteger)
    fixed_assets = db.Column(db.BigInteger)
    esp = db.Column(db.Integer)
    bvps = db.Column(db.Integer)
    pb = db.Column(db.Integer)
    time_to_market = db.Column(db.Date)
    undp = db.Column(db.Integer)
    perundp = db.Column(db.Integer)
    rev = db.Column(db.Integer)
    profit = db.Column(db.Integer)
    npr = db.Column(db.Integer)
