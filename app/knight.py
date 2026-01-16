from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight_property = knight
        self.name = knight["name"]
        self.power = 0
        self.hp = 0
        self.protection = 0

    def is_item(self, key: str) -> bool:
        if self.knight_property[key] is not None:
            return True
        return False

    def set_power(self) -> int:
        return (self.knight_property["power"]
                + (self.knight_property["weapon"].get("power", 0)
                   if self.is_item("weapon") else 0)
                + (self.knight_property["potion"]["effect"].get("power", 0)
                   if self.is_item("potion") else 0))

    def set_hp(self) -> int:
        return (self.knight_property["hp"]
                + (self.knight_property["potion"]["effect"].get("hp", 0)
                   if self.is_item("potion") else 0))

    def set_protection(self) -> int:
        return ((sum(protec["protection"]
                     for protec in self.knight_property["armour"])
                 if self.is_item("armour") else 0)
                + (self.knight_property["potion"]["effect"].get("protection",
                                                                0)
                   if self.is_item("potion") else 0))

    def preparation(self) -> None:
        self.power = self.set_power()
        self.hp = self.set_hp()
        self.protection = self.set_protection()

    def reduce_power(self, other: Knight) -> Knight:
        knight = Knight(self.knight_property)
        knight.power = self.power - other.protection
        return knight

    def fight(self, other: Knight) -> Knight:
        self.hp -= other.power
        self.hp = max(self.hp, 0)
        return self
