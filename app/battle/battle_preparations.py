from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    @staticmethod
    def apply_weapon(knight_weapon: dict) -> dict:
        knight_weapon["power"] += knight_weapon["weapon"]["power"]
        return knight_weapon

    @staticmethod
    def apply_armour(knight_armor: dict) -> dict:
        knight_armor["protection"] = 0
        for index_armor in knight_armor["armour"]:
            knight_armor["protection"] += index_armor["protection"]
        return knight_armor

    @staticmethod
    def apply_potion(knight_potion: dict) -> dict:
        if knight_potion["potion"] is not None:
            if "power" in knight_potion["potion"]["effect"]:
                knight_potion["power"] += \
                    knight_potion["potion"]["effect"]["power"]

            if "protection" in knight_potion["potion"]["effect"]:
                knight_potion["protection"] += \
                    knight_potion["potion"]["effect"]["protection"]

            if "hp" in knight_potion["potion"]["effect"]:
                knight_potion["hp"] += \
                    knight_potion["potion"]["effect"]["hp"]

        return knight_potion

    def get_ready(self) -> None:
        self.knight = self.apply_weapon(self.knight)
        self.knight = self.apply_armour(self.knight)
        self.knight = self.apply_potion(self.knight)

    def battle_start(self, knight: Knight) -> None:
        self.knight["hp"] -= \
            knight.knight["power"] - self.knight["protection"]
        knight.knight["hp"] -= \
            self.knight["power"] - knight.knight["protection"]

        # check if someone fell in battle
        if self.knight["hp"] <= 0:
            self.knight["hp"] = 0

        if knight.knight["hp"] <= 0:
            knight.knight["hp"] = 0
