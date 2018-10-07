import pandas
from ..models.daily import Daily
from ..models.stock_basic import StockBasic

from . import pro
from .service_base import ServiceBase


class DailyService(ServiceBase):
    def import_all_stock_daily(self):
        query = self.session.query(StockBasic)
        stocks = query.limit(2)

        for stock in stocks:
            self.import_daily(stock.ts_code)


    def import_daily(self, ts_code, trade_date = None):
        print('=== import daily ===')

        df: pandas.DataFrame = pro.query('daily',
                                         ts_code=ts_code,
                                         trade_date=trade_date)

        if df is not None:
            for index, row in df.iterrows():
                daily = Daily(
                    ts_code=ts_code,
                    trade_date=row.get('trade_date'),
                    open=row.get('open'),
                    high=row.get('high'),
                    low=row.get('low'),
                    close=row.get('close'),
                    pre_close=row.get('pre_close'),
                    change=row.get('change'),
                    pct_change=row.get('pct_change'),
                    vol=row.get('vol'),
                    amount=row.get('amount'),
                )

                self.session.add(daily)

            self.session.commit()


        print('== import daily done')
