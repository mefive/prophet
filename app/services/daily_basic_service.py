import pandas
from .service_base import ServiceBase
from . import pro
from ..models.daily_basic import DailyBasic
from ..models.stock_basic import StockBasic


class DailyBasicService(ServiceBase):
    def get_model(self):
        return StockBasic

    def import_all_daily_basic(self):
        query = self.session.query(StockBasic)
        stocks = query.limit(1)

        for stock in stocks:
            self.import_daily_basic(stock.ts_code)

    def import_daily_basic(self, ts_code=None, trade_date=None):
        print('== import daily basic start ==')

        df: pandas.DataFrame = pro.query('daily_basic', ts_code=ts_code, trade_date=trade_date)

        if df is not None:
            for index, row in df.iterrows():
                daily_basic = DailyBasic(
                    ts_code=ts_code,
                    trade_date=row.get('trade_date'),
                    close=row.get('close'),
                    turnover_rate=row.get('turnover_rate'),
                    volume_ratio=row.get('volume_ratio'),
                    pe=row.get('pe'),
                    pe_ttm=row.get('pe_ttm'),
                    pb=row.get('pb'),
                    ps=row.get('ps'),
                    ps_ttm=row.get('ps_ttm'),
                    total_share=row.get('total_share'),
                    float_share=row.get('float_share'),
                    free_share=row.get('free_share'),
                    total_mv=row.get('total_mv'),
                    circ_mv=row.get('circ_mv'),
                )

                self.session.add(daily_basic)

            self.session.commit()

            print('== import daily basic done ==')
