from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_weapon(self) -> dict:
        self.knight["power"] += self.knight["weapon"]["power"]
        return self.knight

    def apply_armour(self) -> dict:
        self.knight["protection"] = 0
        for index_armor in self.knight["armour"]:
            self.knight["protection"] += index_armor["protection"]
        return self.knight

    def apply_potion(self) -> dict:
        if self.knight["potion"] is not None:
            mass_values = ["power", "protection", "hp"]
            for value in mass_values:
                if value in self.knight["potion"]["effect"]:
                    self.knight[value] += \
                        self.knight["potion"]["effect"][value]

        return self.knight

    def get_ready(self) -> None:
        self.apply_weapon()
        self.apply_armour()
        self.apply_potion()

    def battle_start(self, knight: Knight) -> None:
        self.knight["hp"] -= \
            knight.knight["power"] - self.knight["protection"]
        knight.knight["hp"] -= \
            self.knight["power"] - knight.knight["protection"]

        if self.knight["hp"] <= 0:
            self.knight["hp"] = 0

        if knight.knight["hp"] <= 0:
            knight.knight["hp"] = 0
