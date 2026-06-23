from typing import List

from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp

    def add_armour(self, armours: List[Armour]) -> None:
        for armour in armours:
            self.protection += armour.protection

    def add_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def add_potion(self, potion: Potion) -> None:
        effect = potion.effect
        self.protection += effect.get("protection", 0)
        self.power += effect.get("power", 0)
        self.hp += effect.get("hp", 0)
