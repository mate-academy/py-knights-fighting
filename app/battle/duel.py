from app.knights.knight import Knight


def fight(first: Knight, second: Knight) -> None:
    damage_to_first = second.power - first.protection
    damage_to_second = first.power - second.protection

    first.take_damage(damage_to_first)
    second.take_damage(damage_to_second)
