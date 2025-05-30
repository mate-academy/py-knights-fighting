from __future__ import annotations
from knights import KNIGHTS


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list | None,
            potion: dict | None,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = protection
        self.add_armour()
        self.add_potion()
        self.add_weapon()

    def add_armour(self) -> Knight:
        if self.armour:
            for part in self.armour:
                self.protection += part["protection"]
        return self

    def add_potion(self) -> Knight:
        if self.potion:
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
        return self

    def add_weapon(self) -> Knight:
        self.power += self.weapon["power"]
        return self

    def battle(self, other: Knight) -> dict:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0

        return {self.name: self.hp,
                other.name: other.hp
                }


knights_list = []
for knight in KNIGHTS.values():
    knights_list.append(
        Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            knight["weapon"],
            knight["armour"],
            knight["potion"]
        )
    )
print(knights_list[0].battle(knights_list[1]))
