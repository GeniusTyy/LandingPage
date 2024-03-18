from landpage.ext.mail import send_mail
import requests
import time


def test_email_receipt(app):
    """
    Teste para validar o recebimento do email
    """
    recipient = "test@test.com"
    with app.app_context():
        send_mail(recipient)

    # Esperando um tempo para garantir que o email chegou
    time.sleep(2)

    response = requests.get("http://localhost:1080/messages")
    assert response.status_code == 200

    data = response.json()

    # TODO: arrumar os testes
    found = 
    for item in data:
        email = [
            recipient.replace("<", "").replace(">", "")
            for recipient in item["recipients"]
        ]
        assert recipient in email
