from app.knights.knight import Knight


def prepare(knight: Knight) -> Knight:
    knight.get_protection()
    knight.get_power()
    knight.get_hp()

    return knight
