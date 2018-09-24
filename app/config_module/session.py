from injector import Module, provider
from flask_sqlalchemy import SessionBase


class SessionModule(Module):
    def __init__(self, session: SessionBase):
        self.session = session

    @provider
    def provide_db(self) -> SessionBase:
        return self.session
