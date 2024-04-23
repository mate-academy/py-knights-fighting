from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_armour(self, armour: Armour) -> None:
        self.protection += armour.protection

    def get_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def get_potion(self, potion: Potion) -> None:
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]

    def battle(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        if self.hp <= 0:
            self.hp = 0
