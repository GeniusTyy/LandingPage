import sqlite3

# Uma classe Singleton para garantir que ela seja instanciada apenas uma vez!
class DataBase:
    _instance = None
    
    def __new__(cls, path_database):
        # Verifica se a instância já existe; se não, cria uma nova
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__new__(cls)
            cls._instance.path_db = path_database 
        return cls._instance
 
    
    def __enter__(self):
        # Context manager para lidar com a abertura do banco de dados
        self.conn = sqlite3.connect(self.path_db)
        self.cursor = self.conn.cursor()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        # Context manager para lidar com o fechamento do banco de dados
        self.conn.close()

    
    def _create_table(self):
        try:
            # Cria a tabela se ela não existir
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR(255) NOT NULL,
                    registration_date DATE NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela: {e}")


    def _append(self, email:str, date:str):
        # TODO: Efetuar Tratamento de ERROS.
        self.cursor.execute("INSERT INTO Data (email, registration_date) VALUES(?, ?)", (email, date))
        self.conn.commit()
            
    
    def _get_all(self):
        self.cursor.execute("SELECT * FROM Data")
        data = self.cursor.fetchall()
        return data

# Quando este script é executado diretamente
if __name__ == '__main__':
    # Uso do contexto do banco de dados para criar a tabela
    with DataBase("teste.db") as db:
        db._create_table()
