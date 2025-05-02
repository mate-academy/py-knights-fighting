from __future__ import annotations


class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def calculate_protection(self, armour: dict) -> None:
        for protection_points in armour:
            self.protection += protection_points["protection"]

    def calculate_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            for attribute in ["hp", "power", "protection"]:
                if attribute in potion["effect"]:
                    setattr(
                        self,
                        attribute,
                        getattr(self, attribute) + potion["effect"][attribute]
                    )

    @staticmethod
    def prepare_knight(config: dict) -> Knight:
        knight = Knight(config["name"], config["hp"], config["power"])
        knight.calculate_protection(config["armour"])
        knight.calculate_power(config["weapon"])
        knight.apply_potion(config["potion"])

        return knight
