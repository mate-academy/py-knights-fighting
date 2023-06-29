from typing import List

from app.upgrades.armour import Armour
from app.upgrades.potion import Potion
from app.upgrades.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour],
            weapon: Weapon,
            potion: Potion,
    ):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0  # 0 by default
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    @classmethod
    def from_dict(cls, knight_data: dict):
        armour = [Armour(**armour_data) for armour_data in knight_data.pop("armour")]
        weapon = Weapon(**knight_data.pop("weapon"))
        potion = None if (potion_data := knight_data.pop("potion")) is None else Potion(**potion_data)

        return cls(
            **knight_data,
            armour=armour,
            weapon=weapon,
            potion=potion
        )

    def apply_armour(self):
        self.protection += sum(armour.protection for armour in self.armour)

    def apply_weapon(self):
        self.power += self.weapon.power

    def apply_potion(self):
        if self.potion is None:
            return

        stats = ("power", "hp", "protection")
        for stat in stats:
            if stat in self.potion.effect:
                setattr(self, stat, getattr(self, stat) + self.potion.effect[stat])

    def battle(self, other):
        self.hp = max(0, self.hp - other.power + self.protection)
        other.hp = max(0, other.hp - self.power + other.protection)