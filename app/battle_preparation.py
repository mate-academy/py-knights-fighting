from __future__ import annotations


class KnightPreparation:

    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 armour: list,
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for ar in self.armour:
            self.protection += ar["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for prop in self.potion["effect"]:
                value = getattr(self, prop) + self.potion["effect"][prop]
                setattr(self, prop, value)

    def prepare_knight(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
