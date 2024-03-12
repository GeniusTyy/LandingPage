from flask import Blueprint, redirect, render_template, request
from datetime import datetime

from infra.database import get_db

web = Blueprint("web", __name__)


@web.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        date = datetime.now().strftime("%d/%m/%Y")

        # Inicia uma instacia do banco de dados..
        db = get_db()

        # Insere o valor no banco.
        db.cursor().execute(
            "INSERT INTO local (email, data) VALUES(%s, %s)", (email, date)
        )

        return redirect("/")

    return render_template("home.html", message="Hello world"), 200
