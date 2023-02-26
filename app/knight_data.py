from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def added(self) -> None:
        self.power += self.weapon["power"]
        for gun in self.armour:
            self.protection += gun["protection"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def duel(self, rival: Knight) -> None:
        self.hp -= rival.power - self.protection
        rival.hp -= self.power - rival.protection
        if self.hp <= 0:
            self.hp = 0
        if rival.hp <= 0:
            rival.hp = 0
