# Importa a classe Flask do módulo flask
from flask import Flask 

# Importa o blueprint 'webui' do módulo api.blueprints
from api.blueprints import webui

# Define uma função para criar a aplicação Flask
def create_app():
    # Cria uma instância da aplicação Flask
    app = Flask(__name__)
    # Inicializa o blueprint 'webui' com a aplicação Flask
    webui.init_app(app)

    # Retorna a aplicação Flask
    return app
