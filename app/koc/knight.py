from __future__ import annotations


class Knight:
    def __init__(self
                 , name: str
                 , power: int
                 , hp: int
                 , armour: list = None
                 , weapon: dict = None
                 , potion: dict = None) -> None:
        from app.gear.armour import Armour
        from app.gear.potion import Potion
        from app.gear.weapon import Weapon

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = Armour(armour) if armour else None
        self.weapon = Weapon(**weapon) if weapon else None
        self.potion = Potion(**potion) if potion else None

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_armour(self) -> None:
        if self.armour:
            self.protection += self.armour.protection

    def apply_potion(self) -> None:
        if self.potion:
            self.potion.apply(self)

    def attack(self, other: Knight) -> None:
        other.take_damage(self.power)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage - self.protection
        if self.hp <= 0:
            self.hp = 0
