from __future__ import annotations
from knight_description.armour_part import ArmourPart
from knight_description.potion import Potion
from knight_description.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armour: dict = None,
            potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def create_knight(cls, knight_stats: dict) -> Knight:
        name = knight_stats["name"]
        power = knight_stats["power"]
        hp = knight_stats["hp"]

        armour = None
        if "armour" in knight_stats:
            armour = ArmourPart.get_armor(knight_stats["armour"])

        weapon = Weapon(knight_stats["weapon"]["name"],
                        knight_stats["weapon"]["power"])

        potion = None
        if knight_stats["potion"] is not None:
            potion = Potion(knight_stats["potion"]["name"],
                            knight_stats["potion"]["effect"])

        return cls(name, power, hp, weapon, armour, potion)

    def prepare_for_battle(self) -> None:
        if self.armour is not None:
            self.protection = self.armour["protection"]

        self.power += self.weapon.power

        if self.potion is not None:
            effect: dict = self.potion.effect
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

        if self.hp < 0:
            self.hp = 0

        if self.power < 0:
            self.power = 0

        if self.protection < 0:
            self.protection = 0
