from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def armour(self, armour: list) -> int:
        for part in armour:
            self.hp += part["protection"]
        return self.hp

    def weapon(self, weapon_power: int) -> int:
        self.power += weapon_power
        return self.power

    def potion(self, potion: dict) -> callable:
        if potion is not None:
            if potion["effect"].get("protection"):
                self.hp += potion["effect"]["protection"]
            if potion["effect"]["hp"] is not None:
                self.hp += potion["effect"]["hp"]
            if potion["effect"]["power"] is not None:
                self.power += potion["effect"]["power"]
        return self.hp, self.power
