from flask import Flask, request, jsonify
from models.diet import Diet
from datetime import datetime

app = Flask(__name__)

diets = []
diet_id_control = 1


@app.route("/diets", methods=["POST"])
def create_diet():

    global diet_id_control
    data = request.get_json()

    new_diet = Diet(
        id=diet_id_control,
        name=data["name"],
        description=data["description"],
        datetime=datetime.now(),
        is_diet=data["is_diet"],
    )
    diet_id_control += 1

    diets.append(new_diet)
    return jsonify(
        {"message": "Nova refeição da dieta criada com sucesso!", "id": new_diet.id}
    )


@app.route("/diets", methods=["GET"])
def get_diets():

    diet_list = [diet.to_dict() for diet in diets]

    output = {"diets": diet_list, "total_diets": len(diet_list)}

    return output


@app.route("/diets/<int:id>", methods=["GET"])
def get_diet(id):

    for d in diets:
        if d.id == id:
            return jsonify(d.to_dict())

    return jsonify({"message": "Não foi possível encontrar a dieta solicitada!"}), 404


@app.route("/diets/<int:id>", methods=["PUT"])
def update_diet(id):
    diet = None

    for d in diets:
        if d.id == id:
            diet = d
            break

    print(diet)
    if diet == None:
        return (
            jsonify({"message": "Não foi possível encontrar a dieta solicitada!"}),
            404,
        )

    data = request.get_json()
    diet.name = data["name"]
    diet.description = data["description"]
    diet.is_diet = data["is_diet"]

    print(diet)
    return jsonify({"message": "dieta atualizada com sucesso!"})


@app.route("/diets/<int:id>", methods=["DELETE"])
def delete_diet(id):
    diet = None

    for t in diets:
        if t.id == id:
            diet = t
            break

    if not diet:
        return (
            jsonify({"message": "Não foi possível encontrar a dieta solicitada!"}),
            404,
        )

    diets.remove(diet)

    return jsonify({"message": "dieta deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
