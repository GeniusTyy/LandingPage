from flask import g, current_app
import sqlite3

DB_PATH = "test.db"


# função por pegar uma instancia do banco de dados.
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
    return db


# função por inicializar o banco de dados e carregar os schemas.
def init_db():
    with current_app.app_context():
        db = get_db()
        with current_app.open_resource("ext/schemas/schema.sql") as file:
            db.executescript(file.read().decode("utf8"))


# função reponsavel por encerrar o banco de dados.
def close_db(e=None):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# função responsavel por inicializar o banco de dados.
def init_app(app):
    app.teardown_appcontext(close_db)
