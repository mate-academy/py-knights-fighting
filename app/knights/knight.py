from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon


class Knight:

    def __init__(
            self, name: str, power: str, hp: int,
            armour: list, weapon: dict, potion: dict
    ):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Armour(armour)
        self.weapon = Weapon(weapon)
        self.potion = Potion(potion)

    @classmethod
    def knight_list(cls, knights: dict):
        return [
            cls(
                knight["name"], knight["power"], knight["hp"],
                knight["armour"], knight["weapon"], knight["potion"]
            ) for knight in knights.values()
        ]

    def full_hp(self):
        return self.hp + self.potion.effect["hp"]

    def full_power(self):
        return self.power + self.weapon.power + self.potion.effect["power"]

    def full_protection(self):
        armour = sum([armour["protection"] for armour in self.armour.items])
        return armour + self.potion.effect["protection"]
