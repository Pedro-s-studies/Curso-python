import pytest
from .registry_order_validator import registry_order_Validator


def test_registry_order_validator():
    body = {
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
    registry_order_Validator(body)

def test_registry_order_validator_with_errors():
    body = {
        "data": {
            "named": "Pedrinho",
            "addresses": "Rua do limao",
            "cupom": "false",
            "itens": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "Pizza", "quantidade": 3},
            ],
        }
    }
    with pytest.raises(Exception):
        registry_order_Validator(body)