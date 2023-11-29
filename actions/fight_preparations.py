from __future__ import annotations
from characters.knights import Knights
from items.potion import Potion
from items.armour import Armour
from items.weapon import Weapon


class FightPreparations:

    def __init__(self) -> None:
        pass

    @staticmethod
    def apply_potion(knight: Knights) -> None:
        for potion in Potion.potions.values():
            if potion.owner == knight.name:
                knight.hp += potion.hp
                knight.power += potion.power
                knight.protection += potion.protection

    @staticmethod
    def apply_armour(knight: Knights) -> None:
        for armour in Armour.armour.values():
            if armour.owner == knight.name:
                knight.protection += armour.protection

    @staticmethod
    def apply_weapon(knight: Knights) -> None:
        for weapon in Weapon.weapons.values():
            if weapon.owner == knight.name:
                knight.power += weapon.power

    @classmethod
    def apply_all(
            cls,
            knight: Knights,
            weapon: bool = True,
            armour: bool = True,
            potion: bool = True
    ) -> None:
        if weapon:
            cls.apply_weapon(knight)
        if armour:
            cls.apply_armour(knight)
        if potion:
            cls.apply_potion(knight)
