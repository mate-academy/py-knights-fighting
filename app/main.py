from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = Knight.knights_from_dict(knights_config)

    lancelot, arthur, mordred, red_knight = knights

    for knight in knights:
        knight.drink_potion()

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    knights_stats = {}
    for knight in knights:
        knights_stats[knight.name] = knight.hp

    return knights_stats
