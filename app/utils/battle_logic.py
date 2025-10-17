from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    damage_to_1 = max(knight2.power - knight1.protection, 0)
    damage_to_2 = max(knight1.power - knight2.protection, 0)

    knight1.take_damage(damage_to_1)
    knight2.take_damage(damage_to_2)
