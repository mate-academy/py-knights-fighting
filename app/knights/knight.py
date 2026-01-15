from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list[dict[str, int]],
                 weapon: dict[str, int],
                 potion: dict[str, dict[str, int]]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.apply_armour(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def apply_armour(self,
                     armour: list[dict[str, int]]) -> list[dict[str, int]]:
        self.protection += sum(part.get("protection", 0) for part in armour)
        return armour

    def apply_weapon(self, weapon: dict[str, int]) -> dict[str, int]:
        self.power += weapon.get("power", 0)
        return weapon

    def apply_potion(self, potion: dict[str, dict[str, int]]) -> None:
        if potion is not None and "effect" in potion:
            effect = potion["effect"]
            for attribute, value in effect.items():
                if hasattr(self, attribute):
                    current_value = getattr(self, attribute)
                    setattr(self, attribute, current_value + value)

    def check_hp(self) -> int:
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    @staticmethod
    def attack(attacker_knight: Knight, defender_knight: Knight) -> None:
        damage_to_defender = attacker_knight.power - defender_knight.protection
        damage_to_attacker = defender_knight.power - attacker_knight.protection

        defender_knight.hp -= damage_to_defender
        attacker_knight.hp -= damage_to_attacker
