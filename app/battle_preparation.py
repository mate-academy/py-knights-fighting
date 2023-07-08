from __future__ import annotations


class Knight:
    def __init__(self, knights: dict) -> None:
        self.name = knights.get("name")
        self.power = knights.get("power")
        self.hp = knights.get("hp")
        self.armour = knights.get("armour")
        self.weapon = knights.get("weapon")
        self.potion = knights.get("potion")
        self.protection = knights.get("protection")
        self.battle_preparation()

    def battle_preparation(self) -> None:
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
