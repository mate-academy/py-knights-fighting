from __future__ import annotations

from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            **kwargs
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def set_armours(armours: list) -> list[Armour] | None:
        if not armours:
            return None
        return [
            Armour(armour["part"], armour["protection"])
            for armour in armours
        ]

    @staticmethod
    def set_weapon(weapon: dict) -> Weapon | None:
        if not weapon:
            return None
        return Weapon(weapon["name"], weapon["power"])

    @staticmethod
    def set_potion(potion: dict) -> Potion | None:
        if not potion:
            return None
        return Potion(potion["name"], potion["effect"])

    def use_potion(self) -> None:
        if not self.potion:
            return
        for key, value in self.potion.effect.items():
            if key == "power":
                self.power += value
            elif key == "hp":
                self.hp += value
            elif key == "protection":
                self.protection += value

    def __str__(self) -> str:
        return (
            f"Knight: {self.name} "
            f"Power: {self.power} "
            f"HP: {self.hp} "
            f"Armour: {self.armour} "
            f"Weapon: {self.weapon.__dict__} "
            f"Potion: {self.potion} "
            f"Protection: {self.protection}"
        )
