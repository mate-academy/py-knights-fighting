from __future__ import annotations


class Knights:
    def __init__(self, info: dict) -> None:
        self.info = info
        self.name = info["name"]
        self.hp = self.info["hp"]
        self.power = self.info["power"] + self.info["weapon"]["power"]
        self.protection = 0
        self.hp_total()
        self.power_total()
        self.protection_total()

    def hp_total(self) -> int:
        if self.info["potion"] is not None:
            if "hp" in self.info["potion"]["effect"]:
                self.hp += self.info["potion"]["effect"]["hp"]
        return self.hp

    def power_total(self) -> int:
        if self.info["potion"] is not None:
            if "power" in self.info["potion"]["effect"]:
                self.power += self.info["potion"]["effect"]["power"]
        return self.power

    def protection_total(self) -> int:
        if self.info["potion"] is not None:
            if "protection" in self.info["potion"]["effect"]:
                self.protection += self.info["potion"]["effect"]["protection"]

        if len(self.info["armour"]) > 0:
            for armour in self.info["armour"]:
                self.protection += armour["protection"]
        return self.protection

    def holding_a_battle(self, other: Knights) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
