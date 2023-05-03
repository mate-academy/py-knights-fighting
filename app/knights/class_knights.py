from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
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

    # apply armour
    def apply_armour(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    # apply weapon
    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    # apply potion if exist
    def apply_potion(self) -> None:
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                if effect == "power":
                    self.power += value
                if effect == "protection":
                    self.protection += value
                if effect == "hp":
                    self.hp += value

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
