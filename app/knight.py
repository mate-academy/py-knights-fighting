from __future__ import annotations
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: list = None,
                 potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = 0

    @staticmethod
    def from_dict(knight: dict) -> Knight:
        return Knight(knight["name"],
                      knight["power"],
                      knight["hp"],
                      Weapon.from_dict(knight["weapon"]),
                      Armour.from_list(knight["armour"]),
                      Potion.from_dict(knight["potion"]))

    def equip_weapon(self) -> None:
        self.power += self.weapon.power
        self.weapon.power = 0

    def equip_armor(self) -> None:
        if self.armour:
            for item in self.armour:
                self.protection += item.protection

    def use_potion(self) -> None:
        if self.potion:
            if self.potion.effect.get("hp"):
                self.hp += self.potion.effect.get("hp")
            if self.potion.effect.get("power"):
                self.power += self.potion.effect.get("power")
            if self.potion.effect.get("protection"):
                self.protection += self.potion.effect.get("protection")

    def get_ready_to_battle(self) -> Knight:
        self.equip_armor()
        self.equip_weapon()
        self.use_potion()
        return self

    def __str__(self) -> str:
        return f"name={self.name}, " \
               f"power={self.power}, " \
               f"hp={self.hp}, " \
               f"protection={self.protection}, " \
               f"armour={self.armour}, " \
               f"weapon={self.weapon}, " \
               f"potion={self.potion}"

    @staticmethod
    def fight_knight(first: Knight, second: Knight) -> None:
        first.hp -= second.power - first.protection
        second.hp -= first.power - second.protection
        if first.hp < 0:
            first.hp = 0
        if second.hp < 0:
            second.hp = 0
