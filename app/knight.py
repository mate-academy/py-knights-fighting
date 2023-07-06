from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = sum(element["protection"] for element in armour)
        self.weapon = weapon
        if potion is not None:
            self.apply_potion_effect(potion)

    def apply_potion_effect(self, potion: dict) -> None:
        effects = potion.get("effect", {})
        for attribute, value in effects.items():
            current_value = getattr(self, attribute, 0)
            setattr(self, attribute, current_value + value)

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        damage_knight1 = max(0, knight2.power - knight1.protection)
        damage_knight2 = max(0, knight1.power - knight2.protection)
        knight1.hp = max(0, knight1.hp - damage_knight1)
        knight2.hp = max(0, knight2.hp - damage_knight2)
