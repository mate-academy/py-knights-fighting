from app.knight import Knight


def simulate_single_battle(
    first_knight: Knight, second_knight: Knight
) -> None:
    dmg_to_second = first_knight.power - second_knight.protection
    dmg_to_first = second_knight.power - first_knight.protection

    second_knight.hp = max(
        0, second_knight.hp - max(0, dmg_to_second)
    )
    first_knight.hp = max(
        0, first_knight.hp - max(0, dmg_to_first)
    )
