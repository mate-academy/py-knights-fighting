from app.knight import Knight


def fight(first: Knight = None, second: Knight = None) -> dict:
    first.prepare()
    second.prepare()

    damage_to_first_knight = max(0, second.power - first.protection)
    damage_to_second_knight = max(0, first.power - second.protection)

    first.take_damage(damage_to_first_knight)
    second.take_damage(damage_to_second_knight)

    return {first.name: first.hp, second.name: second.hp}
