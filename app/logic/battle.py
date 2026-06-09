from app.logic.knight import Knight


def fight(
    first_knight: Knight,
    second_knight: Knight
) -> None:
    first_damage = (
        second_knight.power
        - first_knight.protection
    )

    second_damage = (
        first_knight.power
        - second_knight.protection
    )

    first_knight.take_damage(first_damage)

    second_knight.take_damage(second_damage)
