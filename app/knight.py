from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, armour: list,
                 weapon: dict, potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.hp = hp
        self.protection = 0

    def apply_armour(self) -> None:
        if len(self.armour) != 0:
            for arm in self.armour:
                self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def battle_knights(self, other: Knight) -> dict:
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
