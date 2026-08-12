from typing import Dict, Tuple


def knight_attacks(attacker: Dict, target: Dict) -> None:
    target["hp"] -= attacker["power"] - target["protection"]


def fell_check(knight: Dict) -> None:
    if knight["hp"] <= 0:
        knight["hp"] = 0


def vs_battle(knight1: Dict, knight2: Dict) -> Tuple[Dict, Dict]:
    # 1 Lancelot vs Mordred:
    knight_attacks(knight1, knight2)
    knight_attacks(knight2, knight1)

    fell_check(knight1)
    fell_check(knight2)

    return knight1, knight2


def battle_result(*knights: Dict) -> Dict:
    return {knight["name"]: knight["hp"] for knight in knights}
