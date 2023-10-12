from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"] + knight["weapon"].get("power", 0)
        self.protection = sum(arm["protection"] for arm in knight["armour"])
        if knight["potion"] is not None:
            self.check_potion(knight["potion"])

    def check_potion(self, potion: dict) -> None:
        if "power" in potion["effect"]:
            self.power += potion["effect"]["power"]

        if "protection" in potion["effect"]:
            self.protection += potion["effect"]["protection"]

        if "hp" in potion["effect"]:
            self.hp += potion["effect"]["hp"]

    def battle_with_enemy(self: Knight, other: Knight) -> None:
        self.hp = max(0, self.hp - (other.power - self.protection))
        other.hp = max(0, other.hp - (self.power - other.protection))
