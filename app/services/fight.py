from app.models.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight_power = first_knight.power
    second_knight_power = second_knight.power

    first_knight.take_damage(second_knight_power)
    second_knight.take_damage(first_knight_power)