from typing import Dict
from app.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    knight1.take_damage(knight2.power_sum())
    knight2.take_damage(knight1.power_sum())
    return {
        knight1.name: knight1.hp_sum(),
        knight2.name: knight2.hp_sum()
    }
