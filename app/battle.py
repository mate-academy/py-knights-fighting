from typing import Dict
from app.knight import Knight, create_knight


def battle_calculate(knight1: Knight, knight2: Knight) -> Dict[str, int]:

    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}


def battle(knight: [str, Dict]) -> Dict[str, int]:
    lancelot = create_knight(knight["lancelot"])
    arthur = create_knight(knight["arthur"])
    mordred = create_knight(knight["mordred"])
    red_knight = create_knight(knight["red_knight"])

    lancelot.apply_armour()
    lancelot.apply_weapon()
    lancelot.apply_potion()

    mordred.apply_armour()
    mordred.apply_weapon()
    mordred.apply_potion()

    arthur.apply_armour()
    arthur.apply_weapon()
    arthur.apply_potion()

    red_knight.apply_armour()
    red_knight.apply_weapon()
    red_knight.apply_potion()

    result_battle_lancelot_and_mordred = battle_calculate(lancelot, mordred)
    result_battle_arthur_and_red_knight = battle_calculate(arthur, red_knight)

    return {**result_battle_lancelot_and_mordred,
            **result_battle_arthur_and_red_knight}
