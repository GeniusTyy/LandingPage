
from config import PATH, PATH_DB, USER, PASSWORD
from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)
app.secret_key = 'gjfakkjfasijgçalkgk'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = USER
app.config['MAIL_PASSWORD'] = PASSWORD

mail = Mail(app)


from core import routes 