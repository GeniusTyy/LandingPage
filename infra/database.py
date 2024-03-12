import psycopg2  # Reponsavel por fazer a ponte entre o Python e o Postgres
import click  # Modulo para criar comandos CLI

from flask import current_app, g
from psycopg2 import (
    extras,
)  # Retornar dados em formatos de dicionarios {'nome':'maria'}


from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(**current_app.config["DB_PARAMS"])
        g.db.autocommit = True
        g.db.cursor_factory = extras.RealDictCursor

    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def create_db_connection(app):
    @app.before_request
    def before_request():
        g.db = get_db()

    @app.teardown_appcontext
    def teardown_appcontext(error=None):
        close_db()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db = get_db()
    with current_app.open_resource("../infra/schema.sql") as f:
        db.cursor().execute(f.read().decode("utf8"))
    click.echo("Initialized the database.")
