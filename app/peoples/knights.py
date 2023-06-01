from __future__ import annotations
from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potions import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.stats = {
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection
        }

    @classmethod
    def from_dict(cls, knight_dict: dict) -> Knight:
        if knight_dict["potion"]:
            return cls(
                knight_dict["name"],
                knight_dict["power"],
                knight_dict["hp"],
                Armour.from_list_to_list(knight_dict["armour"]),
                Weapon.from_dict(knight_dict["weapon"]),
                Potion.from_dict(knight_dict["potion"])
            )
        return cls(
            knight_dict["name"],
            knight_dict["power"],
            knight_dict["hp"],
            Armour.from_list_to_list(knight_dict["armour"]),
            Weapon.from_dict(knight_dict["weapon"]),
            None
        )

    def wear_armour(self) -> None:
        for item in self.armour:
            self.protection += item.protection

    def take_weapon(self) -> None:
        self.power += self.weapon.power

    def drink_potion(self) -> None:
        if self.potion:
            self.hp += self.potion.change_hp
            self.power += self.potion.change_power
            self.protection += self.potion.change_protection

    def prepare_to_battle(self) -> None:
        self.wear_armour()
        self.take_weapon()
        self.drink_potion()

    def show_stats(self) -> None:
        self.prepare_to_battle()
        print(self.stats)
