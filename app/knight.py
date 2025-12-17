from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def knight_statistic(
            name: str,
            hp: int,
            power: int,
            armours: list,
            weapon: dict,
            potion: dict | None = None
    ) -> Knight:
        knight_stats = {"power": power, "hp": hp, "protection": 0}
        knight_stats["power"] += weapon["power"]
        if armours:
            for armour in armours:
                knight_stats["protection"] += armour["protection"]
        if potion:
            potion_effects = ["power", "hp", "protection"]
            for effect in potion_effects:
                if effect in potion["effect"]:
                    knight_stats[effect] += potion["effect"][effect]
        return Knight(
            name,
            knight_stats["power"],
            knight_stats["hp"],
            knight_stats["protection"]
        )

    @staticmethod
    def new_knight(dictionary: dict) -> Knight:
        knight = Knight.knight_statistic(
            dictionary["name"],
            dictionary["hp"],
            dictionary["power"],
            dictionary["armour"],
            dictionary["weapon"],
            dictionary["potion"])
        return knight

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

    def check_hp(self) -> int:
        if self.hp < 0:
            self.hp = 0
        return self.hp

    @staticmethod
    def results(knights: list[Knight]) -> dict[str, int]:
        return {
            knight.name: knight.check_hp()
            for knight in knights
        }
