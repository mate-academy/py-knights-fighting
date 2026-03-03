from typing import Dict
from app.knight import Knight


def battle_between(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    knight1.prepare_for_battle()
    knight2.prepare_for_battle()

    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
