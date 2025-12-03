class HttpResponse:
    def __init__(self, body: dict, status_cod: int) -> None:
        self.body = body
        self.status_cod = status_cod
    