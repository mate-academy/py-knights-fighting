def damage_calc(attacker: dict, defender: dict) -> int:
    return max(0, attacker["power"] - defender["protection"])


def health_points(knight_1: dict, knight_2: dict) -> None:
    knight_2["hp"] = max(0, knight_2["hp"] - damage_calc(knight_1, knight_2))
    knight_1["hp"] = max(0, knight_1["hp"] - damage_calc(knight_2, knight_1))


def effects(knight: dict) -> None:
    knight["protection"] = sum(
        armour["protection"]
        for armour in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        potion_effects = knight["potion"]["effect"]
        if "power" in potion_effects:
            knight["power"] += potion_effects["power"]
        if "protection" in potion_effects:
            knight["protection"] += potion_effects["protection"]
        if "hp" in potion_effects:
            knight["hp"] += potion_effects["hp"]


def battle(knights_data: dict) -> dict:
    for knight in knights_data.values():
        effects(knight)
    health_points(knights_data["lancelot"], knights_data["mordred"])
    health_points(knights_data["arthur"], knights_data["red_knight"])

    return {knight["name"]: knight["hp"] for knight in knights_data.values()}
