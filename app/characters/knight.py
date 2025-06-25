from __future__ import annotations


class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data.get("name", "Unknown")
        self.power = data.get("power", 0)
        self.hp = data.get("hp", 0)
        self.protection = 0

        self.wear_armour(data.get("armour"))
        self.take_weapon(data.get("weapon"))
        self.use_potion(data.get("potion"))

    def wear_armour(self, armour: list[dict]) -> None:
        if not armour:
            return

        for item in armour:
            self.protection += item.get("protection", 0)

    def take_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power", 0)

    def use_potion(self, potion: dict) -> None:
        if not potion:
            return

        effects = potion.get("effect", {})
        self.hp += effects.get("hp", 0)
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)

    def attack(self, other: Knight) -> None:
        other.hp = max(0, other.hp - (self.power - other.protection))
