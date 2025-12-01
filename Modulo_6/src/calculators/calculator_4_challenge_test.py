from typing import Dict
from pytest import raises
from .calculator_4_challenge import Calculator4


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [2, 3, 5, 7, 10]})
    calculator_4 = Calculator4()

    response = calculator_4.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 5.4
    assert response["data"]["Calculator"] == 4


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"number": [1]})
    calculator_4 = Calculator4()

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"