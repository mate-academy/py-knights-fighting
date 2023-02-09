from app.characters.items.equipment import Weapon, Armour
from app.characters.items.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 protection: int = 0
                 ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def add_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def add_potion(self, potion: Potion) -> None:
        if potion.check_for_effect("hp"):
            self.hp += potion.effect["hp"]
        if potion.check_for_effect("power"):
            self.power += potion.effect["power"]
        if potion.check_for_effect("protection"):
            self.protection += potion.effect["protection"]

    def add_armour(self, armour: Armour) -> None:
        self.protection += armour.protection
