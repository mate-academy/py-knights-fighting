from app.models.armour import get_total_protection

# Your KNIGHTS dict goes here
KNIGHTS = {...}


def prepare_knight(knight: dict) -> dict:
    knight = knight.copy()  # Don't mutate original

    # Apply armour
    knight["protection"] = get_total_protection(knight["armour"])

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion
    if knight.get("potion"):
        effect = knight["potion"]["effect"]
        if "power" in effect:
            knight["power"] += effect["power"]
        if "protection" in effect:
            knight["protection"] += effect["protection"]
        if "hp" in effect:
            knight["hp"] += effect["hp"]

    return knight
