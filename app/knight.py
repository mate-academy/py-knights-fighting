from __future__ import annotations

from app.gear.armor_part import ArmorPart
from app.gear.weapon import Weapon
from app.items.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armor: list[ArmorPart],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.base_power = power
        self.power = power
        self.base_hp = hp
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.apply_gear_and_items()

    @classmethod
    def from_dict(cls, knight_dict: dict) -> Knight:
        name = knight_dict["name"]
        power = knight_dict["power"]
        hp = knight_dict["hp"]
        armor = [
            ArmorPart(armor_part["part"], armor_part["protection"])
            for armor_part in knight_dict["armour"]
        ]
        weapon = Weapon(
            knight_dict["weapon"]["name"],
            knight_dict["weapon"]["power"]
        )
        potion = (
            Potion(
                knight_dict["potion"]["name"],
                knight_dict["potion"]["effect"]
            )
            if knight_dict["potion"]
            else None
        )
        return cls(name, power, hp, armor, weapon, potion)

    def apply_gear_and_items(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0
        for armor_part in self.armor:
            self.protection += armor_part.protection
        self.power += self.weapon.power
        if self.potion:
            self.potion.apply(self)

    def attack(self, opponent: Knight) -> None:
        damage = (
            self.power - opponent.protection
            if self.power - opponent.protection > 0
            else 0
        )
        opponent.hp = opponent.hp - damage if opponent.hp - damage > 0 else 0
