from typing import Callable


class Battle:
    def __init__(self, knight1: str, knight2: str) -> Callable:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> dict:
        self.knight1.take_damage(self.knight2.power)
        self.knight2.take_damage(self.knight1.power)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
