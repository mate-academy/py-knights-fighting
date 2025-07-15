from __future__ import annotations
from app.knights.knight_stuff.armour import Armour
from app.knights.knight_stuff.potion import Potion
from app.knights.knight_stuff.weapon import Weapon


class Knight:
    knights = []

    def __init__(self, name: str, power: int, hp: int, weapon: Weapon,
                 armour: list[Armour] = None, potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour if armour is not None else []
        self.potion = potion
        self.protection = 0
        Knight.knights.append(self)

    def __repr__(self) -> str:
        return (f"Knight(name={self.name}, power={self.power}, hp={self.hp}, "
                f"weapon={self.weapon}, armour={self.armour}, "
                f"potion={self.potion})")

    def add_armour_protection(self) -> int:
        return sum([arm.protection for arm in self.armour])

    def add_weapon_power(self) -> None:
        self.power += self.weapon.power

    def prepare(self) -> None:
        self.protection = self.add_armour_protection()
        self.add_weapon_power()
        if self.potion:
            eff = self.potion.effect
            self.power += eff.get("power", 0)
            self.protection += eff.get("protection", 0)
            self.hp += eff.get("hp", 0)

    def attack(self, enemy: Knight) -> None:
        damage = max(0, self.power - enemy.protection)
        enemy.hp = max(0, enemy.hp - damage)
