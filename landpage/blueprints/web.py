from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    get_flashed_messages,
    flash,
)
from datetime import datetime

from infra.database import get_db
from landpage.ext.mail import send_mail

web = Blueprint("web", __name__)


@web.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        date = datetime.now().strftime("%d/%m/%Y")

        try:
            # Inicia uma instacia do banco de dados..
            #db = get_db()
            #with db.cursor() as db:
            #    db.execute(
            #        "INSERT INTO local (email, data) VALUES(%s, %s)", (email, date)
            #    )
            send_mail(email)

        except Exception as err:
            print(f"Erro ao processar a solicitação {err}")

        return redirect("/")

    return render_template("home.html", message="Hello world"), 200
