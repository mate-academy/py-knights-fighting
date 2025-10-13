from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: dict,
                 weapon: int,
                 potion: int) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour_items = [Armour(a["part"], a["protection"])
                             for a in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"], potion["effect"]) \
            if potion else None

        self.hp = self.base_hp
        self.power = self.base_power + self.weapon.power
        self.protection = sum(a.protection
                              for a in self.armour_items)

        if self.potion:
            self.potion.apply_effect(self)

        if self.hp < 0:
            self.hp = 0

    def attack(self, enemy: dict) -> None:
        return max(self.power - enemy.protection, 0)

    def take_damage(self, damage: int) -> None:
        self.hp = max(self.hp - damage, 0)
