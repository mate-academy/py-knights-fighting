from app.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.take_damage(second_knight.power)
    second_knight.take_damage(first_knight.power)
