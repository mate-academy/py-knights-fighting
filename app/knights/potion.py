from __future__ import annotations


# Class for storing and processing all potions
class Potion:
    def __init__(self, name: str, power: int = 0,
                 hp: int = 0, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def set_property(self, prop: str, value: int) -> None:
        match prop:
            case "power": self.power = value
            case "hp": self.hp = value
            case "protection": self.protection = value

    def get_power(self) -> int:
        return self.power

    def get_hp(self) -> int:
        return self.hp

    def get_protection(self) -> int:
        return self.protection

    @staticmethod
    def create_potion(info: dict | None) -> Potion | None:
        new_potion = None
        if info is not None:
            new_potion = Potion(info["name"])
            for prop, value in info["effect"].items():
                new_potion.set_property(prop, value)
        return new_potion
