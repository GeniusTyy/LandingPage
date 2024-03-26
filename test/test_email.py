from landpage.ext.mail import send_mail
import requests
import time


def test_send_valid_email(app):
    """
    Teste para testar o envio de emails validos.
    """
    valid_emails = [
        "valid@proton.me",
        "test-name@domain.com",
        "test-name1@domain.com",
        "test@name.com.org",
        "test@name.gov",
    ]

    for email in valid_emails:
        with app.app_context():
            assert send_mail(email) == True


def test_send_invalid_email(app):
    """
    Teste para verificar o envio de emails invalidos
    """
    invalid_emails = [
        "email.com",
        "email@.com",
        "email@domain",
        "email@domain.",
        "email@domain.com.",
        "email@domain.com..",
        "email@domain.com@domain.com",
        "email@domain.com#",
        "email@domain.com$",
        "email@domain.com%",
        "email@domain.com^",
        "email@domain.com&",
        "email@domain.com*",
        "email@domain.com(",
        "email@domain.com)",
        "email@domain.com-",
        "email@domain.com_",
        "email@domain.com+",
        "email@domain.com=",
        "email@domain.com[",
        "email@domain.com]",
        "email@domain.com{",
        "email@domain.com}",
        "email@domain.com|",
        "email@domain.com\\",
        "email@domain.com;",
        "email@domain.com:",
        "email@domain.com'",
        'email@domain.com"',
        "email@domain.com<",
        "email@domain.com>",
        "email@domain.com,",
        "email@domain.com?",
        "email@domain.com/",
        "email-te.com",
    ]

    for email in invalid_emails:
        with app.app_context():
            assert send_mail(email) == False


def test_email_receipt(app):
    """
    Teste para validar o recebimento do email
    """
    recipient = "test@test.com"
    with app.app_context():
        send_mail(recipient)

    # Esperando um tempo para garantir que o email chegou
    time.sleep(2)

    # Coleta as mensagens recebidas pelo mailcatcher
    response = requests.get("http://localhost:1080/messages")
    assert response.status_code == 200

    data = response.json()

    # Verifica se o email consta na caixa de entrada do email catcher.
    found = False
    for item in data:
        email = [
            recipient.replace("<", "").replace(">", "")
            for recipient in item["recipients"]
        ]
        if recipient in email:
            found = True
            break

    assert found == True
