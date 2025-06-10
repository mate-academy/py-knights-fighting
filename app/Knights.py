from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.protection = 0
        self.hp = knight["hp"]
        for armour in knight["armour"]:
            self.protection += armour["protection"]
        self.power = knight["weapon"]["power"] + knight["power"]
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]

    def battle(self, other: Knight) -> None:
        self.hp -= max(0, other.power - self.protection)
        if self.hp <= 0:
            self.hp = 0
