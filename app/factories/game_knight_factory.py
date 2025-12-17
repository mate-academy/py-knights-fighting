from app.models.knight import Armour, Knight, Potion, Weapon
from typing import List, Optional


class GameKnightFactory:
    name: str
    hp: int
    power: int
    protection: int

    def __init__(self, knight: Knight) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.protection = self._calculate_protection(knight["armour"])
        self.power = self._calculate_power(knight["power"], knight["weapon"])

        if knight["potion"] is not None:
            self._apply_potion(knight["potion"])

    def __getitem__(self, key: str) -> str | int:
        if key == "name":
            return self.name
        elif key == "hp":
            return self.hp
        elif key == "power":
            return self.power
        elif key == "protection":
            return self.protection

    def __setitem__(self, key: "hp", value: int) -> None:
        self.hp = value

    def _calculate_protection(self, armour: List[Optional[Armour]]) -> int:
        return sum(item.get("protection", 0) if item else 0 for item in armour)

    def _calculate_power(self, power: int, weapon: Weapon) -> int:
        return power + weapon["power"]

    def _apply_potion(self, potion: Potion) -> None:
        effect = potion.get("effect", {})

        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def battle_with(self, another_knight: "GameKnightFactory") -> None:
        damage_to_self = max(0, another_knight.power - self.protection)
        damage_to_another = max(0, self.power - another_knight.protection)

        self.hp = max(0, self.hp - damage_to_self)
        another_knight.hp = max(0, another_knight.hp - damage_to_another)
