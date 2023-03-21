from __future__ import annotations
from app.util.armour import get_armor
from app.util.weapon import get_weapon


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = get_weapon(knight)
        self.protection = get_armor(knight)
        self.get_potion(knight)

    def get_potion(self, knight: dict) -> None:
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]
