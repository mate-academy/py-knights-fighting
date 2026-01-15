from typing import Dict
from app.models.knight import Knight


def battle_knights(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    damage_to_knight1 = max(
        0, knight2.total_power() - knight1.total_protection()
    )
    damage_to_knight2 = max(
        0, knight1.total_power() - knight2.total_protection()
    )

    knight1.hp = max(0, knight1.hp - damage_to_knight1)
    knight2.hp = max(0, knight2.hp - damage_to_knight2)
    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
