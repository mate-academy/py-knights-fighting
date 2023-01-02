from __future__ import annotations
from app.knight import Knight


class Potion:
    def __init__(
            self,
            name: str,
            hp: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def check_effect(self, effects: dict) -> None:
        for effect in effects:
            if effect == "hp":
                self.hp = effects["hp"]
            elif effect == "power":
                self.power = effects["power"]
            elif effect == "protection":
                self.protection = effects["protection"]

    def apply_potion(self, knight: Knight) -> None:
        knight.hp += self.hp
        knight.power += self.power
        knight.protection += self.protection
