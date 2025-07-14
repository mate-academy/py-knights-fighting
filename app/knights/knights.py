from __future__ import annotations
from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    knights = []

    def __init__(
            self, name: str,
            power: int,
            hp: int,
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = None
        self.weapon = None
        self.potion = None
        self.protection = 0
        Knight.knights.append(self)

    def apply_armour(self, armour: list[dict] | None) -> None:
        new_armour = []

        if armour is not None:
            for i in range(len(armour)):
                new_armour.append(Armour(
                    armour[i]["part"],
                    armour[i]["protection"]
                ))

            self.armour = new_armour
            for i in range(len(self.armour)):
                self.protection += self.armour[i].protection

    def apply_weapon(self, weapon: dict) -> None:
        new_weapon = Weapon(weapon["name"], weapon["power"])
        self.weapon = new_weapon
        self.power += self.weapon.power

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            effects = potion["effect"]
            new_potion = Potion(
                potion["name"],
                effects.get("power", 0),
                effects.get("hp", 0),
                effects.get("protection", 0)
            )

            self.potion = new_potion
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection

    @classmethod
    def battle(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= max(knight2.power - knight1.protection, 0)
        knight2.hp -= max(knight1.power - knight2.protection, 0)

        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0
