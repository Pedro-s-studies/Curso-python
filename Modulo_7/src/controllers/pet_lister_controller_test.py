from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="dog", id=5),
            PetsTable(name="gatoPreto", type="cat", id=6),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "id": 5},
                {"name": "gatoPreto", "id": 6}
            ],
        }
    }

    assert response == expected_response
