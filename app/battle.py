from app.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> dict:
    # A knight prepares for battle
    for knight in (first_knight, second_knight):
        knight.battle_preparations()

    # The health of the knights after the battle
    first_knight.hp = max(
        first_knight.hp - (second_knight.power - first_knight.protection), 0
    )
    second_knight.hp = max(
        second_knight.hp - (first_knight.power - second_knight.protection), 0
    )

    # Return battle results:
    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp,
    }
