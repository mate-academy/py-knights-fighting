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
        self.wear_armour()
        self.take_weapon()
        self.drink_potion()

    @classmethod
    def from_dict(cls, knight_dict: dict) -> Knight:
        return cls(
            knight_dict["name"],
            knight_dict["power"],
            knight_dict["hp"],
            Armour.from_list_to_list(knight_dict["armour"]),
            Weapon.from_dict(knight_dict["weapon"]),
            Potion.from_dict(knight_dict["potion"])
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

    def after_fight(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        knight_1.after_fight()
        knight_2.after_fight()
