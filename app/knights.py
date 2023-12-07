from __future__ import annotations


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def preparation(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
