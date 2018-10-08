import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lkjasdkljalsd'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@localhost/stock?charset=utf8&use_unicode=1'.format(
        os.environ.get('DEV_DB_USER'),
        os.environ.get('DEV_DB_PASSWORD'),
    )


config = {
    'development': DevelopmentConfig
}
