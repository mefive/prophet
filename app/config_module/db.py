from injector import Module, provider
from flask_sqlalchemy import SQLAlchemy


class DBModule(Module):
    def __init__(self, db):
        self.db = db

    @provider
    def provide_db(self) -> SQLAlchemy:
        return self.db
