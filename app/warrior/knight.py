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
        self.armour = list(armour)
        self.weapon = dict(weapon)

        if potion is not None:
            self.potion = dict(potion)
        else:
            self.potion = None

    def battle_prepation(self) -> None:

        self.protection = 0

        for element in self.armour:
            self.protection += element["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
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
