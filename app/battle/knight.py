from typing import Dict, List


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: List[Dict[str, int]],
                 weapon: Dict[str, int],
                 potion: Dict[str, Dict[str, int]],
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        self.apply_armour(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def __str__(self) -> str:
        return self.name

    def apply_armour(self, armour: List[Dict[str, int]]) -> None:
        for piece in armour:
            self.protection += piece.get("protection", 0)

    def apply_weapon(self, weapon: Dict[str, int]) -> None:
        self.power += weapon.get("power", 0)

    def apply_potion(self, potion: Dict[str, Dict[str, int]]) -> None:
        if potion:
            for attr in ["hp", "power", "protection"]:
                effect = potion.get("effect", {}).get(attr, 0)
                setattr(self, attr, getattr(self, attr) + effect)

    @staticmethod
    def battle(knight1: "Knight", knight2: "Knight") -> Dict[str, int]:
        knight1_damage = max(0, knight2.power - knight1.protection)
        knight2_damage = max(0, knight1.power - knight2.protection)

        knight1.hp = max(0, knight1.hp - knight1_damage)
        knight2.hp = max(0, knight2.hp - knight2_damage)

        return {knight1.name: knight1.hp, knight2.name: knight2.hp}
