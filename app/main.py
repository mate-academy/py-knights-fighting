from copy import deepcopy

from app.knight.knight import Knight
from app.fight.fight import fight


def battle(knights_config: dict) -> dict:
    config = deepcopy(knights_config)

    knights = {
        key: Knight(data)
        for key, data in config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
