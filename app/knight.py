from __future__ import annotations

from app.equipment.armour import Armour
from app.equipment.effect import Effect
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.armour = [Armour(armour) for armour in knight["armour"]]
        self.weapon = Weapon(knight["weapon"])
        self.potion = (
            Potion(knight["potion"])
            if knight.get("potion")
            else None
        )

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        self.apply_effect(self.potion.effect)

    def apply_effect(self, effect: Effect) -> None:
        self.power += effect.power
        self.protection += effect.protection
        self.hp += effect.hp

    def equip(self) -> None:
        # apply armour
        self.apply_armour()
        # apply weapon
        self.apply_weapon()
        # apply potion if exist
        self.apply_potion()

    def check_hp(self) -> None:
        # check if someone fell in battle
        if self.hp < 0:
            self.hp = 0

    def fight(self, other_knight: Knight) -> None:
        self.hp -= other_knight.power - self.protection
        self.check_hp()

    @staticmethod
    def battle(knight1: Knight, knight2: Knight) -> None:
        knight1.fight(knight2)
        knight2.fight(knight1)
