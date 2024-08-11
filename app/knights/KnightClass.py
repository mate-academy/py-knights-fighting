from __future__ import annotations


class Knight:
    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.hp = stats["hp"]
        self.power = stats["power"] + stats["weapon"]["power"]
        self.protection = sum(shield["protection"]
                              for shield in stats["armour"])

        if stats["potion"] is not None:
            self.power += stats["potion"]["effect"].get("power", 0)
            self.protection += stats["potion"]["effect"].get("protection", 0)
            self.hp += stats["potion"]["effect"].get("hp", 0)

    def battle(self, other: Knight) -> None:
        self.hp = max(0, self.hp - (other.power - self.protection))
        other.hp = max(0, other.hp - (self.power - other.protection))
