from flask import render_template, flash, current_app, request
from datetime import datetime

from landpage.models import User
from landpage.ext.database import db


# Define uma função para renderizar a página inicial
def home():
    if request.method == "POST":

        # Pegando o email informado no formulario.
        email = request.form.get("email")

        # Formata a data corretamente para o formato 'YYYY-MM-DD'
        data = datetime.now().strftime("%Y-%m-%d")
        try:

            # Cria um novo objeto User
            user = User(email=email, date=data)

            # Adiciona o novo usuário à sessão do banco de dados
            db.session.add(user)

            # Confirma as mudanças no banco de dados
            db.session.commit()

            flash("Inscrição realizada com Sucesso!", "sucess")
        except Exception as err:
            flash(
                "Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde.",
                "error",
            )
            pass

    return render_template("home.html")