from app.equipments.armours import Armour
from app.equipments.weapons import Weapon
from app.equipments.potions import Potion


class Knight(Armour, Weapon, Potion):
    knights = []

    def __init__(self, name: str, power: int, hp: int,
                 weapon: dict, armour: list, protection: int = 0,
                 potion: dict = None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
        Armour.armours[self.name] = armour
        Weapon.weapons[self.name] = weapon
        Potion.potions[self.name] = potion

    def check_result(self) -> None:
        if self.hp < 0:
            self.hp = 0

    def hit(self, other: None) -> None:
        self.hp -= other.power - self.protection

    def fight(self, other: None) -> None:
        self.hit(other)
        other.hit(self)
        self.check_result()
        other.check_result()

    @staticmethod
    def battle(name_1: str, name_2: str) -> None:
        for knight in Knight.knights:
            if knight.name == name_1:
                knight_1 = knight
            if knight.name == name_2:
                knight_2 = knight
        knight_1.fight(knight_2)
