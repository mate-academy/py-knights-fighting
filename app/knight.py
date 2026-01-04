from app.armour.armour import Armour
from app.potion.potion import Potion
from app.weapon.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: dict,
                 weapon: dict, potion: dict = None) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = [Armour(a["part"], a["protection"]) for a in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"], potion["effect"]) \
            if potion else None

        self.total_protection = sum(a.protection for a in self.armour)
        self.total_power = self.base_power + self.weapon.power

        if self.potion:
            if "power" in self.potion.effect:
                self.total_power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.total_protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def attack(self, opponent: "Knight") -> None:
        damage = max(0, self.total_power - opponent.total_protection)
        opponent.hp = max(0, opponent.hp - damage)
