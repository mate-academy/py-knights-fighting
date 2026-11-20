from app.knights.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_damage = second_knight.power - first_knight.protection
    second_damage = first_knight.power - second_knight.protection
    damage_pairs = (
        (first_knight, first_damage),
        (second_knight, second_damage),
    )
    for knight, damage in damage_pairs:
        knight.take_damage(damage)
