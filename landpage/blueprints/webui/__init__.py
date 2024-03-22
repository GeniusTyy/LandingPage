# Importa a classe Blueprint do módulo flask
from flask import Blueprint

# Importa a função 'home' do módulo views
from landpage.blueprints.webui.views import home

# TODO: Corrigir o problema de importação relacionado ao static.
# Cria um objeto Blueprint com o nome 'webui'
bp = Blueprint('webui', __name__, static_folder='static', template_folder='templates')


# Adiciona uma regra de URL para a rota raiz ("/") que renderiza a função 'home'
bp.add_url_rule("/", view_func=home)


# Define uma função para inicializar o blueprint 'webui' com a aplicação Flask
def init_app(app):
    # Registra o blueprint 'webui' na aplicação Flask
    app.register_blueprint(bp)
