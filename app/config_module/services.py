from injector import Module, provider
from flask_sqlalchemy import SessionBase
from ..services import HDataService, StockBasicService


class ServicesModule(Module):
    @provider
    def provide_h_data_service(self, session: SessionBase) -> HDataService:
        return HDataService(session)

    @provider
    def provide_stock_basic_service(self, session: SessionBase) -> StockBasicService:
        return StockBasicService(session)
