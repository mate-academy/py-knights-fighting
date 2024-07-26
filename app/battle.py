from typing import Dict
from app.knights import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> Dict[str, int]:
        knight1_hp = (self.knight1.hp
                      - (self.knight2.power - self.knight1.protection))
        knight2_hp = (self.knight2.hp
                      - (self.knight1.power - self.knight2.protection))

        knight1_hp = max(0, knight1_hp)
        knight2_hp = max(0, knight2_hp)

        return {
            self.knight1.name: knight1_hp,
            self.knight2.name: knight2_hp
        }
