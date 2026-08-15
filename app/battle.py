from app.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.prepare_for_battle()
    second_knight.prepare_for_battle()

    first_knight.receive_damage(
        second_knight.power - first_knight.protection
    )
    second_knight.receive_damage(
        first_knight.power - second_knight.protection
    )
