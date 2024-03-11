# Módulo responsável por gerenciar a conexão com o banco de dados
import psycopg2
from config import (
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_DB,
    POSTGRES_PORT,
    POSTGRES_USER,
)


class Database:
    def __init__(self):
        pass

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            host=POSTGRES_HOST,
            password=POSTGRES_PASSWORD,
            port=POSTGRES_PORT,
        )

    # TODO: Adicionar a classe responsavel por criar as tabelas
    def create_table():
        pass
