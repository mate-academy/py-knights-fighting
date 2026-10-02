def apply_equipment(knight: dict) -> dict:
    """Applies armour, weapon and potion effects to a single knight."""
    knight["protection"] = 0
    for piece in knight["armour"]:
        knight["protection"] += piece["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]

        if "power" in effect:
            knight["power"] += effect["power"]

        if "protection" in effect:
            knight["protection"] += effect["protection"]

        if "hp" in effect:
            knight["hp"] += effect["hp"]

    return knight
