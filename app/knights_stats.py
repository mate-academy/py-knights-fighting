from __future__ import annotations


class TheKnight:
    def __init__(self,
                 name: str,
                 hp: int, power: int,
                 protection: int
) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def stats(self, stats: dict) -> list:
        list_of_knights = []
        for knight in stats:
            self.name = knight["name"]
            self.hp = knight["hp"]
            self.power = knight["power"]
            self.protection = knight["armour"]["protection"]
            if knight["potion"] is not None:
                self.hp += knight["potion"]["effect"]["hp"]
                self.power += knight["potion"]["effect"]["power"]
            list_of_knights.append({"name": self.name,
                                    "hp": self.hp,
                                    "power": self.power,
                                    "protection": self.protection})
        return list_of_knights
