from app.preparations_for_batle.create_knights import Knight
from app.start_battle.act_battle import BattleKnights


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # Create a list of instances of the Knight class
    all_knights = []
    for knight in knights_config.values():
        all_knights.append(
            Knight(
                knight["name"],
                knight["power"],
                knight["hp"],
                knight["armour"],
                knight["weapon"],
                knight["potion"]
            )
        )
    # Apply armour, weapon, poison
    for prepare_knight in all_knights:
        prepare_knight.apply_weapon()
        prepare_knight.apply_armour()
        prepare_knight.apply_potion()
    lancelot = all_knights[0]
    arthur = all_knights[1]
    mordred = all_knights[2]
    red_knight = all_knights[3]
    # BATTLE:
    # 1 Lancelot vs Mordred:
    BattleKnights.battle(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    BattleKnights.battle(arthur, red_knight)
    # Return battle results:
    return BattleKnights.battle_result(all_knights)
