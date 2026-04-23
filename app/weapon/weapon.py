def apply_weapon(knights_data: dict) -> dict:
    for knight in knights_data.values():
        knight["power"] += knight["weapon"]["power"]
    return knights_data
