from typing import Dict
from app.knight import Knight


class Battle:
    def __init__(self) -> None:
        pass

    def fight(self, knight1: Knight, knight2: Knight) -> Dict[str, int]:
        damage_to_knight1 = max(0, knight2.power - knight1.protection)
        damage_to_knight2 = max(0, knight1.power - knight2.protection)

        knight1.take_damage(damage_to_knight1)
        knight2.take_damage(damage_to_knight2)

        knight1.hp = max(knight1.hp, 0)
        knight2.hp = max(knight2.hp, 0)

        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp,
        }
