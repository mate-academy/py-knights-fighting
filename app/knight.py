from __future__ import annotations


class Knight:
    def __init__(self,
                 knight: dict) -> None:
        self.name = knight["name"]

        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        self.init_ammunition(knight)

    def init_armour(self,
                    parts: list) -> None:
        for part in parts:
            self.protection += part["protection"]

    def init_weapon(self,
                    weapon: dict) -> None:
        self.power += weapon["power"]

    def init_potion(self,
                    potion: dict | None) -> None:
        if potion:
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]

            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

    def init_ammunition(self,
                        knight: dict) -> None:
        self.init_armour(knight["armour"])
        self.init_weapon(knight["weapon"])
        self.init_potion(knight["potion"])

    def fight(self,
              knight: Knight) -> None:
        self.hp -= knight.power - self.protection

        if self.hp <= 0:
            self.hp = 0
