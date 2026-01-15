from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]
        self.protection = sum(
            [armour["protection"] for armour in knight["armour"]]
        )

        if knight["potion"]:
            effect = knight["potion"]["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    @staticmethod
    def battle(knight1: Knight, knight2: Knight) -> None:
        knight1.hp = max(0, knight1.hp + knight1.protection - knight2.power)
        knight2.hp = max(0, knight2.hp + knight2.protection - knight1.power)
