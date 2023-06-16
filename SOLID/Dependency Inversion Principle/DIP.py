
"""
Nesse exemplo, a classe NotificationService depende de uma abstração 
(a classe EmailSender) em vez de uma implementação concreta. 
Isso permite que diferentes implementações de EmailSender sejam 
injetadas no NotificationService, facilitando a substituição e a extensão. 
O DIP inverte a dependência em relação às camadas de alto nível e baixo nível, 
promovendo um código mais flexível e desacoplado.
"""

class EmailSender:
    def send_email(self, to, subject, body):
       return f"to: {to}, \nsubject: {subject} \nbody: {body}"
        

class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def send_notification(self, user, message):
        return f"user: {user} \nmessage: {message}"

if __name__ == "__main__":
    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)
