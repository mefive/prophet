import tushare
import pandas
from .service_base import ServiceBase
from ..models.stock_basic import StockBasic
from . import pro


class StockBasicService(ServiceBase):
    def get_page(self):
        query = self.session.query(StockBasic)
        return query.limit(20)

    def import_stock_basic(self):
        df: pandas.DataFrame = pro.query('stock_basic')

        if df is not None:
            for index, row in df.iterrows():
                stock_basic = StockBasic(
                    ts_code=row.get('ts_code'),
                    symbol=row.get('symbol'),
                    name=row.get('name'),
                    fullname=row.get('fullname'),
                    enname=row.get('enname'),
                    exchange_id=row.get('exchange_id'),
                    curr_type=row.get('curr_type'),
                    list_status=row.get('list_status'),
                    list_date=row.get('list_date'),
                    delist_date=row.get('delist_date'),
                    is_hs=row.get('is_hs'),
                )

                self.session.add(stock_basic)

            self.session.commit()
