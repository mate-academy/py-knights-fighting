def apply_effects(knight: dict) -> None:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for effect_type, effect_value in knight["potion"]["effect"].items():
            if effect_type in ["power", "protection", "hp"]:
                knight[effect_type] += effect_value


def battle(knights_config: dict) -> dict:
    for knight_name, knight_data in knights_config.items():
        apply_effects(knight_data)

    for attacker_name, defender_name in\
            [("lancelot", "mordred"), ("arthur", "red_knight")]:
        attacker = knights_config[attacker_name]
        defender = knights_config[defender_name]

        attacker["hp"] -= max(0, defender["power"] - attacker["protection"])
        defender["hp"] -= max(0, attacker["power"] - defender["protection"])

        attacker["hp"] = max(0, attacker["hp"])
        defender["hp"] = max(0, defender["hp"])

    return {knight_data["name"]: knight_data["hp"]
            for knight_data in knights_config.values()}
