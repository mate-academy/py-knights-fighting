from app.apply.armour import apply_armour


def apply_potion(knight: dict) -> tuple:
    knight["protection"] = apply_armour(knight)
    if knight["potion"]:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]

    return knight["power"], knight["protection"], knight["hp"]
