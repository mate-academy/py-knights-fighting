from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"].get("power")
        self.hp = knight["hp"]
        self.protection = sum(
            armour_part["protection"] for armour_part in knight["armour"]
        )

        if knight["potion"] is not None:
            potion_effects = knight["potion"].get("effect")

            for key, value in potion_effects.items():
                current_value = getattr(self, key)
                setattr(self, key, current_value + value)

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> dict:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        if knight1.hp < 0:
            knight1.hp = 0

        if knight2.hp < 0:
            knight2.hp = 0

        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }
