from __future__ import annotations


class Knight:

    knights = []

    def __init__(self, knight: dict) -> None:

        knight["protection"] = 0
        for person in knight["armour"]:
            knight["protection"] += person["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"]\
                    += knight["potion"]["effect"]["protection"]
            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]

        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"]
        self.protection = knight["protection"]
        self.__class__.knights.append(self)
