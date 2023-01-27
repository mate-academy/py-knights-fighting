from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply_armour(self, armour: list) -> int:
        for part in armour:
            self.protection += part["protection"]
        return self.hp

    def apply_weapon(self, weapon_power: int) -> int:
        self.power += weapon_power
        return self.power

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            self.hp += potion["effect"].get("hp", 0)
            self.power += potion["effect"].get("power", 0)
            self.protection += potion["effect"].get("protection", 0)
