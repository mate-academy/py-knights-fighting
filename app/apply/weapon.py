def apply_weapon(knight: dict) -> int:
    knight["power"] += knight["weapon"]["power"]
    return knight["power"]
