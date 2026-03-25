from typing import Dict
from app.models.knight import Knight


def battle(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    damage_to_k1 = knight2.power - knight1.protection
    damage_to_k2 = knight1.power - knight2.protection

    knight1.take_damage(damage_to_k1)
    knight2.take_damage(damage_to_k2)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
