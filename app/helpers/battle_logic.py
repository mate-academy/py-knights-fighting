from app.models.knight import Knight


def fight(k1: Knight, k2: Knight) -> None:
    damage_to_k1 = k2.power - k1.protection
    damage_to_k2 = k1.power - k2.protection

    k1.hp = max(0, k1.hp - damage_to_k1)
    k2.hp = max(0, k2.hp - damage_to_k2)
