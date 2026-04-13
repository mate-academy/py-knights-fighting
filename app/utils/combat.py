from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    damage_to_k1 = max(0, knight2.power - knight1.protection)
    damage_to_k2 = max(0, knight1.power - knight2.protection)

    knight1.hp -= damage_to_k1
    knight2.hp -= damage_to_k2

    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)
