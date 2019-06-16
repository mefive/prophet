from flask.cli import with_appcontext
from flask_migrate import Migrate
from app import create_app, db
from app.services.index_basic_service import IndexBasicService
from app.services.index_daily_service import IndexDailyService
from app.models.index_basic import IndexBasic
from app.models.index_basic import IndexBasicSchema
import click
import datetime
from dateutil.relativedelta import relativedelta

app = create_app('development')

Migrate(app, db)


@app.cli.command()
@click.argument('market')
def import_index_basic(market):
    service = IndexBasicService(db.session)
    service.import_index_basic(market)


@app.cli.command()
@click.argument('ts_code')
def import_index_daily(ts_code):
    service = IndexDailyService(db.session)

    today = datetime.date.today()

    from app.models import IndexBasic

    index_basic = db.session.query(IndexBasic).limit(20).all()

    # service.import_index_daily(
    #     ts_code=ts_code,
    #     end_date=today.strftime('%Y%m%d'),
    #     start_date=(today - relativedelta(year=10)).strftime('%Y%m%d')
    # )


@app.cli.command()
@with_appcontext
def index_basic_page():
    service = IndexBasicService(db.session)
    (index_basic_list, count) = service.get_page(1, 20)

    for index_basic in index_basic_list:
        print(IndexBasicSchema().dump(index_basic))


@app.cli.command()
def echo():
    print('echo')
