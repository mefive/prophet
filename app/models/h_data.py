from flask_sqlalchemy import SQLAlchemy

Column = SQLAlchemy.Column

class HData(SQLAlchemy.Model):
    __tablename__ = 'h_data'

    id = Column(Column.Integer, primary_key=True)
    code = Column(Column.String(10), index=True)
    date = Column(Column.Date)
    open = Column(Column.Integer)
    high = Column(Column.Integer)
    close = Column(Column.Integer)
    volume = Column(Column.BigInteger)
    amount = Column(Column.BigInteger)
