from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder


class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}

    def insert_document(self, document: dict) -> None:
        self.insert_document_att["document"] = document


def test_registry():
    repo = OrdersRepositoryMock()
    registry_order = RegistryOrder(repo)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "Pedrinho",
                "address": "Rua do limao",
                "cupom": False,
                "itens": [
                    {"item": "Refrigerante", "quantidade": 2},
                    {"item": "Pizza", "quantidade": 3},
                ],
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert "name" in repo.insert_document_att["document"]
    assert "address" in repo.insert_document_att["document"]
    assert "created_at" in repo.insert_document_att["document"]
