from app.battles.knights_preparing import preparing


def battle(knights_config: dict) -> dict:
    battle_result = {}
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for first_duel, second_duel in pairs:
        first_duel_result = preparing(knights_config[first_duel])
        second_stats_result = preparing(knights_config[second_duel])

        first_duel_result["hp"] -= \
            (
                second_stats_result["power"] - first_duel_result["protection"]
        )
        if first_duel_result["hp"] <= 0:
            first_duel_result["hp"] = 0
        second_stats_result["hp"] -= \
            (
                first_duel_result["power"] - second_stats_result["protection"]
        )
        if second_stats_result["hp"] <= 0:
            second_stats_result["hp"] = 0

        battle_result[first_duel_result["name"]] = first_duel_result["hp"]
        battle_result[second_stats_result["name"]] = second_stats_result["hp"]

    return battle_result
