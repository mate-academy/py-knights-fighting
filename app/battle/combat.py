from typing import Dict
from app.models.knight import Knight


class Combat:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def engage(self) -> None:
        if self.knight1.magic:
            self.knight1.apply_magic()

        if self.knight2.magic:
            self.knight2.apply_magic()

        # Knight1 attacks Knight2
        self.knight2.take_damage(self.knight1.power)

        # Knight2 attacks Knight1
        self.knight1.take_damage(self.knight2.power)

    def get_result(self) -> Dict[str, int]:
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp
        }
