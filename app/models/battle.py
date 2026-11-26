from typing import Dict
from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    power1 = knight1.power
    power2 = knight2.power
    knight1.take_damage(power2)
    knight2.take_damage(power1)


def battle(knights_config: dict) -> Dict[str, int]:
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
