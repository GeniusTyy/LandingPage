
import config 
from flask import Flask
from core import models

app = Flask(__name__)
database = models.DataBase(config.PATH_DB)

from core import routes 