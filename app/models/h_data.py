from .. import db

class HData(db.Model):
    __tablename__ = 'h_data'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), index=True)
    date = db.Column(db.Date)
    open = db.Column(db.Integer)
    high = db.Column(db.Integer)
    close = db.Column(db.Integer)
    volume = db.Column(db.BigInteger)
    amount = db.Column(db.BigInteger)


