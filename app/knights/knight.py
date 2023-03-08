from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = None

    def apply_armour(self, armour: list[dict[str, int]]) -> None:
        for part in armour:
            if "protection" in part:
                self.protection += part["protection"]

    def apply_weapon(self, weapon: dict[str, int]) -> None:
        if "power" in weapon:
            self.power += weapon["power"]

    def apply_potion(self, potion: dict[str, dict[str, int]]) -> None:
        if potion is not None and "effect" in potion:
            effect = potion["effect"]
            if "hp" in effect:
                if effect["hp"] > 0:
                    self.hp += effect["hp"]
                else:
                    self.hp -= abs(effect["hp"])
            if "power" in effect:
                if effect["power"] > 0:
                    self.power += effect["power"]
                else:
                    self.power -= abs(effect["power"])
            if "protection" in effect:
                if effect["protection"] > 0:
                    self.protection += effect["protection"]
                else:
                    self.protection -= abs(effect["protection"])

    def check_hp(self) -> int:
        if self.hp <= 0:
            self.hp = 0
        return self.hp
