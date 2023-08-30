from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            protection: int,
            health_point: int,
            armour: list | dict,
            weapon: list | dict,
            potion: list | dict
    ) -> None:
        self.name = name
        self.power = power
        self.protection = protection
        self.health_point = health_point
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def calculate_stats(self) -> Knight:
        stats = [self.weapon, self.armour, self.potion]

        for source in stats:
            if isinstance(source, list):
                for piece in source:
                    self.protection += piece.get("protection", 0)
                    self.power += piece.get("power", 0)
                    self.health_point += piece.get("hp", 0)
                    self.apply_effect(piece.get("effect", {}))
            if isinstance(source, dict):
                self.protection += source.get("protection", 0)
                self.power += source.get("power", 0)
                self.health_point += source.get("hp", 0)
                self.apply_effect(source.get("effect", {}))
        return self

    def apply_effect(self, effects: dict) -> None:
        self.protection += effects.get("protection", 0)
        self.power += effects.get("power", 0)
        self.health_point += effects.get("hp", 0)

    def versus_step(self, other: Knight) -> None:
        if self.power - other.protection >= 0:
            other.health_point -= self.power - other.protection
        if other.power - self.protection >= 0:
            self.health_point -= other.power - self.protection
        if self.health_point <= 0:
            self.health_point = 0
        if other.health_point <= 0:
            other.health_point = 0
