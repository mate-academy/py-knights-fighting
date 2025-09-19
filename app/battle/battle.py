from typing import Dict
from app.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    knight1_power = knight1.power_sum()
    knight2_power = knight2.power_sum()
    knight1_protection = knight1.protect_sum()
    knight2_protection = knight2.protect_sum()

    damage_to_knight1 = max(0, knight2_power - knight1_protection)
    damage_to_knight2 = max(0, knight1_power - knight2_protection)

    knight1.hp = max(0, knight1.hp - damage_to_knight1)
    knight2.hp = max(0, knight2.hp - damage_to_knight2)

    return {
        knight1.name: knight1.hp_sum(),
        knight2.name: knight2.hp_sum()
    }
