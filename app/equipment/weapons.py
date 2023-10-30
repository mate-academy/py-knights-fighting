from __future__ import annotations
from app.knights import Knight


class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon["name"]
        self.power = weapon["power"]

    def equip_weapon(self, knight: Knight) -> None:
        knight.power += self.power
        print(f"{knight.name} equipped {self.name} "
              f"and now his power {knight.power}")
