from typing import Dict, Tuple


class BattleService:
    @staticmethod
    def calculate_damage(attacker_power: int, defender_protection: int) -> int:
        damage = attacker_power - defender_protection
        return max(0, damage)

    @staticmethod
    def fight(
        knight1: Dict[str, int],
        knight2: Dict[str, int]
    ) -> Tuple[Dict[str, int], Dict[str, int]]:
        damage_to_knight2 = BattleService.calculate_damage(
            knight1["power"],
            knight2["protection"]
        )
        damage_to_knight1 = BattleService.calculate_damage(
            knight2["power"],
            knight1["protection"]
        )

        knight1_hp = max(0, knight1["hp"] - damage_to_knight1)
        knight2_hp = max(0, knight2["hp"] - damage_to_knight2)

        return (
            {"name": knight1["name"], "hp": knight1_hp},
            {"name": knight2["name"], "hp": knight2_hp},
        )
