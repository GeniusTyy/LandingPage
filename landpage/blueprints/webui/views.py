from flask import render_template, flash, current_app


# Define uma função para renderizar a página inicial
def home():

    # Retorna uma string HTML que será renderizada como a página inicial
    flash("Esta é uma mensagem de teste", "success")

    return render_template("home.html")
