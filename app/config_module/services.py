from injector import Module, provider
from flask_sqlalchemy import SessionBase
from ..services.stock_basic_service import StockBasicService
from ..services.daily_service import DailyService
from ..services.daily_basic_service import DailyBasicService
from ..services.index_daily_service import IndexDailyService

class ServicesModule(Module):
    @provider
    def provide_stock_basic_service(self, session: SessionBase) -> StockBasicService:
        return StockBasicService(session)

    @provider
    def provide_daily_service(self, session: SessionBase) -> DailyService:
        return DailyService(session)

    @provider
    def provide_daily_basic_service(self, session: SessionBase) -> DailyBasicService:
        return DailyBasicService(session)

    @provider
    def provide_index_basic_service(self, session: SessionBase) -> IndexDailyService:
        return IndexDailyService(session)

