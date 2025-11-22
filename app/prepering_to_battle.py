from __future__ import annotations


class Knight:
    def __init__(
            self, name: str, power: int, hp: int,
            weapon: dict, armour: dict | None, potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.base_power = power
        self.base_hp = hp

    def preparing_to_battle(self) -> None:
        self.protection = 0
        self.power = self.base_power
        self.hp = self.base_hp

        if self.armour:
            for armor in self.armour:
                self.protection += armor["protection"]
        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def duel(self, other: Knight) -> None:
        new_hp = self.hp - max(0, other.power - self.protection)
        other_new_hp = other.hp - max(0, self.power - other.protection)
        self.hp = max(0, new_hp)
        other.hp = max(0, other_new_hp)


def build_knight(name: str, knights_config: dict) -> Knight:
    warrior = knights_config[name]
    bad_night = Knight(
        warrior["name"],
        warrior["power"],
        warrior["hp"],
        warrior["weapon"],
        warrior["armour"],
        warrior["potion"])
    return bad_night
