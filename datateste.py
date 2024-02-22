import sqlite3

class DataBase:
    _instance = None

    def __new__(cls, path_database):
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__new__(cls)
            cls._instance.path_db = path_database 
        return cls._instance
 
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.path_db)
        self.cursor = self.conn.cursor()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    
    def _create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR(255) NOT NULL
                )
            """)
            self.conn.commit()
            print("Tabela criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela: {e}")





with DataBase("teste.db") as db:
    db._create_table()