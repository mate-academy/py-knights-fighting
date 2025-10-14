from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from app.knights.knight import Knight


def duel(knight1: "Knight", knight2: "Knight") -> Dict[str, int]:
    dmg_to_2 = knight1.attack(knight2)
    dmg_to_1 = knight2.attack(knight1)

    knight2.take_damage(dmg_to_2)
    knight1.take_damage(dmg_to_1)

    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
