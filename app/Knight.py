from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict | None],
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = 0
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]

        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
