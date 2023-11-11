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
        potion_hp_bonus = sum(
            [potion.hp for potion in Potion.potions.values()
             if potion.owner == knight.name]
        )

        potion_power_bonus = sum(
            [potion.power for potion in Potion.potions.values()
             if potion.owner == knight.name]
        )

        potion_protection_bonus = sum(
            [potion.protection for potion in Potion.potions.values()
             if "protection" in potion.__dict__
             and potion.owner == knight.name]
        )

        knight.hp += potion_hp_bonus
        knight.power += potion_power_bonus
        knight.protection += potion_protection_bonus

    @staticmethod
    def apply_armour(knight: Knights) -> None:
        armour_protection_bonus = sum(
            [armour.protection for armour in Armour.list_of_armour
             if armour.owner == knight.name]
        )

        knight.protection += armour_protection_bonus

    @staticmethod
    def apply_weapon(knight: Knights) -> None:
        weapon_power_bonus = sum(
            [weapon.power for weapon in Weapon.weapons.values()
             if weapon.owner == knight.name]
        )

        knight.power += weapon_power_bonus

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
