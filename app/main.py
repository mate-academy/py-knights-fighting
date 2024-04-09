from app.battle_preparations import knight_preparations


def knights_battle(first_op: dict, second_opp: dict) -> None:
    first_op["hp"] -= (second_opp["power"] - first_op["protection"])
    second_opp["hp"] -= first_op["power"] - second_opp["protection"]

    if first_op["hp"] <= 0:
        first_op["hp"] = 0

    if second_opp["hp"] <= 0:
        second_opp["hp"] = 0


def battle(knights_config: dict) -> dict:
    lancelot = knight_preparations(knights_config["lancelot"])
    arthur = knight_preparations(knights_config["arthur"])
    mordred = knight_preparations(knights_config["mordred"])
    red_knight = knight_preparations(knights_config["red_knight"])

    knights_battle(lancelot, mordred)
    knights_battle(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
