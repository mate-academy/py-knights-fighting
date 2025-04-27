from knights.knight import Knight
from knights.armour import Armour
from knights.weapon import Weapon
from knights.potion import Potion


class Preparations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def apply_armour(knight: Knight, armour: Armour) -> None:
        knight.knight_protection += armour.protection

    @staticmethod
    def apply_weapon(knight: Knight, weapon: Weapon) -> None:
        knight.power += weapon.power

    @staticmethod
    def apply_potion(knight: Knight, potion: Potion) -> None:
        for effect in potion.effects:
            if effect == "hp":
                knight.hp += effect
            elif effect == "power":
                knight.power += effect
            elif effect == "protection":
                knight.knight_protection += effect

    def preparations(self, knight: Knight, weapons: list, armours: list, potions: list):
        for weapon in weapons:
            if isinstance(weapon, Weapon):
                self.apply_weapon(knight, weapon)

        for armour in armours:
            if isinstance(armour, Armour):
                self.apply_armour(knight, armour)

        for potion in potions:
            if isinstance(potion, Potion):
                self.apply_potion(knight, potion)
