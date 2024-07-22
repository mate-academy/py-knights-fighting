from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def calculate_armour(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

    def calculate_weapon(self) -> None:
        self.power += self.weapon["power"]

    def calculate_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        if self.hp < 0:
            self.hp = 0
