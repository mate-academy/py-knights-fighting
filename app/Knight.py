from __future__ import annotations


class Knight:

    knights = []

    def __init__(self, knight: dict) -> None:

        knight["protection"] = 0
        for person in knight["armour"]:
            knight["protection"] += person["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:

            status = knight["potion"]["effect"]
            change_knight = ["power", "protection", "hp"]
            for param in change_knight:
                if param in status:
                    knight[param] += status[param]

        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"]
        self.protection = knight["protection"]
        self.__class__.knights.append(self)
