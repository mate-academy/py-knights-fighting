def battle_fight(knights_config) -> dict:
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]
    arthur = knights_config["arthur"]

    fight(lancelot, mordred)
    fight(arthur, red_knight)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


def fight(attacker, defender) -> None:
    attacker["hp"] -= defender["power"] - attacker["protection"]
    defender["hp"] -= attacker["power"] - defender["protection"]
    if attacker["hp"] <= 0:
        attacker["hp"] = 0

    if defender["hp"] <= 0:
        defender["hp"] = 0
