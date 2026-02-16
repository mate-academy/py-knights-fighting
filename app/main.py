from app.data.knights import (
    lancelot,
    arthur,
    mordred,
    red_knight)
from app.domain.knight import Knight


def duel(knight_1: Knight, knight_2: Knight) -> dict[str, int]:

    combatant_1 = knight_1.apply_equipment()
    combatant_2 = knight_2.apply_equipment()

    dmg_to_c1 = max(0, combatant_2.power - combatant_1.protection)
    dmg_to_c2 = max(0, combatant_1.power - combatant_2.protection)

    combatant_1.hp = max(0, combatant_1.hp - dmg_to_c1)
    combatant_2.hp = max(0, combatant_2.hp - dmg_to_c2)

    return {
        combatant_1.name: combatant_1.hp,
        combatant_2.name: combatant_2.hp
    }


def battle2(*args: tuple[Knight, Knight]) -> list:
    result = []
    for fight in args:
        result.append(duel(fight[0], fight[1]))
    return result


print(battle2(
      (lancelot, mordred),
      (arthur, red_knight)
      ))

def battle(*args:)