from __future__ import annotations


class Knight:
    def __init__(self, params: dict) -> None:
        self.name = params["name"]
        self.power = params["power"]
        self.hp = params["hp"]
        self.armour = params["armour"]
        self.weapon = params["weapon"]
        self.potion = params["potion"]
        self.protection = 0

    def apply_armor(self) -> None:
        self.protection = sum(armor["protection"] for armor in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]

        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]

    def damage(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp < 0:
            self.hp = 0
        elif other.hp < 0:
            other.hp = 0
