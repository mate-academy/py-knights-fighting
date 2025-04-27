from app.battle_preparations import prepare_knight


def calculate_damage(attacker: dict, defender: dict) -> dict:
    defender_copy = defender.copy()
    defender_copy["hp"] -= attacker["power"] - defender_copy["protection"]

    if defender_copy["hp"] < 0:
        defender_copy["hp"] = 0

    return defender_copy


def battle(knights_config: dict) -> dict:

    lancelot_ready = prepare_knight(knights_config["lancelot"])
    arthur_ready = prepare_knight(knights_config["arthur"])
    mordred_ready = prepare_knight(knights_config["mordred"])
    red_knight_ready = prepare_knight(knights_config["red_knight"])

    mordred_ready = calculate_damage(lancelot_ready, mordred_ready)
    lancelot_ready = calculate_damage(mordred_ready, lancelot_ready)

    red_knight_ready = calculate_damage(arthur_ready, red_knight_ready)
    arthur_ready = calculate_damage(red_knight_ready, arthur_ready)

    return {
        lancelot_ready["name"]: lancelot_ready["hp"],
        arthur_ready["name"]: arthur_ready["hp"],
        mordred_ready["name"]: mordred_ready["hp"],
        red_knight_ready["name"]: red_knight_ready["hp"],
    }
