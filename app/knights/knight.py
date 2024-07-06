from __future__ import annotations


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: str = None,
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __str__(self) -> str:
        return self.name

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            attributes = ["power", "protection", "hp"]
            for attr in attributes:
                if attr in effect:
                    setattr(self, attr, getattr(self, attr) + effect[attr])

    def fight(self, other: Knight) -> None:
        self.hp -= max(other.power - self.protection, 0)
        other.hp -= max(self.power - other.protection, 0)

        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0

    def prepare_for_fight(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
