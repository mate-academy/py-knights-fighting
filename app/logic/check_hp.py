from app.knights.knight import Knight


def check_hp(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
