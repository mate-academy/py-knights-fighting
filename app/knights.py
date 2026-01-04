def apply_effects(knight: dict) -> None:
    knight["protection"] = sum(arm["protection"] for arm in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        potion_effects = knight["potion"]["effect"]
        if "power" in potion_effects:
            knight["power"] += potion_effects["power"]
        if "protection" in potion_effects:
            knight["protection"] += potion_effects["protection"]
        if "hp" in potion_effects:
            knight["hp"] += potion_effects["hp"]


def damage_calculation(attacker: dict, defender: dict) -> int:
    return max(0, attacker["power"] - defender["protection"])


def knight_battle(knight1: dict, knight2: dict) -> None:
    damage_to_knight2 = damage_calculation(knight1, knight2)
    damage_to_knight1 = damage_calculation(knight2, knight1)

    knight2["hp"] = max(0, knight2["hp"] - damage_to_knight2)
    knight1["hp"] = max(0, knight1["hp"] - damage_to_knight1)


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        apply_effects(knight)

    knight_battle(knights_config["lancelot"], knights_config["mordred"])
    knight_battle(knights_config["arthur"], knights_config["red_knight"])

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}
