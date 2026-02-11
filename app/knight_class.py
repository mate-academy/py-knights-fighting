from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list | None,
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.add_armour()
        self.add_weapon()
        self.add_potion()

    def add_armour(self) -> Knight:
        if self.armour:
            for part in self.armour:
                self.protection += part["protection"]
        return self

    def add_weapon(self) -> Knight:
        self.power += self.weapon["power"]
        return self

    def add_potion(self) -> Knight:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

        return self

    def battle(self, other: Knight) -> dict:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0

        return {
            self.name: self.hp,
            other.name: other.hp
        }
