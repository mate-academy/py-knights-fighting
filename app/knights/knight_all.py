from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:

        self.name = knight["name"]

        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

        # apply armour
        self.protection = 0
        for armour in knight["armour"]:
            self.protection += armour["protection"]

        # apply weapon
        self.power = knight["power"] + knight["weapon"]["power"]

        self.hp = knight["hp"]

        # apply potion if exist
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]

    def battle(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection

        if self.hp <= 0:
            self.hp = 0

        if knight.hp <= 0:
            knight.hp = 0
