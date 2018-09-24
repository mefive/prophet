from flask_sqlalchemy import SessionBase


class ServiceBase:
    def __init__(self, session: SessionBase):
        self.session = session
