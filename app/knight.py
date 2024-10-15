from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.name = knight["name"]
        self.power = (knight["power"]
                      + (knight["weapon"].get("power", 0)
                         if knight["weapon"] else 0)
                      + (knight["potion"]["effect"].get("power", 0)
                         if knight["potion"] else 0))
        self.hp = (knight["hp"]
                   + (knight["potion"]["effect"].get("hp", 0)
                      if knight["potion"] else 0))
        self.protection = ((sum(protec["protection"]
                                for protec in knight["armour"])
                            if knight["armour"] else 0)
                           + (knight["potion"]["effect"].get("protection", 0)
                              if knight["potion"] else 0))

    def __sub__(self, other: Knight) -> Knight:
        knight = Knight(self.knight)
        knight.power = self.power - other.protection
        return knight

    def __isub__(self, other: Knight) -> Knight:
        self.hp -= other.power
        self.hp = max(self.hp, 0)
        return self
