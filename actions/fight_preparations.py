from __future__ import annotations
from characters.knight import Knight
from items.potion import Potion
from items.armour import Armour
from items.weapon import Weapon


class FightPreparation:

    @staticmethod
    def apply_potion(knight: Knight) -> None:
        knight.hp += Potion.potions[knight.name].hp
        knight.power += Potion.potions[knight.name].power
        knight.protection += Potion.potions[knight.name].protection

    @staticmethod
    def apply_armour(knight: Knight) -> None:
        knight.protection += Armour.armours[knight.name].protection

    @staticmethod
    def apply_weapon(knight: Knight) -> None:
        knight.power += Weapon.weapons[knight.name].power

    @classmethod
    def apply_all(
            cls,
            knight: Knight,
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
