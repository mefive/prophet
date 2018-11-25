from flask_sqlalchemy import SessionBase
from abc import ABC, abstractmethod
from ..models import db


class ServiceBase(ABC):
    def __init__(self, session: SessionBase):
        self.session = session

    def get_page(self, start=1, limit=20):
        query = self.session.query(self.get_model())
        return query.offset(start - 1).limit(limit), query.count()

    @abstractmethod
    def get_model(self) -> db.Model:
        pass