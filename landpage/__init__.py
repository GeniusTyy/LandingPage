<<<<<<< HEAD
=======
# create_app.py

from flask import Flask
from .blueprints.web import web
from config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    EMAIL_USER,
    EMAIL_PASSWORD,
    EMAIL_SMTP_HOST,
    EMAIL_SMTP_PORT,
)
from infra.database import create_db_connection, init_db_command


def create_app():
    app = Flask(__name__)
    app.secret_key = "development"
    app.register_blueprint(web)

    # Configurações do banco de dados
    app.config["DB_PARAMS"] = {
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD,
        "port": POSTGRES_PORT,
        "host": POSTGRES_HOST,
        "dbname": POSTGRES_DB,
    }

    app.config["EMAIL_USER"] = EMAIL_USER
    app.config["EMAIL_PASSWORD"] = EMAIL_PASSWORD
    app.config["EMAIL_SMTP_HOST"] = EMAIL_SMTP_HOST
    app.config["EMAIL_SMTP_PORT"] = EMAIL_SMTP_PORT

    # Inicializa a conexão do banco de dados
    create_db_connection(app)

    # Registra o comando click
    app.cli.add_command(init_db_command)

    return app
>>>>>>> main
