def get_weapon(knight: dict) -> dict:
    knight["power"] += knight["weapon"]["power"]
    return knight["power"]
