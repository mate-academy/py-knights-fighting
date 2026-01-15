from __future__ import annotations

from app.warriors.armour import Armour
from app.warriors.potion import Potion
from app.warriors.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = None

    def take_armour(self, armour: Armour) -> None:
        self.armour.append(armour)
        self.protection += armour.protection

    def take_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def take_potion(self, potion: Potion) -> None:
        self.potion = potion
        for key, value in potion.effect.items():
            field_value = getattr(self, key)
            setattr(self, key, field_value + value)

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection
        self.hp = 0 if self.hp < 0 else self.hp
        knight.hp = 0 if knight.hp < 0 else knight.hp
