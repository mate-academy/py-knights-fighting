from __future__ import annotations
from app.equipment.military import Armour, Weapon, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list = 0,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection: int = 0
        Knight.equip(self)

    def apply_armour(self, armour: list[Armour]) -> None:
        for unit in armour:
            self.protection += unit.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        if potion:
            for effect_name, value in potion.effect.items():
                self.__dict__[effect_name] += value

    def equip(self) -> None:
        self.apply_armour([Armour(armour.get("part"),
                                  armour.get("protection"))
                           for armour in self.armour])
        self.apply_weapon(Weapon(self.weapon.get("name"),
                                 self.weapon.get("power")))
        if self.potion:
            self.apply_potion(Potion(self.potion.get("name"),
                                     self.potion.get("effect")))

    def strike(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
