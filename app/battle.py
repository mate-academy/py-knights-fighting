from app.knights import Knight


def battle(knights_config: dict) -> dict:
    knights = {key: Knight(**value) for key, value in knights_config.items()}

    for knight in knights.values():
        knight.calculate_stats()

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for knight1, knight2 in battles:
        knights[knight1].take_damage(
            knights[knight2].total_power - knights[knight1].protection
        )
        knights[knight2].take_damage(
            knights[knight1].total_power - knights[knight2].protection
        )

    return {knight.name: knight.hp for knight in knights.values()}
