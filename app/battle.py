
from typing import List, Union

from app.knight import Knight


def perform_battle(knights: List[Knight]) -> Union[str, None]:
    lancelot = knights[0]
    mordred = knights[2]

    lancelot_protection = lancelot.apply_armour()
    lancelot_power = lancelot.apply_weapon()
    mordred_power = mordred.apply_weapon()

    while lancelot.hp > 0 and mordred.hp > 0:
        lancelot.hp -= mordred_power - lancelot_protection
        mordred.hp -= lancelot_power - mordred.apply_armour()

    if lancelot.hp <= 0 and mordred.hp <= 0:
        return "Draw"
    elif lancelot.hp <= 0:
        return "Mordred wins"
    else:
        return "Lancelot wins"
