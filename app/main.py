from app.preparations_for_batle.create_knights import Knight
from app.start_battle.act_battle import BattleKnights


def battle(knights_config: dict) -> dict:
    all_knights = [Knight(**knight) for knight in knights_config.values()]
    for prepare_knight in all_knights:
        prepare_knight.apply_weapon()
        prepare_knight.apply_armour()
        prepare_knight.apply_potion()
    lancelot = all_knights[0]
    arthur = all_knights[1]
    mordred = all_knights[2]
    red_knight = all_knights[3]
    BattleKnights.battle(lancelot, mordred)
    BattleKnights.battle(arthur, red_knight)
    return BattleKnights.battle_result(all_knights)
