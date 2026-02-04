from app.knight import Knight
from app.utils import duel


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare()

    # Battles (by scenario)
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
