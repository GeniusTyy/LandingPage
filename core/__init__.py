
from config import PATH, PATH_DB
from flask import Flask

app = Flask(__name__)
app.secret_key = 'gjfakkjfasijgccalkgk'

from core import routes 
