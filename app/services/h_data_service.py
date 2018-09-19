import pandas
import tushare
import time
from dateutil import parser
from dateutil.relativedelta import relativedelta
from flask_sqlalchemy import SQLAlchemy

from ..models.h_data import HData

index_codes = {
    '000001',
    '399001',
    '399006',
    '000016',
    '000300'
}


class HDataService:
    def __init__(self, session: SQLAlchemy.Session):
        self.session = session

    def import_index_h_data(self):
        start = parser.parse('2010-01-01').date()
        end = parser.parse('2010-12-31')

        while start != parser.parse('2012-01-01'):
            for code in index_codes:
                self.import_h_data(code, start, end)

            time.sleep(1)
            start = start + relativedelta(years=1)
            end = end + relativedelta(years=1)

    def import_h_data(self, code, start, end):
        print('=== import h data ===')
        print('start: {:%Y-%m-%d} end: {:%Y-%m-%d}'.format(start, end))

        df: pandas.DataFrame = tushare.get_h_data(
            code=code,
            start='{:%Y-%m-%d}'.format(start),
            end='{:%Y-%m-%d}'.format(end),
            index=True
        )

        if df is not None:
            for index, row in df.iterrows():
                h_data = HData(
                    code=code,
                    date=index,
                    open=row['open'],
                    close=row['close'],
                    high=row['high'],
                    volume=row['volume'],
                    amount=row['amount']
                )

                self.session.add(h_data)

            self.session.commit()

        print('done')


if __name__ == 'main':
    from .. import db

    service = HDataService(db.session)
