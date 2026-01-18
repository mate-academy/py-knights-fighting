from app.entities.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(key, config)
        for key, config in knights_config.items()
    }

    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for k1, k2 in pairs:
        Battle(knights[k1], knights[k2]).start()

    return {
        knight.name: max(knight.hp, 0)
        for knight in knights.values()
    }
