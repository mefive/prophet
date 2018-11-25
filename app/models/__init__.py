from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .daily import Daily
from .stock_basic import StockBasic
from .daily_basic import DailyBasic
from .index_basic import IndexBasic
from .index_daily import IndexDaily
