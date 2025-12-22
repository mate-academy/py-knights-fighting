from app.models.knight import Knight


def fight(k1: Knight, k2: Knight) -> None:
    k1.hp -= k2.power - k1.protection
    k2.hp -= k1.power - k2.protection

    if k1.hp < 0:
        k1.hp = 0
    if k2.hp < 0:
        k2.hp = 0
