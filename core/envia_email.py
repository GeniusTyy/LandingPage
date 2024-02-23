from core import app, mail, USER, Message

class SendMail:
    def __enter__(self):
        try:
            return self  # Retorna a instância correta para o contexto
        except Exception as e:
            print(f"Erro ao conectar ao servidor SMTP: {e}")
            return None  # Retorna None se ocorrer um erro

    def send_mail(self, email: str, msg: str):
        with app.app_context():
            message = Message()
            message.body = msg
            message.subject = 'Testando o Envio de E-mail'
            message.sender = USER
            message.recipients = [email]  # Altere para o destinatário desejado

            mail.send(message)

    def __exit__(self, exc_type, exc_value, traceback):
        pass  # Não é necessário fazer nada ao sair do contexto, pois o Flask-Mail gerencia a conexão automaticamente
