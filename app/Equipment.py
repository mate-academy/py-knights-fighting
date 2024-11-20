from typing import Any


class Armour:
    def __init__(self, armor_data: list) -> None:
        self.armor_data = armor_data

    def __str__(self) -> str:
        return str(self.armor_data)

    def sum_protection(self) -> int:
        protection = 0
        for item in self.armor_data:
            protection += item.get("protection", 0)
        return protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f"{self.name}, {self.power}"


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __str__(self) -> str:
        return f"{self.name}, {self.effect}"

    def apply_effect(self,
                     power: int = 0,
                     hp: int = 0,
                     protection: int = 0) -> Any:
        return {
            "power": power + self.effect.get("power", 0),
            "hp": hp + self.effect.get("hp", 0),
            "protection": protection + self.effect.get("protection", 0),
        }

    @staticmethod
    def empty() -> "Potion":
        return Potion(name="None", effect={})
