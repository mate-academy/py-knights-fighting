from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict] | None,
            weapon: dict,
            potion: dict | None

    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def is_died(self) -> bool:
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def upgrade_stats(self) -> None:
        if self.armour is not None:
            for part in self.armour:
                self.protection += part["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    @classmethod
    def create_knight(cls, knights: dict, identifier: str) -> Knight:
        return cls(
            name=knights[identifier]["name"],
            power=knights[identifier]["power"],
            hp=knights[identifier]["hp"],
            armour=knights[identifier]["armour"],
            weapon=knights[identifier]["weapon"],
            potion=knights[identifier]["potion"]
        )
