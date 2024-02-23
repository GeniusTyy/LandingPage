import os
from core.models import DataBase
from dotenv import load_dotenv

load_dotenv()

# Configurações do Email.
USER = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Data Base Config.
PATH = os.path.abspath('data')
PATH_DB = os.path.join(PATH, 'DataBase.db')

# Verifica se o diretório existe, caso não exista, cria-o.
if not os.path.exists(PATH):
    os.makedirs(PATH)

with DataBase(PATH_DB) as db:
    db._create_table()
