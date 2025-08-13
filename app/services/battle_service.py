from app.models.knight import Knight


def fight(k1: Knight, k2: Knight) -> None:
    k1.hp -= max(k2.power - k1.protection, 0)
    k2.hp -= max(k1.power - k2.protection, 0)

    if k1.hp < 0:
        k1.hp = 0
    if k2.hp < 0:
        k2.hp = 0
