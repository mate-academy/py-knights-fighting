from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def armour_defence(self, armour: list) -> int:
        for part in armour:
            self.hp += part["protection"]
        return self.hp

    def use_of_weapons(self, weapon_power: int) -> int:
        self.power += weapon_power
        return self.power

    def apply_potion(self, potion: dict) -> None:
        if potion is not None:
            if potion["effect"].get("protection"):
                self.hp += potion["effect"]["protection"]
            if potion["effect"].get("power"):
                self.power += potion["effect"]["power"]
            if potion["effect"].get("hp"):
                self.hp += potion["effect"]["hp"]
        return self.hp, self.power
