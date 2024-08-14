from typing import Dict
from app.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> Dict[str, int]:
        self.knight1.hp -= max(0, self.knight2.power - self.knight1.protection)
        self.knight2.hp -= max(0, self.knight1.power - self.knight2.protection)
        self.knight1.hp = max(0, self.knight1.hp)
        self.knight2.hp = max(0, self.knight2.hp)
        return {
            self.knight1.name.title(): self.knight1.hp,
            self.knight2.name.title(): self.knight2.hp
        }
