from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:

    def calculate(self, request: FlaskRequest) -> None:
        body = request.json
        input_data = self.__validate_body(body)
        calculate_mean = self.__process_data(input_data)

        response = self.__format_response(calculate_mean)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or len(body["numbers"]) <= 1:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        sum_values = sum(input_data)
        qtd_values = len(input_data)

        calculate = sum_values / qtd_values
        return calculate

    def __format_response(self, calc_result: float) -> Dict:
        return {"data": {"Calculator": 4, "result": round(calc_result, 2)}}
