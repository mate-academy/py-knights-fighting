from app.knight.one_knight import Knight


def weapon_preparation(knight: Knight) -> int:
    knight.power += knight.weapon["power"]
    return knight.power
