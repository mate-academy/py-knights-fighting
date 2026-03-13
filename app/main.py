from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]
    for player1_name, player2_name in battles:
        p1 = knights[player1_name]
        p2 = knights[player2_name]
        p1.take_damage(p2.power)
        p2.take_damage(p1.power)

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
