import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo padrão (.env)
load_dotenv()

# Verificar se o ambiente está definido como "development" e carregar o arquivo específico
if os.getenv("ENVIRONMENT") == "development":
    load_dotenv(dotenv_path=".env.development")


DATABASE_URL = os.getenv("DATABASE_URL")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
