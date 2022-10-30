from __future__ import annotations

from app.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.weapon = knight["weapon"]
        self.armour = knight["armour"]
        self.potion = knight["potion"]
        self.protection = 0

    def equip(self) -> None:

        weapon = Weapon(self.weapon)
        weapon.take(self)

        if self.armour:
            armour = Armour(self.armour)
            armour.put_on(self)

        if self.potion:
            potion = Potion(self.potion)
            potion.drink(self)

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection

        if self.hp < 0:
            self.hp = 0

        if knight.hp < 0:
            knight.hp = 0
