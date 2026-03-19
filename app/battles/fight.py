from copy import deepcopy


def fight(knight1: dict, knight2: dict) -> dict:
    knight1 = deepcopy(knight1)
    knight2 = deepcopy(knight2)
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0

    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"]
    }
