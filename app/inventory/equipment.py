from __future__ import annotations

from app.character.knight import Knight


class Equipment:
    def __init__(self, armor: list, weapon: dict, potion: dict = None) -> None:
        self.armour = armor
        self.weapon = weapon
        self.potion = potion

    def knight_buff(self, knight: Knight) -> None:
        if self.armour:
            for arm in self.armour:
                knight.protection += arm["protection"]

        if self.weapon:
            knight.power += self.weapon["power"]

        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                knight.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                knight.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                knight.protection += self.potion["effect"]["protection"]
