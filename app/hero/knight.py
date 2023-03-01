from app.hero.armour import Armour
from app.hero.weapon import Weapon
from app.hero.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Armour(armour)
        self.weapon = Weapon(weapon)
        self.potion = Potion(potion)

    @classmethod
    def load_list(cls, knights: dict) -> list:
        result = []

        for knight in knights.values():
            result.append(cls(knight["name"], knight["power"], knight["hp"],
                              knight["armour"], knight["weapon"],
                              knight["potion"]))

        return result

    def full_hp(self):
        return self.hp + self.potion.effect["hp"]

    def full_power(self):
        return self.power + self.weapon.power + self.potion.effect["power"]

    def full_protection(self):
        armour = sum([armour["protection"] for armour in self.armour.items])
        return armour + self.potion.effect["protection"]
