from typing import Dict, Any

from app.legendary_knights import KNIGHTS
from app.structuring_the_knight_personality import Knight
from app.preparing_for_the_great_battle import BeforeBattle
from app.great_battle import BattleOfTwoKnight

# ______________________WELCOME TO THE TOURNAMENT__________________________


def battle(knights: Dict[str, Any] = KNIGHTS) -> Dict[str, int]:

    lancelot = Knight(**knights["lancelot"])
    arthur = Knight(**knights["arthur"])
    mordred = Knight(**knights["mordred"])
    red_knight = Knight(**knights["red_knight"])
    # list of registered knights for the duel
    list_knight = [lancelot, arthur, mordred, red_knight]

    for knight in list_knight:
        BeforeBattle.apply_armour(knight)
        BeforeBattle.apply_weapon(knight)
        BeforeBattle.apply_potion(knight)

    BattleOfTwoKnight.battle_action_phase(lancelot, mordred)
    BattleOfTwoKnight.battle_action_phase(arthur, red_knight)

    for knight in list_knight:
        BattleOfTwoKnight.result_after_battle(knight)

    return {
        knight.name: knight.hp
        for knight in list_knight
    }


print(battle())
