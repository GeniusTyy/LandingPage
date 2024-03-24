from flask import render_template, flash, current_app
from landpage.ext.database import get_db, init_db


# Define uma função para renderizar a página inicial
def home():
    with current_app.app_context():
        init_db()
    db = get_db()

    # Retorna uma string HTML que será renderizada como a página inicial
    flash("Esta é uma mensagem de teste", "success")

    return render_template("home.html")
