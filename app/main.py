from typing import Dict

from app.characters.knight import Knight
from app.data.knights_data import knights
from app.actions import actions


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    battle_members = {knight["name"]: Knight(knight)
                      for knight in knights_config.values()}

    pairs = [[battle_members["Lancelot"], battle_members["Mordred"]],
             [battle_members["Artur"], battle_members["Red Knight"]]]

    for pair in pairs:
        pair[0].prepare_for_battle()
        pair[1].prepare_for_battle()
        actions.duel(pair)
        actions.check_hp(pair[0])
        actions.check_hp(pair[1])

    return {knight.name: knight.hp for knight in battle_members.values()}


print(battle(knights))
