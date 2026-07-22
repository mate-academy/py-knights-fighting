from copy import deepcopy


def prepare_knight(knight: dict) -> dict:
    prepared_knight = deepcopy(knight)

    prepared_knight["protection"] = 0
    for armour_item in prepared_knight["armour"]:
        prepared_knight["protection"] += armour_item["protection"]

    prepared_knight["power"] += prepared_knight["weapon"]["power"]

    if prepared_knight["potion"] is not None:
        for stat, value in prepared_knight["potion"]["effect"].items():
            prepared_knight[stat] += value

    return prepared_knight


def prepare_knights(knights_config: dict) -> dict:
    return {
        knight_key: prepare_knight(knight)
        for knight_key, knight in knights_config.items()
    }


def fight(knight1: dict, knight2: dict) -> dict:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0

    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"],
    }
