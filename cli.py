import click
from flask.cli import with_appcontext

@click.command
@with_appcontext
def echo():
    print('echo')