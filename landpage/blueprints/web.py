from flask import Blueprint, redirect, render_template, request
from infra.database import query
from datetime import datetime

web = Blueprint("web", __name__)


@web.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        date = datetime.now().strftime("%d/%m/%Y")

        # TODO: implementar a função para salvar no banco de dados

        return redirect("/")

    return render_template("home.html", message="Hello world"), 200
