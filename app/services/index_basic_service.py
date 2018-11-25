import pandas
from .service_base import ServiceBase
from . import pro
from ..models.index_basic import IndexBasic
import numpy


class IndexBasicService(ServiceBase):
    def get_model(self):
        return IndexBasic

    def import_index_basic(self, market):
        print('== index basic import start ==')
        df: pandas.DataFrame = pro.index_basic(market=market)

        if df is not None:
            for index, row in df.iterrows():
                base_point = row.get('base_point');

                if numpy.isnan(base_point):
                    base_point = 0

                index_basic = IndexBasic(
                    ts_code=row.get('ts_code'),
                    name=row.get('name'),
                    fullname=row.get('fullname'),
                    market=row.get('market'),
                    publisher=row.get('publisher'),
                    index_type=row.get('index_type'),
                    category=row.get('category'),
                    base_date=row.get('base_date'),
                    base_point=base_point,
                    list_date=row.get('list_date'),
                    weight_rule=row.get('weight_rule'),
                    desc=row.get('desc'),
                    exp_date=row.get('exp_date')
                )

                self.session.add(index_basic)

            self.session.commit()

            print('== index basic import done ==')
        else:
            print('== index basic import fail ==')
