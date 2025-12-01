# D - Principio da Inversão da Dependência (DIP)
## "Módulos de alto nível não devem depender diretamente dos módulos de baixo nível"
### O Princípio da Inversão da Dependência (DIP) nos diz que os sistemas mais flexíveis são aqueles em que as depêndencias do código-fonte referem-se apenas a abstrações. não a concreções.


from notificator_interface import NotificatorInterface


class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)