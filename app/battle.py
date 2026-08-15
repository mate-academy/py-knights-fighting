from app.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    k1_damage_power = knight1.power
    k2_damage_power = knight2.power

    knight1.take_damage(k2_damage_power)
    knight2.take_damage(k1_damage_power)
