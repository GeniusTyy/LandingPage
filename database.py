import sqlite3
from config import PATH_DB

class DataBase:
    def __init__(self, path_database):
        self.path_db = path_database

    def connect(self):
        self.conn = sqlite3.connect(self.path_db)
        self.cursor = self.conn.cursor()

if __name__ == '__main__':
    db = DataBase(PATH_DB)
    db.connect()
