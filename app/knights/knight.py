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
                 protection=None
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(part=item["part"],
                              protection=item["protection"]
                              ) for item in armour]
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_effects(self) -> None:
        self.power += self.weapon["power"]
        self.protection = sum(part.protection for part in self.armour)

        if self.potion is not None and self.potion["effect"] is not None:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat, 0) + value)
