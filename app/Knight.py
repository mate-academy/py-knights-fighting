from __future__ import annotations


class Knight:

    knights = []

    def __init__(self, knight: dict) -> None:

        knight["protection"] = 0
        for person in knight["armour"]:
            knight["protection"] += person["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            stats = knight["potion"]["effect"]
            if "power" in stats:
                knight["power"] += stats["power"]
            if "protection" in stats:
                knight["protection"]\
                    += stats["protection"]
            if "hp" in stats:
                knight["hp"] += stats["hp"]

        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"]
        self.protection = knight["protection"]
        self.__class__.knights.append(self)
