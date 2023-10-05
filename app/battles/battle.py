from app.battles.prepare import prepare_for_battle


def battle(knights_config: dict) -> dict:
    battle_result = {}
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for first_duel, second_duel in pairs:
        first_out = prepare_for_battle(knights_config[first_duel])
        second_out = prepare_for_battle(knights_config[second_duel])

        first_out["hp"] -= (second_out["power"] - first_out["protection"])
        first_out["hp"] = max(first_out["hp"], 0)
        second_out["hp"] -= (first_out["power"] - second_out["protection"])
        second_out["hp"] = max(second_out["hp"], 0)

        battle_result[first_out["name"]] = first_out["hp"]
        battle_result[second_out["name"]] = second_out["hp"]

    return battle_result
