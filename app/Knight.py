from __future__ import annotations
from app.Knight_data import KNIGHTS


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.armour = knight.get("armour")
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")
        self.protection = knight.get("protection")
        self.battle_preparing()

    def battle_preparing(self) -> None:
        self.protection = self.protection or 0
        for armour in self.armour:
            self.protection += armour["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def __repr__(self) -> str:
        return f"{self.name} = " \
               f"'hp': {self.hp}, " \
               f"'power': {self.power}, " \
               f"'protection': {self.protection}"

    def duel(self, opponent: Knight) -> dict:
        shot1 = self.power - opponent.protection
        shot2 = opponent.power - self.protection
        self.hp -= shot2
        opponent.hp -= shot1
        if self.hp < 0:
            self.hp = 0
        if opponent.hp < 0:
            opponent.hp = 0
        return {
            self.name: self.hp,
            opponent.name: opponent.hp
        }


lancelot = Knight(KNIGHTS["lancelot"])
mordred = Knight(KNIGHTS["mordred"])
