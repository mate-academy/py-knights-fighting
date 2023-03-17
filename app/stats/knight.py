from typing import List
from app.stats.armour import Armour
from app.stats.weapon import Weapon
from app.stats.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[dict],
            weapon: dict,
            potion: dict,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour: List[Armour] = [
            Armour(
                part=armor_.get("part"),
                protection=armor_.get("protection"),
            ) for armor_ in armour
        ]
        self.weapon: Weapon = Weapon(
            weapon.get("name"),
            weapon.get("power")
        ) if weapon else None
        self.potion: Potion = Potion(
            potion.get("name"),
            potion.get("effect")
        ) if potion else None
        self.protection = 0

    def apply_armour(self) -> None:
        if self.armour:
            self.protection += sum([
                armor_.protection for armor_ in self.armour
            ])

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            effect: dict = self.potion.effect
            if effect.get("hp"):
                self.hp += effect.get("hp")
            if effect.get("power"):
                self.power += effect.get("power")
            if effect.get("protection"):
                self.protection += effect.get("protection")
