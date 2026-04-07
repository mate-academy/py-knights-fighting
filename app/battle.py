from app.knight import Knight


def fight(knight_a: Knight, knight_b: Knight) -> None:
    power_a = knight_a.power
    power_b = knight_b.power
    knight_a.take_damage(power_b)
    knight_b.take_damage(power_a)
