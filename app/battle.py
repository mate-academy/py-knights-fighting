def battle(knight1: dict, knight2: dict) -> None:
    damage_to_1 = max(0, knight2["power"]) - knight1["protection"]
    damage_to_2 = max(0, knight1["power"]) - knight2["protection"]

    knight1["hp"] -= damage_to_1
    knight2["hp"] -= damage_to_2

    if knight1["hp"] <= 0:
        knight1["hp"] = 0
    if knight2["hp"] <= 0:
        knight2["hp"] = 0


def battle_round(
    lancelot: dict,
    mordred: dict,
    arthur: dict,
    red_knight: dict,
) -> dict:
    battle(lancelot, mordred)
    battle(arthur, red_knight)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"]
    }
