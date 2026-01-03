from app.knights.knight import Knight


def prepare(knight: Knight) -> None:
    knight.get_protection()
    knight.get_power()
    knight.get_hp()
