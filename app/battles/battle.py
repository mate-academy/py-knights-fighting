from app.battles.prepare import preparing


def battle(knights_config: dict) -> dict:
    battle_result = {}
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for first_duel, second_duel in pairs:
        first_out = preparing(knights_config[first_duel])
        second_out = preparing(knights_config[second_duel])

        first_out["hp"] -= (second_out["power"] - first_out["protection"])
        if first_out["hp"] <= 0:
            first_out["hp"] = 0
        second_out["hp"] -= (first_out["power"] - second_out["protection"])
        if second_out["hp"] <= 0:
            second_out["hp"] = 0

        battle_result[first_out["name"]] = first_out["hp"]
        battle_result[second_out["name"]] = second_out["hp"]

    return battle_result
