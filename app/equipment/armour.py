from __future__ import annotations
from app.knights import Knight


class Armour:
    def __init__(self, set_piece: dict) -> None:
        self.name = set_piece["part"]
        self.protection = set_piece["protection"]

    def equip_armour(self, knight: Knight) -> None:
        knight.protection += self.protection
        print(f"{knight.name} equipped {self.name} "
              f"and now his defence {knight.protection}.")
