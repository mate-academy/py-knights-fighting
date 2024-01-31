from app.battle.pre_battle import prepare_knights


def battle(knights_one: dict) -> dict:

    prepare_knights(knights_one)

    lancelot = knights_one["lancelot"]
    mordred = knights_one["mordred"]
    arthur = knights_one["arthur"]
    red_knight = knights_one["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    result_dict = {}

    for knight in knights_one:
        if knights_one[knight]["hp"] <= 0:
            knights_one[knight]["hp"] = 0
        result_dict[knights_one[knight]["name"]] = knights_one[knight]["hp"]

    return result_dict
