from app.items.armor import Armor
from app.items.weapon import Weapon
from app.items.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def set_protection(self, armours: list[Armor]) -> None:
        if armours:
            self.protection += sum(armor.protection for armor in armours)

    def increase_power(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def set_effect(self, potion: Potion) -> None:
        self.hp += potion.effect.get("hp", 0)
        self.power += potion.effect.get("power", 0)
        self.protection += potion.effect.get("protection", 0)
