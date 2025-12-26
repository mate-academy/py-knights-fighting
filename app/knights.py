from __future__ import annotations


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def preparation(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            for key in self.potion["effect"]:
                setattr(
                    self, key, getattr(self, key) + self.potion["effect"][key]
                )

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
