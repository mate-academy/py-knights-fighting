from __future__ import annotations


class Knight:
    def __init__(self, info: dict[list | str | int]) -> None:
        self.name = info["name"]
        self.power = info["power"] + info["weapon"]["power"]
        self.hp = info["hp"]
        protection = 0
        if info["armour"]:
            for armor in info.get("armour"):
                protection += armor["protection"]
        self.protection = protection
        if info.get("potion"):
            self.hp += info["potion"]["effect"].get("hp", 0)
            self.power += info["potion"]["effect"].get("power", 0)
            self.protection += info["potion"]["effect"].get("protection", 0)

    def __sub__(self, other: Knight) -> None:
        self.hp = self.hp - (other.power - self.protection)
        if self.hp <= 0:
            self.hp = 0
