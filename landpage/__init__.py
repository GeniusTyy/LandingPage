from flask import Flask
from .blueprints.api import api
from .blueprints.web import web


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(web)

    return app
