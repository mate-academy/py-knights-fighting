from app.battle import Battle
from app.knight_clas import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight.from_dict(config)
        for name, config in knights_config.items()
    }

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for knight1, knight2 in battles:
        Battle(knights[knight1], knights[knight2]).start()

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
