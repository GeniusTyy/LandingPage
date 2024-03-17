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
            db = get_db()
            with db.cursor() as db:
                db.execute(
                    "INSERT INTO local (email, data) VALUES (%s, TO_DATE(%s, 'DD/MM/YYYY'))",
                    (email, date)
                )
            send_mail(email)
            # Commit changes to database
            flash("Inscrição realizada com Sucesso!", "sucess")

        except Exception as err:
            print(f"Erro ao processar a solicitação {err}")
            flash("Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde.", "error")
            
        finally:
            return render_template("home.html", message=get_flashed_messages(with_categories=True)), 200
    print(get_flashed_messages(with_categories=True))

    return render_template("home.html", message=get_flashed_messages(with_categories=True)), 200
