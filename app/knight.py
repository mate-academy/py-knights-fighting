from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def preparation(self) -> None:
        self.name = self.knight["name"]
        self.power = (self.knight["power"]
                      + (self.knight["weapon"].get("power", 0)
                         if self.knight["weapon"] else 0)
                      + (self.knight["potion"]["effect"].get("power", 0)
                         if self.knight["potion"] else 0))
        self.hp = (self.knight["hp"]
                   + (self.knight["potion"]["effect"].get("hp", 0)
                      if self.knight["potion"] else 0))
        self.protection = ((sum(protec["protection"]
                                for protec in self.knight["armour"])
                            if self.knight["armour"] else 0)
                           + (self.knight["potion"]["effect"].get("protection"
                                                                  , 0)
                              if self.knight["potion"] else 0))

    def reduce_power(self, other: Knight) -> Knight:
        knight = Knight(self.knight)
        knight.power = self.power - other.protection
        return knight

    def fight(self, other: Knight) -> Knight:
        self.hp -= other.power
        self.hp = max(self.hp, 0)
        return self
