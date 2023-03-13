from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list[dict[str, int]],
                 weapon: dict[str, int],
                 potion: dict[str, dict[str, int]]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.apply_armour(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def apply_armour(self,
                     armour: list[dict[str, int]]) -> list[dict[str, int]]:
        for part in armour:
            if "protection" in part:
                self.protection += part["protection"]
        return armour

    def apply_weapon(self, weapon: dict[str, int]) -> dict[str, int]:
        if "power" in weapon:
            self.power += weapon["power"]
        return weapon

    def apply_potion(self, potion: dict[str, dict[str, int]]) -> None:
        if potion is not None and "effect" in potion:
            effect = potion["effect"]
            for attribute, value in effect.items():
                if hasattr(self, attribute):
                    current_value = getattr(self, attribute)
                    setattr(self, attribute, current_value + value)

    def check_hp(self) -> int:
        if self.hp <= 0:
            self.hp = 0
        return self.hp
