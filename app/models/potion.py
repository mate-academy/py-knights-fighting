def create_potion(name: str, effect: dict) -> dict:
    return {"name": name, "effect": effect}


def apply_potion(knight: dict, potion: dict) -> dict:
    if not potion:
        return knight

    effect = potion["effect"]
    if "power" in effect:
        knight["power"] += effect["power"]
    if "protection" in effect:
        knight["protection"] += effect["protection"]
    if "hp" in effect:
        knight["hp"] += effect["hp"]

    return knight
