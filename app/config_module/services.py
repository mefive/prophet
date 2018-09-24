from injector import Module, provider
from flask_sqlalchemy import SQLAlchemy
from ..services.h_data_service import HDataService


class ServicesModule(Module):
    @provider
    def provide_h_data_service(self, db: SQLAlchemy) -> HDataService:
        return HDataService(db)
