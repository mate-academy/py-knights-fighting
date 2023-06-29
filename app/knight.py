from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: dict,
                 armour: list,
                 potion: dict) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.weapon = weapon
        self.protection = sum(element["protection"] for element in armour)
        if potion is not None:
            self.apply_potion_effects(potion)

    def apply_potion_effects(self, potion: dict) -> None:
        effects = potion.get("effect", {})
        self.power += effects.get("power", 0)
        self.hp += effects.get("hp", 0)
        self.protection += effects.get("protection", 0)

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        if knight1.protection < knight2.power:
            damage = knight2.power - knight1.protection
            knight1.hp = max(0, knight1.hp - damage)
        if knight2.protection < knight1.power:
            damage = knight1.power - knight2.protection
            knight2.hp = max(0, knight2.hp - damage)
