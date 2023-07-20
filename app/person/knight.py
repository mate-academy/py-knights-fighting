from app.item.armor import Armor
from app.item.potion import Potion
from app.item.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[Armor],
                 weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_to_battle(self) -> None:
        self.equip_weapon()
        self.equip_armour()
        self.drink_potion()

    def equip_weapon(self) -> None:
        self.power += self.weapon.power

    def equip_armour(self) -> None:
        for armor in self.armour:
            self.protection += armor.protection

    def drink_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.effect.hp
            self.power += self.potion.effect.power
            self.protection += self.potion.effect.protection
