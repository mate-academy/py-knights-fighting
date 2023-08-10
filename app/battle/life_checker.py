from app.knights.data import Knight
# This function check knight health points


def life_check(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
