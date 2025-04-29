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
        for effect in potion.effect:
            if effect == "hp":
                knight.hp += potion.effect[effect]
            elif effect == "power":
                knight.power += potion.effect[effect]
            elif effect == "protection":
                knight.knight_protection += potion.effect[effect]

    def preparations(self, knight: Knight) -> None:
        for armour in knight.armours:
            if isinstance(armour, Armour):
                self.apply_armour(knight, armour)

        if isinstance(knight.weapon, Weapon):
            self.apply_weapon(knight, knight.weapon)

        if isinstance(knight.potion, Potion):
            self.apply_potion(knight, knight.potion)
