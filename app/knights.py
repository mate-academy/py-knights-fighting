from typing import List
from armour import Armour, helmet, breastplate, boots
from weapon import Weapon, metal_sword, two_handed_sword, poisoned_sword, sword
from potion import Potion, berserk, blessing


class Knight:
    knights = []

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour] = None,
            weapon: List[Weapon] = None,
            potion: List[Potion] = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armor(self) -> int:
        total_protection = sum(
            armor.protection for armor in self.armour
        ) if self.armour else 0
        return total_protection

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion.__dict__.items():
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)

    def attack(self, other: 'Knight') -> None:
        damage = max(self.power - other.apply_armor(), 0)
        other.hp -= damage


# Knight instances
lancelot = Knight(
    "Lancelot",
    35,
    100,
    armour=None,
    weapon=[metal_sword],
    potion=None
)

arthur = Knight(
    "Arthur",
    45,
    75,
    armour=[helmet, breastplate, boots],
    weapon=[two_handed_sword],
    potion=None
)

mordred = Knight(
    "Mordred",
    30,
    90,
    armour=[breastplate, boots],
    weapon=[poisoned_sword],
    potion=berserk
)

red_knight = Knight(
    "Red Knight",
    40,
    70,
    armour=[breastplate],
    weapon=[sword],
    potion=blessing
)
