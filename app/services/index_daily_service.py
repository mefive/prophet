import pandas
from .service_base import ServiceBase
from . import pro
from ..models.index_daily import IndexDaily


class IndexDailyService(ServiceBase):
    def get_model(self):
        return IndexDaily

    def import_index_daily(self, ts_code, start_date, end_date, trade_date = None):
        print('== index daily import start ==')

        df: pandas.DataFrame = pro.index_daily(
            ts_code=ts_code,
            start_date=start_date,
            end_date=end_date,
            trade_date=trade_date
        )

        if df is not None:
            for index, row in df.iterrows():
                index_daily = IndexDaily(
                    ts_code=row.get('ts_code'),
                    trade_date=row.get('trade_date'),
                    close=row.get('close'),
                    open=row.get('open'),
                    high=row.get('high'),
                    low=row.get('low'),
                    pre_close=row.get('pre_close'),
                    change=row.get('change'),
                    pct_change=row.get('pct_change'),
                    vol=row.get('vol'),
                    amount=row.get('amount')
                )

                self.session.add(index_daily)

            self.session.commit()

            print('== index daily import done ==')
        else:
            print('== index daily import fail ==')
