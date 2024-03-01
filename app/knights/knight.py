from typing import List
from .armour import Armour
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[dict],
                 weapon: Weapon,
                 potion: Potion,
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(part=item["part"],
                              protection=item["protection"]
                              ) for item in armour]
        self.weapon = weapon
        self.potion = potion

    def apply_effects(self) -> None:
        self.power += self.weapon["power"]

        if self.potion is not None and self.potion["effect"] is not None:
            for stat, value in self.potion["effect"].items():
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)

    def calculate_protection(self) -> int:
        protection = sum(part.protection for part in self.armour)

        if (self.potion is not None
                and self.potion["effect"] is not None
                and self.potion["effect"].get("protection")):
            protection += self.potion["effect"]["protection"]

        return protection
