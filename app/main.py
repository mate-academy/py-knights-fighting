from app.knight import Knight
from app.knight import duel


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight.from_config(config)
        for key, config in knights_config.items()
    }

    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
