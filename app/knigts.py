from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list[dict]) -> None:
        if armour is not []:
            for i in armour:
                self.protection += i.get("protection")

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power")

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            effect = potion.get("effect")
            for key, value in effect.items():
                setattr(self, key, getattr(self, key) + value)

    @classmethod
    def battle(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0

        # if potion is not None:
        #     effect = potion.get("effect")
        #     if effect is not None:
        #         if "power" in effect:
        #             self.power += effect.get("power")
        #         if "protection" in effect:
        #             self.protection += effect.get("protection")
        #         if "hp" in effect:
        #             self.hp += effect.get("hp")
        # old version
