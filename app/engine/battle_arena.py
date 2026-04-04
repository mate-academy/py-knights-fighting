from app.models.knight import Knight  # Capital K


def fight(knight1: Knight, knight2: Knight) -> None:
    damage_to_k1 = max(0, knight2.power - knight1.protection)
    damage_to_k2 = max(0, knight1.power - knight2.protection)

    knight1.take_damage(damage_to_k1)
    knight2.take_damage(damage_to_k2)
