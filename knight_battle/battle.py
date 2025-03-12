from knight_battle.knight.knight import Knight
from typing import Dict

def battle_logic(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    knight1.attack(knight2)
    knight2.attack(knight1)

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
