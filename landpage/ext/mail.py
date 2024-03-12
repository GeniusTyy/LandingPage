import smtplib
from email.mime.text import MIMEText
from flask import current_app


# Configurações do email


# TODO: Mudar para o Mailcatcher de forma dinamica
def send_mail(target):

    # Configurações para o servidor SMTP do Mailcatcher
    smtp_server = current_app.config["EMAIL_SMTP_HOST"]
    smtp_port = current_app.config["EMAIL_SMTP_PORT"]
    smtp_user = current_app.config["EMAIL_USER"]
    smtp_password = current_app.config["EMAIL_PASSWORD"]

    sender_email = smtp_user
    receiver_email = target

    subject = "Incrição"

    body = """<!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parabéns pela Inscrição!</title>
    <style>
        body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        background-color: #000;
        color: #fff;
        margin: 0;
        padding: 0;
        text-align: center;
        }

        .container {
        max-width: 600px;
        margin: 50px auto;
        padding: 20px;
        background-color: #222;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }

        h1 {
        color: #fff;
        }

        p {
        color: #ccc;
        }

        .emoji {
        font-size: 30px;
        margin-bottom: 10px;
        }
    </style>
    </head>

    <body>
    <div class="container">
        <div class="emoji">🎉</div>
        <h1>Parabéns!</h1>
        <p>Obrigado por se inscrever na nossa newsletter.</p>
        <p>Fique ligado para receber as últimas notícias e atualizações.</p>
        
        <p>📬🎊</p>
    </div>
    </body>

    </html>

    """

    # Configuração da mensagem
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        # Conexão e envio do email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, [receiver_email], msg.as_string())
            print("Email enviado com sucesso!")

    except Exception as err:
        print(f"Erro ao enviar Email: {err}")
